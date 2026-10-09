# Changes from v16 to v2

*Writer's file, October 9, 2026. Follows `review/CONVENTIONS.md`. Maps every change in `review/article_v2.md` against `review/article_draft.md` (v16) to its source. Decisions behind each change are in `review/decision_log.md`.*

**Keys**

* **F-nnn / U-n**: finding in `findings.csv` / unmapped item in `findings_v16_unmapped.csv`.
* **RC n**: row n of `required_corrections_v16.md`, numbered top to bottom (1 F-005; 2 F-006; 3–4 F-007; 5–7 F-012; 8 F-015; 9–10 U-3).
* **NTC §s.n**: item n, counted top to bottom, in section s of `new_text_check.md`.
* **Attack n**: attack n in `feedback/skeptic.md`; **SK pt n**: its cross-cutting point n.
* **CC**: the Citation check in `verification_summary.md`. **R2**: its Round 2 verification.
* **Instr.**: your instructions for this task.

**Unchanged by design.** Section numbers and headings; the title line and byline; the placeholders [Figure 1], [Figure 2], [Figure 3], [Figure 6], [Figure 7], [Figure 8], [DATE], [DATE SENT] and [proposed title]; the evidence-tag legend; every figure in the body tables (rows are relabeled, and one row is added to the sec. 5 exhibit; S5.2). The review-notes block is left out (Instr.).

---

## Executive summary

| # | v2 location | Change | Source |
|---|---|---|---|
| E1 | ¶1, sentence 1 | "between $488 billion and $753 billion in Medicaid revenue over the next ten years" → "about $488 billion to $753 billion worse off over 2026–2035, in 2026 dollars, net of the provider taxes they would no longer pay". | NTC §1.2, §1.3 |
| E2 | ¶1, sentences 2–3 | Rules described as carrying out Sections 71115 and 71116, each defined; added that CMS measures both against a projection without the OBBBA, so its estimates include the OBBBA's effect. | NTC §4.1 |
| E3 | ¶1, sentences 4–5 | Hospital sentence now gives both CMS statements (most reductions on hospitals; no data to attribute by provider type) and points to sec. 7. | F-012; RC 5; attack 3 |
| E4 | ¶2 | Cut "a twelvefold spread" and the "Hospitals, states and policymakers … goes unreported" sentence; "figures in circulation" → "published figures for the two rules"; "because each measures" → two separate facts; "such as federal savings, state savings or one rule's effect alone" → "such as federal savings only or one rule alone". | Instr.; NTC §1.1, §1.4, §3.1, §3.2, §3.15 |
| E5 | ¶2, last sentence | Added CMS's statement that the two rules together would still cut provider payments significantly, and that THEIA found no CMS figure for it (pointer to sec. 4). | F-011 |
| E6 | ¶3 | "$916.9 billion" sentence now says "from the two sections, as the rules would carry them out"; "combined" kept. | NTC §4.1 |
| E7 | ¶4 | "the eliminated SDPs" → "the state share of the SDP cut"; "SDP arrangements" kept; IGTs glossed; cut "and others use general revenue"; "Public data do not show" → "THEIA Services found no current public source showing"; "public data cannot narrow" → "CMS's data therefore cannot narrow". | Instr.; NTC §2.2, §2.5, §2.12, §3.3, §3.5, §5.8, §6.2 |
| E8 | ¶4, last sentence | Added that the range rests on CMS's 30 percent state-offset assumption [E], read as already inside CMS's totals [I]. | F-007 |
| E9 | ¶5 | "Providers can still gauge" → "Hospitals can still gauge", tagged [I]; "the new 3.5 percent limit" → "3.5 percent, the threshold reached in 2032"; "A provider's own" → "A hospital's own"; added "state decisions make the result a range, not a single number". | NTC §2.1, §3.4, §5.9, §6.3 |

## 1. The OBBBA and the two proposed rules

