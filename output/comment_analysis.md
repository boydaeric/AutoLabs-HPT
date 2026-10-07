# Public comments on CMS-2449-P and CMS-2452-P: analysis

## Methods note

This is the report's only methods note; the sections below do not repeat it.

**Sources.** 1,174 public comments collected from regulations.gov (API v4): 960 filed on CMS-2449-P (docket CMS-2026-1916) and 214 filed on CMS-2452-P (docket CMS-2026-2476). Text comes from each comment body and every attachment, with OCR for scanned pages. Tags are in `output/comments_tagged.csv`; every dollar figure and impact estimate is in `output/evidence_ledger_delta.csv`.

**Reading conventions.**

* Plain text is my paraphrase of what commenters argued; it is not their wording.
* **Verbatim** lines are exact quotes, each under 25 words, taken from the merged comment text in `data/<docket>/_text/`. They keep source typos and OCR errors, and `…` marks where a quote was cut mid-sentence. Every quote carries its comment ID.
* **[inferred]** marks anything I did not read directly in a comment: classifications, totals I computed, keyword-based counts, or a judgment about what a figure means.
* Comment IDs drop the `CMS-2026-` prefix in the body text (`1916-0128` = `CMS-2026-1916-0128`).

**Docket totals, two ways.** Every docket total is given as filed on regulations.gov and corrected after moving the one letter filed in the wrong docket, `2476-0199`. That letter is the California Behavioral Health Association's comment on CMS-2449-P. Its text is identical to `1916-0958`, which the association filed in the CMS-2449-P docket on 28 July; the copy in the CMS-2452-P docket was posted on 22 September. Moved to CMS-2449-P, it adds one comment but no new distinct text: it becomes an exact duplicate in the 12-letter campaign headed by `1916-0958`.

| | CMS-2449-P as filed | CMS-2449-P corrected | CMS-2452-P as filed | CMS-2452-P corrected |
|---|---:|---:|---:|---:|
| Comments | 960 | 961 | 214 | 213 |
| Distinct texts (campaign copies counted once) | 660 | 660 | 188 | 187 |
| Comments inside campaigns | 361 | 362 | 36 | 36 |
| Evidence-ledger rows | 3,636 | 3,637 | 568 | 567 |
| Comments with a ledger row | 473 | 474 | 114 | 113 |

Both rules combined: 1,174 comments either way; 848 distinct texts as filed, 847 corrected. The same two views are in `output/docket_totals.csv` for every output file. The `docket` column in each row-level file is always as filed, and a `docket_corrected` column gives the corrected docket; `docket_corrections.csv` is the source for the move. The position-by-type tables below are shown both ways.

**Misfiled-letter check.** I scanned every comment's full text for the rule number it cites, for content terms from each rule (directed payments and Medicare limits vs. provider taxes and hold harmless), and for near-duplicate text across the two dockets, then read the borderline cases. `2476-0199` is the only letter filed under the wrong one of the two rules. Letters that mention the other rule are on their own rule: the Idaho and Iowa hospital associations (`2476-0095`, `2476-0076`) and AMGA (`2476-0131`) cite CMS-2449-P only as a cross-reference, and Sutter Health's page footers read "Docket No. CMS-2449-P" (`2476-0123`) although its subject line and argument are CMS-2452-P. Six comments address neither rule, so they cannot be moved. Three are coaching-code letters in the CMS-2449-P docket (`1916-0851`, `1916-0937`, `1916-0941`). Three are individual comments about Medicaid work requirements (`1916-0031` in CMS-2449-P; `2476-0002` and `2476-0017` in CMS-2452-P). All six stay in their filed docket in both views and carry a `filing_note` in `comments_tagged.csv`. They are classified as commenter type "off-topic" and position "unclear / off-topic", so they appear in that row and column of every table and in `output/docket_totals.csv`, and they remain in the comment totals. Many short comments (for example "Cuts to Medicaid will cost lives") do not say which rule they address, so they stay where filed **[inferred]**.

**Off-topic reclassification, before and after.** Reclassifying the six moved two comments in CMS-2452-P out of "oppose" (`2476-0002`, `2476-0017`) and left the four in CMS-2449-P in the same position, because they were already tagged unclear / off-topic. Positions, as filed on regulations.gov:

| Position | CMS-2449-P before | CMS-2449-P after | CMS-2452-P before | CMS-2452-P after |
|---|---:|---:|---:|---:|
| Oppose | 351 | 351 | 75 | 73 |
| Request for changes | 461 | 461 | 127 | 127 |
| Mixed | 121 | 121 | 8 | 8 |
| Support | 14 | 14 | 4 | 4 |
| Unclear / off-topic | 13 | 13 | 0 | 2 |
| **Total** | **960** | **960** | **214** | **214** |

The corrected view differs from as filed only by `2476-0199` (one request-for-changes comment), so its before-and-after change is the same. Commenter types changed in both dockets. CMS-2449-P: association 176 to 174, individual 197 to 196, other 249 to 248, off-topic 0 to 4. CMS-2452-P: individual 33 to 31, off-topic 0 to 2. All other type counts are unchanged.

**What is exact and what is approximate.**

* *Exact counts* come straight from the CSVs: comments by docket, commenter type and position, and campaign sizes. Positions were assigned by a person reading the opening, closing and key-ask excerpts of each distinct text, not full reads of long letters, and campaign copies inherit their representative's position. Commenter type and state are rule-based with manual corrections. Campaigns are groups of letters with similar text (word 5-gram Jaccard similarity, within one docket) **[inferred]**.
* *Approximate counts* are every "about N" count of comments or distinct texts that raise a theme or cite a figure. They come from keyword matching over the full text (`count_themes.py`), are rounded to the nearest 10, and can over-count passing mentions or miss different wording **[inferred]**. They show scale, not tallies. Moving `2476-0199` changes none of them at this rounding.
* *Figures.* The ledger's 4,204 rows were extracted mechanically. Every figure cited in this report was checked against its source file for number, unit, time period and attribution, as were the 64 rows found only in OCR output or not re-located (`output/verification_log.csv`: 162 rows, 144 confirmed, 18 corrected; none unverifiable). `build_evidence_ledger.py` applies the corrections from `ledger_corrections.csv`, so a rebuild keeps them. In the ledger, `file_basis` shows whether an excerpt was re-found in the original text layer (4,141 rows) or in OCR output (60 rows, each page image read visually); three docx-table rows were read directly. The `figure_source_inferred` column (own figure, cites CMS or CBO, example, table) is rule-based and **[inferred]**. Ledger rows outside the verification log were not read individually.

---

# CMS-2449-P — State directed payments and FFS targeted practitioner payments (docket CMS-2026-1916)

## Counts by commenter type and position

