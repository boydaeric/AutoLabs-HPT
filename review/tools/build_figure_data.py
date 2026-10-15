"""Build one CSV per figure in review/figures/data/.

Figures 1, 2, 4 and 5 hold values stated in article_v8.md or quoted in the
ledger; each row carries `source_text`, a phrase that gate2_check.py finds
verbatim in article_v8.md or a ledger file, and `found_in`.

Figure 3 rebuilds each state's group (A–E) from KFF's chart data in
review/figures/sources/kff/ and App. H's definitions:
  expansion status   KFF expansion tracker (ZJUAA/5)
  SDPs above caps    KFF Aug 14, 2026, Figure 1 map (ZdNkK/23):
                     "Hospital SDPs likely affected"
  dollars            KFF Aug 14, 2026, Figure 4 (UbS1f/14)
  provider taxes     KFF Aug 20, 2026, appendix table (q3dXL/7)
  A expansion, SDPs above caps, hospital tax above 3.5%
  B expansion, SDPs above caps, non-hospital tax above 3.5% only
  C expansion, SDPs above caps, no non-exempt tax above 3.5%
  D non-expansion, SDPs above caps
  E all others
Nothing is adjusted to fit the text; gate2_check.py compares the result.

Usage: python review/tools/build_figure_data.py
"""
import csv
from pathlib import Path

REVIEW = Path(__file__).resolve().parents[1]
DATA = REVIEW / "figures" / "data"
KFF = REVIEW / "figures" / "sources" / "kff"


