#!/usr/bin/env python3
"""Collect every public comment (and attachment) on two CMS dockets via the
regulations.gov v4 API.

CMS-2449-P and CMS-2452-P are CMS rule file codes; on regulations.gov they
live in dockets CMS-2026-1916 and CMS-2026-2476 (see DOCKETS below).

Phases (each idempotent, so the script can be killed and re-run at any time):
  1. enumerate  - walk /comments in lastModifiedDate slices (bisecting any
                  slice that reports >= 5,000 results) into data/<docket>/_index.json
  2. details    - GET /comments/{id}?include=attachments -> data/<docket>/<id>.json
  3. attachments- download every attachment file to data/<docket>/attachments/
  4. report     - counts vs. the total the API reports, plus any gaps

The API key is read from the REGULATIONS_API_KEY environment variable and is
never written to disk.
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

API = "https://api.regulations.gov/v4"
# file code -> regulations.gov docket id
DOCKETS = {"CMS-2449-P": "CMS-2026-1916", "CMS-2452-P": "CMS-2026-2476"}
PAGE_SIZE = 250          # API maximum
RESULT_CAP = 5000        # 20 pages x 250
DATE_FMT = "%Y-%m-%d %H:%M:%S"   # filter dates are interpreted as US Eastern
SLICE_START = datetime(2025, 12, 1)
DATA = Path("data")
BROWSER_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"


def log(msg):
    print(f"{datetime.now():%H:%M:%S} {msg}", flush=True)


def write_json(path, obj):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, indent=2, ensure_ascii=False))
    os.replace(tmp, path)


def read_json(path, default):
    return json.loads(path.read_text()) if path.exists() else default


class HttpError(Exception):
    def __init__(self, status, url):
        super().__init__(f"HTTP {status} for {url}")
        self.status = status


class Client:
    def __init__(self, key):
        self.s = requests.Session()
        self.s.headers["X-Api-Key"] = key
        self.remaining = None

    def get_json(self, url, params=None, max_tries=8):
        tries = 0
        while True:
            if self.remaining is not None and self.remaining <= 2:
                log("rate limit nearly exhausted; sleeping 60s")
                time.sleep(60)
                self.remaining = None
            try:
                r = self.s.get(url, params=params, timeout=60)
            except requests.RequestException as e:
                tries += 1
                if tries >= max_tries:
                    raise
                wait = min(2 ** tries, 60)
                log(f"network error ({type(e).__name__}); retry in {wait}s")
                time.sleep(wait)
                continue
            rem = r.headers.get("x-ratelimit-remaining")
            self.remaining = int(rem) if rem and rem.isdigit() else self.remaining
            if r.status_code == 429:
                wait = int(r.headers.get("Retry-After", 0) or 0) or 120
                log(f"429 rate limited; sleeping {wait}s")
                time.sleep(wait)
                self.remaining = None
                continue  # 429s don't count against max_tries
            if r.status_code >= 500:
                tries += 1
                if tries >= max_tries:
                    raise HttpError(r.status_code, url)
                wait = min(2 ** tries, 60)
                log(f"HTTP {r.status_code}; retry in {wait}s")
                time.sleep(wait)
                continue
            if r.status_code != 200:
                raise HttpError(r.status_code, url)
            return r.json()


# ---------------------------------------------------------------- phase 1
def list_page(c, docket, start, end, page):
    params = {
        "filter[docketId]": docket,
        "filter[lastModifiedDate][ge]": start.strftime(DATE_FMT),
        "filter[lastModifiedDate][le]": end.strftime(DATE_FMT),
        "sort": "lastModifiedDate,documentId",
        "page[size]": PAGE_SIZE,
        "page[number]": page,
    }
    return c.get_json(f"{API}/comments", params)


def docket_total(c, docket):
    j = c.get_json(f"{API}/comments", {"filter[docketId]": docket, "page[size]": 5})
    return j["meta"]["totalElements"]


def enumerate_docket(c, docket, d):
    state_path, index_path = d / "_state.json", d / "_index.json"
    state = read_json(state_path, {"done": [], "split": [], "oversize": []})
    index = read_json(index_path, {})
    done, split = set(state["done"]), set(state["split"])
    now = datetime.now(ZoneInfo("America/New_York")).replace(tzinfo=None)
    stack = [(SLICE_START, now + timedelta(days=1))]

    def save():
        state.update(done=sorted(done), split=sorted(split))
        write_json(state_path, state)
        write_json(index_path, index)

    while stack:
        s, e = stack.pop()
        key = f"{s.strftime(DATE_FMT)}|{e.strftime(DATE_FMT)}"
        if key in done:
            continue
        if key in split:
            first = None
        else:
            first = list_page(c, docket, s, e, 1)
            total = first["meta"]["totalElements"]
            if total == 0:
                done.add(key)
                continue
            if total >= RESULT_CAP and e > s:
                split.add(key)
                save()
                log(f"{docket} slice {key} has {total} results; bisecting")
        if key in split:
            mid = s + (e - s) / 2
            mid = mid.replace(microsecond=0)
            stack.append((mid + timedelta(seconds=1), e))
            stack.append((s, mid))
            continue
        if total >= RESULT_CAP:  # single-second slice still over the cap
            state["oversize"].append(key)
        page, data = 1, first
        while True:
            for item in data["data"]:
                index[item["id"]] = item["attributes"]
            if not data["meta"].get("hasNextPage") or page >= RESULT_CAP // PAGE_SIZE:
                break
            page += 1
            data = list_page(c, docket, s, e, page)
        done.add(key)
        save()
        log(f"{docket} slice {key}: {total} results (index now {len(index)})")
    save()
    return index


# ---------------------------------------------------------------- phase 2
def att_filename(comment_id, url, fmt):
    """<comment id>_attachment_N.<ext>, taken from the download URL."""
    base = url.rsplit("/", 1)[-1] if url else f"attachment.{fmt}"
    return f"{comment_id}_{base}"


def build_record(file_code, docket, j, list_attrs):
    a = j["data"]["attributes"]
    name = " ".join(p for p in (a.get("firstName"), a.get("lastName")) if p) or None
    atts = []
    for inc in j.get("included", []):
        if inc.get("type") != "attachments":
            continue
        ia = inc["attributes"]
        for ff in ia.get("fileFormats") or []:
            atts.append({
                "attachment_id": inc["id"],
                "title": ia.get("title"),
                "format": ff.get("format"),
                "size": ff.get("size"),
                "url": ff.get("fileUrl"),
                "local_path": None,
            })
    return {
        "id": j["data"]["id"],
        "docket": docket,
        "docket_file_code": file_code,
        "commenter_name": name,
        "organization": a.get("organization"),
        "posted_date": a.get("postedDate"),
        "last_modified_date": a.get("lastModifiedDate") or list_attrs.get("lastModifiedDate"),
        "title": a.get("title"),
        "withdrawn": a.get("withdrawn"),
        "comment": a.get("comment"),
        "attachments": atts,
    }


def fetch_details(c, file_code, docket, d, index):
    for i in index:  # backfill records saved before last_modified_date was merged in
        p = d / f"{i}.json"
        if p.exists():
            rec = json.loads(p.read_text())
            if not rec.get("last_modified_date") and index[i].get("lastModifiedDate"):
                rec["last_modified_date"] = index[i]["lastModifiedDate"]
                write_json(p, rec)
    todo = [i for i in sorted(index) if not (d / f"{i}.json").exists()]
    log(f"{docket}: {len(todo)} comment details to fetch ({len(index) - len(todo)} cached)")
    failures = {}
    for n, cid in enumerate(todo, 1):
        try:
            j = c.get_json(f"{API}/comments/{cid}", {"include": "attachments"})
        except HttpError as e:
            failures[cid] = str(e)
            log(f"  {cid}: {e}")
            continue
        write_json(d / f"{cid}.json", build_record(file_code, docket, j, index[cid]))
        if n % 25 == 0:
            log(f"  {docket}: {n}/{len(todo)} details")
    return failures


# ---------------------------------------------------------------- phase 3
def download(session, url, dest, max_tries=5):
    for attempt in range(1, max_tries + 1):
        try:
            with session.get(url, stream=True, timeout=120) as r:
                if r.status_code in (429, 500, 502, 503, 504):
                    raise requests.RequestException(f"HTTP {r.status_code}")
                if r.status_code != 200:
                    return f"HTTP {r.status_code}"
                tmp = dest.with_suffix(dest.suffix + ".part")
                with open(tmp, "wb") as f:
                    for chunk in r.iter_content(1 << 16):
                        f.write(chunk)
                os.replace(tmp, dest)
                return None
        except requests.RequestException as e:
            if attempt == max_tries:
                return str(e)
            wait = min(2 ** attempt, 60)
            log(f"  download retry in {wait}s ({e})")
            time.sleep(wait)


def fetch_attachments(d):
    adir = d / "attachments"
    adir.mkdir(exist_ok=True)
    session = requests.Session()
    # downloads.regulations.gov (CloudFront) 403s the default python-requests UA
    session.headers["User-Agent"] = BROWSER_UA
    failures = {}
    for path in sorted(d.glob("*.json")):
        if path.name.startswith("_"):
            continue
        rec = json.loads(path.read_text())
        changed = False
        for att in rec["attachments"]:
            if not att["url"]:
                continue
            dest = adir / att_filename(rec["id"], att["url"], att["format"])
            if not dest.exists():
                err = download(session, att["url"], dest)
                if err:
                    failures[dest.name] = err
                    log(f"  {att['url']}: {err}")
                    continue
            rel = str(dest)
            if att["local_path"] != rel:
                att["local_path"] = rel
                changed = True
        if changed:
            write_json(path, rec)
    return failures


# ---------------------------------------------------------------- phase 4
def report(c, file_code, docket, d, det_fail, att_fail):
    index = read_json(d / "_index.json", {})
    saved = [p for p in d.glob("*.json") if not p.name.startswith("_")]
    api_total = docket_total(c, docket)
    missing = sorted(set(index) - {p.stem for p in saved})
    expected_atts = missing_atts = 0
    for p in saved:
        rec = json.loads(p.read_text())
        for att in rec["attachments"]:
            if att["url"]:
                expected_atts += 1
                if not (d / "attachments" / att_filename(rec["id"], att["url"], att["format"])).exists():
                    missing_atts += 1
    oversize = read_json(d / "_state.json", {}).get("oversize", [])
    print(f"\n=== {file_code} ({docket}) ===")
    print(f"API-reported total : {api_total}")
    print(f"IDs enumerated     : {len(index)}")
    print(f"Comment JSONs saved: {len(saved)}")
    print(f"Attachment files   : {expected_atts - missing_atts}/{expected_atts}")
    gaps = []
    if len(index) != api_total:
        gaps.append(f"enumerated {len(index)} != API total {api_total}")
    gaps += [f"no detail JSON: {m}  ({det_fail.get(m, 'not fetched')})" for m in missing]
    gaps += [f"attachment failed: {k}  ({v})" for k, v in att_fail.items()]
    gaps += [f"slice still over cap: {k}" for k in oversize]
    print("Gaps:" if gaps else "Gaps: none")
    for g in gaps:
        print(f"  - {g}")
    return not gaps


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--only", choices=list(DOCKETS), help="restrict to one file code")
    ap.add_argument("--skip-attachments", action="store_true")
    ap.add_argument("--report-only", action="store_true")
    args = ap.parse_args()

    key = os.environ.get("REGULATIONS_API_KEY")
    if not key:
        sys.exit("Set REGULATIONS_API_KEY in the environment.")
    c = Client(key)
    ok = True
    for file_code, docket in DOCKETS.items():
        if args.only and args.only != file_code:
            continue
        d = DATA / docket
        (d / "attachments").mkdir(parents=True, exist_ok=True)
        det_fail = att_fail = {}
        if not args.report_only:
            index = enumerate_docket(c, docket, d)
            det_fail = fetch_details(c, file_code, docket, d, index)
            if not args.skip_attachments:
                att_fail = fetch_attachments(d)
        ok &= report(c, file_code, docket, d, det_fail, att_fail)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
