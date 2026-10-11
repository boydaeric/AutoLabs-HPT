# New-text check on v4

*New-text checker, October 11, 2026. Writes only this file; `review/article_v4.md` is not edited. Follows `review/CONVENTIONS.md`. Compares `review/article_v4.md` with `review/article_v3.md` sentence by sentence (72 changed passages) and checks only what changed.*

**Method.** I diffed v3 and v4 by sentence. I checked each changed sentence against v3, `verification_summary.md`, `findings.csv` and the Federal Register (FR) PDFs for CMS-2449-P (91 FR 30400–30466) and CMS-2452-P (91 FR 46562–46599). I downloaded the PDFs from govinfo; they are not committed. Where I read the FR myself, the row says "FR read here". Then I traced every issue in `review/new_text_check_v3.md` (NTC3) through `decision_log.md` ("New-text check v3 decisions") into v4.

**Not available.** The same three limits as in the v3 check:
- v15 was not attached.
- The base evidence ledger is not in the repo.
- Outside documents (KFF, HFMA, POLITICO, ASPE, GAO, the press pieces, CMS-2450, the bills) cannot be read here. Changes to sentences about them were checked for wording, tags and citations only.

**Bottom line.**
- **Numbers.** No new number beyond the pinpoint "46583", and the only dropped numbers are the comment IDs -0056 and -0106. Every recomputation holds. The year-basis fix is a stated limit, as decided (decision 2), not a resolution.
- **Citations.** Most new or changed pinpoints check out. Four problems: the FR 46583 cite does not support "quarter ending"; the FR 30450 cite supports only the default rule; "Section 71116" carries no subsection; and the sec. 7 step 2 pointer to "(sec. 3)" for the $51.0 billion now dangles.
- **Tags.** Most retags are correct. Three are wrong: one regression in the sec. 5 "two figures" sentence, one [I] over a CMS-stated fact in App. F, and one [I] over an outside fact in sec. 9 item 6.
- **New claims beyond the sources.** Three overstate the FR:
  - sec. 7 step 2 ("could not continue" for "in some cases ... ineligible");
  - sec. 9 item 6 ("a decision on appeal", resting on an unverified note);
  - sec. 8 (the 91 FR 30450 cite).
