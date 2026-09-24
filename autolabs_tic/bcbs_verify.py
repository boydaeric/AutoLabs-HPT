#!/usr/bin/env python3
"""Verify the Blue Cross MA 95924 / 95922 / 93660 office-rate gap.

1. From the raw kept items (raw_items_bcbsma_*.jsonl): every negotiated
   price for 95922, 95924, 93660 grouped by billing_class, service_codes,
   modifiers, negotiated_type (count, provider references, rate range),
   plus an explicit test for professional rows without modifier 26 and
   for TC rows.
2. Re-scan the four Blue Cross files (same validated brace-depth scanner
   as extract_tic.py) for comparison codes - nerve conduction, EMG, ECG,
   Holter, vascular ultrasound - and report whether each has an office
   (POS 11 / blank) professional global rate. The same pass records TIN
   business names from provider_references.
3. The tax IDs holding 95924-26 rates, with every NPI attached through the
   provider references of those negotiated rates (not truncated), rates,
   files and business names -> output/bcbs_95924_26_tins.csv.

Usage:  .venv/bin/python bcbs_verify.py
"""
import csv
import glob
import gzip
import io
import json
import os
import re
from collections import defaultdict

import pandas as pd

import extract_tic as X

HERE = X.HERE
OUT = X.OUT
GAP_CODES = ["95922", "95924", "93660"]
CONTEXT = (["95907", "95908", "95910", "95911"] + [str(c) for c in range(95860, 95887)]
           + ["93000", "93224", "93225", "93226", "93227", "93880", "93886"])
ALL_SCAN = set(CONTEXT) | {"95921", "95922", "95923", "95924", "93660"}
REPORT = os.path.join(OUT, "bcbs_verify.txt")
buf = io.StringIO()


def p(s=""):
    print(s)
    buf.write(s + "\n")


def is_office(svc):
    return not svc or "11" in svc


def price_rows(item):
    for nr in item.get("negotiated_rates") or []:
        refs = nr.get("provider_references") or []
        for pr in nr.get("negotiated_prices") or []:
            yield refs, pr


# ------------------------------------------------------------------ part 1
def part1():
    p("== 1. Blue Cross rows for 95922, 95924, 93660 (from raw items)")
    violations = []
    for path in sorted(glob.glob(os.path.join(OUT, "raw_items_bcbsma_*.jsonl"))):
        fid = os.path.basename(path)[len("raw_items_bcbsma_"):-6]
        recs = []
        for line in open(path):
            it = json.loads(line)
            if it["billing_code"] not in GAP_CODES:
                continue
            for refs, pr in price_rows(it):
                mods = ",".join(sorted(pr.get("billing_code_modifier") or [])) or "(none)"
                svc = ",".join(sorted(pr.get("service_code") or [])) or "(blank)"
                recs.append(dict(code=it["billing_code"], billing_class=pr.get("billing_class"),
                                 service_codes=svc, modifiers=mods,
                                 negotiated_type=pr.get("negotiated_type"),
                                 rate=float(pr["negotiated_rate"]), refs=len(refs)))
                if (pr.get("billing_class") == "professional" and "26" not in
                        (pr.get("billing_code_modifier") or [])) or \
                        "TC" in (pr.get("billing_code_modifier") or []):
                    violations.append((fid, it["billing_code"], pr))
        d = pd.DataFrame(recs)
        p(f"\n-- {fid}")
        g = d.groupby(["code", "billing_class", "service_codes", "modifiers", "negotiated_type"]).agg(
            prices=("rate", "size"), provider_refs=("refs", "sum"),
            rate_min=("rate", "min"), rate_max=("rate", "max"))
        p(g.to_string())
    p(f"\n   professional rows without modifier 26, or any TC row, for {', '.join(GAP_CODES)} "
      f"in any Blue Cross file: {len(violations)}")
    for v in violations[:20]:
        p(f"     {v}")
    return not violations