**All comments, as filed (n = 960)**

| Commenter type | Oppose | Request for changes | Mixed | Support | Unclear / off-topic | Total |
|---|---:|---:|---:|---:|---:|---:|
| Hospital / health system | 41 | 138 | 94 | 0 | 0 | 273 |
| Other | 128 | 107 | 10 | 3 | 0 | 248 |
| Individual | 90 | 94 | 0 | 5 | 7 | 196 |
| Association | 63 | 94 | 15 | 0 | 2 | 174 |
| Advocacy group | 23 | 9 | 0 | 6 | 0 | 38 |
| State agency | 6 | 19 | 2 | 0 | 0 | 27 |
| Off-topic (addresses neither rule) | 0 | 0 | 0 | 0 | 4 | 4 |
| **Total** | **351** | **461** | **121** | **14** | **13** | **960** |

**All comments, corrected (n = 961).** The moved letter is an association asking for changes, so only the Association row (174 to 175) and the request-for-changes column (461 to 462) change.

| Commenter type | Oppose | Request for changes | Mixed | Support | Unclear / off-topic | Total |
|---|---:|---:|---:|---:|---:|---:|
| Hospital / health system | 41 | 138 | 94 | 0 | 0 | 273 |
| Other | 128 | 107 | 10 | 3 | 0 | 248 |
| Individual | 90 | 94 | 0 | 5 | 7 | 196 |
| Association | 63 | 95 | 15 | 0 | 2 | 175 |
| Advocacy group | 23 | 9 | 0 | 6 | 0 | 38 |
| State agency | 6 | 19 | 2 | 0 | 0 | 27 |
| Off-topic (addresses neither rule) | 0 | 0 | 0 | 0 | 4 | 4 |
| **Total** | **351** | **462** | **121** | **14** | **13** | **961** |

**Distinct texts, as filed (n = 660)**

| Commenter type | Oppose | Request for changes | Mixed | Support | Unclear / off-topic | Total |
|---|---:|---:|---:|---:|---:|---:|
| Other | 89 | 74 | 2 | 3 | 0 | 168 |
| Association | 56 | 80 | 10 | 0 | 2 | 148 |
| Hospital / health system | 31 | 103 | 8 | 0 | 0 | 142 |
| Individual | 83 | 40 | 0 | 5 | 7 | 135 |
| Advocacy group | 22 | 8 | 0 | 6 | 0 | 36 |
| State agency | 6 | 19 | 2 | 0 | 0 | 27 |
| Off-topic (addresses neither rule) | 0 | 0 | 0 | 0 | 4 | 4 |
| **Total** | **287** | **324** | **22** | **14** | **13** | **660** |

**Distinct texts, corrected (n = 660).** Unchanged: the moved letter is an exact copy of `1916-0958`, which is already counted.

The 94 "mixed" hospital comments are almost all one campaign: 90 letters from Tennessee-area hospitals (representative `1916-0909`, Parkwest Medical Center). They support keeping separate payment terms through the grandfathering period but oppose other provisions. Collapsing campaigns shrinks "mixed" from 121 to 22.

**Campaigns:** 61 campaigns cover 361 comments as filed (362 corrected, because `2476-0199` joins the `1916-0958` campaign). By role, as filed: 9 exact duplicates, 76 near-identical form letters and 215 template variants with organization-specific content (10 exact duplicates corrected) **[inferred: Jaccard similarity of word 5-grams]**. The largest:

* 90 Tennessee-area hospital letters (`1916-0909`)
* 39 fire-service letters asking for an EMS exemption (`1916-0425`)
* Two 12-letter ambulance-district and fire-district templates (`1916-0132`, `1916-0206`)
* 11 chronic-illness patient letters (`1916-0174`)
* 11 behavioral health provider letters as filed (`1916-0958`); 12 corrected

## Top recurring arguments

Counts below are "about N" keyword-match counts of distinct texts (see the methods note) **[inferred]**.

### 1. The rule goes beyond what Congress enacted (about 230 distinct texts)
Section 71116 of P.L. 119-21 capped SDPs only for four service types: inpatient hospital, outpatient hospital, nursing facility, and practitioner services at academic medical centers. Commenters argued that CMS extends Medicare-based limits to all other SDP services and adds a new FFS targeted-payment limit (§447.381) that Congress never directed. Many call the extensions legally vulnerable and ask CMS to implement only the statute.
* Temple University Health System (`1916-0121`). **Verbatim:** “…the proposed rule extends beyond both the statute’s text and congressional intent.”
* Illinois Academy of Family Physicians (`1916-0122`). **Verbatim:** “Rather than limiting implementation to the four service categories identified by Congress, the proposed rule would extend Medicare-based payment limits to virtually all non-grandfathered…”
* Legal Action Center and 39 co-signers (`1916-0407`). **Verbatim:** “…as CMS has exceeded its statutory authority and failed to act within the bounds of reasoned decision-making in extending SDP limits to all Medicaid…”

### 2. CMS's own savings estimate is over three times the statute's (about 110 distinct texts)
Commenters set CMS's regulatory impact analysis ($510.1 billion in federal savings over 2026–2035; $774.8 billion including the state share) against CBO's $149.4 billion score for §71116. They cite the gap as proof that the rule cuts far deeper than Congress authorized.
* American Academy of Family Physicians (`1916-0128`). **Verbatim:** “CMS estimates that the combined statutory and regulatory changes would reduce federal Medicaid spending by approximately $510 billion over 10 years—more than three times…”
* Lee County Community Hospital (`1916-0902`). **Verbatim:** “CMS’s own projected federal savings exceed CBO’s score for the statute by $360.7 billion.”
* Allegheny Health Network (`1916-0756`) makes the same $510 billion vs. $149.4 billion comparison.

### 3. Calculate the Medicare limit in the aggregate, not claim by claim (about 200 distinct texts)
CMS proposes testing compliance at the individual service or discharge level, including all Medicare adjustments. Hospitals and states argued this is administratively unworkable and asked for an aggregate, class-level test like the existing FFS upper payment limit (UPL). Several states described the scale of repricing involved; North Carolina cited nearly 2 million unique payment rates (`1916-0387`).
* Rural Hospital Coalition (`1916-0130`). **Verbatim:** “We respectfully urge CMS to permit states to calculate the Medicare payment limit in the aggregate, consistent with existing Medicaid payment methodologies.”
* Mercy Health Ministry (`1916-0058`). **Verbatim:** “CMS proposes to implement SDP limits at the patient and service level rather than on an aggregate basis.”
* Tennessee hospital campaign (`1916-0909` and 89 others). **Verbatim:** “…we urge CMS to allow states to calculate fhe Medicare limit in the aggregate, consistent with the current approach to determining compliance with SDP…” (OCR typo "fhe" is in the source text.)

