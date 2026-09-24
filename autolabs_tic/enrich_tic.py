#!/usr/bin/env python3
"""Enrich tic_autonomic_rates with provider identity and flags.

1. autonomic_billers.csv - every NPI in MA/NH/RI/CT that billed Medicare
   for 95921-95924 in 2022-2024, from the CMS "Medicare Physician & Other
   Practitioners - by Provider and Service" data. Local copies in
   reference/Medicare_Physician_Other_Practitioners_by_Provider_and_Service_<year>.csv
   are used when present; otherwise the same dataset is queried on
   data.cms.gov (filtered by code and state; raw responses cached in
   reference/cms_prov_svc/).
2. NPI identity from the NPPES monthly full replacement file, streamed from
   the zip (no extraction), for every NPI in provider_refs_needed. NPIs not
   found there are looked up on the NPI Registry API (cached, <= 5/s).
3. Row flags (any NPI of the row's provider group): known_autonomic_biller,
   neurology, idtf, ma_located, hospital_affiliated (+ the rule that
   matched), plus provider_name and, for Harvard Pilgrim, the tax ID's fee
   tier. Written back to output/tic_autonomic_rates.csv.gz.
4. Report -> output/enrich_report.txt.

Usage:  .venv/bin/python enrich_tic.py
"""
import csv
import glob
import gzip
import io
import json
import os
import re
import sys
import time
import zipfile
from collections import Counter, defaultdict

import pandas as pd
import requests

import extract_tic as X
import normalize_tic as N

HERE = X.HERE
OUT = X.OUT
REF = os.path.join(HERE, "reference")
DL = os.path.join(HERE, "downloads")
NPPES_ZIP = os.path.join(DL, "NPPES_Data_Dissemination_September_2026_V2.zip")
NPPES_URL = "https://download.cms.gov/nppes/NPPES_Data_Dissemination_September_2026_V2.zip"
NUCC_CSV = os.path.join(REF, "nucc_taxonomy_261.csv")
REGISTRY = "https://npiregistry.cms.hhs.gov/api/?version=2.1&number={}"
REGISTRY_CACHE = os.path.join(REF, "npi_registry_cache")

AUTONOMIC = ["95921", "95922", "95923", "95924"]
BILLER_STATES = ["MA", "NH", "RI", "CT"]
CMS_DATASETS = {2022: "e650987d-01b7-4f09-b75e-b0b075afbf98",
                2023: "0e9f2f2b-7bf9-451a-912c-e02e654dd725",
                2024: "92396110-2aed-4d63-a6a2-5d6207d46a29"}

# Taxonomy codes (NUCC v26.1). Neurology: the Psychiatry & Neurology
# specialisations for neurology / clinical neurophysiology / neuromuscular
# (and neurology subspecialties), plus PM&R Neuromuscular Medicine.
NEURO_TAXONOMY = {
    "2084N0400X": "Neurology", "2084N0402X": "Child Neurology",
    "2084N0600X": "Clinical Neurophysiology", "2084N0008X": "Neuromuscular Medicine (P&N)",
    "2081N0008X": "Neuromuscular Medicine (PM&R)", "2084V0102X": "Vascular Neurology",
    "2084E0001X": "Epilepsy", "2084B0040X": "Behavioral Neurology & Neuropsychiatry",
    "2084A2900X": "Neurocritical Care",
}
# NUCC has no taxonomy named "IDTF"; CMS's Medicare Provider and Supplier
# Taxonomy Crosswalk maps Medicare specialty 47 "Independent Diagnostic
# Testing Facility (IDTF)" to 293D00000X Laboratories/Physiological Laboratory.
IDTF_TAXONOMY = {"293D00000X"}

KNOWN_HOSPITAL_TINS = {"042697983": "Massachusetts General Hospital",
                       "042312909": "Brigham and Women's Hospital",
                       "042768256": "Brigham and Women's Faulkner Hospital",
                       "020260334": "Wentworth-Douglass Hospital",
                       "042103881": "Beth Israel Deaconess Medical Center"}
