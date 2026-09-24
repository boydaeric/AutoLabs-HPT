#!/usr/bin/env python3
"""Normalise the extracted TiC items into output/tic_autonomic_rates.csv.

1. (only if output/tic_refs.sqlite exists) export the provider_refs rows
   whose provider_group_id is referenced by a kept item to
   output/provider_refs_needed.csv. Everything below reads only that CSV
   and the raw_items_*.jsonl files, never the SQLite database.
2. One output row per payer x network file x code x modifier set x
   billing_class x service_code set x negotiated_type x negotiated_rate x
   tax ID (plus description / arrangement / expiration / additional
   information, which are carried, not collapsed). NPIs of every provider
   group resolving to the same tax ID are merged.
3. Print the checks and write them to output/tic_checks.txt.

No imputation: percentage rates go to negotiated_percentage with the
dollar field blank; unresolved provider references keep blank TIN fields
and are counted.

Usage:  .venv/bin/python normalize_tic.py
"""
import csv
import glob
import gzip
import hashlib
import io
import json
import os
import sqlite3
import sys
from collections import Counter, defaultdict

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output")
DB = os.path.join(OUT, "tic_refs.sqlite")
# gzip-compressed: the plain CSVs are ~56 MB and ~1.2 GB (Harvard Pilgrim
# lists ~19,000 tax IDs per price), too large to commit uncompressed.
REFS_CSV = os.path.join(OUT, "provider_refs_needed.csv.gz")
RATES_CSV = os.path.join(OUT, "tic_autonomic_rates.csv.gz")
CHECKS_TXT = os.path.join(OUT, "tic_checks.txt")

SLUG_PAYER = {"hphc": "Harvard Pilgrim Health Care", "tufts": "Tufts Health Plan",
              "bcbsma": "Blue Cross Blue Shield of Massachusetts"}
# Place-of-service codes paid at the Medicare facility rate.
FACILITY_POS = {"19", "21", "22", "23", "24", "26", "31", "34", "51", "52", "53", "56", "61"}
NPI_LIMIT = 50

# CY2026 MPFS non-facility global, Metro Boston (locality 01), user-supplied
# (same values as build_summary.py). No PPRRVU2026 / GPCI files are in the
# repository, so Rest of Massachusetts = 0.88 x Metro Boston.
MEDICARE_METRO = {"95924": 174.79, "95923": 141.36, "battery": 316.15}
REST_FACTOR = 0.88
MEDICARE_REST = {k: round(v * REST_FACTOR, 2) for k, v in MEDICARE_METRO.items()}

COLUMNS = ["payer", "network_file", "file_last_updated", "code", "description",
           "negotiation_arrangement", "modifiers", "billing_class", "service_codes",
           "setting_group", "negotiated_type", "negotiated_rate", "negotiated_percentage",
           "expiration_date", "additional_information", "tin_type", "tin_value",
           "npi_count", "npis", "provider_ref_unresolved"]


# ---------------------------------------------------------------- step A
def export_needed_refs():
    if not os.path.exists(DB):
        print(f"{DB} not found; using existing {REFS_CSV}")
        return
    con = sqlite3.connect(DB)
    cur = con.execute("""
        SELECT p.file_id, p.provider_group_id, p.npi, p.tin_type, p.tin_value, p.source
        FROM provider_refs p JOIN needed_refs n
          ON p.file_id = n.file_id AND p.provider_group_id = n.provider_group_id
        ORDER BY p.file_id, CAST(p.provider_group_id AS INTEGER), p.tin_value, p.npi""")
    n = 0
    with gzip.open(REFS_CSV, "wt", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["file_id", "provider_group_id", "npi", "tin_type", "tin_value", "source"])
        for row in cur:
            w.writerow(row)
            n += 1
    print(f"Wrote {REFS_CSV}: {n:,} rows")


def load_refs():
    refs = defaultdict(lambda: defaultdict(set))       # (file, pgid) -> (tin_type, tin) -> {npi}
    df = pd.read_csv(REFS_CSV, dtype=str, keep_default_na=False)
    for f, g, npi, tt, tv in zip(df.file_id, df.provider_group_id, df.npi, df.tin_type, df.tin_value):
        s = refs[(f, g)][(tt, tv)]
        if npi:
            s.add(npi)
    return refs


