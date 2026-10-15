"""Gate 2: check the figure CSVs against article_v8.md, the ledger and KFF.

1. Every numeric value in fig1, fig2, fig4 and fig5: its source_text occurs
   verbatim in article_v8.md (found_in = article_v8.md) or in a ledger file
   (found_in = ledger ...), and the value is printed in that source_text.
2. Figure 3: the rebuilt groups reproduce the text exactly: counts 24, 2, 3,
   8, 14 (51); App. H's named members; dollar totals $45.43B, $1.96B,
   $0.80B, $11.91B and $0 from KFF's UbS1f/14; MN and MO in A without a KFF
   estimate; the five lower-threshold Group E states; KFF's 28 hospital-tax
   and 31 any-tax expansion-state counts; 37 states with SDPs above the caps.

Usage: python review/tools/gate2_check.py
"""
import csv
import re
import sys
from pathlib import Path

REVIEW = Path(__file__).resolve().parents[1]
DATA = REVIEW / "figures" / "data"
KFF = REVIEW / "figures" / "sources" / "kff"
article = (REVIEW / "article_v8.md").read_text(encoding="utf-8")
ledger = "\n".join(p.read_text(encoding="utf-8") for p in (REVIEW / "ledger").glob("*.md"))
fails = []


def check(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        fails.append(msg)


def num_forms(v):
    v = float(v)
    s = f"{abs(v):.2f}".rstrip("0").rstrip(".") if abs(v) % 1 else f"{abs(v):.1f}"
    return {s, f"{abs(v):.1f}", f"{abs(v):.2f}"}


# 1. numeric values
for name in ("fig1_overlap.csv", "fig2_waterfall.csv", "fig4_pediatric.csv", "fig5_psychiatric.csv"):
    for r in csv.DictReader(open(DATA / name, encoding="utf-8")):
        hay = article if r["found_in"] == "article_v8.md" else ledger
        present = r["source_text"] in hay
        printed = any(re.search(rf"(?<![\d.]){re.escape(f)}(?![\d])", r["source_text"])
                      for f in num_forms(r["value"]))
        check(present and printed,
              f"{name}: {r['item']} = {r['value']} in {r['found_in']}"
              + ("" if present else " [source_text not found]")
              + ("" if printed else " [value not in source_text]"))

# arithmetic that the figures display
f1 = {r["item"]: float(r["value"]) for r in csv.DictReader(open(DATA / "fig1_overlap.csv"))}
check(abs(f1["Overlap: already counted in the SDP rule"] + f1["Provider tax rule, additional cut"]
          - f1["Provider tax rule, measured alone"]) < 0.05, "fig1: 241.9 + 142.1 = 384.0")
check(abs(f1["SDP rule"] + f1["Provider tax rule, additional cut"] - f1["Both rules combined"]) < 0.05,
      "fig1: 774.8 + 142.1 = 916.9")
f2 = [float(r["value"]) for r in csv.DictReader(open(DATA / "fig2_waterfall.csv"))]
check(abs(f2[0] + f2[1] - f2[2]) < 0.15, f"fig2: {f2[0]} + {f2[1]} = {f2[0] + f2[1]:.1f}, CMS prints {f2[2]} (rounding, App. E)")
f5 = [r for r in csv.DictReader(open(DATA / "fig5_psychiatric.csv"))]
check(sorted({r["year"] for r in f5 if not r["item"].startswith("Note")}) == ["2011", "2023"], "fig5: only 2011 and 2023")
check(abs(9.06 + 19.5 - 28.56) < 1e-9, "fig5 note: 9.06 + 19.5 = 28.56")

# FG-07 bed series rule
fg07 = next(l for l in ledger.splitlines() if l.startswith("| FG-07"))
quotes = re.findall(r"“([^”]+)”", fg07)
ped_beds_q = any("19.5" in q for q in quotes)
adult_beds_q = any("3.0%" in q for q in quotes)
f4items = [r["item"] for r in csv.DictReader(open(DATA / "fig4_pediatric.csv"))]
beds_in = any("beds" in i.lower() for i in f4items)
check(beds_in == (ped_beds_q and adult_beds_q),
      f"fig4: bed series {'included' if beds_in else 'left out'}; FG-07 quotes pediatric beds -19.5%: {ped_beds_q}, adult beds -3.0%: {adult_beds_q}")

# 2. Figure 3
rows = list(csv.DictReader(open(DATA / "fig3_state_groups.csv", encoding="utf-8")))
groups = {g: sorted(r["abbrev"] for r in rows if r["group"] == g) for g in "ABCDE"}
counts = {g: len(v) for g, v in groups.items()}
check(len(rows) == 51 and len({r["abbrev"] for r in rows}) == 51, f"fig3: 51 jurisdictions ({len(rows)})")
check(counts == {"A": 24, "B": 2, "C": 3, "D": 8, "E": 14}, f"fig3: counts {counts} vs 24, 2, 3, 8, 14")
check(groups["B"] == ["WA", "WV"], f"fig3: B = {groups['B']} (text: WA, WV)")
check(groups["C"] == ["DC", "DE", "HI"], f"fig3: C = {groups['C']} (text: DC, DE, HI)")
check(groups["D"] == sorted(["FL", "GA", "KS", "MS", "SC", "TN", "TX", "WI"]), f"fig3: D = {groups['D']}")
check({"MN", "MO"} <= set(groups["A"]), "fig3: MN and MO in A")
low_e = sorted(r["abbrev"] for r in rows if "lower threshold" in r["flag"])
check(low_e == ["AR", "CO", "CT", "IN", "VT"], f"fig3: lower-threshold Group E = {low_e}")
check(all(r["group"] == "E" for r in rows if r["abbrev"] in low_e), "fig3: lower-threshold states are all Group E")
amb = [r["abbrev"] for r in rows if r["abbrev"] in low_e and "non-hospital" in r["flag"]]
check(amb == ["AR"], f"fig3: only AR reached through a non-hospital (ambulance) tax: {amb}")
co = next(r for r in rows if r["abbrev"] == "CO")
check("left out of KFF" in co["flag"] and co["group"] == "E", "fig3: Colorado flagged, Group E")
no_est = sorted(r["abbrev"] for r in rows if "no KFF estimate" in r["flag"])
check(no_est == ["MN", "MO"], f"fig3: no KFF estimate = {no_est}")
# the text's group lists, by script from article_v8.md
for g, want in (("B", "2 (WA, WV)"), ("C", "3 (DC, DE, HI)"), ("D", "8 (FL, GA, KS, MS, SC, TN, TX, WI)")):
    check(want in article, f"fig3: sec. 6 table reads '{want}'")
for n in ("24 expansion states", "| 14 "):
    check(n in article, f"fig3: sec. 6 table reads '{n.strip('| ')}'")

dollars = {r["State"].strip(): float(r["Federal SDP spending on hospitals above new limits"])
           for r in csv.DictReader(open(KFF / "UbS1f_14.csv", encoding="utf-8"), delimiter="\t")}
name = {r["abbrev"]: r["state"] for r in rows}
sums = {g: sum(dollars.get(name[a], 0.0) for a in groups[g]) / 1e9 for g in "ABCDE"}
want = {"A": "45.43", "B": "1.96", "C": "0.80", "D": "11.91", "E": "0"}
for g in "ABCDE":
    got = f"{sums[g]:.2f}" if g != "E" else f"{sums[g]:.0f}"
    check(got == want[g], f"fig3: group {g} ${got}B vs text ${want[g]}B")
check("$45.43 billion, $1.96 billion, $0.80 billion, $11.91 billion and $0" in article,
      "fig3: App. H prints the five rebuilt totals")
check(f"{sum(sums.values()):.1f}" == "60.1" and "about $60.1 billion" in article,
      f"fig3: all groups ${sum(sums.values()):.2f}B vs text 'about $60.1 billion'")
check(set(dollars) <= {r["state"] for r in rows if r["group"] != "E"}, "fig3: every KFF dollar state is in A–D")
above = sum(1 for r in rows if r["kff_sdp_status"] == "Hospital SDPs likely affected")
check(above == 37 and "Hospital SDPs in 37 states" in article, f"fig3: {above} states with SDPs above the caps (text 37)")

exp_yes = [r for r in rows if r["expansion"] == "yes"]
any_tax = sum(1 for r in exp_yes if r["kff_tax_above_3_5"] == "Yes")
hosp = sum(1 for r in exp_yes if r["kff_tax_above_3_5"] == "Yes" and "Hospital" in r["kff_affected_taxes"])
amb_n = sum(1 for r in exp_yes if "Ambulance" in r["kff_affected_taxes"])
mco_n = sum(1 for r in exp_yes if "MCO" in r["kff_affected_taxes"])
check((any_tax, hosp) == (31, 28) and "31 expansion states have a non-exempt provider tax above 3.5 percent: 28 with hospital taxes" in article,
      f"fig3: {any_tax} expansion states with any tax, {hosp} with hospital taxes (text 31 and 28)")
check((amb_n, mco_n) == (10, 6) and "10 with ambulance taxes and 6 with managed care organization taxes" in article,
      f"fig3: ambulance {amb_n}, MCO {mco_n} (text 10 and 6)")
check(len(exp_yes) == 41, f"fig3: {len(exp_yes)} expansion jurisdictions (KFF tracker: 41 including DC)")

print("\nGATE 2:", "FAIL (%d)" % len(fails) if fails else "PASS")
sys.exit(1 if fails else 0)
