#!/usr/bin/env python3
"""Report docket totals two ways, for every output file.

  as filed  - the docket each comment carries on regulations.gov
  corrected - after moving letters filed in the wrong docket (docket_corrections.csv)

Writes output/docket_totals.csv (one row per file x measure x docket) and adds `docket` /
`docket_corrected` columns to output/verification_log.csv so that file can be totalled both ways too.
Run after tag_comments.py and build_evidence_ledger.py.

  python3 build_docket_totals.py              # write the files
  python3 build_docket_totals.py --markdown   # also print the position x type tables used in comment_analysis.md
"""
import collections
import csv
import sys
from pathlib import Path

OUT = Path("output")
DOCKETS = [("CMS-2026-1916", "CMS-2449-P"), ("CMS-2026-2476", "CMS-2452-P")]
POSITIONS = ["oppose", "request for changes", "mixed", "support", "unclear / off-topic"]
TYPE_LABEL = {"hospital/health system": "Hospital / health system", "association": "Association", "individual": "Individual",
              "advocacy group": "Advocacy group", "state agency": "State agency", "MCO": "MCO", "other": "Other",
              "off-topic": "Off-topic (addresses neither rule)"}
TYPES = ["hospital/health system", "association", "individual", "advocacy group", "state agency", "MCO", "other", "off-topic"]


def read(name):
    return list(csv.DictReader((OUT / name).open(newline="", encoding="utf-8")))


def annotate_verification_log():
    """Look each logged row's docket up by comment ID (row 117 was dropped from the ledger but stays in the log)."""
    tagged = {r["comment_id"]: r for r in read("comments_tagged.csv")}
    path = OUT / "verification_log.csv"
    rows = read("verification_log.csv")
    fields = [f for f in rows[0] if f not in ("docket", "docket_corrected")]
    i = fields.index("comment ID") + 1
    fields[i:i] = ["docket", "docket_corrected"]
    for r in rows:
        t = tagged[r["comment ID"]]
        r["docket"], r["docket_corrected"] = t["docket"], t["docket_corrected"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fields)
        w.writeheader()
        w.writerows(rows)