- **NTC3 follow-through.** All 62 issues (NTC3's tables as numbered in the decision log) are either fixed or logged. Six are logged not fixed and are unchanged in v4, as logged. Two logged as "Fixed" are not fully fixed: 5-8 (ASPE) and 3b-8 (step 2). One "Fixed in part" claim is overstated: 1d-5. One log number is off by one (the quote word count).

---

## 1. Numbers

| Location | Check | Result |
|---|---|---|
| Whole document | Number tokens in v4 absent from v3, and the reverse | One new token: "46583" (an FR page). Two dropped: comment IDs -0056, -0106, removed on purpose (NTC3 3b-9). No figure changed. |
| Sec. 5 "two figures", App. E | "$163.7 billion less $142.1 billion is $21.6 billion" | ✓ 21.6; CMS prints 21.7 (rounding). The subtraction now runs the right way. NTC3 1d-1 and 1d-2 are fixed. |
| Sec. 5 ¶4, App. F | $601.0B − 80.6 − 18.9 = $501.5B; $755.9B − 80.6 − 44.4 = $630.9B | ✓ both. FR read here: 2035 federal is 80.6 (Table 19, 91 FR 30452) and 18.9 (Table 14, 91 FR 46593). 44.4 is Table 11's 2035 (91 FR 46591). |
| Sec. 5 ¶4 | "nine years against CBO's ten" | ✓ 2026–2034 is nine years; CBO's fiscal years 2025–2034 are ten. |
| Sec. 5 ¶4 | "$755.9 billion for 2026–2035" "federal total without the interaction" | ✓ 510.1 + 245.8. |
| Sec. 5 POLITICO ¶3 | "$510.1 billion + $245.8 billion, 2026–2035, 2026 dollars" | ✓ Both are real 2026 dollars in the FR (91 FR 30451; 91 FR 46591). |
| Sec. 4 | "about $122 billion (low-savings, after step 3) … about $1,126 billion (high-savings, after step 2), in 2026 dollars over 2026–2035" | ✓ 122.5 and 1,125.8 as in v3's App. D table; the labels are now right. |
| Sec. 1 | "$98.6 billion in calendar year 2026" | ✓ exact FR wording, 91 FR 46589. |
| Sec. 1 table note | "−$5.34 billion is federal plus state spending (91 FR 30453)" | ✓ FR read here: "$5.34 billion … Federal $3.51 billion … State $1.83 billion". |
| Sec. 1 table note | "−$2.44 billion is in 2026 dollars (91 FR 30456)" | ✓ ("total computable … real 2026 dollars"). See 2a-3 for the missing "federal plus state". |
| Sec. 2 | "80 to 90 percent of SDPs … by the end of 2025, on CMS's preprint data (91 FR 30452)" | ✓ FR read here: "SDP preprint data indicates that by the end of 2025, 80 to 90 percent of SDPs relied entirely or in part on provider taxes or IGTs". Fixes NTC3 3b-7. |
| Sec. 4 quote | Fragment lengths | 10 and 10 words (the decision log says 10 and 9, total 19). Total 20, still under 24. |
| App. D | Table header "billions of 2026 dollars, 2026–2035"; "low-savings" labels | ✓ Figures unchanged and correct. |

**Clean:** every other number in the changed text is unchanged from v3, which the v3 check confirmed.

---

## 2. Changed sentences: citations, tags, new claims, undefined terms, unstated bases

### 2a. Executive summary and sec. 1–2

| Location | Issue | Fix |
|---|---|---|
| Exec ¶1, sentence 1, "of the most providers could stop paying to fund the cut payments" | This was the fix for NTC3 1d-5 (the floor also nets IGT savings). "The cut payments" is unclear, and the sentence still does not mention IGTs. The reader cannot tell that the floor subtracts money paid to fund the state share of SDPs, taxes and IGTs alike. | "…net of lower provider taxes and, at the lower end, of the most providers could save by paying less in taxes and IGTs to fund the state share of SDPs." |
| Sec. 1, SDP definition, "most approved in advance by CMS (42 CFR 438.6(c)(1); 91 FR 30447)" | "Most" has no source. 91 FR 30447 says only that its $143.8B excludes SDPs that need no written prior approval; it gives no share. Paragraph (c)(1) is the general rule, not the approval requirement (that is (c)(2)(i), named in the Citation check). | "…generally approved in advance by CMS (some are exempt; 42 CFR 438.6(c)(2)(i); 91 FR 30447)". |
| Sec. 1, SDP table note, "the −$2.44 billion is in 2026 dollars" | Both figures are federal plus state (FR read here: 30456 "total computable (Federal plus non-Federal shares)"). The note says so only for the −$5.34B. The dollar basis of the −$5.34B is not stated. | "Both are federal plus state spending (91 FR 30453, 30456); the −$2.44 billion is in 2026 dollars." |
| Sec. 2, "(its high-savings and low-savings values)" | Fixes NTC3 5-4. The 55% and 75% scenario values are at 91 FR 46593–46594, but the sentence cites only 46592. | "(91 FR 46592; the scenario values are at 46593–46594)". |
| Exec ¶2 (outside estimates; HFMA spelled out) | HFMA is spelled out correctly (NTC3 5-7 ✓). The sentence now says "each measure something narrower or on a different basis", which fits KFF's $155B and POLITICO's $681B but not HFMA's $56.6B (sec. 5 reads it as a double subtraction). | "…narrower, on a different basis or, in HFMA's case, apparently in error". Carried from v3; low. |

**Clean in this group:**
- Exec ¶1 sentences 2–4: the [E] pointers and the baseline [E] / "so they include" [I] split (NTC3 4-2 ✓).
- Exec ¶2 last sentence ("without giving a combined figure" [I]).
- Exec ¶3 ("implement them").
- Exec ¶4 ("or how states will fund SDPs going forward" [I]; NTC3 3b-11 ✓).
- Exec ¶6 (pointer to sec. 1).
- Sec. 1 provider tax ¶1 ("calendar year 2026").
- Threshold source note "91 FR 46565, 46576, 46598". FR read here: 46565 gives 5.5% in FFY 2028 falling 0.5 points a year to 3.5% in FFY 2032; 46576 and the proposed text at 46598 list each year. This fixes NTC3 2-1.
- Sec. 2 ¶2 (the 80–90% sentence, apart from the cite).

### 2b. Sec. 3

| Location | Issue | Fix |
|---|---|---|
| Sec. 3, "CMS applies each set of assumptions nationally (91 FR 30453–30454, 46591–46594) [E]" | Added cite, but none of the cited pages says "nationally". They present national scenario tables. The tag is [E] over a reading. | Tag [I], or "CMS's scenario tables are national (…)". |
| Sec. 3, year-basis sentence | The content is right (FR read here: Tables 18–20 head the year column "Fiscal Year", 91 FR 30451–30452; "$98.6 billion in revenue for States in calendar year 2026", 91 FR 46589). "Offset by a few months" is vague: a federal fiscal year is three months from a calendar year, and a state fiscal year is typically six. | "…may be offset by three to six months". Low. |
| Sec. 3, "$198.7 billion over 2026–2035 (Tables 6–8, 91 FR 46589–46590; Appendix B), of which CMS assigns…" | The split was moved to App. B (verified: freeze $51.0B at 46589, threshold $147.7B at 46590). Sec. 7 step 2 still points to "(sec. 3)" for the $51.0 billion. See 2e. | See 2e. |

**Clean in this group:**
- Sec. 3 ¶1: the new sentence "The SDP rule prices Section 71116 (Tables 18–20, 91 FR 30451–30452) and its extension to other services (91 FR 30453) separately [E]". FR read here: Tables 18–20 are titled "…limiting SDPs under section 71116…", and 30453 introduces the extension with "In addition to these impacts … $5.34 billion". The [E]/[I] split on "THEIA Services found no separate estimate" is right. This resolves NTC3 3b-2.
- Fee-for-service baseline sentence.
- Merged scenario paragraph (30% offset, "the other estimates change all three").
- The $384.0B / $142.1B / $241.9B offset sentence.
- Table note ("implement").
- State ¶ ($264.7B / $264.4B).

### 2c. Sec. 4

| Location | Issue | Fix |
|---|---|---|
| Sec. 4, step 3 quote, "where providers pay the provider taxes or IGTs that fund the state share of SDPs" | The paraphrase replaces CMS's "To the extent providers pay…" with "where". "To the extent" means in proportion; "where" reads as all-or-nothing. Quote lengths 10 and 10 words, one passage (91 FR 30453). | "to the extent providers pay…" in the paraphrase. |
| Sec. 4 range sentence, "(high-savings, after step 2)" | Correct, but a reader will ask why the high end stops at step 2 (after step 3 it is $786B). The reason is in App. D only. | Add "(the high-savings figure after step 3 is about $786 billion)". Low. |

**Clean in this group:**
- Sec. 4 ¶1 ("gives no combined figure").
- Step table row 1 ("both rules combined"), row 3, and the source note ("as the rules would implement them"; "other entities, such as local governments"; FR read here, 91 FR 30450 and 30462). This closes NTC3 7-1 and 3b-5.
- Best-case ¶.
- Hospital ¶: "for the SDP rule CMS says it cannot attribute… (91 FR 30462), and for the provider tax rule it expects the largest decreases to fall on hospitals (91 FR 46591)". FR read here, wording matches. This closes NTC3 3b-4. "Calendar year 2026" for Table 4 is fine.

### 2d. Sec. 5

| Location | Issue | Fix |
|---|---|---|
| Sec. 5 ¶1, "KFF's $155 billion … ASPE's $891 billion" | "ASPE" is used here before it is spelled out (the subsection below does it). The decision log says the acronym "is spelled out at its first use in sec. 5". It is not: the first use is this sentence. NTC3 5-8 is not fixed. | "…and the Assistant Secretary for Planning and Evaluation's (ASPE) $891 billion", or "HHS's $891 billion". |
| Sec. 5 exhibit header, "CMS central estimates, 2026–2035 (billions of 2026 dollars)" | The header now says "CMS". The combined column and the last row (range 488–753) are THEIA's arithmetic. The note says so; the header could mislead. | "Central estimates (CMS's tables; combined column THEIA's)". |
| Sec. 5 "two figures", sentence 1 | "neither covering both rules" now sits inside the [E] sentence. v3 had it as a separate [I]. | Split: "…(91 FR 46590–46593) [E]; neither covers both rules. [I]" |
| Sec. 5 ASPE ¶3, "Some organizations already net provider taxes against payments (Appendix F). [I]" | Vague, and the tag is [I] over facts App. F tags [E]. It also invites the reading that FAH, AHA and the South Carolina agency net provider taxes against payments in the sense of a net loss; App. F says they asked about the payment-rate test, which is different. | "CMS's provider tax rule and the Texas Hospital Association net provider taxes against payments (Appendix F). [E]" |
| Sec. 5 POLITICO ¶3, "Its $756 billion, both rules' federal savings measured alone ($510.1 billion + $245.8 billion…)" | The composition is THEIA's match, not POLITICO's stated components. Carried from v3; the tag [I] covers it, but the wording asserts it. | "…equals both rules' federal savings measured alone…". Low. |

**Clean in this group:**
- POLITICO ¶2 (CBO pinpoints pp. 4–5 for section figures and p. 6 for interactions, NTC3 2-3 ✓; "names no source" [I] and "which CBO does not print" [I], NTC3 4-1 ✓).
- POLITICO ¶3 as a statement of basis. It now says "on THEIA Services' reading of CBO's tables" and "differs from them in years, dollars and baseline", which fixes NTC3 3a-1. The old "matches CBO's section-by-section basis" is gone.
- POLITICO ¶4: layout hedge ✓ (3a-3); "treated the same way" ✓ (3a-2); $501.5B / $630.9B labelled (3b-1 ✓); "converting 2026 dollars to CBO's unadjusted dollars … raises it" is the VS direction-only finding ✓; "one later comment restates it (comment CMS-2026-2476-0079)" ✓ (F-014; posted September 22, per F-001).
- HFMA retags ("found $56.6 billion in neither rule" [I]; "had not replied" [I]; FR and ledger delta confirm 56.6 is in neither).
- ASPE ¶1 "does not say whether it removes the overlap" [I].
- ASPE ¶2 ("implement").
- The "thus already nets out" [I] / Table 12 title [E] split.
- No new FR quote anywhere.

### 2e. Sec. 6–7

| Location | Issue | Fix |
|---|---|---|
| Sec. 7 step 2, "…zero in non-expansion states unless the state enacted or raised the tax after July 4, 2025 [I], since CMS says taxes not in place on that date could not continue past October 1, 2026 (91 FR 46589) [E]" | The [E] overstates the FR. FR read here: "These amounts also include provider taxes not already enacted and imposed as of July 4, 2025; in some cases, these taxes would be ineligible to remain in place beyond October 1, 2026." CMS says "in some cases", and the sentence is about taxes not enacted and imposed, not about raised rates. NTC3 3b-8 is "Fixed" but the fix adds an overstatement. | "…unless the state enacted or raised the tax after July 4, 2025 [I]; CMS says some taxes not enacted and imposed on that date would be ineligible to continue past October 1, 2026 (91 FR 46589) [E]". |
| Sec. 7 step 2, "$198.7 billion in lower collections that include $51.0 billion of tax increases avoided under the freeze … (sec. 3)" | The $51.0B now appears only in App. B. Sec. 3 no longer has it. The pointer dangles. | "(sec. 3; Appendix B)". |
| Sec. 7 step 3, "(SDP preprint, Section VI) [E]" | Names a section of the SDP preprint form with no page or document; no verification row covers it (on the re-check list, U-5). Logged, not new. | Leave as logged. |
| Sec. 6 Group E, "the lower threshold reaches Colorado, Connecticut, Indiana and Vermont, whose hospital taxes exceed 3.5 percent, and two Group E states carry KFF data-quality flags (Appendix H). [I]" | One [I] over an [E] KFF fact, and the inference "their lack of identified SDPs partly reflects limited data" now lives only in App. H. | Tag the KFF fact [E] and the inference [I], and name Alabama and Wyoming in the body. Low. |

**Clean in this group:**
- Sec. 6 first ¶ and bullets (Minnesota/Missouri parenthetical; KFF numbers unchanged from v3; the share-above-caps bullet and Texas dollars moved to App. H with tags intact; table note shortened).
- Sec. 7 step 1 (grandfathering cites Section 71116; sec. 1 pointer; the inputs sentence moved to App. C, and "preprint" is now defined in step 3, its first body use).
- Step 3's [I] retag.
- The merged first question.

### 2f. Sec. 8–9

| Location | Issue | Fix |
|---|---|---|
| Sec. 8 rural ¶2, "…cap defaults to the state Medicaid plan rate (91 FR 30450) [E]" | FR read here: 91 FR 30450 supports only the default ("unless no total published Medicare payment rate exists for the service, in which case the payment limit is the State plan approved rate"). It does not support "critical access, freestanding children's and certain cancer hospitals are paid on cost and have no published Medicare rate". The log says "fixed in part". | Move the cite after "state Medicaid plan rate" and mark the first clause uncited, or cite its source. |
| Sec. 8 rural ¶1, "phase down from 2028 like other hospitals'" and "(Section 71116; sec. 1)" | "From 2028" drops "each state's first managed care rating period on or after January 1, 2028". The cite names the section with no subsection; the rural definition is at § 71116(d)(2) (FR read here: 91 FR 30458 quotes "rural hospital (as defined in subsection (d)(2))"). | Restore the rating-period wording; cite "§ 71116(b), (d)(2)". Same for App. B's rural note. |
| Sec. 9 item 6, "A decision on appeal in Texas v. CMS … [E]" | It asserts an appeal. The only source for an appeal is the research note (VS F-024: secondary, unread brief). The sentence's [E] (CHAT's description with ID and pages) is right; "on appeal" is not CHAT's statement. | "A decision in any appeal of Texas v. CMS…", or move "on appeal" into the [I] sentence. |
| Sec. 9 item 6, "An unverified research note gives the appeal as Fifth Circuit No. 25-40766, pending as of June 24, 2026. [I]" | A public note should not cite "an unverified research note". The tag [I] is for THEIA's reading; this is an outside fact from a secondary source. | "A June 24, 2026 amicus brief, as reported by a secondary source we could not verify, gives the appeal as Fifth Circuit No. 25-40766." Or cut until verified. |
| Sec. 9 item 8, "…for the quarter ending December 31, 2026, the first basis… (91 FR 46583) [I]" | The pinpoint does not support "quarter ending". FR read here: 46583 says the one-time interim information is provided "by December 31, 2026", for "the SFY that contains July 4, 2025"; the "CMS–64 for QE December 31, 2026" timing is in the table at 46578. | "…data states would file with CMS by December 31, 2026, for the state fiscal year containing July 4, 2025 (91 FR 46578, 46583)". |

