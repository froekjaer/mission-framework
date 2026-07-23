# Mission Framework Governance

## Purpose

This document defines how Mission Framework is governed, changed, reviewed, and released.

## Principles

- Openness
- Traceability
- Evidence-based decision making
- Engineering discipline
- Proportionality
- Human accountability
- Continuous improvement

## Project structure

Mission Framework consists of three tracks:

- **Standards** — approved normative content and reusable requirements.
- **Research** — evidence, hypotheses, alternatives, and material under evaluation.
- **Build** — repository structure, templates, tooling, examples, and release assets.

The Review Kit supports all three tracks but does not replace accountable human decisions.

## Roles

### Maintainer

A maintainer SHALL:

- preserve the integrity of the repository;
- ensure that governance and review requirements are applied;
- approve, reject, or defer material changes;
- manage releases and versioning;
- document significant decisions.

### Contributor

A contributor SHALL:

- identify the purpose and track of a proposed change;
- provide sufficient rationale and evidence;
- address review findings;
- preserve traceability and attribution.

### Reviewer

A reviewer SHALL:

- assess content independently;
- record findings with evidence and severity;
- distinguish fact, inference, assumption, and opinion;
- disclose conflicts of interest;
- avoid approving work not reviewed in substance.

### Decision-maker

The decision-maker accepts or rejects material changes and any residual risk. The maintainer may act as decision-maker unless independence is required.

## Decision model

Routine, low-risk changes may be approved by a maintainer after proportionate review.

Material changes require:

1. a documented proposal or pull request;
2. review appropriate to impact and risk;
3. resolution or explicit acceptance of blocking findings;
4. a recorded decision and rationale;
5. an identifiable accountable person.

Where reviewers disagree, the decision record SHALL summarize the competing positions and explain the chosen outcome.

## Change classes

- **Editorial:** wording, formatting, spelling, or references without changed meaning.
- **Minor:** backward-compatible clarification or capability.
- **Major:** changed normative meaning, governance, architecture, or compatibility.
- **Emergency:** urgent correction required to address material harm, illegality, or security risk.

Review depth SHALL be proportional to the change class and potential impact.

## Review requirements

A material change SHALL be reviewed for:

- purpose and scope;
- internal consistency;
- evidence quality;
- terminology;
- implementation feasibility;
- dependencies and compatibility;
- safety, security, legal, ethical, and operational risk;
- traceability.

Critical findings block approval. Major findings block approval unless an authorized decision-maker explicitly accepts the residual risk and records the rationale.

## AI use

AI MAY support research, drafting, analysis, testing, and review. AI SHALL NOT be treated as the accountable approver.

Material AI-generated or AI-assisted content SHALL be checked by a human for accuracy, provenance, confidentiality, bias, omissions, and fabricated evidence.

## Records and traceability

Significant changes SHALL be traceable through one or more of:

- commits;
- pull requests;
- issues;
- review records;
- decision records;
- changelog entries;
- release notes.

Records should identify the component, version or commit, author, reviewer, decision-maker, date, findings, decision, and evidence.

## Releases

A release SHALL:

- have a unique version;
- identify included changes;
- satisfy defined exit criteria;
- have no unresolved unaccepted blocking findings;
- update the changelog;
- preserve reproducible source material.

Pre-release versions may be used while the framework remains under development.

## Exceptions

An exception to a normative governance requirement SHALL be:

1. explicit;
2. time-bound or scope-bound;
3. justified;
4. approved by an accountable decision-maker;
5. recorded with residual risk and compensating controls.

## Governance changes

Changes to this document are Major changes and require documented review and approval.
