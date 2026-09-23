#!/usr/bin/env python3
"""Stream-extract target billing codes from the MRFs listed in manifest.csv.

For each MRF:
  * JSON (plain/.gz): streamed from HTTP and parsed with ijson; keeps every
    standard_charge_information item whose code_information has a target code.
  * CSV tall/wide (plain/.gz): streamed row by row; keeps every row where any
    code|N column holds a target code (all columns kept, incl. payer/plan).
  * .zip: downloaded to disk (after a 1.2x free-space check), only the data
    member(s) extracted, stream-parsed, then both files deleted.

Nothing reads a whole file into memory. Downloads retry up to 3 times,
resuming with HTTP Range where the server supports it.

Output: raw_<hospital>.jsonl (one match per line, original record under
"record"), extract_log.csv (per-file stats).

Usage:  python extract_codes.py [--manifest manifest.csv] [--out DIR]
"""
import argparse
import csv
import gzip
import io
import json
import os
import re
import shutil
import sys
import time
import zipfile
from decimal import Decimal

import ijson
import requests
import urllib3

from discover_mrfs import make_session

TARGET_CODES = {"95921", "95922", "95923", "95924", "93660"}
JSON_HEADER_SCALARS = ("hospital_name", "last_updated_on", "version")
JSON_HEADER_OBJECTS = ("license_information",)
ITEM_PREFIX = "standard_charge_information.item"
MAX_RETRIES = 3
CHUNK = 1 << 20

csv.field_size_limit(sys.maxsize)


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def slug(name):
    return re.sub(r"[^a-z0-9]+", "_", name.lower().replace("'", "")).strip("_")


def code_matches(value):
    """True if value is a target code, optionally followed by a non-digit
    suffix (e.g. '95921-26'). Never matches e.g. '959210'."""
    v = str(value or "").strip()
    return v[:5] in TARGET_CODES and (len(v) == 5 or not v[5].isdigit())


def to_json(obj):
    def default(o):
        if isinstance(o, Decimal):
            return int(o) if o == o.to_integral_value() and o.as_tuple().exponent >= 0 else float(o)
        raise TypeError(type(o))
    return json.dumps(obj, default=default, ensure_ascii=False)


# --------------------------------------------------------------------------
# Resumable HTTP byte stream
# --------------------------------------------------------------------------
class ResumableStream(io.RawIOBase):
    """File-like view of an HTTP body that transparently reconnects on
    failure, resuming with a Range request (or skipping already-read bytes
    if the server ignores Range). Yields wire bytes (Content-Encoding is
    NOT decoded here, so byte offsets stay valid for Range)."""

    RETRYABLE = (requests.ConnectionError, requests.Timeout, requests.HTTPError,
                 urllib3.exceptions.HTTPError, ConnectionError, TimeoutError)

    def __init__(self, session, url):
        self.session, self.url = session, url
        self.pos, self.retries, self.resp = 0, 0, None
        self.content_encoding = ""
        self.range_used = False
        self._with_retry(self._open)
        self.content_encoding = self.resp.headers.get("Content-Encoding", "").lower()

    def _with_retry(self, fn):
        while True:
            try:
                return fn()
            except self.RETRYABLE as e:
                if isinstance(e, requests.HTTPError) and e.response is not None \
                        and e.response.status_code < 500 and e.response.status_code != 429:
                    raise
                if self.retries >= MAX_RETRIES:
                    raise
                self.retries += 1
                log(f"    retry {self.retries}/{MAX_RETRIES} at byte {self.pos}: {e.__class__.__name__}: {e}")
                time.sleep(2 ** self.retries)
                if self.resp is not None:
                    self.resp.close()
                    self.resp = None  # _read reconnects (inside this retry loop)

    def _open(self):
        headers = {"Accept-Encoding": "identity"}
        if self.pos:
            headers["Range"] = f"bytes={self.pos}-"
        r = self.session.get(self.url, headers=headers, stream=True, timeout=(30, 120))
        r.raise_for_status()
        if self.pos:
            if r.status_code == 206:
                self.range_used = True
            else:  # server ignored Range: discard what we already have
                left = self.pos
                while left:
                    chunk = r.raw.read(min(left, CHUNK), decode_content=False)
                    if not chunk:
                        raise ConnectionError("stream ended while skipping to resume offset")
                    left -= len(chunk)
        self.resp = r

    def readable(self):
        return True

    def readinto(self, b):
        def _read():
            if self.resp is None:
                self._open()
            data = self.resp.raw.read(len(b), decode_content=False)
            n = len(data)
            b[:n] = data
            return n
        n = self._with_retry(_read)
        self.pos += n
        return n

    def close(self):
        if self.resp is not None:
            self.resp.close()
        super().close()


class CountingReader(io.RawIOBase):
    """Counts decoded bytes flowing to the parser."""

    def __init__(self, f):
        self.f, self.n = f, 0

    def readable(self):
        return True

    def readinto(self, b):
        data = self.f.read(len(b))
        n = len(data)
        b[:n] = data
        self.n += n
        return n


