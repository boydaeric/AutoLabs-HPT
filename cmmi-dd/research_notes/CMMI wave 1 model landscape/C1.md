# C1 — CMMI Model Landscape and Eligibility Triage for an NYS IPA with an Affiliated IPPS Hospital (as of October 8, 2026)

Scope note: "the Client" means an independent physician association (IPA) in New York State with an affiliated IPPS acute-care hospital. The Client's county, CBSA, hospital CCN, specialty mix, and attributed-beneficiary count were not available to this card. Every UNCLEAR verdict below can be resolved by one of those facts. All claims are tagged [C1, H/M/L]. Status labels follow the card's definitions: **established** = operating or finalized in regulation; **proposed** = in a proposed rule; **announced** = stated by CMS but not yet in regulation or an RFA. Where CMS's own website label differs from the card's definition (e.g., CMS shows "Announced" for models already finalized in rule text), both are shown.

Method note: the CMS models index page (cms.gov/priorities/innovation/models) is rendered by JavaScript. Its underlying data feed is the CMS "Innovation Center Model Summary Information" dataset on data.cms.gov, which this card pulled directly (105 rows: 20 Active, 8 Announced, 4 Authorized for Expansion, 9 Performance Period Ended, 61 Not Active, 3 Withdrawn). That dataset was the starting candidate set, so the candidate set was not assumed. Participant and geography spreadsheets (TEAM, ASM, IOTA, AHEAD) were downloaded from cms.gov and filtered for New York.

---

## Q1. Which CMMI models are open, announced, or upcoming as of October 2026, and which have ended? (Full landscape and triage)

### Takeaway
Fourteen models matter for an NYS IPA plus hospital. Five are **mandatory and geography- or facility-driven**, so the Client's role is to prepare, not to choose: TEAM (since Jan 1, 2026, in 6 NY CBSAs), CJR-X (nationwide from Jan 1, 2028 for non-TEAM IPPS hospitals), ASM (from Jan 1, 2027, in 11 upstate NY CBSAs, not NYC or Long Island), IOTA (only if the hospital runs a kidney transplant program in a selected NY DSA), and WISeR (not in NY). The **voluntary paths that are actually open or opening** are: ACCESS (rolling applications), LEAD (PY2027 window closed May 17, 2026; CMS expects future windows and accepts Letters of Interest), MSSP (non-CMMI baseline; the window for a Jan 1, 2027 start closed June 2026), AHEAD/Geo AHEAD (New York joined as a downstate sub-state region; Geo Entity RFA expected Q1 2027; performance from Jan 1, 2028), and MAHA ELEVATE cohort 2 (2027, window not yet posted). EOM, ACO REACH, KCC, GUIDE, and ACO PC Flex have no open window. MCP, PCF, ETC, and Maryland TCOC ended early by Dec 31, 2025 [C1, H].

### (a) Summary landscape table