HOSPITAL_PATTERNS = [
    r"\bHOSPITALS?\b", r"\bMEDICAL CENTER\b", r"\bMED(ICAL)? CTR\b", r"\bHEALTH ?CARE SYSTEM\b",
    r"\bHEALTH SYSTEM\b", r"\bPHYSICIANS? ORGANI[SZ]ATION\b", r"\bFACULTY\b", r"\bUNIVERSITY\b",
    r"\bACADEMIC\b", r"\bMGPO\b", r"\bHMFP\b", r"\bMASS(ACHUSETTS)? GENERAL\b", r"\bBRIGHAM\b",
    r"\bBETH ISRAEL\b", r"\bLAHEY\b", r"\bUMASS MEMORIAL\b", r"\bBAYSTATE\b", r"\bDANA.?FARBER\b",
    r"\bCAMBRIDGE (HEALTH ALLIANCE|PUBLIC HEALTH COMMISSION)\b", r"\bVAMC\b|\bVA MEDICAL\b",
    r"\bWENTWORTH.?DOUGLASS\b", r"\bPARTNERS HEALTHCARE\b", r"\bLIFESPAN\b", r"\bYALE\b",
    r"\bDARTMOUTH\b",
]
HOSPITAL_RE = [(pat, re.compile(pat, re.I)) for pat in HOSPITAL_PATTERNS]

HPHC_TIERS = [1.000, 1.025, 1.133, 1.212, 1.333]
TIER_TOL = 0.0015                                    # ratio tolerance (tiers are 3-dp)

REPORT = os.path.join(OUT, "enrich_report.txt")
_buf = io.StringIO()


def p(s=""):
    print(s)
    _buf.write(s + "\n")


def digits(s):
    return re.sub(r"\D", "", s or "")


# ------------------------------------------------------------ 1. billers
def cms_rows(year):
    local = os.path.join(REF, f"Medicare_Physician_Other_Practitioners_by_Provider_and_Service_{year}.csv")
    codes = set(AUTONOMIC) | {"93660"}
    if os.path.exists(local):
        with open(local, newline="", encoding="utf-8-sig") as fh:
            for r in csv.DictReader(fh):
                if r.get("HCPCS_Cd") in codes and r.get("Rndrng_Prvdr_State_Abrvtn") in BILLER_STATES:
                    yield r, "local"
        return
    cache = os.path.join(REF, "cms_prov_svc")
    os.makedirs(cache, exist_ok=True)
    for code in sorted(codes):
        for st in BILLER_STATES:
            path = os.path.join(cache, f"{year}_{code}_{st}.json")
            if not os.path.exists(path):
                rows, off = [], 0
                while True:
                    url = (f"https://data.cms.gov/data-api/v1/dataset/{CMS_DATASETS[year]}/data"
                           f"?filter[HCPCS_Cd]={code}&filter[Rndrng_Prvdr_State_Abrvtn]={st}"
                           f"&size=5000&offset={off}")
                    page = X.SESSION.get(url, timeout=120).json()
                    rows += page
                    if len(page) < 5000:
                        break
                    off += 5000
                json.dump(rows, open(path, "w"))
            for r in json.load(open(path)):
                yield r, "data.cms.gov API"


