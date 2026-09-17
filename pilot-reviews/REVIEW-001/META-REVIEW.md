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

## Synthesis into the reference architecture

The meta-review SHALL produce a synthesis that becomes the input to a separately governed reference architecture on `main`. The synthesis SHALL:

- identify selected elements per architecture layer;
- preserve dissenting but reasoned alternatives;
- record the mapping from selected elements to their originating reviewer submission;
- identify gaps that none of the reviewers addressed;
- propose the integration sequence for `main`.

## Outputs

The meta-review SHALL produce:

- a meta-review record (using the structure of [`review-template.md`](../../review-kit/review-template.md) where applicable);
- a per-element decision table with rationale and origin mapping;
- a dissent register;
- a shared-component register;
- a risk register for the synthesised architecture;
- an integration plan for `main` with owners and target sequencing;
- explicit residual risk and conditions accepted by the Mission Owner.

## Integrity

The meta-review SHALL remain independent from delivery pressure, reviewer preference, and brand reputation. Evidence and applicable requirements take precedence.

Material AI-assisted analysis SHALL record the model or service used, the relevant inputs, and the validation performed, in line with the [`evidence-standard`](../../review-kit/evidence-standard.md).

## Closure

REVIEW-001 is closed when the meta-review record is complete, the integration plan is approved by the Mission Owner, and the synthesis is handed off to a separately governed build track on `main`. Closure does not authorise direct merging of any reviewer branch into `main`.
