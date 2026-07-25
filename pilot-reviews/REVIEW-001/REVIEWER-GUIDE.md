# REVIEW-001 Reviewer Guide

## Welcome

You are participating in REVIEW-001 as an independent architect and builder. Your task is to read and evaluate the existing TimeLapse Pro system and design and build an independent modular successor — Mission Platform — in your assigned workspace.

This guide tells you how to do that work within the REVIEW-001 rules. It complements the binding documents:

- [`INVITATION.md`](INVITATION.md) — the binding mission and constraints.
- [`REVIEW-PROCESS.md`](REVIEW-PROCESS.md) — the controlled review process.
- [`SUBMISSION-CHECKLIST.md`](SUBMISSION-CHECKLIST.md) — your submission gate.

Normative words (SHALL, SHALL NOT, SHOULD, MAY) follow the [`terminology-standard`](../../review-kit/terminology-standard.md).

## Repository roles at a glance

| Repository | Classification | What you may do |
|---|---|---|
| `froekjaer/timelapse-pro` | Immutable Reference Implementation | Read only. No writes of any kind. |
| `froekjaer/Mission-Platform` | Implementation Repository | Write only inside your assigned branch and workspace. |
| `froekjaer/mission-framework` | Governance Repository | Read only; it governs the process. |

## Your writable boundary

You have exactly **one** writable branch and **one** writable workspace.

- **Repository:** `froekjaer/Mission-Platform`
- **Branch:** `review/review-001-<reviewer>`
- **Workspace:** `review-lab/REVIEW-001/<reviewer>/`

> This workspace is the ONLY writable location assigned to this reviewer.
> The reviewer SHALL NOT create or modify files outside the assigned workspace.

## Before you start

1. Read [`INVITATION.md`](INVITATION.md) in full.
2. Read the destination baseline documents in your workspace's parent directory:
   - `review-lab/REVIEW-001/README.md`
   - `review-lab/REVIEW-001/BASELINE.md`
   - `review-lab/REVIEW-001/SUBMISSION-CHECKLIST.md`
3. Confirm the frozen source baseline commit on `timelapse-pro`:
   - `eed9e3c8c67369e1924c25a11908616220c3c753`
4. Inspect the source repository read-only, starting from its documentation index.

## Architecture principles

SABSA is the recommended thinking structure because it forces business/contextual architecture before technology choices.

The recommended SABSA flow:

1. Business / contextual architecture
2. Conceptual architecture
3. Logical architecture
4. Physical architecture
5. Component architecture
6. Operational architecture

You MAY choose or combine another method — including TOGAF, domain-driven design, hexagonal architecture, C4, event-driven architecture, or clean architecture — when you document why it is better suited, what it replaces, what risks it introduces, and how traceability to business needs is preserved.

## Business-first thinking

Every material architectural decision SHALL answer three questions, with a traceable record:

- **Why?** What mission, stakeholder need, or necessary value does this serve?
- **Because?** What evidence, constraint, dependency, risk, or responsibility justifies it?
- **For whom?** How is capability delivered proportionately to need, consequence, cost, quality, privacy, sovereignty, accessibility, and accountability?

Guiding principle:

> Deliver the right intelligence and capability where it creates necessary value, proportionate to need, consequence, cost, sovereignty, and accountability.

## Deliverables

Each reviewer SHALL produce the following deliverables inside their workspace. They map to the structure already created in your workspace (`docs/`, `adr/`, `platform/`, `payloads/`, `implementation/`, `migration/`, `tests/`, `evidence/`):

- Business architecture
- Conceptual architecture
- Logical architecture
- Physical architecture
- Component model
- ADRs
- Migration strategy
- Operational model
- Implementation
- Tests
- Evidence
- Risk register
- Roadmap

Existing architecture in TimeLapse Pro is evidence, not an unquestionable answer. You MAY challenge or replace an accepted decision only through a new ADR written in your workspace. That ADR MUST describe the decision being challenged, the evidence and reasoning, alternatives considered, migration and compatibility consequences, and a reversible validation path.

## Independence enforcement

You SHALL work independently.

You SHALL NOT:

- inspect another reviewer's solution before the independent phase closes;
- reuse another reviewer's code;
- merge another reviewer's implementation;
- attempt to converge on another reviewer's design.

You MAY disclose external sources, tools, and collaborators used.

## Shared components

If you identify functionality that looks common across reviewers, you SHALL document the proposal inside your own workspace — its purpose, interface, ownership, and rationale — but you SHALL NOT implement shared components during the independent phase.

Selection of shared components belongs exclusively to the Meta Review.

## Prohibited directories

To keep workspaces isolated, you SHALL NOT create any of the following outside your own workspace:

- `shared/`
- `common/`
- `core/`
- root-level `platform/`

## Submission

When your work is ready:

1. Complete every applicable item in [`SUBMISSION-CHECKLIST.md`](SUBMISSION-CHECKLIST.md).
2. Freeze the reviewed commit SHA and record it.
3. Provide a concise handover (executive summary, roadmap, next safe step).
4. Stop implementation until the blind comparison and meta-review begin.

No reviewer solution is merged automatically.

## Where to get help

The Mission Owner (Peter Frøkjær) MAY answer clarification questions about scope, baseline, and rules. The Mission Owner SHALL NOT reveal another reviewer's solution or steer all reviewers toward one design.

## Authority

Peter Frøkjær is Mission Owner and retains final authority over whether a proposal serves the mission.
