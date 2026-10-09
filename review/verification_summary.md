# Verification against primary sources

*Comment analyst's file, October 8, 2026. Follows `review/CONVENTIONS.md`. The full notes, with source URL, page, exact wording and effect on v16, are in the **verification note** column of `review/findings.csv` (U-3 and U-4: `review/findings_v16_unmapped.csv`) and the matching bullets in `review/findings.md`. This pass changed only the verification status and added the verification note. No other field changed, including the v16 flag, the old → new section and the still-open columns.*

## Result by finding

Status is one of: confirmed, corrected, not found, unverifiable. When a finding rests on two sources and they came out differently, each part is listed.

*This table records the October 8 results. The October 9 pass changed F-003, F-005, F-006, F-007, F-008, F-010, F-015, F-022 and F-024; see “Round 2 verification” at the end.*

| Finding | What was checked | Status | Primary source and page | What this changes in v16 |
|---|---|---|---|---|
| F-003 | regulations.gov "comments received" vs posted counts (960; 214) | **Unverifiable** (received counter); posted counts re-confirmed | v4 API, October 8, 2026: `meta.totalElements` = 960 (CMS-2026-1916) and 214 (CMS-2026-2476). The document records have no comment-count field. www.regulations.gov returned HTTP 403. | Nothing |
| F-005 | CMS RIA: "no effect on enrollment"; CBPP "full range of scenarios" | **Confirmed** | 91 FR 46590 (CMS-2452-P, sec. V.C.2). The high and low scenarios (46593–46594) do not change it. | Qualifies: CMS assumes zero enrollment effect, which is not the same as v16 sec. 5's "do not model" |
| F-005 | CBO: 1.1 million more uninsured | **Unverifiable** | cbo.gov returned HTTP 403 | – |
| F-006 | BCBSA: CMS-2452-P's analysis considers CMS-2448-F (sec. 71117) | **Confirmed** | 91 FR 46590 fn 23; 91 FR 46592 (sec. V.C.3, "Offsets"). CMS says the interaction has no significant impact on its estimates. | Qualifies: v16 omits section 71117, but CMS's figures already account for it |
| F-006 | CBPP: CMS-2448-F RIA $78.2B federal / $46.9B state | **Confirmed** | 91 FR 4829 (printed "$78,2 billion"); 2027–2036, real 2027 dollars | – |
| F-006 | CBPP: CBO $34B for the uniformity-waiver provision | **Unverifiable** | cbo.gov returned HTTP 403 | – |
| F-007 | 30 percent state offset in the central scenario | **Confirmed** | 91 FR 46591. Central scenario also: 65 percent tax-financed, at most 80 percent of cuts on SDPs (46592). High scenario: 20 percent offset (46593). Low scenario: 40 percent (46594). | Qualifies: v16 sec. 3 lists offsets and SDP shares for the low and high estimates only |
| F-008 | THA: CBO assumed states replace 50 percent of lost financing | **Unverifiable** | cbo.gov returned HTTP 403. THA cites no CBO document. | Nothing (hold) |
| F-011 | "would still be a significant reduction to provider payments through Medicaid over time" in the RIA | **Confirmed** | 91 FR 46593 (sec. V, RIA; C.3, after Table 14) | Nothing (v16 does not use it; cite available) |
| F-012 | 91 FR 30462: hospitals bear most cuts, or CMS cannot attribute by provider type | **Confirmed** (both readings, same page) | 91 FR 30462: "The majority of these projected reductions would be for hospitals" (end of the accounting-statement discussion). The RFA paragraph on the same page says CMS lacks data to "reliably attribute or disaggregate these impacts to specific provider types". | Qualifies: v16's Executive summary, sec. 3 and sec. 4 cite only the first reading |
| F-015 | CBPP: the CMS vs CBO gap survives window, interaction and dollar-basis adjustments | **Corrected** (see note) | CMS: $510.1B (91 FR 30451; Table 19 at 30452) + $90.9B (91 FR 46593) = $601.0B. | Qualifies: v16 sec. 5 names these differences, but on CMS's tables they do not close the gap |
| F-015 | CBO $340.5B ($191.1B + $149.4B) | **Unverifiable** | cbo.gov returned HTTP 403 | – |
| F-022 | IHA: Idaho's inpatient tax is above the phased-down threshold | **Unverifiable** | IHA gives no rate. Idaho Code § 56-1404 sets the rate by an annual calculation, capped at the federal limit, with no fixed percentage. Idaho DHW and medicaid.gov refused connections. | Nothing (Group E placement can be neither confirmed nor contradicted) |
| F-024 | Texas HHSC SFY2027 CHIRP preprint, CMS Rounds 1–4 | **Confirmed** | Texas HHSC PDF p. 17 of 19 (Round 4, sent September 3, 2026; same text on pp. 14 and 16): CMS lists two issues that must be resolved before approval. "Withhold" is Texas's own word, in its response on p. 18. | Nothing |
| F-024 | Texas v. CMS, 805 F. Supp. 3d 734 (E.D. Tex. 2025) | **Unverifiable** | courtlistener.com refused the connection. govinfo's court-opinion search returned no match. | – (v16 item 6 "set aside" vs CHAT "permanently enjoined" stays open) |
| F-027 | Chartis rural margins | **Confirmed** | Chartis web page "2025 State of the State" (February 10, 2025): 46 percent negative operating margin, national median 1.0 percent, 432 vulnerable | Nothing (v16 does not use them) |
| U-3 | Rule text on the 6.0 percent threshold and the 75/75 test | **Confirmed** | 91 FR 46564 (75/75 defined); 46572 and proposed § 433.68(f)(3)(ii)(A)(3) at 46598 (6 percent cap unless the tax met 75/75 on July 4, 2025; CMS expects no state to qualify); 46581 and summary 46562 (75/75 dropped from FFY2027) | Qualifies: v16's "at most 6.0%" is CMS's proposed cap and cites 46562 rather than 46572/46598 |
| U-4 | Nursing facility / ICF exemption: statutory or proposed | **Confirmed** (statutory) | P.L. 119-21 § 71115(a)(2), new SSA § 1903(w)(4)(D)(iv), 139 Stat. 302; 42 CFR 433.56(a)(3)–(4). CMS calls it statutory (91 FR 46565, 46576). | Nothing (v16's column is right; the exemption is from the phase-down only, and the classes keep their July 4, 2025 threshold) |

No item came out **not found**. Every passage commenters attribute to CMS was located in the Federal Register.

## Why F-015 is "corrected"

The finding says CBPP's footnote argues that "two of the three adjustments lower CMS's figure". CBPP's footnote 23 (2476-0033, p. 9 of 13) says the opposite. The extra year raises CMS's estimate. The interaction and the 2026-dollar basis each lower it. So adjusting for the interaction and the dollar basis would raise CMS's figure, and only the window adjustment lowers it.

CMS's own tables bear out CBPP's conclusion:

| CMS federal figure | 2026–2035 | 2026–2034 (2035 dropped) |
|---|---:|---:|
| With interaction: SDP rule + provider tax rule | $601.0B (510.1 + 90.9) | $501.5B (less 80.6 and 18.9) |
| Without interaction: SDP rule + provider tax rule | $755.9B (510.1 + 245.8) | $630.9B (less 80.6 and 44.4) |

Sources: Table 19 (91 FR 30452), Table 14 (91 FR 46593) and Table 11 (91 FR 46591). Table 11's annual federal row sums to $245.9B against CMS's stated $245.8B, a rounding difference.

CMS states its figures in real 2026 dollars and gives no conversion factor, so the dollar-basis adjustment is direction only. CBO's $340.5B could not be read (cbo.gov returned HTTP 403). The finding's own text was not edited, because this pass may change only the verification fields. The wording fix is for the next findings revision.

## Sources reached and not reached

| Source | Result |
|---|---|
| Federal Register PDFs on govinfo: 91 FR 30400 (CMS-2449-P), 91 FR 46562 (CMS-2452-P), 91 FR 4794 (CMS-2448-F) | Read in full text. Page numbers come from the printed page headers. Tables printed as images at 91 FR 30451–30452 were read from the page images. |
| P.L. 119-21 (govinfo, PLAW-119publ21) | Read, section 71115 at 139 Stat. 301–302 |
| 42 CFR 433.56 (govinfo, CFR 2025 edition) | Read |
| Texas HHSC CHIRP preprint questions (pfd.hhs.texas.gov) | Read, 19 pages |
| Chartis 2025 State of the State (chartis.com) | Read (web page) |
| Idaho Code § 56-1404 (legislature.idaho.gov) | Read only through the web-fetch tool, which returns model-extracted text. The quoted subsection (4) was not byte-checked. Direct connection was refused. |
| regulations.gov v4 API (key supplied through an environment variable, not stored) | Read |
| www.regulations.gov web pages | HTTP 403 |
| cbo.gov (all CBO documents) | HTTP 403, both direct and through the web-fetch tool |
| courtlistener.com, congress.gov, ecfr.gov | Connection refused by the network policy |
| Idaho Department of Health and Welfare, medicaid.gov, kff.org | Connection refused by the network policy |

No secondary summary was used to verify anything. One web-search lead, that THA's 50 percent may come from an earlier CBO budget option rather than the 2025 score, is recorded in F-008's note as unread and not relied on.

## Other things the primary sources show

These were not part of the request and nothing was edited for them:

* **THA mislabels CMS's scenarios.** THA (2476-0109, p. 6 of 9) calls 20 percent the "low scenario". At 91 FR 46593, 20 percent is the high (higher-savings) scenario; v16, CE-32 and CHLA have it right.
* **CBPP misdescribes the offset base.** CBPP (2476-0033, p. 9) describes the 30 percent as a share of "reduced federal spending". CMS applies it to "these cuts", the payment reductions that follow lost tax revenue (91 FR 46591).
* **CMS-2449-P's state figure is internally inconsistent.** The text on 91 FR 30452 says $264.4 billion, while Table 20 on the same page sums to $264.7 billion. This bears on F-020, which already describes the two figures; F-020 was not re-checked or edited in this pass.
* **Ledger CE-32 is contradicted.** CE-32 says the primary scenario carries one parameter. The Federal Register gives the central scenario three: the 30 percent offset, 65 percent tax-financed and the 80 percent SDP ceiling. This is for the ledger owner.

## Departure from the conventions

`review/CONVENTIONS.md` allows one quote per source across a file. This task asked for exact wording in each verification note, so several notes quote the same Federal Register document (CMS-2452-P is quoted in F-005, F-006, F-007, F-011, F-015 and U-3). Each quote is verbatim and at most 24 words, and F-012's two fragments from one page count as one quote. All quotes except the Idaho one were matched by script against the downloaded source text. F-006's CMS sentence wraps from one column to the next around Table 12, and was checked against the page layout.

## Citation check

*October 9, 2026. One row per citation in the research team's citation table (C2). That table was produced with a fetch tool and model-extracted text, so every row was re-read here at a primary source. **Status** says whether the citation supports the claim: confirmed, partly, or wrong page. **Checked here** says how this pass verified the wording: confirmed (matched by script against a downloaded primary source), secondary (rests on the research table) or unverifiable (source blocked). eCFR, Cornell LII and ssa.gov were blocked by this session's network policy, so the regulations were read in the CFR 2025 edition (revised as of October 1, 2025) and the statutes in the United States Code 2024 edition, both on govinfo.gov. Federal Register pages come from the printed page headers in the govinfo PDFs.*

| Citation as given | Status | Correct pinpoint | Exact wording (24 words or fewer) | Checked here |
|---|---|---|---|---|
| 42 CFR 433.70 | confirmed, at (b) only | **42 CFR 433.70(b)**, not § 433.70 generally. Paragraph (a) only says there is no limit on tax revenue if § 433.68 is met. | “CMS will deduct from a State’s medical assistance expenditures, before calculating FFP, revenues from health care-related taxes that do not meet the requirements …” | Confirmed (CFR 2025 edition, govinfo). Paragraph (b) also refers to limits in a paragraph (a)(1) that § 433.70(a) does not have. |
| 42 CFR 433.68(f) | confirmed | (f)(1) for correlated non-Medicaid payments, (f)(2) for Medicaid payments that vary with the tax, (f)(3) for guarantees | (f)(2): “All or any portion of the Medicaid payment to the taxpayer varies based only on the tax amount” | Confirmed (CFR 2025 edition) |
| SSA § 1903(w)(4) | confirmed | § 1903(w)(4)(C)(i) (42 U.S.C. 1396b(w)(4)(C)(i)) for the guarantee test; (A) covers correlated payments and (B) payments that vary with the tax | “provides (directly or indirectly) for any payment, offset, or waiver that guarantees to hold taxpayers harmless for any portion of the costs” | Confirmed (U.S. Code 2024 edition). **The ssa.gov compilation C2 used may predate the 2025 amendments.** The 2024 U.S. Code edition read here cites no P.L. 119-21 amendment to § 1396b either. P.L. 119-21 § 71115 amended § 1903(w)(4) (139 Stat. 301–302; see U-4), so cite the amended text for anything on thresholds. |
| SSA § 1903(w)(6)(A) | confirmed | None. It does not say "intergovernmental transfer". Do not confuse it with § 1903(d)(6)(A). | “transferred from or certified by units of government within a State as the non-Federal share of expenditures under this subchapter” | Confirmed in the U.S. Code, which reads "this subchapter" where C2's ssa.gov text reads "this title" (ssa.gov blocked) |
| SSA § 1902(a)(10)(A)(i)(VIII) | confirmed | None. Effective January 1, 2014; it is made subject to subsection (k) generally, not (k)(1). | “beginning January 1, 2014, who are under 65 years of age … does not exceed 133 percent of the poverty line” | Confirmed (U.S. Code 2024 edition, 42 U.S.C. 1396a) |
| 42 CFR 438.6(c) | confirmed | 42 CFR 438.6(c)(1) (general rule). The heading of (c), which C2 had not confirmed, reads "State directed payments under MCO, PIHP, or PAHP contracts". | “the State may not in any way direct the MCO’s, PIHP’s or PAHP’s expenditures under the contract” | Confirmed (CFR 2025 edition) |
| SSA § 1905(a) and § 1905(i) | confirmed | Exclusion: § 1905(a), closing text after the numbered paragraphs, clause (B), which opens "except as otherwise provided in paragraph (16)". Definition: § 1905(i), more than 16 beds, primarily mental-disease care. Under-21 exception: § 1905(a)(16), defined in § 1905(h). | “any individual who has not attained 65 years of age and who is a patient in an institution for mental diseases” | Confirmed (U.S. Code 2024 edition, 42 U.S.C. 1396d) |
| 42 CFR 438.6(e) | confirmed | None. Heading: payments to MCOs and PIHPs for enrollees who are patients in an institution for mental disease. | “The State may make a monthly capitation payment to an MCO or PIHP for an enrollee aged 21–64” | Confirmed (CFR 2025 edition; printed with an en dash, "21–64") |
| 31 U.S.C. § 1102 | confirmed | None | “The fiscal year of the Treasury begins on October 1 of each year and ends on September 30 of the following year.” | Confirmed (U.S. Code 2024 edition) |
| 91 FR 46589–46591, Tables 5, 9 and 10 (CMS-2452-P) | partly | Table 5 is at 91 FR 46589 and Tables 9 and 10 at 46591. **The captions use only the acronym WFTC, and Table 5 misspells it "WTFC".** The full name, "Working Families Tax Cut (WFTC) legislation", is spelled out at **91 FR 46562** (SUMMARY) and **46564** (heading "D. Working Families Tax Cut Legislation"). At 46570 the title of CMS's November 14, 2025 guidance uses the plural, "Working Families Tax Cuts Legislation". | “TABLE 5—PROJECTED PROVIDER TAX REVENUE ABSENT THE EFFECTS OF THE WTFC LEGISLATION” (Tables 9 and 10: “… ABSENT THE EFFECTS OF THE WFTC LEGISLATION”) | Confirmed (govinfo PDF). The captions are printed in capitals; C2 gave them in title case. |
| 91 FR 30447 (CMS-2449-P), "hospitals (87.5 percent)" | partly | 91 FR 30447 (RIA, "3. Transfers", "a. State Directed Payments (SDPs) (§ 438.6)"). **Base:** "these payments" are the SDPs states are estimated to have paid in **FFY 2025, $143.8 billion**, excluding SDPs that need no written prior approval (no preprint) under § 438.6(c)(2)(i). The $143.8 billion is not split into federal and state shares. | “The largest recipients of these payments were hospitals (87.5 percent), AMCs (4.9 percent), physicians (3.6 percent), and nursing facilities (2.5 percent).” | Confirmed (govinfo PDF). The 87.5 percent is hospitals' share of an estimated $143.8 billion of preprint-reviewed SDPs in one year (FFY 2025). It is not a share of all SDP spending, and not a share of the projected cuts. CMS says the $143.8 billion is 14 percent of all Medicaid benefit spending and 26 percent of managed care payments. |
| 91 FR 46562, "CMS announces final state thresholds on September 30, 2028" | wrong page | **91 FR 46574**. The date is repeated at 46579 ("anticipated no later than") and 46580 ("If that announcement occurs by September 30, 2028, as intended"), and appears in the timing table at 46578. Page 46562 has no 2028 date. | “CMS intends to announce final thresholds to States … no later than September 30, 2028.” | Confirmed (govinfo PDF). CMS states an intention and a deadline ("intends", "no later than"), not a fixed announcement date. |

The sentences quoted from 46579 and 46580 are short fragments of the same CMS-2452-P document. See the departure note under “Round 2 verification”.

## Round 2 verification

*Packet builder, October 9, 2026. This pass re-checked every row of the research team's open-item table (C1) and citation table (C2) against primary sources, resolved F-003, F-008, F-015, F-022 and F-024, and read three Federal Register passages. The research tables used a fetch tool, downloaded nothing, and their quoted wording was model-extracted, so they were treated as leads. In `review/findings.csv` and `review/findings.md` only the **verification status** and **verification note** fields changed. Each new status starts with the October 9 result and keeps the October 8 result after it. Each note keeps its October 8 text and adds a "Round 2 (October 9, 2026)" paragraph. F-010 had no note, so its note is new.*

### Sources this pass reached and did not reach

| Source | Result |
|---|---|
| CBO, Supplemental Cost Estimate for P.L. 119-21, Title VII, Subtitle B, Chapter 1, Medicaid (October 28, 2025; publication 61837), PDF attached to the request, 8 pages | Read in full (pdftotext). Page 1 says its amounts are the same as CBO's July 2025 estimate. |
| CBO, estimated budgetary effects of P.L. 119-21 (July 21, 2025; publication 61570), spreadsheet attached to the request | Read: sheet "Title VII" (Table 7, millions of dollars, by fiscal year), rows for sections 71115, 71116 and 71117 |
| federalregister.gov API (`/api/v1/documents/2026-10292.json`, `2026-14897.json`) | Read. The HTML document pages redirected to a bot check (unblock.federalregister.gov). |
| govinfo.gov: Federal Register PDFs for CMS-2452-P (91 FR 46562–46599) and CMS-2449-P (91 FR 30400–30466); CFR 2025 edition, 42 CFR 433.68, 433.70 and 438.6; U.S. Code 2024 edition, 42 U.S.C. 1396a, 1396b, 1396d and 31 U.S.C. 1102 | Read. Table 19 at 91 FR 46596 was read from the page image. |
| regulations.gov v4 API (public demo key) | 214 comments re-confirmed for CMS-2026-2476. The CMS-2026-1916 re-query hit the demo key's rate limit, so 960 rests on October 8. |
| govinfo court-opinion search (USCOURTS) | No Texas v. CMS opinion. The only hit was an unrelated 2021 E.D. Tex. case (6:21-cv-00191). |
| www.regulations.gov, downloads.regulations.gov (comment letters) | HTTP 403 |
| ecfr.gov, law.cornell.edu, ssa.gov, legislature.idaho.gov, essentialhospitals.org | Blocked by the proxy (CONNECT 403) |

### Research table C1, re-checked row by row

Status is confirmed only where this pass matched the wording or value at the primary source itself; secondary where it rests on the research table or a commenter's quotation; unverifiable where the source was blocked.

| Finding | Research-table lead | Result of the re-check | Source and page | Exact wording or value | Status |
|---|---|---|---|---|---|
| F-003, CMS-2449-P | The Federal Register page shows "Comments" 6,344; regulations.gov returned nothing; no count date shown | 6,344 on the Federal Register against 960 posted as filed / 961 corrected on regulations.gov. The Federal Register's record says when it last refreshed the count (September 4, 2026) but not what the count covers. Comments closed July 21, 2026. | federalregister.gov API record for 2026-10292 (field values, no page) | `comments_count` 6344; `checked_regulationsdotgov_at` 2026-09-04T23:55:03Z; `comments_close_on` 2026-07-21 | Confirmed (both counts). What the 6,344 counts: unverifiable. |
| F-003, CMS-2452-P | The Federal Register shows 245; no posted count seen | 245 on the Federal Register against 214 posted as filed / 213 corrected. The record spans 91 FR 46562–46599, matching the research table. | federalregister.gov API record for 2026-14897 | `comments_count` 245; `checked_regulationsdotgov_at` 2026-09-24T08:55:04Z | Confirmed (both counts). What the 245 counts: unverifiable. |
| F-003, proposed-rule document pages | Not attempted | The regulations.gov document records carry no count field (October 8). The www.regulations.gov pages returned HTTP 403. | – | – | Unverifiable |
| F-005 | Two commenter letters quote "no effect on enrollment"; 91 FR 46590 not read; Healthcare Dive's 2.4 million may conflict | CMS's sentence matched at 91 FR 46590. CBO's 1.1 million matched. The 2.4 million is CBO's statute-level Medicaid enrollment drop for section 71115, so it does not conflict with CMS's rule-level zero. The CBPP letter was not re-read. | 91 FR 46590; CBO PDF pp. 4–5 | “we estimate that this proposed rule would have no effect on enrollment” (CMS); “the number of people without health insurance will increase by 1.1 million in 2034” (CBO, p. 5) | Confirmed (CMS, CBO). The letters 2476-0051 and 2476-0075 are secondary (downloads.regulations.gov returned HTTP 403). |
| F-006 | The CBO document covers 71101, 71102, 71107, 71115, 71116 and 71119, not 71117 | The October 2025 PDF's scope is confirmed. CBO's July 2025 table does cover section 71117: outlays −$34.6 billion and revenues −$0.6 billion, so a net of about $34.0 billion, which CBO does not print. That matches CBPP's $34 billion. | CBO spreadsheet, Title VII, cells O262 and O856 | −34,606 and −638 (millions of dollars, 2025–2034) | Confirmed (CBO cells; the net is arithmetic) |
| F-008 | CBO says states "will not replace all of the lost revenue"; no 50 percent found | Wording matched. Neither CBO document has a 50 percent replacement share. CMS's 30 percent was matched at 91 FR 46591 itself, not through a comment letter. | CBO PDF p. 4; 91 FR 46591 | “states will not replace all of the lost revenue with revenue from other sources” | Confirmed (CBO wording). **THA's 50 percent: not found in CBO.** |
| F-015 | $340.5B not printed; $191.1B + $149.4B; October 2025 shows $182.7B | All three components matched. $340.5 billion is their sum (191,118 + 149,424 = 340,542 million) and is printed in neither CBO file. $182.7 billion is section 71115's deficit effect, outlays less an $8.4 billion revenue loss. CMS's $601.0 billion and $501.5 billion were confirmed on CMS's tables on October 8. | CBO spreadsheet, Title VII, cells O253, O257 and O850; CBO PDF pp. 4–5 | “section 71115 will decrease deficits by $182.7 billion over the 2025-2034 period” (p. 5; the sentence begins on p. 4) | Confirmed (components). The $340.5 billion total is not a CBO figure. |
| F-024 | No appellate opinion; Fifth Circuit No. 25-40766; amicus brief dated June 24, 2026, p. 15 | Could not be read. The brief's host was blocked, and govinfo had no matching opinion. | Research table only | (secondary) the district court “declared CMS's interpretation unlawful” | Secondary (source blocked). No appellate opinion found. |
| F-022 | Idaho Code § 56-1404(5); no numeric rate on Idaho pages | Could not be read; legislature.idaho.gov was blocked. No published Idaho rate. | Research table only | (secondary) “The assessment base shall be the hospital's net patient revenue for the applicable period.” | Unverifiable (the wording is secondary) |

### Federal Register passages read for this pass

* **F-007: do CMS's central-estimate figures already include the 30 percent state offset? Yes, on CMS's text (91 FR 46590–46593).** At 46591 the sentence assuming states offset 30 percent of the cuts comes directly before CMS's projection that federal Medicaid spending falls $245.8 billion and state spending $138.2 billion, a total of $384.0 billion (Table 11). At 46592 CMS splits the $384.0 billion into $142.1 billion of additional cuts once the SDP rule is counted and $241.9 billion already attributed to SDP cuts. Its 80 percent example applies to what a state "would reduce", the post-offset amount. CMS prints no pre-offset total and never says "net of the offset" in words. The full note is on F-007.
* **91 FR 46596, accounting statement (Table 19): what CMS reports as state effects.** It reports one net transfer: –$147.5 billion to states over 2026–2035, including the interaction. CMS defines it as lower payments to providers plus lower provider-tax payments to states. Annualized, it is −$13,159 million (7 percent) and −$14,056 million (3 percent) in the medium case, in 2026 dollars. The statement does not show $198.7 billion or $51.2 billion. $198.7 billion is the revenue loss (Table 8, 46590). $51.2 billion is $138.2 billion less $87.0 billion, not printed by CMS, and $51.2 − $198.7 = −$147.5. F-010 cites NRHA's $147.5 billion, so the note is on **F-010**. No finding cites $51.2 billion or $198.7 billion; those figures appear in v16's sec. 5 table and in `review/feedback/skeptic.md` (F-010, attack 2).
* **91 FR 30447, "hospitals (87.5 percent)".** The denominator is "these payments": the SDPs states are estimated to have paid in **FFY 2025**, **$143.8 billion**, excluding SDPs that need no preprint approval under § 438.6(c)(2)(i). The base is not split into federal and state shares. No finding or v16 sentence cites this figure, so the result is recorded here and in the citation check above.

### Findings changed in this pass

| Finding | New status | What changed |
|---|---|---|
| F-003 | Confirmed (both counts); what the Federal Register count measures is unverifiable | Was unverifiable. 6,344 (Federal Register, refreshed September 4, 2026) against 960 as filed / 961 corrected; 245 (refreshed September 24, 2026) against 214 as filed / 213 corrected. Neither the definition nor a displayed date is shown. |
| F-005 | Confirmed (CMS limb and CBO limb) | The CBO limb was unverifiable. 1.1 million is at CBO PDF p. 5. |
| F-006 | Confirmed, including the CBO limb from CBO's own cells | The CBO limb was unverifiable. Section 71117: −$34.6 billion outlays and −$0.6 billion revenues; the about $34.0 billion net is not printed by CBO. |
| F-007 | Confirmed (unchanged) | Note added: $384.0 billion, $142.1 billion and $241.9 billion are post-offset figures. |
| F-008 | **Not found**: THA's 50 percent is not in CBO | Was unverifiable. CBO says only that states "will not replace all" lost revenue (p. 4). |
| F-010 | Confirmed (CMS figures) | Was located only. $90.9 billion and −$147.5 billion are at 91 FR 46593 and 46596, and −$136.1 billion at 46594. Note added on the accounting statement's state line. The commenters' letters were not re-read. |
| F-015 | Corrected (unchanged); CBO limb confirmed (components) | The CBO limb was unverifiable. $191.1 billion and $149.4 billion are outlays, 2025–2034. $340.5 billion is their sum, not printed by CBO. $182.7 billion is section 71115's deficit effect (October 2025, pp. 4–5). |
| F-022 | Unverifiable (unchanged) | Note added: no published Idaho rate; the research table's statute wording is secondary. |
| F-024 | Confirmed (Texas HHSC document); court ruling and appeal secondary | The court part was unverifiable and is now secondary. No appellate opinion was found; the citation is Texas v. CMS, 805 F. Supp. 3d 734 (E.D. Tex. 2025), on appeal as Fifth Circuit No. 25-40766, pending as of a June 24, 2026 amicus brief. |

### Moved from unverifiable or not checked to confirmed or corrected

* **F-003**: both counts, from unverifiable to confirmed. What the Federal Register's count measures is still unverifiable.
* **F-005**, CBO limb: from unverifiable to confirmed.
* **F-006**, CBO limb: from unverifiable to confirmed (CBO's cells; the net is arithmetic).
* **F-010**: from not checked (located in the letters only) to confirmed for CMS's figures.
* **F-015**, CBO limb: from unverifiable to confirmed for the components; the $340.5 billion total is not a CBO figure.

No finding moved to corrected in this pass. F-008 moved to not found, F-024's court part to secondary, and F-022 stays unverifiable.

### Other things the sources show

Nothing was edited for these:

* **F-004.** CBO's $182.7 billion is from CBO's estimate of the law as enacted. The July 21, 2025 table is headed "As enacted on July 4, 2025", and the October 2025 document repeats its amounts. So the UHA campaign's "pre-enactment" label for $183 billion does not describe this estimate. Whether CBO also published a pre-enactment figure near $183 billion was not checked.
* **v16 sec. 5.** On CBO's deficit measure, sections 71115 and 71116 sum to $332.1 billion (182.7 + 149.4), against $340.5 billion on outlays. This is arithmetic done here, not a CBO total.
* **CMS's standalone state net.** Without the interaction, CMS's net for states is −$60.5 billion (Table 12, 91 FR 46592). With it, the net is −$147.5 billion (Tables 14 and 19).

### Departures from the conventions in this pass

* **Repeated quotes from one source.** This file now quotes the CMS-2452-P Federal Register document, the CBO October 2025 estimate and 42 CFR 438.6 more than once, because the request asked for exact wording in each row. This departs from the one-quote-per-source rule (`review/CONVENTIONS.md`, section 5). The October 9 notes in the findings files add one more quote each from CMS-2452-P (F-007, F-010) and from the CBO estimate (F-005, F-008, F-015).
* **Checking.** Every quote this pass marks confirmed was matched by script against the downloaded source text, and each is at most 24 words. The two quotes marked secondary (F-022's Idaho statute and F-024's amicus brief) come from the research table and were not matched. Values from the CBO spreadsheet and the Federal Register API are cell and field values, given with cell references or field names.