**Clean in this group:**
- Sec. 8 opening ([E] pointing to the studies below).
- IMD ¶ citing Social Security Act § 1905(a), which is the pinpoint in the Citation check.
- Virginia sentence (ID and p. 3 unchanged).
- Item 2 ("(91 FR 30453)", FR read here: "We expect to provide an analysis of the interaction between these proposals in future rulemaking").
- Item 3 (shortened).
- Item 7 ([I] on the lawsuit negative; the stale date is logged, not fixed).
- Items 9 and 10 (retagged; "state hospital association").

### 2g. Appendix

| Location | Issue | Fix |
|---|---|---|
| App. F, "$341 billion, its rounding of the sum of CBO's two section figures" | An inference. CBPP's footnote (F-015) says "$341 billion" and does not say it is that sum; VS records only that $340.5B is the sum and is printed by neither CBO file. | "…$341 billion (evidently its rounding of $340.5 billion, the sum of CBO's two section figures) [I]". |
| App. F "who nets provider taxes", "The cap test compares an SDP's total payment rate, base payment plus SDP, with the Medicare-based cap (sec. 7, step 1) … [I]" | This is stated by CMS (FR read here, 91 FR 30450: "the total payments (that is, the sum of the base payment, SDP, and any other SDPs … ) may not exceed 100 percent of the Medicare payment rate … "), so the first half is [E] with a cite. The inference "changes the rate tested, not the net provider loss" is [I]. | Split: [E] with "(91 FR 30450)", then [I]. |
| App. F, THA 2025 figures [E] | No document cited. On the re-check list (decision 3). | Logged. |
| App. D, scenario ratios | The labels "closer together (low-savings) / further apart (high-savings)" are gone from the whole note. App. D still gives the ratios (1.37 / 1.89 / 2.55), so low and high are recoverable, but the body no longer says which scenario assumes the gaps are closer. | Restore one clause in sec. 3 or App. D. Low. |
| App. B rural note "(Section 71116)" | See sec. 8 row above. | Cite § 71116(d)(2). |