# ------------------------------------------------------------------ part 2
def scan_file(rec):
    """Stream one Blue Cross file; return {code: [items]} and {tin: names}."""
    items, names = defaultdict(list), defaultdict(set)
    X.SUBSTRINGS = tuple(c.encode() for c in sorted(ALL_SCAN))   # scanner pre-filter

    def on_ref(raw):
        o = json.loads(raw)
        for pg in o.get("provider_groups") or []:
            t = pg.get("tin") or {}
            if t.get("business_name"):
                names[str(t.get("value"))].add(t["business_name"].strip())

    def on_item(raw, _off):
        it = json.loads(raw)
        c = str(it.get("billing_code", "")).strip()
        if str(it.get("billing_code_type", "")).upper() in X.CODE_TYPES and c in ALL_SCAN:
            items[c].append(it)

    log = {"bytes_downloaded": 0, "bytes_decompressed": 0}
    sc = X.Scanner(on_ref, on_item)
    for seg, final in X.segments(X.byte_source(rec, log), log):
        sc.feed(seg, final)
    return items, names, sc.scanned


def summarise_code(its):
    """Office professional global (no modifier) price stats for one code."""
    g_rates, g_refs, other, weighted = [], 0, defaultdict(int), defaultdict(int)
    for it in its:
        for refs, pr in price_rows(it):
            mods = pr.get("billing_code_modifier") or []
            key = (pr.get("billing_class"), ",".join(mods) or "global",
                   "office" if is_office(pr.get("service_code")) else "facility/other")
            other[key] += 1
            if key == ("professional", "global", "office") and \
                    str(pr.get("negotiated_type", "")).lower() != "percentage":
                g_rates.append(float(pr["negotiated_rate"]))
                g_refs += len(refs)
                weighted[float(pr["negotiated_rate"])] += len(refs)
    return g_rates, g_refs, other, weighted


def part2(recs):
    p("\n== 2. Office professional global rates for comparison codes (Blue Cross)")
    all_names, rows = defaultdict(set), []
    for rec in recs:
        items, names, scanned = scan_file(rec)
        for k, v in names.items():
            all_names[k] |= v
        fid = rec["file_code"]
        present = sorted(items)
        p(f"\n-- {fid}: {scanned:,} in_network items scanned; comparison codes present: "
          f"{len([c for c in present if c in CONTEXT])} of {len(CONTEXT)} listed")
        for c in sorted(ALL_SCAN):
            if c not in items:
                if c in CONTEXT:
                    rows.append(dict(file=fid, code=c, in_file="N"))
                continue
            rates, nrefs, shapes, weighted = summarise_code(items[c])
            rng = f"{min(rates):.2f}-{max(rates):.2f}" if rates else ""
            # modal (non-percentage) rate weighted by provider references (a proxy
            # for how many provider groups carry it)
            mode = max(weighted, key=weighted.get) if weighted else None
            shape_txt = "; ".join(f"{bc}/{m}/{s}={n}" for (bc, m, s), n in sorted(shapes.items()))
            rows.append(dict(file=fid, code=c, in_file="Y", office_global="Y" if rates else "N",
                             office_global_prices=len(rates), office_global_provider_refs=nrefs,
                             office_global_range=rng, office_global_mode=mode, price_shapes=shape_txt))
    d = pd.DataFrame(rows)
    d.to_csv(os.path.join(OUT, "bcbs_office_coverage.csv"), index=False)
    # compact cross-file view: office_global Y/N per code per file
    piv = d.assign(v=d.apply(lambda r: "absent" if r.in_file == "N" else
                             (f"Y {r.office_global_mode:.2f}" if r.office_global == "Y" else "N"), axis=1)) \
        .pivot(index="code", columns="file", values="v").fillna("")
    piv.columns = [c.replace("-Fully-Insured", "").replace("New-England-Managed-Care", "NEMC")
                   .replace("Blue-Care-Elect", "BCE") for c in piv.columns]
    p("\n   office professional global: Y <modal non-percentage rate, weighted by provider references> / "
      "N (code present, no office global) / absent (code not in file)")
    p(piv.to_string())
    ctx = d[d.code.isin(CONTEXT) & (d.in_file == "Y")]
    p(f"\n   comparison codes present in files: {ctx.code.nunique()} of {len(CONTEXT)} listed; "
      f"with an office global rate in every file: "
      f"{ctx.groupby('code').office_global.apply(lambda s: (s == 'Y').all()).sum()}")
    lacking = sorted(ctx[ctx.office_global == "N"].code.unique())
    p(f"   comparison codes present but lacking office global in some file: {lacking or 'none'}")
    for c in lacking:
        p(f"     {c}: " + d[(d.code == c)].price_shapes.iloc[0])
    return all_names


