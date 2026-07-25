# REVIEW-001 Review Process

## Purpose

This document defines the controlled process by which REVIEW-001 is conducted under Mission Framework governance. It exists so that the review is reproducible, evidence-based, and fair to every independent reviewer.

It applies the shared Mission Framework standards in [`review-kit/`](../../../review-kit/), in particular:

- [`terminology-standard.md`](../../../review-kit/terminology-standard.md) — normative language (SHALL, SHOULD, MAY).
- [`evidence-standard.md`](../../../review-kit/evidence-standard.md) — what counts as acceptable evidence.
- [`review-decision-standard.md`](../../../review-kit/review-decision-standard.md) — possible review outcomes.
- [`reviewer-mission.md`](../../../review-kit/reviewer-mission.md) — reviewer responsibilities.

Normative words in this document follow the meanings defined in the terminology standard and align with RFC 2119 intent.

## Scope

This process governs the full REVIEW-001 lifecycle: invitation, independent implementation, submission, blind comparison, and meta-review.

It does not govern the day-to-day Mission Framework review of unrelated components.

## Repository roles

REVIEW-001 spans three repositories, each with a distinct and binding classification.

### Immutable Reference Implementation — `froekjaer/timelapse-pro`

- Classification: **Immutable Reference Implementation**.
- Frozen baseline commit: `eed9e3c8c67369e1924c25a11908616220c3c753` ("Extract Edge provisioning security services").
- Purpose: the authoritative reference implementation and evidence base for REVIEW-001.
- This repository SHALL be treated as **read-only** for the entire REVIEW-001 lifecycle.
- No implementation work SHALL be performed here.

Permitted activities — reviewers MAY:

- read documentation;
- inspect source code;
- inspect architecture;
- inspect ADRs;
- inspect tests;
- inspect configuration;
- inspect operational behaviour;
- analyse migration requirements.

Prohibited activities — reviewers SHALL NOT:

- commit;
- push;
- create branches;
- create pull requests;
- create issues;
- modify files;
- delete files;
- reorganise the repository;
- perform implementation work.

This repository exists solely as the evidence source for REVIEW-001.

### Implementation Repository — `froekjaer/Mission-Platform`

- Classification: **Implementation Repository**.
- Purpose: the destination repository.
- All architecture, documentation, implementation and migration work for REVIEW-001 SHALL be created here, on the assigned reviewer branch and inside the assigned reviewer workspace only.
- No reviewer work outside an assigned workspace is permitted.

### Governance Repository — `froekjaer/mission-framework`

- Classification: **Governance Repository**.
- Purpose: contains the methodology, governance, review process and evidence describing how reviews are performed.
- This document, together with the other REVIEW-001 documents in this directory, governs the process.

## Independence

Each reviewer SHALL work independently from every other reviewer.

A reviewer SHALL NOT:

- inspect another reviewer's solution before the independent phase closes;
- reuse another reviewer's code;
- merge another reviewer's implementation;
- attempt to predict or converge on another reviewer's design.

Divergence is valuable when it is reasoned and evidenced. The Mission Owner MAY answer clarification questions but SHALL NOT reveal another reviewer's solution or steer all reviewers toward one design.

## Phases

The review SHALL proceed through the following phases. A phase SHALL NOT start before its predecessor closes.

### Phase 1 — Invitation and baseline freeze

- The invitation ([`INVITATION.md`](INVITATION.md)) and this process document SHALL be available to every reviewer.
- The frozen source baseline commit SHALL be recorded and SHALL NOT move during the independent phase.
- The destination baseline (shared lab documents on `main` of `Mission-Platform`) SHALL be present before any reviewer branch is created.
- Reviewer branches and workspaces SHALL exist before reviewers begin implementation.

### Phase 2 — Independent implementation

- Each reviewer works on their assigned branch and inside their assigned workspace only.
- The reviewer SHALL produce the deliverables listed in [`REVIEWER-GUIDE.md`](REVIEWER-GUIDE.md).
- The reviewer SHALL NOT modify anything outside their assigned workspace.

### Phase 3 — Submission gate

- A submission is complete only when the conditions in [`SUBMISSION-CHECKLIST.md`](SUBMISSION-CHECKLIST.md) are satisfied.
- The reviewer SHALL freeze and record a final commit SHA.
- After freezing, the reviewer SHALL stop implementation until the blind comparison and meta-review begin.

### Phase 4 — Blind comparison

- Once all intended submissions are frozen, Mission Framework performs a comparison of the independent results.
- No reviewer solution is merged automatically.
- The comparison preserves dissent rather than forcing convergence.

### Phase 5 — Meta-review and synthesis

- Governed by [`META-REVIEW.md`](META-REVIEW.md).
- The meta-review selects the strongest supported elements, records dissent, and produces a separately governed integration plan for `main`.

## Shared components

Common functionality discovered independently by reviewers SHALL be documented, not implemented across workspaces.

A reviewer SHALL NOT:

- create a repository-level `shared/`, `common/`, `core/`, or root `platform/` directory outside their own workspace;
- implement shared components during the independent phase.

A reviewer SHALL:

- document any proposed shared component inside their own workspace;
- describe its purpose, interface, ownership and rationale.

Selection of shared components belongs exclusively to the Meta Review.

## Evidence

All claims, findings, and architectural decisions SHALL be supported by evidence in accordance with the [`evidence-standard`](../../../review-kit/evidence-standard.md). Acceptable evidence includes the frozen TimeLapse Pro baseline, runtime evidence, ADRs, tests, configuration, and operational records.

AI-generated content SHALL NOT be treated as evidence by itself; it SHALL be validated against underlying source material before it supports a finding or decision.

## Source authority hierarchy

For claims about the source system, prefer in this order:

1. verified runtime evidence;
2. current code and automated tests;
3. accepted ADRs;
4. authoritative current documentation;
5. historical documentation and discussion.

Conflicts SHALL be recorded rather than silently reconciled.

## Baseline movement

The TimeLapse Pro baseline SHALL NOT move during the independent phase. A later source update requires:

- an explicit REVIEW-001 baseline decision;
- a documented impact assessment;
- whether all reviewers received the same correction;
- Mission Owner approval.

## Process integrity and violations

A violation of independence, the read-only boundary, or the workspace boundary is a governance issue. It SHALL be recorded and assessed against the [`severity-classification`](../../../review-kit/severity-classification.md) and may invalidate a submission in whole or in part.

## Authority

Peter Frøkjær is Mission Owner and retains final authority over whether a proposal serves the mission. The Mission Owner does not prescribe the technical solution and SHALL NOT remove productive diversity before independent submission.
