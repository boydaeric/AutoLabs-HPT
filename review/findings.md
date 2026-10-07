# Findings from the public comments

*Comment analyst's file. Follows `review/CONVENTIONS.md`. The same findings, field for field, are in `review/findings.csv`.*

## Scope and sources

* **Comments.** Every public comment posted on regulations.gov for CMS-2449-P (docket CMS-2026-1916) and CMS-2452-P (docket CMS-2026-2476), collected through the v4 API on October 7, 2026, with attachment text (OCR for scanned pages). The API's reported totals matched the download.
  * CMS-2449-P: 960 comments as filed / 961 corrected; 660 distinct texts in both views.
  * CMS-2452-P: 214 comments as filed / 213 corrected; 188 distinct texts as filed / 187 corrected.
  * The corrected view moves `CMS-2026-2476-0199`, the California Behavioral Health Association's CMS-2449-P letter, which is an exact copy of `CMS-2026-1916-0958`. 1,174 comments in total either way.
* **Compared against.** The Evidence Ledger v3 (`260927_Evidence_Ledger_v3.md` and `260927_Evidence_Ledger_SectionA_v3.xlsx`; the spreadsheet's 201 Section A rows match the markdown), `output/evidence_ledger_delta.csv`, and the verified rows of `output/verification_log.csv`.
* **`review/article_draft.md` was not available.** It is not in the repository or on any branch. Article sections are therefore given as the published note's sections, as the ledger maps them (synced to note v9): sec. 1-7, footnotes, figures and ledger row IDs. Re-map once the draft is in place.
* **What counts as a finding.** Anything in the comments that confirms, contradicts, adds detail to or opens a new angle on a claim the ledger records. No article text is drafted here.

## Conventions applied

* Counts give both docket views. Counts of hits that were each read are exact; keyword-only counts say "about" and are rounded.
* A commenter's own number is labeled **advocacy figure**. A commenter's restatement of a CMS, CBO or other figure names the original source.
* Quotes are verbatim, at most 24 words, one per source across this file, each with comment ID and page. Everything else is paraphrase.
* "Verification status" cites `output/verification_log.csv` rows where they exist. Otherwise it says where the passage was located for this review, and what was not checked.

## Summary

30 findings. By effect: adds detail 12, confirms 11, contradicts 4, new angle 3. By candidate use: lead 1, support 12, footnote 11, hold 6.

| ID | Rule | Effect | Use | Section | Finding |
|---|---|---|---|---|---|
| F-001 | CMS-2452-P | adds detail | support | status box; sec. 6, gap 6 and gap table; Limitations | The CMS-2452-P comment record is now complete as posted: 214 comments as filed / 213 corrected, of which the 186 numbered -0030 to -0215 were posted on September 22, 2026, after the 28 comments (-0002 to -0029) the ledger reviewed. |
| F-002 | CMS-2452-P | adds detail | footnote | sec. 3b | Of the six organizations whose September 21 letters the ledger could not find on public sites, four filed in the docket: the Children's Hospital Association, NAMD, the Texas Hospital Association and the California Hospital Association. The Illinois Health and Hospital Association and the Illinois Attorney General did not, and MACPAC's letter, which the ledger read on MACPAC's site, is not in the posted docket either. |
| F-003 | CMS-2449-P | contradicts | footnote | sec. 1 | The ledger records 6,344 comments 'posted' in the CMS-2449-P docket, but the regulations.gov API returned 960 posted comments for that docket (961 corrected), so the 6,344 is likely a different counter, such as comments received. |
| F-004 | CMS-2452-P | confirms | support | sec. 1 | Commenters cite CBO's Section 71115 estimate on two different measures with inconsistent labels. Some use $191.1 billion in outlays. Others use $183 billion: a three-letter campaign calls it CBO's 'pre-enactment' estimate, the Pennsylvania human services department calls it a deficit reduction, HAP leaves it unattributed, and AHCCCS presents the two as a '$183 billion to $191 billion' range. |
| F-005 | CMS-2452-P | confirms | support | sec. 1 and footnote 4, fifth axis | Commenters quote CMS's RIA as assuming the provider tax rule has no effect on Medicaid enrollment, and CBPP says the assumption holds across all scenarios. This supports the CMS limb of the note's enrollment axis, which the ledger rates single-source. |
| F-006 | both | new angle | hold | sec. 1 and status box | Commenters bring a third, already-final rule into the accounting: the Section 71117 uniformity-waiver rule. BCBSA says CMS's CMS-2452-P analysis considers it alongside the two proposed rules; CBPP sets its CMS estimate against CBO's; and Iroquois blames it for a $1.5 billion shortfall in New York's MCO tax. |
| F-007 | CMS-2452-P | contradicts | support | sec. 2.3 and Figure 4 note | Commenters quote CMS's primary scenario as assuming states offset 30 percent of lost provider tax revenue, citing 91 FR 46591. The ledger says the primary-scenario narrative carries no offset parameter. |
| F-008 | CMS-2452-P | adds detail | hold | footnote 4, fifth axis 'enrollment and behavioral assumptions' | The Texas Hospital Association says CBO assumed states would replace 50 percent of lost financing when it scored Section 71115, against CMS's 30 percent: a behavioral-assumption difference between the two estimates the note compares. |
| F-009 | both | confirms | footnote | sec. 2.3 | Commenters restate CMS's tax-financing parameter as a share of spending: the Minnesota Hospital Association calls the 65 percent a share of 'state directed payment spending', and NRHA applies CMS's 55-75 percent range to the $774.8 billion SDP reduction. |
| F-010 | CMS-2452-P | confirms | footnote | sec. 2.2-2.4 | Two commenters cite CMS's interaction-inclusive figures as the provider tax rule's effect: Saving Hospitals Saves Lives ($90.9 billion federal, and a $136.1 billion net provider reduction in the high scenario) and NRHA ($90.9 billion federal and $147.5 billion to states, from the accounting statement). |
| F-011 | CMS-2452-P | confirms | support | Summary of findings; sec. 2.4, cautions 2 and 4; Figures 3 and 5 | CHLA Medical Group explains that the +$21.7 billion arises because CMS's interaction analysis assigns most of the payment cut to the SDP rule. It quotes CMS saying the two rules together 'would still be a significant reduction to provider payments', a CMS sentence the ledger does not record. |
| F-012 | CMS-2452-P | adds detail | footnote | sec. 2.4, caution 2 | CHLA Medical Group allocates CMS's provider line to hospitals by their 63 percent share of 2026 provider tax revenue, giving about $138 billion over ten years. It labels this 'an illustrative allocation, not a CMS estimate', which is the disclosed distributional assumption the note says any hospital figure needs. |
| F-013 | CMS-2452-P | confirms | support | sec. 3a | Four commenters, including a state Medicaid agency and a state hospital association, describe CMS's $220.3 billion as a cut in Medicaid payments to providers. Only CHLA Medical Group (and, earlier, Georgetown CCF) describes it as net of the $163.7 billion in tax relief. |
| F-014 | CMS-2452-P | confirms | support | sec. 3b | One comment in the full CMS-2452-P record uses the $681 billion: an individual restates it as a hospital loss, 'in addition to' a $340 billion statutory cost, with no source and no derivation. |
| F-015 | CMS-2452-P | contradicts | lead | sec. 3b, 'The core problem', and footnote 4 | CBPP sets CMS's combined, overlap-adjusted federal estimate ($601 billion) against CBO's $341 billion. In a footnote it argues that adjusting for the extra year, the interaction and the dollar basis would leave a large gap, because two of the three adjustments lower CMS's figure. |
| F-016 | CMS-2449-P | confirms | support | sec. 3b and footnote 4 | Setting CMS's $510 billion against CBO's $149.4 billion is the dominant quantitative argument in the SDP docket, mostly offered as proof that the rule exceeds the statute. Lee County Community Hospital even computes a $360.7 billion difference. |
| F-017 | CMS-2452-P | adds detail | footnote | sec. 3c and the KFF $155 billion | Two national trade groups misstate CMS's interaction-adjusted federal figures. AHIP calls the $154.9 billion federal overlap the reduction remaining after the SDP rule (CMS's figure for that is $90.9 billion). BCBSA gives CMS's range as $9.1 to $90.9 billion, leaving out the $191.8 billion high scenario. |
| F-018 | CMS-2449-P | adds detail | support | sec. 3c | In the SDP docket, the argument that CMS should measure Medicaid payments net of provider taxes is made by the American Hospital Association, a state Medicaid agency (South Carolina DHHS) and a template used by Texas and South Carolina hospitals. That is beyond the six sources the note credits with the gross/net distinction. |
| F-019 | CMS-2449-P | adds detail | footnote | sec. 3c | FAH's argument that CMS should account for the provider taxes that partly finance SDPs is in its CMS-2449-P letter (1916-0676) on page 2, not page 1 as the note cites. The letter confirms the substance. |
| F-020 | both | confirms | footnote | footnote 1 | Commenters reproduce CMS's narrative state figure of $264.4 billion for the SDP rule (FEHP, BCBSA, Paragon), while the one commenter citing CMS-2452-P's restatement uses the table-consistent $264.7 billion. |
| F-021 | CMS-2452-P | confirms | footnote | sec. 3d | Paragon Health Institute carries ASPE's $502-875 billion benefit to non-Medicaid payers and 3.5 percent price effect into the record as support for the rule. It attributes them, correctly, to the 2025 law's reforms. |
| F-022 | CMS-2452-P | contradicts | support | sec. 4 and Figure 6 | The Idaho Hospital Association says Idaho's inpatient hospital assessment already sits above the phased-down threshold class by class, while outpatient is about 1 percent of net patient revenue. If so, the phase-down reaches Idaho, which the note's grouping places in Group E without the phase-down. |
| F-023 | both | adds detail | hold | sec. 4 and Figure 6 | State hospital associations and others put their own dollar figures on several states that the note's grouping flags for data quality or leaves blank. These include Missouri and Minnesota (no estimable above-limit figure) and Florida, Texas, Tennessee and Mississippi (flagged Group D). |
| F-024 | CMS-2452-P | adds detail | support | sec. 7, items 6 and 7 | Texas commenters tie the directed-payment approval dispute to Texas's local provider participation funds. CHAT says CMS is withholding approval of Texas SDP preprints over hold-harmless concerns, using a test CHAT says a federal court has enjoined. TEHP cites CMS's 'Round 1-4' questions on the SFY2027 CHIRP preprint. |
| F-025 | CMS-2452-P | adds detail | footnote | sec. 4, Group D and Texas panel | The Texas Hospital Association says Texas has no statewide hospital tax: its hospital Medicaid payments are funded almost entirely by intergovernmental transfers and 35 local provider assessments, which the state says support about $12 billion in Medicaid payments a year. |
| F-026 | CMS-2449-P | confirms | support | sec. 5, rural paragraph | Many CMS-2449-P commenters, including the Virginia Medicaid agency, argue that defaulting the payment limit to the State plan rate where no Medicare rate exists would freeze payments at the levels SDPs were meant to fix. That supports the note's reading that the default could be more restrictive, not just more uncertain. |
| F-027 | CMS-2452-P | new angle | hold | sec. 5 | NRHA cites third-party figures on rural hospital finances: nearly half operating at negative margins and a median margin of about 1 percent (Chartis). That is the kind of evidence the note says its cited studies do not provide. |
| F-028 | both | adds detail | footnote | sec. 7, item 11 | Many commenters in both dockets set out the legal arguments a challenge would use (Loper Bright, the APA, exceeding statutory authority), and one says CMS is already bound by an injunction on the hold-harmless test. No comment reports a filed suit against either rule. |
| F-029 | CMS-2449-P | new angle | hold | sec. 2.4 caution 2 | The largest single bloc in the SDP docket is fire-based and public EMS agencies opposing Medicare-based limits on GEMT payments. This provider class is inside CMS's provider aggregate but outside the note's hospital-focused exposure analysis. |
| F-030 | CMS-2449-P | adds detail | hold | sec. 5, psychiatric beds and IMD paragraph | The Manhattan Institute flags that the proposed FFS limit's exception for IMDs and psychiatric residential treatment facilities depends on cross-references that do not name them, a drafting gap relevant to the note's point about IMDs and Medicaid adults. |

