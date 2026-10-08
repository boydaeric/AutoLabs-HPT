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