def decoded_stream(raw, content_encoding, is_gz_file):
    """Layer HTTP content-encoding and .gz file decompression on a byte stream."""
    s = io.BufferedReader(raw, CHUNK)
    if content_encoding == "gzip":
        s = gzip.GzipFile(fileobj=s)
    if is_gz_file:
        s = gzip.GzipFile(fileobj=s)
    return s


# --------------------------------------------------------------------------
# Parsers (operate on a binary file-like; return stats, yield matches)
# --------------------------------------------------------------------------
def parse_json(f, stats, emit):
    """Single ijson pass: build each standard_charge_information item and the
    header objects; everything else is skipped at the event level."""
    header = {}
    building = None  # (kind, builder, depth)
    for prefix, event, value in ijson.parse(f):
        if building is None:
            if prefix == ITEM_PREFIX and event == "start_map":
                building = ["item", ijson.ObjectBuilder(), 0]
            elif prefix in JSON_HEADER_OBJECTS and event in ("start_map", "start_array"):
                building = [prefix, ijson.ObjectBuilder(), 0]
            elif prefix in JSON_HEADER_SCALARS and event not in ("start_map", "start_array", "map_key"):
                header[prefix] = value
                continue
            else:
                continue
        kind, builder, depth = building
        builder.event(event, value)
        if event in ("start_map", "start_array"):
            building[2] = depth + 1
        elif event in ("end_map", "end_array"):
            building[2] = depth - 1
            if building[2] == 0:
                obj = builder.value
                building = None
                if kind == "item":
                    stats["items_scanned"] += 1
                    codes = [c.get("code") for c in obj.get("code_information") or []
                             if isinstance(c, dict)]
                    if any(code_matches(c) for c in codes):
                        emit(obj)
                else:
                    header[kind] = obj
    stats["schema_version"] = str(header.get("version", ""))
    return header


def norm_col(c):
    return re.sub(r"\s+", "", c.strip().lower())


def parse_csv(f, stats, emit):
    text = io.TextIOWrapper(f, encoding="utf-8-sig", errors="replace", newline="")
    reader = csv.reader(text)
    pre = []
    columns = None
    for row in reader:
        normed = [norm_col(c) for c in row]
        if "description" in normed and any(re.fullmatch(r"code\|\d+", c) for c in normed):
            columns = row
            break
        pre.append(row)
        if len(pre) > 20:
            raise ValueError("CSV column header row not found in first 20 rows")
    if columns is None:
        raise ValueError("CSV column header row not found")
    header = dict(zip(pre[0], pre[1])) if len(pre) >= 2 else {}
    normed = [norm_col(c) for c in columns]
    code_idx = [i for i, c in enumerate(normed) if re.fullmatch(r"code\|\d+", c)]
    stats["csv_layout"] = "tall" if "payer_name" in normed else "wide"
    ver_key = next((k for k in header if norm_col(k) == "version"), None)
    stats["schema_version"] = header.get(ver_key, "") if ver_key else ""
    for row in reader:
        stats["items_scanned"] += 1
        if any(i < len(row) and code_matches(row[i]) for i in code_idx):
            emit(dict(zip(columns, row)))
    return header


def sniff_format(path_or_name, first_bytes=b""):
    n = path_or_name.lower().removesuffix(".gz")
    if n.endswith(".json"):
        return "JSON"
    if n.endswith(".csv"):
        return "CSV"
    return "JSON" if first_bytes.lstrip()[:1] in (b"{", b"[") else "CSV"


# --------------------------------------------------------------------------
# Per-MRF drivers
# --------------------------------------------------------------------------
def run_parser(fmt, f, stats, emit):
    counter = CountingReader(f)
    buf = io.BufferedReader(counter, CHUNK)
    fmt = fmt if fmt in ("JSON", "CSV") else sniff_format("", buf.peek(64))
    stats["parsed_as"] = fmt
    try:
        return (parse_json if fmt == "JSON" else parse_csv)(buf, stats, emit)
    finally:
        stats["decoded_bytes"] += counter.n


def process_stream(session, row, stats, emit):
    url = row["mrf_url"]
    raw = ResumableStream(session, url)
    try:
        is_gz = row["compression"] == "gz" or url.lower().split("?")[0].endswith(".gz")
        f = decoded_stream(raw, raw.content_encoding, is_gz)
        fmt = sniff_format(url.split("?")[0]) if row["format"].startswith("unknown") else row["format"].split()[0]
        stats["member"] = os.path.basename(url.split("?")[0])
        return [(stats["member"], run_parser(fmt, f, stats, emit))]
    finally:
        stats["wire_bytes"] += raw.pos
        stats["retries"] += raw.retries
        stats["range_resumed"] = stats["range_resumed"] or raw.range_used
        raw.close()


def free_bytes(path):
    return shutil.disk_usage(path).free


