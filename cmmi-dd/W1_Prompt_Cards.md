# W1 · Prompt Cards: Landscape, EOM, CJR-X, Fit Scaffold

Program: CMMI model due diligence for the Client (IPA + affiliated health system, NYS). Plan date 2026-10-08. Deadline 2026-10-21.
Decision anchor (included in every card): *Voluntary models: join directly, join through a participating organization, or defer/decline, and when. Mandatory models: how to prepare and position.*

## Wave map

| Wave | Cards | Purpose | Target dates |
|---|---|---|---|
| **W1** | C1, C2, C3, C4, P1, P2, P3, P4 | Establish the candidate set; mechanics briefs for EOM and CJR-X; recency checks; rubric scaffold | Run Oct 8–10 · Checkpoint Oct 11 |
| W2 (provisional) | C5 data and reporting crosswalk · C6 model interactions and exclusions · C7 illustrative scenarios · briefs for any models C1 rules in · P-cards from the checkpoint · DR held in reserve | Fit evidence | Oct 12–15 · Checkpoint Oct 16 |
| W3 (provisional) | C8 program synthesis: matrix fill, open-questions list, source index, Evidence Ledger A–D, HTML + PDF | Deliverable | Oct 16–20 |

## Dependency map

| Output | Feeds | How |
|---|---|---|
| C1 landscape | W2 briefs for ruled-in models; C6; matrix columns | Attach C1 output |
| C2 EOM brief | C5, C6, C7, matrix | Attach |
| C3 CJR-X brief | C5, C6, C7, matrix | Attach |
| C4 rubric scaffold | C8 (matrix fill); W2 cards use its criteria as headings | Attach |
| P1 EOM window | C2 cross-check at checkpoint; A2 verdict | Paste summary |
| P2 TEAM/NY + CJR-X overlap | C3 cross-check (deliberate triangulation of a load-bearing fact); A3 verdict | Paste summary |
| P3 EOM participant experience | C2 "results to date"; C7 scenario realism | Attach |
| P4 LEAD / ASM / ACCESS status | C1 cross-check; decides which W2 briefs get written | Paste summary |

No W1 card depends on another W1 output. Where cards overlap (C1 with P4, C3 with P2), the overlap is deliberate triangulation and is scoped to one load-bearing fact.

## Falsification and negative-finding commitments (§7)
- **EOM:** an uncomfortable answer would be: an IPA or ACO cannot be an EOM participant, the Client's oncologists could join only as a TIN-level physician group practice, and no intake window opens before Jun 30, 2030. That makes EOM "closed to new entry: defer, or join via an existing participant only if that is permitted," and we accept it. "No further window announced as of Oct 2026" is a **successful** P1 output, provided it lists what was searched.
- **CJR-X:** an uncomfortable answer would be: the Client's hospital(s) are mandatory with no exemption, and IPA physicians share in gains only through hospital-controlled collaborator agreements. That is a valid "prepare and position" finding.
- **Landscape:** "No model beyond EOM and CJR-X fits an NYS IPA in 2026–27" is an acceptable C1 result.

---