# ------------------------------------------------------------------ part 3
def part3(names):
    p("\n== 3. Tax IDs holding Blue Cross 95924-26 rates")
    refs = pd.read_csv(os.path.join(OUT, "provider_refs_needed.csv.gz"), dtype=str,
                       keep_default_na=False)
    refs = refs[refs.file_id.isin([os.path.basename(f)[len("raw_items_bcbsma_"):-6] for f in
                                   glob.glob(os.path.join(OUT, "raw_items_bcbsma_*.jsonl"))])]
    grp = defaultdict(list)
    for f, g, npi, tt, tv in zip(refs.file_id, refs.provider_group_id, refs.npi, refs.tin_type,
                                 refs.tin_value):
        grp[(f, g)].append((tt, tv, npi))
    tins = defaultdict(lambda: {"tin_type": "", "npis": set(), "rates": set(), "files": set(),
                                "settings": set()})
    for path in sorted(glob.glob(os.path.join(OUT, "raw_items_bcbsma_*.jsonl"))):
        fid = os.path.basename(path)[len("raw_items_bcbsma_"):-6]
        for line in open(path):
            it = json.loads(line)
            if it["billing_code"] != "95924":
                continue
            for nr in it.get("negotiated_rates") or []:
                prs = [pr for pr in nr.get("negotiated_prices") or []
                       if (pr.get("billing_code_modifier") or []) == ["26"]]
                if not prs:
                    continue
                for ref in nr.get("provider_references") or []:
                    for tt, tv, npi in grp.get((fid, str(ref)), []):
                        t = tins[tv]
                        t["tin_type"] = tt
                        if npi:
                            t["npis"].add(npi)
                        t["files"].add(fid)
                        for pr in prs:
                            t["rates"].add(f"{float(pr['negotiated_rate']):.2f}"
                                           if pr.get("negotiated_type") != "percentage"
                                           else f"{pr['negotiated_rate']}%")
                            t["settings"].add(",".join(pr.get("service_code") or []) or "blank")
    rows = []
    for tv, t in tins.items():
        rows.append(dict(tin_type=t["tin_type"], tin_value=tv,
                         business_names=" | ".join(sorted(names.get(tv, []))),
                         rates_95924_26=" | ".join(sorted(t["rates"], key=lambda r: float(r.rstrip("%")))),
                         service_codes=" | ".join(sorted(t["settings"])),
                         n_files=len(t["files"]), files=" | ".join(sorted(t["files"])),
                         npi_count=len(t["npis"]), npis="|".join(sorted(t["npis"]))))
    d = pd.DataFrame(rows).sort_values(["npi_count", "tin_value"], ascending=[False, True])
    path = os.path.join(OUT, "bcbs_95924_26_tins.csv")
    d.to_csv(path, index=False)
    p(f"   {len(d)} tax IDs; {d.npi_count.sum():,} NPI links ({len(set('|'.join(d.npis).split('|')) - {''}):,} "
      f"distinct NPIs); in all 4 files: {(d.n_files == 4).sum()}; with business name: "
      f"{(d.business_names != '').sum()}")
    p(f"   rate distribution (TINs): " + ", ".join(
        f"{r}: {n}" for r, n in d.rates_95924_26.value_counts().head(8).items()))
    p(f"   written to {os.path.relpath(path, HERE)}; full list:")
    p(f"   {'tin':12} {'npis':>5} {'files':>5}  {'95924-26 rate(s)':22} business name / first NPIs")
    for r in d.itertuples():
        first = r.npis.split("|")[:3]
        p(f"   {r.tin_value:12} {r.npi_count:5} {r.n_files:5}  {r.rates_95924_26[:22]:22} "
          f"{r.business_names[:60]}  [{', '.join(first)}{'...' if r.npi_count > 3 else ''}]")


def main():
    ok1 = part1()
    sel = [r for r in csv.DictReader(open(os.path.join(HERE, "selection.csv")))
           if r["process"] == "Y" and r["payer"].startswith("Blue Cross")]
    names = part2(sel)
    part3(names)
    p(f"\nFinding confirmed for 95922/95924/93660 (no professional non-26 row, no TC row): {ok1}")
    open(REPORT, "w").write(buf.getvalue())
    print(f"\nWrote {REPORT}")


if __name__ == "__main__":
    main()