def process_zip(session, row, stats, emit, workdir):
    url = row["mrf_url"]
    size = int(row["size_bytes"] or 0)
    need = int(size * 1.2)
    if free_bytes(workdir) < need:
        raise OSError(f"insufficient disk: need {need}, free {free_bytes(workdir)}")
    zpath = os.path.join(workdir, f"_dl_{slug(row['hospital'])}.zip")
    headers = []
    try:
        raw = ResumableStream(session, url)
        try:
            src = decoded_stream(raw, raw.content_encoding, False)
            with open(zpath, "wb") as out:
                shutil.copyfileobj(src, out, CHUNK)
        finally:
            stats["wire_bytes"] += raw.pos
            stats["retries"] += raw.retries
            stats["range_resumed"] = stats["range_resumed"] or raw.range_used
            raw.close()
        stats["zip_bytes"] = os.path.getsize(zpath)
        with zipfile.ZipFile(zpath) as zf:
            members = [m for m in zf.infolist()
                       if not m.is_dir() and not m.filename.startswith("__MACOSX")
                       and re.search(r"\.(json|csv)(\.gz)?$", m.filename, re.I)]
            if not members:
                raise ValueError(f"no data member in zip: {[m.filename for m in zf.infolist()]}")
            stats["member"] = ";".join(m.filename for m in members)
            for m in members:
                if free_bytes(workdir) < int(m.file_size * 1.2):
                    raise OSError(f"insufficient disk to extract {m.filename} ({m.file_size} bytes)")
                mpath = zf.extract(m, os.path.join(workdir, "_extract"))
                try:
                    with open(mpath, "rb") as fh:
                        f = gzip.GzipFile(fileobj=fh) if mpath.lower().endswith(".gz") else fh
                        headers.append((m.filename, run_parser(sniff_format(m.filename), f, stats, emit)))
                finally:
                    os.remove(mpath)
    finally:
        if os.path.exists(zpath):
            os.remove(zpath)
        shutil.rmtree(os.path.join(workdir, "_extract"), ignore_errors=True)
    return headers


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="manifest.csv")
    ap.add_argument("--out", default=".")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.manifest, newline="")))
    session = make_session()
    log_rows = []
    opened = set()
    log_cols = ["hospital", "mrf_url", "member", "parsed_as", "csv_layout", "schema_version",
                "wire_bytes", "zip_bytes", "decoded_bytes", "items_scanned", "matches",
                "matches_by_code", "retries", "range_resumed", "elapsed_s", "status", "error"]

    for row in rows:
        hosp = row["hospital"]
        out_path = os.path.join(args.out, f"raw_{slug(hosp)}.jsonl")
        mode = "a" if out_path in opened else "w"
        opened.add(out_path)
        stats = dict.fromkeys(log_cols, "")
        stats.update(hospital=hosp, mrf_url=row["mrf_url"], wire_bytes=0, zip_bytes=0,
                     decoded_bytes=0, items_scanned=0, retries=0, range_resumed=False)
        matches = []  # only matched records are held; header may follow items in JSON
        by_code = {}

        def emit(rec):
            matches.append(rec)

        log(f"==> {hosp}: {row['mrf_url']}")
        t0 = time.time()
        try:
            if row["compression"] == "zip":
                headers = process_zip(session, row, stats, emit, args.out)
            else:
                headers = process_stream(session, row, stats, emit)
            stats["status"] = "ok"
        except Exception as e:  # log and move on to the next file
            headers = []
            stats["status"] = "failed"
            stats["error"] = f"{e.__class__.__name__}: {e}"
        stats["elapsed_s"] = round(time.time() - t0, 1)

        header = headers[0][1] if len(headers) == 1 else {m: h for m, h in headers}
        with open(out_path, mode) as out:
            for rec in matches:
                codes = sorted({str(v).strip()[:5] for k, v in _code_items(rec) if code_matches(v)})
                for c in codes:
                    by_code[c] = by_code.get(c, 0) + 1
                out.write(to_json({"hospital": hosp, "mrf_url": row["mrf_url"],
                                   "source_member": stats["member"], "format": stats["parsed_as"],
                                   "matched_codes": codes, "header": header, "record": rec}) + "\n")
        stats["matches"] = len(matches)
        stats["matches_by_code"] = ";".join(f"{c}:{n}" for c, n in sorted(by_code.items()))
        log(f"    {stats['status']}: wire={stats['wire_bytes']:,}B decoded={stats['decoded_bytes']:,}B "
            f"scanned={stats['items_scanned']:,} matches={stats['matches']} ({stats['matches_by_code']}) "
            f"schema={stats['schema_version']} {stats['parsed_as']} {stats['csv_layout']} "
            f"retries={stats['retries']} {stats['elapsed_s']}s {stats['error']}")
        log_rows.append(stats)

    with open(os.path.join(args.out, "extract_log.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=log_cols)
        w.writeheader()
        w.writerows(log_rows)
    return 0 if all(r["status"] == "ok" for r in log_rows) else 1


def _code_items(rec):
    """(key, code) pairs from a JSON item's code_information or CSV code|N cols."""
    if "code_information" in rec:
        return [("code", c.get("code")) for c in rec["code_information"] or [] if isinstance(c, dict)]
    return [(k, v) for k, v in rec.items() if re.fullmatch(r"code\|\d+", norm_col(k))]


if __name__ == "__main__":
    sys.exit(main())