## C1 — CMMI landscape scan and eligibility triage (W1)
**Objective:** Establish the full set of open, announced, upcoming, and mandatory-by-geography CMMI models that could reach an NYS IPA or health system, and triage each one.
**Depends on:** none.
**Tool + settings:** Claude → deep-research skill | Researchers: 1 | Extra round: OFF. (claude.ai fallback: Opus | Effort: High | Extended thinking: ON | Web search: ON | Research: ON)
**Prompt text:**
> Context: I am building a due-diligence evidence base on CMS Innovation Center (CMMI) models for "the Client," an independent physician association (IPA) with an affiliated health system (IPPS acute-care hospital[s]) in New York State. The decision this supports: for voluntary models, whether to join directly, join through a participating organization, or defer or decline, and when; for mandatory models, how to prepare and position. Today is October 2026.
>
> Task: Produce the complete current CMMI model landscape relevant to this kind of organization. Do not assume the candidate set. Start from CMS's model index (cms.gov/priorities/innovation/models) and the 2025–2026 announcements, and check at least these: Enhancing Oncology Model (EOM), CJR-X, TEAM, LEAD, ACO REACH (and its end date), Ambulatory Specialty Model (ASM), ACCESS, WISeR, AHEAD, IOTA, Kidney Care Choices, any primary-care or specialty model announced in 2025–2026, and any announced successors to ending models. Include MSSP only as a non-CMMI baseline row, because it is the common route for joining through another organization.
>
> For each model, report: (1) status label (established, meaning in operation or finalized in regulation; proposed, meaning in a proposed rule; announced, meaning stated by CMS but not yet in regulation or an RFA), each with dates; (2) voluntary or mandatory; (3) eligible participant types, and whether an IPA, ACO, clinically integrated network, physician group practice (TIN), or hospital can be the direct participant; (4) geography, and whether New York State or any NY CBSA is included (list the CBSAs for geography-selected models); (5) application window: open, closed, next expected, or none; (6) start and end dates; (7) any volume or case-count thresholds; (8) a triage verdict for an NYS IPA plus affiliated hospital: ELIGIBLE, INELIGIBLE, or UNCLEAR, with a one-line reason and what would resolve UNCLEAR.
>
> Rules: cite a primary source (CMS model page, Federal Register, RFA, CMS fact sheet or FAQ) for every status, date, and eligibility claim; use secondary sources only to flag something to verify, and label them as secondary. Where sources conflict, show both and do not resolve the conflict. Grade each row's confidence H/M/L (H = multiple independent high-quality sources agree; M = a single strong source; L = thin, dated, or contested). Concluding that nothing beyond EOM and CJR-X is relevant is acceptable if the evidence says so.
>
> Output: (a) one summary table with the columns above; (b) up to 5 lines of notes per ELIGIBLE or UNCLEAR model; (c) a short "Ruled out and why" list; (d) a "Gaps" list. Tag substantive claims [C1].

**Return protocol:** saved as `outputs/W1_C1_Landscape.md`.
**Success criteria:** ≥10 models assessed; every ELIGIBLE/UNCLEAR row has a primary-source URL and a dated status label; NY CBSA inclusion stated explicitly for TEAM and ASM. *Failure mode:* a narrative list of model descriptions with no triage verdicts or NY geography → rerun with the table enforced.

---

## C2 — EOM mechanics, eligibility paths, and reporting brief (W1)
**Objective:** Produce a primary-sourced EOM brief that tests A1 (direct vs through-participant entry), A4 (data burden), and A5 (thresholds).
**Depends on:** none.
**Tool + settings:** Claude → deep-research skill | Researchers: 1 | Extra round: OFF. (Fallback: Opus | High | ON | Web ON | Research ON)
**Prompt text:**
> Context: Due diligence for "the Client," an IPA with an affiliated health system in New York State, on the CMS Enhancing Oncology Model (EOM). Decision: join EOM directly, join through a participating organization, or defer or decline, and when. The Client runs Epic plus many point solutions, with no layer that aggregates data or shows it in uniform dashboards. Today is October 2026.
>
> Produce an EOM brief from primary sources (EOM RFA 2021 and 2024 versions, the participation agreement if public, the CMS EOM page, FAQs, second-cohort fact sheet, payment methodology documents, the CMS/evaluation-contractor evaluation reports). Cover:
> 1. **Who can participate:** the definition of an EOM participant (physician group practice, TIN-level requirements, whether all oncologists billing under the TIN must participate), payer participants, and explicitly whether an IPA, ACO, or clinically integrated network can be a participant itself, or whether its member practices must apply individually. Test both paths: (a) the Client's oncology practice(s) apply directly; (b) they join through, or are covered by, an existing participant or ACO. Say what is permitted, prohibited, or unaddressed.
> 2. **Timeline:** cohort 1 and 2 dates, application windows, end date (June 30, 2030), and any CMS statement about future cohorts or late entry. If there is no window, say so.
> 3. **Episode and payment mechanics:** cancer types, episode trigger and length, Monthly Enhanced Oncology Services (MEOS) amounts by cohort (including any dual-eligible or HRSN adjustment), benchmark and target-price construction, risk arrangements (downside-risk levels, stop-loss and stop-gain), novel-therapy adjustments, Advanced APM and MIPS status.
> 4. **Participant redesign activities and data or reporting requirements:** 24/7 access, patient navigation, care plans, HRSN screening, the electronic patient-reported outcomes (ePRO) phase-in and timing, clinical data elements, quality measures, CEHRT requirements, and submission cadence and format. For each, note whether it implies EHR integration or aggregation across systems.
> 5. **Volume or case-count thresholds:** any minimum episodes or beneficiaries, low-volume rules, or reconciliation-pooling options.
> 6. **Interactions:** overlap rules with MSSP, ACO REACH, LEAD, and other episode models (who keeps savings when beneficiaries overlap).
> 7. **Results to date:** participant counts by cohort, withdrawals, and any evaluation findings, with dates.
>
> Rules: primary source for every mechanics claim; label each claim established, proposed, or announced, with its effective date; if cohort 1 and cohort 2 terms differ, show both; surface contradictions rather than smoothing them; grade confidence H/M/L. Tag claims [C2].
>
> Output: a Markdown brief with the 7 headed sections, a one-paragraph "Implications for the decision anchor" section that states what the evidence permits (not a recommendation), and a "Gaps / Client information needed" list.

