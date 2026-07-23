# Documentation Standard

Version: 1.0  
Status: Approved  
Category: Core Review Standard  
Owner: Mission Framework Maintainers  
Review Cycle: Annual or after material framework change

---

## Purpose

This standard defines the minimum requirements for creating, structuring, maintaining, reviewing, and retiring documentation within the Mission Framework.

The objective is to ensure that documentation is clear, complete, accurate, consistent, traceable, maintainable, and suitable for both operational use and independent review.

---

## Scope

This standard applies to all Mission Framework documentation, including:

- core standards;
- review-kit documents;
- governance material;
- procedures and runbooks;
- templates and checklists;
- decision records;
- implementation guidance;
- evidence descriptions;
- release notes and change records; and
- machine-generated or AI-assisted documentation.

---

## Fundamental Principle

Documentation SHALL be sufficient for an informed reader to understand:

1. what the document is for;
2. who it applies to;
3. what requirements or guidance it contains;
4. how it relates to other Mission Framework material;
5. what has changed over time; and
6. who is responsible for maintaining it.

Documentation SHALL NOT depend on undocumented assumptions, private knowledge, or inaccessible context.

---

## Documentation Principles

### Clarity

Documentation SHALL use plain, precise, and unambiguous language.

Specialist terminology MAY be used where necessary, but terms SHALL follow the Terminology Standard and SHALL be defined when a reasonable reader may not understand them.

### Completeness

A document SHALL include all information required to fulfill its stated purpose.

Known gaps, unresolved questions, and dependencies SHALL be identified explicitly rather than omitted.

### Accuracy

Statements presented as fact SHALL be correct to the best available knowledge and supported by evidence or authoritative references where appropriate.

Outdated, superseded, or uncertain information SHALL be marked clearly.

### Consistency

Documentation SHALL use consistent terminology, formatting, requirement language, and document structure across the framework.

Equivalent concepts SHALL NOT be described differently without an intentional and documented reason.

### Maintainability

Documentation SHALL be structured so that future maintainers can update it without reconstructing the original author's intent.

Requirements, rationale, examples, and references SHOULD be separated where practical.

### Traceability

Material requirements, decisions, evidence, and changes SHALL be traceable in accordance with the Traceability Standard.

---

## Required Document Metadata

Every normative Mission Framework document SHALL include, at minimum:

- **Title** — the official document name;
- **Version** — the current document version;
- **Status** — for example Draft, Proposed, Approved, Deprecated, or Retired;
- **Category** — the document class or framework area;
- **Owner** — the role or group responsible for maintenance; and
- **Review Cycle** — the expected review frequency or review trigger.

Where relevant, a document SHOULD also include:

- effective date;
- last review date;
- next review date;
- related standards;
- superseded document;
- approval authority; and
- confidentiality or distribution classification.

---

## Mandatory Structure

Normative standards SHALL normally contain the following sections:

1. Purpose;
2. Scope;
3. Fundamental Principle;
4. Requirements;
5. Roles and Responsibilities;
6. Exceptions;
7. Review and Maintenance;
8. Related Documents; and
9. Change History.

A section MAY be omitted where it is genuinely not applicable, but the document structure SHALL remain understandable and internally consistent.

Templates, procedures, and guidance documents MAY use a different structure when this better supports their purpose.

---

## Requirement Language

Normative documents SHALL use the following terms consistently:

- **SHALL** — mandatory requirement;
- **SHALL NOT** — mandatory prohibition;
- **SHOULD** — recommended practice where deviation requires justification;
- **SHOULD NOT** — discouraged practice where use requires justification; and
- **MAY** — permitted option.

Lowercase alternatives such as "must", "should", or "may" SHOULD NOT be used to express formal framework requirements unless they appear in quoted material.

---

## Sources and References

References SHALL be sufficiently specific for another person to locate the source.

A reference SHOULD include, where available:

- author or issuing organization;
- title;
- version or publication date;
- section, page, control, or clause;
- stable identifier or link; and
- access date where online content may change.

A document SHALL distinguish between:

- authoritative requirements;
- supporting evidence;
- explanatory guidance;
- examples; and
- author interpretation.

---

## Change Documentation

Every material document change SHALL be recorded through version control.

The change record SHALL make clear:

- what changed;
- why it changed;
- who approved or committed the change;
- when the change occurred; and
- whether related documents require review.

Commit messages SHALL identify the relevant BUILD, repair, release, or maintenance activity where applicable.

Changes that alter normative meaning SHALL result in an appropriate version update.

---

## Document Status

The following statuses SHALL be used consistently:

- **Draft** — under active development and not approved for normative use;
- **Proposed** — complete enough for formal review;
- **Approved** — authorized for use;
- **Deprecated** — still available but no longer recommended;
- **Superseded** — replaced by another identified document; and
- **Retired** — no longer active and retained only for history or audit purposes.

A deprecated, superseded, or retired document SHALL identify its replacement where one exists.

---

## AI-Assisted Documentation

AI tools MAY be used to draft, restructure, summarize, or review documentation.

AI-generated or AI-assisted content SHALL be subject to human review before approval.

The reviewer SHALL verify:

- factual accuracy;
- completeness;
- internal consistency;
- appropriate terminology;
- source validity;
- absence of fabricated references;
- confidentiality and privacy compliance; and
- alignment with Mission Framework standards.

AI output SHALL NOT be treated as evidence solely because it is well written or plausible.

---

## Roles and Responsibilities

### Document Owner

The document owner SHALL:

- maintain the document;
- ensure scheduled review;
- coordinate material updates;
- resolve identified inconsistencies; and
- initiate deprecation or retirement when appropriate.

### Author or Contributor

Authors and contributors SHALL follow this standard and SHALL identify assumptions, limitations, and unresolved issues.

### Reviewer

Reviewers SHALL assess documentation for accuracy, clarity, completeness, consistency, traceability, and suitability for the intended audience.

### Maintainer

Repository maintainers SHALL preserve version history, review commit quality, and ensure approved documents remain accessible.

---

## Exceptions

An exception to this standard SHALL be documented and SHALL include:

- the requirement being waived;
- the reason for the exception;
- the responsible owner;
- the associated risk;
- compensating measures, if any; and
- an expiry or review condition.

Permanent undocumented exceptions are not permitted.

---

## Review and Maintenance

This standard SHALL be reviewed at least annually or when:

- the Mission Framework document model changes;
- repository governance changes;
- material documentation quality issues are identified;
- new publication formats are introduced; or
- related standards are materially revised.

Review findings SHALL be recorded through the repository workflow.

---

## Related Documents

- `CONTRIBUTING.md`
- `GOVERNANCE.md`
- `CHANGELOG.md`
- `review-kit/evidence-standard.md`
- `review-kit/traceability-standard.md`
- `review-kit/terminology-standard.md`
- `review-kit/review-decision-standard.md`

---

## Change History

| Version | Change | Status |
|---|---|---|
| 1.0 | Initial approved Documentation Standard | Approved |
