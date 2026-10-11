# New-text check on v3

*New-text checker, October 11, 2026. Writes only this file; `review/article_v3.md` is not edited. Follows `review/CONVENTIONS.md`.*

**Sources used.** `review/article_v3.md`; `review/article_draft.md` (v16, review-notes block ignored); `review/verification_summary.md` (October 8 table, Citation check, Round 2, Round 3); `review/findings.csv`; `output/evidence_ledger_delta.csv`; `output/docket_totals.csv`; `output/comment_analysis.md`.

**Not available.**
- **v15** was not attached.
- **The base evidence ledger** (rows CE-, RM-, SB-, TP-, AC-, SE-) is not in the repo. Only the comment-evidence delta is. Ledger rows quoted below come second-hand from the findings and the earlier check.
- **Sources outside the repo and unreachable here.** KFF, HFMA, POLITICO, ASPE, GAO, Michelson, Lindenfeld, the Texas Tribune and Fierce Healthcare, CMS-2450 and the bill numbers. Where v3 carries one of these unchanged from v16, I compared v3 with v16 only and say so.
- **Federal Register PDFs.** I downloaded the two proposed rules from govinfo into the scratchpad (91 FR 30400–30466 and 46562–46599; not committed). I used them to re-check page pinpoints and arithmetic, to settle item 8, and to check a few claims no verification row covers. Every such use is marked "FR read here".

**Bottom line.**
- **Numbers.** Every number in v3 is in v16, the ledger delta, or a confirmed verification row. None is in no source. All arithmetic recomputes, with one sign slip in the wording (item 1).
- **Sec. 5 "same basis".** The statement that POLITICO's $756 billion is on the same basis as CBO's section figures does not follow as written. It follows for one dimension only, the treatment of the interaction, and only on a layout-based reading of CBO (item 3).
- **Claims the sources do not support, or contradict:**
  - The sec. 3 claim that neither rule separates the OBBBA's requirements from CMS's additions is contradicted for the SDP rule (item 3).
  - The "$56.6 billion to $681 billion" range is contradicted by figures in v3 itself (item 3).
- **Citation errors.** One wrong pinpoint (the threshold table), one missing pinpoint (CBO), and one commenter attribution that does not match the findings (item 2 and item 6).
- **Tags.** Mostly consistent. The main inconsistency is how search negatives ("THEIA found no…") are tagged (item 4).
- **Item 7** is clean except for two table notes.
- **Item 8** cannot be settled from the Federal Register text; I report what it does say.

---

## 1. Numbers: scenario, gross or net, outlays or deficits, years

### 1a. Recomputations of every arithmetic result v3 shows

| Result in v3 | Recomputed | Verdict |
|---|---|---|
| $916.9B = 774.8 + 142.1 | 916.9 | ✓ |
| $753.2B = 916.9 − 163.7 | 753.2 | ✓ |
| $488.5B = 753.2 − 264.7 | 488.5 | ✓ |
| $774.8B = 510.1 + 264.7 | 774.8 | ✓ |
| $264.7B = sum of Table 20 | 6.3+10.3+16.3+21.8+26.7+30.9+34.3+37.1+39.5+41.5 = 264.7 (FR read here, image of 91 FR 30452) | ✓ |
| $510.1B = sum of Table 19 | 11.9+19.4+31.2+41.6+51.3+59.4+66.3+71.8+76.6+80.6 = 510.1 (FR read here) | ✓ |
| $774.8B = sum of Table 18 | 18.2+29.7+47.5+63.4+78.0+90.3+100.6+108.9+116.1+122.1 = 774.8 (FR read here) | ✓ |
| $384.0B = 245.8 + 138.2 | 384.0 | ✓ |
| $142.1B = 384.0 − 241.9 | 142.1 | ✓ |
| $241.9B = 154.9 + 87.0 | 241.9 | ✓ |
| $90.9B = 245.8 − 154.9 | 90.9 | ✓ |
| $51.2B = 138.2 − 87.0 | 51.2 | ✓ |
| $142.1B = 90.9 + 51.2 | 142.1 | ✓ |
| $315.9B = 264.7 + 51.2 | 315.9 | ✓ |
| $601.0B = 510.1 + 90.9 | 601.0 | ✓ |
| $601.0B + $315.9B = $916.9B | 916.9 | ✓ (federal and state columns reconcile) |
| $198.7B = 51.0 + 147.7 | 198.7 | ✓ |
| $198.7B = 163.7 + 35.0 | 198.7 | ✓ |
| −$220.3B = 163.7 − 384.0 | −220.3 | ✓ (see wording note 1c) |
| +$21.7B printed; 163.7 − 142.1 | +21.6 | ✓ rounding, but see 1c |
| $147.5B = 198.7 − 51.2 | 147.5 | ✓ |
| $60.5B = 198.7 − 138.2 | 60.5 | ✓ |
| $755.9B = 510.1 + 245.8 | 755.9 | ✓ |
| $630.9B = 755.9 − 80.6 − 44.4 | 630.9 | ✓ (arithmetic; see 3c on its label) |
| $501.5B = 601.0 − 80.6 − 18.9 | 501.5 | ✓ (arithmetic; its labelled derivation appears only in App. F) |
| Table 11 annual federal row sum | 245.9 against stated 245.8; CMS rounds | ✓ matches v3's App. F |
| $340.5B = 191.1 + 149.4 | 340.5 | ✓ |
| $182.7B = 191.1 − 8.4 | 182.7 | ✓ |
| $332.1B = 182.7 + 149.4 | 332.1 | ✓ |
| App. D table: 258.8 = 408.4 − 149.6; 1,125.8 = 989.7 + 136.1; 122.5 = 258.8 − 136.3; 785.8 = 1,125.8 − 340.0 | all correct | ✓ |
| App. D header: derived overlaps ≈ $285B and ≈ $180B | 149.6 − (−135.0) = 284.6; −136.1 − (−316.5) = 180.4 | ✓ (−135.0, −316.5, +149.6, −136.1 all read in FR here, 91 FR 46593–46594) |
| App. D: Table 23 state cells sum to $340.0B (text says $339.6B) | 6.8+11.3+18.7+25.9+33.0+39.2+44.5+49.4+53.7+57.5 = 340.0; federal 649.7 + 340.0 = 989.7 (FR read here) | ✓ |
| Sec. 1: 61.8 + 28.1 + 7.3 + 1.4 = 98.6; 98.6 / 376 ≈ 26% | ✓ | ✓ |
| Sec. 6: A 24 + B 2 + C 3 + D 8 = 37; plus E 14 = 51; $45.4+2.0+0.8+11.9 = $60.1B ("about $60 billion") | ✓ | ✓ |
| Sec. 6: 28 hospital-tax states = A 24 + CO, CT, IN, VT | ✓ | ✓ |
| Sec. 7: at least 20% outside SDPs = 100% − CMS's 80% ceiling | ✓ (central estimate only) | ✓ |
| App. I: 960 as filed / 961 corrected (660 distinct, both views); 214 / 213 (188 / 187) | matches `output/docket_totals.csv` | ✓ |