**Read first:**

* **F-015 (lead).** CBPP publishes the same CMS-versus-CBO comparison the note makes in sec. 3b and argues that the gap survives comparability adjustments. This is a direct counter-argument the note does not yet answer.
* **F-007.** Commenters quote a 30 percent primary-scenario offset at 91 FR 46591, which contradicts the ledger's description of the scenario parameters (CE-32).
* **F-022.** Idaho's own hospital association describes a class-level tax position that would put Idaho within the phase-down's reach, against the note's Group E reading.
* **F-003.** The ledger's 6,344 'posted' comments for the SDP docket do not match the API's 960 posted comments.
* **F-011.** A CMS sentence quoted in the record states the note's central caution about the +$21.7 billion. Find it in the RIA before use.
* **F-001.** The full CMS-2452-P record is now readable; the ledger's re-sweep (M-1) can be completed.

## Findings

### F-001: The CMS-2452-P comment record is now complete as posted: 214 comments as filed / 213 corrected, of which the 186 numbered -0030 to -0215 were posted on September 22, 2026, after the 28 comments (-0002 to -0029) the ledger reviewed.

* **Rule:** CMS-2452-P. **Effect on the article:** adds detail. **Candidate use:** support.
* **Comments:** All comments in docket CMS-2026-2476 (IDs -0002 to -0215).
* **Excerpt:** paraphrase only.
* **Figure:** Counts, docket CMS-2026-2476: 214 comments as filed / 213 corrected; 188 distinct texts as filed / 187 corrected; 10 campaigns covering 36 comments in both views. Positions as filed / corrected: oppose 73/73, request for changes 127/126, mixed 8/8, support 4/4, unclear or off-topic 2/2. Collected from the regulations.gov v4 API on October 7, 2026; the API's reported total (214) matched the download.
* **Verification:** Counts reproduce from output/comments_tagged.csv and output/docket_totals.csv. Posting dates are the API's postedDate field: the 186 later comments all carry 2026-09-22.
* **Distinct texts vs campaign copies:** Distinct texts 188 as filed / 187 corrected; comments inside campaigns 36 in both views.
* **Article section:** Note status box; sec. 6, gap 6 and gap table; Limitations (ledger RM-21, RM-22, NC-14, C-11, B-7, monitoring trigger M-1).
* **What it changes:** The ledger's M-1 re-sweep (scheduled from ID -0030) can be run against the full posted record. Gap 6 rates the CMS-2452-P comment record 'Partial (reviewed only for the $681 billion figure)'; the whole posted record has now been read for the figures and claims in F-002 to F-030. Whether the note extends its scope is the author's decision.
* **Risk:** Low for the counts. Medium if the note widens its negative claims: the record is a snapshot (October 7, 2026), keyword searches over OCR text can miss figures printed as images, and letters published only on submitters' sites are not in it (F-002).

### F-002: Of the six organizations whose September 21 letters the ledger could not find on public sites, four filed in the docket: the Children's Hospital Association, NAMD, the Texas Hospital Association and the California Hospital Association. The Illinois Health and Hospital Association and the Illinois Attorney General did not, and MACPAC's letter, which the ledger read on MACPAC's site, is not in the posted docket either.

* **Rule:** CMS-2452-P. **Effect on the article:** adds detail. **Candidate use:** footnote.
* **Comments:** Now posted: 2476-0148 Children's Hospital Association; 2476-0116 National Association of Medicaid Directors; 2476-0109 Texas Hospital Association; 2476-0057 California Hospital Association. Letters the ledger read on submitters' sites, now also posted: 2476-0113 AHA; 2476-0070 FAH; 2476-0086 AAMC; 2476-0074 America's Essential Hospitals; 2476-0089 HAP; 2476-0130 Paragon. Not in the posted docket: MACPAC, Illinois Health and Hospital Association, Illinois Attorney General.
* **Excerpt:** paraphrase only.
* **Figure:** n/a
* **Verification:** Matched on the organization field of each posted comment (output/comments_tagged.csv). Each letter's text was searched for the $681 billion, a multi-state net-of-tax estimate and a reconciliation of CMS's overlap or net provider figures (results in F-014, F-015, F-018, F-011).
* **Distinct texts vs campaign copies:** 10 comments, 10 distinct texts in both views; none is a campaign copy.
* **Article section:** Note sec. 3b (search scope for the $681 billion); ledger C-4, C-9, NC-04, NC-09.
* **What it changes:** The list of organizations 'for which no letter was located' in C-4 is out of date for four of six. None of the four contains the $681 billion figure.
* **Risk:** Low. Organization names were matched by text; a letter filed under an individual's name would be missed.

### F-003: The ledger records 6,344 comments 'posted' in the CMS-2449-P docket, but the regulations.gov API returned 960 posted comments for that docket (961 corrected), so the 6,344 is likely a different counter, such as comments received.