**Clean in this group:**
- App. B: the IMD note marking "most … are IMDs" and "certain demonstrations" as not yet sourced; the new freeze/threshold note (FR read here: Tables 6 and 7, 91 FR 46589–46590).
- App. C: the [I] / [E] split (NTC3 4-9 ✓) and the new inputs note [I].
- App. D: the scope note on the high-savings total (FR read here, 91 FR 30454: "This includes the impacts to services subject to the payment limits under section 71116 … and additional services with limits proposed under this rule"); "[E]" for CMS's two statements, "[I]" for "has not confirmed"; the low/high labels; the 65% note now cites only comment -0204, p. 10 (F-009 ✓).
- App. E: the rounding note with its cite and tags; "high-savings" wording.
- App. F: the year-basis note. FR read here: Tables 18–20 headed "Fiscal Year"; FFY 2025 base at 91 FR 30447; "$98.6 billion … calendar year 2026"; the freeze "begin[s] October 1, 2026" and "reduces projected tax revenue by $2.3 billion in 2026" (91 FR 46589). The inference "probably not a federal fiscal year" is correctly [I], and "CBO's are federal fiscal years" matches VS ("by fiscal year"). This replaces the old "Open:" line and settles NTC3 item 8 as a stated limit.
- App. F reconciliation relabels.
- App. F's keyword-count hedge ("about 11 comments, about 8 distinct texts … keyword count").
- App. G: "restates POLITICO's $681 billion" ✓ and "[I]" on the search negatives ✓.
- App. H: the three moved notes, wording and tags unchanged from v3.