| # | v2 location | Change | Source |
|---|---|---|---|
| S1.1 | ¶1 | Added cite for the Working Families Tax Cut name: 91 FR 46562 (not the table captions NTC proposed). | NTC §2.3, §3.7; CC (row "91 FR 46589–46591") |
| S1.2 | ¶1, new sentence 2 | Section 71117 and CMS-2448-F: CMS's provider tax estimates take them into account, with no significant change (91 FR 46590 n. 23, 46592). | F-006; RC 2 |
| S1.3 | SDP rule, ¶1 | Definition cited to 42 CFR 438.6(c); "mostly hospitals" replaced by hospitals' 87.5 percent of an estimated $143.8 billion of SDPs needing written prior approval in the fiscal year ending September 30, 2025 (91 FR 30447), with a sentence saying it is one year's payments, not the projected cuts. | NTC §2.4, §5.10; CC (rows "42 CFR 438.6(c)", "91 FR 30447"); F-012; Instr. |
| S1.4 | SDP table, row 1 | Expansion states cited to Social Security Act § 1902(a)(10)(A)(i)(VIII); "−$5.34 billion" → "CMS estimates −$5.34 billion in spending". | NTC §2.6, §6.6; CC; U-1 (figures unchanged) |
| S1.5 | SDP table, row 2 | "(July 4, 2025 for rural hospitals)" → "(by July 4, 2025 …)"; "rating period" defined; "−$2.44 billion" → "CMS estimates −$2.44 billion in spending". | NTC §2.13, §6.5, §6.6 |
| S1.6 | Provider tax, ¶2, sentence 1 | "Federal rules" → "Federal law and rules"; hold harmless cited to Social Security Act § 1903(w)(4)(C)(i) and 42 CFR 433.68(f)(3). | NTC §2.7; CC (rows "SSA § 1903(w)(4)", "42 CFR 433.68(f)") |
| S1.7 | Provider tax, ¶2, sentence 2 | Second prong named as the 75/75 test, in the aggregate (91 FR 46564); "6 percent today" → "at most 6 percent". | U-3; RC 9; NTC §1.8 |
| S1.8 | Provider tax, ¶2, sentence 3 | Kept v16's "federal matching funds on the revenue that does not qualify", added the mechanism and cite 42 CFR 433.70(b). | NTC §3.8; CC (row "42 CFR 433.70") |
| S1.9 | Provider tax table, row 1, right | "Drops the second part of the test" → "Stops applying the 75/75 test from federal fiscal year 2027"; cite 91 FR 46562, 46581. | U-3 |
| S1.10 | Provider tax table, row 2, left | Exemption restored as "taxes on nursing facilities and on intermediate care facilities for people with intellectual disabilities are exempt from the lower threshold and stay at their July 4, 2025 level"; cite P.L. 119-21 § 71115(a)(2) and 91 FR 46565, 46576. | U-4; NTC §6.4 |
| S1.11 | Threshold table source note | Added the 6 percent cap's pinpoint (proposed § 433.68(f)(3)(ii)(A)(3); 91 FR 46572, 46598) and its 75/75 exception that CMS expects no state to use; added 31 U.S.C. 1102 for the fiscal year. 91 FR 46562 kept for the schedule. | U-3; RC 10; NTC §2.14; CC (row "31 U.S.C. § 1102") |

## 2. What links the two rules

