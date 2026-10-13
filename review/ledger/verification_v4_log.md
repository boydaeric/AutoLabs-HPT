# Verification log: evidence ledger v4 flagged rows

*Verifier's file, October 13, 2026. Covers the 91 rows of `261011_Evidence_Ledger_v4.md` and `261011_Evidence_Ledger_SectionA_v4.xlsx` whose Status ended in NEEDS VERIFICATION. The draft checked against is `review/drafts/Exposure-Not-Loss-v17-draft.docx` (its text is word for word `review/article_v4.md`).*

**What was done.** Each flagged row was checked against the primary source it names, in the order requested: [CM] Federal Register pinpoints, [DL4] comment IDs, [DL3] re-check items (rows cited in the Executive summary and secs. 3–5 first), then AC-14. A row **matches** when the source says what the row claims at the pinpoint given; the flag is removed and the base status kept or upgraded. A row is **corrected** when the source says something different; the ledger's Status records the source's wording (24 words or fewer), the pinpoint and what v17 must change. A row stays flagged with “blocked: <host>” when the source's host refused the connection from this session, or “not found” when the source was reachable but the item was not in it. For [DL3], the rows cited in the Executive summary and secs. 3–5 (POLITICO, HFMA, Georgetown CCF, ASPE, KFF and CBO items: SB-01 to SB-03, SB-18, TP-01, TP-04, TP-08, TP-10 to TP-15, TP-23, TP-24, TP-26) were attempted first; every one of those sources sits on a host this session's network policy refused, so they stay flagged. The rest followed. No match was inferred: every matched phrase and every quotation was found by script in the downloaded text, except for the four rows on Lindenfeld et al., which were read through the PubMed connector (section 4). Only the Cross-check and Status columns of flagged rows were edited, plus the Legend, the title line ([FIRM] → THEIA Services) and the coverage and vocabulary notes, mirrored in both files.

## Summary

| Result | Rows |
|---|---|
| match | 34 |
| corrected | 8 |
| blocked | 47 |
| not found | 2 |
| **total flagged on October 11** | 91 |

## 1. Row results

Ledger order. "Result" is for the row as a whole after every tag it carries was checked; a match removes the flag. For corrected rows the source's wording (24 words or fewer) is in the Status column of both ledger files and repeated here.