**Return protocol:** saved as `outputs/W1_C2_EOM.md`.
**Success criteria:** Section 1 gives an explicit verdict on IPA/ACO direct participation, with a citation; MEOS and risk terms are stated per cohort; ePRO timing is dated. *Failure mode:* a generic EOM overview that is silent on A1 or cites only trade press → rerun with Section 1 first.

---

## C3 — CJR-X final-rule mechanics, applicability, and physician-sharing brief (W1)
**Objective:** Produce a primary-sourced CJR-X brief that tests A3 (required vs exempt; physician sharing), A4, and A5.
**Depends on:** none.
**Tool + settings:** Claude → deep-research skill | Researchers: 1 | Extra round: OFF. (Fallback: Opus | High | ON | Web ON | Research ON)
**Prompt text:**
> Context: Due diligence for "the Client," an IPA with an affiliated health system (IPPS hospital[s]) in New York State, on CJR-X (Comprehensive Care for Joint Replacement Expanded), which reportedly was finalized in the FY 2027 IPPS/LTCH PPS final rule (CMS-1849-F, mid-2026) as mandatory for most IPPS hospitals from January 1, 2028. Decision: how the Client should prepare and position. Today is October 2026.
>
> Produce a CJR-X brief from primary sources (the Federal Register final rule and proposed rule, the CMS CJR-X model page, fact sheets, FAQs, any published participant list, and the CJR evaluation reports). Cover:
> 1. **Status and timeline:** the proposed-rule date, the final-rule date and Federal Register citation (resolve the conflict between Jul 31 and Aug 4, 2026 if possible), what changed from proposed to final, performance-year calendar, baseline years, and when target prices or participant lists are published.
> 2. **Applicability:** which hospitals are required; every exclusion or exemption (TEAM participants, Maryland, CAHs, rural or low-volume, others); and how CJR-X treats a hospital that is in TEAM. Whether a CJR-X participant list exists and where.
> 3. **Episode definition:** procedures (hip, knee, ankle; inpatient and outpatient), trigger, 90-day window, exclusions.
> 4. **Payment mechanics:** target-price method (regional or hospital blend, risk adjustment, TEAM-derived features), discount factor, quality adjustment, stop-loss and stop-gain, any glide path or safety-net provisions, and reconciliation timing.
> 5. **Quality measures and data reporting:** each measure, its data source (claims, hospital-reported, or patient-reported such as the THA/TKA PRO-PM), and submission requirements. Note which require data aggregation beyond claims.
> 6. **How physicians share in results:** collaborator types (physician group practices, individual physicians, ACOs, PGPs, others), sharing and distribution arrangement rules, caps, required written agreements, quality criteria, beneficiary incentives, waivers (for example the SNF 3-day rule), and the Advanced APM track or CEHRT requirements that would let physicians qualify.
> 7. **Volume thresholds:** any minimum episode counts or low-volume treatment.
> 8. **Interactions:** overlap with TEAM, MSSP or other ACOs, BPCI Advanced legacy, and other episode models.
> 9. **Track record:** CJR (2016–2024) evaluation results: savings, quality, and what drove them, with dates and report citations.
>
> Rules: primary source for every mechanics claim; label each claim established (final rule), proposed, or announced, with effective dates; where the proposed and final rules differ, show both; surface contradictions; grade confidence H/M/L. Tag claims [C3].
>
> Output: a Markdown brief with the 9 headed sections, an "Implications for prepare and position" section that states what the evidence permits (not a recommendation), and a "Gaps / Client information needed" list.