### 4. "10 percentage points" means points of Medicare, not 10% of the dollar amount (about 140 distinct texts)
The statute phases grandfathered SDPs down by "10 percentage points" a year. CMS reads this as cutting 10% of the original grandfathered dollar amount each year. Commenters argued the cuts become steeper as the base shrinks (10%, then 11.1%, then 12.5% of the remaining balance). Many proposed stepping the payment rate down in Medicare terms instead (200% to 190% to 180%), or applying 10% to the prior year's balance.
* Minnesota Hospital Association (`1916-0785`). **Verbatim:** “…a reduction from 200 percent of Medicare to 190, then to 180, and so on.”
* Monroe County Medical Center (`1916-0255`). **Verbatim:** “The 10-Percentage-Point Reduction Should Be Applied to the Prior Year's Balance, Not the Original Grandfathered Amount…”
* Tennessee Hospital Association (`1916-0399`) put a dollar figure on it. **Verbatim:** “…for Tennessee’s hospital SDP, this means cuts of $320,411,458 per year, based on the grandfathered amount set…”

### 5. Keep uniform-increase SDPs (about 180 distinct texts)
CMS proposes prohibiting new and renewed uniform rate-increase SDPs from 2028. Physician societies, hospital associations and states argued these are the most common, simplest SDP tool. Policy Matters Ohio (`1916-0699`) said they account for more than two-thirds of SDP spending.
* American College of Obstetricians and Gynecologists (`1916-0522`). **Verbatim:** “We urge CMS to not finalize this policy and retain uniform increase SDPs to ensure states have flexibility when designing SDPs to address the…”
* American College of Physicians (`1916-0231`). **Verbatim:** “ACP therefore recommends that CMS retain uniform increase SDPs when states can demonstrate that such arrangements are being used to strengthen clinician participation, improve…”
* AAMC (`1916-0763`) asked CMS to withdraw the prohibition.

### 6. Exempt public and fire-based EMS (GEMT) from Medicare-based limits (about 140 distinct texts, about 240 comments)
This is the largest single bloc by volume, mostly fire departments, fire districts and ambulance districts in California, Illinois, Oregon and Missouri. They argued the Medicare Ambulance Fee Schedule pays far below cost and ignores 24/7 readiness costs. Their GEMT programs are cost-reconciled certified public expenditures rather than inflated payments, they said, so they should qualify for the cost-reconciliation exception (§447.381(d)(2)) or be exempted outright. Many give their own annual loss (see the figures section).
* Fire-service campaign (`1916-0425` and 38 others). **Verbatim:** “As a leader in America’s fire service, I urge CMS to modify the proposal to exempt other provider types for state-directed payments for fire-based…”
* Page, Wolfberg & Wirth, an EMS law firm (`1916-0396`), citing RAND's analysis of CMS ground-ambulance cost data (GADCS). The figure is an all-payer median, not a Medicare-only shortfall. **Verbatim:** “Public safety-based EMS systems face median per-transport shortfalls of –$1,362 (69 percent below cost).”
* Pasadena Fire Department (`1916-0162`). **Verbatim:** “…we estimate an annual funding shortfall of approximately $1 to $1.5M annually, a gap that would need to be absorbed by the City's general…”

### 7. Withdraw the new FFS targeted-payment limit (§447.381) (about 170 distinct texts)
Physician groups, children's hospitals and academic medical centers argued that §71116 covers only managed-care SDPs, so a new Medicare limit on FFS practitioner supplemental payments has no statutory basis. They warned it would end ACR-based (average commercial rate) physician supplemental payments.
* American Academy of Pediatrics (`1916-0926`). **Verbatim:** “We recommend CMS withdraw its proposal to establish a new Medicare-based limit for targeted Medicaid fee-for-service payments, as this policy exceeds the requirements of…”
* NAPNAP (`1916-0408`). **Verbatim:** “NAPNAP urges CMS to withdraw the new Medicare-based limit on targeted Medicaid FFS practitioner payments in its entirety, and withdraw the extension of the…”
* Tufts Medicine (`1916-0781`). **Verbatim:** “We urge CMS to withdraw the proposed FFS practitioner payment limit, or at a minimum to defer it and provide a meaningful transition and…”

### 8. Medicare is the wrong benchmark for children's hospitals and IPPS-exempt providers (about 80 distinct texts)
Freestanding children's hospitals have almost no Medicare volume and are paid on cost by Medicare. They argued a claim-level Medicare limit is meaningless or punitive for them, and asked for a Medicare UPL methodology, an exemption, or a pediatric-specific benchmark. Driscoll argued a cost-based limit would cut far more than Congress intended.
* Children's Hospital Association (`1916-0404`). **Verbatim:** “We expect these changes to reduce children’s hospitals’ SDP payments by over 40% by 2036.”
* Children's Hospital Los Angeles (`1916-0818`). **Verbatim:** “CMS should adopt the Medicare Upper Payment Limit (UPL) methodology as the payment rate limit framework.”
* Driscoll Children's Hospital (`1916-0922`). **Verbatim:** “…rejecting a cost-based SDP limit, which would cut payments well beyond Congress's intended savings; granting IPPS-exempt children's hospitals a targeted exemption or delaying implementation…”

### 9. No Medicare rate, and behavioral health services Medicare doesn't price (about 100 and about 40 distinct texts)
Where no Medicare rate exists, the proposed limit defaults to the Medicaid state plan rate. Commenters argued this freezes payment at the levels SDPs were designed to fix. The concern is sharpest for community behavioral health (CCBHCs, mobile crisis, peer support), HCBS, dental and pediatric services.
* Virginia DMAS (`1916-0755`). **Verbatim:** “CMS Should Not Default Payment Limits to State Plan Rates for Services Without a Medicare Equivalent…”
* WellPower (`1916-0807`). **Verbatim:** “Medicare does not adequately recognize many of the community-based behavioral health services we are required to provide, including crisis response, peer support and care…”
* Ohio Department of Medicaid (`1916-0209`), on its statewide youth mobile-crisis system. **Verbatim:** “A per-service reconciliation does not recognize the defining characteristic of population-based payments.”

