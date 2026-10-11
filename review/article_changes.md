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

---

# v2 → v3

*Writer's file, October 11, 2026. Maps every change in `review/article_v3.md` against `review/article_v2.md`. Keys as above, plus: **M2** / **S2** = the Round 2 sections of `feedback/messaging.md` / `feedback/skeptic.md` (N = new issue, cut = cut number, D = decision number); **R3 n** = row n of "Round 3 verification" in `verification_summary.md`; **Dn** = your decision n of October 11; **Instr. 3** = your instructions for this round; **Len** = moved or trimmed to meet the 15 percent cap (D5), with nothing cut. Decisions are logged under "Round 2 decisions" in `review/decision_log.md`.*

**Unchanged by design.** Section numbers; headings except the sec. 5 POLITICO subsection (D2); [E]/[I]/[C] tags on carried claims; placeholders [Figure 1], [Figure 2], [Figure 3], [Figure 6], [Figure 7], [Figure 8], [DATE], [DATE SENT], [proposed title]; the four quotes (CMS-2449-P at 91 FR 30453; the CMS-2452-P Table 12 title; HFMA; POLITICO). No new quotes.

## Body

| # | v3 location | Change | Source |
|---|---|---|---|
| T1 | Exec ¶1 | Baseline sentence scoped to "SDP and provider tax estimates", pointer to sec. 3, no cite; last sentence ("A hospital's own records …") folded into ¶5. | M2 N-5; S2 N-5; R3 1; D1; M2 cut 1 |
| T2 | Exec ¶2 | "would still cut" → "would on net still cut". | M2 N-6; Instr. 3 |
| T3 | Exec ¶4 | Cut the 80–90 percent statistic, IGT gloss, "lower SDPs may reduce" sentence and the 30 percent sentence; IGTs named in the first sentence. | M2 cut 1; S2 cut 1; Instr. 3 |
| T4 | Exec ¶5 | Cut the state-exposure sentences; merged into one sentence with the range-not-a-single-number clause. | M2 cut 1 |
| T5 | Sec. 1 ¶1 | Section 71117 sentence shortened, description moved to App. C; comment-close dates moved to App. I. | S2 citation exception (71117); Len |
| T6 | Sec. 1, SDP rule ¶; provider tax ¶2 | Publication-date sentences moved to App. I. | Len |
| T7 | Sec. 1, SDP table | Expansion-state statute cite moved to App. B. | Len |
| T8 | Sec. 1, provider tax ¶1 | 26 percent / $376 billion and the non-hospital payer amounts moved to App. B; hospitals' $61.8 billion kept. | Len |
| T9 | Sec. 1, hold harmless ¶ | Statute and regulation cites and "in Medicaid or other state payments" moved to App. B; 75/75 test kept in full in the body; deduction mechanism moved to App. B; its cite (42 CFR 433.70(b)) stays in the body. | Len |
| T10 | Sec. 1, threshold source note | Shortened; same cites. | Len |
| T11 | Sec. 2 ¶1 | Lead sentence merged into the overlap paragraph ("Because provider taxes fund many SDPs and …"). | Len (repeat) |
| T12 | Sec. 2 ¶2 | IGT statute cite moved to App. B; the 91 FR 30410 shares and "count arrangements, not dollars" removed from the body, shares moved to App. C with footnote 40's base. | S2 F-009; R3 4; Instr. 3; Len |
| T13 | Sec. 2, overlap ¶ | Cut "which assumes states make up 30 percent of the cut from other revenue (sec. 3)". | M2 cut 3; S2 cut 1 |
| T14 | Sec. 3 ¶1 | Baseline cited by rule: 91 FR 30447 (SDP estimates) and 91 FR 46589–46591 (provider tax rule); added that the SDP rule's fee-for-service estimates state no baseline (91 FR 30455). | M2 N-5; S2 N-5; R3 1; Instr. 3 |
| T15 | Sec. 3 ¶2 and SDP bullet | Pointer to App. D; price ratios moved to App. D. | Len |
| T16 | Sec. 3, provider tax bullet | 65 percent / 80 percent stated by reference to sec. 2; scenario values moved to App. D; "prints no total before the offset" moved in from App. D. Offset reading stays here (body statement 1 of 2). | M2 cut 3; S2 cut 1, cut 5; Len |
| T17 | Sec. 3, ¶ after table | Low-savings and high-savings SDP totals moved to App. D; full 91 FR 30462 caveat kept here (the one full statement). | S2 cut 2; Instr. 3; Len |
| T18 | Sec. 3, state ¶ | Rewritten: net-loss statement scoped to the provider tax rule, with CMS-2452-P Table 19 named by rule; "not a state saving" for the whole column cut; SDP rule's state figure described as in the sec. 5 exhibit (before changes in funding taxes and IGTs, no state net); added why v3 uses $264.7 billion rather than $264.4 billion. | S2 N-3, N-8, F-010; M2 F-010; S2 cut 3; Instr. 3 |
| T19 | Sec. 4 ¶2 | "Driven entirely" and "also rests" replaced: the gap between the ends comes from step 3 alone; both ends rest on CMS's central assumptions (pointer to sec. 3 and sec. 7). Offset restatement removed. | M2 N-2; S2 cut 1; Instr. 3 |
| T20 | Sec. 4 step-table source note | $264.7 billion / $264.4 billion line removed (now in sec. 3). | Len (repeat) |
| T21 | Sec. 4, ¶ after quote | "Providers' savings … cannot exceed $264.7 billion" cut (repeats the table row and the summary). | Len (repeat) |
| T22 | Sec. 4, scenario range | Scenario table, its source note and the pairing sentence moved to App. D; the body keeps the range with "paired by THEIA Services". | Len |
| T23 | Sec. 4, hospital ¶ | 91 FR 30462 restatement replaced by "(sec. 3)"; provider-type list trimmed; disclosed one-year share kept. | S2 cut 2; Instr. 3 |
| T24 | Sec. 5 ¶1; exhibit source note | ¶1 trimmed; source note names CMS-2452-P for Tables 12 and 19 and points to sec. 3 for the blank state nets. | M2 cut 4; S2 N-8 |
| T25 | Sec. 5, two figures | Table removed (repeats the exhibit); its arithmetic kept in one sentence; rounding note moved to App. E. | Len (repeat) |
| T26 | Sec. 5, HFMA ¶2 | "HFMA's reading is not unusual" cut; commenter sentence cites comments CMS-2026-2476-0049, -0085, -0190, -0201 and -0212. v16's HFMA handling otherwise kept. | S2 F-013, N-6; Instr. 3; D4 |
| T27 | Sec. 5, POLITICO heading | Retitled "… and the Congressional Budget Office's estimates". | D2; M2 D1; S2 cross-cutting 1 |
| T28 | Sec. 5, POLITICO ¶2 | Added that CBO reports interactions on separate lines (CBO July 21, 2025, Table 7; October 28, 2025, p. 6); coverage sentence moved to App. F. | R3 2; S2 N-4; Instr. 3 |
| T29 | Sec. 5, POLITICO ¶3 | Rewritten: the $756 billion matches CBO's section-by-section basis but double-counts the federal overlap as a two-rule total; state-net clause replaced by "(sec. 3)". | R3 2; M2 cut 4; S2 cut 3 |
| T30 | Sec. 5, POLITICO ¶4 | Rewritten: CBO's section figures exclude the interaction [I], so the like-for-like CMS figure is $755.9 billion and $601.0 billion has no CBO counterpart; of the three adjustments, only the extra year lowers CMS's figure (to $630.9 billion), the other two raise it; remaining differences of unknown direction; "unresolved" once; coverage dropped from the causes; "reconciliation … no single cause" sentence cut; arithmetic in App. F. | M2 N-1, cut 5; S2 N-4, F-015, cut 4; R3 2; Instr. 3 |
| T31 | Sec. 5, ASPE ¶3 | Trimmed; FAH cited as comment CMS-2026-1916-0676, p. 2. | Instr. 3 (commenter IDs); Len |
| T32 | Sec. 6, Group D ¶ | KFF flag list moved to App. H. | Len |
| T33 | Sec. 6, Minnesota/Missouri ¶ | Repeat of the exclusion trimmed to "have no KFF estimate". | Len (repeat) |
| T34 | Sec. 7, step 1 | Added that step 1 covers only SDP amounts above the cap and leaves out cuts that follow lost provider tax revenue, including the share outside SDPs (at least 20 percent under CMS's 80 percent ceiling). | S2 N-2; Instr. 3 |
| T35 | Sec. 7, step 2 | Rewritten: drop in the hospital's own tax bill; zero in non-expansion states and for taxes at or below the threshold; threshold not the hospital's own rate; 91 FR 46574 cited only for CMS's intent to calculate and provide per-class thresholds no later than September 30, 2028; not directly comparable with the national $163.7 billion (no-OBBBA baseline; $51.0 billion freeze component of the $198.7 billion; after the $35.0 billion to private payers). | M2 N-4; S2 N-1, citation exception (46574); R3 3; Instr. 3 |
| T36 | Sec. 7, step 3, third case | Offset scoped to the provider tax rule's cuts; replacing SDP payments lost to the cap is relief the national range does not include. | M2 N-3; Instr. 3 |
| T37 | Sec. 7, closing ¶ | The $35.0 billion private-payer clause removed (now in step 2). | Len (repeat) |
| T38 | Sec. 8, IMD ¶ | IMD definition and statute and regulation cites moved to App. B. | Len |
| T39 | Sec. 8, rural ¶1 | Shortened; rural definition moved to App. B. | Len |
| T40 | Sec. 8, rural ¶2 | Ohio and the "many providers" keyword count removed; Virginia's agency cited as comment CMS-2026-1916-0755, p. 3, stating only its located heading. | M2 N-7; S2 F-026, N-6; R3 5; Instr. 3 |
| T41 | Sec. 9, item 4 | RIN moved to App. I. | Len |
| T42 | Sec. 9, item 5 | Pointer to App. I removed. | S2 N-9; Instr. 3 |
| T43 | Sec. 9, item 6 | Rewritten: only the case (Texas v. CMS, 805 F. Supp. 3d 734 (E.D. Tex. 2025)), its pending appeal (Fifth Circuit No. 25-40766) and CHAT's description, labelled as CHAT's (comment CMS-2026-2476-0114, pp. 13–14). Cut "set aside", the 2024 rule provisions, the 2023–2024 guidance, September 2025, and the issue description. | S2 F-024; R3 6; Instr. 3 |
| T44 | Sec. 9, item 7 | Bill numbers moved to App. I. | Len |
| T45 | Sec. 9, item 8 | Same 91 FR 46574 wording as step 2; no claim that each state's figures will be published. | M2 N-4; S2 N-1; R3 3; Instr. 3 |

## Appendix (headings and bullets A–J unchanged)

| # | Location | Change | Source |
|---|---|---|---|
| T46 | B | New notes: hold harmless cites and 75/75 wording; expansion-state and IGT statute cites; 2026 provider tax breakdown; IMD definition and cites; rural definition. | Len (moved from body) |
| T47 | C | New notes: Section 71117 description with CMS-2448-F (91 FR 4794); the 91 FR 30410 shares with footnote 40's base of 402 approved SDPs; stated limits (no nominal-dollar or annual view, no commercial-price or uncompensated-care estimate). | S2 citation exception; S2 F-009; R3 4; D4 |
| T48 | D | Parameters note now holds only the other scenarios' values (moved from sec. 3); new SDP rule parameters note (price ratios; $408.4 billion and $989.7 billion); scenario table, source note and pairing sentence moved from sec. 4; commenter note cites comment IDs. | Len; S2 cut 5; Instr. 3 |
| T49 | E | Table 12 cross-reference note cut (repeats sec. 5); text-against-tables note trimmed; new rounding note (+$21.7 billion vs +$21.6 billion) and two-Tables-19 note; commenter notes cite comment IDs. | S2 cut 5, N-8; Instr. 3 |
| T50 | F | CBO-measures note trimmed (sum is now in the body); new interaction-layout note ([E] layout, [I] reading); reconciliation note rewritten with the arithmetic for $755.9 billion, $630.9 billion, $601.0 billion and $501.5 billion, all [I]; coverage note moved from the body, direction not established; commenter notes cite comment IDs; payment-limit note's closing sentence cut. | R3 2; Instr. 3; M2 cut 5; S2 cut 5, F-005 |
| T51 | G | Commenter sentences cite comment IDs (2476-0079; 2476-0148, -0116, -0109, -0057). | Instr. 3 |
| T52 | H | New note: Group D data-quality flags (moved from sec. 6). | Len |
| T53 | I | New dates-and-bills note (moved from secs. 1 and 9); methods note drops "cover each docket as filed" and tags the one-count, no-corrected-view statement [I]; legal-record note cites an example comment ID and tags the no-suit statement [I]. | M2 N-8; S2 N-7, F-003; Instr. 3; Len |

## Citation to add after verification: status after v3

| v2 list # | Status in v3 |
|---|---|
| 1 (FAH, 1916-0676, p. 2) | Now cited in sec. 5 under your commenter rule (Instr. 3). |
| 2 (rural definition; cost-paid cap default) | Still to add. The rural definition is now in App. B, still uncited. |
| 3 (statute pinpoint for the threshold schedule) | Still to add. |
| 4 (91 FR 46570, thresholds by state and class) | No longer needed: R3 confirms the per-class point at 91 FR 46574. |
| 5 (91 FR 46594, F-011 repeated for low-savings) | Still to add. |
| 6 (CRS R48633) | Still to add if wanted. |
| 7 (comment IDs) | Now cited wherever v3 describes what commenters said (Instr. 3). |
| 8–9 (IMD: "most freestanding psychiatric hospitals"; "certain demonstrations") | Still to add. |
| 10 (ASPE and Section 71117) | Still on hold (D3 keeps Section 71117 figures out; the ASPE point is not used). |

**Existing citations flagged in v2 for re-check: status.** 91 FR 30410 "arrangements, not dollars": resolved, claim cut (R3 4). 91 FR 46589–46591 for both rules' baseline: resolved, now 91 FR 30447 for the SDP rule's SDP estimates and 46589–46591 for the provider tax rule (R3 1). Sec. 9 item 6 "set aside": resolved, cut (R3 6). Still open: 91 FR 46562 for the threshold schedule and the new permissible class; GAO-24-106202 Table 4 and the preprint's financing fields (U-5).

---

# v3 → v4

*Writer's file, October 11, 2026. Maps every change in `review/article_v4.md` against `review/article_v3.md`. Keys: **NTC3 x-n** = issue n in section x of `review/new_text_check_v3.md` (numbered as in the decision log's "New-text check v3 decisions"); **D1–D3** = your decisions of October 11 (D1 POLITICO basis; D2 year basis; D3 unverified v16 citations); **Instr. 4** = your instructions for this round; **Len** = moved to the appendix or trimmed as a repeat to stay under the 15 percent cap.*

