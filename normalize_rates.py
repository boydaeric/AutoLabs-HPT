#!/usr/bin/env python3
"""Normalise raw_*.jsonl (from extract_codes.py) into hpt_autonomic_rates.csv.

One row per hospital x code x modifier x setting x billing class x payer x
plan (plus payer-less rows for gross/cash-only charges). Only values present
in the MRF are copied; the one derived value is implied_dollar, which for a
percentage-of-charges rate without a dollar amount is gross_charge x pct/100
taken from the SAME row (implied_flag=TRUE). Nothing is borrowed across rows.

Handles:
  * JSON v2.x/v3.x: standard_charge_information[].standard_charges[]
    .payers_information[]
  * CSV tall v2.x/v3.x: one row per payer/plan
  * CSV wide: payer/plan encoded in column names
    (standard_charge|<payer>|<plan>|<field>)

Usage:  python normalize_rates.py [--in DIR] [--out hpt_autonomic_rates.csv]
"""
import argparse
import csv
import difflib
import glob
import json
import os
import re
import sys

from extract_codes import code_matches, norm_col

COLUMNS = [
    "hospital", "mrf_version", "mrf_last_updated", "code", "code_type", "description",
    "modifiers", "setting", "billing_class", "gross_charge", "discounted_cash",
    "deidentified_min", "deidentified_max", "payer_name", "plan_name",
    "standard_charge_dollar", "standard_charge_percentage", "standard_charge_algorithm",
    "methodology", "estimated_amount", "median_amount", "percentile_10th",
    "percentile_90th", "allowed_count", "additional_notes",
    "implied_dollar", "implied_flag", "rate_type",
    "raw_setting", "raw_billing_class", "raw_methodology",
    "source_format", "source_ref",
]

# Canonical vocabularies (CMS template values) and known aliases.
SETTINGS = {"inpatient": "inpatient", "outpatient": "outpatient", "both": "both",
            "ip": "inpatient", "op": "outpatient"}
BILLING_CLASSES = {"facility": "facility", "professional": "professional", "both": "both",
                   "hospital": "facility", "institutional": "facility", "pro": "professional"}
METHODOLOGIES = {
    "case rate": "case rate", "fee schedule": "fee schedule",
    "percent of total billed charges": "percent of total billed charges",
    "percentage of total billed charges": "percent of total billed charges",
    "percent of billed charges": "percent of total billed charges",
    "per diem": "per diem", "other": "other",
}


def canon(value, vocab):
    """Case/spacing/spelling-insensitive map onto a vocabulary. Unknown
    values are returned lower-cased with a '?' prefix so they stand out."""
    v = re.sub(r"[\s_\-]+", " ", str(value or "").strip().lower())
    if not v:
        return ""
    if v in vocab:
        return vocab[v]
    close = difflib.get_close_matches(v, list(vocab), n=1, cutoff=0.8)
    return vocab[close[0]] if close else f"?{v}"


def s(v):
    """Stringify a source value without reformatting it."""
    if v is None:
        return ""
    if isinstance(v, float):
        return repr(v).removesuffix(".0") if v.is_integer() else repr(v)
    if isinstance(v, (list, tuple)):
        return "|".join(s(x) for x in v)
    if isinstance(v, dict):
        return json.dumps(v, ensure_ascii=False)
    return str(v).strip()


def num(v):
    try:
        return float(str(v).replace(",", "").replace("$", "").replace("%", "").strip())
    except (TypeError, ValueError):
        return None


def finish(row):
    """Normalise categorical fields; derive implied_dollar and rate_type."""
    row["raw_setting"], row["raw_billing_class"], row["raw_methodology"] = (
        row["setting"], row["billing_class"], row["methodology"])
    row["setting"] = canon(row["setting"], SETTINGS)
    row["billing_class"] = canon(row["billing_class"], BILLING_CLASSES)
    row["methodology"] = canon(row["methodology"], METHODOLOGIES)

    dollar, pct, gross = (num(row["standard_charge_dollar"]),
                          num(row["standard_charge_percentage"]), num(row["gross_charge"]))
    if not row["payer_name"] and not row["plan_name"]:
        row["rate_type"] = "no payer (gross/cash only)"
    elif dollar is not None:
        row["rate_type"] = "dollar"
    elif pct is not None:
        row["rate_type"] = "percentage"
    elif row["standard_charge_algorithm"]:
        row["rate_type"] = "algorithm"
    else:
        row["rate_type"] = "none"

    if dollar is not None:
        row["implied_dollar"], row["implied_flag"] = row["standard_charge_dollar"], "FALSE"
    elif pct is not None and gross is not None:
        row["implied_dollar"], row["implied_flag"] = f"{gross * pct / 100:.2f}", "TRUE"
    return row