| # | v2 location | Change | Source |
|---|---|---|---|
| S2.1 | ¶1 | "because provider taxes and IGTs fund many SDPs" → "because provider taxes fund many SDPs". | NTC §3.9 |
| S2.2 | ¶2 | IGTs glossed and cited to Social Security Act § 1903(w)(6)(A), worded as the statute's "units of government … non-federal share"; "80 to 90 percent of SDPs" → "of SDP arrangements"; GAO spelled out at first use. | NTC §2.5, §2.11, §2.12; CC (row "SSA § 1903(w)(6)(A)") |
| S2.3 | ¶3 | "loses funding under the provider tax rule" → "the provider tax rule limits the taxes that fund it". | NTC §3.10 |
| S2.4 | ¶4 | Overlap statement split from the CMS figures and tagged [I]; figures labeled "under CMS's central estimate, which assumes states make up 30 percent of the cut from other revenue". | NTC §5.1, §6.7; F-007 |
| S2.5 | ¶5 | Overlap rests on two stated assumptions (65 percent tax-financed; at most 80 percent on SDPs, 91 FR 46592); added that CMS's other estimates move them together with the offset (91 FR 46593–46594), so no one assumption's effect can be isolated. | F-007; RC 4 |

## 3. CMS's estimates for each rule

| # | v2 location | Change | Source |
|---|---|---|---|
| S3.1 | SDP bullet | "closer together and further apart" labeled (low-savings) and (high-savings). | NTC §6.8 |
| S3.2 | Provider tax bullet | Added the central values (65 percent, at most 80 percent, 30 percent offset; 91 FR 46591–46592) and both other scenarios with the Medicaid-paid tax share; added that CMS states the offset immediately before the $384.0 billion total and splits $142.1 billion and $241.9 billion from it [E], and that THEIA reads all three as net of the offset [I]. | F-007; RC 3; SK pt 2; attack 2; Instr. |
| S3.3 | Table header | "Central estimate …" → "Reduction in Medicaid spending, central estimate …". | F-010; attack 2; Instr. (state effects) |
| S3.4 | Table source note | Added "All rows score Sections 71116 and 71115 as the rules would carry them out." | NTC §4.3 |
| S3.5 | ¶ after table | "federal and state savings" → "federal and state reductions"; added CMS's same-page statement that it cannot reliably attribute impacts to provider types, with its reason (91 FR 30462). | F-012; RC 6; Instr. (state effects) |
| S3.6 | New ¶ after the $198.7 billion paragraph | CMS's accounting statement shows states only as a net loss of $147.5 billion (Table 19, 91 FR 46596); measured alone, $60.5 billion (Table 12, 91 FR 46592) [E]; reconciled as $51.2 billion or $138.2 billion less $198.7 billion [I]; state column called a spending reduction, not a saving; SDP rule's $264.7 billion said to be before any change in the taxes and IGTs that fund it. | F-010; attack 2; R2 (accounting statement); Instr. (state effects) |

## 4. The net effect on providers

| # | v2 location | Change | Source |
|---|---|---|---|
| S4.1 | New ¶1 | CMS's statement after the +$21.7 billion that the two rules together would on net still leave providers paid significantly less (91 FR 46593), paraphrased, with the qualifier that it confirms no combined figure. | F-011; Instr. (no new quotes) |
| S4.2 | ¶2, sentence 1 | "which no public source reports" → "which THEIA Services found in no public source". | NTC §3.1 (same scoping, applied here) |
| S4.3 | ¶2, sentences 2–3 | Cross-reference: the range rests on CMS's 30 percent offset, read as inside the $142.1 billion; a state replacing more or less than CMS assumes narrows or widens the loss (pointer to sec. 7, step 3). | F-007; Instr. |
| S4.4 | Step-table row 3; ¶ after the quote | "funding fewer SDPs" → "paying less to fund the state share of SDPs". | NTC §6.9 |
| S4.5 | Step-table source note | Added that $264.7 billion is Table 20's sum and CMS's text gives $264.4 billion (Appendix E). | F-020 |
| S4.6 | ¶ on best case | "above $488 billion and at or below $753 billion" → "above about $488 billion and at or below about $753 billion". | NTC §6.10 |
| S4.7 | Scenario-table source note | "which CMS's narrative rounds to $339.6 billion" → "which CMS's text gives as $339.6 billion; Appendix E". | F-020 (v16 flag); attack 4 |
| S4.8 | Last ¶ | Split into CMS's two same-page statements (91 FR 30462); hospitals' 2026 tax share stated as a projection; the one-year-share allocation of the $163.7 billion labeled THEIA's assumption, not CMS's; pointer to sec. 7. | F-012; RC 7; SK pt 4; attack 3 |

