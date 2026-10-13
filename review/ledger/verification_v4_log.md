# Verification log: evidence ledger v4 flagged rows

*Verifier's file, October 13, 2026. Covers the 91 rows of `261011_Evidence_Ledger_v4.md` and `261011_Evidence_Ledger_SectionA_v4.xlsx` whose Status ended in NEEDS VERIFICATION. The draft checked against is `review/drafts/Exposure-Not-Loss-v17-draft.docx` (its text is word for word `review/article_v4.md`).*

**What was done.** Each flagged row was checked against the primary source it names, in the order requested: [CM] Federal Register pinpoints, [DL4] comment IDs, [DL3] re-check items (rows cited in the Executive summary and secs. 3–5 first), then AC-14. A row **matches** when the source says what the row claims at the pinpoint given; the flag is removed and the base status kept or upgraded. A row is **corrected** when the source says something different; the ledger's Status records the source's wording (24 words or fewer), the pinpoint and what v17 must change. A row stays flagged with “blocked: <host>” when the source's host refused the connection from this session, or “not found” when the source was reachable but the item was not in it. No match was inferred: every matched phrase and every quotation was found by script in the downloaded text (section 4). Only the Cross-check and Status columns of flagged rows were edited, plus the Legend, the title line ([FIRM] → THEIA Services) and the coverage and vocabulary notes, mirrored in both files.

## Summary

| Result | Rows |
|---|---|
| match | 13 |
| corrected | 4 |
| blocked | 0 |
| not found | 0 |
| not yet checked | 74 |
| **total flagged on October 11** | 91 |

