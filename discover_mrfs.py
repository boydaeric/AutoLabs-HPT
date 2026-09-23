#!/usr/bin/env python3
"""Discover hospital price transparency MRFs and write manifest.csv.

Steps:
  1. Read each health system's cms-hpt.txt (fall back to its price
     transparency page if the txt file is missing).
  2. Keep only the target hospitals (all of their MRFs).
  3. HEAD each MRF URL; record size, type, encoding, last-modified.
  4. Infer format (CSV tall / CSV wide / JSON) and compression.
  5. Write manifest.csv and print it. MRFs are NOT downloaded; the only
     body bytes fetched are an optional small Range peek (--peek-bytes)
     at the start of CSV files to tell tall from wide layout.

Usage:  python discover_mrfs.py [--out DIR] [--peek-bytes N]
"""
import argparse
import csv
import io
import re
import sys
import zlib
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import requests

CMS_HPT_URLS = [
    "https://www.massgeneralbrigham.org/cms-hpt.txt",
    "https://www.bilh.org/cms-hpt.txt",
    "https://www.bidmc.org/cms-hpt.txt",
]
FALLBACK_PAGES = {
    "massgeneralbrigham.org": "https://www.massgeneralbrigham.org/en/patients-visitors/billing-insurance/billing/cms-required-hospital-charge-data",
    "bilh.org": "https://bilh.org/billing-financial-services/price-transparency",
    "bidmc.org": "https://bilh.org/billing-financial-services/price-transparency",
}

# Canonical hospital name -> (include regex, exclude regex) on normalized names.
TARGETS = {
    "Massachusetts General Hospital": (r"\bmassachusetts general hospital\b|\bmgh\b", r"children|brigham|salem|cooley|north shore|newton"),
    "Brigham and Women's Hospital": (r"\bbrigham and womens? hospital\b|\bbwh\b", r"faulkner"),
    "Brigham and Women's Faulkner Hospital": (r"\bfaulkner\b", r"$^"),
    "Wentworth-Douglass Hospital": (r"\bwentworth douglass\b", r"$^"),
    "Beth Israel Deaconess Medical Center": (r"\bbeth israel deaconess medical center\b|\bbidmc\b", r"milton|needham|plymouth"),
}

UA = {"User-Agent": "Mozilla/5.0 (price-transparency research; autolabs_hpt)"}
TIMEOUT = 60


def norm(name):
    name = name.lower().replace("’", "'").replace("'", "")
    return re.sub(r"[^a-z0-9]+", " ", name).strip()


def match_target(location_name):
    n = norm(location_name)
    for canon, (inc, exc) in TARGETS.items():
        if re.search(inc, n) and not re.search(exc, n):
            return canon
    return None


def parse_cms_hpt(text):
    """Parse cms-hpt.txt into a list of dicts (one per location block)."""
    entries, cur = [], {}
    for line in text.splitlines():
        line = line.strip().lstrip("﻿")
        if not line:
            continue
        key, sep, val = line.partition(":")
        if not sep:
            continue
        key = key.strip().lower()
        if key == "location-name" and cur.get("location-name"):
            entries.append(cur)
            cur = {}
        cur[key] = val.strip()
    if cur:
        entries.append(cur)
    return entries


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self._href, self._text = [], None, []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href, self._text = dict(attrs).get("href"), []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href:
            self.links.append((self._href, " ".join("".join(self._text).split())))
            self._href = None


MRF_LINK = re.compile(r"\.(json|csv|zip|gz)(\?|$)|standardcharges|standard-charges", re.I)


def scrape_fallback(page_url, session):
    """Pull MRF links off a price transparency page (link text used as name)."""
    r = session.get(page_url, timeout=TIMEOUT)
    r.raise_for_status()
    p = LinkParser()
    p.feed(r.text)
    out = []
    for href, text in p.links:
        url = urljoin(page_url, href)
        if MRF_LINK.search(url):
            # Filename often carries the hospital name if link text doesn't.
            label = text or urlparse(url).path.rsplit("/", 1)[-1]
            out.append({"location-name": label, "source-page-url": page_url, "mrf-url": url})
    return out


def discover(session):
    rows, seen_names, log = [], [], []
    tried_fallback = set()
    for url in CMS_HPT_URLS:
        domain = urlparse(url).netloc.removeprefix("www.")
        entries = []
        try:
            r = session.get(url, timeout=TIMEOUT)
            if r.status_code == 200 and "mrf-url" in r.text.lower():
                entries = parse_cms_hpt(r.text)
                log.append(f"{url}: {len(entries)} entries")
            else:
                log.append(f"{url}: HTTP {r.status_code}, no mrf-url entries")
        except requests.RequestException as e:
            log.append(f"{url}: ERROR {e.__class__.__name__}: {e}")
        if not entries:
            fb = FALLBACK_PAGES.get(domain)
            if fb and fb not in tried_fallback:
                tried_fallback.add(fb)
                try:
                    entries = scrape_fallback(fb, session)
                    log.append(f"  fallback {fb}: {len(entries)} MRF links")
                except requests.RequestException as e:
                    log.append(f"  fallback {fb}: ERROR {e.__class__.__name__}: {e}")
        for e in entries:
            name = e.get("location-name", "")
            seen_names.append(name)
            canon = match_target(name) or match_target(e.get("mrf-url", ""))
            if canon and e.get("mrf-url"):
                rows.append({"hospital": canon, "location_name": name,
                             "source_page_url": e.get("source-page-url", ""),
                             "mrf_url": e["mrf-url"]})
    # De-duplicate (bidmc.org and bilh.org may list the same file).
    uniq = {}
    for r in rows:
        uniq.setdefault((r["hospital"], r["mrf_url"]), r)
    return list(uniq.values()), seen_names, log


