#!/usr/bin/env python3
"""Extract target-code in_network items (and provider references) from the
TiC in-network files marked process = Y in selection.csv.

Byte sources
  * .json.gz / .json < 5 GB : streamed straight from the URL through zlib.
  * .json.gz / .json >= 5 GB: resumable Range download to downloads/ (only if
    free space >= 1.1 x size), stream-parsed from disk, then deleted.
  * .zip (Harvard Pilgrim, Tufts): a zip cannot be read without its central
    directory at the end, so it is downloaded to downloads/ with the same
    resumable Range logic, its JSON member(s) stream-decompressed from disk,
    then the zip is deleted.

Parsing (pre-filter mode, the default)
  The decompressed stream is scanned in ~8 MB segments. numpy locates every
  structural character ({ } [ ]) outside JSON strings and tracks brace depth,
  which splits the two top-level arrays into their elements without parsing
  them:
    * provider_references[] elements: every one is json-parsed and written to
      SQLite provider_refs (one row per NPI), or remote_refs if it only has a
      location URL.
    * in_network[] elements: the element's own "billing_code" (the one at
      element depth, not bundled/covered codes deeper down) is read with a
      regex. Only elements whose code contains "9592" or "93660" are kept in
      memory and json-parsed; an item is kept if billing_code_type is CPT or
      HCPCS and billing_code is a target. Elements with no element-level
      billing_code fall back to the same substring test on the whole element.
  Kept items are written minified but otherwise byte-for-byte unchanged to
  output/raw_items_<payer>_<fileid>.jsonl; their provider_references IDs go
  to needed_refs.

  The first file processed is also validated: a full ijson (yajl2_c) parse of
  its first 2 GB of decompressed data must yield exactly the same kept items
  and the same number of in_network items as the pre-filter over that range.

After all files, remote_refs whose provider_group_id is in needed_refs are
fetched and added to provider_refs.

Usage:  .venv/bin/python extract_tic.py [--only FILE_ID ...] [--no-validate]
"""
import argparse
import csv
import json
import os
import re
import shutil
import sqlite3
import sys
import time
import zipfile
import zlib

import ijson
import numpy as np
import requests

from tic_common import SESSION, verify_for

if ijson.backend != "yajl2_c":
    sys.exit(f"ijson backend is {ijson.backend!r}; yajl2_c is required")

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output")
DL = os.path.join(HERE, "downloads")
DB_PATH = os.path.join(OUT, "tic_refs.sqlite")

TARGET_CODES = {"95921", "95922", "95923", "95924", "93660"}
CODE_TYPES = {"CPT", "HCPCS"}
SUBSTRINGS = (b"9592", b"93660")
PAYER_ORDER = ["Harvard Pilgrim Health Care", "Tufts Health Plan",
               "Blue Cross Blue Shield of Massachusetts"]
PAYER_SLUG = {"Harvard Pilgrim Health Care": "hphc", "Tufts Health Plan": "tufts",
              "Blue Cross Blue Shield of Massachusetts": "bcbsma"}
BCBS_SIZE_LIMIT = 25e9
STREAM_LIMIT = 5e9
SEGMENT = 8 << 20
READ = 1 << 20
VALIDATE_BYTES = 2 << 30

LUT = np.zeros(256, np.int8)
LUT[ord("{")] = LUT[ord("[")] = 1
LUT[ord("}")] = LUT[ord("]")] = -1
CODE_RE = re.compile(rb'"billing_code"\s*:\s*"?([^",\s}\]]*)')
KEY_TAIL_RE = re.compile(rb'"((?:[^"\\]|\\.)*)"\s*:\s*$')
MINIFY_RE = re.compile(rb'("(?:[^"\\]|\\.)*")|\s+')


class SchemaError(Exception):
    pass


def minify(raw):
    """Drop whitespace outside strings; everything else stays byte-identical."""
    return MINIFY_RE.sub(lambda m: m.group(1) or b"", raw)


def rss_mb():
    with open("/proc/self/status") as fh:
        for line in fh:
            if line.startswith("VmRSS:"):
                return int(line.split()[1]) / 1024
    return 0.0