| ID | Tag | Result | Source and pinpoint | Change needed in v17 |
|---|---|---|---|---|
| RM-10 | DL3 | blocked: www.reginfo.gov | not read: www.reginfo.gov refused the connection | None until the source is read. |
| RM-13 | CM | match | 91 FR 30452 (CMS-2449-P) | None. |
| RM-14 | CM | match | 91 FR 46589 (CMS-2452-P) | None. |
| RM-16 | DL3 | match (upgraded) | P.L. 119-21 § 71116(b), 139 Stat. 303 | None required. |
| RM-17 | DL3 | match (upgraded) | P.L. 119-21 § 71116(d)(2), 139 Stat. 304 | None required. |
| RM-18 | CM/DL3 | **corrected**. Source: “we propose to use the most recent and complete Medicare cost report … for the purpose of establishing the prospective SDP payment limit” | 91 FR 30414 (CMS-2449-P; cost-report proposal and the alternative not proposed); 91 FR 30450 (general default); P.L. 119-21 § 71116(a), 139 Stat. 303 (statutory default) | Sec. 8, 'Rural hospitals' ¶2: replace 'are paid on cost and have no published Medicare rate, so their cap defaults to the state Medicaid plan rate (91 FR 30450) [E], which may leave little or no room for SDPs above base rates. [I]' with: CMS proposes to set these hospitals' SDP limit from their most recent Medicare cost report; a default to the state plan rate was an alternative it did not propose (91 FR 30414). [E] Drop or rework the [I] 'little or no room' clause (AC-16). The Virginia comment sentence (1916-0755) can stay; it concerns services with no Medicare equivalent. |
| RM-19 | CM | **corrected**. Source: “We are proposing that this information be provided by December 31, 2026, in a form and manner specified by CMS.” | 91 FR 46583; Table 1, 91 FR 46578; 91 FR 46574 (CMS-2452-P) | Sec. 9 item 8: replace 'Interim provider tax data states would file with CMS under the proposed rule for the quarter ending December 31, 2026, the first basis for calculating a state's lower threshold (91 FR 46583) [I]' with: interim provider tax data for the state fiscal year that contains July 4, 2025, which states would file by December 31, 2026 and from which CMS would calculate an interim threshold for state planning (91 FR 46583) [E]. Rest of the item unchanged. |
| RM-23 | DL3 | blocked: www.reginfo.gov | not read: www.reginfo.gov refused the connection | None until the source is read. |
| RM-24 | DL3 | blocked: www.reginfo.gov | not read: www.reginfo.gov refused the connection | None until the source is read. |
| RM-25 | DL3 | blocked: www.texastribune.org; www.fiercehealthcare.com | not read: www.texastribune.org; www.fiercehealthcare.com refused the connection | None until the source is read. |
| RM-26 | DL3 | not found | Fifth Circuit opinion search, www.ca5.uscourts.gov/opinions/search (0 results) | None; sec. 9 item 6 already attributes the number and status to an unverified research note. |
| RM-28 | CM/DL3 | match (upgraded) | 91 FR 46565, 46576, 46598, 46562 (CMS-2452-P); P.L. 119-21 § 71115(a)(2), 139 Stat. 302 | None required. |
| RM-29 | CM | match | 91 FR 46565, 46576 (CMS-2452-P) | None. |
| RM-30 | DL3 | match (upgraded) | 91 FR 46562, 46581 (CMS-2452-P); 91 FR 30453, 30456 (CMS-2449-P) | None. |
| RM-31 | CM | match (upgraded) | 91 FR 30453 (CMS-2449-P) | None. |
| RM-32 | DL3 | blocked: www.reginfo.gov | not read: www.reginfo.gov refused the connection | None until the source is read. |
| RM-34 | DL4 | match (upgraded) | regulations.gov API (meta.totalElements, October 13, 2026); full comment download | None. |
| RM-36 | DL4 | match (upgraded) | Comments CMS-2026-2476-0199, CMS-2026-1916-0958; search of both dockets | None required. |
| RM-42 | CM | match | 91 FR 46572, 46598 (CMS-2452-P) | None. |
| RM-45 | DL3 | blocked: www.medicaid.gov | not read: www.medicaid.gov refused the connection | None until the source is read. |
| RM-46 | CM | **corrected**. Source: “in some cases, these taxes would be ineligible to remain in place beyond October 1, 2026 under the provisions of this proposed rule” | 91 FR 46589 (CMS-2452-P) | Sec. 7, step 2: replace 'since CMS says taxes not in place on that date could not continue past October 1, 2026 (91 FR 46589) [E]' with 'since CMS says such taxes would in some cases be ineligible to remain in place beyond October 1, 2026 (91 FR 46589) [E]', and soften the [I] 'It is zero in non-expansion states unless …' to match (for example 'usually zero'). |
| CE-05 | CM | match (upgraded) | 91 FR 30456, Table 27 (CMS-2449-P) | None required. Optional: the sec. 1 source note could also say the −$2.44 billion is federal plus state (total computable). |
| CE-06 | CM | match (upgraded) | 91 FR 30453, Table 21 (CMS-2449-P) | None required. Optional: the sec. 1 source note could add that the −$5.34 billion is also in 2026 dollars (Table 21 caption). |
| CE-56 | CM | match (upgraded) | 91 FR 30451–30452 (Tables 18–20), 91 FR 30453 (Table 21) (CMS-2449-P) | None. |
| CE-57 | CM | match (upgraded) | 91 FR 30451–30452 (Tables 18–20), 91 FR 30447 (CMS-2449-P) | None. |
| CE-58 | CM | match (upgraded) | 91 FR 46589 (CMS-2452-P) | None. |
| CE-61 | CM | **corrected**. Source: “we have developed low and high scenarios to account for the potential differences in relative prices” | 91 FR 30453 (CMS-2449-P); 91 FR 46593 (CMS-2452-P); searched 30453–30454, 46591–46594 | Sec. 3 ¶3: replace 'CMS applies each set of assumptions nationally (91 FR 30453–30454, 46591–46594) [E], so …' with: 'CMS states each scenario's assumptions as single values, not by state (91 FR 30453–30454, 46593–46594) [E]; THEIA Services reads them as applying nationally, so …' and tag the reading [I]. |
| CE-64 | CM | match (upgraded) | 91 FR 46591 (CMS-2452-P) | None. |
| CE-71 | CM | match (upgraded) | 91 FR 30454, 30451–30452 (CMS-2449-P) | None. |
| SB-01 | DL3 | blocked: www.politico.com | not read: www.politico.com refused the connection | None until the source is read. |
| SB-02 | DL3 | blocked: www.politico.com | not read: www.politico.com refused the connection | None until the source is read. |
| SB-03 | DL3 | blocked: www.politico.com | not read: www.politico.com refused the connection | None until the source is read. |
| SB-12 | DL4 | match | Comment CMS-2026-2476-0079 (comment text); full-docket search | None. |
| SB-18 | DL3 | blocked: www.politico.com; www.cbo.gov | not read: www.politico.com; www.cbo.gov refused the connection | None until the source is read. |
| SB-32 | DL4 | match (upgraded) | Comments CMS-2026-2476-0201 p. 1; -0029 p. 1; -0097 p. 17, -0187 p. 18, -0195 p. 21; -0126 p. 1; -0089 p. 1 | None. |
| SB-33 | DL4 | match (upgraded) | Full CMS-2026-1916 docket; comments -0902 p. 1, -0128 p. 5, -0756 p. 2 | None. |
| TP-01 | DL3 | blocked: www.hfma.org | not read: www.hfma.org refused the connection | None until the source is read. |
| TP-04 | DL3 | blocked: www.hfma.org | not read: www.hfma.org refused the connection | None until the source is read. |
| TP-08 | DL3 | blocked: ccf.georgetown.edu | not read: ccf.georgetown.edu refused the connection | None until the source is read. |
| TP-10 | DL3 | blocked: aspe.hhs.gov | not read: aspe.hhs.gov refused the connection | None until the source is read. |
| TP-11 | DL3 | blocked: aspe.hhs.gov | not read: aspe.hhs.gov refused the connection | None until the source is read. |
| TP-12 | DL3 | blocked: aspe.hhs.gov | not read: aspe.hhs.gov refused the connection | None until the source is read. |
| TP-13 | DL3 | blocked: aspe.hhs.gov | not read: aspe.hhs.gov refused the connection | None until the source is read. |
| TP-14 | DL3 | blocked: aspe.hhs.gov | not read: aspe.hhs.gov refused the connection | None until the source is read. |
| TP-15 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| TP-17 | DL3 | blocked: www.tha.org | not read: www.tha.org refused the connection | None until the source is read. |
| TP-21 | DL4 | match (upgraded) | Comment CMS-2026-1916-0676, p. 2 of 45 (also pp. 8–9) | None. |
| TP-23 | DL3 | blocked: www.hfma.org | not read: www.hfma.org refused the connection | None until the source is read. |
| TP-24 | DL3 | blocked: www.hfma.org | not read: www.hfma.org refused the connection | None until the source is read. |
| TP-26 | DL3 | blocked: aspe.hhs.gov | not read: aspe.hhs.gov refused the connection | None until the source is read. |
| TP-29 | DL4 | match (upgraded) | Full CMS-2026-2476 docket; comments -0049 p. 2, -0085 p. 1, -0190 p. 2, -0201 p. 1, -0212 p. 6 | None. |
| TP-30 | DL3 | blocked: www.gao.gov; files.gao.gov | not read: www.gao.gov; files.gao.gov refused the connection | None until the source is read. |
| TP-31 | DL4 | match | Comment CMS-2026-2476-0114, pp. 13–14 of 14 | None. |
| TP-32 | DL4 | match (upgraded) | Comment CMS-2026-2476-0204, p. 10; 91 FR 46592 | None. |
| TP-33 | DL4 | match (upgraded) | Comments CMS-2026-1916-0417, p. 6; -0509, p. 38; -0648, p. 3 | None. |
| TP-34 | DL4 | match (upgraded) | Comments CMS-2026-2476-0145, pp. 3–4; -0093, p. 8; -0101, p. 1; -0091, p. 27 | None. |
| TP-35 | DL4 | match (upgraded) | Comment CMS-2026-1916-0755, p. 3 of 5 | None. |
| TP-36 | DL4 | match (upgraded) | Comment CMS-2026-2476-0130, pp. 1–2 | None. |
| TP-37 | DL4 | match (upgraded) | Comments CMS-2026-1916-0928 p. 11; -0923 p. 3; -0369, -0476, -0808, -0437, -0424, -0787; full-docket keyword count | None. |
| TP-38 | DL3 | blocked: www.tha.org | not read: www.tha.org refused the connection | None until the source is read. |
| TP-40 | DL4 | **corrected**. Source: “We believe CMS has far exceeded its statutory authority to interpret and implement Public Law 119-21 (H.R. 1) and the Social Security Act” | Comment CMS-2026-1916-0407, p. 1 of 7; full-docket count; CMS-2026-1916-0288, p. 2 | App. I, 'Draft note, the legal record': the example '(… for example, comment CMS-2026-1916-0407, p. 1)' sits with the Loper Bright count but that comment does not cite Loper Bright. Either attach -0407 to 'arguments a legal challenge could use' or replace it with a comment that cites Loper Bright, for example CMS-2026-1916-0288, p. 2. |
| SE-01 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-02 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-03 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-04 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-05 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-06 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-07 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-08 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-09 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-10 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-11 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-12 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-13 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-14 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-16 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-20 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| SE-24 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| AC-07 | DL3 | match | Lindenfeld et al., PLoS Med 2025, Results ¶1 and abstract (PMC12310024) | None required. |
| AC-08 | DL3 | **corrected**. Source: “For all types of IPBs, the average annual percent change over the study period was not significant” | Lindenfeld et al., PLoS Med 2025, Results ¶1, Fig 1 note, Tables 2–3 (PMC12310024) | Sec. 8, psychiatry bullet: replace 'with no statistically significant trend for any type of bed' with 'and the average annual percent change was not significant for any type of bed, although the authors' regression models show a significant yearly decline in general hospitals' psychiatric beds'. Same change in the [Figure 8] caption (FG-08). |
| AC-09 | DL3 | blocked: www.gao.gov; files.gao.gov | not read: www.gao.gov; files.gao.gov refused the connection | None until the source is read. |
| AC-10 | DL3 | blocked: jamanetwork.com; pmc.ncbi.nlm.nih.gov | not read: jamanetwork.com; pmc.ncbi.nlm.nih.gov refused the connection | None until the source is read. The citation 'Michelson et al., December 2024' should say JAMA Pediatrics (print February 2025) once read. |
| AC-11 | DL3 | match | Lindenfeld et al., PLoS Med 2025, abstract and Results ¶1 (PMC12310024) | None required. |
| AC-14 | DL3 | not found | none found; searches listed in the Cross-check | None required: v17 already tags the sentence [I] and App. B says it is not yet sourced. If a source is wanted, MACPAC's IMD work is the likely place (not reachable here). |
| AC-15 | DL3 | match (upgraded) | 81 FR 27562 (FR Doc. 2016-09581) | None required; see optional. |
| NC-06 | DL3 | blocked: www.reginfo.gov | not read: www.reginfo.gov refused the connection | None until the source is read. |
| NC-15 | DL3 | match | govinfo BILLSTATUS-119s2279.xml and BILLSTATUS-119hr4807.xml | None required. |
| NC-17 | DL4 | **corrected**. Source: “The Medicaid and CHIP Payment and Access Commission (MACPAC) appreciates the opportunity to comment on the notice of proposed rulemaking” | Comments CMS-2026-2476-0173 (p. 1), -0148, -0116, -0109, -0057, -0079; full-docket search | App. G, 'Draft note, comment records': change 'Of six September 21, 2026 letters earlier not located, four are now posted (… -0148, -0116, -0109 and -0057)' to five, adding MACPAC (comment CMS-2026-2476-0173), and remove MACPAC from 'found no letters from MACPAC, the Illinois Health and Hospital Association or the Illinois Attorney General'. Optional: California's letter is dated September 18, 2026, so 'letters sent for the September 21, 2026 deadline' is more exact. |
| FG-06 | DL3 | blocked: www.kff.org; files.kff.org | not read: www.kff.org; files.kff.org refused the connection | None until the source is read. |
| FG-07 | DL3 | blocked: jamanetwork.com; pmc.ncbi.nlm.nih.gov | not read: jamanetwork.com; pmc.ncbi.nlm.nih.gov refused the connection | None until the source is read. The citation 'Michelson et al., December 2024' should say JAMA Pediatrics (print February 2025) once read. |
| FG-08 | DL3 | **corrected**. Source: “For all types of IPBs, the average annual percent change over the study period was not significant” | Lindenfeld et al., PLoS Med 2025, Results ¶1, Fig 1, Tables 2–3 (PMC12310024) | Sec. 8, [Figure 8] caption: replace 'the authors found no statistically significant trend for any type of bed' with 'the average annual percent change was not significant for any type of bed'. |