**Unchanged by design.** Section numbers and headings; placeholders; the [E]/[I]/[C] legend; no new quotes from either rule (the CMS-2449-P quote is shortened, not added to).

## Body

| # | v4 location | Change | Source |
|---|---|---|---|
| U1 | Exec ¶1, sentence 1 | Basis of the range: net of lower provider taxes and, at the lower end, of the most providers could stop paying to fund the cut payments. | NTC3 1d-5 |
| U2 | Exec ¶1 | [E] sentences point to the body section that cites them (sec. 1, sec. 3); "so they include the OBBBA's own effect" split off as [I]. | NTC3 4-2; Instr. 4 (every [E] cited) |
| U3 | Exec ¶2 | Range sentence replaced: the outside estimates examined (HFMA, spelled out; KFF; POLITICO) each measure something narrower or on a different basis; CMS's figures and an $891 billion HHS estimate measure different things. CMS's net-reduction statement: [E] with pointer; "without giving a combined figure" [I]. | NTC3 3b-3, 5-7, 5-8; Instr. 4 |
| U4 | Exec ¶3, ¶4, ¶6 | "carry them out" → "implement them"; "states have not decided" → no source found [I]; ¶6 [E] points to sec. 1. | NTC3 7-2, 3b-11, 4-1 |
| U5 | Sec. 1, SDP ¶ | "most approved in advance by CMS"; cite 42 CFR 438.6(c)(1) and 91 FR 30447. | NTC3 2-2, 3b-6 |
| U6 | Sec. 1, SDP table source note | Bases of −$5.34 billion (federal plus state; 91 FR 30453) and −$2.44 billion (2026 dollars; 91 FR 30456). | NTC3 1d-4 |
| U7 | Sec. 1, provider tax ¶1 | $98.6 billion labelled calendar year 2026. | NTC3 8-1; D2 |
| U8 | Sec. 1, threshold source note | 91 FR 46562 → 91 FR 46565, 46576, 46598. | NTC3 2-1; Instr. 4 |
| U9 | Sec. 2 ¶2 | "SDP arrangements" → CMS's wording, "SDPs … by the end of 2025, on CMS's preprint data"; pointer to App. C replaces the v3 clause about funding shares. | NTC3 3b-7; Len |
| U10 | Sec. 2, overlap ¶ | "(its high-savings and low-savings values)" after 55 to 75 percent. | NTC3 5-4 |
| U11 | Sec. 3 ¶1 | Baseline [E] split from "so both include" [I]; "neither rule separates what the OBBBA requires from what CMS added" removed and replaced: the SDP rule prices Section 71116 (Tables 18–20) and its extension to other services (91 FR 30453) separately [E]; no separate estimate found for the provider tax rule's additions [I]. | NTC3 3b-2, 4-2; Instr. 4 |
| U12 | Sec. 3 ¶2 | SDP-rule bullet folded into the paragraph; provider tax bullet now prose. | Len |
| U13 | Sec. 3, "nationally" | Cite added (91 FR 30453–30454, 46591–46594); "not differences among states" trimmed. | NTC3 4-10; Len |
| U14 | Sec. 3, after the combined table | New year-basis sentence. | D2; NTC3 8-1 |
| U15 | Sec. 3, table note | "carry them out" → "implement them". | NTC3 7-2 (consistency) |
| U16 | Sec. 3, $198.7 billion ¶ | Freeze/threshold split moved to App. B. | Len |
| U17 | Sec. 3, state ¶ | Table 20 sentence shortened (same content). | Len |
| U18 | Sec. 4 ¶1 | F-011 qualifier: "gives no combined figure". | Len (repeat of the [I] search result) |
| U19 | Sec. 4 step table | Row 1 "both rules combined"; rows 1 and 3 shortened; source note adds the Sections 71116/71115 attribution and CMS's other-entities point. | NTC3 7-1, 3b-5; Instr. 4; Len |
| U20 | Sec. 4, step 3 quote | Opening clause paraphrased; quoted fragments now 19 words. | NTC3 6-6; Instr. 4 |
| U21 | Sec. 4, best-case ¶ | Shortened; range sentence states each end's scenario, step, dollars and years. | NTC3 5-1; Instr. 4; Len |
| U22 | Sec. 4, hospital ¶ | Provider-type caveat scoped to the SDP rule (91 FR 30462); provider tax rule: largest decreases expected on hospitals (91 FR 46591); "calendar year 2026"; "A hospital's own records…" removed (repeats exec ¶5). | NTC3 3b-4; Instr. 4; Len |
| U23 | Sec. 5 ¶1 | Range sentence replaced as in U3; table-description sentence removed. | NTC3 3b-3; Len |
| U24 | Sec. 5 exhibit | Header gives central estimates, 2026–2035, billions of 2026 dollars; source note adds the attribution and is shortened. | NTC3 1d-3, 7-2; Instr. 4 |
| U25 | Sec. 5, two figures | Rewritten: CMS's two reported figures [E]; "$163.7 billion less $142.1 billion is $21.6 billion; the difference is rounding in CMS's components" [I]; "thus … nets out" [I]. | NTC3 1d-1, 4-3; Instr. 4 |
| U26 | Sec. 5, HFMA | "found $56.6 billion in neither rule" [I]; "had not replied" [I]. | NTC3 4-1, 4-4 |
| U27 | Sec. 5, POLITICO ¶2 | "names no source" [I]; CBO section figures cited to pp. 4–5, interactions to p. 6; "CBO does not print" [I]. | NTC3 2-3, 4-1; Instr. 4 |
| U28 | Sec. 5, POLITICO ¶3 | Your D1 wording; basis of the $756 billion stated. | D1; NTC3 3a-1, 5-3 |
| U29 | Sec. 5, POLITICO ¶4 | Layout hedge in the body; "like-for-like" → "treated the same way"; $501.5 billion and $630.9 billion each labelled; nine years against ten; dollar conversion not given by CMS; year-basis clause; unknown-direction list limited to the provider tax rule's additions and comparison projections; one later comment (ID) instead of "later references". | NTC3 3a-2, 3a-3, 3b-1, 3b-2, 3b-13, 5-2, 8-1; D2; Instr. 4 |
| U30 | Sec. 5, ASPE | "does not say whether it removes the overlap" [I]; "carry out" → "implement"; netting paragraph moved to App. F, replaced by a one-sentence pointer. | NTC3 4-1, 7-2; Len |
| U31 | Sec. 6 | KFF share-above-caps bullet moved to App. H; Minnesota/Missouri parenthetical shortened; expansion-status sentence cut (the table shows it); Group E paragraph shortened, flags to App. H; table note no longer repeats the Minnesota/Missouri exclusion; Texas and other state dollars moved to App. H (v3). | Len |
| U32 | Sec. 7, step 1 | Grandfathering cites Section 71116; data-source sentence moved to App. C. | Instr. 4 (every [E] cited); Len |
| U33 | Sec. 7, step 2 | Zero in non-expansion states unless a tax was enacted or raised after July 4, 2025 (91 FR 46589); "over 2026–2035" added to the $163.7 billion. | NTC3 3b-8; Instr. 4 |
| U34 | Sec. 7, step 3 | "That money flows…" retagged [I]; preprint defined here and cited to the SDP preprint, Section VI. | NTC3 4-1; Instr. 4; Len |
| U35 | Sec. 7, questions | First two questions merged. | Len |
| U36 | Sec. 8 | Opening [E] points to the studies below; IMD restriction cites § 1905(a); rural ¶1 names Section 71116, points to App. B for the definition and drops the repeated phase-down detail; rural ¶2 cites 91 FR 30450; Virginia sentence trimmed. | NTC3 2-6, 4-6, 5-6; Instr. 4; Len |
| U37 | Sec. 9, item 2 | "(91 FR 30453)". | NTC3 2-7 |
| U38 | Sec. 9, item 3 | Shortened. | Len |
| U39 | Sec. 9, item 6 | [E] only for what CHAT's letter says (ID, pages); the appeal number and pending status attributed to an unverified research note [I]. | NTC3 2-9, 4-7; Instr. 4 |
| U40 | Sec. 9, item 7 | Lawsuit negative [I]. | NTC3 4-1 |
| U41 | Sec. 9, item 8 | "would file … under the proposed rule", "first basis" (not "public"), 91 FR 46583. | NTC3 3b-12 |
| U42 | Sec. 9, items 9 and 10 | Negatives reworded and tagged [I]; "state hospital association", pointer to App. F. | NTC3 4-1, 2-11, 4-5 |