* **Rule:** CMS-2449-P. **Effect on the article:** contradicts. **Candidate use:** footnote.
* **Comments:** Docket CMS-2026-1916 as a whole.
* **Excerpt:** paraphrase only.
* **Figure:** 960 posted comments as filed / 961 corrected (adding 2476-0199), collected October 7, 2026; the API's reported total (960) matched the download. Ledger figure: 6,344 'posted' (RM-04, as of September 5, 2026).
* **Verification:** API total and enumerated IDs both 960 in the collection log. The regulations.gov docket page's 'comments received' counter was not checked.
* **Distinct texts vs campaign copies:** All 960 comments; 660 distinct texts in both views.
* **Article section:** Note sec. 1 (ledger RM-04, RM-21; decision log B-7, which contrasts 20 CMS-2452-P comments with 6,344).
* **What it changes:** The note's comment count for the SDP docket may need relabelling ('received', not 'posted') or replacing. B-7's comparison of 20 against 6,344 mixes the two counters if 6,344 is a received count.
* **Risk:** Medium. Until the docket page is checked, either number could be the right one for the note's purpose. The 6,344 is perishable in the ledger's own terms.

### F-004: Commenters cite CBO's Section 71115 estimate on two different measures with inconsistent labels. Some use $191.1 billion in outlays. Others use $183 billion: a three-letter campaign calls it CBO's 'pre-enactment' estimate, the Pennsylvania human services department calls it a deficit reduction, HAP leaves it unattributed, and AHCCCS presents the two as a '$183 billion to $191 billion' range.

* **Rule:** CMS-2452-P. **Effect on the article:** confirms. **Candidate use:** support.
* **Comments:** 2476-0201 Arizona Health Care Cost Containment System (AHCCCS, state agency); 2476-0097 UHA, 2476-0187 Health System Alliance of Arizona, 2476-0195 North Carolina Healthcare Association (one 3-letter campaign); 2476-0126 Pennsylvania Department of Human Services; 2476-0089 HAP; outlay users include 2476-0029 Georgetown CCF, 2476-0107 OpenSky, 2476-0099 Families USA, 2476-0033 CBPP.
* **Excerpt:** "…scored the provider tax provisions of H.R. 1 at roughly $183 billion to $191 billion in federal savings…" (`CMS-2026-2476-0201`, Arizona Health Care Cost Containment System (AHCCCS); CMS-2026-2476-0201_attachment_1.pdf, p. 1 of 14)
* **Figure:** CBO figures as quoted by commenters: $191.1 billion, federal outlays, FY2025-2034 (Georgetown CCF); $183 billion, '10 years' (UHA campaign) or 'reduction in federal deficits' (PA DHS). Ledger: CBO Sec. 71115 outlays $191.1B and net deficit $182.7B, FY2025-2034, nominal (SB-09, SB-14).
* **Verification:** AHCCCS range: verification_log row 4145 confirmed, p. 1. Georgetown $191.1B: row 3648 confirmed, p. 1. HAP $183B: row 3854 corrected (source unnamed by HAP). UHA campaign (p. 17 of 20) and PA DHS (p. 1 of 23): located for this review; not in the verification log.
* **Distinct texts vs campaign copies:** Keyword count of comments citing $183 billion or $191 billion: 17 comments (14 distinct texts) in both views. The UHA wording appears in all three campaign letters.
* **Article section:** Note sec. 1 (CBO comparison) and footnote 2 (ledger SB-09, SB-14, SB-17, CE-28, D-13; C-4 'nearest passage' on HAP).
* **What it changes:** This is direct evidence for D-13's diagnosis: readers treat one CBO estimate on two measures as two vintages ('pre-enactment') or as a range. It also updates C-4, which found that none of four site letters attributed a Sec. 71115 figure to CBO; several posted comments do.
* **Risk:** Low. Commenters are quoting CBO second-hand; the CBO figures themselves rest on CRS R48633 per the ledger.

### F-005: Commenters quote CMS's RIA as assuming the provider tax rule has no effect on Medicaid enrollment, and CBPP says the assumption holds across all scenarios. This supports the CMS limb of the note's enrollment axis, which the ledger rates single-source.