## 2. Changes v17 needs, by section

Required changes come from corrected rows. Optional ones are improvements a matched row suggests; v17 is accurate without them.

### Sec. 1

- **RM-28** (optional). Threshold table source note: add the statute pinpoint '(P.L. 119-21, § 71115(a)(2), 139 Stat. 302)'.
- **CE-05** (optional). SDP table source note: add that the −$2.44 billion is also federal plus state (total computable), 91 FR 30456.
- **CE-06** (optional). SDP table source note: add that the −$5.34 billion is also in 2026 dollars (Table 21 caption, 91 FR 30453).

### Sec. 3

- **CE-61** (required). Sec. 3 ¶3: replace 'CMS applies each set of assumptions nationally (91 FR 30453–30454, 46591–46594) [E], so …' with: 'CMS states each scenario's assumptions as single values, not by state (91 FR 30453–30454, 46593–46594) [E]; THEIA Services reads them as applying nationally, so …' and tag the reading [I].

### Sec. 7

- **RM-46** (required). Sec. 7, step 2: replace 'since CMS says taxes not in place on that date could not continue past October 1, 2026 (91 FR 46589) [E]' with 'since CMS says such taxes would in some cases be ineligible to remain in place beyond October 1, 2026 (91 FR 46589) [E]', and soften the [I] 'It is zero in non-expansion states unless …' to match (for example 'usually zero').