def totals():
    tagged = read("comments_tagged.csv")
    campaigns = read("campaigns.csv")
    flags = read("parse_flags.csv")
    ledger = read("evidence_ledger_delta.csv")
    vlog = read("verification_log.csv")
    out = []

    def add(file, measure, filed, corrected, note=""):
        """filed / corrected: dict docket -> number; adds a 'both dockets' total."""
        for d, rule in DOCKETS:
            out.append([file, measure, d, rule, filed.get(d, 0), corrected.get(d, 0), note])
        out.append([file, measure, "both", "both rules", sum(filed.values()), sum(corrected.values()), note])

    def count(rows, key, pred=lambda r: True):
        return dict(collections.Counter(r[key] for r in rows if pred(r)))

    def distinct(rows, key, rolekey):
        return count(rows, key, lambda r: r[rolekey] in ("unique", "representative"))

    n = "comments_tagged.csv"
    add(n, "comments", count(tagged, "docket"), count(tagged, "docket_corrected"))
    add(n, "distinct texts (campaign copies counted once; campaigns do not span dockets)",
        distinct(tagged, "docket", "campaign_role"), distinct(tagged, "docket_corrected", "campaign_role_corrected"))
    add(n, "campaigns (2+ comments)", count(tagged, "docket", lambda r: r["campaign_role"] == "representative"),
        count(tagged, "docket_corrected", lambda r: r["campaign_role_corrected"] == "representative"))
    add(n, "comments inside campaigns", count(tagged, "docket", lambda r: int(r["campaign_size"]) > 1),
        count(tagged, "docket_corrected", lambda r: int(r["campaign_size_corrected"]) > 1))
    for typ in TYPES:
        add(n, f"comments, commenter type = {typ}", count(tagged, "docket", lambda r, t=typ: r["commenter_type"] == t),
            count(tagged, "docket_corrected", lambda r, t=typ: r["commenter_type"] == t))
    for pos in POSITIONS:
        add(n, f"comments, position = {pos}", count(tagged, "docket", lambda r, p=pos: r["position"] == p),
            count(tagged, "docket_corrected", lambda r, p=pos: r["position"] == p))

    n = "campaigns.csv"
    add(n, "campaigns (rows)", count(campaigns, "docket"), count(campaigns, "docket_corrected"))
    f1, c1 = collections.Counter(), collections.Counter()
    for r in campaigns:
        f1[r["docket"]] += int(r["size"])
        c1[r["docket_corrected"]] += int(r["size_corrected"])
    add(n, "comments covered (sum of campaign sizes)", dict(f1), dict(c1))
    ex_f, ex_c = collections.Counter(), collections.Counter()
    for r in campaigns:
        ex_f[r["docket"]] += int(r["n_exact_duplicates"])
        ex_c[r["docket_corrected"]] += int(r["n_exact_duplicates_corrected"])
    add(n, "exact duplicates inside campaigns", dict(ex_f), dict(ex_c))

    add("parse_flags.csv", "flagged comments (rows)", count(flags, "docket"), count(flags, "docket_corrected"))

    n = "evidence_ledger_delta.csv"
    add(n, "ledger rows", count(ledger, "docket"), count(ledger, "docket_corrected"))
    for label, key in (("comments with at least one ledger row", "docket"),):
        filed = collections.Counter({d: len({r["comment ID"] for r in ledger if r["docket"] == d}) for d, _ in DOCKETS})
        corr = collections.Counter({d: len({r["comment ID"] for r in ledger if r["docket_corrected"] == d}) for d, _ in DOCKETS})
        add(n, label, dict(filed), dict(corr))

    n = "verification_log.csv"
    add(n, "ledger rows checked (rows)", count(vlog, "docket"), count(vlog, "docket_corrected"))
    add(n, "ledger rows checked, status = corrected", count(vlog, "docket", lambda r: r["status"] == "corrected"),
        count(vlog, "docket_corrected", lambda r: r["status"] == "corrected"))

    for row in out:
        if row[4] != row[5]:
            row[6] = (row[6] + " " if row[6] else "") + "differs after moving 2476-0199 (see docket_corrections.csv)"
    with (OUT / "docket_totals.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["file", "measure", "docket", "rule", "as_filed", "corrected", "note"])
        w.writerows(out)
    return out


def markdown_tables():
    """Position x commenter-type tables, as filed and corrected, for each rule (pasted into comment_analysis.md)."""
    tagged = read("comments_tagged.csv")
    for d, rule in DOCKETS:
        for view, dk, rk in (("as filed on regulations.gov", "docket", "campaign_role"),
                              ("corrected", "docket_corrected", "campaign_role_corrected")):
            for label, pred in (("All comments", lambda r: True),
                                 ("Distinct texts", lambda r, rk=rk: r[rk] in ("unique", "representative"))):
                rows = [r for r in tagged if r[dk] == d and pred(r)]
                by = collections.defaultdict(collections.Counter)
                for r in rows:
                    by[r["commenter_type"]][r["position"]] += 1
                order = sorted(by, key=lambda t: (t == "off-topic", -sum(by[t].values()), t))   # off-topic row last
                print(f"\n[{rule} | {label} | {view}] n = {len(rows)}\n")
                print("| Commenter type | Oppose | Request for changes | Mixed | Support | Unclear / off-topic | Total |")
                print("|---|---:|---:|---:|---:|---:|---:|")
                for t in order:
                    print(f"| {TYPE_LABEL[t]} | " + " | ".join(str(by[t][p]) for p in POSITIONS) + f" | {sum(by[t].values())} |")
                tot = collections.Counter(r["position"] for r in rows)
                print("| **Total** | " + " | ".join(f"**{tot[p]}**" for p in POSITIONS) + f" | **{len(rows)}** |")


if __name__ == "__main__":
    annotate_verification_log()
    rows = totals()
    print(f"wrote output/docket_totals.csv ({len(rows)} rows) and annotated output/verification_log.csv")
    if "--markdown" in sys.argv:
        markdown_tables()