### 10. Technical fixes to the Medicare comparison (wage index, net of provider tax, value-based payment)
* **Area wage index (about 30 distinct texts, about 160 comments counting the Tennessee campaign letters).** Low-wage states said Medicare wage adjustments would lock in lower limits; several asked for a 1.0 floor. Vanderbilt Health (`1916-0466`). **Verbatim:** “…we encourage CMS to include a wage index floor of 1.0.”
* **Net of provider taxes (about 10 distinct texts).** Providers fund part of the non-federal share through taxes, so gross Medicaid payments overstate what they keep. Texas Hospital Association (`1916-0581`). **Verbatim:** “CMS should consider aggregate Medicare payment limits from a net-of-tax perspective.” Catawba Valley Medical Center (`1916-0715`) proposed testing only the federal share.
* **Value-based and population-based SDPs (about 160 distinct texts).** Per-service reconciliation conflicts with population-based payment. NAACOS (`1916-0765`). **Verbatim:** “…we do not support requiring States to provide a detailed validation methodology to ensure that payments from value-based payment (VBP) state directed payments (SDPs)…”

### 11. The supporting side: fiscal integrity and financing loopholes (14 support comments)
The 14 supporters were six fiscally conservative think tanks, five individuals, a county fiscal officer (`1916-0309`), a one-person company (`1916-0017`) and one large private ambulance operator. They described uncapped SDPs, funded by provider taxes and intergovernmental transfers (IGTs), as a way to draw extra federal match, and backed the Medicare benchmark.
* FGA Action (`1916-0734`). **Verbatim:** “Uncapped SDPs constitute a loophole for states to effectively launder federal Medicaid dollars.”
* Paragon Health Institute (`1916-0648`). **Verbatim:** “We strongly support CMS’s efforts to faithfully implement these reforms and believe the proposed rule represents an important step toward restoring accountability and integrity…”
* Arnold Ventures (`1916-0117`). **Verbatim:** “We strongly support CMS’s implementation of limits on SDPs, which will break the tie between Medicaid and ACR and curb the rapidly rising use…”
* Others in support: Competitive Enterprise Institute (`1916-0817`, supporting "several of the provisions"), Americans for Prosperity (`1916-0883`), Center for a Free Economy (`1916-0101`) and Global Medical Response (`1916-0332`).

### Individuals (196 comments)
Paraphrase: Most individual comments are short and oppose Medicaid "cuts" in general, often from pediatricians, behavioral health clinicians, home-care aides and chronic-illness patients. Many do not engage the rule's provisions. A coordinated 11-letter chronic-illness campaign (`1916-0174`) asks CMS to weigh patients' perspectives. Eight sitting state legislators filed in their official capacity (counted as state agencies). They argued the rule usurps state authority (`1916-0259`, `1916-0379`, `1916-0960`); one puts the cuts at nearly $800 billion (`1916-0204`). An anonymous pediatrician (`1916-0009`). **Verbatim:** “The proposed cuts in Medicaid funding proposed by CMS will have a severe effect on the 50% of kids that I take care of…”

## Dollar figures and impact estimates cited (CMS-2449-P)

The full list is in `output/evidence_ledger_delta.csv`: 3,636 rows from 473 CMS-2449-P comments as filed (3,637 rows from 474 comments corrected). The table below lists the figures I read in context, chosen for size, specificity or how often they recur. The excerpts are verbatim; "Means" is my paraphrase. Classifying whether a figure is the commenter's own estimate or cited from CMS, CBO or another source is **[inferred]**.

**National estimates (cited, not original to the commenters)**

| Figure | Means (paraphrase) | Commenter / ID | Source file |
|---|---|---|---|
| $510 billion | CMS RIA federal savings, 2026–2035; cited in about 120 comments (about 90 distinct texts) **[inferred count]** | AAFP, `1916-0128` | `data/CMS-2026-1916/attachments/CMS-2026-1916-0128_attachment_1.docx` |
| $149.4 billion | CBO score of §71116, cited in about 90 comments (about 60 distinct texts) **[inferred count]** | Allegheny Health Network, `1916-0756` | `…/CMS-2026-1916-0756_attachment_1.pdf` |
| $360.7 billion | CMS estimate minus CBO score | Lee County Community Hospital, `1916-0902` | `…/CMS-2026-1916-0902_attachment_1.docx` |
| $774.8 billion | CMS total (federal + state) SDP reduction, 2026–2035 | e.g. Kentucky Health Collaborative, `2476-0056` (cited cross-docket) and about 30 CMS-2449-P comments (about 10 distinct texts) **[inferred count]** | see ledger |
| $0.13 million | RIA's annualized cost-saving line; SPAN asks CMS to clarify it, given the RIA says benefits cannot be quantified | SPAN, `1916-0629` | `…/CMS-2026-1916-0629_attachment_1.docx` |

