#!/usr/bin/env python3
"""Print the network inventory and write selection.csv (process = Y/N).

Reads output/network_inventory.csv (from toc_inventory.py), prints it
sorted by payer then number_of_reporting_plans (desc) with per-payer size
totals, flags the files that most likely hold each payer's main
Massachusetts commercial networks, and writes selection.csv.

selection.csv is meant to be hand-edited before anything is downloaded.

Usage:  .venv/bin/python select_networks.py [--out DIR]
"""
import argparse
import os
import re

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))

# File-name code -> reason. Codes are the part of the file name after the
# date, e.g. "A008-P1". P1 = issuer's own fully-insured book (TOC entity
# type HEALTH INSURANCE ISSUER, HIOS-keyed plans, group + individual);
# FS = the same product sold to employer groups (TOC entity type THIRD
# PARTY ADMINISTRATOR, EIN-keyed employer plans).
FLAG = {
    "A008-P1": "HPHC flagship 'HMO' network, issuer book (HIOS 36046 alongside 'Focus Network - MA HMO'; group+individual)",
    "A008-FS": "HPHC 'HMO' network for employer groups; most widely shared file (37 plans / 36 employer TOCs)",
    "A002-P1": "'Harvard Pilgrim PPO' network, issuer book",
    "A002-FS": "'Harvard Pilgrim PPO' network for employer groups (22 plans incl. BC, Brandeis, BILH)",
    "A001-FS": "'Access America' open-access network for employer groups (19 plans incl. MA GIC, house acct)",
    "TuftsHealthPublicPlans_DirectNonSubsidizedGroup": "Tufts Health Direct small-group network - only Tufts commercial network published (27,680 plans)",
    "TuftsHealthPublicPlans_DirectNonSubsidizedIndividual": "Tufts Health Direct individual (Health Connector, unsubsidized)",
    "TuftsHealthPublicPlans_DirectSubsidizedIndividual": "Tufts Health Direct individual (ConnectorCare subsidized); may carry different rates",
}
NOT_REASONS = [
    (r"UNITEDHEALTHCARE", "UnitedHealthcare national wrap network for out-of-area care (UHC rates, not HPHC MA contracts); ~10.5-10.8 GB"),
    (r"Dental", "Dental network, not relevant; HEAD returns 404"),
    (r"A0(35|43|61|87|88|25|75)-", "New Hampshire / Maine product (ElevateHealth, NH Local, LP)"),
    (r"A081-", "Maine product (Maine's Choice Plus)"),
    (r"A09[1]-", "Rhode Island product (Ocean State Access America)"),
    (r"A0(77|78|79|99)-|A100-", "BILH employer-specific custom network"),
    (r"A09[2389]-|A097-|A101-|A074-", "Single-employer custom network (Cape Cod Healthcare, Clergy, UNITE HERE, HMFP)"),
    (r"A089-|A090-", "GIC-only custom product (Quality HMO / Explorer POS)"),
    (r"A013-", "Focus Network - MA HMO: limited-network MA product; candidate if narrow-network rates wanted"),
    (r"A014-|A015-", "ChoiceNet HMO/PPO: tiered/select network; candidate secondary network"),
    (r"A010-|A020-", "Best Buy HSA variants of the PPO/HMO networks; likely same contracts as A002/A008"),
    (r"A067-|A068-|A09[456]-", "Flex/PPO Access variants; secondary product networks"),
    (r"A102-", "National Access EPO"),
    (r"A009-|A027-|A031-|A001-P1", "POS/PPO variants with few plans; secondary"),
]


def code(url):
    fn = url.rsplit("/", 1)[-1]
    fn = re.sub(r"^\d{4}-\d{2}-\d{2}_", "", fn)
    return re.sub(r"_in-network-rates.*$", "", fn)


def reason_for(url):
    c = code(url)
    if c in FLAG:
        return "Y", FLAG[c]
    for pat, why in NOT_REASONS:
        if re.search(pat, url):
            return "N", why
    return "N", "Minor / employer-specific network"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=f"{HERE}/output")
    args = ap.parse_args()

    d = pd.read_csv(f"{args.out}/network_inventory.csv")
    d["file_code"] = d.location_url.map(code)
    d[["process", "reason"]] = d.location_url.map(reason_for).apply(pd.Series)
    d = d.sort_values(["payer", "number_of_reporting_plans"], ascending=[True, False])

    pd.set_option("display.width", 250)
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_colwidth", 70)
    for payer, g in d.groupby("payer", sort=True):
        show = g.assign(size_mb=(g.size_bytes / 1e6).round(1))[
            ["process", "file_code", "file_description", "number_of_reporting_plans",
             "plan_market_types", "n_employer_tocs", "size_mb", "last_modified"]]
        print(f"\n=== {payer}: {len(g)} files, total {g.size_bytes.sum() / 1e9:.2f} GB "
              f"({g.size_bytes.isna().sum()} without size); flagged Y: "
              f"{(g.process == 'Y').sum()} files, {g.size_bytes[g.process == 'Y'].sum() / 1e9:.2f} GB")
        print(show.to_string(index=False))

    print("\n=== Flagged files (process = Y)")
    for _, r in d[d.process == "Y"].iterrows():
        print(f"  {r.payer[:26]:26} {r.file_code:52} {r.size_bytes / 1e6:8.1f} MB  {r.reason}")

    sel = d[["process", "payer", "file_code", "file_description", "number_of_reporting_plans",
             "plan_market_types", "example_plan_names", "size_bytes", "last_modified",
             "reason", "location_url"]]
    sel.to_csv(f"{HERE}/selection.csv", index=False)
    print(f"\nWrote {HERE}/selection.csv ({len(sel)} rows, {(sel.process == 'Y').sum()} flagged Y)")


if __name__ == "__main__":
    main()