## Appendix (headings and bullets A–J unchanged)

| # | Location | Change | Source |
|---|---|---|---|
| U43 | B | IMD note marks "most … are IMDs" and "certain demonstrations" as not yet sourced; rural note cites Section 71116; new note on the freeze/threshold split of the $198.7 billion. | NTC3 4-8; Len |
| U44 | C | Stated-limits note split into [I] limits and [E] CMS facts; new note on step 1's data sources. | NTC3 4-9; Len |
| U45 | D | Scope note on the SDP rule's high-savings total (91 FR 30454); "(moved from sec. 4)" removed; low/high labels; 65 percent note cites only 2476-0204. | NTC3 3b-10, 5-11, 5-9, 3b-9, 6-1; Instr. 4 |
| U46 | E | Rounding note fixed and cited; high-savings label. | NTC3 1d-2, 5-9; Instr. 4 |
| U47 | F | $630.9 billion labelled; "Open:" line replaced by a year-basis note; CBPP's $341 billion labelled; netting note absorbs the moved body paragraph, says what the cap test measures and hedges its keyword count. | NTC3 3b-1, 8-1, 6-2, 5-5, 6-4; D2; Instr. 4; Len |
| U48 | G | Restated figure named as POLITICO's; search negatives [I]. | NTC3 6-3, 4-1 |
| U49 | H | New notes: share of spending above the caps by state (moved from sec. 6); Texas and other state dollars; Alabama and Wyoming flags. | Len |