**State and system impact estimates (commenters' own figures)**

| Figure | Means (paraphrase) | Commenter / ID | Source file |
|---|---|---|---|
| $320,411,458 / yr | Tennessee hospital SDP cut under CMS's dollar-based phase-down (same claim in the 90-letter campaign as "over $320 million") | Tennessee Hospital Association, `1916-0399`; Parkwest, `1916-0909` | `…/CMS-2026-1916-0399_attachment_1.pdf`; `…/CMS-2026-1916-0909_attachment_1.pdf` |
| $2.4 billion | Tennessee uncompensated care that would have been higher in 2025 without the SDP | Tennessee Hospital Association, `1916-0399` | `…/CMS-2026-1916-0399_attachment_1.pdf` |
| $4.3 billion / yr | Texas hospital payment reduction once the phase-down completes, which TEHP attributes to the statute's SDP provisions (WFTC), not to the rule's extensions | Texas Essential Healthcare Partnerships, `1916-0415` (also DHR Health, `1916-0814`) | `…/CMS-2026-1916-0415_attachment_1.pdf` |
| $915 million / yr | Removed from Texas CHIRP each year from SFY 2029 | Texas Health Resources, `1916-0885` | `…/CMS-2026-1916-0885_attachment_1.pdf` |
| $4.4 billion | Florida DPP payment reduction when fully implemented | Florida Essential Healthcare Partnerships, `1916-0417` | `…/CMS-2026-1916-0417_attachment_1.pdf` |
| $1.2 billion / yr (66.7%) | New Mexico SDPs falling from $1.8 billion to about $600 million | New Mexico Health Care Authority, `1916-0835` | `…/CMS-2026-1916-0835_attachment_1.pdf` |
| $3.4 billion through 2032 | New Jersey hospital funding loss from §71116 alone | New Jersey Hospital Association, `1916-0751` | `…/CMS-2026-1916-0751_attachment_1.pdf` |
| $30 billion+ | Projected reductions for Virginia hospitals from the H.R. 1 SDP provisions | Virginia Hospital & Healthcare Association, `1916-0555` | `…/CMS-2026-1916-0555_attachment_1.pdf` |
| $11.7 billion | Cumulative statewide reductions over the implementation period; the state, Louisiana, is **[inferred]** from the next heading (the sentence does not name it) | FMOL Health, `1916-0338` | `…/CMS-2026-1916-0338_attachment_1.pdf` |
| $160 million / yr | Mississippi hospital losses | Baptist Memorial Health Care, `1916-0650` | `…/CMS-2026-1916-0650_attachment_1.pdf` |
| $2 billion+ | New York hospital Medicaid revenue lost to the H.R. 1 SDP changes | GNYHA, `1916-0822` | `…/CMS-2026-1916-0822_attachment_1.pdf` |
| $600 million | Cumulative Massachusetts hospital SDP reduction by phase-down year 3 | Tufts Medicine, `1916-0781` | `…/CMS-2026-1916-0781_attachment_1.pdf` |
| $322 million | Added Colorado impact of an accelerated phase-down over 7 years | Denver Health, `1916-0323` | `…/CMS-2026-1916-0323_attachment_1.pdf` |
| $340 million / yr | Children's Health (Dallas) SDP loss under a facility-wide cost-to-charge method | Children's Health, `1916-0634` | `…/CMS-2026-1916-0634_attachment_1.pdf` |
| 40% by 2036 | Children's hospitals' SDP payment reduction | Children's Hospital Association, `1916-0404` | `…/CMS-2026-1916-0404_attachment_1.pdf` |
| $66.3 million / yr (57.7%) | Woman's Hospital (LA) inpatient payment drop | Woman's Hospital, `1916-0519` | `…/CMS-2026-1916-0519_attachment_1.pdf` |
| $22.35M to $6.21M | Mt. Graham Regional (AZ) HEALTHII payments, FFY2026 to FFY2031 | Mt. Graham Regional Medical Center, `1916-0608` | `…/CMS-2026-1916-0608_attachment_1.docx` |
| $100 million+ / yr | Physician practice plan's Medicaid reimbursement loss moving from ACR to Medicare | University of Colorado Anschutz, `1916-0390` | `…/CMS-2026-1916-0390_attachment_1.pdf` |
| $892,374 (93%) | Bath Community Hospital (VA critical access hospital) SDP loss | Bath Community Hospital, `1916-0844` | `…/CMS-2026-1916-0844_attachment_1.docx` |
| $6.6 million / yr, ~68 FTEs | Virginia's added staffing to administer claim-level compliance | Commonwealth of Virginia, `1916-0890` | `…/CMS-2026-1916-0890_attachment_1.pdf` |
| ~2 million rates | Unique payment rates North Carolina would have to compare with Medicare | NC DHHS, `1916-0387` | `…/CMS-2026-1916-0387_attachment_1.pdf` |

**EMS figures**

| Figure | Means (paraphrase) | Commenter / ID | Source file |
|---|---|---|---|
| –$1,362 per transport | Median all-payer revenue shortfall per transport for public-safety EMS (69% below cost), from RAND's analysis of CMS GADCS Year 1–4 data (Dec 2025). PWW's Medicare-only figures for these providers: median –$1,640 (83%), mean –$3,216 (91%) | Page, Wolfberg & Wirth, `1916-0396` | `…/CMS-2026-1916-0396_attachment_1.pdf` |
| ~$10 million / yr | CENCAL Fire & EMS Authority GEMT revenue at risk (about 15% of budget) | CENCAL, `1916-0333` | `…/CMS-2026-1916-0333_attachment_1.pdf` |
| $5 million+ | Anaheim Fire & Rescue reimbursement loss | City of Anaheim, `1916-0955` | `…/CMS-2026-1916-0955_attachment_1.docx` |
| $1.65 million / yr | South Elgin & Countryside FPD (IL) revenue loss | `1916-0230` | `…/CMS-2026-1916-0230_attachment_1.pdf` |
| $1–1.5M / yr | Pasadena Fire Department shortfall | `1916-0162` | `data/CMS-2026-1916/CMS-2026-1916-0162.json` (comment field) |

**Supporters' figures**

| Figure | Means (paraphrase) | Commenter / ID | Source file |
|---|---|---|---|
| $192–385 billion | Reduced "excess burden of taxation" over a decade | Paragon Health Institute, `1916-0648` | `…/CMS-2026-1916-0648_attachment_1.pdf` |
| $26B to $137B | Growth in annual SDP spending, 2020 to 2026 | Competitive Enterprise Institute, `1916-0817` | `…/CMS-2026-1916-0817_attachment_1.pdf` |
| ~$2,609 vs. $339 per transport | CFE: pending California public-provider rate, "286 percent above documented costs" (measured against Huntington Beach's reported ~$676 cost), vs. private providers' total Medi-Cal payment per transport. The 911 Alliance cites the same $339 but puts the pending public rate at over $1,600 | Center for a Free Economy, `1916-0101` ($2,609, 286%, $339); 911 Ambulance Provider's Medi-Cal Alliance, `1916-0943` ($339) | `data/CMS-2026-1916/CMS-2026-1916-0101.json` (comment field); `…/CMS-2026-1916-0943_attachment_1.pdf` |

Pattern **[inferred]**: national figures in this docket are almost all citations of CMS's RIA or CBO. Original quantification comes from state hospital associations and individual systems (mostly annual dollar losses) and from EMS agencies (per-transport cost vs. Medicare rate, and annual GEMT revenue at risk). Few commenters estimate coverage or access effects in numbers; most access claims are qualitative.

## Notable outliers and novel arguments (CMS-2449-P)

* **A large private ambulance operator supports the rule.** Global Medical Response (`1916-0332`), which describes itself as the largest US EMS provider, backs the proposed rule (**Verbatim:** “…which it strongly supports.”). It argues Medicaid should pay for services, not ownership. The 911 Ambulance Provider's Medi-Cal Alliance (`1916-0943`) and the Center for a Free Economy (`1916-0101`) argue California's public-provider GEMT payments far exceed private rates. This directly contradicts the fire-service campaign (argument 6).
* **Stop approving pending SPAs now.** The Center for a Free Economy (`1916-0101`) asks CMS to stop approving state plan amendments that rely on methods the rule would end. **Verbatim:** “CMS should not approve pending State Plan Amendments (SPAs), waivers, or related financing requests that rely upon reimbursement methodologies CMS has already identified as…”
* **Interstate transfer framing.** CEI (`1916-0817`) argues low-SDP states subsidize high-SDP states. **Verbatim:** “Florida is sending about $5.5 billion to other states that are using SDPs disproportionately.”
* **Make Medicare the floor, not the ceiling.** Families USA (`1916-0792`). **Verbatim:** “…we urge CMS to set the Medicare benchmark as the floor.”
* **A higher fallback for services with no Medicare rate.** University of Missouri Health Care (`1916-0867`) proposes a limit that **Verbatim:** “…should be triple the approved Medicaid state plan rate.”
* **Recoupment penalizes success.** A group of pediatric practices (`1916-0305`) works through an example where a per-member care-management payment pushes a practice over the Medicare benchmark only after it reduces utilization. **Verbatim:** “…the proposal could claw back money in the very year the practice cut the child's total cost of care from $2,610 to $700.”
* **MCO downstream payments.** Waymark (`1916-0281`) asks CMS to confirm that MCO-negotiated payments to provider-enablement partners are not SDPs.
* **Psychiatric facility carve-out.** The Manhattan Institute's mental health policy team (`1916-0659`). **Verbatim:** “We recommend that CMS explicitly exempt IMDs and PRTFs from the proposed rule altogether.”
* **Fix the ambulance fee schedule instead.** The International Association of Fire Fighters (`1916-0444`) urges a holistic reform of the Medicare and Medicaid ambulance fee schedules rather than tying Medicaid to Medicare's rates.
* **Narrow support from a value-based-care company.** Diverge Health (`1916-0405`) supports guardrails on SDPs that **Verbatim:** “…exist to enrich a narrow set of providers with no clear connection to…” while objecting to how the limits treat value-based arrangements **[inferred from its position tag; not read in full]**.
* **Individual supporter on debt grounds.** Leona Herndon (`1916-0048`). **Verbatim:** “…which I greatly support because this country needs to reduce our debt.”
* **Off-topic or misfiled.** Three nursing/coaching organizations (`1916-0851`, `1916-0937`, `1916-0941`) comment on national payment for health-coaching billing codes (CPT 0591T–0593T), which is not part of this rule **[inferred: they belong to a different rulemaking]**. They are counted as off-topic in the type and position tables. Conversely, the California Behavioral Health Association's CMS-2449-P letter was filed a second time in the CMS-2452-P docket (`2476-0199`, an exact copy of `1916-0958`); the methods note covers the corrected totals. A work-requirements question from an individual (`1916-0031`) also does not concern this rule and is counted as off-topic.

---

# CMS-2452-P — Indirect hold harmless threshold for health care-related taxes (docket CMS-2026-2476)

## Counts by commenter type and position

**All comments, as filed (n = 214)**

| Commenter type | Oppose | Request for changes | Mixed | Support | Unclear / off-topic | Total |
|---|---:|---:|---:|---:|---:|---:|
| Association | 19 | 60 | 4 | 0 | 0 | 83 |
| Advocacy group | 19 | 11 | 0 | 3 | 0 | 33 |
| Individual | 20 | 9 | 1 | 1 | 0 | 31 |
| Hospital / health system | 3 | 25 | 2 | 0 | 0 | 30 |
| State agency | 9 | 12 | 1 | 0 | 0 | 22 |
| Other | 2 | 10 | 0 | 0 | 0 | 12 |
| MCO | 1 | 0 | 0 | 0 | 0 | 1 |
| Off-topic (addresses neither rule) | 0 | 0 | 0 | 0 | 2 | 2 |
| **Total** | **73** | **127** | **8** | **4** | **2** | **214** |

**All comments, corrected (n = 213).** Removing the CMS-2449-P letter `2476-0199` changes only the Association row (83 to 82) and the request-for-changes column (127 to 126).

| Commenter type | Oppose | Request for changes | Mixed | Support | Unclear / off-topic | Total |
|---|---:|---:|---:|---:|---:|---:|
| Association | 19 | 59 | 4 | 0 | 0 | 82 |
| Advocacy group | 19 | 11 | 0 | 3 | 0 | 33 |
| Individual | 20 | 9 | 1 | 1 | 0 | 31 |
| Hospital / health system | 3 | 25 | 2 | 0 | 0 | 30 |
| State agency | 9 | 12 | 1 | 0 | 0 | 22 |
| Other | 2 | 10 | 0 | 0 | 0 | 12 |
| MCO | 1 | 0 | 0 | 0 | 0 | 1 |
| Off-topic (addresses neither rule) | 0 | 0 | 0 | 0 | 2 | 2 |
| **Total** | **73** | **126** | **8** | **4** | **2** | **213** |

**Distinct texts, as filed (n = 188):** oppose 64, request for changes 110, mixed 8, support 4, unclear / off-topic 2. By type: association 72, advocacy group 31, hospital / health system 26, individual 26, state agency 22, other 8, MCO 1, off-topic 2.

**Distinct texts, corrected (n = 187):** oppose 64, request for changes 109, mixed 8, support 4, unclear / off-topic 2. By type: association 71, advocacy group 31, hospital / health system 26, individual 26, state agency 22, other 8, MCO 1, off-topic 2.

Campaigns are small: 10 campaigns cover 36 comments, as filed and corrected. The largest is 11 behavioral health and IDD provider letters (`2476-0136`, Ability Network of Delaware).

The mix differs from CMS-2449-P. Hospital associations mostly *request changes* to how the threshold is measured and enforced. Opposition is concentrated among individuals, advocacy groups and state budget think tanks, plus insurance regulators and state-based marketplaces objecting to the new health insurer tax class.

## Top recurring arguments

### 1. Drop the new "services of health insurers" tax class (about 100 distinct texts)
CMS proposes a new permissible class, §433.56(a)(19). Commenters argued it would sweep premium taxes, marketplace user fees, reinsurance assessments and other non-Medicaid levies into Medicaid provider-tax rules and the new caps. State insurance departments, marketplaces and the NAIC said CMS lacks authority and the class threatens marketplace funding. Some, like Oklahoma, Pennsylvania and Indiana, accepted the goal but asked for explicit exclusions.
* NAIC (`2476-0027`). **Verbatim:** “This would impact state premium taxes, state guarantee association assessments, state-based reinsurance programs, licensing fees used to support the operations of state insurance departments…”
* Oregon Department of Consumer and Business Services (`2476-0096`). **Verbatim:** “We oppose the proposed addition of “services of health insurers” to section 433.56 because CMS lacks statutory authority to make this change.”
* Families USA (`2476-0099`). **Verbatim:** “…we strongly urge CMS to withdraw its proposal to include taxes on the “services of health insurers” within the CMS-regulated provider tax framework.”

### 2. Keep the 75/75 test, the second prong of the hold harmless test (about 80 distinct texts)
Commenters argued P.L. 119-21 does not require eliminating it, that it was codified by Congress in 2006, and that CMS cites almost no evidence of abuse.
* National Health Law Program (`2476-0031`). **Verbatim:** “The Department lacks the authority to eliminate the 75/75 test, which was codified by Congress in the Tax Relief and Health Care Act of…”
* Sutter Health (`2476-0123`). **Verbatim:** “Given that there is no evidence of gaming occurring through this long-legitimate pathway, Sutter Health urges CMS to maintain the 75/75 test as an…”
* Arizona Hospital & Healthcare Association (`2476-0077`). **Verbatim:** “Rare use indicates a narrow compliance pathway, not a loophole.”

### 3. Enforce prospectively, and penalize only the excess (about 120 and about 40 distinct texts)
CMS would set thresholds from actual collections reconciled years later. Exceeding a threshold by any amount would disallow the entire tax for the class. Commenters argued this "cliff" is disproportionate and unmanageable, and asked for prospective, rate-based compliance and disallowance limited to the excess.
* Michigan Health & Hospital Association (`2476-0036`). **Verbatim:** “…theoretically by even one penny, would result in invalidation of the entire provider tax for the entire class.”
* Hospital and Healthsystem Association of Pennsylvania (`2476-0089`), illustrating the cliff. **Verbatim:** “CMS would deduct the full $1,000,000,000.29, not just $0.29 from the state’s Medical Assistance expenditures.”
* Mosaic (`2476-0054`). **Verbatim:** “…breaching the tax threshold by even a tiny fraction triggers a class-wide "cliff" penalty that invalidates the entire tax structure, exposing states to multi-hundred-million-dollar…”

### 4. "Enacted and imposed": support for the new definitions, requests for flexibility (about 100 distinct texts)
This is the provision most often praised. Many commenters welcomed the broader reading of which taxes count as enacted and imposed by July 4, 2025, which grandfathers more existing taxes than CMS's November 2025 guidance. Many also asked to choose the 12-month measurement period, since the choice can move a state's grandfathered amount materially.
* Alliance of Community Health Plans (`2476-0040`). **Verbatim:** “We particularly support CMS' proposed interpretation of "enacted and imposed," which preserves more existing provider taxes than CMS' earlier guidance suggested.”
* National Conference of State Legislatures (`2476-0210`). **Verbatim:** “We strongly support the clarification of the November 2025 guidance included in the proposed rule regarding the definition of an “imposed” provider tax which…”
* Arizona Hospital & Healthcare Association (`2476-0077`). **Verbatim:** “Allow each state to select any 12-month measurement period that includes July 4, 2025.”

### 5. Reporting burden and deadlines (§433.74) (about 90 distinct texts)
The new one-time and quarterly reporting would require provider-level data, often from local governments. Commenters said the deadlines are unrealistic: December 31, 2026 for interim data and June 30, 2028 for final data.
* Defend Forgotten America (`2476-0045`). **Verbatim:** “A reporting requirement that seems modest when viewed from Baltimore may require a State Medicaid agency to contact dozens of local governments, each of…”
* NAIC (`2476-0027`). **Verbatim:** “It does seem clear that the proposal would place onerous reporting requirements on many states.”
* Steven Singleton (`2476-0023`, individual). **Verbatim:** “…set fixed, concrete deadlines -- December 31, 2026, for interim data and June 30, 2028, for final data -- for the one-time submissions that…”

### 6. The impact analysis understates harm (about 40 distinct texts)
CMS projects $246 billion in federal savings against CBO's $183–191 billion for §71115 (CBO attribution as cited by AHCCCS `2476-0201`, UHA `2476-0097` and PA DHS `2476-0126`). Commenters argued this shows the rule goes beyond the statute. They also faulted the RIA for assuming no coverage loss, against CBO's 1.1 million more uninsured, and for assuming states replace 30% of lost revenue.
* Hospital and Healthsystem Association of Pennsylvania (`2476-0089`). **Verbatim:** “CMS projects federal savings of approximately $246 billion, substantially exceeding the estimated $183 billion associated with the statutory changes enacted by Congress.”
* Jason Levitis (`2476-0179`). **Verbatim:** “CMS assumes without any basis that the rule would have no effect on health coverage, despite reducing federal Medicaid spending by almost $250 billion.”
* Texas Hospital Association (`2476-0109`), on the 30% offset assumption. **Verbatim:** “…it is highly improbable that it would be equal to 30 percent of lost funds (or even a much smaller fraction of that).”

### 7. Expansion-state phase-down and state budget effects (about 60 distinct texts)
The threshold falls from 6% toward 3.5% in expansion states from FFY 2028. State budget groups and hospital associations quantified state-level losses (see figures) and warned of rate cuts and lost coverage.
* Missouri Hospital Association (`2476-0035`). **Verbatim:** “Once the tax threshold reaches 3.5%, the ongoing annual impact to Missouri would be $1.25 billion.”
* New Mexico Health Care Authority (`2476-0186`). **Verbatim:** “…will result in $125M less in collections from hospitals annually to the State of New Mexico and a nearly $8.5B reduction in revenue to…”
* OpenSky Policy Institute, Nebraska (`2476-0107`). **Verbatim:** “Starting October 2027, these revenues would be reduced by an estimated $68 million combined.7 In an already strained budget environment, these changes would most…”

### 8. The supporting side (4 support comments)
Supporters framed provider taxes as a financing gimmick that shifts cost to federal taxpayers and private payers.
* FGA Action (`2476-0192`). **Verbatim:** “FGA Action supports the proposed rule.”
* National Taxpayers Union (`2476-0207`). **Verbatim:** “NTU strongly supports CMS’s efforts to faithfully implement Congress’s reforms to Medicaid provider taxes.”
* Paragon Health Institute (`2476-0130`). **Verbatim:** “This translates into $502 billion to $875 billion in benefits for non-Medicaid consumers over the 2025-2034 period.”
* Michelle Mitchell (`2476-0028`, individual). **Verbatim:** “I support the proposed rule CMS-2452-P, Medicaid Program: Amending the Indirect Hold Harmless Threshold of Health Care-Related Taxes.”

## Dollar figures and impact estimates cited (CMS-2452-P)

Full list: 568 ledger rows from 114 CMS-2452-P comments as filed (567 rows from 113 comments corrected; the one row moved is a Medi-Cal enrollment count in `2476-0199`, not cited here). The table below lists the figures I read in context; "Means" is my paraphrase and source classification is **[inferred]**.

**National estimates (cited)**

| Figure | Means (paraphrase) | Commenter / ID | Source file |
|---|---|---|---|
| $246B vs. $183B | CMS RIA federal savings vs. "the estimated $183 billion associated with the statutory changes". HAP does not name the source of $183B; other commenters attribute it to CBO | HAP, `2476-0089` | `…/CMS-2026-2476-0089_attachment_1.docx` |
| $384B ($245.8B federal + $138.2B state) | CMS RIA total Medicaid spending reduction, 2026–2035 | Center for Civil Justice, `2476-0108` | `…/CMS-2026-2476-0108_attachment_1.pdf` |
| $198.7B (27%) | CMS RIA reduction in state provider-tax revenue | Massachusetts Medical Society, `2476-0115` | `…/CMS-2026-2476-0115_attachment_1.pdf` |
| $220.3B | CMS RIA net reduction in payments to providers | AHCCCS, `2476-0201` | `…/CMS-2026-2476-0201_attachment_1.pdf` |
| $601B | CMS combined federal reduction, provider tax plus SDP rules (per CBPP) | CBPP, `2476-0033` | `…/CMS-2026-2476-0033_attachment_1.pdf` |
| 1.1 million | CBO: more uninsured from §71115 by 2034 | Georgetown CCF, `2476-0029` | `…/CMS-2026-2476-0029_attachment_1.pdf` |
| $9.1B–$90.9B | CMS net federal savings range after interaction with the SDP rule | BCBSA, `2476-0091` | `…/CMS-2026-2476-0091_attachment_1.pdf` |
| ~$138B | Hospitals' share of the $220.3B; the commenter labels it "an illustrative allocation, not a CMS estimate" | CHLA Medical Group, `2476-0212` | `…/CMS-2026-2476-0212_attachment_1.docx` |

**State impact estimates (commenters' own or state agencies' figures)**

| Figure | Means (paraphrase) | Commenter / ID | Source file |
|---|---|---|---|
| $1.25B / yr | Missouri annual impact once the threshold reaches 3.5% | Missouri Hospital Association, `2476-0035` | `…/CMS-2026-2476-0035_attachment_1.pdf` |
| $55.6M per 0.1% | Federal match lost per 0.1-point tax cut in Missouri | Missouri Hospital Association, `2476-0035` | same file |
| $4.2B | New York hospital revenue loss across three proposals when fully implemented | GNYHA, `2476-0184` | `…/CMS-2026-2476-0184_attachment_1.pdf` |
| $1.5B | New York MCO tax yielding about $1.5B less than projected (originally $3.7B over two years), which Iroquois attributes to CMS's February 2026 uniformity-waiver final rule, not to CMS-2452-P | Iroquois Healthcare Association, `2476-0072` | `…/CMS-2026-2476-0072_attachment_1.pdf` |
| $125M / yr; ~$8.5B / decade; 21,600 jobs | New Mexico collections loss, hospital revenue loss, and job impact (the commenter scales a published study) | New Mexico Health Care Authority, `2476-0186` | `…/CMS-2026-2476-0186_attachment_1.pdf` |
| $1B / yr | Minnesota loss from the provider-tax reforms (citing Minnesota DHS) | Minnesota Medical Association, `2476-0150` | `…/CMS-2026-2476-0150_attachment_1.pdf` |
| up to $2.5B / yr | Colorado Medicaid funding at risk | Colorado Fiscal Institute, `2476-0178` | `data/CMS-2026-2476/CMS-2026-2476-0178.json` (comment field) |
| $1.7B / yr | Texas revenue capacity eliminated by the freeze | Texas Essential Healthcare Partnerships, `2476-0172` | `…/CMS-2026-2476-0172_attachment_1.pdf` |
| $272M / yr | Florida revenue capacity eliminated by the freeze | Florida Essential Healthcare Partnerships, `2476-0176` | `…/CMS-2026-2476-0176_attachment_1.pdf` |
| $150M | Immediate supplemental-payment cut to UMMC (Mississippi) | University of Mississippi Medical Center, `2476-0165` | `…/CMS-2026-2476-0165_attachment_1.docx` |
| $68M | Nebraska revenue reduction from October 2027 | OpenSky Policy Institute, `2476-0107` | `…/CMS-2026-2476-0107_attachment_1.pdf` |
| ~$120M / yr | Colorado insurer affordability fee exposed to the new insurer class | State of Colorado, `2476-0156` | `…/CMS-2026-2476-0156_attachment_1.pdf` |
| ~$50M | Swing in Arizona's grandfathered amount depending on the 12-month window | AzHHA, `2476-0077` | `…/CMS-2026-2476-0077_attachment_1.pdf` |
| 16% | Average premium reduction from state reinsurance in 2023, which the insurer class could threaten | Families USA, `2476-0099` | `…/CMS-2026-2476-0099_attachment_1.pdf` |
| 55% | Share of surveyed IDD providers that turned away referrals because of staffing | ANCOR, `2476-0068` | `…/CMS-2026-2476-0068_attachment_1.pdf` |

**Supporters' figures**

| Figure | Means (paraphrase) | Commenter / ID | Source file |
|---|---|---|---|
| $502–875B; $61.5–123B | Benefits to non-Medicaid consumers; reduced excess tax burden | Paragon Health Institute, `2476-0130` | `…/CMS-2026-2476-0130_attachment_1.pdf` |

Pattern **[inferred]**: CMS-2452-P commenters lean even more heavily on the RIA's own numbers ($246B, $384B, $198.7B, $220.3B) than CMS-2449-P commenters do. Original estimates come mainly from state hospital associations and three state agencies (New Mexico, Arizona, Colorado).

## Notable outliers and novel arguments (CMS-2452-P)

* **A misfiled letter.** `2476-0199` is the California Behavioral Health Association's CMS-2449-P (SDP) letter, an exact copy of `1916-0958`. It is tagged against the SDP rule in `comments_tagged.csv`, counts in this docket's as-filed totals, and is left out of the corrected totals above.
* **A private-coverage consumer opposes the rule.** Alex Li (`2476-0010`), a privately insured California resident, argues insurer taxes will be passed on in premiums. **Verbatim:** “I oppose CMS-2452-P because it may shift Medicaid financing costs onto people with private coverage.”
* **Non-Medicaid assessments caught by the insurer class.** PATH Foundation (`2476-0119`) asks that SUVP assessments be excluded. **Verbatim:** “…establish conclusively that SUVP assessments are not considered health care-related taxes under federal Medicaid law.” A Washington state agency (`2476-0202`) asks the same for its universal childhood vaccine program's assessment. Marketplaces and vendors (HealthSource RI `2476-0177`, Access Health CT `2476-0132`, Vimo `2476-0024`) raise exchange user fees.
* **Supporters cite rural closures.** Paragon (`2476-0130`) claims provider-tax states had more than three times the rural hospital closures of non-provider-tax states (**Verbatim:** “…rural hospital closures per 10 million residents.”). Opponents argue the opposite: provider taxes sustain rural hospitals.
* **Cross-rule interaction.** Several commenters (Kentucky Health Collaborative `2476-0056`, CBPP `2476-0033`, CHLA Medical Group `2476-0212`) argue the two rules must be analyzed together, since much of the SDP spending capped by CMS-2449-P is financed by the taxes capped here.
* **Off-topic individual comments.** Two individuals (`2476-0002`, `2476-0017`) write about Medicaid work requirements rather than provider taxes. Both are counted as off-topic in the tables above (they were "oppose" before the reclassification).