def base_row(line):
    h = line.get("header") or {}
    ver = next((v for k, v in h.items() if norm_col(k) == "version"), "")
    upd = next((v for k, v in h.items() if norm_col(k) == "last_updated_on"), "")
    r = dict.fromkeys(COLUMNS, "")
    r.update(hospital=line["hospital"], mrf_version=s(ver), mrf_last_updated=s(upd),
             source_format=line.get("format", ""))
    return r


def join_notes(*parts):
    return " | ".join(p for p in (s(x) for x in parts) if p)


# --------------------------------------------------------------------------
def from_json(line, lineno):
    rec = line["record"]
    targets = [(s(c.get("code")), s(c.get("type"))) for c in rec.get("code_information") or []
               if isinstance(c, dict) and code_matches(c.get("code"))]
    for code, ctype in targets:
        for si, sc in enumerate(rec.get("standard_charges") or []):
            mods = sc.get("modifier_code", sc.get("modifiers", ""))
            common = dict(
                code=code, code_type=ctype, description=s(rec.get("description")),
                modifiers=s(mods), setting=s(sc.get("setting")),
                billing_class=s(sc.get("billing_class")),
                gross_charge=s(sc.get("gross_charge")),
                discounted_cash=s(sc.get("discounted_cash")),
                deidentified_min=s(sc.get("minimum")), deidentified_max=s(sc.get("maximum")),
            )
            payers = sc.get("payers_information") or []
            if not payers:
                r = base_row(line)
                r.update(common, additional_notes=join_notes(sc.get("additional_generic_notes")),
                         source_ref=f"line{lineno}.standard_charges[{si}]")
                yield finish(r)
            for pi, p in enumerate(payers):
                r = base_row(line)
                r.update(common,
                         payer_name=s(p.get("payer_name")), plan_name=s(p.get("plan_name")),
                         standard_charge_dollar=s(p.get("standard_charge_dollar")),
                         standard_charge_percentage=s(p.get("standard_charge_percentage")),
                         standard_charge_algorithm=s(p.get("standard_charge_algorithm")),
                         methodology=s(p.get("methodology")),
                         estimated_amount=s(p.get("estimated_amount")),
                         median_amount=s(p.get("median_amount")),
                         percentile_10th=s(p.get("10th_percentile")),
                         percentile_90th=s(p.get("90th_percentile")),
                         allowed_count=s(p.get("count")),
                         additional_notes=join_notes(sc.get("additional_generic_notes"),
                                                     p.get("additional_payer_notes")),
                         source_ref=f"line{lineno}.standard_charges[{si}].payers_information[{pi}]")
                yield finish(r)


def csv_get(rec, *names):
    """Value of the first column whose normalised name matches."""
    idx = {norm_col(k): k for k in rec}
    for n in names:
        if n in idx:
            return s(rec[idx[n]])
    return ""


