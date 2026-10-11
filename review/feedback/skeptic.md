# Skeptical-reader review of the findings against v16

*Skeptical-reader reviewer's file, October 8, 2026. Follows `review/CONVENTIONS.md`. This file edits nothing else. Its ownership row in CONVENTIONS section 2 is for the editor to add.*

**Read, in order:** `review/CONVENTIONS.md`; `review/article_draft.md` (v16, without the review-notes block); `review/findings.csv` (F-001 to F-030); `review/verification_summary.md`; `review/required_corrections_v16.md`; `review/new_text_check.md`.

**Scope rules applied**

* The defects listed in `required_corrections_v16.md` and `new_text_check.md` are not reported again. v16 is judged as it will read once they are fixed. A fix is mentioned only where it changes how a finding can be used.
* Any finding, or part of one, marked unverifiable, not found or not checked (including "rule text not re-read" and claims that were only located in a comment and never checked against their source) is hold-level. No lead or support placement is recommended for it.
* F-015 is marked corrected, so its corrected fact is used: CBPP's footnote says the interaction and the dollar basis each *lower* CMS's figure, so adjusting for them would raise it, and only the window adjustment lowers it.
* This file does not endorse any citation proposed in `new_text_check.md`. None of them has been verified.
* This file contains no quotations. Every source is paraphrased, so no quote budget is used.
* Comment counts are given in both docket views. CMS-2452-P (docket CMS-2026-2476): 214 as filed / 213 corrected. CMS-2449-P (CMS-2026-1916): 960 as filed / 961 corrected. The only move is CMS-2026-2476-0199. Keyword counts are approximate.

**Readers**

* **CFO**: a hospital CFO. Thinks in nominal dollars, fiscal years and own-hospital cash. Checks every figure against "is this my money, and is it net?"
* **Director**: a state Medicaid director. Knows the financing mechanics, the preprints and the state budget, and reads "state savings" from the state's side.
* **HFMA**: an HFMA reader who knows HFMA's $56.6 billion piece and will defend it, and who expects gross versus net and outlays versus deficit to be kept apart.

**Challenge types:** campaign overweighting · advocacy figure read as neutral · mismatched units or periods · as-filed vs corrected counts · basis mismatch.

---

## Cross-cutting points that set how several findings can be used

