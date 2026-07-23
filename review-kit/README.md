# Mission Framework Review Kit

## Purpose

The Review Kit defines a consistent, traceable process for reviewing Mission Framework components before they become normative, reusable, or release-ready.

It is designed for both human reviewers and AI-assisted review.

## Review objectives

A review SHALL determine whether a component is:

- clear and internally consistent;
- aligned with the Mission Framework purpose and governance model;
- supported by evidence appropriate to its claims;
- usable by its intended audience;
- traceable to decisions, sources, and changes;
- safe to reuse in later standards, research, or implementations.

## Review scope

Reviews MAY cover:

- standards and normative requirements;
- research notes and evidence summaries;
- architecture and implementation guidance;
- templates, examples, and operating procedures;
- governance and decision records;
- release candidates and repository changes.

The review scope SHALL identify what was reviewed, what was excluded, and the exact version or commit assessed.

## Review levels

### Level 1 — Editorial review

Used for low-risk wording, formatting, references, and structural clarity. It verifies that meaning has not unintentionally changed.

### Level 2 — Technical review

Used for substantive content. It assesses correctness, consistency, evidence, feasibility, dependencies, and risk.

### Level 3 — Independent assurance review

Used for high-impact, safety-sensitive, security-sensitive, legally significant, or release-critical components. The reviewer should be independent of the author and suitably competent for the subject.

The selected level SHALL be proportionate to impact, uncertainty, novelty, and reversibility.

## Required review assets

The Review Kit consists of:

- `reviewer-mission.md` — reviewer responsibilities and conduct;
- `review-template.md` — standard review record;
- `severity-classification.md` — consistent finding severity;
- `evidence-standard.md` — evidence quality and traceability requirements when added.

## Review process

1. Identify the component, owner, version, and review level.
2. Define scope, exclusions, criteria, and dependencies.
3. Collect and validate relevant evidence.
4. Assess the component independently.
5. Record findings using the standard template.
6. Classify findings using the severity standard.
7. Allow the owner to respond and remediate.
8. Verify material remediation.
9. Record the final decision and residual risk.
10. Preserve the review record with the reviewed version.

## Finding requirements

Each finding SHALL include:

- a unique identifier;
- a concise title;
- severity;
- affected location or component;
- observed condition;
- expected condition or criterion;
- impact and rationale;
- supporting evidence;
- recommended action;
- status and owner where applicable.

## Review statuses

- **Draft** — review is being prepared.
- **In review** — assessment is active.
- **Awaiting response** — findings require owner input.
- **Remediation in progress** — corrective work is underway.
- **Ready for decision** — review work is complete.
- **Approved** — component is accepted for its stated purpose.
- **Approved with conditions** — acceptance depends on recorded conditions.
- **Changes required** — blocking findings remain.
- **Rejected** — component is unsuitable for the stated purpose.
- **Superseded** — a later review replaces this record.

## Decision rules

- Critical findings block approval.
- Major findings normally block approval.
- A Major finding may be accepted only by an authorized decision-maker with documented rationale, residual risk, and conditions.
- Minor findings may be deferred with an owner and target disposition.
- Observations do not block approval but should be considered.

## AI-assisted review

AI MAY assist with consistency checks, source comparison, gap analysis, drafting findings, and test generation.

A human SHALL remain accountable for:

- review scope;
- factual verification;
- evidence quality;
- severity and decision;
- confidentiality and data protection;
- final approval.

AI output SHALL be treated as unverified until checked against the component and authoritative evidence.

## Traceability

A completed review SHALL identify:

- the exact reviewed version or commit;
- reviewer and date;
- criteria and evidence;
- findings and dispositions;
- remediation references;
- final decision and decision-maker;
- residual risks and conditions.

## Completion criteria

A review is complete when the scope has been assessed, findings are recorded, blocking issues are resolved or formally accepted, the decision is documented, and the record is stored with sufficient traceability for another competent reviewer to reproduce the conclusion.
