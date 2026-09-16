# Framework Finding — FF-TLP-0001

**Identifier:** FF-TLP-0001
**Source:** TimeLapse Pro (`froekjaer/timelapse-pro`, PR #240)
**Status (disposition):** Accepted — the governance/architecture decision and its disposition (Extend) are approved. This does **not** mean propagation is complete.
**Propagation status:** Open — see "Propagation targets" in Disposition below; none are yet closed.
**Submitted:** 2026-09-15
**Confidence:** High

## Title

**Consequential governance/architecture decisions require an explicit, evidence-backed cross-repository and publication impact assessment, with owner and disposition tracked to closure — not just intra-repository review**

## Canonical Reference

- [`OP-001-Mission-Operational-Preamble.md`](../operational/OP-001-Mission-Operational-Preamble.md), Step 7 ("Check Cross-Repository Consistency") and §8 ("Visible Preamble Record")
- This document, "Minimum finding record" and "Repository practice"

## Context

TimeLapse Pro (a downstream reference implementation) developed a local governance model (its "§16" capability-register proposal) covering capability-equivalence review, search-before-create discipline, evidence-freshness standards, and correction/supersession discipline. During the work, TimeLapse's own governing participant (Peter, TimeLapse Pro decision authority) requested and reviewed a cross-repository impact analysis before treating the local work as complete, and found:

1. Mission Framework's OP-001 Step 7 named cross-repository consistency but did not operationalise impact *assessment*, evidence for negative conclusions, or gap tracking, and OP-001's own Visible Preamble Record (§8) did not expose Steps 7–9 at all — a session could show a fully "complete" preamble while never having assessed cross-repository impact.
2. Mission Framework's Framework Findings process (this document) was structurally the correct existing feedback channel, but was operationally unused for this purpose: it had no Owner field, and — discovered during verification — real findings already existed in peripheral repositories (`FF-PUB-001..004` in `-Publication-Pipeline`; `FF-0001`/`FF-0002` in `mission-solar-eclipse`) without being discoverable from `mission-framework` itself, contrary to this document's own "Repository practice" rule.
3. Independent adversarial review (two rounds) of both the TimeLapse-local proposal and this generalisation confirmed the underlying architecture — extend OP-001 Step 7 and Framework Findings rather than build a third mechanism — while finding concrete, already-materialised instances of the failure mode being guarded against (a Mission-Platform-published page presenting ADR content matching no real ADR file; a Collaborative Intelligence published page diverging from its own README).

## Observation

The generic pattern — consequential decisions in one repository silently failing to reach, or being silently contradicted by, other repositories and their published artefacts — is not specific to TimeLapse. It was independently observed to have already occurred in at least two other repositories in this programme (Mission-Platform's ADR index/website; Collaborative Intelligence's published page), and Mission Framework's own operational procedure had no mechanism that would have caught any of these before this finding.

## Interpretation

OP-001 and Framework Findings already contain the right conceptual pieces (Governing Maxim, Operational Knowledge States, a findings lifecycle with an explicit "Propagation to affected repositories and publications" step). What was missing was not a new mechanism but: (a) an explicit, both-directions statement of the propagation obligation in Step 7 itself, (b) visible completion evidence for Step 7 so it cannot be silently skipped, and (c) enough structure in a Finding record (owner, affected artefacts, propagation targets, closure evidence) to track an open cross-repository gap to actual closure rather than losing it.

## Evidence

- TimeLapse Pro PR #240, head `ae30f7a2f58dc3d3ebd4d4330defa138e8ac24bf` — `Dokumentation/CROSS_REPOSITORY_GOVERNANCE_PROPAGATION_ANALYSIS_2026-09-14_CLAUDE.md` (impact/placement analysis, independently adversarially reviewed twice) and `Dokumentation/CAPABILITY_REGISTER_FINAL_PROPOSAL_2026-09-13_CLAUDE.md` §16 (the originating local governance model).
- Direct verification (2026-09-15) of current `mission-framework` state confirming: OP-001 Step 7's prior text was direction-agnostic and untied to any completion evidence; §8's Visible Preamble Record omitted Steps 7–9; the Findings schema had no Owner field; six real findings existed in `-Publication-Pipeline` and `mission-solar-eclipse` unreferenced from `mission-framework`.
- Independently verified, materialised anti-pattern instances: Mission-Platform's published site presents ADR content ("ADR-1..4") matching no file under `docs/adr/` (only `ADR-0001`/`ADR-0002` exist); Collaborative Intelligence's published `index.html` diverges from its own `README.md`/`AI_CONTEXT.md`.

## Consequence

Without an explicit, evidence-backed, both-directions propagation obligation with visible completion evidence and trackable ownership, a consequential decision — upstream or downstream — can be declared complete while a real cross-repository or publication inconsistency remains permanently undiscovered, exactly as already observed to have happened at least twice in this programme.

## Proposed Disposition

**Extend.** Extend OP-001 Step 7 (impact-assessment obligation, both directions, evidence standard for negative conclusions, gap registration) and extend Framework Findings' minimum record (Owner, affected repositories/artefacts, propagation targets, verification/closure evidence), plus add a central findings index so existing and future findings are discoverable from `mission-framework` as this document's own "Repository practice" rule already requires. No new cross-repository mechanism is introduced; no TimeLapse-specific implementation mechanics (its GRC register, rollout/health-check mechanics) are copied upstream — only the generalised principle.

## Review Criteria

1. ✅ Observation is traceable to a real, documented cross-repository review (TimeLapse PR #240, two independent adversarial review rounds)
2. ✅ Issue concerns canonical operational procedure (OP-001 Step 7/§8) and framework process (Framework Findings), not a local TimeLapse design choice
3. ✅ Existing definitions were genuinely incomplete: Step 7 lacked directionality/evidence/completion representation; Findings lacked ownership and central discoverability
4. ✅ Proposed change improves operational value: makes propagation assessment reviewable rather than assumable
5. ✅ Change is additive/clarifying to existing structure; does not introduce a competing mechanism or redefine unrelated concepts
6. ✅ Evidence is sufficient: two independent adversarial reviews plus direct, dated verification against current `mission-framework` state
7. ✅ Affected documents identified: `OP-001-Mission-Operational-Preamble.md`, `FRAMEWORK_FINDINGS.md`; downstream propagation to TimeLapse Pro, Collaborative Intelligence, Mission Platform and their publications remains open (see disposition below and the implementing pull request's registered gaps)

---

## Disposition

**Status (disposition):** Accepted. This records that the governance/architecture decision and its disposition (Extend) have identifiable human approval — it is **not** a claim that downstream propagation is complete. A Finding is not closed merely because its disposition was accepted; closure requires the propagation targets below to be completed and verified, or separately re-dispositioned (see "Verification/closure evidence").
**Propagation/implementation status:** Open — none of the propagation targets below are yet complete.
**Rationale:** Identifiable human approval given by TimeLapse Pro's decision authority (Peter), who reviewed the underlying analysis, two independent adversarial review rounds, and explicitly authorised moving from analysis to controlled Mission Framework implementation (TimeLapse PR #240 head `ae30f7a2f58dc3d3ebd4d4330defa138e8ac24bf`). Per "Authority and accountability" above, this constitutes the identifiable human approval required for a consequential change; the change itself is implemented in the pull request that introduces this finding.
**Owner:** Mission Framework maintainer (accepting/implementing this finding); TimeLapse Pro decision authority for the originating analysis and for the downstream TimeLapse-side propagation items below.
**Affected repositories/artefacts:** `mission-framework` (`OP-001-Mission-Operational-Preamble.md`, `FRAMEWORK_FINDINGS.md` — this wave); `timelapse-pro`, `collaborative-intelligence`, `Mission-Platform` and their publications (downstream — not implemented in this wave, see propagation targets).
**Propagation targets (not yet closed):**
- `timelapse-pro`: add a §16 sub-clause referencing the now-extended OP-001 Step 7; extend `PAKKE_SPOR_REGISTER.md` with a propagation-gap convention; decide and record its OP-001 integration model (continue vendoring with sync discipline, load canonical live, or a cached/fallback hybrid) — TimeLapse's decision authority has not yet made this choice.
- `Mission-Platform`: correct or explain the published-site ADR content that matches no real ADR file, and the ADR index omission of `ADR-0002` — Mission-Platform's own decision.
- `collaborative-intelligence`: reconcile the published `index.html` with `README.md`/`AI_CONTEXT.md` — Collaborative Intelligence's own decision.
- `mission-framework` publication: confirm the rendered book reflects this finding's changes once merged to `main` and the publication pipeline runs (not verified in this wave — the pipeline only triggers on push to `main`, and this finding is introduced via a pull request that is not merged in this wave).

**Investigated 2026-09-15 (pre-merge verification):** whether canonical OP-001 (`docs/operational/OP-001-Mission-Operational-Preamble.md`) is intentionally excluded from `publication/book.yml`, or an omission. `git log` shows `book.yml`'s source list was authored by the same person, the same day OP-001 was added (2026-07-22), roughly 2.5 hours later — the curated list includes a sibling operational document (`docs/operational/TRUST-BOOTSTRAP-CREDIBILITY-ONBOARDING-EVIDENCE-MATURITY.md`, headed "Status: Operational concept specification") while excluding OP-001 (headed "Status: Canonical Operational Procedure"). `docs/publication/PUBLICATION-PIPELINE.md` §"Book" defines a book as assembling "a sustained argument or body of knowledge" — a genre TRUST-BOOTSTRAP's narrative/conceptual form fits and OP-001's imperative, checklist-style mandatory procedure does not naturally fit. This is circumstantial but real evidence leaning toward **intentional exclusion (classification A)** rather than drift (B) — but no explicit written rationale sentence stating this was found anywhere in the repository, so it is not conclusively confirmed. `book.yml` is therefore **not modified** by this finding or its implementing pull request.

**Decided 2026-09-16, by Peter (identifiable human decision authority):** OP-001's absence from `book.yml` is confirmed as **intentional separation of publication surfaces**, not an open propagation gap. Rationale given: Mission Framework's book and the operational procedures serve different publication purposes — `book.yml` is the narrative Mission Framework publication; OP-001 remains a canonical operational procedure with its own authoritative placement outside that publication. This decision supersedes the "not conclusively confirmed" qualifier above (kept visible, not deleted, as the evidence trail that informed the decision); it does not retroactively claim the prior circumstantial-evidence classification was certain before this decision existed. Consequently, this propagation target is **closed as "no book.yml change required"** — replaced by the requirements below, which remain open:

- OP-001 shall be clearly discoverable from Mission Framework's relevant navigation/onboarding surfaces (not only from the book).
- Its canonical/authoritative status shall be unambiguous wherever it is referenced or linked.
- Integration mechanisms (loaders, vendoring, live-loading) shall be able to identify and use the correct canonical version.
- Changes to OP-001 shall be subject to cross-repository propagation assessment (already provided by this finding's OP-001 Step 7 extension).
- Publication or distribution of OP-001 shall not create a competing normative copy (already provided by Step 7's authoritative-vs-derived distinction).

This decision does **not** resolve which OP-001 integration model TimeLapse (or another downstream consumer) should use — vendored copy with freshness/sync control (A), canonical-live loading (B), or canonical source with a controlled local cache/fallback (C). That remains a separate, explicitly open DECISION REQUIRED item for each downstream consumer's own decision authority.
**Verification/closure evidence:** Not yet applicable — this finding remains open at the "Mission Framework extended" milestone; it closes only once the propagation targets above are each either completed and verified, or separately re-dispositioned.