## 5. What the published figures measure

| # | v2 location | Change | Source |
|---|---|---|---|
| S5.1 | ¶1 | "range … because each answers" → two facts, with "or uses a different basis". | NTC §3.15 |
| S5.2 | Exhibit table | "Federal savings" → "Federal Medicaid spending reduction"; "State savings" → "State Medicaid spending reduction, before lost provider tax revenue"; new row "Net for states": loss of 60.5 (alone), loss of 147.5 (after the SDP rule), "Not estimated here" for the SDP rule and both rules; source note says why. | F-010; attack 2; Instr. (state effects) |
| S5.3 | Two figures, ¶ after table | Added that +$21.7 billion is the provider tax rule's increment, not the combined effect, which CMS calls a significant reduction (pointer to sec. 4). | F-011 |
| S5.4 | KFF | Match with CMS's $154.9 billion split into its own sentence, tagged [I]. | NTC §5.2 |
| S5.5 | HFMA ¶1 | "$220.3 billion is the provider line" → "matches the provider line". | NTC §3.11 |
| S5.6 | HFMA ¶2, sentences 1–2 | "CMS's wording may explain the reading" tagged [I]; CMS's "shown in table 12" wording paraphrased instead of quoted, so v2 quotes CMS-2452-P once (the Table 12 title); restored "and Table 12 shows the net −$220.3 billion". | NTC §5.3, §6.11; SK pt 5 (quote budget); Instr. (no new quotes) |
| S5.7 | HFMA ¶2, new sentence 3 | Of the five provider-tax-docket comments citing $220.3 billion (five distinct texts, same in both views), four read it as a payment cut; none reaches $56.6 billion. | F-013; attack 4 |
| S5.8 | POLITICO ¶1 | Restored "under the 2025 law". | NTC §6.12 |
| S5.9 | POLITICO ¶2, sentences 1–3 | CBO named and abbreviated; $191.1 billion and $149.4 billion stated as CBO's estimates of reduced federal outlays, 2025–2034, cited to CBO's July 21, 2025 Table 7 (replacing CRS R48633); added that CBO does not print their sum; $340.5 billion described as that sum, tagged [I]. | F-015; NTC §1.6; R2; Instr. |
| S5.10 | POLITICO ¶2, last sentence | "The Congressional Budget Office also scored the OBBBA itself, including enrollment effects CMS's estimates do not model" → CBO counts coverage effects (1.1 million more uninsured in 2034 from Section 71115, none from 71116; CBO, October 28, 2025, pp. 4–5); CMS assumes the provider tax rule has no effect on enrollment (91 FR 46590). | F-005; RC 1; SK pt 3; R2 |
| S5.11 | POLITICO ¶3 | "$265 billion is the SDP rule's state savings alone" → "the SDP rule's reduction in state spending alone", adding the $198.7 billion lost tax revenue that leaves states a net loss under the provider tax rule (pointer to sec. 3). | F-010; attack 2; Instr. (state effects) |
| S5.12 | POLITICO ¶4 | Rewritten as a reconciliation on CMS's tables: $601.0 billion against the $340.5 billion sum; only the extra year lowers CMS's figure ($501.5 billion); without the interaction $755.9 billion ($630.9 billion without 2035); dollar conversion raises it by an amount not computable from CMS's tables; remainder unresolved; THEIA attributes it to no single cause. Removed "a gap that does not show the rules exceed the OBBBA". Pointers to Appendices F and G. | F-015; RC 8; attack 1; F-014; Instr. |
| S5.13 | ASPE ¶1 | ASPE spelled out. | NTC §2.10 |
| S5.14 | ASPE ¶2 | "the counterpart of the $35.0 billion" attached to the price effect only; "ASPE analyzed the OBBBA rather than the rules" → "ASPE scored the OBBBA's provisions directly rather than as CMS's proposed rules would carry them out"; "is not comparable to the combined $916.9 billion" → "cannot be compared directly with THEIA Services' combined $916.9 billion". | NTC §3.12, §3.13, §4.2 |
| S5.15 | ASPE ¶3 | "Several organizations already separate these quantities" split: CMS and THA net provider taxes against payments [E]; FAH's request described as accounting for provider taxes when calculating the total payment rate tested against the cap [E], a test of payment rates, not a net provider loss [I] (Appendix F). | F-018; F-019 |