1. **Every CBO limb is unverified in this cycle.** cbo.gov returned HTTP 403 and congress.gov was refused, so neither CBO nor CRS R48633 was read. That covers $191.1B, $149.4B, $340.5B, $182.7B, 1.1 million uninsured, the 50 percent replacement assumption and $34B. v16's own CMS–CBO comparison (sec. 5) rests on figures not re-read in this cycle. No finding can be used to shore it up, and any finding whose point depends on a CBO number is held for that part (F-004, F-005, F-006, F-008, F-015, F-016).
2. **The F-007 fix changes how the totals are read.** After the correction, sec. 3 will state the central estimate's 30 percent state offset and its 80 percent SDP ceiling. A Director will then ask at once whether $384.0B, $142.1B and the $241.9B overlap are already net of that 30 percent offset. The findings do not say, and the Federal Register order of computation was not checked. Until it is, no finding about offsets (F-007, F-008, F-015) can be set against the $488B–$753B range. Otherwise readers will either subtract the offset a second time or say THEIA left it out.
3. **The F-005 fix must stay scoped.** CMS's zero-enrollment statement is confirmed for CMS-2452-P only (91 FR 46590). No finding checks whether CMS-2449-P's RIA states an enrollment assumption. A corrected sentence that says "CMS's estimates assume no enrollment effect" for both rules goes beyond the evidence.
4. **The F-012 fix invites a tu quoque.** Once the same-page caveat is added (CMS cannot reliably attribute impacts by provider type, 91 FR 30462), sec. 4 still credits hospitals with most of the $163.7B relief because they pay $61.8B of 2026's $98.6B in provider taxes. That applies a one-year share to a ten-year figure, which is the same move F-012 records CHLA disclosing as "illustrative". If the piece uses F-012 to point out the limits of CHLA's allocation, a CFO will point out that the piece does the same thing.
5. **The quote budget for the Federal Register is spent.** v16 sec. 5 already quotes CMS-2452-P twice (the Table 12 title, and CMS's "shown in table 12" wording), and sec. 4 quotes CMS-2449-P at 91 FR 30453. Any CMS wording imported from the findings (F-005, F-007, F-011, F-012) has to be paraphrased with a Federal Register pin cite. It cannot be quoted, and it should not be quoted through a commenter.
6. **Commenter restatements are never the cite for a CMS fact.** Where a finding shows a commenter quoting CMS correctly, cite the Federal Register page. Where it shows a commenter quoting CMS wrongly (THA's scenario labels, CBPP's offset base, AHIP, BCBSA, NRHA's docket misprint), any use is as an example of misreading, and it carries the commenter's name.
7. **Docket counts are snapshots.** They were taken from the regulations.gov v4 API on October 7, 2026. Keyword searches over OCR text can miss figures printed as images, and letters published only on submitters' sites are not in the docket (F-001, F-002). Every negative claim drawn from the record ("no comment…") has to carry that scope.

---

## Findings

### F-001: CMS-2452-P record complete as posted

* **Challenges.** HFMA and the Director, on as-filed vs corrected counts: 214 as filed / 213 corrected, 188 / 187 distinct texts, and the position split 127 / 126 for requests for changes. A count that gives only one view will be challenged. Campaign overweighting: 36 comments sit in 10 campaigns (both views), so position shares should rest on distinct texts.
* **Verdict: safe to use, with a qualifier.** Give both views, distinct texts and the October 7, 2026 snapshot date. The positions are the analyst's coding, not commenters' self-labels.

### F-002: which September 21 letters are in the docket

* **Challenges.** The Director, on a name-matching gap: a letter filed under a person's name would be missed. Minor.
* **Verdict: safe to use, with a qualifier** (appendix or footnote level). Ten comments, ten distinct texts in both views. State the matching method. MACPAC and the two Illinois letters are still not located, so the negative stays scoped to the posted docket.

### F-003: 6,344 "posted" vs 960 posted

* **Challenges.** HFMA and the Director, on mismatched counters: received vs posted. Any line contrasting about 20 CMS-2452-P comments with 6,344 (ledger B-7) sets one counter against the other.
* **Verdict: hold** for 6,344 and any received count; the regulations.gov counter is unverifiable. Posted counts (960 as filed / 961 corrected; 214 / 213) are **safe with a qualifier**: label them posted, with the date.

### F-004: commenters' CBO $183B / $191.1B

* **Challenges.** HFMA, on outlays vs deficit (basis mismatch). The finding's diagnosis assumes the commenters' $183B is CBO's $182.7B net-deficit figure. That mapping is unverified (CBO not read). "Pre-enactment" could also be literally true if CBO scored an earlier version of the bill. Campaign overweighting: three of the $183B uses are one UHA text. Of 17 comments, 14 are distinct texts (both views).
* **Verdict: hold.** The point depends on CBO's two measures, which are unverifiable this cycle. The UHA and PA DHS passages were located but not logged.

### F-005: CMS assumes zero enrollment effect

* **Challenges.** The CFO: zero enrollment effect means CMS also models no rise in uninsured patients and uncompensated care, a cost a hospital will count. HFMA, on scope: the confirmed statement covers CMS-2452-P only (see point 3).
* **Verdict: split.** CMS limb (91 FR 46590): **use with a qualifier.** Cite the Federal Register, not Levitis or CBPP. Scope it to the provider tax rule. Paraphrase it (point 5). CBO's 1.1 million: **hold** (unverifiable).

### F-006: Section 71117 / CMS-2448-F interaction

* **Challenges.** The Director and HFMA, on mismatched periods and bases: CMS-2448-F's $78.2B federal / $46.9B state cover 2027–2036 in real 2027 dollars, against v16's 2026–2035 in 2026 dollars, so they cannot be added to or set beside $916.9B. Advocacy figure read as neutral: Iroquois's $1.5B shortfall for New York is an advocacy figure over two years. Its corrected cause is the February 2026 final rule, not CMS-2452-P. After the F-006 fix, a Director will ask whether CMS-2449-P's RIA also takes CMS-2448-F into account; nothing checks that.
* **Verdict: split.** CMS's statement that the interaction does not significantly change CMS-2452-P's estimates (91 FR 46590 fn 23; 46592): **use with a qualifier.** It applies to that rule only. CMS-2448-F figures: **use with a qualifier.** Different window and dollar year; never sum them. CBPP's CBO $34B: **hold** (unverifiable). Iroquois $1.5B: **hold** (advocacy figure, single state, different rule).

### F-007: central-scenario 30 percent offset and 80 percent ceiling

* **Challenges.** The Director, on basis: CMS applies the offset to the payment cuts that follow lost tax revenue (91 FR 46591), not to federal spending as CBPP describes it. Whether the published totals are already net of it is open (point 2). Advocacy source read as neutral: THA's letter, the commenter that gives the page, mislabels the 20 percent as the low scenario. Campaign overweighting: 12 quoting comments, 9 distinct texts (both views), including 3 UHA copies and a 2-letter campaign.
* **Verdict: use with a qualifier.** Cite 91 FR 46591–46594 directly, paraphrased. Say the three scenarios move the offset, the tax-financed share and the SDP ceiling together, so the direction of any one parameter's effect cannot be isolated. Do not cite THA for the parameter.

### F-008: THA says CBO assumed 50 percent replacement

* **Challenges.** HFMA and the Director, on an advocacy account of CBO's method read as neutral, with no CBO document cited. It is a behavioral assumption, not an enrollment one.
* **Verdict: hold** (unverifiable).

### F-009: 65 percent restated as a share of SDP spending

* **Challenges.** The CFO and HFMA, on mismatched units (arrangements vs dollars). CMS's own wording mixes them: 65 percent of "SDPs" against 55–75 percent of SDP spending. NRHA's application of the range to $774.8B is NRHA's own derivation. v16 sec. 2 says the 91 FR 30410 shares count arrangements, not dollars. Ledger CE-48 says CMS does not state which, and no finding checks 91 FR 30410. A HFMA reader will ask for the page.
* **Verdict: use with a qualifier** (footnote). Use it only to show that readers convert the parameter into dollars. Do not reproduce NRHA's dollar application. Keep the 65 percent in CMS's wording. Four comments, four distinct texts (both views).

### F-010: interaction-inclusive figures in comments

* **Challenges.** The Director, on basis: NRHA's $147.5B "to states" equals $198.7B in lost provider tax revenue minus THEIA's $51.2B state savings. It looks like a net state fiscal loss, the opposite sign from the "state savings" rows in v16's tables. HFMA, on scenario: SHSL's −$136.1B is the high scenario and is easy to read as central.
* **Verdict: split.** $90.9B federal (confirmed at 91 FR 46593 in F-015): **use with a qualifier.** Label it the increment after the SDP rule, central estimate. −$136.1B: **use with a qualifier.** Label it high-savings and including interaction. It matches the ledger but was not re-read in this cycle. $147.5B and the Table 19 accounting statement (91 FR 46596): **hold** (not checked). But see attack 2.

### F-011: CMS says both rules together are still a significant reduction

* **Challenges.** The CFO: the sentence is qualitative. It does not validate THEIA's $488B–$753B or any combined figure. Advocacy figure read as neutral: CHLA is a provider group arguing against the rule.
* **Verdict: use with a qualifier.** Attribute it to CMS at 91 FR 46593, paraphrased (point 5), not through CHLA. Do not present it as CMS endorsing the stacked total.

### F-012: hospital attribution and CHLA's $138B

* **Challenges.** The CFO, on mismatched periods: CHLA applies a one-year (2026) tax-revenue share, 63 percent, to a ten-year net provider line. The result is an advocacy figure, not a hospital estimate. After the required correction, the tu quoque in point 4 applies to sec. 4. The Director: CMS's own reason it cannot attribute by type (SDPs are optional for states, and effects on providers are indirect) cuts against any hospital share.
* **Verdict: split.** The CMS caveat: per the required correction. CHLA's $138B: **hold** as a hospital estimate. **Use with a qualifier** only as an example of a disclosed allocation: advocacy figure (CHLA Medical Group), about $13.8B a year, one-year share on a ten-year line. Use it that way only if sec. 4's own hospital-share sentence carries the same disclosure.

### F-013: $220.3B read as a payment cut

* **Challenges.** HFMA: the finding helps HFMA as much as THEIA. CMS's wording and four of the five comments that cite $220.3B treat it as a payment cut. That supports "an understandable reading", not "an error HFMA alone made". None of the five reproduces $56.6B. "Cut" may be loose wording for "net payments". Mismatched periods: NJHA's 2025–2035 is 11 years. Counts: 5 comments, 5 distinct texts (both views), out of 214 / 213.
* **Verdict: use with a qualifier.** Frame it as four of the five comments that cite the figure, in both views. Do not say "common in the record" or "widespread". The ACOG, PAR and NJHA passages were located but are not in the verification log. Pair it with v16's acknowledgment that CMS's wording invites the reading, not with the double-subtraction charge.

### F-014: one restatement of $681B

* **Challenges.** HFMA, on scope: a search of the posted dockets is not a search of the press, newsletters or consultancies. The single hit is an individual's.
* **Verdict: safe to use, with a qualifier.** One comment, one distinct text, in both views and both dockets (the other "681" hit is a telephone number). Snapshot of October 7, 2026, OCR text included. Do not use it to say how hospitals read the figure.

### F-015: CBPP says the CMS–CBO gap survives adjustment

* **Challenges.** The Director and HFMA, on basis: v16 sets real 2026 dollars over 2026–2035 against nominal FY2025–2034 dollars. The corrected fact cuts against v16's sec. 5 conclusion. Only the window adjustment lowers CMS's figure ($501.5B for 2026–2034). Removing the interaction raises it ($755.9B, or $630.9B without 2035), and converting to nominal dollars raises it too. Once the required correction is made, "does not show the rules exceed the OBBBA" rests only on unquantified axes: the comparison projection, enrollment (zero at CMS, unread at CBO) and behavioral assumptions (F-008, held). The CFO will also ask whether CMS's years are federal fiscal years or calendar years. No finding says. Advocacy figure read as neutral: CBPP opposes the rule, and its footnote is qualitative.
* **Verdict: split. Not lead.** The CMS-side arithmetic (91 FR 30451–30452, 46591, 46593): **use with a qualifier.** It is CMS's own federal figures by window, and the dollar effect is direction only. CBPP's argument: **use with a qualifier.** Attribute it to CBPP as its reasoning (2476-0033), opposing the rule, with no adjusted figures. Any statement of the gap against $340.5B, or its size: **hold** until CBO or CRS is read.

### F-016: $510B vs $149.4B dominates the SDP docket

* **Challenges.** HFMA and the CFO, on campaign overweighting and overreach. About 120 comments (about 90 distinct texts) of 960 as filed / 961 corrected cite $510B, and about 90 (about 60 distinct) cite $149.4B, so "most commenters" is not supported. The roughly 380 comments using "beyond the statute" language are a legal-wording count, not the numeric comparison. Advocacy figure: Lee County's $360.7B difference sets real 2026 dollars over 2026–2035 against nominal FY2025–2034 dollars. THA, MDA and PPC use $515B ($510.1B plus $5.34B; see U-1), a different scope.
* **Verdict: split.** The pattern, that many commenters set the two figures side by side: **use with a qualifier.** Approximate counts, distinct texts, both views, no "most". CBO's $149.4B as a fact: **hold** (unverifiable). Lee County's $360.7B: **hold** (advocacy figure, basis mismatch).

### F-017: AHIP and BCBSA misstate the interaction figures

* **Challenges.** The CFO: these are payer trade groups' errors, and quoting the errors of rule-adjacent groups can read as cherry-picking. AHIP's intended quantity is inferred from a terse footnote. The low and high federal values ($9.1B, $191.8B) come from the ledger and were not re-read in this cycle.
* **Verdict: use with a qualifier** (footnote). Say AHIP's meaning is inferred. Cite CMS's figures from the Federal Register, not from these letters. Two comments, two distinct texts (both views).

### F-018: net-of-tax arguments in the SDP docket

* **Challenges.** HFMA, on basis: these letters ask for a net-of-tax payment-limit test (Medicaid rate net of taxes against Medicare). That is a different quantity from the RIA's net provider aggregate that v16 builds. Campaign overweighting: 11 comments, 8 distinct texts (both views), several of them template variants.
* **Verdict: use with a qualifier.** Keep the payment-limit concept separate from THEIA's net provider arithmetic. Count distinct texts. Do not cite the letters as support for the $488B–$753B method.

### F-019: FAH's provider-tax point is on page 2

* **Challenges.** Same concept caveat as F-018. FAH's ask is about calculating the total payment rate.
* **Verdict: safe to use, with a qualifier.** Pin cite 1916-0676, p. 2 of 45. Describe the ask as about the payment rate.

### F-020: $264.4B vs $264.7B

* **Challenges.** HFMA, on CMS's internal inconsistency: the narrative says $264.4B and Table 20 sums to $264.7B (91 FR 30452). A reader holding the narrative figure will find the step 3 cap off by $0.3B. The same applies to the higher-savings $340.0B against CMS's $339.6B. F-020's flag says that is a narrative-to-table gap, not the rounding v16's source note calls it.
* **Verdict: safe to use, with a qualifier.** State that the cap is the table sum and that CMS's text prints a different figure. Three comments use $264.4B and one uses $264.7B (each in both views).

### F-021: Paragon carries ASPE into the record

* **Challenges.** The CFO, on basis: Paragon's $61.5B–$123B multiplies CMS's $245.8B (federal savings, provider tax rule alone) by 0.25–0.5 and calls the result excess tax burden. That is an advocacy figure on the wrong base. ASPE's $502B–$875B covers 2025–2034 for the statute, not the rules. A CFO will also note that ASPE's benefit to other payers is the commercial-price channel through which hospitals lose revenue. That channel sits outside v16's net figure, apart from CMS's $35.0B (see attack 5).
* **Verdict: split.** ASPE's figures as Paragon quotes them: **use with a qualifier.** Cite ASPE directly; they match ledger TP-12 but were not re-read in this cycle. Use it as the balancing example only. Paragon's $61.5B–$123B: **hold** (advocacy figure, basis mismatch).

### F-022: Idaho, class by class

* **Challenges.** The Director: the threshold applies per class (91 FR 46570), so a state-level KFF indicator can miss class-level exposure.
* **Verdict: hold** (unverifiable; no inpatient rate found). Keep it as an open question for Appendix H, not as a reassignment of Idaho.

### F-023: state-sourced dollar figures for flagged states

* **Challenges.** The Director, on mismatched units and bases: all-funds vs federal, tax capacity vs payments, statute vs rule (Texas's $4.3B is corrected to "statute"), annual vs one-time, and 2024 data vs FFY2025. Every figure is an advocacy figure.
* **Verdict: hold.** None is on KFF's measure, so none may enter the group table or be summed with it.

### F-024: Texas preprint dispute and court case

* **Challenges.** The Director: CMS's questions in the Texas HHSC document concern multi-jurisdictional districts and a combined inpatient/outpatient assessment base. The document does not cite the court case. So the finding's link between the preprint dispute and "the same hold-harmless question as the litigation" is not shown. "Withholding approval" is Texas's word, from its response on p. 18, not CMS's. Advocacy account read as neutral: CHAT describes CMS's motives.
* **Verdict: split.** The HHSC document (CMS conditions approval of the SFY2027 CHIRP preprint on two financing issues): **use with a qualifier.** Cite HHSC p. 17 of 19, not CHAT, and attribute "withholding" to Texas. The court ruling, the injunction and its scope: **hold** (unverifiable). This leaves v16 item 6's "set aside" unchecked against CHAT's "permanently enjoined".

### F-025: Texas finances hospital payments through IGTs and local assessments

* **Challenges.** The Director, on an advocacy relay of a state figure with no year. The $12B coincides with the roughly $12B reauthorization (ledger M-7) and invites a false link.
* **Verdict: hold.** Located in THA's letter only. The structural claim and the $12B were not checked against Texas law or HHSC.

### F-026: default to the State plan rate where no Medicare rate exists

* **Challenges.** The Director: agencies' and providers' positions show concern, not outcomes. Mismatched periods: CHA's "more than 40 percent by 2036" runs past CMS's window. The CFO, on units: Cordell's $22,418 "a year" is 10 percent of a 15-month SHOPP share (April 2024 – June 2025), and the phase-down is 10 *percentage points of Medicare* a year, not 10 percent of SDP receipts. Campaign overweighting: about 140 comments (about 100 distinct texts) in both views, approximate.
* **Verdict: split.** Positions, including Virginia DMAS and Ohio Medicaid: **use with a qualifier.** Approximate counts, distinct texts, framed as positions, consistent with v16's conditional reading. CHA's 40 percent and Cordell's $22,418: **hold** (advocacy figures, period and unit mismatch).

### F-027: Chartis rural margins via NRHA

* **Challenges.** The CFO: Chartis gives all-payer operating margins from HCRIS Q3 2024 data. It says nothing about the rules' effect, and NRHA's "nearly 50 percent" is 46 percent.
* **Verdict: use with a qualifier, only if the author reopens decision D-4.** Cite Chartis (February 10, 2025) directly at 46 percent and a 1.0 percent median. Draw no causal link. Otherwise leave it out. The evidence is verified, so placement is a scope call, not an evidence hold.

### F-028: legal groundwork in comments; no filed suit reported

* **Challenges.** The Director and the CFO: proposed rules are rarely challenged before they are final, so "no suit" carries little information. The comment record is not evidence of litigation status. Campaign overweighting: the Loper Bright counts are about 40 comments (about 20 distinct texts) in CMS-2449-P and about 11 (about 8) in CMS-2452-P, both views, approximate.
* **Verdict: split.** That letters set out the legal arguments: **use with a qualifier** (approximate counts, distinct texts). CHAT's injunction claim: **hold** (F-024).

### F-029: EMS/GEMT bloc in the SDP docket

* **Challenges.** HFMA, on campaign overweighting: about 240 comments (about 140 distinct texts), including a 39-letter campaign, so "largest single bloc" is not shown by keyword counts. Advocacy figures: Pasadena's $1M–$1.5M a year; PWW's −$1,362 is corrected to an all-payer median. The claim that GEMT payments sit inside CMS's $774.8B was not checked against the RIA.
* **Verdict: hold.** That CMS's aggregate covers non-hospital providers is already v16's [E] statement and needs no comment evidence.

### F-030: Manhattan Institute on the IMD/PRTF cross-references

* **Verdict: hold** (rule text not re-read).

### U-items (not in the reading list; noted for completeness)

U-3 and U-4 are covered by `required_corrections_v16.md`. U-2 bears on attack 4: commenters describe the September 30, 2028 date as intended, at the latest or at the earliest. U-1 bears on F-016.

---

## The five likeliest attacks if the piece uses this material

**1. "Your CMS–CBO comparison is unchecked, and the comment record argues against it."** (HFMA, Director; F-015, F-016, F-005, F-008, F-004)
Once corrected, sec. 5 concedes that the window is the only adjustment that lowers CMS's figure, and it still leaves $501.5B against $340.5B. The claim that the gap "does not show" the rules exceed the statute then rests on the comparison projection, enrollment and behavioral assumptions, and none of them is quantified. CBPP's reasoning and roughly 120 comments in the SDP docket are on the record against it.
*Missing evidence:* CBO's cost estimate or CRS R48633 read at the source (outlays and deficit for Secs. 71115 and 71116, the 1.1 million uninsured, any replacement assumption); whether CMS-2449-P states an enrollment assumption; whether CMS's 2026–2035 are fiscal or calendar years.

**2. "Your 'state savings' are a state loss."** (Director; F-010, F-007, F-006)
v16's tables show states saving $315.9B, but states fund their SDP share largely from provider taxes and IGTs and lose $198.7B in tax collections. NRHA's accounting-statement figure, a $147.5B net reduction to states, is that loss netted against THEIA's $51.2B. A Director will read the piece as having the state sign wrong. Once the 30 percent offset is stated, the Director will also ask whether the totals already include the general revenue that states put in.
*Missing evidence:* the CMS-2452-P accounting statement (Table 19, 91 FR 46596) read for its state, federal and provider lines; CMS's order of computation for the offset at 91 FR 46591–46592; whether CMS prints its own state figure that checks THEIA's $51.2B.

**3. "Your hospital framing outruns CMS, and you do what you fault CHLA for."** (CFO; F-012, F-029, F-021)
Once corrected, CMS says on the same page that it cannot attribute impacts by provider type. Sec. 4 still assigns most of the relief to hospitals using a one-year tax share, the same disclosed-assumption move as CHLA's $138B. EMS, managed care plans and nursing facilities sit inside the aggregate.
*Missing evidence:* any CMS or state data splitting SDP dollars or provider tax relief by provider type over the ten years; at minimum, a disclosed allocation assumption in sec. 4 to match the one the piece expects of others.

**4. "You called HFMA's figure an error when CMS's text and most citing commenters read it the same way."** (HFMA; F-013, F-020)
Four of the five comments that cite $220.3B (both views) call it a payment cut, and CMS's own cross-reference points to the wrong table. CMS's narrative and tables also disagree on the state figures ($264.4B vs $264.7B; $339.6B vs $340.0B). That invites the reply that the piece uses CMS's tables selectively while correcting others' readings of them.
*Missing evidence:* HFMA's reply (v16 still carries a [DATE SENT] placeholder); any CMS correction notice for the "shown in table 12" wording; a stated rule for when the piece uses CMS's table sums over CMS's narrative figures.

**5. "Your 'net' leaves out what a CFO actually loses."** (CFO, Director; F-021, F-006, F-005, F-007, F-022, F-023, F-025)
The net figure counts tax relief but not commercial price effects. ASPE's $502B–$875B benefit to other payers, 2025–2034, is the mirror of provider commercial revenue, against CMS's $35.0B. It also leaves out uncompensated care from coverage loss (CMS assumes none for CMS-2452-P), state general-revenue replacement and the Section 71117 rule. Figures are in real 2026 dollars, while hospitals budget in nominal dollars. At the state level, Directors in Idaho, Missouri, Minnesota and Texas will set their own class-level or all-funds numbers against the KFF-based groups.
*Missing evidence:* ASPE's report read directly (whether its $891B removes the overlap, and its link to commercial prices); a nominal-dollar or annual view of CMS's central series; Idaho's inpatient assessment rate as of July 4, 2025, and KFF's indicator definition; Texas HHSC's figures on local assessments and IGTs; the regulations.gov received counter, if any count beyond posted comments is to be used.

---

# Round 2

*Skeptical-reader reviewer, October 9, 2026. Appended to this file only. Read, in order: Round 1 above; `review/article_v2.md`; `review/article_changes.md`; `review/decision_log.md`; `review/verification_summary.md`, including "Citation check" and "Round 2 verification". The Round 2 notes in `review/findings.csv` were consulted where the summary points to them. Same rules as Round 1: unverifiable, not found, not checked and secondary material stays hold-level; no quotations; counts given in both docket views.*

**Size check.** v2's body (title through sec. 9) runs about 7,370 words, against about 5,700 for v16, so it is about 29 percent longer. The appendix notes add about 1,350 words. Part 5 counts against the body first.

## 1. Round 1 points, by status

### Cross-cutting points

| Round 1 point | Status | Where v2 handles it |
|---|---|---|
| 1. Every CBO figure unverified | **Resolved** (evidence), **open** (heading) | Round 2 read CBO's July 21, 2025 Table 7 and the October 28, 2025 estimate. Sec. 5, POLITICO ¶2 cites CBO directly and calls $340.5B THEIA's sum. The sec. 5 heading still credits CBO with $340.5B (part 4). |
| 2. Whether CMS's totals are net of the 30 percent offset | **Resolved** | Sec. 3 provider tax bullet: CMS's sequence [E], read as post-offset [I]. Also sec. 2 ¶4, sec. 4 ¶2, sec. 7 step 3 case 3 and the exec summary ¶4. Placing the 80 percent ceiling in sec. 3 exposes a new gap in sec. 7 (N-2). |
| 3. Scope the zero-enrollment statement to CMS-2452-P | **Resolved** | Sec. 5, POLITICO ¶2 and ¶4 both say "for the provider tax rule". |
| 4. Tu quoque on the hospital share | **Resolved** | Sec. 4, last ¶: the one-year share is disclosed as THEIA's assumption, and CHLA's $138B is cut. |
| 5. Quote budget | **Resolved** | The Table 12 title is v2's one CMS-2452-P quote. "Shown in table 12" is paraphrased in sec. 5 and App. E, and F-011 is paraphrased in sec. 4 ¶1. The 91 FR 30453 passage stays CMS-2449-P's one quote. |
| 6. Never cite a commenter for a CMS fact | **Resolved** | CMS facts are cited to the Federal Register throughout. Commenter readings sit in App. E and F, plus two body sentences about what commenters argued (see N-6). |
| 7. Docket counts are snapshots | **Resolved** | App. G limits sentence and App. I methods note. The two body sentences that carry counts (sec. 5 HFMA ¶2; sec. 8 rural ¶2) rely on App. I for the date, which is acceptable. |

### Findings, against Round 1 verdicts

| ID | Round 1 verdict | Status | Where in v2 |
|---|---|---|---|
| F-001 | Safe, with qualifier | Resolved | App. C note; App. I (both views, distinct texts, October 7 snapshot) |
| F-002 | Safe, with qualifier | Resolved | App. G (matching method stated) |
| F-003 | Hold the 6,344; posted counts safe | Partly resolved | App. I. See part 3. |
| F-004 | Hold | Resolved for placement | App. F note, with the $183B-to-$182.7B mapping tagged [I]. Acceptable at appendix level now that CBO has been read. Whether CBO printed a pre-enactment figure near $183B is unchecked, so the note must not call the commenters' labels wrong, and it does not. |
| F-005 | CMS limb with qualifier; CBO limb hold | Resolved | Sec. 5 POLITICO ¶2. See part 3. |
| F-006 | Split | Resolved | Sec. 1 ¶1, scoped to the provider tax rule's estimates. The CMS-2448-F figures are held, which is stricter than my Round 1 qualifier and acceptable. |
| F-007 | Use with qualifier | Resolved | Sec. 2 ¶4–5; sec. 3 bullet; sec. 4 ¶2; sec. 7 case 3. The cite is the Federal Register, not THA. |
| F-008 | Hold | Resolved (cut) | Not found in CBO. Removed. |
| F-009 | Footnote with qualifier | Partly resolved | App. D note is fine. v16's sec. 2 claim that the 91 FR 30410 shares count arrangements, not dollars, is kept as [E] and is on the writer's own re-check list. **Open.** |
| F-010 | $147.5B hold | Moved to confirmed | Sec. 3 new ¶; sec. 5 exhibit. See part 3 and N-3. |
| F-011 | Use with qualifier | Resolved | Sec. 4 ¶1, paraphrased, qualitative-only qualifier present. |
| F-012 | CMS caveat per correction; CHLA hold | Resolved | Exec ¶1; sec. 3; sec. 4 last ¶. CHLA cut. |
| F-013 | Use with qualifier | Partly resolved | Sec. 5 HFMA ¶2 uses "four of the five" in both views, as asked. Two problems remain: the framing sentence calling HFMA's reading "not unusual" is new, and the sentence is tagged [E] with no cited document (N-6). |
| F-014 | Safe, with qualifier | Resolved | App. G |
| F-015 | CMS arithmetic with qualifier; CBO gap hold | Moved | Sec. 5 POLITICO ¶4; App. F. See part 3. |
| F-016 | Pattern with qualifier; CBO and Lee County hold | Resolved | App. F (approximate counts, distinct texts, no "most"). Lee County held. |
| F-017 | Footnote with qualifier | Resolved | App. E ("appears to"; ledger scenario values not stated) |
| F-018 | Use with qualifier | Resolved | Sec. 5 ASPE ¶3 split; App. F counts |
| F-019 | Safe, with qualifier | Resolved | Sec. 5 ASPE ¶3 wording. The pin cite is deferred to the citation-to-add list. |
| F-020 | Safe, with qualifier | Resolved | Sec. 4 source notes; App. E (table-sum rule; "rounds" dropped) |
| F-021 | ASPE with qualifier; Paragon hold | Resolved | App. F, one sentence; Paragon held |
| F-022 | Hold | Resolved | Held; Group E unchanged |
| F-023 | Hold | Resolved | Held |
| F-024 | HHSC document with qualifier; court part hold | Partly resolved | App. I note is correct and makes no link to the court case. **Open:** sec. 9 item 6 still states the "set aside" ruling as [E] on a source that is only secondary. The new pointer from item 5 to App. I also places an unnamed, press-sourced lapse next to the Texas preprint (N-9). |
| F-025 | Hold | Resolved | Held |
| F-026 | Positions with qualifier; figures hold | Partly resolved | Sec. 8 rural ¶2: approximate counts and positions only. Two problems: Ohio is named but was never located (only Virginia DMAS's passage was), and the sentence is tagged [E] with no cited document (N-6). |
| F-027 | Scope call | Resolved | Held (decision D-4 not reopened) |
| F-028 | Use with qualifier; injunction hold | Resolved | App. I |
| F-029 | Hold | Resolved | Held |
| F-030 | Hold | Resolved | Held |

### The five attacks

| Attack | Status | Where v2 handles it, and what remains |
|---|---|---|
| 1. The CMS–CBO comparison is unchecked and contested | **Partly resolved** | CBO has been read, the verdict is gone and the reconciliation is in sec. 5 ¶4. Still open: whether the interaction adjustment is like-for-like, the direction of the coverage effect (N-4), fiscal versus calendar years (App. F) and the heading. |
| 2. "State savings" are a state loss | **Resolved, overcorrected** | Exhibit row "Net for states" and its source note handle it correctly. Sec. 3's new paragraph now goes too far the other way (N-3). |
| 3. The hospital framing outruns CMS | **Resolved** | Same-page caveat in each place; disclosed assumption; 87.5 percent given with its base. |
| 4. HFMA singled out | **Partly resolved** | Four-of-five framing and the App. E table-sum rule are in. HFMA's reply ([DATE SENT]) and any CMS correction notice are still missing. |
| 5. "Net" omits what a CFO loses | **Partly resolved** | 2026 dollars are stated up front, the scope paragraph is in sec. 7 and the zero-enrollment assumption is stated. There is still no nominal or annual view and no commercial-price or uncompensated-care figure. The reconstructed step 2 adds a new basis gap (N-1). |

## 2. New issues introduced by v2

Ranked most consequential first.

**N-1. Sec. 7, step 2, as reconstructed, does not use the national method's basis.** (CFO; basis mismatch)
* The new first sentence defines step 2 as the hospital's current tax bill minus its bill under each lower threshold. Step 1 is likewise measured against current SDP receipts. National step 2's $163.7 billion is measured against CMS's no-OBBBA projection and includes the freeze ($51.0 billion of the $198.7 billion). Freeze relief is avoided future increases, not a lower bill.
* Sec. 7 still says the hospital uses "the same three steps", and step 3 case 3 tells the hospital to compare its result "with the national range". As written, the hospital result is on a current-payments basis and the national range is on a no-OBBBA basis, so they are not comparable without saying so.
* "Its tax bill at each step of the lower threshold, from 5.5 percent of net patient revenue" treats the threshold, a cap on a class's tax revenue as a share of that class's net patient revenue, as the hospital's own rate. That holds only for a uniform tax levied on net patient revenue. It does not hold for per-day or per-bed taxes, or for states whose July 4, 2025 level sits below a given step (step 2 is then zero for that year). The sentence is tagged [I], but the assumption needs to be stated.
* "By state and tax class" is now attached to 91 FR 46574. The Citation check confirms that page for the intended date only. The per-class point rests on 91 FR 46570, which is on the writer's own citation-to-add list. The same applies to sec. 9 item 8.
* No v16 text, finding or verified source supports the current-bill definition. It is the writer's reconstruction.

**N-2. Placing F-007 exposes that sec. 7, step 1 misses part of the cut.** (CFO, Director)
Sec. 3 now says CMS applies at most 80 percent of the provider tax rule's cut to SDPs. So at least 20 percent falls on other Medicaid payments, and the SDP share can reduce SDPs that are below the cap because their funding is gone. Hospital step 1 counts only the SDP amount above the cap. A CFO checking the hospital method against sec. 4's step 1 ($142.1 billion from the provider tax rule) will find no hospital counterpart for funding-driven cuts. The gap was present in v16, but v2 now prints the parameter that reveals it. The constraint: sec. 7 must say that step 1 covers the cap only, and that cuts the state makes because tax revenue falls are a separate exposure.

**N-3. Sec. 3's new state paragraph overcorrects.** (Director; basis mismatch)
"For states, that lost tax revenue outweighs the lower spending" is true for the provider tax rule ($51.2B or $138.2B against $198.7B), but the sentence is not scoped to that rule. The paragraph then says the whole state column is "not a state saving", including the SDP rule's $264.7 billion. That contradicts the piece's own step 3: the $264.7 billion is a state saving unless the state passes it back to providers by collecting less tax or fewer IGTs, which is exactly the unknown the exhibit's "Not estimated here" note names. On v2's own figures, before any change in SDP-funding taxes or IGTs, the combined state position is $264.7B + $51.2B − $198.7B = about +$117.2B [I, this reviewer's arithmetic], a net state gain. A Director will run that sum. The constraint: scope every net-loss statement to the provider tax rule, and describe the SDP column as before any change in the taxes and IGTs that fund it, without calling it "not a saving". The exhibit and its source note already do this correctly. The POLITICO ¶3 clause ("leave states a net loss under that rule") is correctly scoped.

**N-4. Sec. 5 POLITICO ¶4 claims more than the reconciliation shows.** (HFMA, Director). Detail is in part 3, F-015.
* "Of the differences between them, only the extra year lowers CMS's figure" covers all the differences, including the comparison projection, whose direction is unknown. It is supported only for the three adjustments computed (window, interaction, dollar basis).
* The no-interaction figure ($755.9B) is presented as one of "the differences between them". It is a comparability adjustment only if CBO's section-by-section outlays exclude the interaction. Whether CBO's Table 7 rows are stacked was not checked. If they are stacked, the with-interaction $601.0 billion is already the like-for-like figure.
* The coverage effect is listed as an unresolved cause, but its direction is knowable. CBO's $191.1 billion includes outlay savings from 2.4 million fewer Medicaid enrollees (CBO p. 4), so removing it would lower CBO's figure and widen the gap. This is direction only [I], since CBO does not split the $191.1 billion. Leaving the direction out invites the charge that v2 lists a factor that cannot help close the gap as if it could.

**N-5. The exec summary promotes an unchecked [E].** The new ¶1 sentence says CMS measures *both* rules against a projection without the OBBBA, tagged [E]. Ledger CE-43 verified that for the provider tax rule only, and the writer's own re-check list (`article_changes.md`, last paragraph) names this exact citation. v16 carried it in sec. 3. v2 moves it into the headline paragraph, where a challenge does the most damage. The constraint: it stays out of the summary as [E] for the SDP rule until 91 FR 30400 et seq. is read for the baseline.

**N-6. Two body sentences are tagged [E] with no cited document.**
* Sec. 5 HFMA ¶2: four of the five comments, including a state Medicaid agency and a state hospital association.
* Sec. 8 rural ¶2: Virginia, Ohio and many providers.

The legend defines [E] as stated in a cited public document. The writer deferred every comment ID to the citation-to-add list. But under the writer's own evidence rule, "located" verifies what a commenter wrote, and these sentences claim only what commenters wrote. Citing the docket comment IDs is therefore consistent with the evidence rule. Leaving them out makes the [E] unsourced. Separately, **Ohio (1916-0209) was never located.** F-026's verification covers the Virginia DMAS heading (p. 3 of 5) and two advocacy figures only. Naming Ohio is a not-checked claim and should not appear until it is located.

**N-7. App. I tags a reading as [E].** "They cover each docket as filed and do not say what they count" is tagged [E]. The second half is fine. The first half is the analyst's reasoning in F-003's Round 2 note (the Federal Register count has no corrected view), not something either source states, so it is [I]. Conventions section 3 requires both views. Saying explicitly that no corrected view exists for the Federal Register counts meets that rule better than implying one.

**N-8. Two different "Table 19"s are both cited.** Sec. 3 cites Table 19 at 91 FR 46596 (the provider tax rule's accounting statement). Sec. 5 ¶4 cites Table 19 at 91 FR 30452 (the SDP rule's annual federal figures). Both cites are correct, but a reader checking one will land on the other. Appendix E, which collects citation traps, should list this.

**N-9. The sec. 9 item 5 pointer to App. I implies a link that is not established.** Item 5's lapse comes from two press articles that were not re-read (ledger RM-25). App. I's note is about CMS's Round 4 questions on Texas's SFY2027 CHIRP preprint. The pointer invites readers to treat the lapse and the preprint questions as the same dispute, and nothing verified connects them. The constraint: either drop the pointer or have App. I say the two are separate items.

**Citations new in v2 that the Citation check does not confirm.** Every new citation in v2 matches a confirmed row in the Citation check, the verification summary or a Round 2 finding note, with three exceptions:
* 91 FR 46574 is cited for "by state and tax class" (sec. 7 step 2; sec. 9 item 8) but confirmed for the date only (N-1).
* The exec summary ¶1 baseline [E] for the SDP rule (N-5).
* The Section 71117 description in sec. 1 ¶1 ("requirements for waivers of the rule that provider taxes be uniform") carries no cite of its own. Its substance matches CMS-2448-F, which was read, so this is low risk, but it needs a pinpoint.

Two items checked and found clean, so not flagged: "none from Section 71116" (CBO p. 5, in F-005's Round 2 note) and the $332.1 billion deficit-basis sum (CBO's Table 7 has no Section 71116 revenue row; F-015's Round 2 note).

## 3. Findings moved to confirmed or corrected

### F-003: Federal Register counts (moved from unverifiable to confirmed for the counts)

* **Challenges.** HFMA and the Director, on mismatched counters. The Federal Register shows 6,344 against 960 posted as filed / 961 corrected, and 245 against 214 / 213. What the Federal Register counts is still unverifiable. 245 exceeding the 214 later posted fits a received-type counter but does not prove one. The two refresh dates differ (September 4 and September 24, 2026), so the two counts are not even as of the same date. As-filed vs corrected: the Federal Register counts have no corrected view.
* **Verdict: safe to use, with a qualifier.** Give the source (Federal Register document record), the refresh date and the fact that its definition is not stated. Do not call it received or posted. Never set it beside posted counts or against the other docket; v2's App. I already does neither. Say outright that no corrected view exists, and change "cover each docket as filed" to [I] (N-7). The definition stays **hold**.

### F-005, CBO limb: coverage effects (moved from unverifiable to confirmed)

* **Challenges.** The CFO: CBO's 1.1 million more uninsured in 2034 is a statute-level effect from Section 71115, while CMS's zero is a rule-level assumption for CMS-2452-P. They are different objects, and CMS-2449-P's enrollment assumption is still unread. HFMA, on direction: see N-4. Coverage savings sit inside CBO's $191.1 billion, so the coverage difference widens the CMS–CBO gap and cannot explain it away. The 2.4 million fewer Medicaid enrollees (p. 4) is the figure that drives outlays; the 1.1 million uninsured is a net-coverage figure.
* **Verdict: use with a qualifier**, as v2 does in sec. 5 ¶2. Keep CMS's zero scoped to the provider tax rule. If coverage is listed among the unresolved differences, give its direction. Do not quote CBO; the CBO quote slot is unused, but paraphrase is enough.

### F-006, CBO limb: Section 71117 (moved from unverifiable to confirmed)

* **Challenges.** HFMA, on outlays vs deficit: CBO's cells give $34.6 billion in outlays and $0.6 billion in revenue. CBPP's $34 billion is the unprinted deficit net. Any use alongside sec. 5's outlay figures must use $34.6 billion. Scope: the October 2025 CBO estimate does not discuss Section 71117, so only the July table supports it.
* **Verdict: confirmed, but hold for placement**, as v2 does. It is outside the note's two-section scope, and putting it beside $340.5 billion would invite a three-section sum the note never makes. If it is ever used: outlays basis, $34.6 billion, FY2025–2034, nominal, CBO's July 21, 2025 Table 7.

### F-010: CMS's net state figures (moved from not checked to confirmed)

* **Challenges.** The Director, on scope and sign: −$147.5 billion (Table 19, 91 FR 46596) and −$60.5 billion (Table 12, 91 FR 46592) are the provider tax rule's net for states, after and before the interaction. Both are confirmed and correctly placed in the exhibit. The challenge is to what v2 builds on them in sec. 3 (N-3): extending "not a saving" to the SDP rule's $264.7 billion contradicts step 3. On v2's own numbers, the combined state position before any change in SDP-funding taxes is a gain of about $117 billion. The accounting statement's annualized 7 and 3 percent figures are not used, which is correct, since they would add a third basis. The high-savings −$136.1 billion (46594) is correctly labeled in App. E.
* **Verdict: use with a qualifier.** Keep both CMS net figures as the provider tax rule's state effect, scoped to that rule in every sentence. The reconciliation ($51.2B or $138.2B less $198.7B) stays [I]. No net state figure for the SDP rule or for both rules, consistent with the exhibit. Revise sec. 3's closing sentence per N-3.

### F-015: CMS against CBO, as placed in sec. 5 (corrected; CBO components moved to confirmed)

* **Challenges.**
  * HFMA, on attribution: the heading still credits CBO with $340.5 billion, which the body's second paragraph says CBO does not print (part 4).
  * The Director and HFMA, on basis: N-4's three points. "Only the extra year lowers" is supported for the three computed adjustments, not for every difference. The no-interaction $755.9 billion is a like-for-like adjustment only if CBO's section rows are unstacked, which is unchecked. The coverage effect widens the gap, and v2 lists it without a direction.
  * The CFO: whether CMS's 2026–2035 are fiscal or calendar years is still open, and the body states CBO's years as fiscal and CMS's without a label.
  * Placement: support, not lead, is right. CBPP's reasoning is correctly confined to App. F and attributed as an opposing organization's reasoning with no adjusted figures.
  * The corrected fact is used correctly: the interaction and the dollar basis raise CMS's figure, and only the window lowers it.
* **Verdict: use with a qualifier, as support.** Restrict "only the extra year lowers CMS's figure" to the three adjustments the tables allow. Present the no-interaction figure as conditional on how CBO stacks its section estimates, or leave it in App. F. Give the coverage effect's direction or drop it from the list of unresolved causes. Keep "unresolved" and the no-verdict sentence. The CMS-side figures ($601.0B, $501.5B, $755.9B, $630.9B) and CBO's components are now all confirmed, so nothing in the paragraph is hold-level once these wording limits are applied.

## 4. The five decisions that need input

1. **F-015, support not lead: agree.** The reconciliation is now fully sourced, but lead placement would turn the note into a verdict on statutory authority that the evidence still cannot deliver (N-4). **Heading: no, it should not attribute $340.5 billion to CBO.** It would be the only place the note repeats the attribution error that the F-015 correction removed, and it contradicts the body's own second paragraph. A heading that names CBO's estimates without the sum, or names no figure for CBO, meets the constraint.
2. **F-011 lead, paraphrased, keeping the Table 12 title as the one CMS-2452-P quote: agree.** The title is documentary evidence for a contested reading and loses force in paraphrase, while CMS's significant-reduction sentence does not.
3. **Hospital share kept with the assumption disclosed: agree.** It now carries two stated assumptions: the 2026 share holds for ten years, and relief follows taxes paid. That is the disclosure Round 1 asked for, and cutting CHLA removes the tu quoque.
4. **Keep existing v16 citations and apply the confirmation rule to new ones: agree, with one exception.** A v16 citation already on the writer's re-check list should not be promoted into a more prominent place before it is checked, and the exec summary's both-rules baseline [E] does exactly that (N-5).
5. **Footnote-level material as notes under the existing appendix bullets: agree.** Some of those notes repeat body text verbatim, though (part 5, cut 5).

## 5. Cuts that lose no correction, required qualifier or verified fact

Word counts are approximate. Every cut removes a repeat or folds it into a pointer.

1. **The 30 percent offset is stated five times in the body; keep two** (about 90 words). Keep the full statement in the sec. 3 provider tax bullet (the evidence and the [I] reading) and the sec. 7 step 3 case 3 qualifier (the operational warning). Cut the exec ¶4 last sentence and the clause in sec. 2 ¶4 ("which assumes states make up 30 percent …"). Reduce sec. 4 ¶2's two offset sentences to a pointer to sec. 3 and sec. 7. Every location keeps the qualifier by reference.
2. **CMS's 91 FR 30462 attribution caveat is stated in full three times; keep it in full once** (about 35 words). Keep the full version, with CMS's reason, in sec. 3. Keep the exec ¶1 clause as is, since the required correction applies there. In sec. 4's last ¶, replace the restated sentence with a back-reference to sec. 3 and keep the disclosed one-year-share sentence intact.
3. **The state net is stated in sec. 3, in the exhibit row and its source note, and in POLITICO ¶3; keep the exhibit and one sentence** (about 60 words). The exhibit row and source note carry the figures, sources and the "Not estimated here" reasoning. Trim sec. 3's new paragraph to CMS's two net figures with cites and the [I] reconciliation, which also removes the N-3 overreach. In POLITICO ¶3, cut the clause adding the $198.7 billion and the state net loss; the pointer to sec. 3 remains.
4. **Sec. 5 POLITICO ¶4 says "reconciliation, cause unresolved" twice** (about 45 words). The opening sentence and the closing "This is a reconciliation of published estimates; THEIA Services does not attribute …" say the same thing. Keep one. The coverage clause in the unresolved list repeats ¶2's sentence; a pointer to ¶2 is enough once the direction (N-4) is added there.
5. **Appendix notes that restate body text** (about 170 words, appendix). Cut these, since each says what the body already says with the same cites:
   * App. D parameters note: the same three central values and both scenarios as the sec. 3 bullet. Move its one new fact, that CMS prints no pre-offset total, into the bullet's [E] sentence.
   * App. E Table 12 cross-reference note: the same as sec. 5 HFMA ¶2.
   * The figures in App. F's reconciliation note: the same as sec. 5 ¶4. Keep its dollar-basis line and the open fiscal-versus-calendar item.
   * The closing sentence of App. F's payment-limit note: the same as sec. 5 ASPE ¶3.
