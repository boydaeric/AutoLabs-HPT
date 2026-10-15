# New-text check on v6

*New-text checker, October 15, 2026. This role writes only this file and the Federal Register text files in `review/sources/fr/`. No article, ledger or decision-log file was edited. Follows `review/CONVENTIONS.md`; see "Departure" at the end.*

**Scope.** I diffed `review/article_v5.md` and `review/article_v6.md` sentence by sentence, by script, body and appendix, table cells and captions included.
- **Body:** 30 v6 sentences are new or changed; 16 v5 sentences were removed or rewritten.
- **Appendix:** 34 v6 sentences are new or changed; 26 v5 sentences were removed or rewritten.

Each changed sentence was checked against its row in `decision_log.md` ("New-text check v5 decisions") and `article_changes.md` (W1–W26), the ledger, and the unchanged text. The source checks the writer could not do (step 2) were done against documents downloaded in this session.

## Summary

| Severity | Count |
|---|---:|
| Must fix | 1 |
| Should fix | 2 |
| Optional (decision for Eric) | 1 |
| **Total** | **4** |

**The v5 → v6 changes are clean.**
- Every changed sentence matches its decision-log row, and the change map's W1–W26 cover all of them. I found **no change without a decision-log row**.
- No new error, untagged claim or quote problem was introduced. v6 has the same four quotations as v5, each 24 words or fewer and one per source.
- Changed arithmetic is limited to the corrected keyword counts (12 and 9 in App. F; 9 in App. I), which now match ledger TP-37 and TP-40. No other figure changed; a script compared every number token in v5 and v6, and each difference is accounted for by a logged change.
- "[DATE]" occurs 6 times, as the change map says. "Federal Medicaid payment for IMD patients aged 21 to 64 is restricted by" occurs twice, as the decision log says.

**The source checks settle the four open items, and three of the four results require text changes.**
- **(a) Scenario parameters: all matched.** The 90 and 70 percent parameters and the Medicaid-share point match at 91 FR 46594 and 46593. App. D's hedge sentence is now out of date (NT6-02).
- **(a) 75/75 wording: matched.** The phrase v6 cut matches verbatim at 91 FR 46564, so restoring it is Eric's call (NT6-04).
- **(b) CMS-2448-F: citation confirmed, wording too narrow.** The rule begins at 91 FR 4794 and implements Section 71117. But Section 71117 is a "generally redistributive" test for taxes under a waiver, and CMS applies it to broad-based as well as uniformity waivers, so v6's "waivers of the requirement that provider taxes be uniform" is narrower than the source (NT6-03).
- **(c) Comment CMS-2026-2476-0140: the Illinois Attorney General signed.** Kwame Raoul is a signatory (p. 10), so App. G's scoped negative must be replaced (NT6-01). The Illinois Health and Hospital Association is not among the 24 signatories, and the letter does not contain $681 billion.

**Length.**
- The v6 body is **6,239 words** against the cap of **6,284**: 45 under, which reproduces the writer's count. The appendix is 4,531 words by the same method (4,530 in the writer's count; the one-word difference is the "# Appendix" heading token, as in v5).
- **Every proposed fix is in the appendix; body change 0.** Net change of all fixes: **−7 words** without NT6-04, or **+1** with it.

---

## Findings

