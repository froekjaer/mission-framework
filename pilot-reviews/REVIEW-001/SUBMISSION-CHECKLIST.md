# REVIEW-001 Submission Checklist (Framework Gate)

## Purpose

This document is the framework-owned submission gate for REVIEW-001. It defines the conditions a submission SHALL meet before it is accepted into blind comparison.

The reviewer-fillable version lives in the destination repository at:

- `froekjaer/Mission-Platform/review-lab/REVIEW-001/SUBMISSION-CHECKLIST.md`

That reviewer version is where each reviewer records their frozen submission commit, identity, and per-item confirmation. This document is the normative gate those items are checked against.

Normative words follow the [`terminology-standard`](../../review-kit/terminology-standard.md).

## Submission identity (recorded in the reviewer copy)

A complete submission MUST record:

- reviewer name or system;
- workspace branch (`review/review-001-<reviewer>`);
- frozen submission commit SHA;
- submission date;
- reviewer declaration that the submission is ready for blind comparison.

## Independence gate — MUST

- [ ] The reviewer worked from the shared frozen baseline (`eed9e3c8c67369e1924c25a11908616220c3c753`).
- [ ] The reviewer did not inspect another reviewer workspace before freezing this submission.
- [ ] External sources, tools, and collaborators are disclosed.
- [ ] No write was performed in `froekjaer/timelapse-pro`.
- [ ] No write was performed outside the assigned workspace.

## Deliverables gate — MUST

All of the following SHALL be present in the workspace:

- [ ] Business architecture
- [ ] Conceptual architecture
- [ ] Logical architecture
- [ ] Physical architecture
- [ ] Component model
- [ ] ADRs
- [ ] Migration strategy
- [ ] Operational model
- [ ] Implementation
- [ ] Tests
- [ ] Evidence
- [ ] Risk register
- [ ] Roadmap

## Architecture and traceability — MUST

- [ ] Platform/payload boundary is explicit.
- [ ] Control-plane and data-plane contracts are explicit.
- [ ] Every material decision has an ADR that answers Why? / Because? / For whom?
- [ ] Every migrated source element is traceable to the frozen baseline.
- [ ] Rejected or replaced source elements are explained.
- [ ] Source-to-target traceability shows reused, adapted, rewritten, and rejected elements.

## Security, safety, compliance — SHOULD

- [ ] Trust boundaries and threat assumptions are documented.
- [ ] Privileges and capabilities fail closed.
- [ ] Data ownership, classification, retention, and deletion are defined.
- [ ] AI purpose, prompts, provider use, and result ownership are governed.
- [ ] Relevant GDPR, AI Act, CRA, NIS2, IEC 62443, and ISO 27000 implications are mapped or marked not applicable with rationale, with reference to the [`regulatory-horizon`](../../review-kit/regulatory-horizon.md) where applicable.

## Risk perspectives

Risk SHALL be considered from two distinct perspectives, per [`reviews/MIAR/RISK-METHOD.md`](../../reviews/MIAR/RISK-METHOD.md):

1. **Project and implementation risk** — risks to the project, system, implementation, governance, adoption and long-term viability.
2. **Cybersecurity, architecture and regulatory risk** — risks arising from architecture, software, AI, data, operations, supply chain, privacy, resilience and legal obligations.

### Fairness notice (REVIEW-001)

The original REVIEW-001 invitation did not explicitly require two separate risk registers. Therefore a REVIEW-001 submission SHALL NOT be marked non-compliant solely because it combined the two perspectives into one register. A combined register is acceptable for REVIEW-001; the Meta Review MAY normalise it into the two perspectives for comparison while preserving the reviewer's original evidence and intent.

### Prospective rule (from REVIEW-002 onward)

From REVIEW-002 onward, reviewers SHALL submit two separate risk analyses following [`reviews/MIAR/RISK-METHOD.md`](../../reviews/MIAR/RISK-METHOD.md), unless the review invitation explicitly states otherwise. This prospective rule does not apply to REVIEW-001.

## Evidence and quality — MUST

- [ ] Architectural claims are linked to evidence in accordance with the [`evidence-standard`](../../review-kit/evidence-standard.md).
- [ ] Executable claims have tests or runtime evidence.
- [ ] AI-generated content is validated against source material and not used as evidence by itself.
- [ ] Assumptions and uncertainty are explicit.
- [ ] Risks have owners, consequences, and proposed treatment.

## Collaborative intelligence — SHOULD

- [ ] Contributor types are recommended for each major layer.
- [ ] Recommendations include strengths, limitations, and validation needs.
- [ ] Human accountability and final decision authority are explicit.
- [ ] A candid reviewer self-assessment of strongest and weakest areas is included.

## Handover — MUST

- [ ] Executive summary is complete.
- [ ] Roadmap and next safe step are identified.
- [ ] Final commit SHA is recorded.
- [ ] Implementation stopped after the submission freeze, pending meta-review.

## Freeze

A submission is complete only when every MUST item above is satisfied and the frozen commit SHA is recorded. After freeze, the reviewer SHALL NOT continue implementation until the meta-review concludes.