Rows with two tags whose result covers one tag only (the other tag's flag stays and is reported separately below): RM-18, RM-28.

## 1. Row results

Ledger order. "Result" is for the row as a whole after every tag it carries was checked; a match removes the flag. For corrected rows the source's wording (24 words or fewer) is in the Status column of both ledger files and repeated here.

| ID | Tag | Result | Source and pinpoint | Change needed in v17 |
|---|---|---|---|---|
| RM-10 | DL3 | not yet checked | | |
| RM-13 | CM | match | 91 FR 30452 (CMS-2449-P) | None. |
| RM-14 | CM | match | 91 FR 46589 (CMS-2452-P) | None. |
| RM-16 | DL3 | not yet checked | | |
| RM-17 | DL3 | not yet checked | | |
| RM-18 | CM/DL3 | **corrected**. Source: “we propose to use the most recent and complete Medicare cost report … for the purpose of establishing the prospective SDP payment limit”; [DL3] part pending (group 3) | 91 FR 30414 (CMS-2449-P; cost-report proposal and the alternative not proposed); 91 FR 30450 (general default) | Sec. 8, 'Rural hospitals' ¶2: replace 'are paid on cost and have no published Medicare rate, so their cap defaults to the state Medicaid plan rate (91 FR 30450) [E], which may leave little or no room for SDPs above base rates. [I]' with: CMS proposes to set these hospitals' SDP limit from their most recent Medicare cost report; a default to the state plan rate was an alternative it did not propose (91 FR 30414). [E] Drop or rework the [I] 'little or no room' clause (AC-16). The Virginia comment sentence (1916-0755) can stay; it concerns services with no Medicare equivalent. |
| RM-19 | CM | **corrected**. Source: “We are proposing that this information be provided by December 31, 2026, in a form and manner specified by CMS.” | 91 FR 46583; Table 1, 91 FR 46578; 91 FR 46574 (CMS-2452-P) | Sec. 9 item 8: replace 'Interim provider tax data states would file with CMS under the proposed rule for the quarter ending December 31, 2026, the first basis for calculating a state's lower threshold (91 FR 46583) [I]' with: interim provider tax data for the state fiscal year that contains July 4, 2025, which states would file by December 31, 2026 and from which CMS would calculate an interim threshold for state planning (91 FR 46583) [E]. Rest of the item unchanged. |
| RM-23 | DL3 | not yet checked | | |
| RM-24 | DL3 | not yet checked | | |
| RM-25 | DL3 | not yet checked | | |
| RM-26 | DL3 | not yet checked | | |
| RM-28 | CM/DL3 | match; [DL3] part pending (group 3) | 91 FR 46565, 46576, 46598 (CMS-2452-P) | None for the [CM] part. |
| RM-29 | CM | match | 91 FR 46565, 46576 (CMS-2452-P) | None. |
| RM-30 | DL3 | not yet checked | | |
| RM-31 | CM | match (upgraded) | 91 FR 30453 (CMS-2449-P) | None. |
| RM-32 | DL3 | not yet checked | | |
| RM-34 | DL4 | not yet checked | | |
| RM-36 | DL4 | not yet checked | | |
| RM-42 | CM | match | 91 FR 46572, 46598 (CMS-2452-P) | None. |
| RM-45 | DL3 | not yet checked | | |
| RM-46 | CM | **corrected**. Source: “in some cases, these taxes would be ineligible to remain in place beyond October 1, 2026 under the provisions of this proposed rule” | 91 FR 46589 (CMS-2452-P) | Sec. 7, step 2: replace 'since CMS says taxes not in place on that date could not continue past October 1, 2026 (91 FR 46589) [E]' with 'since CMS says such taxes would in some cases be ineligible to remain in place beyond October 1, 2026 (91 FR 46589) [E]', and soften the [I] 'It is zero in non-expansion states unless …' to match (for example 'usually zero'). |
| CE-05 | CM | match (upgraded) | 91 FR 30456, Table 27 (CMS-2449-P) | None required. Optional: the sec. 1 source note could also say the −$2.44 billion is federal plus state (total computable). |
| CE-06 | CM | match (upgraded) | 91 FR 30453, Table 21 (CMS-2449-P) | None required. Optional: the sec. 1 source note could add that the −$5.34 billion is also in 2026 dollars (Table 21 caption). |
| CE-56 | CM | match (upgraded) | 91 FR 30451–30452 (Tables 18–20), 91 FR 30453 (Table 21) (CMS-2449-P) | None. |
| CE-57 | CM | match (upgraded) | 91 FR 30451–30452 (Tables 18–20), 91 FR 30447 (CMS-2449-P) | None. |
| CE-58 | CM | match (upgraded) | 91 FR 46589 (CMS-2452-P) | None. |
| CE-61 | CM | **corrected**. Source: “we have developed low and high scenarios to account for the potential differences in relative prices” | 91 FR 30453 (CMS-2449-P); 91 FR 46593 (CMS-2452-P); searched 30453–30454, 46591–46594 | Sec. 3 ¶3: replace 'CMS applies each set of assumptions nationally (91 FR 30453–30454, 46591–46594) [E], so …' with: 'CMS states each scenario's assumptions as single values, not by state (91 FR 30453–30454, 46593–46594) [E]; THEIA Services reads them as applying nationally, so …' and tag the reading [I]. |
| CE-64 | CM | match (upgraded) | 91 FR 46591 (CMS-2452-P) | None. |
| CE-71 | CM | match (upgraded) | 91 FR 30454, 30451–30452 (CMS-2449-P) | None. |
| SB-01 | DL3 | not yet checked | | |
| SB-02 | DL3 | not yet checked | | |
| SB-03 | DL3 | not yet checked | | |
| SB-12 | DL4 | not yet checked | | |
| SB-18 | DL3 | not yet checked | | |
| SB-32 | DL4 | not yet checked | | |
| SB-33 | DL4 | not yet checked | | |
| TP-01 | DL3 | not yet checked | | |
| TP-04 | DL3 | not yet checked | | |
| TP-08 | DL3 | not yet checked | | |
| TP-10 | DL3 | not yet checked | | |
| TP-11 | DL3 | not yet checked | | |
| TP-12 | DL3 | not yet checked | | |
| TP-13 | DL3 | not yet checked | | |
| TP-14 | DL3 | not yet checked | | |
| TP-15 | DL3 | not yet checked | | |
| TP-17 | DL3 | not yet checked | | |
| TP-21 | DL4 | not yet checked | | |
| TP-23 | DL3 | not yet checked | | |
| TP-24 | DL3 | not yet checked | | |
| TP-26 | DL3 | not yet checked | | |
| TP-29 | DL4 | not yet checked | | |
| TP-30 | DL3 | not yet checked | | |
| TP-31 | DL4 | not yet checked | | |
| TP-32 | DL4 | not yet checked | | |
| TP-33 | DL4 | not yet checked | | |
| TP-34 | DL4 | not yet checked | | |
| TP-35 | DL4 | not yet checked | | |
| TP-36 | DL4 | not yet checked | | |
| TP-37 | DL4 | not yet checked | | |
| TP-38 | DL3 | not yet checked | | |
| TP-40 | DL4 | not yet checked | | |
| SE-01 | DL3 | not yet checked | | |
| SE-02 | DL3 | not yet checked | | |
| SE-03 | DL3 | not yet checked | | |
| SE-04 | DL3 | not yet checked | | |
| SE-05 | DL3 | not yet checked | | |
| SE-06 | DL3 | not yet checked | | |
| SE-07 | DL3 | not yet checked | | |
| SE-08 | DL3 | not yet checked | | |
| SE-09 | DL3 | not yet checked | | |
| SE-10 | DL3 | not yet checked | | |
| SE-11 | DL3 | not yet checked | | |
| SE-12 | DL3 | not yet checked | | |
| SE-13 | DL3 | not yet checked | | |
| SE-14 | DL3 | not yet checked | | |
| SE-16 | DL3 | not yet checked | | |
| SE-20 | DL3 | not yet checked | | |
| SE-24 | DL3 | not yet checked | | |
| AC-07 | DL3 | not yet checked | | |
| AC-08 | DL3 | not yet checked | | |
| AC-09 | DL3 | not yet checked | | |
| AC-10 | DL3 | not yet checked | | |
| AC-11 | DL3 | not yet checked | | |
| AC-14 | DL3 | not yet checked | | |
| AC-15 | DL3 | not yet checked | | |
| NC-06 | DL3 | not yet checked | | |
| NC-15 | DL3 | not yet checked | | |
| NC-17 | DL4 | not yet checked | | |
| FG-06 | DL3 | not yet checked | | |
| FG-07 | DL3 | not yet checked | | |
| FG-08 | DL3 | not yet checked | | |

## 2. Changes v17 needs, by section

Required changes come from corrected rows. Optional ones are improvements a matched row suggests; v17 is accurate without them.

### Sec. 1

- **CE-05** (optional). SDP table source note: add that the −$2.44 billion is also federal plus state (total computable), 91 FR 30456.
- **CE-06** (optional). SDP table source note: add that the −$5.34 billion is also in 2026 dollars (Table 21 caption, 91 FR 30453).

### Sec. 3

- **CE-61** (required). Sec. 3 ¶3: replace 'CMS applies each set of assumptions nationally (91 FR 30453–30454, 46591–46594) [E], so …' with: 'CMS states each scenario's assumptions as single values, not by state (91 FR 30453–30454, 46593–46594) [E]; THEIA Services reads them as applying nationally, so …' and tag the reading [I].

### Sec. 7

- **RM-46** (required). Sec. 7, step 2: replace 'since CMS says taxes not in place on that date could not continue past October 1, 2026 (91 FR 46589) [E]' with 'since CMS says such taxes would in some cases be ineligible to remain in place beyond October 1, 2026 (91 FR 46589) [E]', and soften the [I] 'It is zero in non-expansion states unless …' to match (for example 'usually zero').

### Sec. 8

- **RM-18** (required). Sec. 8, 'Rural hospitals' ¶2: replace 'are paid on cost and have no published Medicare rate, so their cap defaults to the state Medicaid plan rate (91 FR 30450) [E], which may leave little or no room for SDPs above base rates. [I]' with: CMS proposes to set these hospitals' SDP limit from their most recent Medicare cost report; a default to the state plan rate was an alternative it did not propose (91 FR 30414). [E] Drop or rework the [I] 'little or no room' clause (AC-16). The Virginia comment sentence (1916-0755) can stay; it concerns services with no Medicare equivalent.

### Sec. 9

- **RM-19** (required). Sec. 9 item 8: replace 'Interim provider tax data states would file with CMS under the proposed rule for the quarter ending December 31, 2026, the first basis for calculating a state's lower threshold (91 FR 46583) [I]' with: interim provider tax data for the state fiscal year that contains July 4, 2025, which states would file by December 31, 2026 and from which CMS would calculate an interim threshold for state planning (91 FR 46583) [E]. Rest of the item unchanged.

## 3. Rows still flagged

None so far.

## 4. Method and sources

- **Federal Register.** govinfo.gov PDFs: CMS-2449-P, FR Doc. 2026-10292 (`FR-2026-05-22/pdf/2026-10292.pdf`, 91 FR 30400–30466, 67 pages) and CMS-2452-P, FR Doc. 2026-14897 (`FR-2026-07-23/pdf/2026-14897.pdf`, 91 FR 46562–46599, 38 pages). Text by `pdftotext`, page by page; each page's printed number was checked against its header. Tables printed as images (Tables 17–23 and 27–28 of CMS-2449-P; Table 1 of CMS-2452-P at 46578) were read from 200-dpi page images with Tesseract OCR and by eye.
- **Statute.** P.L. 119-21 from govinfo (`PLAW-119publ21`, HTML), paged by its `[[Page 139 Stat. n]]` markers.
- **Matching.** A Python script normalises case, curly quotes, dashes, line-break hyphens and white space, then requires each phrase (each segment, in order, where a quotation has an ellipsis) to appear on the page cited. Negative findings (for example, that no form of “nation” appears on 91 FR 30453–30454 or 46591–46594) are the same search returning nothing. The script was tested against v17's own wording for the corrected rows and rejects it.
- **Departure from CONVENTIONS.md, section 5.** The corrected rows quote CMS-2449-P and CMS-2452-P more than once in the ledger and in this log, because the request asks for the source's wording in each corrected row. Each quotation is verbatim and 24 words or fewer.
- **Knock-on rows not flagged.** A correction can affect a row that was not flagged; these are named in the change list and were not edited (AC-16, which builds on RM-18).