## 6. Where exposure is concentrated

| # | v2 location | Change | Source |
|---|---|---|---|
| S6.1 | KFF bullets 1–2 | First bullet split in two; the $60 billion excludes Minnesota and Missouri; "about $93 billion" restored. | NTC §1.7 |
| S6.2 | KFF caution | "do not show proportional effects" → "do not show which states face the largest proportional effects". KFF base-rate wording kept as in v16. | NTC §6.14 |
| S6.3 | ¶ after table | Split: "Expansion status decides …" [I]; "other states a 110 percent cap and the freeze only" → "a 110 percent cap, the phase-down and the freeze, but not the lower threshold" [E]; "new provider taxes" → "new or higher provider taxes". | NTC §5.4, §3.14, §6.13 |
| S6.4 | Group E | Added "so the lower threshold reaches all four" [I]. | NTC §6.15 |
| S6.5 | Group D | "least reliable" tagged [I]; "not evidence" kept [I]. | NTC §5.5 |
| S6.6 | Minnesota/Missouri | "IGT-funded SDPs" → "SDPs funded only by IGTs". | NTC §6.16 |

## 7. Estimating one hospital's position

| # | v2 location | Change | Source |
|---|---|---|---|
| S7.1 | Step 1 | "preprint" defined at first use. | NTC §2.13 |
| S7.2 | Step 2, new sentence 1 | What step 2 measures: the tax the hospital would no longer pay, current bill minus each lower bill. | NTC §6.17 |
| S7.3 | Step 2, last sentence | "CMS announces final state thresholds on September 30, 2028" → "CMS intends to announce final thresholds by state and tax class no later than September 30, 2028 (91 FR 46574)"; starting point is the hospital's own tax class. | U-2; NTC §5.6 (cite per CC, row "91 FR 46562") |
| S7.4 | Step 3, ¶1 | [I] definition split from the [E] description of taxes and IGTs. | NTC §5.7 |
| S7.5 | Step 3, third case | Added that CMS's national estimate already assumes states make up 30 percent of the provider tax rule's cuts, so the case is a departure from that assumption, not relief on top of it. | F-007; Instr. |

## 8. Services already under strain

| # | v2 location | Change | Source |
|---|---|---|---|
| S8.1 | Obstetrics | Restored "GAO reported research showing". | NTC §6.1 |
| S8.2 | Pediatrics | Restored "A national study found". | NTC §6.18 |
| S8.3 | Psychiatry | "leaving the total about flat" → "while the total stayed about flat". | NTC §6.19 |
| S8.4 | IMD ¶ | IMDs defined (Social Security Act § 1905(i)); restriction cited to § 1905(a); managed care exception to 42 CFR 438.6(e). | NTC §2.8; CC (rows "SSA § 1905(a) and § 1905(i)", "42 CFR 438.6(e)") |
| S8.5 | Rural ¶1 | "by July 4, 2025, against May 1, 2025 for other hospitals" → "by July 4, 2025, where other hospitals' SDPs must date from before May 1, 2025". | F-026 (v16 flag); NTC §6.5 |
| S8.6 | Rural ¶2 | Added that state Medicaid agencies, including Virginia's and Ohio's, and many providers argued the same in comments (about 140 comments, about 100 distinct texts, same in both views; keyword count). | F-026 |