## Pinpoints from new-text check

Each Federal Register pinpoint below appears in v4 because `new_text_check_v3.md` quotes or reads it from the Federal Register text, not because the Citation check or a verification row confirms it. **Each is: pinpoint from new-text check; re-check in ledger delta.**

| Pinpoint | v4 use |
|---|---|
| 91 FR 46565, 46576, 46598 | Threshold schedule (sec. 1 source note) |
| 91 FR 30453 | −$5.34 billion as federal plus state spending; extension to other services priced separately; SDP rule defers its interaction analysis to future rulemaking (sec. 1, sec. 3, sec. 9 item 2) |
| 91 FR 30456 | −$2.44 billion in 2026 dollars (sec. 1) |
| 91 FR 30451–30452 | Tables 18–20 priced under Section 71116; year columns labelled fiscal years (sec. 3; App. D, App. F) |
| 91 FR 30452 | 80 to 90 percent of SDPs, by the end of 2025, on preprint data (sec. 2) |
| 91 FR 30454 | High-savings total includes the additional services (App. D) |
| 91 FR 30450 | Cap defaults to the state plan rate where no Medicare rate exists (sec. 8) |
| 91 FR 46589 | $98.6 billion for calendar year 2026; freeze begins October 1, 2026; taxes not in place on July 4, 2025 could not continue past October 1, 2026 (sec. 1, sec. 3, sec. 7 step 2, App. F) |
| 91 FR 46591 | Provider tax rule: largest decreases expected on hospitals (sec. 4) |
| 91 FR 46583 | Data states would file with CMS (sec. 9 item 8) |
| 91 FR 30453–30454, 46591–46594 | Each set of assumptions applied nationally (sec. 3) |