def build_billers():
    recs, sources = [], Counter()
    for year in CMS_DATASETS:
        for r, src in cms_rows(year):
            sources[(year, src)] += 1
            recs.append(dict(year=year, npi=r["Rndrng_NPI"], code=r["HCPCS_Cd"],
                             last_org=r.get("Rndrng_Prvdr_Last_Org_Name", ""),
                             first=r.get("Rndrng_Prvdr_First_Name", ""),
                             entity=r.get("Rndrng_Prvdr_Ent_Cd", ""),
                             ptype=r.get("Rndrng_Prvdr_Type", ""),
                             city=r.get("Rndrng_Prvdr_City", ""),
                             state=r.get("Rndrng_Prvdr_State_Abrvtn", ""),
                             pos=r.get("Place_Of_Srvc", ""),
                             benes=int(float(r.get("Tot_Benes") or 0)),
                             srvcs=float(r.get("Tot_Srvcs") or 0)))
    d = pd.DataFrame(recs)
    auto = d[d.code.isin(AUTONOMIC)]
    rows = []
    for npi, g in auto.groupby("npi"):
        last = g.sort_values("year").iloc[-1]
        name = (f"{last.first} {last.last_org}".strip() if last.entity == "I" else last.last_org)
        row = dict(npi=npi, name=name, entity=last.entity, provider_type=last.ptype,
                   city=last.city, state=last.state,
                   setting="/".join(sorted({"office" if x == "O" else "hospital" for x in g.pos})),
                   codes_billed="|".join(sorted(g.code.unique())))
        for y in CMS_DATASETS:
            gy = g[g.year == y]
            # beneficiaries are per code; max over codes is a lower bound on
            # distinct patients (sums would double count)
            row[f"patients_{y}"] = int(gy.benes.max()) if len(gy) else 0
            row[f"services_{y}"] = int(gy.srvcs.sum()) if len(gy) else 0
        tilt = d[(d.npi == npi) & (d.code == "93660")]
        row["also_billed_93660"] = "Y" if len(tilt) else ""
        rows.append(row)
    b = pd.DataFrame(rows).sort_values(["state", "name"])
    b.to_csv(os.path.join(HERE, "autonomic_billers.csv"), index=False)
    return b, sources


# ------------------------------------------------------------ 2. NPPES
def nucc():
    n = pd.read_csv(NUCC_CSV, dtype=str, keep_default_na=False)
    return {r.Code: (r.Specialization and f"{r.Classification} - {r.Specialization}" or r.Classification)
            for r in n.itertuples()}


def nppes_lookup(npis):
    """Stream npidata_pfile from the NPPES zip; keep only rows for npis."""
    if not os.path.exists(NPPES_ZIP):
        size = int(X.SESSION.head(NPPES_URL, timeout=60).headers["Content-Length"])
        X.download(NPPES_URL, NPPES_ZIP, size, {"bytes_downloaded": 0})
    want = {n.encode() for n in npis}
    out = {}
    t0 = time.time()
    with zipfile.ZipFile(NPPES_ZIP) as z:
        member = next(m for m in z.namelist() if m.startswith("npidata_pfile") and "fileheader" not in m)
        with z.open(member) as raw:
            f = io.BufferedReader(raw, buffer_size=1 << 22)
            header = next(csv.reader([f.readline().decode()]))
            ix = {c: i for i, c in enumerate(header)}
            tax_cols = [(ix[f"Healthcare Provider Taxonomy Code_{k}"],
                         ix[f"Healthcare Provider Primary Taxonomy Switch_{k}"]) for k in range(1, 16)]
            n_lines = 0
            for line in f:
                n_lines += 1
                if line[1:11] not in want:
                    continue
                r = next(csv.reader([line.decode("utf-8", "replace")]))
                taxes = [(r[c], r[s]) for c, s in tax_cols if r[c]]
                primary = next((c for c, s in taxes if s == "Y"), taxes[0][0] if taxes else "")
                out[r[0]] = dict(
                    npi=r[0], entity_type={"1": "individual", "2": "organization"}.get(r[ix["Entity Type Code"]], ""),
                    org_name=r[ix["Provider Organization Name (Legal Business Name)"]],
                    other_org_name=r[ix["Provider Other Organization Name"]],
                    last_name=r[ix["Provider Last Name (Legal Name)"]],
                    first_name=r[ix["Provider First Name"]],
                    credential=r[ix["Provider Credential Text"]],
                    primary_taxonomy=primary,
                    taxonomies="|".join(c for c, _ in taxes),
                    city=r[ix["Provider Business Practice Location Address City Name"]],
                    state=r[ix["Provider Business Practice Location Address State Name"]],
                    zip5=r[ix["Provider Business Practice Location Address Postal Code"]][:5],
                    parent_org_lbn=r[ix["Parent Organization LBN"]],
                    parent_org_tin=r[ix["Parent Organization TIN"]],
                    deactivation_date=r[ix["NPI Deactivation Date"]],
                    source="NPPES full file 2026-09")
    print(f"   NPPES: scanned {n_lines:,} records in {time.time() - t0:.0f}s; matched {len(out):,} of {len(want):,}")
    return out


