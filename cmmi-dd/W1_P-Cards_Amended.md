# W1 · Amended Perplexity Cards (post-checkpoint, 2026-10-08)

These replace the original P1–P4 in `W1_Prompt_Cards.md`, per `outputs/W1_Checkpoint.md` §3. If you have already run an original, return that output too; it will be logged as triangulation. All cards use the program Space (§8 instructions in `W1_Prompt_Cards.md`). Refresh model names from the picker first.

Decision anchor: *Voluntary models: join directly, join through a participating organization, or defer/decline, and when. Mandatory models: how to prepare and position.*

---

### P1′ — EOM successor signals and mid-model entry mechanics (W1)
**Objective:** Close C2 gaps Ca9 and Ca11: the remaining "join-through" and "defer trigger" facts for EOM.
**Depends on:** none (C2 context restated below).
**Tool + settings:** Perplexity → Pro Search | Model: GPT-5.4 | Thinking: ON | Connectors: Web ON, Academic ON; Social, Google Drive, Gmail with Calendar, Wiley, CB Insights, PitchBook, Statista OFF
**Prompt text:**
> Context: CMS's Enhancing Oncology Model (EOM) accepts only single-TIN oncology physician group practices. Its last application window closed September 16, 2024, and it ends June 30, 2030. As of October 2026, answer three questions. (1) Has CMS, a CMS official, or a CMS rule (CY 2026 or CY 2027 Physician Fee Schedule, Innovation Center strategy documents) signaled a successor oncology model, a mandatory oncology model, or a third EOM cohort? Include the Chong et al. JCO Oncology Practice (Jan 2025) article if it discusses this. (2) What do public EOM documents (participation agreement summaries, FAQs, office-hours transcripts) say about adding practitioners to a participant's TIN mid-model, practice acquisitions or mergers, TIN changes, and whether every oncologist billing under the TIN must be on the practitioner list? (3) Has CMS published any EOM reconciliation or evaluation results after performance period 3? Label each item established, proposed, or announced, with dates; cite primary sources; and say "none found" with the sources checked where applicable. Lead with findings. Do not restate this prompt. Do not append offers to continue.

**Return protocol:** paste inline → `outputs/W1_P1_EOM-successor.md`
**Success criteria:** each of the 3 parts answered or explicitly negative, with dated sources. *Failure mode:* restating EOM basics → rerun with Model: Claude Sonnet 5.

### P2′ — Physician sharing under TEAM, and LEAD ACOs as collaborators (W1)
**Objective:** Close Ca1, Ca2, Ca5: whether the IPA's physicians can share in TEAM the way they can in CJR-X, and whether a LEAD ACO counts as an "ACO" collaborator.
**Depends on:** none.
**Tool + settings:** Perplexity → Pro Search | Model: Claude Sonnet 5 | Thinking: ON | Connectors: Web ON; all others OFF
**Prompt text:**
> Regulatory questions; cite the Federal Register or 42 CFR part 512 with section numbers, and quote the governing text. (1) Under the Transforming Episode Accountability Model (TEAM; FY 2025 IPPS final rule, 42 CFR part 512 subpart E), who may be a "TEAM collaborator"? Specifically, are physician group practices, individual physicians, and Medicare ACOs included? What are the gainsharing and alignment-payment caps? (2) Under both TEAM and CJR-X (FY 2027 IPPS final rule, 91 FR 49570), does an ACO participating in the CMS Innovation Center's LEAD model, or in ACO REACH, qualify as an "ACO" collaborator, or is the term limited to Shared Savings Program ACOs under §425.20? (3) In the FY 2025 IPPS final rule's TEAM CBSA selection table, list the New York State CBSAs selected. Label each item established, proposed, or announced, with dates. If the regulatory text is silent, say so explicitly. Lead with findings. Do not restate this prompt. Do not append offers to continue.

**Return protocol:** paste inline → `outputs/W1_P2_TEAM-collaborators.md`
**Success criteria:** quoted definitions with section citations; an explicit answer on LEAD ACOs (including "silent"). *Failure mode:* CJR-X rules presented as TEAM rules → rerun with Model: Gemini 3.1 Pro on the FR document.

### P4′ — ASM exemptions and LEAD entry deadlines (W1)
**Objective:** Close Ca3 and Ca4.
**Depends on:** none.
**Tool + settings:** Perplexity → Pro Search | Model: GPT-5.4 | Thinking: ON | Connectors: Web ON; all others OFF
**Prompt text:**
> As of October 2026, cite CMS primary sources (model pages, RFAs, the CY 2026 and CY 2027 Physician Fee Schedule rules, FAQs) to answer two parts. (1) Ambulatory Specialty Model (ASM), mandatory from January 1, 2027: are clinicians exempt or excluded if they are Qualifying APM Participants, participate in a Shared Savings Program ACO, LEAD, or another Advanced APM? Is there any opt-out? Is the participation threshold 20 attributed episodes or 20 Medicare patients? What is the payment-adjustment range by year (±9% initially, rising to 12%?), and is ASM an Advanced APM or MIPS APM? (2) LEAD (Long-term Enhanced ACO Design): what is the deadline for an existing LEAD ACO to add Participant TINs for performance year 2027? When does CMS expect the next application window (for PY2028), and what does the Letter of Interest commit an organization to? Label each item established, proposed, or announced, with dates; end with a summary table. Lead with findings. Do not restate this prompt. Do not append offers to continue.

**Return protocol:** paste inline → `outputs/W1_P4_ASM-LEAD-deadlines.md`
**Success criteria:** an explicit yes, no, or silent answer on each ASM exemption; dated LEAD deadlines, or "not published." *Failure mode:* generic model descriptions → rerun with Model: Sonar 2 for the date items only.

### P5 — New York AHEAD implementation (NEW, W1)
**Objective:** Close Ca7. AHEAD surfaced in C1 as a possible voluntary path for downstate NY; its specifics determine whether a C9/C10 brief is warranted.
**Depends on:** none.
**Tool + settings:** Perplexity → Pro Search | Model: Kimi K2.6 | Thinking: ON | Connectors: Web ON; all others OFF
**Prompt text:**
> New York State joined the CMS States Advancing All-Payer Health Equity Approaches and Development (AHEAD) Model in Cohort 3 as a sub-state ("downstate") region, with performance beginning January 1, 2028. Using CMS and New York State Department of Health sources (including the CMS–New York State Agreement if public), answer: (1) which counties are in the NY AHEAD region, and whether this is final; (2) the timing, eligibility, and selection process for "Geo AHEAD" Geo Entities in New York (RFA expected Q1 2027?), including whether provider-led organizations or IPAs can bid, the minimum beneficiary counts, and overlap rules with the Medicare Shared Savings Program and LEAD; (3) the Hospital Global Budget component in NY: which hospitals are eligible, application dates, and whether participation is voluntary; (4) Primary Care AHEAD in NY: eligibility (NYS PCMH?) and dates. Label each item established, proposed, or announced, with dates; flag any item sourced only to secondary reporting. Lead with findings. Do not restate this prompt. Do not append offers to continue.

**Return protocol:** paste inline → `outputs/W1_P5_NY-AHEAD.md`
**Success criteria:** a county list with a source and finality status; dated Geo Entity and Hospital Global Budget timing, or "not published." *Failure mode:* national AHEAD description with no NY specifics → flag "thin"; this triggers the held DR candidate only if the Client is downstate.

---
**Killed:** P3 (EOM participant experience). Reason: EOM direct entry is closed, and C2 holds the primary results. If already run, return it and it will be archived as context.