### 1b. Number-by-number match to v16, ledger delta and verification rows

| Location | Result |
|---|---|
| Exec ¶1–¶6; sec. 3, 4, 5 tables | All figures match v16 and the verification rows on scenario (central), 2026–2035, 2026 dollars, net for the headline range and gross for $916.9B. |
| Sec. 1: 87.5%, $143.8B, 91 FR 30447 | Matches Citation check row "91 FR 30447": a share of one year's (FFY 2025) preprint-reviewed SDPs, stated as such. ✓ |
| Sec. 3: $147.5B, $60.5B, $264.4B | Match VS (Round 2 accounting-statement note; F-020). Scenario and net/gross are right: both are net-for-states figures, with and without the interaction. ✓ |
| Sec. 5: $340.5B, $191.1B, $149.4B, fiscal years 2025–2034, nominal | Match F-015 note. Outlays, not deficits, and the sum is labelled THEIA's. ✓ |
| App. F: $182.7B and $332.1B | Deficit measure, labelled as such, never set beside the outlay figures. ✓ |
| App. F: $755.9B / $630.9B / $601.0B / $501.5B | Match the VS table under F-015. Federal only; 2026–2035 and 2026–2034 as labelled in App. F. (Body labelling of $630.9B: see 3c.) |
| Sec. 6 and App. H (KFF figures, group dollars, state counts) | Match v16 exactly. No KFF source in the repo, so not independently checked. |
| KFF $155B; HFMA $56.6B / $220.3B / $163.7B; POLITICO $340B / $756B / $265B / $681B; ASPE $891B, $502–875B, 3.5%; GAO and study figures in sec. 8 | Match v16. Not independently checkable here. |
| Sec. 5: $220.3B cited by five comments | `output/evidence_ledger_delta.csv` has exactly five comments citing 220.3, in docket 2476, and none has 56.6 (confirmed by search; 56.6 is also absent from both rules, FR read here). ✓ |

### 1c. Numbers found in no source

**None.** I tokenised every number in the body and appendix and looked for it in v16, the ledger delta and comment analysis, `verification_summary.md` and the findings files. Every one appears in at least one of them. Numbers new in v3 relative to v16 and their homes:

- 87.5, 143.8, 147.5, 60.5, 264.4 and the new page pinpoints are in the VS Citation check or Round 2.
- 755.9, 630.9, 501.5, 80.6, 44.4, 18.9, 245.9 and 332.1 are in the VS table under F-015 and Round 3.
- 8.4 is in VS Round 2.
- Comment IDs are in the findings.

### 1d. Number issues

| Location | Issue | Fix |
|---|---|---|
| Sec. 5 "The two figures", sentence 1 | The arithmetic is written "the $142.1 billion cut less the same $163.7 billion gives the +$21.7 billion CMS prints". 142.1 − 163.7 = −21.6, not +21.7, and it does not give the printed figure; 163.7 − 142.1 = +21.6. App. E says 21.6 and the body says 21.7, so the two disagree. The first half has the same slip: 384.0 − 163.7 = +220.3, which is a loss of 220.3. | "…net of the $163.7 billion in lower provider taxes, the $384.0 billion cut leaves providers worse off by $220.3 billion (Table 12), and the $142.1 billion cut leaves them better off by about $21.6 billion, which CMS prints as +$21.7 billion (Table 14; rounding, Appendix E)." |
| App. E, "rounding" note | "$142.1 billion less $163.7 billion gives +$21.6 billion": sign reversed. | "$163.7 billion less $142.1 billion gives +$21.6 billion". |
| Sec. 5 exhibit (table at top) | The table says "Quantity (billions)" and ¶1 says "central estimates, 2026–2035". The dollar basis (real 2026 dollars) is stated only under the sec. 3 table. | Add "billions of 2026 dollars" to the exhibit header. |
| Sec. 1 SDP table, −$5.34B and −$2.44B | No scenario or dollar basis. The −$5.34B is total computable (federal $3.51B, state $1.83B), and the −$2.44B is "real 2026 dollars" (91 FR 30453, 30456, FR read here). | "…CMS estimates −$5.34 billion in Medicaid spending (federal plus state) over 2029–2035 (91 FR 30453)…" and the same for −$2.44B. |
| Exec ¶1 | The $488B floor is net of step 3, which includes IGT savings as well as lower provider taxes. "Net of the provider taxes they would no longer pay" fits only the $753B ceiling. | "…net of the lower provider taxes (ceiling) and, for the floor, of the most they could save on taxes and IGTs that fund the state share". |

