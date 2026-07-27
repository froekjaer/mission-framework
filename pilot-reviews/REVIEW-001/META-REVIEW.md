# REVIEW-001 Meta-Review

## Purpose

This document defines the meta-review: how the independent REVIEW-001 submissions are compared, evaluated, and synthesised into the Mission Platform reference architecture.

The meta-review is the closing phase of [`REVIEW-PROCESS.md`](REVIEW-PROCESS.md) and uses the outcome types defined in [`review-decision-standard.md`](../../review-kit/review-decision-standard.md).

## Principle

The meta-review is **not a popularity vote**. No complete reviewer branch wins by default.

The meta-review:

- compares independent submissions on evidence and traceability;
- selects the strongest supported elements;
- preserves dissent;
- produces a separately governed integration plan for `main`.

Divergence between reviewers is treated as information, not as a defect to be eliminated.

## Who performs it

The meta-review is performed by the Mission Owner together with the governance function of Mission Framework. The Mission Owner retains final authority over whether a proposal serves the mission.

A reviewer SHALL NOT participate in the meta-review of their own submission in a way that compromises independence of judgement.

## Inputs

The meta-review SHALL consider:

- the frozen submission of every reviewer (commit SHA + workspace);
- the deliverables defined in [`REVIEWER-GUIDE.md`](REVIEWER-GUIDE.md);
- the evidence recorded in each workspace;
- the ADRs, including any ADRs that challenge accepted TimeLapse Pro decisions;
- each reviewer's self-assessment and recommended division of labour;
- the frozen TimeLapse Pro baseline as the common reference.

Submissions that failed the [`SUBMISSION-CHECKLIST.md`](SUBMISSION-CHECKLIST.md) gate SHALL NOT enter comparison until the gate is satisfied, unless the Mission Owner grants an explicit, recorded exception.

## Comparison method

The meta-review SHALL apply a blind, criteria-based comparison. For each reviewed element, the meta-review SHALL assess:

- alignment with mission and stakeholder need (Why? For whom?);
- strength of evidence and reasoning (Because?);
- proportionality to need, consequence, cost, sovereignty, and accountability;
- platform/payload separation and control-plane/data-plane separation;
- security, privacy, safety, and compliance posture;
- operational viability;
- migration feasibility and reversibility;
- testability and reproducibility.

## Decision standard

Each evaluated element SHALL receive one of the outcomes defined in [`review-decision-standard.md`](../../review-kit/review-decision-standard.md):

- **APPROVED** — selected for the reference architecture.
- **APPROVED WITH CONDITIONS** — selected, provided specified conditions are completed.
- **CHANGES REQUIRED** — direction accepted but the element must be corrected and re-evaluated.
- **REJECTED** — not selected; the rationale is recorded.
- **UNABLE TO CONCLUDE** — insufficient evidence to decide; additional evidence or clarification is required.

Deviations from the standard decision matrix SHALL be documented with rationale.

## Shared component selection

Selection of shared components belongs exclusively to the Meta Review.

When two or more reviewers independently propose equivalent shared functionality, the meta-review SHALL:

- document the convergence as evidence of a likely platform concern;
- select one approach, combine approaches, or commission a new design;
- record the rationale and the rejected alternatives.

A reviewer's documented proposal for a shared component SHALL NOT be implemented by the reviewer during the independent phase; only the meta-review may promote such a component.

## Risk perspectives

Risk SHALL be evaluated from two distinct perspectives, in line with [`reviews/MIAR/RISK-METHOD.md`](../../reviews/MIAR/RISK-METHOD.md):

1. **Project and implementation risk** — risks to the project, system, implementation, governance, adoption and long-term viability.
2. **Cybersecurity, architecture and regulatory risk** — risks arising from architecture, software, AI, data, operations, supply chain, privacy, resilience and legal obligations.

The two perspectives SHALL NOT be merged in the synthesis. Cross-reference related risks where useful, but keep the registers distinct because they have different owners, treatments, and evidence types.

### Fairness notice (REVIEW-001)

The original REVIEW-001 invitation did not explicitly require reviewers to produce two separate risk registers. Therefore:

- A REVIEW-001 submission SHALL NOT be marked non-compliant solely because it combined the two risk perspectives into a single register.
- A missing second register caused by this omission in the invitation SHALL be recorded as a **process gap**, not a reviewer failure.
- The Meta Review MAY normalise information from a combined register into the two perspectives for comparison, but SHALL preserve the reviewer's original evidence and intent.