**Return protocol:** saved as `outputs/W1_C3_CJR-X.md`.
**Success criteria:** a Federal Register citation is present; the TEAM-overlap rule is stated with a section citation; collaborator types are listed; each quality measure is mapped to its data source. *Failure mode:* the brief describes the proposed rule as current, or relies on Milliman or trade press for mechanics → rerun with "final rule text first."

---

## C4 — Fit-criteria rubric and comparison-matrix scaffold (W1)
**Objective:** Define how "best fit" will be judged before evidence arrives, so the criteria are not reverse-engineered from the findings.
**Depends on:** none (Kickoff Brief only).
**Tool + settings:** Claude → Opus | Effort: High | Extended thinking: ON | Web search: OFF | Research: OFF (route 1; the orchestrator runs it).
**Prompt text:**
> Using only the Kickoff Brief, draft (1) a fit-criteria rubric for evaluating CMMI models for an NYS IPA plus affiliated health system, and (2) a comparison-matrix scaffold. The criteria must cover eligibility path (direct / through a participant / none), timing and window, financial upside, downside exposure, operational burden, data and reporting burden versus a state of Epic plus point solutions with no aggregation layer, model interactions, policy durability, and evidence confidence. For each criterion give: its definition, a 3-level scale with observable anchors, the evidence that would score it, the Client information needed to score it (de-identified), and whether it can be a deal-breaker. Define explicit decision rules that map scores to the anchor: join directly / join via a participant / defer (with a named trigger) / decline; and for mandatory models: the prepare-and-position tiers. Include "no model fits yet" as an outcome. Matrix rows are criteria and columns are models (EOM, CJR-X, plus placeholders for C1 additions). Each cell holds a score, its confidence, and the prompt IDs supporting it.

**Return protocol:** saved as `outputs/W1_C4_Fit-Rubric.md`.
**Success criteria:** every criterion has observable anchors (not "high / medium / low" alone) and names the Client information needed; the decision rules can produce "defer" and "decline." *Failure mode:* a weighted-score formula that would rank a model the Client cannot enter.

---

## Perplexity cards
Use one Perplexity Space for this program with the §8 instructions (pasted at the bottom of this file). Refresh model names from the picker before running (§13). If a named model has been renamed, use the closest current equivalent and note the substitution.

### P1 — EOM future intake window and trajectory (W1)
**Objective:** Determine whether any further EOM application window or late-entry path exists or has been signaled before Jun 30, 2030 (A2).
**Depends on:** none.
**Tool + settings:** Perplexity → Pro Search | Model: GPT-5.4 | Thinking: ON | Connectors: Web ON; Academic, Social, Google Drive, Gmail with Calendar, Wiley, CB Insights, PitchBook, Statista OFF
**Prompt text:**
> As of October 2026, has CMS announced, proposed, or signaled any further application period (a third cohort), late-entry option, or participant-addition process for the Enhancing Oncology Model (EOM), which ends June 30, 2030? The second cohort applied July 1 to September 16, 2024 and began July 1, 2025. Check the CMS EOM model page, EOM FAQs, CMS press releases and Innovation Center strategy statements from 2025–2026, the CY 2026 and CY 2027 Physician Fee Schedule rules, and statements from oncology societies (ASCO, Community Oncology Alliance, ACCC). Also report: (a) any announced EOM changes taking effect in 2026–2027; (b) any announced successor or companion oncology model; (c) whether a practice can join an existing EOM participant's TIN mid-model (for example through acquisition or reassignment) and how that is treated. Label each item established, proposed, or announced, with dates. If nothing was announced, say "No further window found" and list the sources checked, with dates. Lead with findings. Do not restate this prompt. Do not append offers to continue.