**Clean:**
- Sec. 2 (all figures).
- Sec. 3 tables and the $198.7B / $51.0B / $147.7B / $163.7B / $35.0B paragraph.
- Sec. 4 tables.
- Sec. 6 tables.
- Sec. 7 figures.
- App. B, C, D, G, H and I numbers.

---

## 2. Citations against the Citation check and verification summary

| Location | Issue | Fix |
|---|---|---|
| Sec. 1 threshold table, "Source: 91 FR 46562" | The schedule (5.5% FFY 2028 … 3.5% FFY 2032) is not on 91 FR 46562. The summary there says only that the phase-down starts "Effective October 1, 2027" (FR read here). The percentages are at 91 FR 46565 (FFY 2028 5.5%, falling 0.5 points a year to 3.5% in FFY 2032), 46576 and the proposed text at 46598. The Citation check and VS U-3 corrected only the 6 percent cap's cite, and the change map lists this schedule as "still open". | "Source: 91 FR 46565, 46576, 46598; P.L. 119-21 § 71115." |
| Sec. 1, SDP definition, "(42 CFR 438.6(c))" | The Citation check's pinpoint is 438.6(c)(1), the general rule. | "(42 CFR 438.6(c)(1))" |
| Sec. 5 POLITICO ¶2, "(CBO, July 21, 2025, Table 7; October 28, 2025, p. 6)" | One cite covers both the section figures and the interaction lines. Page 6 supports only the interaction clause; the section figures are at pp. 4–5 (F-015 note) and in Table 7. | "…$149.4 billion (CBO, July 21, 2025, Table 7; October 28, 2025, pp. 4–5), and reports interactions on separate lines (October 28, 2025, p. 6)…" |
| Sec. 2 ¶1, "(GAO-24-106202, Table 4)" | Not in the Citation check or VS. It is still an open item in v16's notes and the change map (U-5). | Mark as unverified or verify before publication. |
| Sec. 8 (GAO-23-105515; Michelson et al.; Lindenfeld et al.) and sec. 9 item 5 (Texas Tribune; Fierce Healthcare) | Carried from v16. No verification row. | Same: not independently checked here. |
| Sec. 8 rural ¶1–¶2 | Statutory and FR pinpoints for the rural rule, the rural definition and the cost-paid hospitals' cap default are not cited (change map: "still to add"). The state-plan-rate default is at 91 FR 30450 (FR read here: "…in which case the payment limit is the State plan approved rate"). | Add "(P.L. 119-21 § 71116; 91 FR 30450)". |
| Sec. 9 item 2, "which the SDP rule defers to future rulemaking [E]" | No cite. FR read here: 91 FR 30453, "We expect to provide an analysis of the interaction between these proposals in future rulemaking." | Add "(91 FR 30453)". |
| Sec. 9 item 4 (CMS-2450), item 7 (bills, lawsuit) | No cite for the OIRA review date, the agenda entry, or the bills' status. The "as of September 22, 2026" date is stale (open item in v16's notes). | Cite reginfo.gov and congress.gov (or mark unverified) and re-date. |
| Sec. 9 item 6, case cite and appeal | VS F-024 and Round 3 #6: the case cite, the Fifth Circuit number and "pending" rest on the research table and a June 24, 2026 amicus brief that no one read. v3 attributes the ruling's terms to CHAT, as Round 3 advised, but states the case number and the pending appeal flatly. | "…the pending appeal (Fifth Circuit No. 25-40766, pending as of a June 24, 2026 amicus brief, as reported by a secondary source)…" |
| Sec. 5 HFMA ¶2, "Georgetown University's Center for Children and Families reported … July 27, 2026" | No cite. Georgetown's comment (2476-0029) is not among the five comments citing $220.3B, so this is a separate publication that appears in no file in the repo. | Cite the Georgetown piece, or mark it unverified. |
| Sec. 5 ASPE ¶3 and sec. 9 item 10, "Texas Hospital Association published paired gross and net figures in 2025" | No cite, and "at least one state has published" (item 10) is not the same as a state hospital association (sec. 5). | Cite the THA publication, and align "state" with "state hospital association". |

**Clean (match the Citation check or verification summary, same pinpoint):**
- 91 FR 46562 for the WFTC name.
- 46590 n. 23 and 46592 for section 71117.
- 91 FR 30447 for the 87.5% / $143.8B.
- 46564 for the 75/75 test.
- 46572 and 46598 for the 6% cap.
- 46574 for the September 30, 2028 date and the per-class thresholds.
- 46581 for dropping the 75/75 test.
- 42 CFR 433.70(b) and 433.68(f)(3).
- SSA § 1903(w)(4)(C)(i), § 1903(w)(6)(A), § 1902(a)(10)(A)(i)(VIII), § 1905(a) and (i).
- 42 CFR 438.6(e).
- 31 U.S.C. 1102.
- P.L. 119-21 § 71115(a)(2), with 91 FR 46565 and 46576.
- 91 FR 4794 (CMS-2448-F).
- 91 FR 30410 and footnote 40.
- Table 4 (46589); Tables 6–8 (46589–46590); Table 11 (46591); Table 12 (46592); Table 14 (46593); Table 19 (46596).
- Tables 18–20 (30451–30452); Tables 22–23 (30453–30454); Tables 14–16 (30449–30450; FR read here: 189%, 137% and 255% inpatient commercial ratios).
- Table 27 (30456).
- 91 FR 30462.
- 91 FR 30452 for 80–90%.
- CBO Table 7 and the October 28 pages (pp. 4–6) cited in App. F.
- Every comment ID and page in the body and appendix, except as listed in item 6.

