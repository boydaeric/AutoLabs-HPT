#!/usr/bin/env python3
"""Build an in-network file inventory from Transparency in Coverage TOCs.

Steps:
  1. HEAD every TOC URL in toc_urls.csv (size, content-type, encoding).
  2. Stream-parse each TOC with ijson (yajl2_c backend) -- never loaded
     whole into memory. If a TOC does not match the TiC table-of-contents
     schema, print its top-level keys and first 2 KB, then stop.
  3. Deduplicate in_network_files by URL -> network_inventory.csv
     (payer, description, url, #plans, example plans, market types).
  4. HEAD every distinct in-network URL (falls back to a 1-byte Range GET)
     and add size_bytes / last_modified.

With --scan-directory, every other TOC listed on the Harvard Pilgrim
plan-list page (employer-group TOCs) is also parsed, so the inventory
shows how widely each network file is shared and whether employer TOCs
point anywhere the primary TOCs do not.

No in-network rate file is downloaded; the only body bytes fetched from
them are 1-byte Range probes when HEAD fails.

Usage:  .venv/bin/python toc_inventory.py [--scan-directory] [--out DIR]
"""
import argparse
import csv
import gzip
import io
import re
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import ijson
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

if ijson.backend != "yajl2_c":
    sys.exit(f"ijson backend is {ijson.backend!r}; yajl2_c is required for speed")

HERE = __file__.rsplit("/", 1)[0] if "/" in __file__ else "."
DIRECTORY_PAGES = {
    "Harvard Pilgrim Health Care": (
        "https://eusprdtransparencymrfp32.z13.web.core.windows.net/hphc",
        "https://eusprdtransparencymrfp32.blob.core.windows.net/hphc/",
    ),
}
PEEK_BYTES = 2048


def make_session():
    s = requests.Session()
    retry = Retry(total=4, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504],
                  allowed_methods=["HEAD", "GET"])
    s.mount("https://", HTTPAdapter(max_retries=retry, pool_maxsize=16))
    s.headers["User-Agent"] = "autolabs-tic-inventory/1.0"
    return s


SESSION = make_session()


# --------------------------------------------------------------------- HEAD
def head_info(url):
    """Return dict with status, size_bytes, content_type, content_encoding,
    last_modified, method, error. Falls back to a 1-byte Range GET."""
    out = {"status": "", "size_bytes": "", "content_type": "", "content_encoding": "",
           "last_modified": "", "method": "", "error": ""}
    try:
        r = SESSION.head(url, allow_redirects=True, timeout=60)
        out.update(status=r.status_code, method="HEAD",
                   content_type=r.headers.get("Content-Type", ""),
                   content_encoding=r.headers.get("Content-Encoding", ""),
                   last_modified=r.headers.get("Last-Modified", ""))
        if r.ok and r.headers.get("Content-Length"):
            out["size_bytes"] = int(r.headers["Content-Length"])
            return out
    except requests.RequestException as e:
        out["error"] = f"HEAD: {type(e).__name__}: {e}"[:300]
    try:
        r = SESSION.get(url, headers={"Range": "bytes=0-0"}, stream=True,
                        allow_redirects=True, timeout=60)
        cr = r.headers.get("Content-Range", "")
        m = re.search(r"/(\d+)$", cr)
        out.update(status=r.status_code, method="RANGE",
                   content_type=r.headers.get("Content-Type", "") or out["content_type"],
                   content_encoding=r.headers.get("Content-Encoding", "") or out["content_encoding"],
                   last_modified=r.headers.get("Last-Modified", "") or out["last_modified"])
        if m:
            out["size_bytes"] = int(m.group(1))
        elif r.status_code == 200 and r.headers.get("Content-Length"):
            out["size_bytes"] = int(r.headers["Content-Length"])
        r.close()
    except requests.RequestException as e:
        out["error"] = (out["error"] + " | " if out["error"] else "") + \
            f"RANGE: {type(e).__name__}: {e}"[:300]
    return out


# ------------------------------------------------------------ stream parse
class Capture(io.RawIOBase):
    """Pass-through reader that remembers the first PEEK_BYTES bytes."""

    def __init__(self, f):
        self.f, self.head = f, bytearray()

    def readable(self):
        return True

    def readinto(self, b):
        data = self.f.read(len(b))
        n = len(data)
        b[:n] = data
        if len(self.head) < PEEK_BYTES:
            self.head += data[:PEEK_BYTES - len(self.head)]
        return n


class SchemaError(Exception):
    pass