def registry_lookup(npis):
    """NPI Registry API for NPIs missing from NPPES (cached, <= 5 req/s)."""
    os.makedirs(REGISTRY_CACHE, exist_ok=True)
    out, last = {}, 0.0
    for npi in npis:
        path = os.path.join(REGISTRY_CACHE, f"{npi}.json")
        if not os.path.exists(path):
            for attempt in range(4):
                wait = 0.2 - (time.time() - last)
                if wait > 0:
                    time.sleep(wait)
                last = time.time()
                try:
                    r = X.SESSION.get(REGISTRY.format(npi), timeout=30)
                    r.raise_for_status()
                    json.dump(r.json(), open(path, "w"))
                    break
                except (requests.RequestException, ValueError):
                    time.sleep(2 ** attempt)
            else:
                continue
        res = (json.load(open(path)).get("results") or [])
        if not res:
            continue
        b = res[0]
        basic = b.get("basic", {})
        loc = next((a for a in b.get("addresses", []) if a.get("address_purpose") == "LOCATION"), {})
        tx = b.get("taxonomies", [])
        prim = next((t for t in tx if t.get("primary")), tx[0] if tx else {})
        out[npi] = dict(npi=npi, entity_type="organization" if b.get("enumeration_type") == "NPI-2" else "individual",
                        org_name=basic.get("organization_name", ""), other_org_name="",
                        last_name=basic.get("last_name", ""), first_name=basic.get("first_name", ""),
                        credential=basic.get("credential", ""), primary_taxonomy=prim.get("code", ""),
                        taxonomies="|".join(t.get("code", "") for t in tx), city=loc.get("city", ""),
                        state=loc.get("state", ""), zip5=(loc.get("postal_code") or "")[:5],
                        parent_org_lbn=basic.get("parent_organization_legal_business_name", ""),
                        parent_org_tin="", deactivation_date="", source="NPI Registry API")
    return out


# ------------------------------------------------------------ BCBS names
def bcbs_tin_names():
    path = os.path.join(OUT, "bcbs_tin_names.csv")
    if os.path.exists(path):
        d = pd.read_csv(path, dtype=str, keep_default_na=False)
        return d.groupby("tin_value").business_name.apply(lambda s: sorted(set(s))).to_dict()
    names = defaultdict(set)
    sel = [r for r in csv.DictReader(open(os.path.join(HERE, "selection.csv")))
           if r["process"] == "Y" and r["payer"].startswith("Blue Cross")]
    X.SUBSTRINGS = ()                                    # provider_references only

    def on_ref(raw):
        for pg in json.loads(raw).get("provider_groups") or []:
            t = pg.get("tin") or {}
            if t.get("business_name"):
                names[str(t.get("value"))].add(t["business_name"].strip())
    for rec in sel:
        log = {"bytes_downloaded": 0, "bytes_decompressed": 0}
        sc = X.Scanner(on_ref, lambda raw, off: None)
        for seg, final in X.segments(X.byte_source(rec, log), log):
            sc.feed(seg, final)
    pd.DataFrame([(t, n) for t, ns in names.items() for n in sorted(ns)],
                 columns=["tin_value", "business_name"]).to_csv(path, index=False)
    return {t: sorted(ns) for t, ns in names.items()}