def infer_compression(url, ctype, cenc):
    path = urlparse(url).path.lower()
    if path.endswith(".zip") or "zip" in ctype and "gzip" not in ctype:
        return "zip"
    if path.endswith(".gz") or "gzip" in ctype or cenc == "gzip":
        return "gz"
    return "none"


def infer_base_format(url, ctype):
    path = re.sub(r"\.(zip|gz)$", "", urlparse(url).path.lower())
    if path.endswith(".json") or "json" in ctype:
        return "JSON"
    if path.endswith(".csv") or "csv" in ctype or "text/plain" in ctype:
        return "CSV"
    return "unknown"


def csv_layout(sample_text):
    """CMS v2 template: tall has payer_name/plan_name columns; wide encodes
    payer|plan in column names like standard_charge|Aetna|PPO|negotiated_dollar."""
    lines = sample_text.splitlines()
    # Header row is line 3 in the v2 template (after 2 general-data rows).
    for line in lines[:6]:
        cols = [c.strip().lower() for c in next(csv.reader(io.StringIO(line)), [])]
        if "payer_name" in cols:
            return "CSV tall"
        if sum(c.startswith("standard_charge|") and c.count("|") >= 3 for c in cols):
            return "CSV wide"
    return "CSV (layout unknown)"


def peek(session, url, compression, nbytes):
    """Fetch the first nbytes (Range request) and return decoded text or None."""
    if nbytes <= 0 or compression == "zip":
        return None  # zip central directory is at the end; can't peek cheaply
    r = session.get(url, headers={"Range": f"bytes=0-{nbytes - 1}", "Accept-Encoding": "identity"},
                    timeout=TIMEOUT, stream=True)
    data = r.raw.read(nbytes, decode_content=False)
    r.close()
    if compression == "gz" or data[:2] == b"\x1f\x8b":
        data = zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(data)
    return data.decode("utf-8-sig", errors="replace")


def head_info(session, url, peek_bytes):
    info = {"http_status": "", "size_bytes": "", "content_type": "", "content_encoding": "",
            "last_modified": "", "format": "unknown", "compression": "unknown", "note": ""}
    try:
        r = session.head(url, allow_redirects=True, timeout=TIMEOUT)
        if r.status_code in (403, 405, 501):  # some hosts refuse HEAD
            r = session.get(url, stream=True, timeout=TIMEOUT)
            r.close()
            info["note"] = "HEAD refused; headers from GET (body not read)"
        h = r.headers
        info.update(http_status=r.status_code, size_bytes=h.get("Content-Length", ""),
                    content_type=h.get("Content-Type", ""),
                    content_encoding=h.get("Content-Encoding", ""),
                    last_modified=h.get("Last-Modified", ""))
    except requests.RequestException as e:
        info["note"] = f"{e.__class__.__name__}: {e}"
        info["compression"] = infer_compression(url, "", "")
        info["format"] = infer_base_format(url, "")
        return info
    ctype, cenc = info["content_type"].lower(), info["content_encoding"].lower()
    info["compression"] = infer_compression(url, ctype, cenc)
    fmt = infer_base_format(url, ctype)
    if fmt == "CSV":
        try:
            sample = peek(session, url, info["compression"], peek_bytes)
            fmt = csv_layout(sample) if sample else "CSV (layout unknown)"
        except (requests.RequestException, zlib.error) as e:
            fmt = "CSV (layout unknown)"
            info["note"] = (info["note"] + f"; peek failed: {e}").strip("; ")
    info["format"] = fmt
    return info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=".", help="directory for manifest files")
    ap.add_argument("--peek-bytes", type=int, default=16384,
                    help="bytes to Range-read from CSV MRFs to detect tall/wide (0 = HEAD only)")
    args = ap.parse_args()

    s = requests.Session()
    s.headers.update(UA)
    rows, seen, log = discover(s)
    print("\n".join(log), file=sys.stderr)
    print(f"\nLocations seen ({len(seen)}); matched MRFs: {len(rows)}", file=sys.stderr)
    for canon in TARGETS:
        if not any(r["hospital"] == canon for r in rows):
            print(f"  WARNING: no MRF found for {canon}", file=sys.stderr)

    for r in rows:
        r.update(head_info(s, r["mrf_url"], args.peek_bytes))

    cols = ["hospital", "mrf_url", "format", "compression", "size_bytes", "last_modified"]
    detail_cols = cols + ["location_name", "source_page_url", "http_status",
                          "content_type", "content_encoding", "note"]
    rows.sort(key=lambda r: (list(TARGETS).index(r["hospital"]), r["mrf_url"]))
    for path, fields in ((f"{args.out}/manifest.csv", cols),
                         (f"{args.out}/manifest_detail.csv", detail_cols)):
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
    with open(f"{args.out}/locations_seen.txt", "w") as f:
        f.write("\n".join(seen) + "\n")

    with open(f"{args.out}/manifest.csv") as f:
        print(f.read())


if __name__ == "__main__":
    main()