### Sec. 8

- **RM-18** (required). Sec. 8, 'Rural hospitals' ¶2: replace 'are paid on cost and have no published Medicare rate, so their cap defaults to the state Medicaid plan rate (91 FR 30450) [E], which may leave little or no room for SDPs above base rates. [I]' with: CMS proposes to set these hospitals' SDP limit from their most recent Medicare cost report; a default to the state plan rate was an alternative it did not propose (91 FR 30414). [E] Drop or rework the [I] 'little or no room' clause (AC-16). The Virginia comment sentence (1916-0755) can stay; it concerns services with no Medicare equivalent.
- **AC-08** (required). Sec. 8, psychiatry bullet: replace 'with no statistically significant trend for any type of bed' with 'and the average annual percent change was not significant for any type of bed, although the authors' regression models show a significant yearly decline in general hospitals' psychiatric beds'. Same change in the [Figure 8] caption (FG-08).
- **FG-08** (required). Sec. 8, [Figure 8] caption: replace 'the authors found no statistically significant trend for any type of bed' with 'the average annual percent change was not significant for any type of bed'.
- **RM-16** (optional). Rural ¶1: add the pinpoint '(P.L. 119-21, § 71116(b), 139 Stat. 303)'.
- **AC-11** (optional). Psychiatry bullet and Figure 8: either keep the abstract's 11.3 and 9.06 and note that the Results give 11.2 and 8.9, or use the Results figures, which sum to the published 28.4.
- **AC-15** (optional). IMD sentence: retag 'certain demonstrations' [E] and cite 81 FR 27562 (section 1115(a) demonstrations under SMDL #15-003).

### Sec. 9

- **RM-19** (required). Sec. 9 item 8: replace 'Interim provider tax data states would file with CMS under the proposed rule for the quarter ending December 31, 2026, the first basis for calculating a state's lower threshold (91 FR 46583) [I]' with: interim provider tax data for the state fiscal year that contains July 4, 2025, which states would file by December 31, 2026 and from which CMS would calculate an interim threshold for state planning (91 FR 46583) [E]. Rest of the item unchanged.
- **NC-15** (optional). Item 7 / App. I: the bill limb can be dated October 13, 2026 (govinfo bill status); keep September 22, 2026 for the litigation limb.

### App. B

- **RM-17** (optional). Rural hospitals note: add the pinpoint '(P.L. 119-21, § 71116(d)(2), 139 Stat. 304)'.
- **AC-15** (optional). IMD note: drop 'the exception for certain demonstrations … not yet sourced'; cite 81 FR 27562.

### App. G

- **NC-17** (required). App. G, 'Draft note, comment records': change 'Of six September 21, 2026 letters earlier not located, four are now posted (… -0148, -0116, -0109 and -0057)' to five, adding MACPAC (comment CMS-2026-2476-0173), and remove MACPAC from 'found no letters from MACPAC, the Illinois Health and Hospital Association or the Illinois Attorney General'. Optional: California's letter is dated September 18, 2026, so 'letters sent for the September 21, 2026 deadline' is more exact.

### App. I

- **TP-40** (required). App. I, 'Draft note, the legal record': the example '(… for example, comment CMS-2026-1916-0407, p. 1)' sits with the Loper Bright count but that comment does not cite Loper Bright. Either attach -0407 to 'arguments a legal challenge could use' or replace it with a comment that cites Loper Bright, for example CMS-2026-1916-0288, p. 2.
- **RM-36** (optional). Methods note: name the moved letter (comment CMS-2026-2476-0199, the same text as CMS-2026-1916-0958).

## 3. Rows still flagged

| ID | Tag still flagged | Result | Host or search | What was tried |
|---|---|---|---|---|
| RM-10 | DL3 | blocked | www.reginfo.gov | reginfo.gov's EO 12866 review list could not be fetched: the proxy refused www.reginfo.gov. |
| RM-23 | DL3 | blocked | www.reginfo.gov | reginfo.gov could not be fetched (www.reginfo.gov refused). The federalregister.gov API (reachable) lists no Federal Register document under RIN 0938-AV70. |
| RM-24 | DL3 | blocked | www.reginfo.gov | reginfo.gov could not be fetched (www.reginfo.gov refused). The federalregister.gov API (reachable) lists no Federal Register document under RIN 0938-AV70. |
| RM-25 | DL3 | blocked | www.texastribune.org; www.fiercehealthcare.com | The Texas Tribune (September 17, 2026) and Fierce Healthcare (September 18, 2026) articles could not be fetched: the proxy refused both hosts. |
| RM-26 | DL3 | not found | PACER (docket); courtlistener.com | Fifth Circuit opinion search (reachable): 0 results for 25-40766. Docket sheet needs PACER; courtlistener.com refused. |
| RM-32 | DL3 | blocked | www.reginfo.gov | reginfo.gov's EO 12866 review list could not be fetched: the proxy refused www.reginfo.gov. |
| RM-45 | DL3 | blocked | www.medicaid.gov | The SDP preprint form could not be fetched: the proxy refused www.medicaid.gov. Neither proposed rule reproduces the form's Section VI (searched 91 FR 30400–30466 and 46562–46599 by script), and no comment in either docket reproduces it (full-docket search). |
| SB-01 | DL3 | blocked | www.politico.com | POLITICO's September 2, 2026 article could not be fetched: the proxy refused www.politico.com. |
| SB-02 | DL3 | blocked | www.politico.com | POLITICO's September 2, 2026 article could not be fetched: the proxy refused www.politico.com. |
| SB-03 | DL3 | blocked | www.politico.com | POLITICO's September 2, 2026 article could not be fetched: the proxy refused www.politico.com. |
| SB-18 | DL3 | blocked | www.politico.com; www.cbo.gov | POLITICO's September 2, 2026 article (www.politico.com refused) and CBO's July 21, 2025 table (www.cbo.gov answered 403) could not be fetched. |
| TP-01 | DL3 | blocked | www.hfma.org | HFMA's July 22, 2026 article could not be fetched: the proxy refused www.hfma.org. |
| TP-04 | DL3 | blocked | www.hfma.org | HFMA's July 22, 2026 article could not be fetched: the proxy refused www.hfma.org. |
| TP-08 | DL3 | blocked | ccf.georgetown.edu | Georgetown CCF's July 27, 2026 post could not be fetched: the proxy refused ccf.georgetown.edu. CCF's own comment on CMS-2452-P (CMS-2026-2476-0029) is posted, but it is not the cited post. |
| TP-10 | DL3 | blocked | aspe.hhs.gov | ASPE's August 12, 2026 report could not be fetched: the proxy refused aspe.hhs.gov. (Paragon's comment CMS-2026-2476-0130 cites the report's URL but does not attach it.) |
| TP-11 | DL3 | blocked | aspe.hhs.gov | ASPE's August 12, 2026 report could not be fetched: the proxy refused aspe.hhs.gov. (Paragon's comment CMS-2026-2476-0130 cites the report's URL but does not attach it.) |
| TP-12 | DL3 | blocked | aspe.hhs.gov | ASPE's August 12, 2026 report could not be fetched: the proxy refused aspe.hhs.gov. (Paragon's comment CMS-2026-2476-0130 cites the report's URL but does not attach it.) |
| TP-13 | DL3 | blocked | aspe.hhs.gov | ASPE's August 12, 2026 report could not be fetched: the proxy refused aspe.hhs.gov. (Paragon's comment CMS-2026-2476-0130 cites the report's URL but does not attach it.) |
| TP-14 | DL3 | blocked | aspe.hhs.gov | ASPE's August 12, 2026 report could not be fetched: the proxy refused aspe.hhs.gov. (Paragon's comment CMS-2026-2476-0130 cites the report's URL but does not attach it.) |
| TP-15 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief could not be fetched (www.kff.org refused). |
| TP-17 | DL3 | blocked | www.tha.org | The Texas Hospital Association's 2025 publication with paired gross and net figures could not be fetched: the proxy refused www.tha.org. THA's comment on CMS-2452-P (CMS-2026-2476-0109) is posted but is not the cited publication. |
| TP-23 | DL3 | blocked | www.hfma.org | HFMA's July 22, 2026 article could not be fetched (www.hfma.org refused). |
| TP-24 | DL3 | blocked | www.hfma.org | HFMA's July 22, 2026 article could not be fetched (www.hfma.org refused). |
| TP-26 | DL3 | blocked | aspe.hhs.gov | ASPE's August 12, 2026 report could not be fetched: the proxy refused aspe.hhs.gov. (Paragon's comment CMS-2026-2476-0130 cites the report's URL but does not attach it.) |
| TP-30 | DL3 | blocked | www.gao.gov; files.gao.gov | GAO-24-106202 could not be fetched: the proxy refused www.gao.gov and files.gao.gov; govinfo's GAO collection does not carry it. |
| TP-38 | DL3 | blocked | www.tha.org | The Texas Hospital Association's 2025 publication with paired gross and net figures could not be fetched: the proxy refused www.tha.org. THA's comment on CMS-2452-P (CMS-2026-2476-0109) is posted but is not the cited publication. |
| SE-01 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-02 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-03 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-04 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-05 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-06 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-07 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-08 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-09 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-10 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-11 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-12 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-13 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-14 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-16 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-20 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| SE-24 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| AC-09 | DL3 | blocked | www.gao.gov; files.gao.gov | GAO-23-105515 could not be fetched: the proxy refused www.gao.gov and files.gao.gov. |
| AC-10 | DL3 | blocked | jamanetwork.com; pmc.ncbi.nlm.nih.gov | Michelson, Cushing and Bucholz, 'National Trends in Pediatric Inpatient Capacity', JAMA Pediatrics 179(2):208–209 (doi:10.1001/jamapediatrics.2024.5110; PMC11612914). PubMed has no abstract, the PubMed connector returned no full text, and the proxy refused jamanetwork.com, pmc.ncbi.nlm.nih.gov and europepmc.org. |
| AC-14 | DL3 | not found | www.macpac.gov; www.kff.org | federalregister.gov full-text API (6 queries); 4 FR documents read on govinfo; PubMed (4 hits, no full text); Lindenfeld et al. 2025. |
| NC-06 | DL3 | blocked | www.reginfo.gov | reginfo.gov's EO 12866 review list could not be fetched: the proxy refused www.reginfo.gov. |
| FG-06 | DL3 | blocked | www.kff.org; files.kff.org | KFF's August 14, 2026 brief, state file and expansion tracker could not be fetched: the proxy refused www.kff.org and files.kff.org. |
| FG-07 | DL3 | blocked | jamanetwork.com; pmc.ncbi.nlm.nih.gov | Michelson, Cushing and Bucholz, 'National Trends in Pediatric Inpatient Capacity', JAMA Pediatrics 179(2):208–209 (doi:10.1001/jamapediatrics.2024.5110; PMC11612914). PubMed has no abstract, the PubMed connector returned no full text, and the proxy refused jamanetwork.com, pmc.ncbi.nlm.nih.gov and europepmc.org. |

**By host.** PACER (docket): RM-26; aspe.hhs.gov: TP-10, TP-11, TP-12, TP-13, TP-14, TP-26; ccf.georgetown.edu: TP-08; courtlistener.com: RM-26; files.gao.gov: TP-30, AC-09; files.kff.org: TP-15, SE-01, SE-02, SE-03, SE-04, SE-05, SE-06, SE-07, SE-08, SE-09, SE-10, SE-11, SE-12, SE-13, SE-14, SE-16, SE-20, SE-24, FG-06; jamanetwork.com: AC-10, FG-07; pmc.ncbi.nlm.nih.gov: AC-10, FG-07; www.cbo.gov: SB-18; www.fiercehealthcare.com: RM-25; www.gao.gov: TP-30, AC-09; www.hfma.org: TP-01, TP-04, TP-23, TP-24; www.kff.org: TP-15, SE-01, SE-02, SE-03, SE-04, SE-05, SE-06, SE-07, SE-08, SE-09, SE-10, SE-11, SE-12, SE-13, SE-14, SE-16, SE-20, SE-24, AC-14, FG-06; www.macpac.gov: AC-14; www.medicaid.gov: RM-45; www.politico.com: SB-01, SB-02, SB-03, SB-18; www.reginfo.gov: RM-10, RM-23, RM-24, RM-32, NC-06; www.texastribune.org: RM-25; www.tha.org: TP-17, TP-38.

## 4. Method and sources

- **Federal Register.** govinfo.gov PDFs: CMS-2449-P, FR Doc. 2026-10292 (`FR-2026-05-22/pdf/2026-10292.pdf`, 91 FR 30400–30466, 67 pages) and CMS-2452-P, FR Doc. 2026-14897 (`FR-2026-07-23/pdf/2026-14897.pdf`, 91 FR 46562–46599, 38 pages). Text by `pdftotext`, page by page; each page's printed number was checked against its header. Tables printed as images (Tables 17–23 and 27–28 of CMS-2449-P; Table 1 of CMS-2452-P at 46578) were read from 200-dpi page images with Tesseract OCR and by eye.
- **Public comments.** Every comment on both dockets was downloaded on October 13, 2026 with the repository's `collect_comments.py` (regulations.gov v4 API with the key in REGULATIONS_GOV_API_KEY; attachments from downloads.regulations.gov with its browser User-Agent). The collector's report showed no gaps: CMS-2026-1916, 960 comments and 892 attachment files; CMS-2026-2476, 214 and 202. Text came from `pdftotext` page by page, with Tesseract OCR for pages without a text layer, so page pinpoints are PDF pages. Whole-docket counts reuse the analyst's own `extract_comment_text.py`, `comment_text_utils.cluster` (shingle Jaccard 0.5) and `count_themes.py` patterns, so 'distinct texts' means what it meant in the analyst's files.
- **Statute.** P.L. 119-21 from govinfo (`PLAW-119publ21`, HTML), paged by its `[[Page 139 Stat. n]]` markers.
- **Matching.** A Python script normalises case, curly quotes, dashes, line-break hyphens and white space, then requires each phrase (each segment, in order, where a quotation has an ellipsis) to appear on the page cited. Negative findings (for example, that no form of “nation” appears on 91 FR 30453–30454 or 46591–46594) are the same search returning nothing. The script was tested against v17's own wording for the corrected rows and rejects it.
- **Journal articles.** Lindenfeld et al. (PLoS Medicine, 2025) was read in the PubMed Central full text that the PubMed connector returned (PMC12310024; doi:10.1371/journal.pmed.1004682). journals.plos.org, pmc.ncbi.nlm.nih.gov and europepmc.org refused the connection, so the text could not be saved to disk; AC-07, AC-08, AC-11 and FG-08 were compared by reading, not by script, and their ledger rows say so. This departs from the script-matching rule; the quotation recorded for AC-08 and FG-08 was copied from the connector's text. Michelson et al. (JAMA Pediatrics) returned no full text, so AC-10 and FG-07 stay blocked.
- **Other sources.** Bills: govinfo BILLSTATUS XML. Fifth Circuit: www.ca5.uscourts.gov opinion search. Older rules for AC-14 and AC-15: govinfo PDFs found through the federalregister.gov search API.
- **Departure from CONVENTIONS.md, section 5.** The corrected rows quote CMS-2449-P and CMS-2452-P more than once in the ledger and in this log, because the request asks for the source's wording in each corrected row. Each quotation is verbatim and 24 words or fewer.
- **The two unresolved rows.** AC-14 is reported above (not found). NC-19 was left unchanged, as instructed: it closes when Appendix C is written.
- **Knock-on rows not flagged.** A correction can affect a row that was not flagged; these are named in the change list and were not edited: AC-16, which builds on RM-18's cost-paid default; and the comment analyst's `output/comments_tagged.csv`, which tags CMS-2026-2476-0173 (MACPAC) as an individual (NC-17).