---

## 3. Undefined terms and figures whose basis is not stated

| Location | Issue | Fix |
|---|---|---|
| Sec. 5 ¶1 | ASPE used before spelled out (2d). | As in 2d. |
| Sec. 7 step 2 | $51.0 billion pointer dangles (2e). | As in 2e. |
| Sec. 4 range sentence | The reason the high end is "after step 2" is only in App. D. | Add a clause (2c). |
| Sec. 3 / sec. 5 | Combined figures add SDP years labelled "Fiscal Year" to provider tax years labelled by calendar-year base. The sentence after the sec. 3 table and App. F state this limit; sec. 4's range and sec. 5's exhibit do not repeat it. | Acceptable as a stated limit (decision 2). Consider a clause in sec. 4's first paragraph: "2026–2035 as CMS labels it (sec. 3)". |

**Clean:**
- "preprint" is defined at its first body use (step 3).
- HFMA is spelled out in the exec summary (NTC3 5-7 ✓).
- "implement" is used consistently.
- "low-savings"/"high-savings" are used throughout (no "lower"/"higher" remain, by grep).
- No new term is undefined in the body, apart from ASPE.

---

## 4. Follow-through on `new_text_check_v3.md`

Every issue in NTC3 appears in the decision log under the numbers it assigns (1d-1…8-1). I checked each log status against v4. "OK" means the log's status matches v4.