def from_csv(line, lineno):
    rec = line["record"]
    # Target codes from code|N / code|N|type pairs.
    targets = []
    for k, v in rec.items():
        m = re.fullmatch(r"code\|(\d+)", norm_col(k))
        if m and code_matches(v):
            targets.append((s(v), csv_get(rec, f"code|{m.group(1)}|type")))
    common = dict(
        description=csv_get(rec, "description"), modifiers=csv_get(rec, "modifiers"),
        setting=csv_get(rec, "setting"), billing_class=csv_get(rec, "billing_class"),
        gross_charge=csv_get(rec, "standard_charge|gross"),
        discounted_cash=csv_get(rec, "standard_charge|discounted_cash"),
        deidentified_min=csv_get(rec, "standard_charge|min"),
        deidentified_max=csv_get(rec, "standard_charge|max"),
    )
    payer_cols = [k for k in rec if norm_col(k).startswith("standard_charge|")
                  and norm_col(k).count("|") >= 3]
    if payer_cols:  # wide: standard_charge|<payer>|<plan>|<field>, plus estimated_amount|.. etc.
        groups = {}
        for k in rec:
            parts = [p.strip() for p in k.split("|")]
            if len(parts) >= 3 and norm_col(parts[0]) in (
                    "standard_charge", "estimated_amount", "median_amount", "10th_percentile",
                    "90th_percentile", "count", "additional_payer_notes"):
                field = parts[-1] if norm_col(parts[0]) == "standard_charge" else parts[0]
                groups.setdefault((parts[1], parts[2]), {})[norm_col(field)] = s(rec[k])
        payer_rows = [dict(payer_name=p, plan_name=pl, **g) for (p, pl), g in groups.items()
                      if any(g.get(f) for f in ("negotiated_dollar", "negotiated_percentage",
                                                "negotiated_algorithm", "estimated_amount",
                                                "median_amount"))]
    else:  # tall
        payer_rows = [dict(
            payer_name=csv_get(rec, "payer_name"), plan_name=csv_get(rec, "plan_name"),
            negotiated_dollar=csv_get(rec, "standard_charge|negotiated_dollar"),
            negotiated_percentage=csv_get(rec, "standard_charge|negotiated_percentage"),
            negotiated_algorithm=csv_get(rec, "standard_charge|negotiated_algorithm"),
            methodology=csv_get(rec, "standard_charge|methodology"),
            estimated_amount=csv_get(rec, "estimated_amount"),
            median_amount=csv_get(rec, "median_amount"),
            **{"10th_percentile": csv_get(rec, "10th_percentile"),
               "90th_percentile": csv_get(rec, "90th_percentile")},
            count=csv_get(rec, "count"),
            additional_payer_notes=csv_get(rec, "additional_payer_notes"))]
    generic_notes = csv_get(rec, "additional_generic_notes")
    for code, ctype in targets:
        for p in payer_rows or [{}]:
            r = base_row(line)
            r.update(common, code=code, code_type=ctype,
                     payer_name=p.get("payer_name", ""), plan_name=p.get("plan_name", ""),
                     standard_charge_dollar=p.get("negotiated_dollar", ""),
                     standard_charge_percentage=p.get("negotiated_percentage", ""),
                     standard_charge_algorithm=p.get("negotiated_algorithm", ""),
                     methodology=p.get("methodology", ""),
                     estimated_amount=p.get("estimated_amount", ""),
                     median_amount=p.get("median_amount", ""),
                     percentile_10th=p.get("10th_percentile", ""),
                     percentile_90th=p.get("90th_percentile", ""),
                     allowed_count=p.get("count", ""),
                     additional_notes=join_notes(generic_notes, p.get("additional_payer_notes")),
                     source_ref=f"line{lineno}" + (f" [{p.get('payer_name')}|{p.get('plan_name')}]"
                                                   if payer_cols else ""))
            yield finish(r)


def normalise(paths):
    for path in paths:
        with open(path) as f:
            for lineno, text in enumerate(f, 1):
                line = json.loads(text)
                line["_path"] = os.path.basename(path)
                gen = from_json if isinstance(line["record"].get("code_information"), list) else from_csv
                for r in gen(line, lineno):
                    r["source_ref"] = f"{line['_path']}:{r['source_ref']}"
                    yield r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="indir", default=".")
    ap.add_argument("--out", default="hpt_autonomic_rates.csv")
    args = ap.parse_args()
    paths = sorted(glob.glob(os.path.join(args.indir, "raw_*.jsonl")))
    rows = list(normalise(paths))
    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    unknown = {(c, r[c]) for r in rows for c in ("setting", "billing_class", "methodology")
               if r[c].startswith("?")}
    print(f"wrote {len(rows)} rows from {len(paths)} files to {args.out}", file=sys.stderr)
    if unknown:
        print(f"WARNING unmapped categorical values: {sorted(unknown)}", file=sys.stderr)


if __name__ == "__main__":
    main()
