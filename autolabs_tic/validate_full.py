#!/usr/bin/env python3
"""Full-file cross-check of the pre-filter for one selected file: a full
ijson (yajl2_c) items() parse of every in_network item vs the
raw_items_*.jsonl the pre-filter wrote.

Usage:  .venv/bin/python validate_full.py FILE_CODE
"""
import csv
import json
import os
import sys
import time

import ijson

import extract_tic as X

X.DL = os.path.join(X.HERE, "downloads_validate")
code = sys.argv[1]
rec = next(r for r in csv.DictReader(open(os.path.join(X.HERE, "selection.csv")))
           if r["file_code"] == code)
slug = X.PAYER_SLUG[rec["payer"]]
fid = code.replace("TuftsHealthPublicPlans_", "")
pre = [json.loads(l) for l in open(os.path.join(X.OUT, f"raw_items_{slug}_{fid}.jsonl"))]

log = {"bytes_downloaded": 0, "bytes_decompressed": 0}
src = X.byte_source(rec, log)
rdr = X.LimitedReader(src, 1 << 62)
t0, n, full = time.time(), 0, []
for item in ijson.items(rdr, "in_network.item", use_float=True):
    n += 1
    if str(item.get("billing_code_type", "")).upper() in X.CODE_TYPES and \
            str(item.get("billing_code", "")).strip() in X.TARGET_CODES:
        full.append(item)
src.close()
canon = lambda o: json.dumps(o, sort_keys=True)
same = sorted(map(canon, pre)) == sorted(map(canon, full))
print(f"{code}: full parse {rdr.n / 1e9:.2f} GB in {time.time() - t0:.0f}s; in_network items {n:,}; "
      f"target items full={len(full)} pre-filter={len(pre)} identical={same}")
sys.exit(0 if same else 1)
