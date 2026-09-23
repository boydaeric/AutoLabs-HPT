#!/usr/bin/env python3
"""QA report for hpt_autonomic_rates.csv (prints to stdout).

Usage:  python check_rates.py [--rates hpt_autonomic_rates.csv] [--in DIR] [--manifest manifest.csv]
"""
import argparse
import csv
import json
import os
import textwrap

import pandas as pd

CODES = ["95921", "95922", "95923", "95924", "93660"]
MIN_PAYERS = 10


def h(title):
    print(f"\n{'=' * 100}\n{title}\n{'=' * 100}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rates", default="hpt_autonomic_rates.csv")
    ap.add_argument("--in", dest="indir", default=".")
    ap.add_argument("--manifest", default="manifest.csv")
    ap.add_argument("--samples", type=int, default=10)
    args = ap.parse_args()

    df = pd.read_csv(args.rates, dtype=str, keep_default_na=False)
    hospitals = [r["hospital"] for r in csv.DictReader(open(args.manifest))]
    has_payer = (df.payer_name != "") | (df.plan_name != "")
    pd.set_option("display.width", 200, "display.max_columns", 50, "display.max_colwidth", 60)

    h("ROW COUNTS BY HOSPITAL x CODE")
    ct = pd.crosstab(pd.Categorical(df.hospital, hospitals), pd.Categorical(df.code, CODES),
                     margins=True, dropna=False)
    print(ct)

    h("DISTINCT PAYERS / PLANS PER HOSPITAL (all codes)")
    p = df[has_payer].groupby("hospital").agg(payers=("payer_name", "nunique"),
                                              payer_plan_pairs=("plan_name", lambda s: 0))
    p["payer_plan_pairs"] = df[has_payer].groupby("hospital").apply(
        lambda g: g[["payer_name", "plan_name"]].drop_duplicates().shape[0])
    print(p.reindex(hospitals).fillna(0).astype(int))

    h("RATE TYPE SHARE (payer rows; type = first of dollar > percentage > algorithm present)")
    pr = df[has_payer]
    share = pd.crosstab(pr.hospital, pr.rate_type, margins=True)
    print(share)
    print("\nshare of all payer rows:")
    print((pr.rate_type.value_counts(normalize=True) * 100).round(1).astype(str) + "%")
    print("\nfields populated on payer rows (a row can carry several):")
    for c in ["standard_charge_dollar", "standard_charge_percentage", "standard_charge_algorithm",
              "estimated_amount", "median_amount", "percentile_10th", "percentile_90th", "allowed_count"]:
        print(f"  {c:28s} {(pr[c] != '').sum():4d} / {len(pr)}")
    print(f"  implied_flag=TRUE (pct x gross)  {(df.implied_flag == 'TRUE').sum()}")

    h("CATEGORICAL NORMALISATION (raw -> normalised)")
    for c in ["billing_class", "setting", "methodology"]:
        m = df.groupby([f"raw_{c}", c], dropna=False).size().reset_index(name="rows")
        print(f"\n{c}:\n{m.to_string(index=False)}")

    h(f"PER HOSPITAL x CODE DETAIL (flag: < {MIN_PAYERS} distinct payers)")
    for hosp in hospitals:
        for code in CODES:
            g = df[(df.hospital == hosp) & (df.code == code)]
            if g.empty:
                print(f"\n{hosp} | {code}: NO ROWS in MRF")
                continue
            gp = g[(g.payer_name != "") | (g.plan_name != "")]
            npay, nplan = gp.payer_name.nunique(), gp[["payer_name", "plan_name"]].drop_duplicates().shape[0]
            flag = "  <-- FLAG: fewer than 10 payers" if npay < MIN_PAYERS else ""
            print(f"\n{hosp} | {code}: {len(g)} rows = {len(gp)} with payer + {len(g) - len(gp)} "
                  f"without payer | {npay} payers, {nplan} payer/plan pairs{flag}")
            for c in ["billing_class", "setting", "modifiers"]:
                vc = g[c].replace("", "(blank)").value_counts().to_dict()
                print(f"    {c:14s} {vc}")

    h("MGH: WHY 95924 HAS 17 ROWS BUT 95923 HAS 9")
    mgh = df[df.hospital == "Massachusetts General Hospital"]
    key = ["payer_name", "plan_name", "setting", "modifiers", "billing_class"]
    a = mgh[mgh.code == "95923"][key + ["standard_charge_dollar", "methodology"]]
    b = mgh[mgh.code == "95924"][key + ["standard_charge_dollar", "methodology"]]
    for lbl, g in (("95923", a), ("95924", b)):
        print(f"\n{lbl}: {len(g)} rows, {g.payer_name.nunique()} payers, "
              f"{g[['payer_name', 'plan_name']].drop_duplicates().shape[0]} payer/plan pairs, "
              f"settings={g.setting.value_counts().to_dict()}, modifiers={g.modifiers.replace('', '(none)').value_counts().to_dict()}")
    pa = set(map(tuple, a[["payer_name", "plan_name"]].values))
    pb = set(map(tuple, b[["payer_name", "plan_name"]].values))
    print("\npayer/plan pairs only in 95924:")
    for x in sorted(pb - pa):
        print("   ", x, b[(b.payer_name == x[0]) & (b.plan_name == x[1])].setting.tolist())
    print("payer/plan pairs only in 95923:")
    for x in sorted(pa - pb):
        print("   ", x)
    print("pairs in both:", len(pa & pb))
    both = b.merge(a, on=["payer_name", "plan_name"], suffixes=("_95924", "_95923"))
    print(both[["payer_name", "plan_name", "setting_95923", "setting_95924",
                "standard_charge_dollar_95923", "standard_charge_dollar_95924"]].to_string(index=False))

    h(f"SAMPLE ROWS: RAW RECORD vs NORMALISED ({args.samples} per hospital)")
    raw_cache = {}
    show = ["code", "code_type", "description", "modifiers", "setting", "billing_class", "gross_charge",
            "discounted_cash", "deidentified_min", "deidentified_max", "payer_name", "plan_name",
            "standard_charge_dollar", "standard_charge_percentage", "standard_charge_algorithm",
            "methodology", "estimated_amount", "median_amount", "percentile_10th", "percentile_90th",
            "allowed_count", "additional_notes", "implied_dollar", "implied_flag", "rate_type"]
    for hosp in hospitals:
        g = df[df.hospital == hosp]
        if g.empty:
            print(f"\n### {hosp}: no rows")
            continue
        # spread samples across codes and payer/no-payer rows
        g = g.assign(_k=g.code + g.rate_type).groupby("_k", group_keys=False).head(3)
        g = g.head(args.samples) if len(g) >= args.samples else pd.concat(
            [g, df[df.hospital == hosp].drop(g.index, errors="ignore")]).head(args.samples)
        print(f"\n### {hosp} ({len(g)} samples)")
        for _, r in g.iterrows():
            fname, ref = r.source_ref.split(":", 1)
            lineno = int(ref.split(".")[0].split()[0].removeprefix("line"))
            if fname not in raw_cache:
                raw_cache[fname] = [json.loads(x)["record"] for x in open(os.path.join(args.indir, fname))]
            raw = raw_cache[fname][lineno - 1]
            if "standard_charges" in raw:  # JSON: show only the referenced branch
                si = int(ref.split("standard_charges[")[1].split("]")[0])
                sc = dict(raw["standard_charges"][si])
                if "payers_information[" in ref:
                    pi = int(ref.split("payers_information[")[1].split("]")[0])
                    sc["payers_information"] = [sc["payers_information"][pi]]
                raw = {**{k: v for k, v in raw.items() if k != "standard_charges"},
                       "standard_charges": [sc]}
                raw_lines = json.dumps(raw, indent=1).splitlines()
            else:
                raw_lines = [f"{k}: {v}" for k, v in raw.items() if v != ""]
            norm_lines = [f"{c}: {r[c]}" for c in show if r[c] != ""]
            print(f"\n--- {r.source_ref}")
            W = 70
            wrap = lambda L: [seg for l in L for seg in (textwrap.wrap(l, W, subsequent_indent='    ') or [''])]
            L, R = wrap(raw_lines), wrap(norm_lines)
            print(f"{'RAW':<{W}} | NORMALISED")
            for i in range(max(len(L), len(R))):
                print(f"{(L[i] if i < len(L) else ''):<{W}} | {R[i] if i < len(R) else ''}")


if __name__ == "__main__":
    main()