def open_stream(url):
    r = SESSION.get(url, stream=True, timeout=(30, 300))
    r.raise_for_status()
    r.raw.decode_content = True              # undo Content-Encoding: gzip
    r.raw.auto_close = False                 # small files: EOF must not close before io reads it
    buf = io.BufferedReader(r.raw, buffer_size=1 << 20)
    if buf.peek(2)[:2] == b"\x1f\x8b":      # .json.gz served as octet-stream
        buf = io.BufferedReader(gzip.GzipFile(fileobj=buf), buffer_size=1 << 20)
    cap = Capture(buf)
    return r, cap, io.BufferedReader(cap, buffer_size=1 << 20)


def iter_toc(url, meta):
    """Yield reporting_structure items one at a time. Fills meta with
    reporting_entity_name/type and top_keys. Raises SchemaError."""
    r, cap, f = open_stream(url)
    meta["top_keys"], meta["_cap"] = [], cap
    builder, n_items = None, 0
    try:
        for prefix, event, value in ijson.parse(f):
            if prefix == "" and event == "map_key":
                meta["top_keys"].append(value)
            elif prefix in ("reporting_entity_name", "reporting_entity_type") and event == "string":
                meta[prefix] = value
            elif prefix == "" and event not in ("start_map", "end_map", "map_key"):
                raise SchemaError(f"top level is {event}, not an object")
            if prefix == "reporting_structure.item" and event == "start_map":
                builder = ijson.ObjectBuilder()
            if builder is not None:
                builder.event(event, value)
                if prefix == "reporting_structure.item" and event == "end_map":
                    item, builder = builder.value, None
                    if not isinstance(item.get("reporting_plans"), list):
                        raise SchemaError("reporting_structure item lacks reporting_plans[]")
                    n_items += 1
                    yield item
    finally:
        r.close()
    if "reporting_structure" not in meta["top_keys"] or n_items == 0:
        raise SchemaError("no reporting_structure[] items found")
    if "reporting_entity_name" not in meta["top_keys"]:
        raise SchemaError("reporting_entity_name missing")


def schema_stop(url, meta, err):
    print(f"\nSCHEMA MISMATCH in {url}\n  reason: {err}", file=sys.stderr)
    print(f"  top-level keys: {meta.get('top_keys')}", file=sys.stderr)
    cap = meta.get("_cap")
    head = bytes(cap.head) if cap else b""
    print(f"  first {len(head)} bytes:\n{head.decode('utf-8', 'replace')}", file=sys.stderr)
    sys.exit(2)


# ------------------------------------------------------------- inventory
def new_rec():
    return {"payers": set(), "descriptions": set(), "plans": {}, "markets": set(),
            "tocs_primary": set(), "tocs_employer": set()}


def ingest(url, payer, role, inv, allowed):
    meta = {}
    t0, n_struct, n_plans, n_links = time.time(), 0, 0, 0
    try:
        for item in iter_toc(url, meta):
            n_struct += 1
            plans = item.get("reporting_plans") or []
            n_plans += len(plans)
            aaf = item.get("allowed_amount_file")
            if isinstance(aaf, dict) and aaf.get("location"):
                allowed[aaf["location"]].add(payer)
            for fobj in item.get("in_network_files") or []:
                loc = (fobj or {}).get("location")
                if not loc:
                    continue
                n_links += 1
                rec = inv[loc]
                rec["payers"].add(payer)
                if fobj.get("description"):
                    rec["descriptions"].add(fobj["description"].strip())
                (rec["tocs_primary"] if role == "primary" else rec["tocs_employer"]).add(url)
                for p in plans:
                    key = (p.get("plan_id_type", ""), str(p.get("plan_id", "")), p.get("plan_name", ""))
                    rec["plans"].setdefault(key, p.get("plan_market_type", ""))
                    if p.get("plan_market_type"):
                        rec["markets"].add(p["plan_market_type"])
    except SchemaError as e:
        schema_stop(url, meta, e)
    return {"entity": meta.get("reporting_entity_name", ""),
            "entity_type": meta.get("reporting_entity_type", ""),
            "structures": n_struct, "plan_rows": n_plans, "in_network_links": n_links,
            "seconds": round(time.time() - t0, 1)}


def directory_tocs(page, blob_base):
    html = SESSION.get(page, timeout=60).text
    names = sorted(set(re.findall(r"\d{4}-\d{2}-\d{2}_[A-Za-z0-9._-]+?_index\.json", html)))
    return [blob_base + n for n in names]