# ---------------------------------------------------------------- step C
def setting_group(svc):
    if not svc or "11" in svc:
        return "office"
    if set(svc) <= FACILITY_POS:
        return "facility"
    return "other"


def fmt_num(x):
    if x is None or x == "":
        return ""
    return f"{float(x):.2f}" if isinstance(x, (int, float)) else str(x)


def build_rows(refs):
    log = pd.read_csv(os.path.join(OUT, "extract_log.csv"), dtype=str)
    updated = dict(zip(log.file_id, log.last_updated_on))
    rows = {}                                           # key -> row dict (npis as set)
    samples = defaultdict(dict)                         # payer -> {price shape: sample}
    stats = Counter()
    for path in sorted(glob.glob(os.path.join(OUT, "raw_items_*.jsonl"))):
        slug, file_id = os.path.basename(path)[len("raw_items_"):-len(".jsonl")].split("_", 1)
        payer = SLUG_PAYER[slug]
        for line in open(path):
            item = json.loads(line)
            code = str(item["billing_code"]).strip()
            for nr_i, nr in enumerate(item.get("negotiated_rates") or []):
                # resolve provider groups -> {(tin_type, tin): npis}
                tins, unresolved = defaultdict(set), []
                for pg in nr.get("provider_groups") or []:          # inline (v1.x)
                    t = pg.get("tin") or {}
                    tins[(t.get("type", ""), str(t.get("value", "")))] |= {str(n) for n in pg.get("npi") or []}
                for ref in nr.get("provider_references") or []:
                    stats["refs_total"] += 1
                    hit = refs.get((file_id, str(ref)))
                    if hit is None:
                        stats["refs_unresolved"] += 1
                        unresolved.append(str(ref))
                        continue
                    for tk, npis in hit.items():
                        tins[tk] |= npis
                targets = list(tins.items()) or [(("", ""), set())]
                for p_i, p in enumerate(nr.get("negotiated_prices") or []):
                    mods = ",".join(sorted(str(m) for m in p.get("billing_code_modifier") or []))
                    svc = sorted(str(s) for s in p.get("service_code") or [])
                    ntype = str(p.get("negotiated_type", "")).strip()
                    pct = ntype.lower() == "percentage"
                    rate = p.get("negotiated_rate")
                    base = (payer, file_id, updated.get(file_id, ""), code,
                            item.get("description", ""), item.get("negotiation_arrangement", ""),
                            mods, str(p.get("billing_class", "")).lower(), ",".join(svc),
                            setting_group(svc), ntype,
                            "" if pct else fmt_num(rate), fmt_num(rate) if pct else "",
                            p.get("expiration_date", ""), p.get("additional_information", "") or "")
                    for (tt, tv), npis in targets:
                        key = base + (tt, tv)
                        r = rows.get(key)
                        if r is None:
                            r = rows[key] = {"npis": set(), "unresolved": False}
                            # first row of each distinct price shape, for C4
                            shape = (code, mods, key[7], key[9], ntype)
                            if shape not in samples[payer]:
                                samples[payer][shape] = (file_id, item, nr_i, p_i, key)
                        r["npis"] |= npis
                        if unresolved and not tins:
                            r["unresolved"] = True
    out = []
    for key, r in rows.items():
        npis = sorted(r["npis"])
        shown = "|".join(npis[:NPI_LIMIT])
        if len(npis) > NPI_LIMIT:
            shown += f" (+{len(npis) - NPI_LIMIT} more)"
        out.append(dict(zip(COLUMNS, key + (len(npis), shown, "Y" if r["unresolved"] else ""))))
    df = pd.DataFrame(out, columns=COLUMNS)
    return df, samples, stats


# ---------------------------------------------------------------- checks
def mode_table(g):
    """Per-TIN mode: rate value -> number of distinct tax IDs."""
    c = g.groupby("negotiated_rate").tin_value.nunique().sort_values(ascending=False)
    return c