## 9. What to watch

| # | v2 location | Change | Source |
|---|---|---|---|
| S9.1 | Item 5 | Restored "before either rule is final"; pointer to Appendix I. | NTC §6.20; F-024 |
| S9.2 | Item 7 | Pointer to Appendix I. | F-028 |
| S9.3 | Item 8 | "CMS's announcement of final thresholds … on September 30, 2028" → "CMS's intended announcement … no later than September 30, 2028 (91 FR 46574)". | U-2; CC (row "91 FR 46562") |

## Appendix (headings and bullets A–J unchanged; draft notes added)

| # | v2 location | Change | Source |
|---|---|---|---|
| A.1 | C | Note: the provider tax rule's full posted record has now been read for sec. 5's figures. | F-001 |
| A.2 | D | Note: the three scenarios' parameters, with pages; CMS prints no pre-offset total. | F-007; R2 |
| A.3 | D | Note: commenters restate the 65 percent as a share of SDP spending. | F-009 |
| A.4 | E | Note: CMS's text against its tables ($264.4 billion vs $264.7 billion; $339.6 billion vs $340.0 billion) and the rule that v2 uses table sums. | F-020; attack 4 |
| A.5 | E | Note: the Table 12 cross-reference (paraphrased). | F-013; attack 4 |
| A.6 | E | Note: how commenters read the provider tax rule's figures ($90.9 billion federal; high-savings −$136.1 billion; the $154.9 billion overlap; a federal range missing the high-savings estimate). | F-010; F-017 |
| A.7 | F | Note: CBO's two measures; $340.5 billion as THEIA's sum; $182.7 billion deficit figure; $332.1 billion deficit-basis sum; the two bases never mixed. | F-015; F-004; R2; Instr. |
| A.8 | F | Note: the federal reconciliation table on CMS's tables; dollar basis direction only; open question on fiscal versus calendar years. | F-015; attack 1 |
| A.9 | F | Note: CBPP's comparison, attributed as its reasoning, opposing the rule, no adjusted figures (2476-0033, p. 9, footnote 23). | F-015 (corrected) |
| A.10 | F | Note: commenters cite CBO's Section 71115 estimate on both measures; the SDP-docket pattern of $510 billion beside $149.4 billion; a supporting group carries ASPE's figures into the record. | F-004; F-016; F-021 |
| A.11 | F | Note: AHA, South Carolina's Medicaid agency and template letters on netting in the payment-limit test (11 comments, 8 distinct texts, both views). | F-018 |
| A.12 | G | Note: full-record search for $681 billion; the four newly posted letters; scope limits. | F-001; F-002; F-014 |
| A.13 | I | Methods note: posted counts (960 as filed / 961 corrected; 214 / 213; distinct texts); Federal Register counts (6,344 and 245, refreshed September 4 and September 24, 2026); the two measure different things and are not compared across dockets. | F-001; F-003; R2; Instr. |
| A.14 | I | Note: legal arguments in comments; no filed suit reported. | F-028 |
| A.15 | I | Note: CMS's Round 4 questions on Texas's SFY2027 CHIRP preprint (Texas HHSC, p. 17 of 19). | F-024 |

---

## Citation to add after verification

Each was proposed by a review file or would source a v2 claim, but neither the Citation check nor the verification summary confirms it, so v2 does not cite it.

