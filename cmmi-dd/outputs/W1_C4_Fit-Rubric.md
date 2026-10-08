# W1 · C4 — Fit-Criteria Rubric and Comparison-Matrix Scaffold

Card: C4 (Wave 1) · Route 1 (Claude, no search) · Built from the Kickoff Brief only, **before** W1 evidence returned, so criteria are not reverse-engineered from findings.
Decision anchor: *Voluntary models: join directly / join through a participating organization / defer (with named trigger) / decline. Mandatory models: prepare-and-position tier.*
Status: scaffold. Cells are filled at the W1/W2 checkpoints and in C8 (W3) synthesis.

---

## 1. Design principles

1. **Gates before profiles.** Eligibility, downside, and data feasibility are checked as gates first. A model that fails a gate is not "ranked low"; it routes to *defer* or *decline*. No weighted total score is computed, because a sum can rank a model the Client cannot enter above one it can.
2. **Mechanism, not Client numbers.** No Client volumes or financials are provided, so upside and downside are scored on *model mechanics plus evidence of what participants actually experienced*, never on projected Client dollars.
3. **Every cell carries lineage.** Each cell has a score (3 / 2 / 1), a confidence (H / M / L per Methodology §6), and the prompt IDs supporting it, e.g. `2 · M · [C2, P3]`.
4. **Unknown is a value.** A cell that turns on Client information not yet supplied is scored `? · — · [Qn]` and linked to the open-questions list; it is never guessed.
5. **Negative outcomes are first-class.** "Defer," "decline," and "no model fits yet" are reachable from the decision rules below.

Scale convention: **3 = favorable · 2 = workable with named effort · 1 = adverse (deal-breaker where flagged)**.

---

## 2. Criteria