**Return protocol:** paste inline; the orchestrator saves it as `outputs/W1_P1_EOM-window.md`.
**Success criteria:** a clear yes or no with a dated primary source, or a dated negative with a list of sources checked; item (c) addressed. *Failure mode:* restating the 2024 window as if it were current → rerun with Model: Claude Sonnet 5.

### P2 — TEAM in New York and the TEAM ↔ CJR-X overlap rule (W1)
**Objective:** Independently pin down the load-bearing applicability facts for A3: which NY areas are in TEAM, and how CJR-X treats TEAM hospitals.
**Depends on:** none.
**Tool + settings:** Perplexity → Pro Search | Model: Claude Sonnet 5 | Thinking: ON | Connectors: Web ON; all others OFF
**Prompt text:**
> Two regulatory questions; cite primary sources (Federal Register, CMS model pages and fact sheets). (1) Transforming Episode Accountability Model (TEAM), which began January 1, 2026: list every CBSA in New York State selected for mandatory TEAM participation, the episode categories TEAM covers (including lower-extremity joint replacement), and TEAM's end date. (2) CJR-X (Comprehensive Care for Joint Replacement Expanded), finalized in the FY 2027 IPPS final rule: how does it treat hospitals that participate in TEAM? Are they excluded from CJR-X, is the joint-replacement episode carved out of one model, or do both apply? Also state any other CJR-X exclusions (CAHs, Maryland, low-volume, others) and whether CMS has published a CJR-X participant list or an eligibility-lookup file, with its location and date. Quote the governing regulatory language where possible and give section citations. Label each item established, proposed, or announced, with dates. If the proposed and final rules differ, show both. Lead with findings. Do not restate this prompt. Do not append offers to continue.

**Return protocol:** paste inline; saved as `outputs/W1_P2_TEAM-NY_CJRX-overlap.md`.
**Success criteria:** a named list of NY CBSAs (or an explicit "none"), and a quoted or cited overlap rule. *Failure mode:* a generic TEAM summary with no NY CBSA list → rerun with Model: Gemini 3.1 Pro on the Federal Register PDF.

### P3 — EOM participant experience and results to date (W1)
**Objective:** Capture real-world participation, attrition, and operational-burden evidence for EOM (scope: participant experience; feeds A4).
**Depends on:** none.
**Tool + settings:** Perplexity → Pro Search | Model: Kimi K2.6 | Thinking: ON | Connectors: Web ON, Academic ON, Social ON; Google Drive, Gmail with Calendar, Wiley, CB Insights, PitchBook, Statista OFF
**Prompt text:**
> Summarize real-world evidence on the CMS Enhancing Oncology Model (EOM) from July 2023 to the present: (1) the number of participating physician group practices and payers in cohort 1 and cohort 2, and how they changed, including withdrawals and the reasons given; (2) findings from any CMS evaluation report or peer-reviewed study of EOM; (3) what participating practices and oncology societies (Community Oncology Alliance, ASCO, ACCC, and others) report as the hardest operational requirements, especially ePRO collection, clinical data submission, HRSN screening, navigation, and EHR or vendor dependence; (4) any reported financial results (reconciliation outcomes, how many practices earned or owed money); (5) how the Oncology Care Model (2016–2022) results shaped EOM, and what lessons are reported to carry over. Distinguish official data from practitioner commentary, and flag commentary that is anecdotal. Give dates for every figure. Lead with findings. Do not restate this prompt. Do not append offers to continue.

**Return protocol:** attach as `outputs/W1_P3_EOM-experience.md`.
**Success criteria:** dated participant counts for both cohorts; at least 3 named operational pain points with sources; official data separated from commentary. *Failure mode:* OCM-only evidence presented as EOM → flag "thin" and decide at the checkpoint.