def write(name, header, rows):
    DATA.mkdir(parents=True, exist_ok=True)
    with open(DATA / name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


H = ["figure", "item", "value", "unit", "role", "source_text", "found_in"]
A = "article_v8.md"
L = "ledger"

# Figure 1: the overlap (sec. 2, sec. 3 table)
write("fig1_overlap.csv", H, [
    [1, "SDP rule", 774.8, "billion 2026 dollars, 2026-2035", "bar: SDP rule",
     "SDP rule                                                                    | 510.1       | 264.7     | 774.8", A],
    [1, "Provider tax rule, measured alone", 384.0, "billion 2026 dollars, 2026-2035", "bar total",
     "would cut provider payments by $384.0 billion alone", A],
    [1, "Overlap: already counted in the SDP rule", 241.9, "billion 2026 dollars, 2026-2035", "segment of provider tax bar",
     "attributes the $241.9 billion difference", A],
    [1, "Provider tax rule, additional cut", 142.1, "billion 2026 dollars, 2026-2035", "segment of provider tax and combined bars",
     "but by only $142.1 billion more once the SDP rule’s cuts are counted", A],
    [1, "Both rules combined", 916.9, "billion 2026 dollars, 2026-2035", "bar total",
     "**Both rules combined**                                                     | **601.0**   | **315.9** | **916.9**", A],
])

# Figure 2: waterfall (sec. 5, App. E)
write("fig2_waterfall.csv", H, [
    [2, "Provider tax rule measured alone (CMS Table 12)", -220.3, "billion 2026 dollars, 2026-2035", "start",
     "the $384.0 billion cut alone leaves providers $220.3 billion worse off (Table 12)", A],
    [2, "Add back the overlap already counted in the SDP rule", 241.9, "billion 2026 dollars, 2026-2035", "step",
     "the difference is the $241.9 billion overlap", A],
    [2, "On top of the SDP rule (CMS Table 14)", 21.7, "billion 2026 dollars, 2026-2035", "end",
     "CMS reports +$21.7 billion for the provider tax rule after the SDP rule’s cuts (Table 14, 91 FR 46593)", A],
    [2, "Note: components give", 21.6, "billion 2026 dollars, 2026-2035", "note: difference is CMS's rounding (Appendix E)",
     "$163.7 billion less $142.1 billion is $21.6 billion; the difference is rounding in CMS’s components", A],
])

# Figure 4: pediatric (sec. 8; ledger AC-10, FG-07)
# Bed series left out: the FG-07 quote gives adult bed counts only, not
# pediatric beds (-19.5%) and adult beds (-3.0%) as quoted figures.
write("fig4_pediatric.csv", H, [
    [4, "Pediatric inpatient units", -29.9, "percent change, 2008-2022", "bar",
     "pediatric inpatient units fell 29.9 percent", A],
    [4, "Adult inpatient units", -4.4, "percent change, 2008-2022", "bar",
     "against a 4.4 percent decline in adult units", A],
])

# Figure 5: psychiatric beds (sec. 8; ledger AC-07, AC-11, FG-08)
write("fig5_psychiatric.csv", H + ["year"], [
    [5, "Short-term acute care hospitals", 11.3, "beds per 100,000 people", "line start",
     "fell from 11.3 to 9.06 in short-term acute care hospitals", A, 2011],
    [5, "Short-term acute care hospitals", 9.06, "beds per 100,000 people", "line end",
     "fell from 11.3 to 9.06 in short-term acute care hospitals", A, 2023],
    [5, "Freestanding psychiatric hospitals", 16.8, "beds per 100,000 people", "line start",
     "rose from 16.8 to 19.5 in freestanding psychiatric hospitals", A, 2011],
    [5, "Freestanding psychiatric hospitals", 19.5, "beds per 100,000 people", "line end",
     "rose from 16.8 to 19.5 in freestanding psychiatric hospitals", A, 2023],
    [5, "Total", 28.1, "beds per 100,000 people", "line start",
     "the total stayed about flat at 28.1 and 28.4", A, 2011],
    [5, "Total", 28.4, "beds per 100,000 people", "line end",
     "the total stayed about flat at 28.1 and 28.4", A, 2023],
    [5, "Note: source's 2023 components sum to", 28.56, "beds per 100,000 people",
     "note: not the stated 28.4", "9.06 + 19.5 = 28.56", L + " FG-08", 2023],
])


# Figure 3: state groups from KFF chart data
def read(name, delim):
    with open(KFF / name, encoding="utf-8") as f:
        return {r["State"].strip(): r for r in csv.DictReader(f, delimiter=delim)}


tracker = read("ZJUAA_5.csv", ",")
tracker = {k: v for k, v in tracker.items() if v["State Abbrev."].strip()}
sdp = read("ZdNkK_23.csv", ",")
dollars = read("UbS1f_14.csv", "\t")
tax = read("q3dXL_7.csv", "\t")
assert len(tracker) == len(sdp) == len(tax) == 51, (len(tracker), len(sdp), len(tax))

rows = []
for state in sorted(tracker):
    abbr = tracker[state]["State Abbrev."].strip().rstrip("*")
    exp_status = tracker[state]["Expansion Status"].strip()
    expansion = exp_status.startswith("Adopted")
    above = sdp[state]["Likelihood of impact"].strip() == "Hospital SDPs likely affected"
    tax_any = tax[state]["Any non-exempt tax above 3.5%"].strip()
    taxes = tax[state]["Affected tax(es)"].strip()
    hosp_tax = tax_any == "Yes" and "Hospital" in taxes
    if above and expansion and hosp_tax:
        g = "A"
    elif above and expansion and tax_any == "Yes":
        g = "B"
    elif above and expansion:
        g = "C"
    elif above:
        g = "D"
    else:
        g = "E"
    flags = []
    if state == "Colorado":
        flags.append("SDP above the new limits left out of KFF's figures")
    if above and state not in dollars:
        flags.append("Group A, no KFF estimate" if g == "A" else f"Group {g}, no KFF estimate")
    if g == "E" and expansion and tax_any == "Yes":
        flags.append("lower threshold reaches " + ("hospital tax" if hosp_tax else "non-hospital tax"))
    rows.append([3, state, abbr, g, "yes" if expansion else "no",
                 sdp[state]["Likelihood of impact"].strip() or sdp[state]["mco_status"].strip(),
                 tax_any, taxes, "; ".join(flags)])

# each group's federal hospital SDPs above the caps, one year, summed from
# KFF's UbS1f/14 and rounded as the sec. 6 table prints it ("About $45.4B")
gsum = {g: 0.0 for g in "ABCDE"}
for r in rows:
    gsum[r[3]] += float(dollars[r[1]]["Federal SDP spending on hospitals above new limits"]) if r[1] in dollars else 0.0
for r in rows:
    r.append(f"{gsum[r[3]] / 1e9:.1f}" if r[3] != "E" else "0")

write("fig3_state_groups.csv",
      ["figure", "state", "abbrev", "group", "expansion", "kff_sdp_status",
       "kff_tax_above_3_5", "kff_affected_taxes", "flag", "group_above_caps_billion"], rows)
print("wrote", ", ".join(sorted(p.name for p in DATA.glob("*.csv"))))