# ------------------------------------------------------------ HPHC tiers
def hphc_tiers(df):
    """Harvard Pilgrim tier of every rate row.

    A multi-specialty tax ID carries several rates per code (one per group
    of its clinicians), so the tier belongs to the rate row, not the TIN.
    For each (code, modifier set) the base is the rate b that puts the most
    distinct (file, TIN, rate) rows on b x {1.000, 1.025, 1.133, 1.212,
    1.333}; each row is then T1..T5 or off-grid."""
    h = df[(df.payer == "Harvard Pilgrim Health Care") & (df.negotiated_type == "fee schedule")
           & df.modifiers.isin(["", "26", "TC"])]
    bases = {}
    for (code, mods), g in h.groupby(["code", "modifiers"]):
        rates = g.drop_duplicates(["network_file", "tin_value", "negotiated_rate"]).negotiated_rate.astype(float)
        vc = rates.value_counts()
        best = (0, None)
        for r in vc.index[:12]:
            for t in HPHC_TIERS:
                b = r / t
                ok = sum(int(vc[((vc.index / b) - t2).__abs__() <= TIER_TOL].sum()) for t2 in HPHC_TIERS)
                if ok > best[0]:
                    best = (ok, b)
        b = best[1]
        t1 = vc[((vc.index / b) - 1).__abs__() <= TIER_TOL]
        bases[(code, mods)] = (b, float(t1.index[0]) if len(t1) else round(b, 2), best[0], int(vc.sum()))

    def tier(code, mods, rate):
        if (code, mods) not in bases or rate == "":
            return ""
        q = float(rate) / bases[(code, mods)][0]
        k = next((i + 1 for i, t in enumerate(HPHC_TIERS) if abs(q - t) <= TIER_TOL), None)
        return f"T{k}" if k else "off-grid"
    return tier, bases