def checks(df, samples, stats, p):
    num = pd.to_numeric(df.negotiated_rate, errors="coerce")
    df = df.assign(rate=num)
    office = df[(df.setting_group == "office") & df.rate.notna()]

    p("== C1. Rows by payer, code and modifier set")
    t = df.assign(modifiers=df.modifiers.replace("", "(global)")) \
        .groupby(["payer", "code", "modifiers"]).size().unstack(fill_value=0)
    p(t.to_string())

    p("\n== C2. Office setting: distinct tax IDs and top-5 negotiated rates (rate: #TINs)")
    for (payer, code, mods), g in office.groupby(["payer", "code", "modifiers"]):
        top = mode_table(g).head(5)
        p(f"  {payer[:30]:30} {code} {mods or 'global':6} TINs={g.tin_value.nunique():6,}  "
          + "  ".join(f"{r}: {n:,}" for r, n in top.items()))

    p("\n== C3. Unresolved provider references")
    share = df.provider_ref_unresolved.eq("Y").mean() if len(df) else 0
    p(f"  provider_reference IDs: {stats['refs_total']:,} total, {stats['refs_unresolved']:,} unresolved; "
      f"rows with no resolvable provider: {df.provider_ref_unresolved.eq('Y').sum():,} "
      f"({share:.3%})")
    if share >= 0.01:
        p("  STOP: unresolved share is 1% or more")
        return False

    p("\n== B1/B2. Modal office global rates (mode over distinct tax IDs) vs CY2026 Medicare "
      "non-facility global")
    p(f"  Medicare Metro Boston: 95924 {MEDICARE_METRO['95924']}, 95923 {MEDICARE_METRO['95923']}, "
      f"battery {MEDICARE_METRO['battery']}")
    p(f"  Medicare Rest of MA:   95924 {MEDICARE_REST['95924']}, 95923 {MEDICARE_REST['95923']}, "
      f"battery {MEDICARE_REST['battery']}  (= {REST_FACTOR} x Metro Boston; no PPRRVU2026/GPCI "
      f"files in the repository to derive exact values)")
    glob_office = office[office.modifiers == ""]
    hdr = (f"  {'payer':30} {'network_file':40} {'code':7} {'modal':>8} {'TINs@mode':>9} "
           f"{'of TINs':>7} {'share':>6} {'xMetro':>6} {'xRest':>6}")
    p(hdr)
    for (payer, nf), g in glob_office.groupby(["payer", "network_file"]):
        modal = {}
        for code in ("95924", "95923"):
            gc = g[g.code == code]
            if gc.empty:
                p(f"  {payer[:30]:30} {nf[:40]:40} {code:7} {'-':>8}  no office global (unmodified) "
                  f"rate in this file; see C2 for modifier rows")
                continue
            c = mode_table(gc)
            rate, n = c.index[0], c.iloc[0]
            tot = gc.tin_value.nunique()
            modal[code] = float(rate)
            p(f"  {payer[:30]:30} {nf[:40]:40} {code:7} {float(rate):8.2f} {n:9,} {tot:7,} "
              f"{n / tot:6.1%} {float(rate) / MEDICARE_METRO[code]:6.2f} "
              f"{float(rate) / MEDICARE_REST[code]:6.2f}")
        if len(modal) == 2:
            b = modal["95924"] + modal["95923"]
            # TIN-level battery: TINs that carry both codes at their own rates
            per = g[g.code.isin(["95924", "95923"])].groupby(["tin_value", "code"]).rate.min().unstack()
            per = per.dropna()
            tb = (per["95924"] + per["95923"]).round(2).value_counts()
            tb_txt = (f"; TIN-level battery mode {tb.index[0]:.2f} at {tb.iloc[0]:,} of "
                      f"{len(per):,} TINs") if len(tb) else ""
            p(f"  {payer[:30]:30} {nf[:40]:40} {'battery':7} {b:8.2f} {'':9} {'':7} {'':6} "
              f"{b / MEDICARE_METRO['battery']:6.2f} {b / MEDICARE_REST['battery']:6.2f}{tb_txt}")

    p("\n== B3. Are the network files identical rate sets within a payer?")
    p("  hash of sorted (code, modifiers, billing_class, service_codes, negotiated_rate, tin_value)")
    for payer, g in df.groupby("payer"):
        hashes = {}
        for nf, gf in g.groupby("network_file"):
            tup = sorted(set(zip(gf.code, gf.modifiers, gf.billing_class, gf.service_codes,
                                 gf.negotiated_rate, gf.tin_value)))
            hashes[nf] = (hashlib.sha256(repr(tup).encode()).hexdigest()[:16], len(tup))
        for nf, (h, n) in hashes.items():
            p(f"  {payer[:30]:30} {nf:40} {h}  ({n:,} tuples)")
        same = len({h for h, _ in hashes.values()}) == 1
        p(f"  -> {payer}: {'IDENTICAL across all ' + str(len(hashes)) + ' files' if same else 'NOT identical'}")
        if not same:
            ref_nf = next(iter(hashes))
            base = set(zip(*[g[g.network_file == ref_nf][c] for c in
                             ("code", "modifiers", "billing_class", "service_codes", "negotiated_rate", "tin_value")]))
            for nf in list(hashes)[1:]:
                other = set(zip(*[g[g.network_file == nf][c] for c in
                                  ("code", "modifiers", "billing_class", "service_codes", "negotiated_rate", "tin_value")]))
                p(f"     {nf} vs {ref_nf}: only-in-{nf} {len(other - base):,}, only-in-{ref_nf} "
                  f"{len(base - other):,}, shared {len(base & other):,}")
                # same restricted to rate schedule without TIN
                bs = {t[:5] for t in base}
                os_ = {t[:5] for t in other}
                p(f"        rate schedule ignoring TIN: only-in-{nf} {len(os_ - bs)}, "
                  f"only-in-{ref_nf} {len(bs - os_)}, shared {len(bs & os_)}")

    p("\n== B4. negotiated_type and additional_information")
    p(df.groupby(["payer", "negotiated_type"]).size().to_string())
    ai = df[df.additional_information != ""].groupby(["payer", "additional_information"]).size()
    p(ai.to_string() if len(ai) else "  (no additional_information text)")

    p("\n== C4. Sample rows: raw item excerpt next to normalised row (10 per payer)")
    for payer, lst in samples.items():
        p(f"\n--- {payer}")
        # round-robin over codes so every code appears before any repeats
        by_code = defaultdict(list)
        for shape, smp in sorted(lst.items(), key=lambda kv: tuple(map(str, kv[0]))):
            by_code[shape[0]].append(smp)
        picked = []
        while len(picked) < 10 and any(by_code.values()):
            for c in sorted(by_code):
                if by_code[c] and len(picked) < 10:
                    picked.append(by_code[c].pop(0))
        for file_id, item, nr_i, p_i, key in picked:
            nr = item["negotiated_rates"][nr_i]
            refs_ = nr.get("provider_references") or []
            raw = {"billing_code": item["billing_code"], "billing_code_type": item["billing_code_type"],
                   "negotiation_arrangement": item.get("negotiation_arrangement"),
                   f"negotiated_rates[{nr_i}].provider_references":
                       refs_[:6] + ([f"... {len(refs_)} total"] if len(refs_) > 6 else []),
                   f"negotiated_rates[{nr_i}].negotiated_prices[{p_i}]": nr["negotiated_prices"][p_i]}
            row = df[(df.network_file == key[1]) & (df.code == key[3]) & (df.modifiers == key[6]) &
                     (df.billing_class == key[7]) & (df.service_codes == key[8]) &
                     (df.negotiated_type == key[10]) & (df.negotiated_rate == key[11]) &
                     (df.tin_value == key[16])].iloc[0].to_dict()
            row.pop("rate", None)
            if len(row["service_codes"]) > 40:
                row["service_codes"] = row["service_codes"][:40] + f"... ({row['service_codes'].count(',') + 1} codes)"
            if len(row["npis"]) > 60:
                row["npis"] = row["npis"][:60] + "..."
            p(f"  [{file_id}] RAW  {json.dumps(raw, separators=(',', ':'))[:700]}")
            p(f"  {'':{len(file_id) + 2}} NORM " + json.dumps({k: row[k] for k in COLUMNS if k not in
                                                                ("payer", "network_file", "description")}))
    return True


def main():
    export_needed_refs()
    refs = load_refs()
    df, samples, stats = build_rows(refs)
    df.sort_values(["payer", "network_file", "code", "modifiers", "billing_class", "setting_group",
                    "negotiated_rate", "tin_value"]).to_csv(RATES_CSV, index=False)
    print(f"Wrote {RATES_CSV}: {len(df):,} rows")
    buf = io.StringIO()

    def p(s=""):
        print(s)
        buf.write(s + "\n")
    ok = checks(df, samples, stats, p)
    open(CHECKS_TXT, "w").write(buf.getvalue())
    print(f"\nWrote {CHECKS_TXT}")
    sys.exit(0 if ok else 3)


if __name__ == "__main__":
    main()