| ID | Location | v6 text | Issue | Evidence | Severity | Replacement | Word change |
|---|---|---|---|---|---|---|---:|
| NT6-01 | App. G, “The comment records”, last two sentences | “THEIA Services found the figure in none of them, and, matching by organization name, found no letter from the Illinois Health and Hospital Association or the Illinois Attorney General in the posted docket. [I] It has not checked whether the Illinois Attorney General signed a multistate attorneys general letter filed with a blank organization field (comment CMS-2026-2476-0140). [I]” | v6 scopes the Illinois Attorney General negative and says -0140 was not checked. It now has been, and the Illinois Attorney General co-signed -0140, a posted letter for the September 21 deadline. Read with App. G's list of letters looked for, the v6 text leaves a reader thinking the Illinois Attorney General filed nothing in the docket. The replacement states the fact [E] and keeps the two search results [I]. It also states that -0140 lacks the figure, which is consistent with App. G's full-record result (one use, -0079). | Source check 2c: attachment p. 10, “KWAME RAOUL / Attorney General of Illinois”; no “681” in the letter (script). Ledger C-4: the Illinois Attorney General was among the letters looked for on submitters' sites. Log § 7: -0140 filed with a blank organization field. | must fix | “THEIA Services found the figure in none of them. [I] The Illinois Attorney General, whose letter it had also looked for, co-signed a multistate attorneys general letter posted with a blank organization field (comment CMS-2026-2476-0140, p. 10) [E], which does not contain the figure either. [I] Matching by organization name, THEIA Services found no letter from the Illinois Health and Hospital Association in the posted docket. [I]” | +9 (appendix) |
| NT6-02 | App. D, Parameters, sentences 3–4 | “THEIA Services’ October checks matched the 75, 55, 40 and 20 percent values against the Federal Register text but not the 90 and 70 percent values or the Medicaid-share point. [I]” … “Each scenario also changes the share of provider taxes Medicaid pays. [E]” | The hedge sentence says the 90 and 70 percent values and the Medicaid-share point were not matched against the Federal Register text. They now are, so the sentence is out of date. The Medicaid-share sentence also lacks a pinpoint. Two edits: (1) delete the hedge sentence; (2) add the pinpoint. | Source checks 2a(1) and 2a(2): all six parameter values and the Medicaid-share assumptions are matched at 91 FR 46593 and 46594. Sec. 2's “CMS’s other estimates move these assumptions together” is now fully supported, which answers the decision log's NT5-14 concern. | should fix | (1) Delete “THEIA Services’ October checks matched the 75, 55, 40 and 20 percent values against the Federal Register text but not the 90 and 70 percent values or the Medicaid-share point. [I]”. (2) Replace “Each scenario also changes the share of provider taxes Medicaid pays. [E]” with “Each scenario also changes the share of provider taxes Medicaid pays (91 FR 46593–46594). [E]”. | -31 and +3 = -28 (appendix) |
| NT6-03 | App. C, “Section 71117”, sentence 1 | “This section governs waivers of the requirement that provider taxes be uniform, and is carried out by the final rule CMS-2448-F (91 FR 4794). [E]” | The citation is right, but “governs waivers of the requirement that provider taxes be uniform” is narrower than the source. Section 71117 adds a test of when a tax is not generally redistributive, and CMS applies it to taxes under a waiver of the broad-based requirement as well as the uniformity requirement. The decision log's re-check list named NT5-30 as open; this closes it. | Source check 2b: 91 FR 4794 (“[CMS-2448-F] RIN 0938-AV58”; “implementing recently added statutory requirements for a tax to be considered generally redistributive”); 4800 (Section 71117 “add[s] a new clause detailing when a tax would not be considered generally redistributive”); 4808 (P1/P2 broad-based and B1/B2 uniform waivers). | should fix | “This section adds a statutory test of when a tax that a waiver exempts from the uniformity or broad-based requirement is not generally redistributive, and the final rule CMS-2448-F implements it (91 FR 4794, 4800, 4808). [E]” | +12 (appendix) |
| NT6-04 | App. B, “Hold harmless and the 75/75 test”, sentence 2 | “75 percent of taxpayers get back 75 percent or more of their tax (91 FR 46564). [E]” | v6 cut “in enhanced Medicaid payments or other state payments” because it could not be matched (NT5-12). It now matches verbatim, so restoring it is a choice, not a correction. The v6 sentence is accurate without it. | Source check 2a(3): 91 FR 46564, “… 75 percent or more of their total tax costs back in enhanced Medicaid payments or other State payments”. | optional (decision for Eric) | “75 percent of taxpayers get back 75 percent or more of their tax in enhanced Medicaid payments or other state payments (91 FR 46564). [E]” | +8 (appendix) |

---

## Source checks

Matching rules:
- Every match below was found by script in text extracted from a downloaded copy, on the page cited. Case, quote marks, dashes, white space and line-break hyphens were normalized before matching.
- Federal Register page numbers were checked against each page's printed header (0 mismatches across 150 pages).
- Nothing was matched by inference.
- Where CMS's sentence is broken by a table in the two-column layout, its parts were matched separately, in order, on the same page; the row says so.