### G1 · Eligibility path (gate)
- **Definition:** Whether, and how, the Client or one of its components (IPA, member physician group practice/TIN, ACO it belongs to, hospital) can enter the model.
- **Anchors (voluntary):**
  - 3 = A Client component meets the participant definition as a *direct* participant.
  - 2 = Entry only *through* another entity (ACO participant list, an existing participant's TIN, a convener, or a collaborator/downstream arrangement).
  - 1 = No entry path for any Client component during the model's remaining life.
- **Anchors (mandatory):** R = required (named or meets the definition) · X = exempt or not selected (state the rule) · U = status unresolved.
- **Evidence:** participant definition in RFA, rule, or agreement; FAQs; participant list.
- **Client info needed:** TIN structure of relevant practices (Q3); ACO affiliations (Q4); hospital list and TEAM/CJR-X status (Q1, Q2).
- **Deal-breaker:** yes, at 1.

### G2 · Timing and window (gate)
- **Definition:** Whether an entry point exists within the decision horizon, and whether enough model life remains to recover start-up cost.
- **Anchors:**
  - 3 = Window open now or dated within 6 months, AND ≥3 performance years remain after entry.
  - 2 = Window expected (announced, but not dated), OR only 2 performance years remain after entry.
  - 1 = No window before model end, OR <2 performance years remain after entry.
- **For mandatory models:** months from today to PY1 start (≥15 = 3, 6–15 = 2, <6 = 1), measuring preparation runway rather than choice.
- **Evidence:** RFA dates, FR effective dates, model end date, CMS statements on future cohorts.
- **Client info needed:** none (model-side), except internal approval lead time.
- **Deal-breaker:** yes, at 1 for voluntary models.

### G3 · Downside exposure (gate)
- **Definition:** The maximum loss the model's terms permit, and whether the Client can choose its risk level.
- **Anchors:**
  - 3 = Upside-only, or a selectable track with downside capped ≤5% of the relevant spending base (benchmark, episode spend, or revenue base as the model defines it).
  - 2 = Two-sided with stop-loss in the >5–15% range, or a phase-in or glide path to two-sided.
  - 1 = Two-sided >15% or uncapped; or mandatory downside with no glide path.
- **Evidence:** risk-arrangement text, stop-loss/stop-gain, glide-path and safety-net provisions.
- **Client info needed:** risk appetite and reserve policy (qualitative, de-identified); whether a partner would hold risk.
- **Deal-breaker:** yes, at 1 combined with U = 1 (adverse upside evidence).

### G4 · Data and reporting feasibility vs current state (gate; tests A4)
- **Definition:** Whether the Client can meet the model's submission and measurement requirements given Epic plus point solutions and **no aggregation or dashboard layer**.
- **Anchors:**
  - 3 = CMS calculates from claims; no Client submission beyond existing programs (e.g., Hospital IQR, MIPS).
  - 2 = Structured submission whose data elements reside natively in **one** system (Epic) and can be extracted with standard reports, on a quarterly or slower cadence.
  - 1 = Requires **new capture** (e.g., ePRO, HRSN, PRO-PM collection not already live) **and/or** aggregation across Epic plus point solutions, with a first submission due before a realistic build date.
- **Evidence:** reporting specifications, data-element lists, submission portals and cadence; P3-type participant pain points.
- **Client info needed:** whether ePRO, HRSN screening, and PRO-PM capture are live in Epic; which required elements sit in point solutions; whether any analytics or aggregation project is funded or under way.
- **Deal-breaker:** yes, at 1, **unless** a dated remediation plan lands before the first submission (then score 2 with a named dependency).

### U · Financial upside (profile)
- **Definition:** The mechanisms by which money flows *to* the Client, and evidence that comparable participants actually received it.
- **Anchors:**
  - 3 = Prospective or per-beneficiary payments independent of savings (e.g., care-management fees) **plus** a savings mechanism where evaluation or reconciliation data show most participants earned.
  - 2 = Savings-contingent upside only, with mixed or not-yet-published participant results.
  - 1 = Evaluation or reconciliation data show most participants owed money or exited for financial reasons.
- **Evidence:** payment methodology; evaluation reports; reconciliation summaries; withdrawal data.
- **Client info needed:** none to score the mechanism; volume bands later for illustration only (A5).

### S · Physician share mechanism (profile; tests A3, critical for hospital-held models)
- **Definition:** How the IPA's physicians participate in gains or losses when the formal participant is another entity (e.g., a hospital in CJR-X, an ACO in LEAD).
- **Anchors:**
  - 3 = Physicians or the IPA are direct participants, or are named collaborators with defined distribution rules the model protects (written agreement, quality criteria, waiver coverage).
  - 2 = Sharing is permitted but discretionary for the participant, or capped narrowly, or untested.
  - 1 = No permitted sharing mechanism, or sharing is barred.
- **Evidence:** collaborator/financial-arrangement provisions, fraud-and-abuse waivers, caps.
- **Client info needed:** IPA–hospital contracting relationship (qualitative).

### O · Operational burden (profile)
- **Definition:** Care-delivery redesign the model requires beyond reporting.
- **Anchors:**
  - 3 = Existing workflows largely satisfy requirements.
  - 2 = New roles or workflows inside settings the Client controls (e.g., navigation, 24/7 access, care plans).
  - 1 = Requires coordination across settings the Client does not control (e.g., post-acute networks, unaffiliated providers) with financial consequence.
- **Evidence:** participant redesign activities; care-coordination requirements; P3-type experience.
- **Client info needed:** existing navigation, after-hours, and post-acute arrangements (qualitative).

### I · Interactions and exclusions (profile)
- **Definition:** How the model coexists with the Client's other current or likely arrangements (MSSP/ACO, LEAD, TEAM, EOM, CJR-X, ASM).
- **Anchors:**
  - 3 = No overlap, or overlap rules are explicit and preserve the Client's savings.
  - 2 = Overlap rules are explicit but allocate some savings away from the Client, or require choosing between arrangements.
  - 1 = Participation conflicts with, or is pre-empted by, an arrangement the Client holds or must hold (e.g., a precedence rule assigns beneficiaries elsewhere).
- **Evidence:** overlap provisions in each rule, RFA, or agreement; C6 (W2).
- **Client info needed:** current ACO participation (Q4); hospital TEAM status (Q2).

### P · Policy durability (profile)
- **Definition:** How likely the model is to exist, substantially unchanged, through the Client's investment horizon.
- **Anchors:**
  - 3 = Established in final regulation or a signed agreement framework, with ≥3 performance years remaining and no signaled termination.
  - 2 = Established, but with a history of mid-course redesign, or ≤2 performance years remaining, or a successor announced.
  - 1 = Announced or proposed only, or CMMI has signaled early termination.
- **Evidence:** status labels with dates; CMMI strategy statements; early-termination precedents (2025).
- **Client info needed:** none.

### V · Option value (profile; never decisive alone)
- **Definition:** Whether preparing for or joining the model builds capabilities (data layer, navigation, episode management, collaborator contracts) that transfer to other candidate models or to the mandatory ones.
- **Anchors:** 3 = capabilities transfer to ≥2 other candidate models · 2 = to 1 · 1 = model-specific.
- **Evidence:** cross-model crosswalk (C5, C6).

### C · Evidence confidence (meta-criterion, not a fit score)
- The lowest confidence grade among the gate cells (G1–G4) for that model. If it is **L** on any gate, the model cannot route to "join"; the most it can reach is "defer pending evidence," with the specific missing evidence named.

---

## 3. Decision rules

### Voluntary models (apply in order; the first rule that matches wins)
1. **Decline**, if G1 = 1 with no announced successor, **or** G3 = 1 together with U = 1, **or** G4 = 1 with no feasible remediation before the model ends.
2. **Defer (named trigger)**, if any of the following hold; record the trigger:
   - G1 = 1 or G2 = 1 now, but a future window is announced or plausible → trigger: "CMS publishes RFA / cohort dates."
   - C = L on any gate → trigger: "missing evidence X obtained."
   - P = 1 → trigger: "model finalized in regulation or RFA."
   - G4 = 1 with remediation feasible later → trigger: "aggregation layer or ePRO live by date D."
   - Any gate cell = `?` → trigger: "Client supplies Qn."
3. **Join through a participating organization**, if G1 = 2, **or** G1 = 3 but G3 or G4 = 1 and an intermediary would absorb that risk or reporting burden (and S ≥ 2 so value reaches the physicians).
4. **Join directly**, if G1 = 3, G2 ≥ 2, G3 ≥ 2, G4 ≥ 2, P ≥ 2, and C ≥ M on all gates.
5. **No model fits yet**: the program-level outcome when every voluntary model resolves to Defer or Decline. Report it together with the earliest named trigger across models.

### Mandatory models (prepare-and-position tiers)
| Tier | Condition | Posture |
|---|---|---|
| **A · Required, build to perform** | G1 = R and preparation runway ≥ 6 months | Data and quality readiness against G4 gaps; collaborator/physician-share agreements (S); post-acute and care-pathway redesign (O); baseline review once target prices publish. |
| **B · Required, limit exposure** | G1 = R and (runway < 6 months, or G3 = 1, or G4 = 1) | Minimum-compliance reporting first; use any available downside protections; defer discretionary sharing arrangements. |
| **C · Exempt / not selected, monitor** | G1 = X | Document the exemption basis and its expiry (e.g., if a TEAM exemption ends when TEAM ends); prepare for transition. |
| **D · Status unresolved, resolve first** | G1 = U | Single action: confirm status (Q1/Q2). No other preparation is scored until it is resolved. |

For every mandatory tier, also record the **physician-side position**, meaning how the IPA's physicians should be positioned (S score and the mechanism).

---

## 4. Comparison-matrix scaffold

Cell format: `score · confidence · [IDs]` · `?` = awaiting Client info (Qn) · `—` = not yet researched · `n/a` = not applicable.

| Criterion | EOM (voluntary) | CJR-X (mandatory) | TEAM (mandatory, CBSA) | LEAD (voluntary) | ASM (mandatory, CBSA) | [C1 addition] | [C1 addition] |
|---|---|---|---|---|---|---|---|
| G1 Eligibility path | — | — (R/X/U) | — (R/X/U) | — | — (R/X/U) | — | — |
| G2 Timing / window | — | — (runway) | — | — | — (runway) | — | — |
| G3 Downside exposure | — | — | — | — | — | — | — |
| G4 Data/reporting feasibility | — | — | — | — | — | — | — |
| U Financial upside | — | — | — | — | — | — | — |
| S Physician share | n/a unless via ACO | — | — | — | — | — | — |
| O Operational burden | — | — | — | — | — | — | — |
| I Interactions | — | — | — | — | — | — | — |
| P Policy durability | — | — | — | — | — | — | — |
| V Option value | — | — | — | — | — | — | — |
| **C Confidence (min of gates)** | — | — | — | — | — | — | — |
| **Routed outcome** | — | Tier — | Tier — | — | Tier — | — | — |
| **Named trigger (if Defer)** | — | n/a | n/a | — | n/a | — | — |

Columns for TEAM, LEAD, and ASM are placeholders pending C1/P4 triage. Columns for models C1 rules **INELIGIBLE** are dropped (scope out), with the reason recorded in the Evidence Ledger.

---

## 5. Client information needed to complete the matrix (feeds the open-questions list)

| Qn | Information (de-identified) | Criteria it unlocks |
|---|---|---|
| Q1 | Any Client hospital on the CJR-X participant list? | G1 (CJR-X), Tier |
| Q2 | Any Client hospital a TEAM participant? | G1 (TEAM), I (CJR-X), Tier |
| Q3 | Oncologists' billing TIN structure; any already in EOM? | G1 (EOM), S |
| Q4 | Current ACO participation (MSSP / REACH / none); intent for LEAD | G1 (LEAD), I (all) |
| Q5 | Whether ePRO, HRSN screening, and THA/TKA PRO-PM capture are live in Epic; which required elements sit in point solutions | G4 (all) |
| Q6 | Whether any data-aggregation or analytics project is funded, with a target date | G4 remediation, V |
| Q7 | Risk appetite (qualitative): willing to hold two-sided risk directly, or only via a partner | G3, routing to "via participant" |
| Q8 | Volume *bands* only (e.g., LEJR episodes per year <50 / 50–200 / >200; oncology chemo patients per year bands), for illustrative scenarios and threshold checks (A5) | U illustration, thresholds |
| Q9 | Nature of the IPA–hospital contracting relationship (qualitative) | S |

---

## 6. Known limitations of this rubric
- The downside and data-feasibility cut-points (5%, 15%, quarterly cadence) are judgment anchors, not industry standards. Revisit them at the W2 checkpoint if the models cluster at a boundary.
- The upside score relies on published participant outcomes, which lag (evaluation reports trail performance by 1–2 years). For new models (LEAD, CJR-X), U will default to 2 with confidence L.
- Option value (V) can tempt "join for learning." By design, it cannot override a gate.