* **Rule:** CMS-2452-P. **Effect on the article:** confirms. **Candidate use:** support.
* **Comments:** 2476-0179 Jason Levitis (individual; quotes the RIA); 2476-0033 Center on Budget and Policy Priorities; 2476-0029 Georgetown CCF (CBO's 1.1 million uninsured).
* **Excerpt:** "…have no effect on enrollment and that all reductions in spending would be made through reductions in provider payments and benefits provided." (`CMS-2026-2476-0179`, Jason Levitis; CMS-2026-2476-0179_attachment_1.pdf, p. 11 of 12)
* **Figure:** CBO, as quoted by commenters: Sec. 71115 increases the uninsured by 1.1 million by 2034. CMS (as quoted): no enrollment effect in any scenario.
* **Verification:** Georgetown 1.1 million: verification_log row 3655 confirmed, p. 4. Levitis quotation located at p. 11 of 12; CBPP 'zero enrollment impacts … across its full range of scenarios' at p. 9 of 13. Neither quotation was checked against the Federal Register page, which the commenters do not give in the quoted passage.
* **Distinct texts vs campaign copies:** Keyword counts, docket CMS-2026-2476 (approximate): about 14 comments (about 13 distinct texts) in both views state the no-enrollment assumption; about 14 comments (about 13 distinct texts) in both views cite '1.1 million'.
* **Article section:** Note sec. 1 and footnote 4, fifth axis (ledger SB-24, SB-21).
* **What it changes:** SB-24's CMS limb rests on the worksheet's lack of an enrollment series. A CMS sentence quoted in the record would let the note cite CMS directly, once the Federal Register page is found.
* **Risk:** Low to medium: commenter quotation of CMS, not yet matched to the RIA page.

### F-006: Commenters bring a third, already-final rule into the accounting: the Section 71117 uniformity-waiver rule. BCBSA says CMS's CMS-2452-P analysis considers it alongside the two proposed rules; CBPP sets its CMS estimate against CBO's; and Iroquois blames it for a $1.5 billion shortfall in New York's MCO tax.

* **Rule:** both. **Effect on the article:** new angle. **Candidate use:** hold.
* **Comments:** 2476-0091 Blue Cross Blue Shield Association; 2476-0033 Center on Budget and Policy Priorities; 2476-0072 Iroquois Healthcare Association.
* **Excerpt:** "This means that New York will yield approximately $1.5 billion less revenue than anticipated." (`CMS-2026-2476-0072`, Iroquois Healthcare Association; CMS-2026-2476-0072_attachment_1.pdf, p. 1 of 3)
* **Figure:** CBPP, quoting CBO: $34 billion net federal reduction from the uniformity-waiver restrictions; CBPP, quoting CMS's final-rule RIA: $78.2 billion federal and $46.9 billion state (period not stated in the passage). Advocacy figure (Iroquois): New York MCO tax yields about $1.5 billion less than the $3.7 billion originally projected over two years.
* **Verification:** Iroquois $1.5B: verification_log row 3779 corrected (cause is the February 2026 uniformity-waiver final rule, not CMS-2452-P), p. 1. BCBSA's CMS-2448-F statement and CBPP's $34B / $78.2B / $46.9B located at p. 27 of 28 and p. 2 of 13; not in the verification log; CMS's RIA for the final rule was not read.
* **Distinct texts vs campaign copies:** Keyword count (approximate): about 40 comments (about 40 distinct texts) in both views mention Sec. 71117, uniformity waivers or CMS-2448-F; most mention them in passing.
* **Article section:** Note sec. 1 and status box (scope of rules analyzed); ledger CE-43 (baselines), TP-13 (ASPE covers Secs. 71115-71117).
* **What it changes:** The note analyzes two proposed rules. If CMS-2452-P's RIA does fold in the finalized Sec. 71117 rule, that bears on what the provider tax rule's figures include (CE-43) and on the overlap. It also shows the CMS-versus-CBO gap recurring for a third provision.
* **Risk:** Medium: BCBSA's description of CMS's analysis is unverified, and the third rule is outside the note's stated scope.

### F-007: Commenters quote CMS's primary scenario as assuming states offset 30 percent of lost provider tax revenue, citing 91 FR 46591. The ledger says the primary-scenario narrative carries no offset parameter.

* **Rule:** CMS-2452-P. **Effect on the article:** contradicts. **Candidate use:** support.
* **Comments:** 2476-0109 Texas Hospital Association (gives 91 FR 46591); 2476-0212 CHLA Medical Group (30 primary, 20 high, 40 low); 2476-0029 Georgetown CCF; 2476-0031 NHeLP; 2476-0097 UHA campaign; 2476-0179 Jason Levitis; 2476-0107 OpenSky; 2476-0033 CBPP; 2476-0089 HAP.
* **Excerpt:** "CMS assumes in this analysis that “states would offset 30 percent of these cuts with other revenue sources,” primarily general fund revenue." (`CMS-2026-2476-0109`, Texas Hospital Association (THA); CMS-2026-2476-0109_attachment_1.pdf, p. 6 of 9)
* **Figure:** CMS assumption, as quoted: states offset 30 percent of the provider tax revenue reductions (primary), 20 percent (high scenario) and 40 percent (low scenario), with the provider tax rule's 10-year horizon 2026-2035.
* **Verification:** THA: verification_log row 3939 confirmed (p. 6) and row 3941 confirmed (p. 7); THA's footnote 10 ('Ibid.') points to 91 FR 46591. CHLA scenario split located (docx). The Federal Register page itself was not read.
* **Distinct texts vs campaign copies:** All quoting comments were read: 12 comments (9 distinct texts) in both views. Three are copies in the UHA campaign; two in another 2-letter campaign (2476-0075 / -0125).
* **Article section:** Note sec. 2.3 and Figure 4 note (ledger CE-32, CE-34, CE-46).
* **What it changes:** CE-32's cross-check says the primary set is 'specified on one parameter' (65 percent) where the low and high sets are specified on three. If 91 FR 46591 carries the 30 percent offset, the primary scenario has at least two stated parameters, and the description of how the scenarios differ needs correcting. The offset also enters the overlap and the net provider line.
* **Risk:** Medium: rests on commenters' quotation until 91 FR 46591 is read. THA itself attaches 20 percent to the low scenario, against CHLA and CE-32 (40 percent low, 20 percent high), so the scenario labels need checking too.

### F-008: The Texas Hospital Association says CBO assumed states would replace 50 percent of lost financing when it scored Section 71115, against CMS's 30 percent: a behavioral-assumption difference between the two estimates the note compares.

* **Rule:** CMS-2452-P. **Effect on the article:** adds detail. **Candidate use:** hold.
* **Comments:** 2476-0109 Texas Hospital Association.
* **Excerpt:** paraphrase only.
* **Figure:** Assumption shares as reported by THA: CBO 50 percent of lost financing replaced (Sec. 71115 score); CMS 30 percent (primary), 20 or 40 percent (other scenarios). Not a dollar figure.
* **Verification:** Located at p. 6 of 9 (paraphrased here; THA is quoted in F-007). THA's account of CBO's assumption was not checked against CBO's cost estimate.
* **Distinct texts vs campaign copies:** 1 comment, 1 distinct text in both views; not in a campaign.
* **Article section:** Note footnote 4, fifth axis 'enrollment and behavioral assumptions' (ledger SB-21, SB-23).
* **What it changes:** If confirmed in CBO's estimate, this gives a named, quantified behavioral difference behind the CMS-CBO gap. That is concrete support for footnote 4's point that the two sides rest on different assumptions.
* **Risk:** Medium to high: single advocacy source describing CBO's method; hold until CBO's documentation is read.

### F-009: Commenters restate CMS's tax-financing parameter as a share of spending: the Minnesota Hospital Association calls the 65 percent a share of 'state directed payment spending', and NRHA applies CMS's 55-75 percent range to the $774.8 billion SDP reduction.

* **Rule:** both. **Effect on the article:** confirms. **Candidate use:** footnote.
* **Comments:** 2476-0204 Minnesota Hospital Association; 2476-0056 Kentucky Health Collaborative ('65 percent of state directed payments'); 2476-0106 BAYADA Home Health Care (55-75 percent 'of SDP spending'); 2476-0093 National Rural Health Association.
* **Excerpt:** "…it assumes that 65 percent of state directed payment spending is financed with provider taxes." (`CMS-2026-2476-0204`, Minnesota Hospital Association; CMS-2026-2476-0204_attachment_1.pdf, p. 10 of 11)
* **Figure:** CMS parameters as quoted: 65 percent (primary) and 55-75 percent (range) of SDPs financed with provider taxes. NRHA pairs the range with CMS's $774.8 billion SDP reduction, 2026-2035, real 2026 dollars.
* **Verification:** Located: MHA p. 10 of 11; KHC p. 2 of 2; BAYADA p. 10 of 12; NRHA p. 7 of 10. Not in the verification log (no dollar figures of the commenters' own).
* **Distinct texts vs campaign copies:** Keyword count: 4 comments (4 distinct texts) in both views.
* **Article section:** Note sec. 2.3 (ledger CE-48, CE-49, CE-31; TP-19 withdrawn).
* **What it changes:** This supports the note's care in keeping CMS's word 'SDPs' for the 65 percent (CE-48). Readers already convert it into a share of dollars, which is the reading behind the withdrawn TP-19 answer. BAYADA's 'of SDP spending' matches CMS's own range sentence (CE-31), so only the 65 percent restatements depart from CMS's wording.
* **Risk:** Low. NRHA also repeats CMS's misprinted docket number 'CMS-2249-P' (RM-20) on the same page.

### F-010: Two commenters cite CMS's interaction-inclusive figures as the provider tax rule's effect: Saving Hospitals Saves Lives ($90.9 billion federal, and a $136.1 billion net provider reduction in the high scenario) and NRHA ($90.9 billion federal and $147.5 billion to states, from the accounting statement).

* **Rule:** CMS-2452-P. **Effect on the article:** confirms. **Candidate use:** footnote.
* **Comments:** 2476-0145 Saving Hospitals Saves Lives Coalition (cites Table 14); 2476-0093 National Rural Health Association (cites Table 19, Accounting Statement, 91 FR 46596).
* **Excerpt:** "After accounting for interaction with the state-directed-payment provisions, CMS’s base scenario projects approximately $90.9 billion less in federal Medicaid spending over ten years…" (`CMS-2026-2476-0145`, Saving Hospitals Saves Lives Coalition; CMS-2026-2476-0145_attachment_1.pdf, p. 3 of 9)
* **Figure:** CMS figures as quoted: federal -$90.9 billion (Table 14, primary, including interaction); states -$147.5 billion net; providers -$136.1 billion (high scenario, including interaction); 2026-2035, real 2026 dollars.
* **Verification:** Located: SHSL p. 3 of 9 ($90.9B) and p. 4 ($136.1B); NRHA p. 8 of 10. Values match the ledger's CE-11 and CE-18. Not in the verification log.
* **Distinct texts vs campaign copies:** 2 comments, 2 distinct texts in both views; neither in a campaign.
* **Article section:** Note sec. 2.2-2.4 (ledger CE-11, CE-18, CE-44).
* **What it changes:** This shows CE-44's point in use: CMS's accounting statement presents the interaction-inclusive figures as the rule's effect, and commenters carry them forward. Neither commenter stacks them with the SDP rule, so the +$21.7 billion versus combined-loss question (sec. 2.4) is not resolved in their letters.
* **Risk:** Low.

### F-011: CHLA Medical Group explains that the +$21.7 billion arises because CMS's interaction analysis assigns most of the payment cut to the SDP rule. It quotes CMS saying the two rules together 'would still be a significant reduction to provider payments', a CMS sentence the ledger does not record.

* **Rule:** CMS-2452-P. **Effect on the article:** confirms. **Candidate use:** support.
* **Comments:** 2476-0212 Children's Hospital Los Angeles Medical Group.
* **Excerpt:** "CMS states that the net effect of both proposed rules “would still be a significant reduction to provider payments through Medicaid over time.”" (`CMS-2026-2476-0212`, Hospital Los Angeles Medical Group; CMS-2026-2476-0212_attachment_1.docx (docx, no fixed pages))
* **Figure:** CMS figure as quoted: providers +$21.7 billion over ten years (CMS-2452-P including interaction, primary, 2026-2035, real 2026 dollars); high scenario -$136.1 billion.
* **Verification:** Located in the docx attachment (no page numbers). The $220.3B and $138B rows of the same letter are verified (verification_log rows 4183, 4184, confirmed). The quoted CMS sentence was not matched to a Federal Register page; CHLA gives none in the passage.
* **Distinct texts vs campaign copies:** 1 comment, 1 distinct text in both views; not in a campaign.
* **Article section:** Note Summary of findings; sec. 2.4, cautions 2 and 4; Figures 3 and 5 (ledger CE-51, CE-52, D-14).
* **What it changes:** If the sentence is in the RIA, CMS itself states the note's central caution: the +$21.7 billion is an increment, not the combined effect. CE-52 currently rests on the note's own stacking arithmetic.
* **Risk:** Medium until the CMS sentence is found in the Federal Register text. CHLA is a provider group arguing against the rule.

### F-012: CHLA Medical Group allocates CMS's provider line to hospitals by their 63 percent share of 2026 provider tax revenue, giving about $138 billion over ten years. It labels this 'an illustrative allocation, not a CMS estimate', which is the disclosed distributional assumption the note says any hospital figure needs.

* **Rule:** CMS-2452-P. **Effect on the article:** adds detail. **Candidate use:** footnote.
* **Comments:** 2476-0212 Children's Hospital Los Angeles Medical Group.
* **Excerpt:** paraphrase only.
* **Figure:** Advocacy figure (CHLA Medical Group): about $138 billion less net Medicaid support to the hospital tax class over ten years (about $13.8 billion a year), computed as 63 percent ($61.8B of $98.6B CY2026 provider tax revenue) of CMS's -$220.3 billion net provider line (Table 12, 2026-2035, real 2026 dollars).
* **Verification:** verification_log rows 4183 ($220.3B) and 4184 ($138B) confirmed (docx). Paraphrased here (CHLA is quoted in F-011).
* **Distinct texts vs campaign copies:** 1 comment, 1 distinct text in both views; not in a campaign.
* **Article section:** Note sec. 2.4, caution 2 (ledger CE-51, NC-07, C-7; durable finding 'a provider aggregate is not a hospital figure').
* **What it changes:** This is a worked example of the conversion the note says cannot be made without a disclosed distributional assumption, made with the assumption disclosed. It applies a one-year tax-revenue share to a ten-year net payment line, which shows how much such an allocation assumes.
* **Risk:** Low as an example. High if cited as a hospital estimate.

### F-013: Four commenters, including a state Medicaid agency and a state hospital association, describe CMS's $220.3 billion as a cut in Medicaid payments to providers. Only CHLA Medical Group (and, earlier, Georgetown CCF) describes it as net of the $163.7 billion in tax relief.

* **Rule:** CMS-2452-P. **Effect on the article:** confirms. **Candidate use:** support.
* **Comments:** Payment-cut reading: 2476-0049 American College of Obstetricians and Gynecologists ('from this rule alone'); 2476-0085 Pennsylvania Advocates and Resources for Autism and Intellectual Disability; 2476-0190 New Jersey Hospital Association ('over 10 years (2025-2035)'); 2476-0201 AHCCCS. Net reading: 2476-0212 CHLA Medical Group.
* **Excerpt:** "…the Regulatory Impact Analysis found that providers would see Medicaid payment cuts of 220.3 billion dollars from this rule alone." (`CMS-2026-2476-0049`, American College of Obstetricians & Gynecologists; CMS-2026-2476-0049_attachment_1.pdf, p. 2 of 7)
* **Figure:** CMS figure as quoted: $220.3 billion, CMS-2452-P Table 12 provider line, standalone, primary, 2026-2035, real 2026 dollars; net of $163.7 billion provider tax relief per the ledger (CE-36).
* **Verification:** AHCCCS: verification_log row 4145 confirmed, p. 1. CHLA: row 4183 confirmed (docx). ACOG p. 2 of 7, PAR p. 1 of 2, NJHA p. 2 of 8: located for this review; not in the verification log.
* **Distinct texts vs campaign copies:** Every comment citing $220.3 billion was read: 5 comments (5 distinct texts) in both views; none in a campaign.
* **Article section:** Note sec. 3a (HFMA's $56.6 billion) and sec. 3c (ledger CE-36, CE-55, TP-01, TP-08, TP-24).
* **What it changes:** HFMA's reading of the provider line as a payment cut is common in the docket, not isolated, which supports CE-55's suggestion that CMS's own 'as shown in table 12' wording invites it. None of the five subtracts the tax relief a second time, so none reproduces the $56.6 billion.
* **Risk:** Low to medium: commenters may mean 'payments net of taxes' loosely. NJHA's period (2025-2035, 11 years) is a commenter error.

### F-014: One comment in the full CMS-2452-P record uses the $681 billion: an individual restates it as a hospital loss, 'in addition to' a $340 billion statutory cost, with no source and no derivation.

* **Rule:** CMS-2452-P. **Effect on the article:** confirms. **Candidate use:** support.
* **Comments:** 2476-0079 Michael Tanasi (individual).
* **Excerpt:** "Hospitals alone stand to lose an estimated $681 billion over a ten-year period, in addition to the $340 billion cost…" (`CMS-2026-2476-0079`, Michael Tanasi; CMS-2026-2476-0079, comment field)
* **Figure:** Figure as restated by the commenter: $681 billion over ten years, attributed to hospitals; $340 billion attributed to H.R. 1. Matches POLITICO's construction (756 + 265 - 340 = 681, ledger SB-02).
* **Verification:** Exact search of every comment's full text, attachments and OCR included: 1 comments (1 distinct texts) in both views contain '$681 billion'. Located in the comment field. Not in the verification log.
* **Distinct texts vs campaign copies:** 1 comment, 1 distinct text in both views; not in a campaign. A second '681' hit is a telephone number (1916-0300).
* **Article section:** Note sec. 3b (ledger SB-01, SB-03, SB-11, SB-12, SB-20, NC-04, C-4).
* **What it changes:** This extends NC-04 and SB-12 to the full posted record: no derivation, one restatement. The restatement reads the figure as a hospital loss, which the note's SB-20 says it cannot be.
* **Risk:** Low. It is an individual's comment and is not evidence of where the figure came from.

### F-015: CBPP sets CMS's combined, overlap-adjusted federal estimate ($601 billion) against CBO's $341 billion. In a footnote it argues that adjusting for the extra year, the interaction and the dollar basis would leave a large gap, because two of the three adjustments lower CMS's figure.

* **Rule:** CMS-2452-P. **Effect on the article:** contradicts. **Candidate use:** lead.
* **Comments:** 2476-0033 Center on Budget and Policy Priorities.
* **Excerpt:** "…a very large gap between the two estimates would remain even with plausible adjustments to increase comparability." (`CMS-2026-2476-0033`, Center on Budget and Policy Priorities; CMS-2026-2476-0033_attachment_1.pdf, p. 9 of 13)
* **Figure:** CMS figure as quoted: $601 billion combined federal Medicaid outlay reduction, both rules, overlap-adjusted (2026-2035, real 2026 dollars; ledger SB-23: 510.1 + 90.9). CBO figure as quoted: $341 billion federal outlays from Secs. 71115 and 71116 (CBPP's rounding of 191.1 + 149.4 = 340.5, FY2025-2034, nominal).
* **Verification:** $601B: verification_log row 3691 confirmed, p. 9. $341B and footnote 23 located at p. 9 of 13 (not in the verification log). CBPP's directional reasoning is its own analysis.
* **Distinct texts vs campaign copies:** 1 comment, 1 distinct text in both views; not in a campaign.
* **Article section:** Note sec. 3b, 'The core problem', and footnote 4 (ledger SB-21, SB-23, NC-10, C-10, NC-13).
* **What it changes:** SB-23 says the $601.0B-versus-$340.5B gap 'does not show that the rules go beyond the statute' and that footnote 4's axes 'leave its cause unresolved'. CBPP, a published source, makes the same comparison and argues the opposite on three axes: window, interaction and dollar basis. It does not address baseline, fiscal-year framing or enrollment assumptions. The note also says it located no public document reconciling these figures (NC-10); CBPP's comment is a partial one on the federal side.
* **Risk:** High if unaddressed: a direct, citable counter-argument from a prominent organization. CBPP opposes the rule, and its footnote is qualitative (no adjusted figures).

### F-016: Setting CMS's $510 billion against CBO's $149.4 billion is the dominant quantitative argument in the SDP docket, mostly offered as proof that the rule exceeds the statute. Lee County Community Hospital even computes a $360.7 billion difference.

* **Rule:** CMS-2449-P. **Effect on the article:** confirms. **Candidate use:** support.
* **Comments:** Examples: 1916-0902 Lee County Community Hospital ($360.7 billion difference); 1916-0128 American Academy of Family Physicians ('more than three times'); 1916-0756 Allegheny Health Network.
* **Excerpt:** "CMS’s own projected federal savings exceed CBO’s score for the statute by $360.7 billion." (`CMS-2026-1916-0902`, Lee County Community Hospital; CMS-2026-1916-0902_attachment_1.docx (docx, no fixed pages))
* **Figure:** CMS figure as quoted: $510.1 billion federal, 2026-2035, real 2026 dollars. CBO figure as quoted: $149.4 billion, Sec. 71116, FY2025-2034, nominal. Advocacy figure (Lee County): $360.7 billion difference.
* **Verification:** verification_log rows 3411 ($360.7B, docx), 87 ($510B, docx), 2532-2533 ($510B, $149.4B, p. 2), all confirmed.
* **Distinct texts vs campaign copies:** Keyword counts, docket CMS-2026-1916: $510 billion in about 120 comments (about 90 distinct texts) in both views; $149.4 billion in about 90 comments (about 60 distinct texts) in both views; 'beyond the statute' language in about 380 comments (about 230 distinct texts) in both views. Approximate.
* **Article section:** Note sec. 3b and footnote 4 (ledger SB-21, SB-23, CE-43).
* **What it changes:** POLITICO's construction mirrors what most CMS-2449-P commenters already did. The note's caution about subtracting a CBO statutory score from CMS rule estimates applies to the docket as a whole, not to one article. Note also that both RIAs score the statute as the rules implement it (CE-43), so the comparison cannot isolate the rule's own effect, which is the claim these commenters make.
* **Risk:** Low for the pattern. Counts are keyword-based and approximate.

### F-017: Two national trade groups misstate CMS's interaction-adjusted federal figures. AHIP calls the $154.9 billion federal overlap the reduction remaining after the SDP rule (CMS's figure for that is $90.9 billion). BCBSA gives CMS's range as $9.1 to $90.9 billion, leaving out the $191.8 billion high scenario.

* **Rule:** CMS-2452-P. **Effect on the article:** adds detail. **Candidate use:** footnote.
* **Comments:** 2476-0101 AHIP; 2476-0091 Blue Cross Blue Shield Association.
* **Excerpt:** "Alternatively, CMS estimates that the reduction would be $154.9 billion after accounting for separate changes in the rules governing state directed payments." (`CMS-2026-2476-0101`, AHIP; CMS-2026-2476-0101_attachment_1.pdf, p. 1 of 12)
* **Figure:** CMS figures per the ledger: federal overlap $154.9 billion (CE-15); federal including interaction +$90.9B primary, +$9.1B low, +$191.8B high (CE-11, CE-29, CE-44); 2026-2035, real 2026 dollars.
* **Verification:** BCBSA: verification_log rows 3869-3870 confirmed, p. 27. AHIP located at p. 1 of 12 (footnote 1); not in the verification log.
* **Distinct texts vs campaign copies:** 2 comments, 2 distinct texts in both views; neither in a campaign.
* **Article section:** Note sec. 3c and the KFF $155 billion (ledger TP-15, CE-15, CE-44).
* **What it changes:** This is more evidence for the note's thesis that the overlap figures are hard to read. AHIP's version inverts KFF's correct framing of the $155 billion (TP-15): it calls the overlap what remains after the SDP rule.
* **Risk:** Low to medium: AHIP's footnote is terse, and its intended quantity is inferred.

### F-018: In the SDP docket, the argument that CMS should measure Medicaid payments net of provider taxes is made by the American Hospital Association, a state Medicaid agency (South Carolina DHHS) and a template used by Texas and South Carolina hospitals. That is beyond the six sources the note credits with the gross/net distinction.

* **Rule:** CMS-2449-P. **Effect on the article:** adds detail. **Candidate use:** support.
* **Comments:** 1916-0928 American Hospital Association; 1916-0923 South Carolina Department of Health and Human Services; template letters 1916-0369 South Carolina Hospital Association, 1916-0476 CHRISTUS Health, 1916-0808 Bexar County Hospital District, 1916-0437 Midland County Hospital District, 1916-0424 Community Health Network, 1916-0787 Baker Donelson; also 1916-0581 Texas Hospital Association, 1916-0814 DHR Health.
* **Excerpt:** "AHA urges CMS to adopt a net-of-tax methodology when implementing the P.L. 119-21 provision limiting SDPs to Medicare rates." (`CMS-2026-1916-0928`, American Hospital Association; CMS-2026-1916-0928_attachment_1.pdf, p. 11 of 17)
* **Figure:** n/a (methodological position).
* **Verification:** Located: AHA p. 11 of 17; SC DHHS p. 3 of 4. Positions, not figures; not in the verification log.
* **Distinct texts vs campaign copies:** Keyword count, docket CMS-2026-1916: 11 comments (8 distinct texts) in both views; several are template variants sharing a heading.
* **Article section:** Note sec. 3c (ledger NC-13, TP-21, TP-17).
* **What it changes:** NC-13 says the measurement discipline 'sits across six sources' and has not been assembled. The record shows the net-of-tax argument is broader, including the largest hospital association and a state agency. These letters apply it to the payment-limit test (Medicaid rate net of taxes against the Medicare rate), not to the RIA's net provider aggregate, so they support the point without assembling it.
* **Risk:** Medium: different concept from the note's gross/net provider line. Conflating the two would overstate the support.

### F-019: FAH's argument that CMS should account for the provider taxes that partly finance SDPs is in its CMS-2449-P letter (1916-0676) on page 2, not page 1 as the note cites. The letter confirms the substance.

* **Rule:** CMS-2449-P. **Effect on the article:** adds detail. **Candidate use:** footnote.
* **Comments:** 1916-0676 Federation of American Hospitals.
* **Excerpt:** "…calculate the total payment rate to reflect the actual effect of SDPs on provider payment, including by accounting for the provider taxes…" (`CMS-2026-1916-0676`, Federation of American Hospitals; CMS-2026-1916-0676_attachment_1.pdf, p. 2 of 45)
* **Figure:** n/a (methodological position).
* **Verification:** Located at p. 2 of 45 (printed page number 2; p. 1 is the letter's opening). Not in the verification log.
* **Distinct texts vs campaign copies:** 1 comment, 1 distinct text in both views; not in a campaign.
* **Article section:** Note sec. 3c (ledger TP-21, which records 'p. 1' and 'letter not re-read').
* **What it changes:** TP-21 can move from single-source to verified, with the pin cite corrected to p. 2.
* **Risk:** Low.

### F-020: Commenters reproduce CMS's narrative state figure of $264.4 billion for the SDP rule (FEHP, BCBSA, Paragon), while the one commenter citing CMS-2452-P's restatement uses the table-consistent $264.7 billion.

* **Rule:** both. **Effect on the article:** confirms. **Candidate use:** footnote.
* **Comments:** $264.4B: 1916-0417 Florida Essential Healthcare Partnerships; 1916-0509 Blue Cross Blue Shield Association; 1916-0648 Paragon Health Institute. $264.7B: 2476-0056 Kentucky Health Collaborative (cites 91 FR 46592-93).
* **Excerpt:** "…with related state Medicaid spending reduced by $264.4 billion over the same time period." (`CMS-2026-1916-0417`, Florida Essential Healthcare Partnerships; CMS-2026-1916-0417_attachment_1.pdf, p. 6 of 14)
* **Figure:** CMS figures as quoted: state reduction $264.4 billion (CMS-2449-P narrative) or $264.7 billion (table-consistent), 2026-2035, real 2026 dollars.
* **Verification:** Located: FEHP p. 6 of 14; BCBSA p. 38 of 40; Paragon p. 3 of 14; KHC p. 2 of 2 (KHC's $774.8B is verification_log row 3757, confirmed). Not otherwise in the verification log.
* **Distinct texts vs campaign copies:** Every hit was read: $264.4 billion in 3 comments (3 distinct texts) in both views; $264.7 billion in 1 comments (1 distinct texts) in both views.
* **Article section:** Note footnote 1 (ledger CE-03, CE-24, B-3).
* **What it changes:** This confirms footnote 1's point that CMS's narrative figure circulates and does not close against $510.1B + X = $774.8B.
* **Risk:** Low.

### F-021: Paragon Health Institute carries ASPE's $502-875 billion benefit to non-Medicaid payers and 3.5 percent price effect into the record as support for the rule. It attributes them, correctly, to the 2025 law's reforms.

* **Rule:** CMS-2452-P. **Effect on the article:** confirms. **Candidate use:** footnote.
* **Comments:** 2476-0130 Paragon Health Institute.
* **Excerpt:** "This translates into $502 billion to $875 billion in benefits for non-Medicaid consumers over the 2025-2034 period." (`CMS-2026-2476-0130`, Paragon Health Institute; CMS-2026-2476-0130_attachment_1.pdf, p. 2 of 12)
* **Figure:** ASPE figures as quoted: $502-875 billion benefit to non-Medicaid consumers, 2025-2034; non-Medicaid prices down up to 3.5 percent in provider-tax markets. Advocacy figure (Paragon): $61.5-123 billion less excess tax burden over a decade (0.25-0.5 x CMS's $246 billion).
* **Verification:** verification_log rows 3987-3988 (p. 2) and 3991-3992 (p. 12), all confirmed. ASPE's figures match the ledger's TP-12.
* **Distinct texts vs campaign copies:** 1 comment, 1 distinct text in both views; not in a campaign.
* **Article section:** Note sec. 3d (ledger TP-10, TP-12, TP-13, TP-14).
* **What it changes:** ASPE's statute-level estimate is entering the rule record on the supporting side, while the note treats ASPE as analysis of the statute (TP-13). It is a balancing example: the statute-versus-rule blur is not one-sided.
* **Risk:** Low: Paragon's attribution is accurate; the use of the figure is the point.

### F-022: The Idaho Hospital Association says Idaho's inpatient hospital assessment already sits above the phased-down threshold class by class, while outpatient is about 1 percent of net patient revenue. If so, the phase-down reaches Idaho, which the note's grouping places in Group E without the phase-down.

* **Rule:** CMS-2452-P. **Effect on the article:** contradicts. **Candidate use:** support.
* **Comments:** 2476-0095 Idaho Hospital Association.
* **Excerpt:** "…the outpatient assessment sits at approximately 1 percent of net patient revenue, while the inpatient assessment is above the phased-down threshold." (`CMS-2026-2476-0095`, Idaho Hospital Association; CMS-2026-2476-0095_attachment_1.pdf, p. 1 of 3 (OCR text; page image not re-read))
* **Figure:** Advocacy figures (IHA): outpatient assessment about 1 percent of net patient revenue; combined effective assessment projected below 2 percent once the phase-down is complete (assessed class by class), against a 3.5 percent threshold from FFY2032.
* **Verification:** verification_log row 3882 ('2 percent') confirmed, p. 1, from the page image; the quoted sentence is on the same page (OCR text).
* **Distinct texts vs campaign copies:** 1 comment, 1 distinct text in both views; not in a campaign.
* **Article section:** Note sec. 4 and Figure 6 (ledger SE-04, SE-09, SE-10, SE-21; decision log B-8).
* **What it changes:** SE-10 names four Group E expansion states the phase-down reaches (CO, CT, IN, VT) because KFF's indicator shows a hospital tax above 3.5 percent. Idaho is absent, presumably because its combined hospital rate is below 3.5 percent. The rule applies the threshold class by class, so a state-level indicator can miss states like Idaho, the same correction B-8 made for four other states.
* **Risk:** Medium: IHA's 'phased-down threshold' is not given as a number. KFF's indicator definition (file C2) is unavailable to the ledger, so the conflict is inferred, not shown.

### F-023: State hospital associations and others put their own dollar figures on several states that the note's grouping flags for data quality or leaves blank. These include Missouri and Minnesota (no estimable above-limit figure) and Florida, Texas, Tennessee and Mississippi (flagged Group D).

* **Rule:** both. **Effect on the article:** adds detail. **Candidate use:** hold.
* **Comments:** MO: 2476-0035 Missouri Hospital Association. MN: 2476-0150 Minnesota Medical Association (citing Minnesota DHS). FL: 1916-0417, 2476-0176 Florida Essential Healthcare Partnerships. TX: 1916-0415, 2476-0172 Texas Essential Healthcare Partnerships; 1916-0885 Texas Health Resources. TN: 1916-0399 Tennessee Hospital Association. MS: 1916-0650 Baptist Memorial Health Care; 2476-0165 University of Mississippi Medical Center.
* **Excerpt:** "Once the tax threshold reaches 3.5%, the ongoing annual impact to Missouri would be $1.25 billion." (`CMS-2026-2476-0035`, Missouri Hospital Association; CMS-2026-2476-0035_attachment_1.pdf, p. 3 of 3)
* **Figure:** Advocacy figures. MO: $1.25 billion a year once the threshold reaches 3.5 percent; $55.6 million per 0.1-point tax cut. MN: $1 billion a year (Minnesota DHS, as cited). FL: $4.4 billion DPP reduction when fully implemented; $272 million a year of tax capacity lost to the freeze (2024 data). TX: more than $4.3 billion a year once the phase-down is complete (attributed to the statute); $1.7 billion a year of tax capacity (2024 data); $915 million a year removed from CHIRP from SFY2029. TN: $320,411,458 a year. MS: at least $160 million a year; $150 million immediate cut to one academic medical center.
* **Verification:** verification_log: MO rows 3712, 3698, 3706 confirmed; FL rows 1303, 4050 confirmed; TX rows 1299 corrected (statute, not rule), 4044 and 3313 confirmed; TN row 1220 confirmed; MS rows 2032, 4040 confirmed. MN $1B located at p. 1 of 3 (not in the log).
* **Distinct texts vs campaign copies:** 12 comments, 12 distinct texts in both views; none is a campaign copy (1916-0415 heads a 2-letter campaign).
* **Article section:** Note sec. 4 and Figure 6 (ledger SE-12, SE-13, SE-14, SE-19, D-8, B-10).
* **What it changes:** This gives state-sourced magnitudes where the note shows blanks or flags. None is on KFF's measure (federal hospital SDP spending above the limits, FFY2025), so none can be placed in the group table or summed with it. Any use must keep the measure and the advocacy label.
* **Risk:** High if mixed with KFF's dollars: different measures (all-funds versus federal, tax capacity versus payments, statute versus rule), different years.

### F-024: Texas commenters tie the directed-payment approval dispute to Texas's local provider participation funds. CHAT says CMS is withholding approval of Texas SDP preprints over hold-harmless concerns, using a test CHAT says a federal court has enjoined. TEHP cites CMS's 'Round 1-4' questions on the SFY2027 CHIRP preprint.

* **Rule:** CMS-2452-P. **Effect on the article:** adds detail. **Candidate use:** support.
* **Comments:** 2476-0114 Children's Hospital Association of Texas (representative of a 4-letter campaign); 2476-0172 Texas Essential Healthcare Partnerships.
* **Excerpt:** "CMS is presently attempting to hinder Texas’s use of LPPFs via various indirect means, such as refusing to approve Texas’s SDP preprints…" (`CMS-2026-2476-0114`, Children's Hospital Association of Texas; CMS-2026-2476-0114_attachment_1.pdf, p. 14 of 14)
* **Figure:** n/a. Citations given by commenters: Texas v. Centers for Medicare & Medicaid Svcs., 805 F. Supp. 3d 734 (E.D. Tex. 2025); CMS Round 1-4 questions on the SFY2027 CHIRP preprint (June-September 2026), posted by Texas HHSC (the file's web address carries the date 9-9-2026).
* **Verification:** Located: CHAT p. 13 of 14 (case citation) and p. 14 of 14; TEHP p. 5 of 7 (footnote 12). Characterizations of CMS's conduct are the commenters' own; the court opinion and the Texas HHSC document were not read.
* **Distinct texts vs campaign copies:** 2 comments, 2 distinct texts in both views. CHAT (2476-0114) heads a 4-letter campaign, but the preprint and injunction passages are only in CHAT's own letter; the three template variants (2476-0048, -0051, -0061) do not contain them. TEHP (2476-0172) is not in a campaign.
* **Article section:** Note sec. 7, items 6 and 7 (ledger RM-25, RM-26, M-7, M-8).
* **What it changes:** The note treats the preprint lapse (item 6) and the Fifth Circuit appeal (item 7) as separate monitoring items and does not name the state. These comments put on record that the Texas preprint dispute turns on the same hold-harmless question as the litigation. They also supply the district court citation RM-26 lacks.
* **Risk:** Medium: advocacy accounts of CMS's motives. Both letters are dated September 21, 2026, after the September 18 reauthorization the ledger records (M-7), so 'presently' may refer to other preprints.

### F-025: The Texas Hospital Association says Texas has no statewide hospital tax: its hospital Medicaid payments are funded almost entirely by intergovernmental transfers and 35 local provider assessments, which the state says support about $12 billion in Medicaid payments a year.

* **Rule:** CMS-2452-P. **Effect on the article:** adds detail. **Candidate use:** footnote.
* **Comments:** 2476-0109 Texas Hospital Association.
* **Excerpt:** paraphrase only.
* **Figure:** Figure as cited by THA from the state of Texas: about $12 billion a year in total Medicaid payments supported by local hospital assessments (year not stated). Count: 35 local provider assessments.
* **Verification:** Located at p. 1 of 9 (no statewide assessment) and p. 2 of 9 ($12 billion, footnote 1). Paraphrased here (THA is quoted in F-007). Not in the verification log.
* **Distinct texts vs campaign copies:** 1 comment, 1 distinct text in both views; not in a campaign.
* **Article section:** Note sec. 4, Group D and Texas panel (ledger SE-11, SE-12, SE-21) and sec. 7 item 6 (M-7).
* **What it changes:** Texas, the largest Group D exposure ($3.5 billion above limits), finances through local assessments and IGTs, a split the grouping cannot show (SE-21). Group D's 'not assessed' tax indicators (SE-11) say nothing about these local taxes. The $12 billion should not be equated with the roughly $12 billion reauthorization in M-7 without a source linking them.
* **Risk:** Medium: a state figure relayed by an advocate, year unstated. Coincidence with M-7's amount invites a false link.

### F-026: Many CMS-2449-P commenters, including the Virginia Medicaid agency, argue that defaulting the payment limit to the State plan rate where no Medicare rate exists would freeze payments at the levels SDPs were meant to fix. That supports the note's reading that the default could be more restrictive, not just more uncertain.

* **Rule:** CMS-2449-P. **Effect on the article:** confirms. **Candidate use:** support.
* **Comments:** 1916-0755 Virginia Department of Medical Assistance Services; 1916-0209 Ohio Department of Medicaid; 1916-0807 WellPower; 1916-0404 Children's Hospital Association; 1916-0596 Cordell Memorial Hospital (Oklahoma critical access hospital).
* **Excerpt:** "CMS Should Not Default Payment Limits to State Plan Rates for Services Without a Medicare Equivalent…" (`CMS-2026-1916-0755`, Virginia Department of Medical Assistance Services (DMAS); CMS-2026-1916-0755_attachment_1.pdf, p. 3 of 5)
* **Figure:** Advocacy figures: children's hospitals' SDP payments down more than 40 percent by 2036 (CHA); Cordell Memorial's proportional exposure about $22,418 a year from the first rating period after January 1, 2028 (10 percent of its $224,181 SHOPP share for April 2024-June 2025).
* **Verification:** verification_log rows 1265 (CHA 40%, p. 1) and 1812 (Cordell $22,418, p. 2, page image read) confirmed. DMAS heading located at p. 3 of 5.
* **Distinct texts vs campaign copies:** Keyword count for the 'no Medicare rate' argument, docket CMS-2026-1916: about 140 comments (about 100 distinct texts) in both views. Approximate.
* **Article section:** Note sec. 5, rural paragraph (ledger AC-16, RM-18, AC-06).
* **What it changes:** AC-16's 'small or zero room, more restrictive' reading is conditional and rests on single-source rule mechanics. State Medicaid agencies make the same argument on the record, which strengthens it without making it a prediction.
* **Risk:** Low to medium: these are agencies' and providers' positions, not evidence of outcomes. Keyword counts are approximate.

### F-027: NRHA cites third-party figures on rural hospital finances: nearly half operating at negative margins and a median margin of about 1 percent (Chartis). That is the kind of evidence the note says its cited studies do not provide.

* **Rule:** CMS-2452-P. **Effect on the article:** new angle. **Candidate use:** hold.
* **Comments:** 2476-0093 National Rural Health Association.
* **Excerpt:** "Nearly 50 percent of rural hospitals are currently operating with negative margins, and the median operating margin for rural hospitals is approximately 1%." (`CMS-2026-2476-0093`, The National Rural Health Association; CMS-2026-2476-0093_attachment_1.pdf, p. 1 of 10)
* **Figure:** Third-party figures as cited by NRHA: about 50 percent of rural hospitals with negative margins; median rural operating margin about 1 percent (Chartis Center for Rural Health, 2025 State of the State); 432 hospitals at risk of closure.
* **Verification:** Located at p. 1 of 10. Chartis was not read; these are NRHA's citations. Not in the verification log.
* **Distinct texts vs campaign copies:** 1 comment, 1 distinct text in both views; not in a campaign.
* **Article section:** Note sec. 5 (ledger NC-12, C-12, D-4, AC-05 superseded).
* **What it changes:** The note deliberately declines to assess rural financial capacity (NC-12) and lists Chartis among sources not searched (C-12). This comment points to that literature but does not change the note's scoped claim.
* **Risk:** Medium: secondary citation by an advocacy group. Using it reopens a decision the note made on purpose (D-4).

### F-028: Many commenters in both dockets set out the legal arguments a challenge would use (Loper Bright, the APA, exceeding statutory authority), and one says CMS is already bound by an injunction on the hold-harmless test. No comment reports a filed suit against either rule.

* **Rule:** both. **Effect on the article:** adds detail. **Candidate use:** footnote.
* **Comments:** Examples: 1916-0407 Legal Action Center and 39 co-signers; 2476-0114 Children's Hospital Association of Texas (injunction).
* **Excerpt:** "…as CMS has exceeded its statutory authority and failed to act within the bounds of reasoned decision-making in extending SDP limits to all Medicaid…" (`CMS-2026-1916-0407`, Legal Action Center, and 39 other signatories; CMS-2026-1916-0407_attachment_1.pdf, p. 1 of 7)
* **Figure:** n/a.
* **Verification:** Legal Action Center located at p. 1 of 7. Keyword counts only; no comment was found reporting litigation filed against either proposed rule.
* **Distinct texts vs campaign copies:** Keyword counts citing Loper Bright: CMS-2449-P about 40 comments (about 20 distinct texts) in both views; CMS-2452-P about 11 comments (about 8 distinct texts) in both views. Approximate.
* **Article section:** Note sec. 7, item 11 (ledger NC-15, C-5, TP-28).
* **What it changes:** This adds texture to 'the formal opposition we located is in comment letters': the letters lay the legal groundwork, which bears on how quickly litigation could follow a final rule. It does not contradict NC-15.
* **Risk:** Low. Keyword counts are approximate, and commenters' legal claims are advocacy.

### F-029: The largest single bloc in the SDP docket is fire-based and public EMS agencies opposing Medicare-based limits on GEMT payments. This provider class is inside CMS's provider aggregate but outside the note's hospital-focused exposure analysis.

* **Rule:** CMS-2449-P. **Effect on the article:** new angle. **Candidate use:** hold.
* **Comments:** Examples: 1916-0162 Pasadena Fire Department; 1916-0425 fire-service campaign representative (39 letters); 1916-0396 Page, Wolfberg & Wirth.
* **Excerpt:** "…we estimate an annual funding shortfall of approximately $1 to $1.5M annually…" (`CMS-2026-1916-0162`, Pasadena Fire Department; CMS-2026-1916-0162, comment field)
* **Figure:** Advocacy figures: Pasadena Fire Department $1-1.5 million a year; per-transport shortfalls from RAND's analysis of CMS ambulance cost data (all-payer median -$1,362 for public-safety EMS, per PWW).
* **Verification:** verification_log rows 116 (Pasadena, confirmed) and 582 (PWW -$1,362, corrected: all-payer median, RAND/GADCS).
* **Distinct texts vs campaign copies:** Keyword count, docket CMS-2026-1916: about 240 comments (about 140 distinct texts) in both views; includes a 39-letter campaign. Approximate.
* **Article section:** Note sec. 2.4 caution 2 (provider aggregate; ledger CE-51) and sec. 4 (KFF's ambulance tax count, SE-04).
* **What it changes:** It shows who else sits in the 'provider aggregate' the note distinguishes from hospitals. It is outside the note's scope unless the author wants a non-hospital example.
* **Risk:** Low as context. Medium if per-transport advocacy figures are used.

### F-030: The Manhattan Institute flags that the proposed FFS limit's exception for IMDs and psychiatric residential treatment facilities depends on cross-references that do not name them, a drafting gap relevant to the note's point about IMDs and Medicaid adults.

* **Rule:** CMS-2449-P. **Effect on the article:** adds detail. **Candidate use:** hold.
* **Comments:** 1916-0659 Manhattan Institute (mental health policy team).
* **Excerpt:** "Yet proposed § 447.381(b)(2) makes its exception to payment limits depend on those cross-references." (`CMS-2026-1916-0659`, Manhattan Institute (mental health policy team); CMS-2026-1916-0659_attachment_1.pdf, p. 1 of 3)
* **Figure:** n/a.
* **Verification:** Located at p. 1 of 3. Rule text not re-read.
* **Distinct texts vs campaign copies:** 1 comment, 1 distinct text in both views; not in a campaign.
* **Article section:** Note sec. 5, psychiatric beds and IMD paragraph (ledger AC-14, AC-15).
* **What it changes:** AC-15 treats the IMD exclusion as long-standing and outside the rules. This comment shows the SDP rule's own FFS-limit exception touches IMDs, which could matter if the note expands the psychiatric point. It does not support AC-14's uncited claim that most freestanding psychiatric hospitals are IMDs.
* **Risk:** Low.