### P4 — Current status of LEAD, ASM, and ACCESS for New York (W1)
**Objective:** Run a recency check on the three non-named models most likely to reach an NYS IPA (triangulates C1).
**Depends on:** none.
**Tool + settings:** Perplexity → Pro Search | Model: GPT-5.4 | Thinking: ON | Connectors: Web ON; all others OFF
**Prompt text:**
> As of October 2026, give the current status of three CMS Innovation Center models for an independent physician association (IPA) and affiliated hospital in New York State. (1) LEAD (Long-term Enhanced ACO Design): application deadline(s); whether a first or later cohort can still be joined; start date; eligible entity types (can an IPA or physician-led network be the ACO?); how specialists or specialty care (oncology, orthopedics) are incorporated; and how LEAD treats beneficiaries also in EOM or CJR-X episodes. (2) Ambulatory Specialty Model (ASM): status (finalized in the CY 2026 PFS?); start date; which specialties and conditions are covered; how participants are selected (CBSAs?); and whether any New York CBSA is included. (3) ACCESS: application window, start date, eligible participants, and any New York relevance. For each, cite the CMS model page, RFA, or Federal Register source; label each item established, proposed, or announced, with dates; and end with a summary table. Lead with findings. Do not restate this prompt. Do not append offers to continue.

**Return protocol:** paste inline; saved as `outputs/W1_P4_LEAD-ASM-ACCESS.md`.
**Success criteria:** each model has a dated status and an application-window answer; the ASM New York CBSA question is answered explicitly. *Failure mode:* a description of model goals with no windows or geography → rerun with Model: Sonar 2 for the status-only items.

---

## Perplexity Space instructions (§8; paste into the Space's custom instructions)
> You are a research engine supporting a structured, multi-tool research program. On every response in this Space:
> 1. Lead with findings. No preamble, no restating my prompt, no summary of what you're about to do.
> 2. Never append an offer to continue. If something could not be determined, add one line at the very end labeled "Gap:" naming what and why — nothing else.
> 3. Cite every substantive claim inline. Prefer primary and official sources over aggregators.
> 4. When authoritative sources conflict, state the conflict explicitly. Do not resolve it by picking a side or averaging.
> 5. Prioritize sources from the last 24 months unless I ask for historical context; flag any load-bearing source older than that.
> 6. Structure multi-part answers with short headers matching the parts of my question, and end substantive sections with a compact summary table where one fits.
> 7. Distinguish "established today" from "proposed or theoretical" for any status, mechanism, policy, or pathway.
> 8. If a claim is thin, dated, or contested, say so inline. Accuracy over completeness.
>
> Topic scope: CMS Innovation Center (CMMI) payment models (federal Medicare policy, 2023–2026) for a New York State physician association and hospital.

---

## Self-critique (run before presenting)
- **Coverage:** every scope-in item maps to a card. Mechanics: C2, C3. Eligibility and timelines: C1–C3, P1, P2, P4. Participant experience: P3, C3 §9, C2 §7. Data and reporting: C2 §4 and C3 §5 now, cross-model crosswalk in C5 (W2). Interactions: C2 §6 and C3 §8 now, consolidated in C6 (W2). Trajectory: C1, P1. Scenarios: C7 (W2). Matrix: C4. Assumption A5 (thresholds) appears in C1, C2, and C3.
- **Redundancy:** C1/P4 and C3/P2 overlap by design and are each scoped to one recency- or applicability-critical fact. P3 is kept apart from C2 because practitioner sentiment (Social connector) is a Perplexity strength.
- **Dependencies:** all W1 cards are independent. The W2 cards (C5–C7) need W1 outputs, so they are correctly deferred.
- **DR budget:** 0 in W1. The 3-call cap is below one-third of the assumed ~15 monthly balance (5), so it complies.
- **Routing:** breadth with analytical depth → deep-research skill (C1–C3); narrow current-state → Pro Search (P1, P2, P4); aggregation plus sentiment → Pro Search with Social and Academic (P3); reasoning only → Claude with no search (C4).
- **Checkability:** every card has on-the-spot success and failure criteria.

**Plan Risk:** The weakest assumption is that the Client's organizational form can stay generic in W1. The EOM path (A1) and CJR-X physician sharing (A3) both turn on facts not yet provided: whether the oncologists bill under their own TINs or a shared one, current ACO participation, and the hospital's TEAM and CJR-X status. If those facts differ from the generic framing, parts of C2 and C3 analyze paths that do not exist for the Client. Mitigation: the cards test both paths, and the open-questions list names each fact.