| Group | Log status | Check against v4 |
|---|---|---|
| 1d-1 to 1d-4 | Fixed | OK (1d-1 has a tag regression, 2d). |
| 1d-5 | Fixed | Fixed in part: wording unclear, IGTs still not named (2a). |
| 2-1, 2-2, 2-3, 2-7 | Fixed | OK. |
| 2-4, 2-5, 2-8, 2-10 | Not fixed (decision 3; re-check list) | OK. GAO, the studies, the press cites, CMS-2450, the bills, "as of September 22, 2026" and Georgetown are unchanged, and each is on the re-check list. |
| 2-6 | Fixed in part | OK. See 2f for the remaining gaps (pinpoint covers only the default; Section 71116 has no subsection). |
| 2-9 | Fixed | Fixed, but it introduces two new problems (2f: "on appeal", "unverified research note"). |
| 2-11 | Fixed in part | OK. |
| 3a-1 to 3a-3 | Fixed | OK. |
| 3b-1, 3b-2, 3b-3, 3b-4, 3b-5, 3b-7, 3b-9, 3b-10, 3b-11, 3b-13 | Fixed | OK. |
| 3b-6 (SDP "approved in advance") | Fixed | Fixed in part: "most" is unsourced (2a). |
| 3b-8 (step 2) | Fixed | Fixed, but the [E] now overstates CMS (2e). |
| 3b-12 (item 8 "public") | Fixed | Fixed ("would file", "public" gone), but the cite does not support "quarter ending" (2f). |
| 4-1 to 4-4, 4-7, 4-9, 4-10 | Fixed | OK. |
| 4-5, 4-6, 4-8 | Fixed in part or by marking | OK. |
| 5-1 to 5-7, 5-9, 5-11 | Fixed | OK. |
| 5-8 (ASPE before spelled out) | Fixed | **Not fixed.** The first sec. 5 use is ¶1, before the subsection that spells it out (2d). |
| 5-10 (Figures 4 and 5) | Not fixed | OK: placeholders unchanged. |
| 6-1 to 6-4 | Fixed | OK. |
| 6-5 (Georgetown) | Not fixed | OK. |
| 6-6 (quote length) | Fixed ("10 and 9 words … 19") | Fixed, but the fragments are 10 and 10 words (20 in all). Immaterial; the log's count is off by one. |
| 7-1, 7-2 | Fixed | OK. |
| 8-1 | Fixed as a stated limit | OK. FR read here confirms the year-basis facts. |

**Not-fixed items are all logged.** I found none that was neither fixed nor logged. The remaining open items are the six logged "Not fixed", the two "Fixed in part" (2-6, 2-11), and the issues in sections 2–3 above.

---

## 5. Overall clean list

- Every figure and every arithmetic result in the changed text.
- Every changed pinpoint except 46583 (the "quarter ending" cite) and 30450 as used in sec. 8: the Citation check rows for 438.6(c)(1), 1905(a) and the FR pages above, and my own FR reads.
- No new FR quote, and the carried CMS-2449-P quote is within the 24-word limit.
- Attribution of $916.9 billion (NTC3 item 7): "combined" and "as the rules would implement them" now appear at every use.
- Comment-ID sentences: every changed sentence about commenters carries its ID, and the CBPP and POLITICO restatements are labelled with their original source.

*Nothing outside this file was edited.*