| # | Citation | Where it would go in v2 | Proposed by / reason |
|---|---|---|---|
| 1 | Federation of American Hospitals, comment CMS-2026-1916-0676, p. 2 of 45 | Sec. 5, ASPE ¶3 | F-019 (located by the analyst; not in CC or the verification summary) |
| 2 | OBBBA Section 71116, and a pinpoint page in 91 FR 30400 et seq., for the rural hospital definition and for cost-paid hospitals' cap defaulting to the state plan rate | Sec. 8, rural ¶1–2 | NTC §2.9 (not covered by CC) |
| 3 | P.L. 119-21 § 71115 pinpoint for the expansion-state threshold schedule (5.5 to 3.5 percent) | Sec. 1, threshold table source note (v2 keeps v16's 91 FR 46562) | U-3 shows the 6 percent cap is not at 46562; the schedule's page was not checked |
| 4 | 91 FR 46570 (thresholds set per state and per permissible class) | Sec. 7, step 2; sec. 9, item 8 | F-022 verification note only |
| 5 | 91 FR 46594 (CMS repeats the F-011 point for the low-savings estimate) | Sec. 4, ¶1 | F-011 note; messaging.md |
| 6 | CRS R48633 (v16's source for CBO's figures) | Sec. 5, POLITICO ¶2, if a CRS cite is wanted beside CBO's own table | v16; not read this cycle (S cross-cutting point 1) |
| 7 | Comment IDs and pages for commenters described in v2: F-013 (2476-0049 p. 2; 2476-0085 p. 1; 2476-0190 p. 2; 2476-0201 p. 1; 2476-0212); F-014 (2476-0079); F-002 (2476-0148, -0116, -0109, -0057); F-004 (2476-0201 p. 1; 2476-0029 p. 1; 2476-0097, -0187, -0195; 2476-0126; 2476-0089); F-016 (1916-0902; 1916-0128; 1916-0756); F-018 (1916-0928 p. 11; 1916-0923 p. 3; 1916-0369, -0476 and other templates); F-021 (2476-0130 p. 2); F-026 (1916-0755 p. 3; 1916-0209); F-028 (1916-0407 p. 1); F-010 (2476-0145 pp. 3–4; 2476-0093 p. 8); F-017 (2476-0101 p. 1; 2476-0091 p. 27); F-020 (1916-0417 p. 6; 1916-0509 p. 38; 1916-0648 p. 3); F-009 (2476-0204 p. 10; 2476-0056; 2476-0106 p. 10; 2476-0093 p. 7) | Appendix notes (C–I) and sec. 5, sec. 8 | Located in `findings.csv`; not in CC or the verification summary. (CBPP 2476-0033, p. 9, footnote 23 is confirmed in the verification summary and is cited in Appendix F.) |
| 8 | A source for "most freestanding psychiatric hospitals are institutions for mental diseases" | Sec. 8, IMD ¶ | ledger AC-14 (uncited in v16; CC confirms only the IMD definition and exclusion) |
| 9 | A source for the IMD exclusion's exception for "certain demonstrations" | Sec. 8, IMD ¶ | NTC §2.8 covers the managed care exception only |
| 10 | ASPE's coverage of Section 71117 | Sec. 5, ASPE ¶1, if added | messaging.md (F-006, optional); ledger TP-13, not re-read |

**Proposed citations not to add.** NTC §2.3's "(Tables 5, 9 and 10 captions, 91 FR 46589–46591)" for the Working Families Tax Cut name: CC found the captions print only the acronym (Table 5 as "WTFC"), so v2 cites 91 FR 46562. NTC §5.6's "(91 FR 46562)" for the 2028 date: CC puts it at 91 FR 46574, worded as an intention.

**Existing v16 citations flagged for re-check** (kept in v2 under decision 4 of the log): 91 FR 30410 for "shares that count arrangements, not dollars" (F-009 flag; ledger CE-48 says CMS does not say); 91 FR 46589–46591 as the source for both rules' no-OBBBA baseline (F-006 flag: verified for the provider tax rule only); 91 FR 46562 for the threshold schedule and the new permissible class; sec. 9 item 6's "set aside" (F-024: secondary); GAO-24-106202 Table 4 and the preprint's financing fields (U-5).