| Item | What was checked | Source read | Result | v6 text affected | Replacement and word change |
|---|---|---|---|---|---|
| 2a(1) | App. D: low-savings 75 / 90 / 40 percent; high-savings 55 / 70 / 20 percent | CMS-2452-P, govinfo PDF (`FR-2026-07-23/pdf/2026-14897.pdf`), 91 FR 46593–46594 | **Match, all six values.** 46594: “we assumed that 75 percent of SDPs are financed by provider taxes and that up to 90 percent of provider payment reductions” (21 words); offset “40 percent of payment reductions”. 46593: the same sentence with 55 and 70 percent; offset “20 percent”. The per-scenario pinpoints v6 gives (low 46594, high 46593) are right. | “THEIA Services’ October checks matched … or the Medicaid-share point. [I]” | NT6-02: delete the hedge sentence (−31, appendix). |
| 2a(2) | App. D: “Each scenario also changes the share of provider taxes Medicaid pays.” | Same, 91 FR 46593 and 46594 | **Match.** High-savings (46593): “we assumed that Medicaid paid providers more to offset some of the taxes (4 percent of the revenue for hospital taxes …”. Low-savings (46594): “that Medicaid did not pay providers any additional amounts due to the taxes”; the sentence's opening, “Under the low scenario, we made the following assumptions. We assumed”, is on the same page before Table 17, which interrupts it, and both parts were matched in order. The central scenario's effective Medicaid payments for provider taxes are in Table 9 (91 FR 46591). | “Each scenario also changes the share of provider taxes Medicaid pays. [E]” | NT6-02: add “(91 FR 46593–46594)” (+3, appendix). |
| 2a(3) | App. B: the 75/75 phrase v6 cut (NT5-12) | Same, 91 FR 46564 | **Match.** “75 percent of taxpayers receive 75 percent or more of their total tax costs back in enhanced Medicaid payments or other State payments” (22 words). | “… 75 percent or more of their tax (91 FR 46564). [E]” | NT6-04 (optional, Eric's call): restore “in enhanced Medicaid payments or other state payments” (+8, appendix). Ledger RM-39 can record the quote either way. |
| 2a(4) | Save both rules' text | govinfo PDFs of CMS-2449-P (`FR-2026-05-22/pdf/2026-10292.pdf`, 67 pages, 91 FR 30400–30466) and CMS-2452-P (38 pages, 91 FR 46562–46599) | **Done.** `review/sources/fr/CMS-2449-P_FR-Doc-2026-10292.txt` and `review/sources/fr/CMS-2452-P_FR-Doc-2026-14897.txt`, one block per page headed “=== 91 FR <page> (PDF page <n>) ===”, with a provenance header. I also saved CMS-2448-F (`review/sources/fr/CMS-2448-F_FR-Doc-2026-02040.txt`), because check 2b and ledger RM-33 rest on it; drop it if only the two proposed rules are wanted. Limit: tables printed as images (for example CMS-2449-P Tables 17–23 and 27–28, CMS-2452-P Table 1) carry no text. | — | — |
| 2b | CMS-2448-F at 91 FR 4794; that it carries out Section 71117 on uniformity waivers | Federal Register API search (`api/v1/documents.json`, term “CMS-2448-F”), then the govinfo PDF `FR-2026-02-02/pdf/2026-02040.pdf` (45 pages, 91 FR 4794–4838) | **Citation confirmed; description too narrow.** 91 FR 4794 is the first page of “[CMS-2448-F] RIN 0938-AV58”, a final rule published February 2, 2026; the API returns citation “91 FR 4794”. The rule says it is “implementing recently added statutory requirements for a tax to be considered generally redistributive” (4794). It also says “Section 71117 of the WFTC legislation enacted changes to section 1903(w) of the Act to add a new clause detailing when a tax would not be considered generally redistributive” (4800, 24 words). The requirement covers broad-based waivers as well as uniformity waivers (4808: “as well as when a State is seeking a uniform requirement waiver using the B1/B2 test. This is consistent with the amendments made by section 71117”, after the P1/P2 broad-based case). | “This section governs waivers of the requirement that provider taxes be uniform, and is carried out by the final rule CMS-2448-F (91 FR 4794). [E]” | NT6-03 (+12, appendix). Ledger RM-33 can now record a quote. |
| 2c | Comment CMS-2026-2476-0140: signatories; the Illinois Attorney General; other organizations App. G says were not found | regulations.gov API (`/v4/comments/CMS-2026-2476-0140?include=attachments`, key from REGULATIONS_GOV_API_KEY): no organization or name fields, posted September 22, 2026, one attachment. Downloaded `https://downloads.regulations.gov/CMS-2026-2476-0140/attachment_1.pdf` with a browser User-Agent (HTTP 200, 12 pages, text layer on every page). **Not committed.** | **The Illinois Attorney General signed.** The letter is dated September 21, 2026 and addressed “Attention: CMS-2452-P”. Its signature block (pp. 10–12) lists 24 attorneys general: Maryland (Anthony G. Brown), Colorado, Arizona, California, Connecticut, Delaware, District of Columbia, Hawaiʻi, **Illinois (“KWAME RAOUL / Attorney General of Illinois”, p. 10)**, Maine, Massachusetts, Michigan, Minnesota, Nevada, New Jersey, New Mexico, New York, North Carolina, Oregon, Rhode Island, Vermont, Virginia, Washington and Wisconsin. The opening paragraph (p. 1) names the same 24. Script search of the letter: no “681” and no “Illinois Health”. App. G's other negative, the Illinois Health and Hospital Association, is not among the signatories. The log's list of organization letters filed with a blank organization field (§ 7) does not include it either, so the scoped negative for it stands. | “… found no letter from the Illinois Health and Hospital Association or the Illinois Attorney General in the posted docket. [I] It has not checked whether the Illinois Attorney General signed … (comment CMS-2026-2476-0140). [I]” | NT6-01 (+9, appendix). |

No host refused a request that mattered. One aside: federalregister.gov answered the search request above, but blocked this session's IP on a later metadata request ("Your IP address has been blocked … Support Code 02"). The CMS-2449-P title in the file header was therefore taken from the rule's first page instead.

---

## Changed sentences: check record

| Change (change map) | Decision-log row | Applied as logged? | New error, tag, quote, agreement |
|---|---|---|---|
| W1 sec. 3 | NT5-18 | Yes; log CE-61's wording kept | None |
| W2 sec. 5 ¶1 | CUT-1 | Yes; ASPE no longer appears before it is spelled out | None |
| W3 sec. 5 CBO | NT5-19 | Yes; "separately" agrees with App. F's "one separate line" | None |
| W4 sec. 5 $756 billion | NT5-09 | Yes, four [I] sentences | None; 510.1 + 245.8 = 755.9 |
| W5 sec. 5 ¶4 | NT5-20, -08, -21 | Yes | None; 601.0 − 80.6 − 18.9 = 501.5; 755.9 − 80.6 − 44.4 = 630.9 |
| W6 sec. 6 row E | NT5-07 | Yes | Agrees with the Group E ¶, the Figure 6 caption and App. H |
| W7 sec. 6 Group D | NT5-24 | Yes | Agrees with App. H's 15 states |
| W8 sec. 7 step 2 | NT5-10, CUT-2 | Yes; "intends" kept | None |
| W9 sec. 7 step 3 | NT5-25 | Yes | None |
| W10 sec. 8 bullet | NT5-26 | Yes; log AC-08's wording verbatim | None |
| W11 sec. 8 IMD | NT5-03 (Dec. a, c) | Yes, as modified: the 1115 exception is removed; managed care is cited to 42 CFR 438.6(e) | None. 438.6(e) is supported by the verification summary's citation check. Sec. 8 names one exception and App. B two; "an exception" does not claim it is the only one. |
| W12 sec. 9 item 7 | NT5-06 (Dec. b) | Yes, "[DATE]" | Re-run due before publication (decision log) |
| W13 sec. 9 item 8 | NT5-28 | Yes | None |
| W14 App. B 75/75 | NT5-12 (Dec. e) | Yes, cut | The cut phrase now matches the FR text verbatim (2a(3)); NT6-04 |
| W15 App. B IMDs | NT5-04, -05 | Yes | None |
| W16 App. C gaps 1–3, Inputs | NT5-11, -15 | Yes | None |
| W17 App. D Parameters | NT5-14, -15 | Yes, with the hedge | The hedge is now out of date (NT6-02) |
| W18 App. E | NT5-15 | Yes | None |
| W19 App. F reconciliation | NT5-15 | Yes | None |
| W20 App. F CBPP | NT5-16 | Yes | None |
| W21 App. F netting count | NT5-01 | Yes, 12 and 9 (ledger TP-37) | None |
| W22 App. G | NT5-42, NT5-13 (Dec. d) | Yes | NT5-13's scoping is superseded by check 2c (NT6-01) |
| W23 App. G Limits | NT5-15 | Yes | None |
| W24 App. H A, E | NT5-15 | Yes | None |
| W25 App. I | NT5-06 (Dec. b) | Yes, "[DATE]" twice | None |
| W26 App. I Loper Bright | NT5-02 | Yes, 9 (ledger TP-40) | None |

The decision log's "Re-check list before publication" has four items. This check closes items 2 (-0140), 3 (App. D values) and 4 (CMS-2448-F). Item 1, the three "[DATE]" re-runs (lawsuit search, OIRA status, bill status), stays open until the publication date.

**For the ledger owner (not edited here).** Each of these rows can now record a quote from the downloaded text:
- CE-32: 91 FR 46593–46594.
- RM-39: 91 FR 46564.
- RM-33: 91 FR 4794, 4800 and 4808.
- NC-17, with log § 7's -0140 row: the 24 signatories, including Illinois.

The D8 items from the v5 check (SB-26, SB-30, and the TP-37 and TP-40 claim columns) are still open.

---

## Departure from CONVENTIONS.md, section 5

This file quotes CMS-2452-P more than once (91 FR 46593, 46594 and 46564) and CMS-2448-F more than once (91 FR 4794, 4800 and 4808). The request asks for the source's wording in each check, as the earlier verification files did. Each quotation is verbatim from the downloaded text and 24 words or fewer. One normalization: the PDF's line-break hyphen in “health care-related” was rejoined as printed.

---

Ready for ledger sync and Word: **no**. NT6-01 (must fix) and NT6-02 and NT6-03 (should fix) must be applied to the appendix first. They need no new source, and they leave the body at 6,239 words. Once they are applied, the answer is yes, with only the three "[DATE]" re-runs left, for publication.