---

## 3. Claims the sources do not support

### 3a. Sec. 5: is POLITICO's $756 billion on the same basis as CBO's section figures?

**v3 text.** "Its $756 billion, both rules' federal savings measured alone ($510.1 billion + $245.8 billion), matches CBO's section-by-section basis…", and later "the like-for-like CMS figure is its federal total without the interaction, $755.9 billion".

**What the verified facts establish.**
- **CMS side.** $510.1B is the SDP rule alone. $245.8B is the provider tax rule "excluding the impacts of the SDP rule" (91 FR 46592, FR read here). Their sum is $755.9B, the figure POLITICO prints as about $756B. That is arithmetic [I].
- **CBO side.** $191.1B (71115) and $149.4B (71116) are separate outlay lines. CBO reports interactions on other lines and prints no figure for the 71115–71116 interaction (VS Round 3 #2). CBO does not say in words that each section excludes the interaction, so "exclude" rests on layout (VS Round 3 #2; App. F says so).
- **The match to POLITICO.** POLITICO's article, per v16, names no components for its $756B. That the sum equals $755.9B is THEIA's matching inference, not a stated composition.

**Does "same basis" follow?** No, not as worded.
- **Follows, with a hedge.** The two figures use the same treatment of interactions (each piece scored alone). This depends on reading CBO's layout, so it is an [I] with a caveat. The body states it without the caveat, which sits only in App. F.
- **Does not follow, and is contradicted by v3's own next paragraph:**
  - **Years.** CMS 2026–2035 against CBO FY2025–2034.
  - **Dollars.** CMS real 2026 against CBO nominal.
  - **Baseline.** CMS uses the President's FY2027 Budget projection without the WFTC; CBO uses its own baseline (January 2025).
  - **Scope.** CMS's provider tax figure includes CMS's own state-offset assumption (30 percent) and design choices.
- **Resulting problem.** Calling $755.9B "like-for-like" overstates it. It is like-for-like on the interaction only, and v3 itself says the rest of the gap is unresolved.

| Location | Issue | Fix |
|---|---|---|
| Sec. 5 POLITICO ¶3, "matches CBO's section-by-section basis" | Overstated, as above. | "…is on the same footing as CBO's section figures in one respect: each rule is scored alone, with no interaction removed (on our reading of CBO's layout; Appendix F). The years, dollars and baselines still differ." |
| Sec. 5 POLITICO ¶4, "the like-for-like CMS figure is…" | Same overstatement. | "…the CMS figure that treats the interaction as CBO's section figures do is… $755.9 billion…" |
| Sec. 5 POLITICO ¶4, "Because CBO scores the two sections one at a time, its section figures exclude the interaction" | A reading (layout-based) stated as a fact. The hedge, "CBO does not say in words that each section figure excludes the interaction", is only in App. F. | Add "CBO does not say so in words; the reading rests on its table layout (Appendix F)." |

### 3b. Other unsupported or contradicted claims

| Location | Issue | Fix |
|---|---|---|
| Sec. 5 POLITICO ¶4, "Of the three adjustments CMS's tables allow (years, interaction, dollar basis), only dropping the extra year lowers CMS's figure, to $630.9 billion" | Three problems. **(1)** CMS's tables allow only two adjustments; App. F says "CMS gives no dollar conversion, so the dollar-basis adjustment is known in direction only". **(2)** $630.9B is not the effect of dropping a year: from the $601.0B headline, dropping 2035 gives $501.5B. $630.9B is the no-interaction total ($755.9B) after dropping 2035, so it combines two adjustments. **(3)** "Dropping the extra year" yields 2026–2034, nine years, against CBO's ten (2025–2034). | "Of the three differences CBPP names, only the extra year lowers CMS's figure: $601.0B becomes $501.5B for 2026–2034; removing the interaction raises it to $755.9B ($630.9B for 2026–2034); CMS gives no conversion for the dollar basis, but converting to nominal dollars would raise it. CBO's window (2025–2034) is also not CMS's 2026–2034." |
| Sec. 3 ¶1, "neither rule separates what the OBBBA requires from what CMS added [I]" (also sec. 5 ¶4, "CMS's additions to the OBBBA … direction unknown") | Contradicted for the SDP rule (FR read here). Tables 18–20 are titled "LIMITING SDPS UNDER SECTION 71116" (91 FR 30451–30452). At 30453 CMS introduces the extension to other services with "In addition to these impacts … $5.34 billion". At 30459 it prices an alternative (a 180-day grandfathering reading) as $778.7B, against the proposal's $774B, and says the alternative's figure includes only services under section 71116. v3's own SDP table shows the additions with their own dollar figures. The sentence may still hold for the provider tax rule: I found no separate estimate for the 75/75 sunset or the 6% cap. It also supports item 7: $774.8B is a section 71116 estimate. | "CMS separates the SDP rule's extensions to other services from its section 71116 estimate (91 FR 30451–30453), but does not separate what the provider tax rule adds to section 71115." Revise sec. 5 ¶4 accordingly: the additions to the SDP figure are outside the $510.1B, so only the provider tax rule's additions and the baselines are of unknown direction. |
| Exec ¶2 and sec. 5 ¶1, "Published figures for the two rules run from $56.6 billion to $681 billion" | Contradicted inside v3. CMS's own published $774.8B (SDP rule, Table 18) is above $681B. So is ASPE's $891B, which v3 discusses. The range holds only for the third-party figures v3 discusses (HFMA, KFF, POLITICO). | "Figures in circulation from HFMA, KFF and POLITICO range from…" or "Figures reported outside CMS's own tables…". |
| Sec. 4 ¶4, "CMS says it cannot attribute the impacts by provider type (sec. 3)" about "CMS's figures" | The statement is the SDP rule's (91 FR 30462). For the provider tax rule CMS says the opposite: "we expect that the largest decreases would be in payments to hospitals given that hospital taxes account for the majority of provider tax revenues" (91 FR 46591, FR read here). Sec. 4's "CMS's figures" covers both rules. | "CMS's SDP figures cover all providers; CMS says it cannot attribute them by provider type (91 FR 30462), and for the provider tax rule it expects the largest decreases to fall on hospitals (91 FR 46591)." |
| Exec ¶3, sec. 4 step 1, sec. 5 row "Payments providers lose" | The full $774.8B and $916.9B are labelled "payments providers lose". CMS says the SDP reductions are "a transfer from affected providers and other relevant individuals and entities (such as State or local jurisdictions that reimburse providers…)" (91 FR 30450, 30462). Sec. 3 says this once; the later labels drop it. | Add "(CMS says part falls on other entities, such as local governments; sec. 3)" at the first use in sec. 4. |
| Sec. 1, SDP definition, "SDPs are extra payments, approved in advance by CMS" | Not all are. 42 CFR 438.6(c)(2)(i) exempts some from written prior approval, and the very next sentence (87.5%) is limited to those that "needed CMS's written prior approval" (VS Citation check, row 91 FR 30447; 91 FR 30447 "excluding SDPs for which States are not required to receive written prior approval"). | "…most approved in advance by CMS…" |
| Sec. 2 ¶1, "Between 80 and 90 percent of SDP arrangements relied…" | CMS writes "80 to 90 percent of SDPs", "by the end of 2025", from preprint data (91 FR 30452, FR read here). VS Round 3 #4 found that CMS does not say whether its shares count arrangements or dollars. "Arrangements" supplies a count basis and drops the date. | "Between 80 and 90 percent of SDPs, by the end of 2025 on CMS's preprint data, relied…" |
| Sec. 7 Step 2, "It is zero in non-expansion states, where the freeze lowers no one's bill [I]" | CMS says projected provider taxes "not already enacted and imposed as of July 4, 2025 … would be ineligible to remain in place beyond October 1, 2026" (91 FR 46589, FR read here). A hospital in a non-expansion state whose state enacted or raised a tax after July 4, 2025 would see a lower bill. | "…zero in non-expansion states unless the state enacted or raised the tax after July 4, 2025 (91 FR 46589), and for a tax already at or below the threshold." |
| App. D, "some commenters describe it as a share of SDP spending (comments …-0204, p. 10; -0056; -0106, p. 10)" | F-009 lists -0056 (Kentucky Health Collaborative) as "'65 percent of state directed payments'" and -0106 (BAYADA) as the 55–75% range "'of SDP spending'". Each uses CMS's own words, and F-009 says "only the 65 percent restatements depart from CMS's wording". Only -0204 restates the 65% as spending. | "one commenter restates the 65 percent as a share of spending (comment CMS-2026-2476-0204, p. 10); another applies the 55–75 percent range to the $774.8 billion (comment CMS-2026-2476-0093, p. 7)". |
| App. D, "Draft note, SDP rule parameters … $408.4B and $989.7B" and the range table | FR 30454 says the high-savings $989.7B "includes … additional services with limits proposed under this rule". The central $774.8B appears to cover section 71116 services only (see the second row above). The central, low and high totals may therefore differ in scope by a small amount. Table 23's own title says "under section 71116". | Check with CMS's tables and add a scope note, or state that the scopes are not confirmed to match. |
| Exec ¶4, "states have not decided how they will fund SDPs going forward [I]" | A claim about all states; no finding or verification row supports it. | "THEIA Services found no source showing how states will fund SDPs going forward." |
| Sec. 9 item 8, "the first public basis for calculating a state's lower threshold" and "Interim provider tax data states file with CMS" | The data go to CMS (91 FR 46583, FR read here), and nothing in the repo says they are public. They are also proposed requirements, not current ones. | "…the data states would file with CMS under the proposed rule, the first basis for calculating…" |
| Sec. 5 POLITICO ¶4, "later references restate POLITICO's figure (Appendix G)" | App. G documents one comment (-0079, an individual) that restates the figure. "References" in the plural is not supported by App. G. | "one later comment restates POLITICO's figure (Appendix G)". |

**Clean:**
- Sec. 4 ¶1–¶3 and the CMS sentence it paraphrases.
- Sec. 5 KFF and HFMA subsections (apart from the tag issues in item 4).
- Sec. 6 (compared with v16; the KFF figures are not independently checkable).
- Sec. 7 steps 1 and 3.
- Sec. 8 (compared with v16).
- Sec. 9 items 1, 3, 9, 10 and 11.
- The CMS statement at 91 FR 46593 (read here): "the net effect of both proposed rules would still be a significant reduction to provider payments through Medicaid over time." v3's paraphrase is faithful. The sentence also names $774.8B, so "does not confirm any combined figure" is right only in the sense that it gives no combined total.

---

## 4. Evidence tags

| Location | Issue | Fix |
|---|---|---|
| Sec. 5 POLITICO ¶2, "which CBO does not print. [E]"; sec. 5 HFMA, "THEIA found $56.6 billion in neither rule [E]"; sec. 5 POLITICO ¶4, "later references restate… [E]"; sec. 9 item 7, "located no lawsuit… [E]"; sec. 9 item 9, "no public source makes that link today. [E]" | **Inconsistent tagging of search negatives.** Elsewhere v3 tags "THEIA found/located no…" as [I] (exec ¶2, ¶4; sec. 2; sec. 3; sec. 4). A negative from THEIA's own search is not stated by a cited document. | Tag all "found/located no…" statements [I], or add one sentence to the legend that [E] covers documented, scoped searches. |
| Exec ¶1 and sec. 3 ¶1, "…so they include the OBBBA's own effect. [E]" | The baseline statement is [E] (91 FR 30447; 46589–46591). "So they include the OBBBA's effect" is THEIA's inference. | Split: baseline [E]; "so…" [I]. |
| Sec. 5 two-figures ¶, "The −$220.3 billion thus already nets out the lower taxes, as the title … indicates. [E]" | "Thus … nets out" is an inference; the title is [E]. | "…nets out the lower taxes [I], as the title of Table 12 … indicates. [E]" |
| Sec. 5 HFMA ¶2, "HFMA had not replied to THEIA Services' request … [E]" | Not stated in a public document. | Drop the tag or use [I]. |
| Sec. 5 HFMA ¶2, Georgetown; sec. 5 ASPE ¶3, THA 2025 figures; sec. 9 item 10, "at least one state has published…" | [E] with no cited document. | Add cites (item 2) or retag. |
| Sec. 8 rural ¶1–¶2 [E]; sec. 9 item 4 and item 7 [E] | No cited document. | Add cites (item 2). |
| Sec. 9 item 6 [E] | Case number, F. Supp. cite and "pending" rest on a secondary source (VS F-024, Round 3 #6). | Qualify (item 2) or retag. |
| Sec. 8 IMD ¶, "most freestanding psychiatric hospitals are IMDs… with exceptions for managed care and certain demonstrations [I]" | "Most … are IMDs" and "certain demonstrations" are factual claims with no cite (change map: still to add). [I] hides that they are uncited. | Cite, or mark uncited. |
| App. C "stated limits [I]" | "CMS's figures are in 2026 dollars, and CMS assigns $35.0 billion … (Table 8)" are CMS-stated facts under an [I] tag. | Split: [E] for the CMS statements; [I] for THEIA's limits. |
| Sec. 3, "CMS applies each set of assumptions nationally [E]" | No cite. | Add "(91 FR 46591–46594; 30453–30454)". |

**Clean:**
- Exec ¶1 (first sentence [I]), ¶2, ¶3, ¶5 and ¶6.
- Sec. 1 [E]/[I] split on the hold-harmless sentences and the 87.5% pair.
- Sec. 2 ¶3–¶4 (the [I]/[E]/[I] chains).
- Sec. 3 table notes and state paragraph.
- Sec. 4 ¶1–¶3.
- Sec. 5 KFF [E]/[I] split; HFMA [I] opening and closing; POLITICO and ASPE.
- Sec. 6 (expansion-status and Group D "[I]" splits).
- Sec. 7 [I]/[E] splits.
- Sec. 8 [C] sentence.
- Sec. 9 item 11 [C].
- App. D, E, F and G tags (draft-note labels match content).

---

## 5. Appendix moves: undefined terms, dangling references, figures whose basis is only in an appendix

| Location | Issue | Fix |
|---|---|---|
| Sec. 4 ¶3, "widen the range to at least about $122 billion and at most about $1,126 billion (Appendix D)" | The $122B is the lower-savings figure after step 3; the $1,126B is the higher-savings figure after step 2 (after step 3 it is $786B). The step, the pairing and the unit (billions of 2026 dollars, 2026–2035) are in App. D only. | "…widen the range to about $122 billion (lower-savings estimates, after step 3) at the low end and about $1,126 billion (higher-savings estimates, after step 2) at the high end, billions of 2026 dollars, 2026–2035." |
| Sec. 5 POLITICO ¶4, "$630.9 billion" and "$755.9 billion" | The base (federal, no interaction) and window are in App. F only. The body gives the window for $755.9B but not for $630.9B, and does not say it is the no-interaction total. | State "federal, without the interaction, 2026–2034" at the first use. |
| Sec. 5 POLITICO ¶4, CBO "scores the two sections one at a time" | The hedge on the layout reading sits only in App. F (see 3a). | Add the hedge in the body. |
| Sec. 2 ¶4, "within CMS's 55 to 75 percent estimate" | That 55% and 75% are the high- and low-savings values is stated only in App. D. | Add "(the high-savings and low-savings values; Appendix D)". |
| Sec. 5 ASPE ¶3, "a test of payment rates, not a net provider loss (Appendix F)" | App. F's FAH note says only that FAH and others asked CMS to net provider taxes in the test; it does not say what the test measures. | State it in App. F, or cite the SDP rule's payment-limit definition. |
| Sec. 8, "(IMDs; Appendix B)" and "defines rural hospitals broadly (Appendix B)" | The IMD definition (more than 16 beds) and the rural list sit only in App. B. The body's argument on IMDs and rural hospitals depends on them. | Acceptable as pointers; the rural list should be in the body if the sentence "defines … broadly" is kept. |
| "HFMA" (sec. 5 heading and text); "KFF" | HFMA is never spelled out. The Appendix lines I–J are still unwritten. | Spell out HFMA at first use. |
| ASPE heading in sec. 5 | The heading uses "ASPE" before the body spells it out. | Spell it out in the heading or at the first mention. |
| Sec. 3 and sec. 4, "low-savings"/"high-savings" against "lower-savings"/"higher-savings" | Two sets of terms for the same CMS estimates (App. D uses lower/higher). | Use one set. |
| Figure placeholders | Figures 1, 2, 3, 6, 7, 8 appear in the body; Figure 4 is referenced nowhere, and Figure 5 only in App. D. | Renumber or note. |
| App. D, "Draft note, range under the other estimates (moved from sec. 4)" | Editorial wording ("moved from sec. 4") is inside the note. | Remove before publication. |

**Clean:**
- Cross-references to secs. 3, 4, 5 and 7 (all targets exist and say what the pointer promises).
- References to App. B (hold harmless, expansion states, IGTs, IMD), C (71117, financing shares), E ($264.4B, rounding), G, H and I (the bills, lawsuit, counts).
- Terms defined in place: SDP, IGT, hold harmless, 75/75 test, threshold, freeze, rating period, permissible class, preprint, central estimate, overlap, expansion state.

---

## 6. Commenters: comment IDs, advocacy label, quotes

**Comment IDs.** Every sentence about what commenters said carries an ID, and every ID and page matches `findings.csv`, except for the points below.

| Location | Issue | Fix |
|---|---|---|
| App. D, 65 percent restatement | -0056 and -0106 do not support the sentence (item 3b). | See 3b. |
| App. F, CBPP, "compared CMS's $601 billion with $341 billion" | The $341B is CBPP's restatement of CBO's figure and carries no source label (Convention §4). | "…with CBO's $341 billion (CBPP's rounding of $340.5 billion)…" |
| App. G, "an individual's, which restates it as a hospital loss" | Does not say whose figure it restates. | "…restates POLITICO's $681 billion as a hospital loss…" |
| App. F, "11 comments, 8 distinct texts, in both docket views" (netting in the payment-limit test) | F-018 gives these as a keyword count. Convention §3: unread keyword counts should be rounded and hedged. v3 hedges the other keyword counts ("about 120", "about 90") but not this one. | "about 11 comments (about 8 distinct texts), keyword count", unless every hit was read. |
| Sec. 5 HFMA ¶2, Georgetown | Not a comment ID case (Georgetown's comment does not cite $220.3B). See item 2. | Cite the publication. |

**Advocacy figures.** No commenter-produced estimate appears in v3, so the label has nothing to attach to. Every commenter number is a restatement of a CMS, CBO or ASPE figure, and each is labelled with its original source ("CMS's figures", "CBO's Section 71115 estimate", "CMS's $510 billion", "ASPE's statute-level estimates"), except the two label gaps above. CBPP's, AHIP's and BCBSA's readings are described as readings, not as estimates. HFMA's $56.6B, KFF's $155B, POLITICO's $681B and ASPE's $891B come from non-commenters; Convention §4 does not apply to them.

**Quotes from the Federal Register: none added.**
- v3 carries the same three FR quotes as v16.
  - Two are from CMS-2449-P, 91 FR 30453.
  - One is the Table 12 title, from CMS-2452-P, 91 FR 46592.
- The v16 "shown in table 12" quote is now paraphrased.
- The only other quotes are HFMA's and POLITICO's.

| Location | Issue | Fix |
|---|---|---|
| Sec. 4, the 91 FR 30453 quote | Carried over, but it breaks Convention §5 in two ways. The first fragment is 29 words (limit 24), and CMS-2449-P is quoted twice (one passage in two fragments; the decision log counts it as one quote). | Trim to 24 words ("…the net change in provider revenue … could be significantly less") and keep or drop the second fragment, or record a departure. |

**Clean:**
- Sec. 5 HFMA ¶2 (five IDs, "five distinct texts, the same as filed and corrected").
- Sec. 5 ASPE ¶3 (FAH, -0676, p. 2).
- Sec. 8 (Virginia, -0755, p. 3).
- Sec. 9 item 6 (CHAT, -0114, pp. 13–14).
- App. D (-0145 pp. 3–4, -0093 p. 8, -0204 p. 10), E, F (all other IDs), G and I.
- Counts in both docket views.

---

## 7. $916.9 billion: "combined" and attributed to the two statutory sections as the rules would carry them out

| Use | Result |
|---|---|
| Exec ¶3 | ✓ "a combined $916.9 billion reduction … from the two sections, as the rules would carry them out". |
| Sec. 3 table, "Both rules combined" row, with the note "All rows score Sections 71116 and 71115 as the rules would carry them out" | ✓ |
| Sec. 4 step table, row 1 | **Gap.** The row builds the figure from $774.8B + $142.1B but never says "combined". The note under that table does not repeat the attribution. Add "(both rules combined)" and the sentence from the sec. 3 note. |
| Sec. 5 exhibit, "Both rules combined" column | **Gap.** The label is right, but the source note does not repeat the attribution. Add it. |
| Sec. 5 ASPE ¶2, "THEIA Services' combined $916.9 billion", "ASPE scored the OBBBA's provisions directly rather than as CMS's proposed rules would carry them out" | ✓ Combined, attributed to THEIA, and the contrast makes the basis clear. |
| Sec. 4 ¶2, "Combined, the two rules would leave providers…" | Acceptable. Sec. 3 ¶1's caveat covers it. |

Supporting evidence from the FR (read here): Tables 18–20 are titled "limiting SDPs under section 71116" and CMS prices the extensions to other services separately (3b). The $774.8B is therefore a section 71116 estimate as the SDP rule would carry it out, which supports the attribution.

---

## 8. Federal fiscal years or calendar years for CMS's 2026–2035

**The Federal Register text I can reach does not state which for the 2026–2035 window.** It says the following (FR read here, govinfo PDFs).

| Rule | Page | Exact wording | What it shows |
|---|---|---|---|
| CMS-2449-P (SDP) | 91 FR 30451 | Table 18, "PROJECTED TOTAL COMPUTABLE MEDICAID SPENDING IMPACT OF LIMITING SDPS UNDER SECTION 71116 OF THE WFTC LEGISLATION BY YEAR (IN BILLIONS OF 2026 DOLLARS)"; the year column heading is "Fiscal Year", rows 2026–2035. | The SDP tables label the years as fiscal years, without saying federal or state. |
| CMS-2449-P | 91 FR 30452 | Tables 19 and 20 carry the same title form ("…FEDERAL SHARE…", "…NON-FEDERAL SHARE…") and the same "Fiscal Year" column heading. Tables 22–23 (91 FR 30454) do too. | As above. |
| CMS-2449-P | 91 FR 30447 | "States are estimated to have paid $143.8 billion of SDPs in FFY 2025…" | Only the one-year base is called a federal fiscal year (FFY). |
| CMS-2449-P | 91 FR 30448 | "…there is data for $136.0 billion in SDPs for payments with effective dates starting in calendar year 2025…" | The source data are by effective date, in calendar years. |
| CMS-2449-P | 91 FR 30456 | "We assumed that the FFS supplemental payment requirements … would go into effect in January 2029 and that these changes would first affect States in July 2029, at the beginning of most States' fiscal years. This adjustment reduced the effective impact by 75 percent for fiscal year 2029." | In the FFS section, "fiscal year" appears to be a State fiscal year (July–June). |
| CMS-2452-P (provider tax) | 91 FR 46589 | "…we estimate provider taxes would result in $98.6 billion in revenue for States in calendar year 2026." | The 2026 provider tax base is a calendar year. |
| CMS-2452-P | 91 FR 46589 | "This freeze would begin October 1, 2026 … This freeze reduces projected tax revenue by $2.3 billion in 2026 and by $51.0 billion from 2026 through 2035." | A freeze that starts October 1, 2026 cannot reduce revenue in federal fiscal year 2026, which ends September 30, 2026. So the provider tax rule's "2026" is not FFY 2026. This is an inference; CMS does not say. |
| CMS-2452-P | Tables 4–14, 91 FR 46589–46594 | Table headings read "[In billions of real 2026 dollars]" with columns "2026 … 2035 2026–2035" and no "fiscal" or "calendar" label. | No statement. |

**What this means for v3.**
- **The two rules' tables may not share a year basis.**
  - The SDP tables are headed "Fiscal Year".
  - The provider tax figures are unlabelled, and the one explicit label is calendar-year 2026, with the freeze evidence pointing the same way.
  - This bears on the combined $916.9B (sec. 3, sec. 4), which adds the two. It is not only the CBO comparison that is open (App. F's "Open: …").
- **A stated limit is needed.** The article should say, at the first use of "2026–2035", that CMS does not say whether these are federal fiscal years or calendar years, and that the SDP tables are headed "Fiscal Year".
- **Fix for App. F's open item.** "Open: whether CMS's 2026–2035 are federal fiscal years or calendar years." → "CMS does not say. The SDP rule's Tables 18–20 are headed 'Fiscal Year' (91 FR 30451–30452), and the provider tax rule gives $98.6 billion for 'calendar year 2026' (91 FR 46589); its other tables are unlabelled."
- **Recommended wording for the body (sec. 3 table note).** "CMS does not say whether its 2026–2035 are federal fiscal years or calendar years; its SDP tables are headed 'Fiscal Year' (91 FR 30451–30452) and its provider tax base year is a calendar year (91 FR 46589)."

---

## Section-by-section status

| Section | Status |
|---|---|
| Executive summary | Issues: range wording (3b), "net of provider taxes" (1d), "so they include" tag (4), "states have not decided" (3b). Everything else clean. |
| 1 | Issues: threshold-table source (2), SDP definition (3b), 438.6(c)(1) (2), −$5.34B/−$2.44B basis (1d). Rest clean. |
| 2 | Issues: "SDP arrangements" and date (3b), GAO cite (2). Rest clean. |
| 3 | Issues: "neither rule separates" (3b), "so both include" tag (4), "nationally" cite (4). Tables and figures clean. |
| 4 | Issues: provider-type sentence (3b), range basis in appendix (5), "payments providers lose" (3b). Tables and arithmetic clean. |
| 5 | Issues: POLITICO basis (3a), $630.9B label and "tables allow" (3b), sign wording (1d), HFMA and Georgetown cites and tags (2, 4), range wording (3b), CBO pinpoint (2). KFF and ASPE figures match v16. |
| 6 | Clean against v16 (KFF figures not independently checkable). |
| 7 | One issue: Step 2 "zero in non-expansion states" (3b). Rest clean. |
| 8 | Citations and tags: rural, IMD (2, 4). Figures match v16. |
| 9 | Issues: items 2, 4, 6, 7, 8, 10 (2, 3b, 4). Items 1, 3, 9, 11 clean. |
| Appendix | Issues: App. D 65 percent attribution and scope note (3b); App. E sign (1d); App. F CBPP label and keyword hedge (6); App. C tag split (4). App. B, G, H and I clean. |

*Nothing outside this file was edited.*