# ------------------------------------------------------------------ sources
def download(url, path, size, log):
    """Resumable Range download of url to path (size bytes)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    part = path + ".part"
    have = os.path.getsize(part) if os.path.exists(part) else 0
    free = shutil.disk_usage(os.path.dirname(path)).free
    if free < 1.1 * (size - have):
        raise RuntimeError(f"not enough disk: need {1.1 * (size - have) / 1e9:.1f} GB, "
                           f"free {free / 1e9:.1f} GB")
    attempts = 0
    while have < size:
        try:
            r = SESSION.get(url, headers={"Range": f"bytes={have}-"}, stream=True,
                            timeout=(30, 300), verify=verify_for(url))
            if r.status_code == 200 and have:        # server ignored Range
                have = 0
                open(part, "wb").close()
            elif r.status_code not in (200, 206):
                r.raise_for_status()
            with open(part, "ab" if have else "wb") as fh:
                for chunk in r.iter_content(READ):
                    fh.write(chunk)
                    have += len(chunk)
                    log["bytes_downloaded"] += len(chunk)
        except (requests.RequestException, OSError) as e:
            attempts += 1
            if attempts > 8:
                raise
            wait = min(2 ** attempts, 60)
            print(f"    download interrupted at {have:,} B ({type(e).__name__}); resume in {wait}s")
            time.sleep(wait)
            have = os.path.getsize(part)
    if have != size:
        raise RuntimeError(f"downloaded {have} bytes, expected {size}")
    os.replace(part, path)
    return path


def gunzip_chunks(read):
    """Decompress a (possibly multi-member) gzip byte source."""
    first = read(READ)
    if first[:2] != b"\x1f\x8b":                     # plain JSON
        while first:
            yield first
            first = read(READ)
        return
    d, buf = zlib.decompressobj(31), first
    while True:
        if not buf:
            buf = read(READ)
            if not buf:
                break
        out = d.decompress(buf)
        if out:
            yield out
        buf = b""
        if d.eof:
            buf = d.unused_data
            d = zlib.decompressobj(31)
            if not buf:
                buf = read(READ)
                if not buf:
                    break
    tail = d.flush()
    if tail:
        yield tail


def byte_source(rec, log):
    """Yield decompressed JSON bytes for one selected file."""
    url, size = rec["location_url"], int(float(rec["size_bytes"]))
    name = url.rsplit("/", 1)[-1].split("?")[0]
    if name.endswith(".zip") or size >= STREAM_LIMIT:
        path = download(url, os.path.join(DL, name), size, log)
        log["mode"] = "disk-zip" if name.endswith(".zip") else "disk-gz"
        try:
            if name.endswith(".zip"):
                with zipfile.ZipFile(path) as zf:
                    members = [m for m in zf.infolist() if m.filename.endswith(".json")]
                    log["members"] = ";".join(m.filename for m in members)
                    if len(members) != 1:
                        raise SchemaError(f"expected 1 JSON member, found {len(members)}")
                    with zf.open(members[0]) as fh:
                        while True:
                            b = fh.read(READ)
                            if not b:
                                break
                            yield b
            else:
                with open(path, "rb") as fh:
                    yield from gunzip_chunks(fh.read)
        finally:
            os.remove(path)
    else:
        log["mode"] = "stream"
        r = SESSION.get(url, stream=True, timeout=(30, 300), verify=verify_for(url))
        r.raise_for_status()
        r.raw.decode_content = False

        def read(n):
            b = r.raw.read(n)
            log["bytes_downloaded"] += len(b)
            return b
        try:
            yield from gunzip_chunks(read)
        finally:
            r.close()


def segments(chunks, log):
    """Regroup decompressed chunks into ~SEGMENT pieces that end right after
    a comma, so no "billing_code": "..." pair is ever split across pieces."""
    parts, n = [], 0
    for c in chunks:
        log["bytes_decompressed"] += len(c)
        parts.append(c)
        n += len(c)
        if n < SEGMENT:
            continue
        data = b"".join(parts)
        cut = data.rfind(b",") + 1
        if cut <= 0:
            parts, n = [data], len(data)
            continue
        yield data[:cut], False
        parts, n = [data[cut:]], len(data) - cut
    yield b"".join(parts), True


# ------------------------------------------------------------------ scanner
class Scanner:
    """Brace-depth splitter for a TiC in-network JSON stream."""

    def __init__(self, on_ref, on_item, stop_at=None):
        self.on_ref, self.on_item = on_ref, on_item
        self.offset = 0                  # global offset of current segment
        self.parity = 0                  # 1 = inside a string at segment start
        self.depth = 0
        self.skeleton = bytearray()      # top-level text with containers emptied
        self.outside_from = 0            # global offset where depth<=1 text resumes
        self.container = None            # key of open top-level container
        self.containers = []
        self.elem = None                 # open element: dict
        self.scanned = 0                 # in_network elements seen
        self.scanned_cut = 0             # ... that close before stop_at (validation)
        self.no_code = 0
        self.first_bytes = b""
        self.stop_at = stop_at

    def feed(self, seg, final=False):
        if not self.first_bytes:
            self.first_bytes = bytes(seg[:2048])
        a = np.frombuffer(seg, np.uint8)
        qpos = np.flatnonzero(a == 34)
        if seg.find(b"\\") >= 0 and len(qpos):
            cand = qpos[(qpos > 0) & (a[np.maximum(qpos - 1, 0)] == 92)]
            if len(cand):
                bad = []
                for q in cand.tolist():
                    k = q - 1
                    while k >= 0 and seg[k] == 92:
                        k -= 1
                    if (q - 1 - k) % 2:
                        bad.append(q)
                if bad:
                    qpos = np.setdiff1d(qpos, np.array(bad, dtype=qpos.dtype))
        d = LUT[a]
        spos = np.flatnonzero(d)
        outside = ((np.searchsorted(qpos, spos) + self.parity) & 1) == 0
        spos = spos[outside]
        dv = d[spos].astype(np.int32)
        dep = np.cumsum(dv) + self.depth
        start_depth = self.depth

        ev = np.flatnonzero(((dv == 1) & ((dep == 2) | (dep == 3))) |
                            ((dv == -1) & ((dep == 1) | (dep == 2))))
        events = [(int(spos[i]), 0, int(dv[i]), int(dep[i])) for i in ev]

        # element-level billing_code values (depth 3 = directly inside an
        # element of a top-level array; bundled/covered codes sit deeper)
        ms = [(m.start(), m.group(1)) for m in CODE_RE.finditer(seg)]
        if ms:
            idx = np.searchsorted(spos, np.fromiter((p for p, _ in ms), np.int64, len(ms)))
            mdep = np.where(idx > 0, dep[np.maximum(idx - 1, 0)] if len(dep) else start_depth,
                            start_depth)
            events += [(p, 1, v, 0) for (p, v), dd in zip(ms, mdep.tolist()) if dd == 3]
        events.sort(key=lambda e: e[0])

        base = self.offset
        for pos, kind, x, y in events:
            if kind == 1:
                e = self.elem
                if e is not None and self.container == "in_network" and e["code"] is None:
                    e["code"] = x
                    if not any(s in x for s in SUBSTRINGS):
                        e["parts"] = None            # not a candidate: stop buffering
                continue
            dv_, dep_ = x, y
            if dv_ == 1 and dep_ == 2:               # top-level container opens
                lo = max(self.outside_from - base, 0)
                self.skeleton += seg[lo:pos + 1]
                m = KEY_TAIL_RE.search(bytes(self.skeleton[-1024:-1]))
                self.container = m.group(1).decode() if m else "?"
                self.containers.append(self.container)
            elif dv_ == -1 and dep_ == 1:            # top-level container closes
                self.skeleton += seg[pos:pos + 1]
                self.outside_from = base + pos + 1
                self.container = None
            elif dv_ == 1 and dep_ == 3:             # element opens
                keep = self.container in ("in_network", "provider_references")
                self.elem = {"start": base + pos, "parts": [] if keep else None,
                             "lo": pos, "code": None}
            elif dv_ == -1 and dep_ == 2:            # element closes
                e, self.elem = self.elem, None
                if e is None:
                    continue
                if self.container == "in_network":
                    self.scanned += 1
                    if self.stop_at is not None and base + pos < self.stop_at:
                        self.scanned_cut += 1
                    if e["code"] is None:
                        self.no_code += 1
                if e["parts"] is None:
                    continue
                raw = b"".join(e["parts"]) + seg[max(e["lo"], 0):pos + 1] \
                    if e["parts"] else seg[max(e["lo"], 0):pos + 1]
                if self.container == "provider_references":
                    self.on_ref(raw)
                elif self.container == "in_network":
                    if e["code"] is None and not any(s in raw for s in SUBSTRINGS):
                        continue
                    self.on_item(raw, base + pos)
        # carry an unfinished element's bytes into the next segment
        if self.elem is not None:
            if self.elem["parts"] is not None:
                self.elem["parts"].append(seg[max(self.elem["lo"], 0):])
            self.elem["lo"] = -1
        if self.container is None:
            lo = max(self.outside_from - base, 0)
            self.skeleton += seg[lo:]
            self.outside_from = base + len(seg)
        self.parity = (self.parity + len(qpos)) & 1
        self.depth = int(dep[-1]) if len(dep) else self.depth
        self.offset += len(seg)
        if final:
            self.finish()

    def finish(self):
        if self.depth != 0:
            raise SchemaError(f"stream ended at depth {self.depth}")
        try:
            self.header = json.loads(bytes(self.skeleton))
        except ValueError as e:
            raise SchemaError(f"top level is not a JSON object: {e}")
        if not isinstance(self.header, dict) or "in_network" not in self.header:
            raise SchemaError("no in_network[] at top level")


# --------------------------------------------------------------- database
def open_db():
    con = sqlite3.connect(DB_PATH)
    con.executescript("""
        PRAGMA journal_mode=WAL; PRAGMA synchronous=OFF;
        CREATE TABLE IF NOT EXISTS provider_refs(file_id TEXT, provider_group_id TEXT,
            npi TEXT, tin_type TEXT, tin_value TEXT, source TEXT);
        CREATE TABLE IF NOT EXISTS remote_refs(file_id TEXT, provider_group_id TEXT,
            location TEXT, status TEXT);
        CREATE TABLE IF NOT EXISTS needed_refs(file_id TEXT, provider_group_id TEXT,
            PRIMARY KEY(file_id, provider_group_id));
    """)
    return con


def clear_file(con, file_id):
    for t in ("provider_refs", "remote_refs", "needed_refs"):
        con.execute(f"DELETE FROM {t} WHERE file_id=?", (file_id,))
    con.commit()


def ref_rows(file_id, obj, source):
    pgid = str(obj.get("provider_group_id", ""))
    for pg in obj.get("provider_groups") or []:
        tin = pg.get("tin") or {}
        for npi in pg.get("npi") or [None]:
            yield (file_id, pgid, None if npi is None else str(npi),
                   tin.get("type"), None if tin.get("value") is None else str(tin.get("value")),
                   source)


# ---------------------------------------------------------------- per file
def process_file(rec, con, validate):
    payer = rec["payer"]
    file_id = re.sub(r"^TuftsHealthPublicPlans_", "", rec["file_code"])
    slug = PAYER_SLUG[payer]
    out_path = os.path.join(OUT, f"raw_items_{slug}_{file_id}.jsonl")
    log = {"payer": payer, "file_id": file_id, "size_bytes": int(float(rec["size_bytes"])),
           "mode": "", "bytes_downloaded": 0, "bytes_decompressed": 0, "items_scanned": 0,
           "items_kept": 0, "kept_by_code": "", "candidates_rejected": 0,
           "items_without_code": 0, "provider_ref_groups": 0, "provider_ref_rows": 0,
           "remote_ref_urls": 0, "needed_refs": 0, "elapsed_s": 0, "mb_per_s": 0,
           "peak_rss_mb": 0, "reporting_entity_name": "", "version": "",
           "last_updated_on": "", "output": os.path.relpath(out_path, HERE), "error": ""}
    clear_file(con, file_id)
    t0, peak = time.time(), rss_mb()
    kept_by_code, rows, needed = {}, [], set()
    kept_offsets = []
    fh = open(out_path, "wb")

    def on_ref(raw):
        nonlocal rows
        obj = json.loads(raw)
        log["provider_ref_groups"] += 1
        if obj.get("location") and not obj.get("provider_groups"):
            con.execute("INSERT INTO remote_refs VALUES (?,?,?,NULL)",
                        (file_id, str(obj.get("provider_group_id", "")), obj["location"]))
            log["remote_ref_urls"] += 1
            return
        rows.extend(ref_rows(file_id, obj, "inline"))
        if len(rows) >= 50000:
            con.executemany("INSERT INTO provider_refs VALUES (?,?,?,?,?,?)", rows)
            log["provider_ref_rows"] += len(rows)
            rows = []

    def on_item(raw, end_offset):
        item = json.loads(raw)
        code = str(item.get("billing_code", "")).strip()
        ctype = str(item.get("billing_code_type", "")).strip().upper()
        if ctype not in CODE_TYPES or code not in TARGET_CODES:
            log["candidates_rejected"] += 1
            return
        fh.write(minify(raw) + b"\n")
        kept_by_code[code] = kept_by_code.get(code, 0) + 1
        if validate:
            kept_offsets.append((end_offset, item))
        for nr in item.get("negotiated_rates") or []:
            for pr in nr.get("provider_references") or []:
                needed.add(str(pr))

    sc = Scanner(on_ref, on_item, stop_at=VALIDATE_BYTES if validate else None)
    try:
        for seg, final in segments(byte_source(rec, log), log):
            sc.feed(seg, final)
            peak = max(peak, rss_mb())
    except SchemaError as e:
        fh.close()
        print(f"\nSCHEMA MISMATCH in {rec['location_url']}\n  reason: {e}", file=sys.stderr)
        print(f"  top-level keys seen: {sc.containers} + skeleton "
              f"{bytes(sc.skeleton[:300])!r}", file=sys.stderr)
        print(f"  first 2 KB:\n{sc.first_bytes.decode('utf-8', 'replace')}", file=sys.stderr)
        sys.exit(2)
    fh.close()
    if rows:
        con.executemany("INSERT INTO provider_refs VALUES (?,?,?,?,?,?)", rows)
        log["provider_ref_rows"] += len(rows)
    con.executemany("INSERT OR IGNORE INTO needed_refs VALUES (?,?)",
                    [(file_id, n) for n in sorted(needed)])
    con.commit()
    el = time.time() - t0
    log.update(items_scanned=sc.scanned, items_kept=sum(kept_by_code.values()),
               kept_by_code="; ".join(f"{k}={v}" for k, v in sorted(kept_by_code.items())),
               items_without_code=sc.no_code, needed_refs=len(needed),
               elapsed_s=round(el, 1), mb_per_s=round(log["bytes_decompressed"] / 1e6 / el, 1),
               peak_rss_mb=round(peak), reporting_entity_name=sc.header.get("reporting_entity_name", ""),
               version=sc.header.get("version", ""), last_updated_on=sc.header.get("last_updated_on", ""))
    if validate:
        log["_validate"] = (sc.scanned_cut, kept_offsets)
    return log


# -------------------------------------------------------------- validation
class LimitedReader:
    def __init__(self, chunks, limit):
        self.it, self.limit, self.n, self.buf = chunks, limit, 0, b""

    def read(self, size=-1):
        if size is None or size < 0:
            size = 1 << 30
        while len(self.buf) < size and self.n < self.limit:
            try:
                c = next(self.it)
            except StopIteration:
                break
            c = c[:self.limit - self.n]
            self.n += len(c)
            self.buf += c
        out, self.buf = self.buf[:size], self.buf[size:]
        return out


def validate_first(rec, pre_scanned, pre_kept):
    """Full ijson parse of the first VALIDATE_BYTES of the same file."""
    print(f"\n== Validating pre-filter on {rec['file_code']} against a full ijson parse "
          f"of the first {VALIDATE_BYTES / 2**30:.0f} GiB")
    log = {"bytes_downloaded": 0, "bytes_decompressed": 0}
    t0 = time.time()
    src = byte_source(rec, log)
    rdr = LimitedReader(src, VALIDATE_BYTES)
    full_scanned, full_kept = 0, []
    try:
        for item in ijson.items(rdr, "in_network.item", use_float=True):
            full_scanned += 1
            if str(item.get("billing_code_type", "")).upper() in CODE_TYPES and \
                    str(item.get("billing_code", "")).strip() in TARGET_CODES:
                full_kept.append(item)
    except ijson.common.IncompleteJSONError:
        pass                                            # truncated at the 2 GiB mark
    src.close()
    el = time.time() - t0
    rate = rdr.n / 1e6 / el
    canon = lambda o: json.dumps(o, sort_keys=True)
    pre = sorted(canon(i) for off, i in pre_kept if off < rdr.n)
    full = sorted(canon(i) for i in full_kept)
    # The pre-filter counts items that close before the cut; ijson yields the
    # same set (an item is only yielded once its closing brace is read).
    ok = pre == full and pre_scanned == full_scanned
    print(f"   ijson items() full parse: {rdr.n / 1e9:.2f} GB decompressed in {el:.0f}s "
          f"= {rate:.1f} MB/s")
    print(f"   in_network items within range: pre-filter {pre_scanned:,} vs full {full_scanned:,}")
    print(f"   target items within range:     pre-filter {len(pre)} vs full {len(full)}  "
          f"identical={pre == full}")
    return ok, rate


def bench_events(rec, nbytes=512 << 20):
    """Throughput of a full event-level ijson parse (what a pure-ijson
    extractor that also handles provider_references must do)."""
    log = {"bytes_downloaded": 0, "bytes_decompressed": 0}
    src = byte_source(rec, log)
    rdr = LimitedReader(src, nbytes)
    t0, n = time.time(), 0
    try:
        for _ in ijson.parse(rdr):
            n += 1
    except ijson.common.IncompleteJSONError:
        pass
    src.close()
    el = time.time() - t0
    return rdr.n / 1e6 / el, n


# --------------------------------------------------------------- remote refs
def fetch_remote(con):
    todo = con.execute("""SELECT DISTINCT r.file_id, r.provider_group_id, r.location
                          FROM remote_refs r JOIN needed_refs n
                          ON r.file_id=n.file_id AND r.provider_group_id=n.provider_group_id
                          WHERE r.status IS NULL""").fetchall()
    print(f"\n== Remote provider references needed: {len(todo)}")
    for file_id, pgid, loc in todo:
        try:
            r = SESSION.get(loc, timeout=120, verify=verify_for(loc))
            r.raise_for_status()
            body = r.content
            if body[:2] == b"\x1f\x8b":
                body = zlib.decompress(body, 31)
            obj = json.loads(body)
            obj.setdefault("provider_group_id", pgid)
            obj["provider_group_id"] = pgid
            rows = list(ref_rows(file_id, obj, "remote"))
            con.executemany("INSERT INTO provider_refs VALUES (?,?,?,?,?,?)", rows)
            status = f"ok:{len(rows)}"
        except (requests.RequestException, ValueError, zlib.error) as e:
            status = f"error:{type(e).__name__}"
        con.execute("UPDATE remote_refs SET status=? WHERE file_id=? AND provider_group_id=? "
                    "AND location=?", (status, file_id, pgid, loc))
        print(f"   {file_id} {pgid} {status}")
    con.commit()
    return len(todo)


# ---------------------------------------------------------------------- main
LOG_FIELDS = ["payer", "file_id", "mode", "size_bytes", "bytes_downloaded", "bytes_decompressed",
              "items_scanned", "items_kept", "kept_by_code", "candidates_rejected",
              "items_without_code", "provider_ref_groups", "provider_ref_rows", "remote_ref_urls",
              "needed_refs", "elapsed_s", "mb_per_s", "peak_rss_mb", "reporting_entity_name",
              "version", "last_updated_on", "output", "error"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="file_code(s) to process")
    ap.add_argument("--no-validate", action="store_true")
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)

    sel = [r for r in csv.DictReader(open(os.path.join(HERE, "selection.csv")))
           if r["process"].strip().upper() == "Y"]
    sel.sort(key=lambda r: (PAYER_ORDER.index(r["payer"]), r["file_code"]))
    if args.only:
        sel = [r for r in sel if r["file_code"] in args.only or
               re.sub(r"^TuftsHealthPublicPlans_", "", r["file_code"]) in args.only]

    # Size gate for Blue Cross
    print("== Blue Cross file sizes (selected)")
    too_big = []
    for r in sel:
        if r["payer"].startswith("Blue Cross"):
            gb = float(r["size_bytes"]) / 1e9
            print(f"   {r['file_code']:45} {gb:8.3f} GB")
            if float(r["size_bytes"]) > BCBS_SIZE_LIMIT:
                too_big.append(r)
    if too_big:
        print(f"   {len(too_big)} Blue Cross file(s) exceed 25 GB -> not processed: "
              + ", ".join(r["file_code"] for r in too_big))
        sel = [r for r in sel if not r["payer"].startswith("Blue Cross")]

    con = open_db()
    logs, first = [], not args.no_validate
    for r in sel:
        print(f"\n-- {r['payer']} / {r['file_code']} ({float(r['size_bytes']) / 1e6:,.0f} MB)")
        for attempt in range(1, 4):
            try:
                log = process_file(r, con, validate=first)
                break
            except (requests.RequestException, zlib.error, OSError, RuntimeError) as e:
                print(f"   attempt {attempt} failed: {type(e).__name__}: {e}")
                clear_file(con, re.sub(r"^TuftsHealthPublicPlans_", "", r["file_code"]))
                if attempt == 3:
                    log = {"payer": r["payer"], "file_id": r["file_code"], "error": str(e)[:300]}
        if first and "_validate" in log:
            pre_scanned, pre_kept = log.pop("_validate")
            ok, rate = validate_first(r, pre_scanned, pre_kept)
            ev_rate, n_ev = bench_events(r)
            print(f"   ijson.parse() event loop: {ev_rate:.1f} MB/s ({n_ev:,} events on 512 MiB)")
            print(f"   pre-filter: {log['mb_per_s']} MB/s over the whole file")
            if not ok:
                sys.exit("PRE-FILTER VALIDATION FAILED - stopping")
            print("   pre-filter validated OK")
            first = False
        log.pop("_validate", None)
        logs.append(log)
        print(f"   {log.get('mode')}: downloaded {log.get('bytes_downloaded', 0) / 1e6:,.0f} MB, "
              f"decompressed {log.get('bytes_decompressed', 0) / 1e9:,.2f} GB, "
              f"scanned {log.get('items_scanned')}, kept {log.get('items_kept')} "
              f"[{log.get('kept_by_code')}], refs {log.get('provider_ref_groups')} groups / "
              f"{log.get('provider_ref_rows')} rows, remote {log.get('remote_ref_urls')}, "
              f"{log.get('elapsed_s')}s ({log.get('mb_per_s')} MB/s), peak {log.get('peak_rss_mb')} MB")
        with open(os.path.join(OUT, "extract_log.csv"), "w", newline="") as fh:
            w = csv.DictWriter(fh, LOG_FIELDS, extrasaction="ignore")
            w.writeheader()
            w.writerows(logs)

    fetch_remote(con)
    print("\n== Extraction log")
    for l in logs:
        print("  " + ", ".join(f"{k}={l.get(k)}" for k in LOG_FIELDS if k not in ("output",)))
    if too_big:
        print("\nSTOPPED: Blue Cross files over 25 GB were not processed: "
              + ", ".join(f"{r['file_code']} ({float(r['size_bytes']) / 1e9:.1f} GB)" for r in too_big))


if __name__ == "__main__":
    main()