| # | Model | (1) Status (card definition) and dates | (2) Vol./Mand. | (3) Eligible participant types; can an IPA / ACO / CIN / PGP (TIN) / hospital be the direct participant? | (4) Geography; NY included? | (5) Application window | (6) Start to end | (7) Volume or case thresholds | (8) Triage for NYS IPA + affiliated hospital |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **TEAM** (Transforming Episode Accountability Model) | **Established**: finalized in FY2025 IPPS final rule, updated FY2026 and FY2027 IPPS. CMS: "Active" [C1, H] | Mandatory (one-time voluntary opt-in only for former BPCI-A/CJR hospitals) [C1, H] | Participant = IPPS acute-care hospital (CCN). IPA, ACO, CIN, PGP: **not** direct participants (collaborator role only, see notes). Hospital: **yes** [C1, H] | Selected CBSAs. **NY included, 6 CBSAs**: 35620 New York-Newark-Jersey City NY-NJ; 15380 Buffalo-Cheektowaga; 12860 Batavia; 36580 Oneonta; 18660 Cortland; 32390 Massena-Ogdensburg [C1, H] | None (mandatory). Opt-in window closed [C1, M] | Jan 1, 2026 to Dec 31, 2030 (5 PYs) [C1, H] | 30-day episodes for LEJR, SHFFT, spinal fusion, CABG, major bowel. Per-episode-category low-volume reconciliation rule (at least 31 episodes in 3-yr baseline; FY2027 rule reg text) [C1, M] | **UNCLEAR**: mandatory if the affiliated hospital's CCN is in one of the 6 NY CBSAs. Resolve by matching the hospital CCN to the CMS TEAM participant list (Aug 18, 2026 version). |
| 2 | **CJR-X** (Comprehensive Care for Joint Replacement Expanded) | **Established**: finalized in FY2027 IPPS/LTCH final rule (CMS-1849-F; 91 FR 49570; FR pub. Aug 4, 2026; effective Oct 1, 2026). CMS website still labels it "Announced" [C1, H] | Mandatory [C1, H] | Participant = acute-care hospital paid under both IPPS and OPPS. Excludes TEAM hospitals, Maryland hospitals, CAHs, and REHs. IPA, ACO, PGP: **not** direct participants. They may be **CJR-X collaborators**; the finalized list includes PGP, physician, hospital, and Medicare ACO [C1, H] | Nationwide (50 states, DC, territories) except TEAM and Maryland hospitals. **NY included** for every NY IPPS hospital not in TEAM [C1, H] | None (mandatory) [C1, H] | Jan 1, 2028; **no fixed end date** (CMS rejected commenters' objections to this). TEAM hospitals move into CJR-X on Jan 1, 2031 after TEAM ends [C1, H] | 90-day LEJR episodes (MS-DRG 469/470/521/522; HCPCS 27447/27130; inpatient and outpatient). Low-volume hospital = fewer than 31 LEJR episodes in baseline. Such hospitals are still participants but are excluded from reconciliation [C1, M] | **ELIGIBLE (mandatory) for the hospital**: from Jan 1, 2028 if the hospital is not in TEAM, or from Jan 1, 2031 if it is. IPA: collaborator role only. |
| 3 | **ASM** (Ambulatory Specialty Model) | **Established**: finalized in CY2026 PFS final rule. CMS website labels it "Announced" and has published the final PY2027 participant list [C1, H] | Mandatory; no opt-out (secondary) [C1, H for mandatory; L for no-opt-out] | Participant = **individual specialist (TIN+NPI)**. Heart failure: cardiology. Low back pain: anesthesiology, pain mgmt, interventional pain, neurosurgery, ortho surgery, PM&R. IPA, ACO, CIN, hospital: **not** direct participants. PGP TIN is the billing unit, and improvement activities and Promoting Interoperability are scored at group level [C1, H] | About one-quarter of CBSAs and metro divisions. **NY included, 11 CBSAs, all upstate**: 10580 Albany-Schenectady-Troy; 15380 Buffalo-Cheektowaga; 27460 Jamestown-Dunkirk; 28740 Kingston; 28880 Kiryas Joel-Poughkeepsie-Newburgh; 32390 Massena-Ogdensburg; 36460 Olean; 38460 Plattsburgh; 40380 Rochester; 45060 Syracuse; 46540 Utica-Rome. **No NYC or Long Island metro division** is listed. The only NY-metro division on the list is 29484 Lakewood-New Brunswick, NJ [C1, H] | None (mandatory). Participant list already final for PY2027 [C1, H] | Performance Jan 1, 2027 to Dec 31, 2031; payment years Jan 1, 2029 to Dec 31, 2033 [C1, H] | At least 20 attributed HF or LBP episodes per year (CMS page) / 20 Medicare patients over 12 months (fact sheet). Payment adjustment −9% to +9% in payment year 1, rising to 12% by PY5 (secondary) [C1, H for threshold and 9%; L for 12%] | **UNCLEAR**: applies only if the IPA's cardiologists or LBP specialists practice in one of the 11 upstate CBSAs and meet the 20-episode threshold. Resolve by checking TIN-NPIs against the ASM participant dataset on data.cms.gov. Not applicable if the Client is NYC or Long Island based. |
| 4 | **LEAD** (Long-term Enhanced ACO Design) | **Established (RFA issued)**: RFA Mar 31, 2026, revised Apr 15, 2026. CMS website: "Announced" [C1, H] | Voluntary [C1, H] | Participant = **ACO legal entity with its own TIN**. Participant TINs (whole-TIN) can include PGPs, "networks of individual practices," hospitals employing practitioners, FQHCs, RHCs, and CAHs. **IPA**: can form or sponsor an ACO legal entity, or join one as Participant TIN(s). **Hospital**: can join as a Participant TIN or as a Preferred Provider [C1, H] | National. NY eligible [C1, H] | **PY2027 window closed** (Mar 31 to May 17, 2026). CMS "anticipates offering additional application windows for subsequent Performance Years." A non-binding Letter of Interest is available [C1, H] | Jan 1, 2027 to Dec 31, 2036. Optional Implementation Period Sep 15 to Dec 31, 2026 [C1, H] | At least 5,000 aligned beneficiaries plus 3,000 claims-aligned in a base year. Lower, phased-in minimums for Newly Entering ACOs and for High Needs/ESRD-heavy ACOs (at least 40% High Needs/ESRD) [C1, H] | **ELIGIBLE** (participant type fits). Direct entry for 2027 is closed. Options are joining an existing LEAD ACO as Participant TINs (deadline for TIN-list changes not confirmed) or applying directly in a future cohort (timing unannounced). Mutually exclusive with MSSP at the TIN level. |
| 5 | **ACO REACH** | **Established** (operating; final PY) [C1, H] | Voluntary [C1, H] | ACOs (Standard, New Entrant, High Needs) [C1, H] | National [C1, H] | **None**: "will not be accepting new applications for the remaining model duration" [C1, H] | 2023 to Dec 31, 2026 (PY2026 is final PY) [C1, H] | n/a | **INELIGIBLE**: closed and ending. Successor is LEAD. |
| 6 | **EOM** (Enhancing Oncology Model) | **Established** (Active) [C1, H] | Voluntary [C1, H] | Oncology **PGPs** (TIN) and payers. Hospital, IPA, ACO: not named as participants [C1, H] | National. **No NY state in CMS's EOM participant-state list** [C1, H] | **None open, none announced**. Last intake (Cohort 2 start Jul 1, 2025; application Jul to Sep 2024 per pre-plan, secondary) is historical [C1, M] | Cohort 1 Jul 1, 2023; Cohort 2 Jul 1, 2025; both end **Jun 30, 2030** [C1, H] | 6-month episodes, 7 cancer types; MEOS $110 PBPM ($140 duals) [C1, H] | **INELIGIBLE (no window)**: an oncology PGP is the right type, but there is no intake path. Resolve only if CMS announces a Cohort 3 (none found). |
| 7 | **ACCESS** (Advancing Chronic Care with Effective, Scalable Solutions) | **Established** (Active; 160+ participants) [C1, H] | Voluntary [C1, H] | Medicare **Part B-enrolled organizations** (excluding DMEPOS and labs) with a Medicare-enrolled Medical/Clinical Director. TIN-level (secondary AAMC). PGP: **yes**. Hospital: only via a Part B-enrolled entity. IPA: only if Part B-enrolled. ACO: not a participant type; ACO practices can join individually [C1, M] | National (Original Medicare); rural adjustment [C1, H] | **Open, rolling** ("reviewed on a rolling basis"); rolling start dates. New tracks start Apr 1, 2027 [C1, M] | **Jul 5, 2026** (CMS) vs Jul 1, 2026 (AAMC, secondary); 10 years (to ~2036) [C1, M; conflict noted] | Outcome-aligned payments; target attainment threshold rises each year (values in CMS "Payment Amounts and Performance Targets" PDF, not reviewed) [C1, M] | **ELIGIBLE**: via a Part B-enrolled member PGP TIN or a Client-controlled enrolled entity. The IPA itself is eligible only if it is a Medicare Part B-enrolled organization. |
| 8 | **AHEAD** (Achieving Healthcare Efficiency through Accountable Design): Hospital Global Budgets, Primary Care AHEAD, **Geo AHEAD** | **Established** (Active state model; NY in Cohort 3). Geo AHEAD components **announced** (specs previewed; RFA due Q1 2027) [C1, H] | Voluntary [C1, H] | **State** is the model participant. **Hospitals** in the NY sub-state region can join Hospital Global Budgets (voluntary). **Primary care practices** can join PC AHEAD (NY: must be in NYS PCMH program; hospital-owned practices only if parent hospital is in HGB). **Geo Entities** can be "provider-led organizations, ... health plans, hospitals, or other entities." An IPA-sponsored ACO could bid, and provider-led Geo Entities can bid on a sub-state division [C1, H for CMS; M for NY DOH] | **NY included as a sub-state region ("downstate New York")**. NY DOH: Bronx, Kings, Queens, Richmond, Westchester counties. **Not** New York County (Manhattan), Nassau, Suffolk, or upstate [C1, H that NY is included; M for county list] | Geo Entity RFA: **Q1 2027** (bid for 2028–2031). Geo specs "Summer 2026". Geo AHEAD webinar Oct 20, 2026. HGB/PC AHEAD application dates for NY: not found [C1, M] | Cohort 2/3 performance period begins **Jan 1, 2028**; all cohorts end **Dec 31, 2035** [C1, H] | Geo Entity: CMS targets at least 20,000 attribution-eligible per sub-state division and at least 10,000 per Geo Entity; at least 3 Geo Entities in the NY sub-state region, or Geo AHEAD does not operate there in PY1 [C1, H] | **UNCLEAR**: highly relevant if the hospital is in, or the IPA's practices are in, Bronx, Kings, Queens, Richmond, or Westchester; otherwise INELIGIBLE. Resolve by confirming the Client's counties and the final NY sub-state definition in the CMS–NY State Agreement. |
| 9 | **IOTA** (Increasing Organ Transplant Access) | **Established** (Active; PY2 changes in Jun 1, 2026 final rule) [C1, H] | Mandatory [C1, H] | Kidney transplant **hospitals** (adult) in selected DSAs. IPA, ACO, PGP: no [C1, H] | Half of DSAs. **NY DSAs included: NYRT (NYC/LI/Westchester), NYWN (Western NY), NYFL (Finger Lakes)**. 13 NY transplant hospitals are listed [C1, H] | None (mandatory) [C1, H] | Jul 1, 2025 to Jun 30, 2031 (6 PYs); downside risk from PY2 (Jul 1, 2026) [C1, H] | At least 15 kidney transplants per year in each of 3 baseline years (CMS page). AAMC Jan 2026 (secondary) says 11, with a proposal to raise to 15 [C1, H for 15 as current] | **UNCLEAR**: applies only if the affiliated hospital runs a qualifying adult kidney transplant program. Resolve by checking the CMS IOTA participant/DSA list. |
| 10 | **WISeR** (Wasteful and Inappropriate Service Reduction) | **Established** (Active) [C1, H] | Mandatory for providers in model states (prior auth or pre-payment review); participants are tech vendors [C1, H] | Participants = 6 technology vendors. Providers are affected, not participants [C1, H] | AZ, NJ, OH, OK, TX, WA. **NY not included**; no expansion mentioned [C1, H] | n/a | Jan 1, 2026 to Dec 31, 2031 [C1, H] | n/a | **INELIGIBLE / not applicable** (NY not a WISeR state). NJ-based IPA sites would be affected. |
| 11 | **KCC** (Kidney Care Choices) | **Established** (Active; 73 KCEs; NY among participant states) [C1, H] | Voluntary [C1, H] | Kidney Contracting Entities (nephrologists plus transplant providers); KCF = nephrology practices [C1, H] | National [C1, H] | **None**: "does not plan further solicitations." KCF open only through end of 2025 [C1, H] | 2022 to end of 2027 (extended) [C1, H] | n/a | **INELIGIBLE** (no window). Join only through an existing KCE (nephrology practices). |
| 12 | **GUIDE** (dementia) | **Established** (Active; 292 participants; NY among states) [C1, H] | Voluntary [C1, H] | Part B-enrolled providers/suppliers that run dementia care programs; can contract Partner Organizations [C1, H] | National [C1, H] | **None found** (page does not mention any open or future window) [C1, M] | Jul 1, 2024 for 8 years (to ~Jun 30, 2032, inferred) [C1, M] | n/a | **INELIGIBLE (no window)**. Resolve if CMS announces another cohort. |
| 13 | **MAHA ELEVATE** | **Announced** (NOFO/cooperative agreement; CMS: "Announced") [C1, H] | Voluntary (grant-like cooperative agreements) [C1, H] | Private medical practices, health systems, ACOs, FQHCs/RHCs, CBOs, and others. **PGP: yes; health system: yes; ACO: yes; IPA: not named** [C1, H] | National [C1, H] | Cohort 1 **closed May 15, 2026**. Cohort 2 starts 2027, **window not posted** [C1, H] | Cohort 1 from Sep 1, 2026 (3-yr agreements); about $100M for up to 30 awards [C1, H] | Must include nutrition or physical activity; 3 awards reserved for dementia [C1, H] | **UNCLEAR**: the participant type fits, but cohort 2 timing is unknown. Resolve when the cohort 2 NOFO posts. Small grant ($100M across 30 awards), not a payment model. |
| 14 | **ACO PC Flex** (ACO Primary Care Flex) | **Established** (Active; 23 ACOs) [C1, H] | Voluntary [C1, H] | Low-revenue MSSP ACOs only [C1, H] | National [C1, H] | **None**: "does not intend to offer another round of applications" [C1, H] | Jan 1, 2025 to 2029 [C1, H] | n/a | **INELIGIBLE** (closed). |
| — | **MSSP** (Medicare Shared Savings Program): **non-CMMI baseline row** | Established (statutory, §1899) | Voluntary | ACO legal entity; IPA-sponsored ACOs, hospital-led ACOs, and PGP-led ACOs are all common forms. Joining an existing ACO as a Participant TIN is the usual "join through another organization" route [C1, M] | National | Jan 1, 2027 start: Phase 1 submission **closed** (Jun 9–23, 2026); final disposition Oct 15, 2026. Next new-ACO window expected mid-2027 for a Jan 1, 2028 start (inference). Joining an existing MSSP ACO depends on that ACO's participant-list change deadlines [C1, M] | Agreement periods (5 yr) | CY2027 PFS proposed rule (CMS-1848-P, Jul 14, 2026; comments closed Sep 14, 2026) would raise BASIC Level E sharing to 60%, end prepaid shared savings after the 2027 cycle, add a growth adjustment for recruiting inexperienced clinicians, and more [C1, H] | **ELIGIBLE (baseline)**: direct (form an ACO) or through an existing ACO. Cannot be combined with LEAD or Geo AHEAD for the same TIN/beneficiaries. |

Other models in the CMS dataset that this card checked and ruled out are listed in (c) below.

### (b) Notes on ELIGIBLE and UNCLEAR models (up to 5 lines each)

**TEAM (UNCLEAR, mandatory for the hospital if in a selected CBSA)**
- The CMS TEAM participant list (dated Aug 18, 2026) lists 65 NY-state hospitals in CBSA 35620, 8 in 15380 Buffalo-Cheektowaga, 2 in 36580 Oneonta, and 1 each in 12860 Batavia, 18660 Cortland, and 32390 Massena-Ogdensburg [C1, H]. Source: [CMS TEAM participant list](https://www.cms.gov/team-model-participant-list)
- The participant is the hospital only. The IPA's role is as a downstream "TEAM collaborator" or care partner for post-acute and episode management. The TEAM collaborator list was not verified in primary text this round (see Gaps) [C1, L].
- TEAM hospitals are excluded from CJR-X until TEAM ends, then move into CJR-X on Jan 1, 2031 [C1, H]. Source: [FY2027 IPPS final rule, 91 FR 49570](https://www.govinfo.gov/content/pkg/FR-2026-08-04/html/2026-15833.htm)
- The FY2027 IPPS final rule adds 3 spinal-fusion MS-DRGs (triggering Oct 1, 2026) and updates target prices and normalization. No evidence was found of a change to the CBSA list (secondary) [C1, L].
- Positioning for a TEAM hospital: the PY1 (2026) episode window is live now. The IPA's leverage is in post-discharge management and gainsharing arrangements.

**CJR-X (ELIGIBLE, mandatory for the hospital)**
- Mandatory nationwide from Jan 1, 2028, for IPPS-and-OPPS hospitals not in TEAM and not in Maryland. CMS projects more than 2,500 hospitals (secondary: Holland & Knight, AHCA) [C1, H]. Sources: [CMS CJR-X page](https://www.cms.gov/priorities/innovation/innovation-models/cjr-x); [CMS FY2027 IPPS fact sheet](https://www.cms.gov/newsroom/fact-sheets/fy-2027-hospital-inpatient-prospective-payment-system-long-term-care-hospital-prospective-payment)
- The start was moved from the proposed Oct 1, 2027 to Jan 1, 2028, and performance years were finalized on a calendar-year basis [C1, H]. Source: [91 FR 49570](https://www.govinfo.gov/content/pkg/FR-2026-08-04/html/2026-15833.htm)
- The model has no fixed end date. Commenters called this unlawful, and CMS disagreed [C1, H].
- The finalized CJR-X collaborator list includes physician group practice, physician, nonphysician practitioner, hospital, and "Medicare Accountable Care Organization." This is the formal hook for an IPA, or an IPA-sponsored ACO, to share in hospital gains [C1, H].
- Low-volume hospitals (fewer than 31 LEJR episodes in baseline) remain participants but are excluded from reconciliation, so they carry no upside or downside [C1, M].

**ASM (UNCLEAR, mandatory for individual specialists in selected CBSAs)**
- NY coverage is upstate only (11 CBSAs). An IPA based in NYC or Long Island has **no** ASM exposure unless its specialists also practice in a listed CBSA. The geography is defined on OMB 2023 delineations [C1, H]. Source: [ASM mandatory geographic areas (xlsx)](https://www.cms.gov/priorities/innovation/files/asm-mandatory-geo-areas.xlsx)
- Final PY2027 participants are published. Check TIN-NPIs in the [ASM participant dataset](https://data.cms.gov/cms-innovation-center-programs/disease-episode-based-payment-models/ambulatory-specialty-model-participants) [C1, H].
- Scoring is individual for quality and cost, and group (TIN) for improvement activities and PI. Adjustments are −9% to +9% in payment year 1 (2029) [C1, H]. Source: [ASM fact sheet](https://www.cms.gov/files/document/asm-model-fact-sheet.pdf)
- The CY2027 PFS proposed-rule fact sheet does not mention ASM changes [C1, M]. ASM is reportedly **not** an Advanced APM (secondary, truncated) [C1, L].
- Whether ACO/LEAD participation or QP status exempts a specialist from ASM was **not resolved** (see Gaps).

**LEAD (ELIGIBLE; 2027 direct window closed; future cohorts expected)**
- RFA: the portal was open Mar 31 to May 17, 2026 (11:59 pm ET). ACO REACH PY2026 ACOs could file an abbreviated application [C1, H]. Source: [LEAD RFA (rev. Apr 15, 2026)](https://www.cms.gov/priorities/innovation/files/lead-rfa.pdf)
- "CMS anticipates offering additional application windows for subsequent Performance Years." Organizations not ready can file a non-binding LOI, and LOI filers are notified when windows open [C1, H].
- 79 ACOs are in the optional Implementation Period (Sep 15 to Dec 31, 2026). CMS is "working with well over 100 ACOs" for PY2027, which "have until mid-December to finalize participation" [C1, H]. Source: [LEAD IP participant list, Sep 21, 2026](https://www.cms.gov/priorities/innovation/files/lead-imp-participant-list.pdf)
- Risk options: Global (up to 100% savings/losses) or Professional (up to 50%). CARA lets ACOs set episode-based risk arrangements with specialists (Global track only, per AAMC secondary) [C1, H/M].
- The overlap rule bars simultaneous MSSP participation at the TIN level. LEAD is CMS's stated successor to ACO REACH [C1, H]. Source: [CMS LEAD page](https://www.cms.gov/priorities/innovation/innovation-models/lead)

**ACCESS (ELIGIBLE via a Part B-enrolled TIN)**
- Applications are "reviewed on a rolling basis" with rolling start dates. New tracks (heart failure, COPD, SUD, tobacco cessation, MSK follow-on) begin Apr 1, 2027 [C1, M]. Source: [CMS ACCESS page](https://www.cms.gov/priorities/innovation/innovation-models/access)
- Tracks: eCKM, CKM, MSK, and behavioral health. Outcome-aligned payments replace visit-based FFS for model patients' conditions (participants are precluded from billing the PFS for those patients, per AAMC secondary) [C1, M].
- PCPs who refer and co-manage get a co-management G-code (about $30, max $100/yr, per AAMC secondary). This is a low-lift role for IPA PCPs even if the IPA is not a participant [C1, L].
- The start date conflicts: CMS says Jul 5, 2026; AAMC says Jul 1, 2026 [C1, M].
- Whether the IPA entity itself (as opposed to member TINs) is Part B-enrolled determines whether the IPA can be the direct participant.

**AHEAD / Geo AHEAD (UNCLEAR; location-dependent; potentially the largest NY-specific opportunity)**
- CMS: AHEAD has 5 states. Cohort 3 is Rhode Island and **New York**. The Cohort 2/3 performance period begins Jan 1, 2028, and all cohorts end Dec 31, 2035 (changes announced Sep 2025) [C1, H]. Source: [CMS AHEAD page](https://www.cms.gov/priorities/innovation/innovation-models/ahead)
- CMS Geo AHEAD preview: "As of Q1 2026, substate region only applies to New York state" ("downstate New York"). The Geo Entity RFA is expected **Q1 2027**, with bids covering 2028–2031. Provider-led Geo Entities may bid on a sub-state division. There will be at least 3 Geo Entities in the NY sub-state region and at least 10,000 attribution-eligible beneficiaries per Geo Entity [C1, H]. Source: [Geo AHEAD Specification Preview: Geo Entity and Bidding](https://www.cms.gov/priorities/innovation/files/ahead-geo-spec-prv-entity-bidding.pdf)
- NY DOH: the five counties are Bronx, Kings, Queens, Richmond, and Westchester. "Any hospital located in these counties can participate" in Hospital Global Budgets. PC AHEAD requires NYS PCMH participation [C1, M]. Source: [NY DOH AHEAD page](https://www.health.ny.gov/health_care/medicaid/redesign/med_waiver_1115/ahead/) (403 on direct fetch; content via search extract)
- Overlap: no beneficiary overlap is allowed between Geo AHEAD and MSSP, PC Flex, ACO REACH, or LEAD. A Geo Participant TIN cannot be in another ACO model. This forces a choice between LEAD/MSSP and Geo AHEAD for in-region TINs [C1, H].
- The CMS AHEAD participant list (xlsx) currently shows only Maryland participants (2026 start). No NY hospitals or practices are listed yet [C1, H].

**IOTA (UNCLEAR; only for a kidney transplant hospital)**
- NY DSAs NYRT, NYWN, and NYFL are in the model. 13 NY kidney transplant hospitals are on the CMS list [C1, H]. Source: [IOTA participant/DSA list](https://www.cms.gov/priorities/innovation/files/iota-participant-dsa-list.xlsx)
- If the affiliated hospital has no adult kidney transplant program, IOTA is not applicable (INELIGIBLE).

**MAHA ELEVATE (UNCLEAR; cohort 2 timing)**
- The cohort 1 application deadline was May 15, 2026 (closed). Awards are expected Fall 2026. The second cohort starts 2027, with no NOFO date posted [C1, H]. Source: [CMS MAHA ELEVATE page](https://www.cms.gov/priorities/innovation/innovation-models/maha-elevate)
- Eligible applicants include private medical practices, health systems, and ACOs. Awards are cooperative agreements, not a payment model.

**MSSP baseline (ELIGIBLE)**
- 2027-start Phase 1 ran Jun 9–23, 2026, and final disposition is Oct 15, 2026 [C1, H]. Source: [CMS MSSP Application Types & Timeline](https://www.cms.gov/medicare/payment/fee-for-service-providers/shared-savings-program-ssp-acos/application-types-timeline)
- CY2027 PFS proposals (CMS-1848-P) include: BASIC Level E sharing raised to 60%; prepaid shared savings ending; a growth adjustment for recruiting inexperienced clinicians; "Legacy" CMMI-ACO TINs no longer counted as risk-experienced without a written risk agreement [C1, H]. Source: [CMS CY2027 PFS proposed rule MSSP fact sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-medicare-physician-fee-schedule-proposed-rule-cms-1848-p-medicare-shared)

### (c) Ruled out and why
- **ACO REACH**: no new applications; final PY ends Dec 31, 2026 [C1, H]. [CMS ACO REACH page](https://www.cms.gov/priorities/innovation/innovation-models/aco-reach)
- **EOM**: no open or announced intake; ends Jun 30, 2030. No NY state in its participant-state list [C1, H]. [CMS EOM page](https://www.cms.gov/priorities/innovation/innovation-models/enhancing-oncology-model)
- **KCC**: no further solicitations; ends 2027 [C1, H]. [CMS KCC page](https://www.cms.gov/priorities/innovation/innovation-models/kidney-care-choices-kcc-model)
- **ACO PC Flex**: no further application rounds; limited to low-revenue MSSP ACOs [C1, H]. [CMS ACO PC Flex page](https://www.cms.gov/priorities/innovation/innovation-models/aco-primary-care-flex-model)
- **GUIDE**: no open or future window found [C1, M]. [CMS GUIDE page](https://www.cms.gov/priorities/innovation/innovation-models/guide)
- **WISeR**: NY is not a model state [C1, H]. [CMS WISeR page](https://www.cms.gov/priorities/innovation/innovation-models/wiser)
- **Drug-pricing models (GLOBE, GUARD, GENEROUS, BALANCE, CGT Access)**: participants are manufacturers, states, or Part D plans. GLOBE affects Part B allowed amounts in selected areas but has no provider participant role [C1, H]. [CMS model dataset](https://data.cms.gov/data-api/v1/dataset/0d753f51-c3de-43cd-95d2-550a23b8606a/data)
- **State Medicaid/child models (InCK [NY listed], TMaH, ASPIRE, IBH [NY is one of 3 states])**: state-led. Practice participation in IBH NY is via state selection, not open to an IPA application. InCK is ending (2020–2026) [C1, M]. [CMS model dataset](https://data.cms.gov/data-api/v1/dataset/0d753f51-c3de-43cd-95d2-550a23b8606a/data); [CMS Mar 12, 2025 fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-innovation-center-announces-model-portfolio-changes-better-protect-taxpayers-help-americans-live)
- **Expanded HHVBP**: applies to home health agencies nationally (relevant only if the hospital owns an HHA; not an IPA/hospital model) [C1, H].
- **Radiation Oncology Model**: still shown as "Announced" in the CMS dataset, but described as "proposed" and never implemented (historical) [C1, M].
- **Ended early by Dec 31, 2025: Making Care Primary (NY was an MCP state), Primary Care First, ESRD Treatment Choices, Maryland TCOC**. Statuses are now "Performance Period Ended" [C1, H]. [CMS Mar 12, 2025 fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-innovation-center-announces-model-portfolio-changes-better-protect-taxpayers-help-americans-live)
- **BPCI Advanced and CJR (original)**: BPCI-A is "Not Active." CJR ended Dec 31, 2024 and has been succeeded by CJR-X [C1, H]. [CMS model dataset](https://data.cms.gov/data-api/v1/dataset/0d753f51-c3de-43cd-95d2-550a23b8606a/data)

### (d) Gaps
- **TEAM selected-CBSA list in rule text** (FY2025 IPPS final rule, Table X.A.-07) was not opened. The NY CBSA list above is derived from the CMS participant list (CBSAs with at least one listed hospital). A selected NY CBSA with no eligible hospital would not appear.
- **TEAM collaborator definition** (whether it includes PGPs and Medicare ACOs, as CJR-X does) was not verified in primary text.
- **ASM exemptions**: whether QPs or Advanced APM/ACO (LEAD, MSSP) participants are excluded from ASM was not found in primary sources.
- **LEAD**: there is no announced date for the PY2028 application window. The deadline for adding Participant TINs to an existing LEAD ACO for PY2027 was not found beyond "mid-December" finalization.
- **AHEAD NY**: application or NOFO dates for NY Hospital Global Budgets and PC AHEAD were not found. The NY sub-state county list rests on the NY DOH page (primary state source, but not directly fetchable: 403). The CMS–NY State Agreement text was not reviewed.
- **ACCESS**: whether an IPA (non-billing) entity can enroll as a Part B organization for ACCESS, and the specific outcome thresholds, were not checked.
- **KCC successor**: none named by CMS.
- **GLOBE status**: CMS dataset says "Active"; AAMC (Jan 2026, secondary) described it as proposed. The final rule was not checked (not material to the Client).

### Cited Findings
- The CMS model dataset lists 20 Active and 8 Announced models. Announced: Radiation Oncology, ASM, GENEROUS, MAHA ELEVATE, LEAD, GUARD, ASPIRE, CJR-X [C1, H]. [data.cms.gov Innovation Center Model Summary Information](https://data.cms.gov/data-api/v1/dataset/0d753f51-c3de-43cd-95d2-550a23b8606a/data); the [data.gov catalog](https://catalog.data.gov/dataset/innovation-center-model-summary-information-2026-09-24) shows a 2026-09-24 version.
- Secondary overview (AAMC, Jan 29, 2026): in 2025 CMMI made 9 new models, 4 early terminations (MD TCOC, MCP, PCF, ETC), and 5 modifications (TEAM, AHEAD, IOTA, CGT Access, plus one other) [C1, M, secondary]. [AAMC CMMI Model Updates slides](https://www.aamc.org/media/88796/download?attachment=)
- CMS (Mar 12, 2025) aimed to end MD TCOC, PCF, ETC (via rulemaking), and MCP "by December 31, 2025." It dropped the $2 Drug List and Accelerating Clinical Evidence models [C1, H]. [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-innovation-center-announces-model-portfolio-changes-better-protect-taxpayers-help-americans-live)
- No new CMMI provider model announced Jun to Oct 2026 was found. Searches returned only late-2025 announcements and 2026 implementation milestones [C1, M].

### Inferences
- For the hospital, episode accountability is unavoidable: TEAM now if it is in a selected CBSA, otherwise CJR-X from 2028. The IPA's realistic role in both is collaborator or gainsharing partner, not participant.
- The IPA's main voluntary total-cost-of-care decision is **LEAD vs. MSSP vs. (if downstate) Geo AHEAD**. These are mutually exclusive at the TIN or beneficiary level, so sequencing matters. The LEAD PY2028 window and the Geo AHEAD RFA (Q1 2027) could both fall in roughly the same 2027 timeframe (timing of the LEAD window is not announced).

### Gaps
- See (d) above.

---

## Q2. For geography-selected mandatory models, which New York CBSAs (or other units) are included?

### Takeaway
TEAM covers 6 NY CBSAs, including the NYC metro and Buffalo. ASM covers 11 upstate NY CBSAs and excludes NYC and Long Island. IOTA covers 3 of NY's DSAs. WISeR excludes NY. CJR-X is nationwide (every NY IPPS hospital not in TEAM). AHEAD (voluntary) covers a 5-county downstate sub-state region [C1, H].

### Cited Findings
- **TEAM NY CBSAs** (hospitals with CBSA State = NY on the Aug 18, 2026 list): 35620 New York-Newark-Jersey City, NY-NJ (65 NY hospitals); 15380 Buffalo-Cheektowaga (8); 36580 Oneonta (2); 12860 Batavia (1); 18660 Cortland (1); 32390 Massena-Ogdensburg (1). There are 722 rows in total, 179 CBSAs with mandatory hospitals, and 10 voluntary participants (none in NY) [C1, H]. [CMS TEAM participant list (xlsx)](https://www.cms.gov/team-model-participant-list)
- TEAM: "Hospitals paid under IPPS in selected CBSAs must participate." The CBSA list was published in the FY2025 IPPS final rule [C1, H]. [CMS TEAM page](https://www.cms.gov/priorities/innovation/innovation-models/team-model)
- Conflict on TEAM CBSA count: AAMC (secondary) says 188 selected CBSAs; LeadingAge (secondary) says 743 hospitals in 187 CBSAs; PYA (secondary) says "118"; the current CMS list shows 179 CBSAs with mandatory hospitals. Not resolved [C1, L]. [AAMC slides](https://www.aamc.org/media/88796/download?attachment=); [LeadingAge](https://leadingage.org/cms-list-743-hospitals-required-to-participate-in-team/); [PYA](https://www.pyapc.com/?p=37281)
- **ASM NY CBSAs**: 10580 Albany-Schenectady-Troy; 15380 Buffalo-Cheektowaga; 27460 Jamestown-Dunkirk; 28740 Kingston; 28880 Kiryas Joel-Poughkeepsie-Newburgh; 32390 Massena-Ogdensburg; 36460 Olean; 38460 Plattsburgh; 40380 Rochester; 45060 Syracuse; 46540 Utica-Rome. The list's metropolitan divisions include none for New York City or Nassau-Suffolk. The only NY-metro division is 29484 Lakewood-New Brunswick, NJ. The file has 235 areas in total [C1, H]. [ASM mandatory geographic areas](https://www.cms.gov/priorities/innovation/files/asm-mandatory-geo-areas.xlsx)
- **IOTA NY DSAs**: NYRT, NYWN, and NYFL (13 NY transplant hospitals) [C1, H]. [IOTA participant/DSA list](https://www.cms.gov/priorities/innovation/files/iota-participant-dsa-list.xlsx)
- **WISeR**: NJ, OH, OK, TX, AZ, and WA only [C1, H]. [CMS WISeR page](https://www.cms.gov/priorities/innovation/innovation-models/wiser)
- **CJR-X**: all acute-care hospitals in the 50 states, DC, and territories except TEAM and Maryland hospitals [C1, H]. [91 FR 49570](https://www.govinfo.gov/content/pkg/FR-2026-08-04/html/2026-15833.htm)
- **AHEAD (voluntary)**: NY sub-state region = "downstate New York" (CMS), comprising Bronx, Kings, Queens, Richmond, and Westchester (NY DOH) [C1, H/M]. [Geo AHEAD preview](https://www.cms.gov/priorities/innovation/files/ahead-geo-spec-prv-entity-bidding.pdf); [NY DOH AHEAD](https://www.health.ny.gov/health_care/medicaid/redesign/med_waiver_1115/ahead/); secondary corroboration: [Crain's NY](https://www.crainsnewyork.com/health-pulse/downstate-counties-selected-ahead/)

### Inferences
- A Manhattan, Bronx, Brooklyn, Queens, Staten Island, Westchester, or Long Island Client has TEAM exposure (CBSA 35620) but **no** ASM exposure. An upstate Client in Buffalo has both. Albany, Rochester, or Syracuse Clients have ASM but not TEAM, and their hospital enters CJR-X in 2028.
- Manhattan, Nassau, and Suffolk sit inside TEAM's CBSA 35620 but outside the AHEAD downstate counties.

### Gaps
- The TEAM rule-text CBSA table was not opened (see Q1 gaps). ASM uses OMB 2023 delineations while TEAM uses the delineation in the FY2025 rule. CBSA codes and names may differ between the two (e.g., ASM's "Kiryas Joel-Poughkeepsie-Newburgh").

---

## Q3. Can an IPA, ACO, CIN, PGP/TIN, or hospital be the direct participant in each model?

### Takeaway
Hospitals are the direct participant only in TEAM, CJR-X, IOTA, and AHEAD Hospital Global Budgets. ACO legal entities are the participant in LEAD, MSSP, and Geo AHEAD (an IPA can sponsor that entity). PGP TINs or Part B-enrolled organizations are the participant in ACCESS, EOM, and GUIDE. ASM attaches to individual TIN-NPIs. No model names an "IPA" or "CIN" as a participant type. An IPA participates by sponsoring an ACO legal entity or through member TINs [C1, H].

### Cited Findings
- LEAD: "An ACO must be a legal entity identified by a federal [TIN]." Participant TIN types include "Physicians or other practitioners in group practice arrangements," "Networks of individual practices of physicians," and "Hospitals employing physicians," with whole-TIN participation [C1, H]. [LEAD RFA](https://www.cms.gov/priorities/innovation/files/lead-rfa.pdf)
- Geo Entities "can be provider-led organizations, technology/digital health companies, health plans, hospitals, or other entities." HGB hospitals can be Geo Participants. Geo Participant TINs may not be in other CMS ACO programs [C1, H]. [Geo AHEAD preview](https://www.cms.gov/priorities/innovation/files/ahead-geo-spec-prv-entity-bidding.pdf)
- CJR-X collaborators include PGPs, hospitals, and "Medicare Accountable Care Organization" [C1, H]. [91 FR 49570](https://www.govinfo.gov/content/pkg/FR-2026-08-04/html/2026-15833.htm)
- ASM participants are "individual specialists, identified by TIN and NPI" [C1, H]. [CMS ASM page](https://www.cms.gov/priorities/innovation/innovation-models/asm)
- ACCESS participants are Medicare Part B-enrolled organizations (excluding DMEPOS and labs) with a Medicare-enrolled Medical Director [C1, M]. [CMS ACCESS page](https://www.cms.gov/priorities/innovation/innovation-models/access)
- EOM participants are PGPs (23) and one payer [C1, H]. [CMS EOM page](https://www.cms.gov/priorities/innovation/innovation-models/enhancing-oncology-model)
- MAHA ELEVATE: private medical practices, health systems, ACOs, and others [C1, H]. [CMS MAHA ELEVATE page](https://www.cms.gov/priorities/innovation/innovation-models/maha-elevate)

### Inferences
- If the IPA is a non-billing contracting entity (typical in NY), it cannot itself be a Part B-enrolled participant in ACCESS, EOM, or GUIDE. It would act through member TINs or a new enrolled entity. It can be the sponsor or legal entity for a LEAD, MSSP, or Geo AHEAD ACO.

### Gaps
- No CMS source addresses "IPA" or "CIN" by name. The treatment of a NY Article 44/IPA-licensed entity as an ACO legal entity is a legal question outside this card.

---

## Q4. Which application windows are open now or expected?

### Takeaway
Open now: **ACCESS (rolling)** only. Recently closed: LEAD PY2027 (May 17, 2026), MSSP 2027 Phase 1 (Jun 23, 2026), MAHA ELEVATE cohort 1 (May 15, 2026). Expected: **Geo AHEAD Geo Entity RFA in Q1 2027**; **LEAD future cohorts** (anticipated, undated; an LOI is available now); **MAHA ELEVATE cohort 2** (2027, undated); **MSSP Jan 1, 2028 cycle** (inferred mid-2027). No window exists or is expected for EOM, ACO REACH, KCC, or ACO PC Flex [C1, H/M].

### Cited Findings
- LEAD portal: Mar 31 to May 17, 2026, 11:59 pm ET. Additional windows are anticipated. CMS committed to release an LOI form "no later than April 20, 2026" [C1, H]. [LEAD RFA](https://www.cms.gov/priorities/innovation/files/lead-rfa.pdf)
- LEAD: 79 ACOs are in the Implementation Period, and ACOs "have until mid-December to finalize participation" for PY2027 [C1, H]. [LEAD IP list](https://www.cms.gov/priorities/innovation/files/lead-imp-participant-list.pdf)
- ACCESS: rolling review. New tracks start Apr 1, 2027 [C1, M]. [CMS ACCESS page](https://www.cms.gov/priorities/innovation/innovation-models/access)
- Geo AHEAD: Geo Entity RFA in Q1 2027. A Geo AHEAD Technical Specifications Webinar is set for Oct 20, 2026 [C1, H]. [Geo AHEAD preview](https://www.cms.gov/priorities/innovation/files/ahead-geo-spec-prv-entity-bidding.pdf); [CMS AHEAD page](https://www.cms.gov/priorities/innovation/innovation-models/ahead)
- MAHA ELEVATE: cohort 1 closed May 15, 2026; cohort 2 begins 2027 [C1, H]. [CMS MAHA ELEVATE page](https://www.cms.gov/priorities/innovation/innovation-models/maha-elevate)
- MSSP: Phase 1 ran Jun 9–23, 2026; final disposition Oct 15, 2026 [C1, M] (via search extract of [CMS timeline page](https://www.cms.gov/medicare/payment/fee-for-service-providers/shared-savings-program-ssp-acos/application-types-timeline)).
- ACO REACH: "will not be accepting new applications" [C1, H]. KCC: "does not plan further solicitations" [C1, H]. ACO PC Flex: "does not intend to offer another round" [C1, H].

### Inferences
- If the Client wants to be a direct LEAD applicant, it should file the LEAD LOI now so it is notified of the PY2028 window. If it wants 2027 participation, the only route is to join an existing LEAD ACO's Participant TIN list before the mid-December 2026 finalization (to be confirmed with that ACO).

### Gaps
- No primary date for the LEAD PY2028 window, MAHA ELEVATE cohort 2, the MSSP 2028 cycle, or NY HGB/PC AHEAD applications.

---

## Q5. Which models are ending, and what are their successors?

### Takeaway
ACO REACH ends Dec 31, 2026, and its successor is LEAD (Jan 1, 2027 to Dec 31, 2036). CJR ended Dec 31, 2024, and its successor is CJR-X (Jan 1, 2028, no fixed end). TEAM (to 2030) feeds into CJR-X in 2031 for LEJR. KCC ends 2027 with no named successor. EOM ends Jun 30, 2030 with no successor named. MCP, PCF, ETC, and MD TCOC were ended early by Dec 31, 2025 with no direct primary-care successor model. CMS pointed to "other regulatory options" [C1, H/M].

### Cited Findings
- LEAD is "a successor to the ACO REACH Model," which "concludes at the end of 2026" (CMS LEAD page). The ACO REACH page itself does not state the successor and says PY2026 is the final PY [C1, H]. [CMS LEAD page](https://www.cms.gov/priorities/innovation/innovation-models/lead); [CMS ACO REACH page](https://www.cms.gov/priorities/innovation/innovation-models/aco-reach)
- CJR "ended on December 31, 2024." CJR-X is "the first nationwide test of a mandatory episode-based payment model" [C1, H]. [CMS model dataset](https://data.cms.gov/data-api/v1/dataset/0d753f51-c3de-43cd-95d2-550a23b8606a/data)
- TEAM participants become CJR-X participants on Jan 1, 2031 after TEAM ends [C1, H]. [91 FR 49570](https://www.govinfo.gov/content/pkg/FR-2026-08-04/html/2026-15833.htm)
- KCC "has been extended through 2027." No successor is named [C1, H]. [CMS KCC page](https://www.cms.gov/priorities/innovation/innovation-models/kidney-care-choices-kcc-model)
- Early terminations, with CMS saying it "will advise state-specific total cost of care and primary care model participants about other regulatory options for advanced primary care payment" [C1, H]. [CMS Mar 12, 2025 fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-innovation-center-announces-model-portfolio-changes-better-protect-taxpayers-help-americans-live)

### Contradictions surfaced (not resolved)
- **CJR-X and ASM status labels**: the CMS website and dataset say "Announced," but both are finalized in regulation (FY2027 IPPS and CY2026 PFS respectively), which makes them "established" under the card's definition.
- **ACCESS start**: CMS says Jul 5, 2026; AAMC (secondary) says Jul 1, 2026.
- **ACO REACH PY2026 count**: 72 (CMS Model Summary), 74 (CMS page body), and 73 (CMS dataset).
- **IOTA participants**: 103 (Model Summary) vs 95 at the PY2 start (same page). The volume threshold is 15/yr per CMS vs 11 per AAMC (Jan 2026, which described 15 as proposed).
- **AHEAD change announcement date**: Sep 3, 2025 vs Sep 2, 2025 (both on the CMS page).
- **FY2027 IPPS final rule date**: CMS released it Jul 31, 2026; Federal Register publication was Aug 4, 2026.
- **TEAM CBSA count**: 188, 187, 118, or 179 depending on source (see Q2).

### Inferences
- There is no CMMI primary-care-only model open to a NY practice after MCP and PCF ended. Primary-care pathways now run through ACO vehicles (LEAD, MSSP, PC AHEAD/Geo AHEAD in downstate) or ACCESS (condition-specific).

### Gaps
- Successors for KCC and EOM are not named. Whether a BPCI-A successor exists beyond TEAM and CJR-X was not confirmed in primary text (the BPCI-A end date of Dec 31, 2025 rests on the TEAM opt-in language and its "Not Active" status, not on an explicit primary date).