### Prospective rule (from REVIEW-002 onward)

From REVIEW-002 onward, reviewers SHALL submit two separate risk analyses following [`reviews/MIAR/RISK-METHOD.md`](../../reviews/MIAR/RISK-METHOD.md), unless the review invitation explicitly states otherwise. This prospective rule does not apply to REVIEW-001.

## Synthesis into the reference architecture

The meta-review SHALL produce a synthesis that becomes the input to a separately governed reference architecture on `main`. The synthesis SHALL:

- identify selected elements per architecture layer;
- preserve dissenting but reasoned alternatives;
- record the mapping from selected elements to their originating reviewer submission;
- identify gaps that none of the reviewers addressed;
- propose the integration sequence for `main`.

## Framework versus Platform classification

For every proposed synthesis decision, the Meta Review SHALL classify the decision as one of:

- **FRAMEWORK** — a reusable governance rule, principle, review requirement, or methodology. Lives in `froekjaer/mission-framework`.
- **PLATFORM** — a Mission Platform implementation or reference-architecture decision. Lives in `froekjaer/Mission-Platform`.
- **BOTH** — requires a governing principle plus a corresponding implementation. Both repositories are affected, and the two artefacts SHALL reference each other.
- **PAYLOAD-SPECIFIC** — belongs only to one payload (e.g. timelapse) and SHALL NOT be promoted to platform or framework without a separate decision.
- **DEFERRED** — insufficient evidence or premature standardisation. Recorded as a candidate for a later review, not enacted now.

The Meta Review SHALL justify every classification. The classification determines *where* a decision becomes binding: a FRAMEWORK classification becomes a rule for future reviews; a PLATFORM classification becomes an implementation choice; conflating the two silently weakens both.

The classification table is part of the synthesis output.

## Outputs

The meta-review SHALL produce:

- a meta-review record (using the structure of [`review-template.md`](../../review-kit/review-template.md) where applicable);
- a per-element decision table with rationale and origin mapping;
- a Framework/Platform classification table (see § Framework versus Platform classification);
- a project risk register and a cyber/regulatory risk register, kept distinct (see § Risk perspectives);
- a dissent register;
- a shared-component register;
- a risk register for the synthesised architecture;
- an integration plan for `main` with owners and target sequencing;
- explicit residual risk and conditions accepted by the Mission Owner;
- the populated [`META-REVIEW-BOARD.md`](META-REVIEW-BOARD.md);
- a Process Retrospective (see below).

## Process Retrospective

The Meta Review SHALL include a Process Retrospective that evaluates the REVIEW-001 *method itself*, not just the submissions. REVIEW-001 is simultaneously a review of a platform and a test of the review method; if the method has weaknesses, this is where they are caught so they do not repeat in REVIEW-002.

The retrospective SHALL evaluate at minimum:

- whether reviewers received sufficient evidence;
- whether instructions were unambiguous;
- whether independence was preserved;
- whether writable boundaries worked;
- whether deliverables were consistently understood;
- which evidence or methods were missing;
- whether the comparison criteria were sufficient;
- what must change before REVIEW-002;
- which parts of the review method should become permanent Mission Framework standards.

### Required output: REVIEW-001 Process Findings

The retrospective SHALL produce a **REVIEW-001 Process Findings** table with one row per finding and the following columns:

- **finding** — what was observed about the process.
- **evidence** — what supports the finding (e.g. an omission shared across multiple submissions).
- **consequence** — the impact on REVIEW-001's validity or on future reviews.
- **proposed framework change** — the concrete remediation, if any.
- **owner** — who is accountable for enacting the change.
- **target review/version** — when the change applies (REVIEW-002, framework vNext, etc.).

A process finding SHALL NOT be used to retroactively penalise a frozen submission. Its purpose is to improve the method prospectively.

## Integrity

The meta-review SHALL remain independent from delivery pressure, reviewer preference, and brand reputation. Evidence and applicable requirements take precedence.

Material AI-assisted analysis SHALL record the model or service used, the relevant inputs, and the validation performed, in line with the [`evidence-standard`](../../review-kit/evidence-standard.md).

## Closure

REVIEW-001 is closed when the meta-review record is complete, the integration plan is approved by the Mission Owner, and the synthesis is handed off to a separately governed build track on `main`. Closure does not authorise direct merging of any reviewer branch into `main`.