## Re-check list (your decision 3)

Existing v16 citations with no verification row. v4 keeps each unchanged.

| Citation | Where in v4 |
|---|---|
| GAO-24-106202, Table 4 | Sec. 2 |
| GAO-23-105515; Michelson et al., December 2024; Lindenfeld et al., PLoS Medicine, July 2025 | Sec. 8 |
| Texas Tribune, September 17, 2026; Fierce Healthcare, September 18, 2026 | Sec. 9 item 5 |
| CMS-2450 (RIN 0938-AV70), its agenda entry and the May 12, 2026 review date; reginfo.gov | Sec. 9 items 3–4; App. I |
| S. 2279, H.R. 4807 and their status; "as of September 22, 2026" | Sec. 9 item 7; App. I |
| Georgetown University Center for Children and Families, July 27, 2026 | Sec. 5, HFMA |
| Texas Hospital Association, paired gross and net figures, 2025 | App. F; sec. 9 item 10 |
| KFF, August 14, 2026 (state file, expansion tracker, $155 billion); HFMA, July 22, 2026; POLITICO, September 2, 2026; ASPE, August 12, 2026 | Secs. 5–6; App. H |
| SDP preprint, Section VI (financing fields) | Sec. 7 step 3 |
| Fifth Circuit No. 25-40766 and its June 24, 2026 status (research note, unverified) | Sec. 9 item 6 |
| Statutory page for Section 71116's rural rule and rural definition | Sec. 8; App. B |
| A source for "most freestanding psychiatric hospitals are IMDs" and the demonstration exception | Sec. 8; App. B |

Still on the earlier citation-to-add list and not resolved here: 91 FR 46594 (F-011 repeated for the low-savings estimate); CRS R48633, if wanted.