# ------------------------------------------------------------ main
def main():
    p("== 1. Medicare autonomic billers (95921-95924) in MA/NH/RI/CT, 2022-2024")
    billers, sources = build_billers()
    for (y, src), n in sorted(sources.items()):
        p(f"   {y}: {n} provider-code rows from {src}")
    p(f"   {len(billers)} NPIs -> autonomic_billers.csv; by state: "
      + ", ".join(f"{k} {v}" for k, v in billers.state.value_counts().items()))
    p(billers.to_string(index=False, max_colwidth=40))
    biller_npis = set(billers.npi)

    p("\n== 2. NPI identity (NPPES full replacement file, streamed from zip)")
    refs = N.load_refs()
    all_npis = sorted({n for grp in refs.values() for ns in grp.values() for n in ns})
    info = nppes_lookup(all_npis)
    missing = [n for n in all_npis if n not in info]
    deact = [n for n, v in info.items() if v["deactivation_date"] and not v["state"]]
    p(f"   NPIs in rate groups: {len(all_npis):,}; found in NPPES: {len(info):,}; "
      f"missing: {len(missing)}; deactivated (no data): {len(deact)}")
    if missing:
        reg = registry_lookup(missing)
        info.update(reg)
        p(f"   NPI Registry API resolved {len(reg)} of {len(missing)} missing NPIs")
    unresolved = [n for n in all_npis if n not in info] + deact
    tax = nucc()
    for v in info.values():
        v["primary_taxonomy_desc"] = tax.get(v["primary_taxonomy"], "")
        codes = set(v["taxonomies"].split("|")) - {""}
        v["neurology"] = bool(codes & set(NEURO_TAXONOMY))
        v["idtf"] = bool(codes & IDTF_TAXONOMY)
        v["ma"] = v["state"] == "MA"
        v["biller"] = v["npi"] in biller_npis
    npi_df = pd.DataFrame(info.values()).drop(columns=["ma", "biller"])
    npi_df.to_csv(os.path.join(OUT, "npi_enrichment.csv.gz"), index=False)

    p("\n== 3. Flags")
    # keyed by TIN digits so Harvard Pilgrim rows (no dash) pick up Blue Cross
    # business names for the same tax ID
    names_bcbs = defaultdict(list)
    for t, ns in bcbs_tin_names().items():
        names_bcbs[digits(t)] += ns
    df, samples, stats, npis_full = N.build_rows(refs, keep_npis=True)
    tier_of, bases = hphc_tiers(df)
    flags = defaultdict(list)
    hosp_hits = Counter()
    for tin_type, tin, npis in zip(df.tin_type, df.tin_value, npis_full):
        vs = [info[n] for n in npis if n in info]
        flags["known_autonomic_biller"].append("Y" if any(v["biller"] for v in vs) else "")
        flags["neurology"].append("Y" if any(v["neurology"] for v in vs) else "")
        flags["idtf"].append("Y" if any(v["idtf"] for v in vs) else "")
        flags["ma_located"].append("Y" if any(v["ma"] for v in vs) else "")
        org_names = sorted({v["org_name"] for v in vs if v["entity_type"] == "organization" and v["org_name"]})
        cands = (names_bcbs.get(digits(tin), []) if tin_type != "npi" else []) + org_names + sorted({v["parent_org_lbn"] for v in vs if v["parent_org_lbn"]})
        match = ""
        if tin_type != "npi" and digits(tin) in KNOWN_HOSPITAL_TINS:
            match = f"tin:{KNOWN_HOSPITAL_TINS[digits(tin)]}"
        elif any(digits(v["parent_org_tin"]) in KNOWN_HOSPITAL_TINS for v in vs):
            match = "parent_org_tin"
        else:
            for pat, rx in HOSPITAL_RE:
                hit = next((c for c in cands if rx.search(c)), None)
                if hit:
                    match = f"name:{pat} ({hit[:40]})"
                    break
        if match:
            hosp_hits[match.split(" (")[0]] += 1
        flags["hospital_affiliated"].append("Y" if match else "")
        flags["hospital_match"].append(match)
        if cands:
            pname = cands[0]
        elif len(vs) == 1 and vs[0]["entity_type"] == "individual":
            pname = f"{vs[0]['first_name']} {vs[0]['last_name']}".strip()
        else:
            pname = ""
        flags["provider_name"].append(pname)
        flags["biller_npis"].append("|".join(n for n in npis if n in biller_npis))
    for k, v in flags.items():
        df[k] = v
    is_h = df.payer == "Harvard Pilgrim Health Care"
    df["hphc_rate_tier"] = [tier_of(c, m, r) if h and nt == "fee schedule" else ""
                            for h, c, m, r, nt in zip(is_h, df.code, df.modifiers, df.negotiated_rate,
                                                      df.negotiated_type)]
    tin_tiers = df[is_h & (df.hphc_rate_tier != "")].groupby("tin_value").hphc_rate_tier.apply(
        lambda s: ",".join(sorted(set(s), key=lambda x: (x == "off-grid", x))))
    df["hphc_tin_tiers"] = df.tin_value.map(tin_tiers).where(is_h, "").fillna("")
    out = df.drop(columns=["biller_npis"]).sort_values(
        ["payer", "network_file", "code", "modifiers", "billing_class", "setting_group",
         "negotiated_rate", "tin_value"])
    out.to_csv(N.RATES_CSV, index=False)
    p(f"   wrote {os.path.relpath(N.RATES_CSV, HERE)} ({len(out):,} rows) with flag columns")

    # ---- report
    p("\n== 4a. Counts by flag and payer (rows / distinct tax IDs)")
    for f in ["known_autonomic_biller", "neurology", "idtf", "ma_located", "hospital_affiliated"]:
        for payer, g in df.groupby("payer"):
            y = g[g[f] == "Y"]
            p(f"   {f:24} {payer[:40]:40} rows {len(y):9,} of {len(g):9,}   TINs {y.tin_value.nunique():6,} "
              f"of {g.tin_value.nunique():6,}")
    p("\n   hospital_affiliated rules that fired (rows):")
    for k, n in hosp_hits.most_common():
        p(f"     {n:9,}  {k}")
    p("   name patterns used: " + "; ".join(HOSPITAL_PATTERNS))
    p("   neurology taxonomies: " + ", ".join(f"{k} {v}" for k, v in NEURO_TAXONOMY.items()))
    p("   idtf taxonomy: 293D00000X (CMS crosswalk: Medicare specialty 47 IDTF -> Laboratories/Physiological Laboratory)")

    p("\n== 4b. Harvard Pilgrim fee tiers (tier ratios " + ", ".join(f"{t:.3f}" for t in HPHC_TIERS) + ")")
    p("   base (T1) rate per code/modifier; rows = distinct (file, TIN, rate) rows on the tier grid / all:")
    for (c, m), (b, t1, ok, tot) in sorted(bases.items()):
        p(f"     {c} {m or 'global':6} T1 {t1:8.2f}  on-grid {ok:7,} / {tot:7,} ({ok / tot:.1%})  "
          + "  ".join(f"T{i + 1} {b * t:.2f}" for i, t in enumerate(HPHC_TIERS)))
    ht = df[is_h & (df.hphc_rate_tier != "")]
    tt = ht.groupby("tin_value").hphc_rate_tier.apply(lambda s: frozenset(s))
    p(f"\n   {len(tt):,} Harvard Pilgrim tax IDs by the tiers their rate rows carry (top 12 combinations):")
    for combo, n in tt.map(lambda s: ",".join(sorted(s, key=lambda x: (x == 'off-grid', x)))).value_counts().head(12).items():
        p(f"     {n:6,}  {combo}")
    # NPI-level view on office global 95924 rows
    sel = is_h & (df.code == "95924") & (df.modifiers == "") & (df.setting_group == "office") \
        & (df.hphc_rate_tier != "")
    recs = set()
    for i in sel[sel].index:
        for n in npis_full[i]:
            recs.add((n, df.at[i, "hphc_rate_tier"], df.at[i, "hospital_affiliated"] or "N",
                      "Y" if n in biller_npis else "N"))
    nv = pd.DataFrame(list(recs), columns=["npi", "tier", "hospital_affiliated", "known_autonomic_biller"])
    nv["state"] = nv.npi.map(lambda n: (info.get(n) or {}).get("state") or "?")
    nv["taxonomy"] = nv.npi.map(lambda n: (info.get(n) or {}).get("primary_taxonomy_desc") or "?")
    nv.to_csv(os.path.join(OUT, "hphc_npi_tiers_95924.csv"), index=False)
    p(f"\n   NPI-level (office global 95924 rows, all HPHC files pooled): {nv.npi.nunique():,} NPIs, "
      f"{len(nv):,} NPI x tier x flag combinations")
    for dim, top in [("state", 10), ("taxonomy", 20), ("hospital_affiliated", None),
                     ("known_autonomic_biller", None)]:
        ct = pd.crosstab(nv[dim], nv.tier)
        if top:
            ct = ct.loc[ct.sum(axis=1).sort_values(ascending=False).index[:top]]
        p(f"\n   tier x {dim} (NPIs):")
        p(ct.to_string())

    p("\n== 4c. Every rate row for known autonomic billers (collapsed over network files)")
    kb = df[df.known_autonomic_biller == "Y"]
    g = kb.groupby(["payer", "tin_value", "provider_name", "biller_npis", "code", "modifiers",
                    "billing_class", "setting_group", "negotiated_type", "negotiated_rate",
                    "negotiated_percentage"]).network_file.nunique().reset_index(name="n_files")
    bname = dict(zip(billers.npi, billers.name))
    g["billers"] = g.biller_npis.map(lambda s: "; ".join(f"{bname.get(n, n)}" for n in s.split("|")))
    pd.set_option("display.width", 250)
    pd.set_option("display.max_rows", 5000)
    pd.set_option("display.max_colwidth", 45)
    p(f"   {len(kb):,} rows -> {len(g):,} distinct (payer x TIN x code x modifier x setting x rate)")
    p(g.drop(columns=["biller_npis"]).assign(modifiers=g.modifiers.replace("", "global"))
      .to_string(index=False))

    p("\n== 4d. NPIs that could not be resolved")
    p(f"   {len(unresolved)} NPIs: " + (", ".join(unresolved[:200]) if unresolved else "none"))
    open(REPORT, "w").write(_buf.getvalue())
    print(f"\nWrote {REPORT}")


if __name__ == "__main__":
    main()