def write_csv(path, rows, fields):
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tocs", default=f"{HERE}/toc_urls.csv")
    ap.add_argument("--out", default=f"{HERE}/output")
    ap.add_argument("--scan-directory", action="store_true",
                    help="also parse every employer TOC on the HPHC plan-list page")
    args = ap.parse_args()

    import os
    os.makedirs(args.out, exist_ok=True)
    tocs = list(csv.DictReader(open(args.tocs)))

    # 1. HEAD each TOC
    print("== TOC HEAD results")
    toc_rows = []
    for t in tocs:
        h = head_info(t["toc_url"])
        toc_rows.append({**t, **h})
        print(f"  [{t['payer'][:22]:22}] {h['status']!s:4} {str(h['size_bytes']):>10} B  "
              f"type={h['content_type'] or '-'}  enc={h['content_encoding'] or '-'}  "
              f"{h['error'][:80]}  {t['toc_url'].rsplit('/', 1)[-1] or t['toc_url']}")

    # 2-3. stream-parse primary TOCs (+ optional employer TOCs)
    inv, allowed = defaultdict(new_rec), defaultdict(set)
    jobs = [(t["toc_url"], t["payer"], "primary") for t in tocs if t["role"] == "primary"]
    if args.scan_directory:
        primary = {j[0] for j in jobs}
        for payer, (page, base) in DIRECTORY_PAGES.items():
            extra = [u for u in directory_tocs(page, base) if u not in primary]
            print(f"\n{payer}: {len(extra)} additional TOCs on plan-list page")
            jobs += [(u, payer, "employer") for u in extra]

    print("\n== Parsing TOCs")
    parse_rows = []
    for i, (url, payer, role) in enumerate(jobs, 1):
        try:
            st = ingest(url, payer, role, inv, allowed)
        except requests.RequestException as e:
            print(f"  FAILED {url}: {e}")
            parse_rows.append({"toc_url": url, "payer": payer, "role": role, "error": str(e)[:300]})
            continue
        parse_rows.append({"toc_url": url, "payer": payer, "role": role, **st})
        if role == "primary" or i % 20 == 0 or i == len(jobs):
            print(f"  {i:3}/{len(jobs)} {role:8} structs={st['structures']:5} plans={st['plan_rows']:6} "
                  f"links={st['in_network_links']:6} {st['seconds']:5}s  entity={st['entity']!r} "
                  f"{url.rsplit('/', 1)[-1]}")
    write_csv(f"{args.out}/toc_parse_log.csv", parse_rows,
              ["payer", "role", "toc_url", "entity", "entity_type", "structures", "plan_rows",
               "in_network_links", "seconds", "error"])
    write_csv(f"{args.out}/toc_heads.csv", toc_rows,
              ["payer", "role", "toc_url", "status", "size_bytes", "content_type",
               "content_encoding", "last_modified", "method", "error", "note"])

    # 4. HEAD every distinct in-network URL
    urls = sorted(inv)
    print(f"\n== {len(urls)} distinct in-network file URLs; sending HEAD requests")
    with ThreadPoolExecutor(max_workers=8) as ex:
        heads = dict(zip(urls, ex.map(head_info, urls)))

    rows = []
    for u in urls:
        rec, h = inv[u], heads[u]
        plans = sorted(rec["plans"], key=lambda k: k[2])
        rows.append({
            "payer": "; ".join(sorted(rec["payers"])),
            "file_description": " | ".join(sorted(rec["descriptions"])),
            "location_url": u,
            "number_of_reporting_plans": len(plans),
            "example_plan_names": " | ".join(list(dict.fromkeys(p[2] for p in plans))[:5]),
            "plan_market_types": "; ".join(sorted(rec["markets"])),
            "n_primary_tocs": len(rec["tocs_primary"]),
            "n_employer_tocs": len(rec["tocs_employer"]),
            "size_bytes": h["size_bytes"],
            "last_modified": h["last_modified"],
            "content_type": h["content_type"],
            "content_encoding": h["content_encoding"],
            "head_method": h["method"],
            "head_status": h["status"],
            "head_error": h["error"],
        })
    fields = list(rows[0]) if rows else []
    write_csv(f"{args.out}/network_inventory.csv", rows, fields)
    write_csv(f"{args.out}/allowed_amount_files.csv",
              [{"payer": "; ".join(sorted(p)), "location_url": u} for u, p in sorted(allowed.items())],
              ["payer", "location_url"])
    bad = [r for r in rows if r["size_bytes"] == ""]
    print(f"Wrote {args.out}/network_inventory.csv ({len(rows)} rows; {len(bad)} without size)")


if __name__ == "__main__":
    main()
