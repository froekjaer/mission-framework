# External Review Synthesis and Disposition

## Purpose

This document consolidates the independent reviews by z.ai, Codex and Claude. It records convergence, unique findings and the project's initial disposition. Reviews are treated as evidence, not authority.

## Overall result

All three reviewers found the foundation promising and the Reality–Observation–Evidence–Decision discipline unusually strong. None recommended abandoning the approach.

The shared condition for proceeding is semantic stabilisation followed by a narrow, executable reference mission. The project is ready for a small experimental vertical slice, but not for freezing a broad ontology or building a general platform.

## Disposition scale

- **Accept** — incorporate into the current stabilisation work.
- **Modify** — accept the concern but adapt the proposed solution.
- **Investigate** — gather evidence before changing Core.
- **Defer** — valid, but not required for the current sprint.
- **Reject** — do not adopt; record the reason.

## Consolidated findings

| Finding | z.ai | Codex | Claude | Disposition |
|---|---:|---:|---:|---|
| Framework must be the canonical semantic source | Yes | Yes | Yes | **Accept** |
| Platform should implement rather than restate semantics | Yes | Yes | Yes | **Accept** |
| Create one canonical glossary/dictionary | Yes | Implied | Yes | **Accept** |
| Define one canonical Mission Loop and label other views | Yes | Implied | Yes | **Accept** |
| Solar Eclipse is not yet a validation case | Yes | Yes | Yes | **Accept** |
| Build a narrow evidence-to-decision vertical slice | Implied | Yes | Compatible | **Accept** |
| Claim is missing from the explicit model | Discussed | Yes | Yes | **Investigate as Experimental Core** |
| Evidence originals must be immutable or append-only | Compatible | Yes | Compatible | **Accept** |
| Relationships require identity, provenance and temporal validity | Compatible | Yes | Compatible | **Accept** |
| Trust and evidence definitions are circular or unstable | Yes | Partly | Yes | **Accept** |
| Split verification history from fitness-for-purpose | Compatible | Compatible | Yes | **Accept** |
| Human/AI accountability requires clearer delegation semantics | Yes | Yes | Yes | **Accept** |
| Add Delegated Authority | Implied | Implied | Yes | **Investigate as Experimental Core** |
| Reality Principle needs an operational evidence-revision rule | Yes | Compatible | Yes | **Accept** |
| Mission Core admission must be procedural and auditable | Discussed | Yes | Yes | **Accept** |
| Constraint and Uncertainty deserve Core evaluation | Yes | Compatible | Compatible | **Investigate** |
| Undefined qualifiers make rules untestable | Partly | Partly | Yes | **Accept** |
| Historical self-claims must be demonstrable | Compatible | Compatible | Yes | **Accept immediately** |

## Decisions adopted in this change set

1. `mission-framework` is the canonical source for definitions and normative semantic invariants.
2. `Mission-Platform` owns schemas, validators, API contracts, tools and implementations that conform to the Framework.
3. Domain repositories own extensions, scenarios, evidence and acceptance cases.
4. `GLOSSARY.md` is introduced as the canonical definition point.
5. One canonical Mission Loop is stated. Other loops must be labelled as views and mapped to it.
6. The Reality Principle is interpreted operationally as an evidence-revision rule: credible contradiction must change the model or remain explicitly unresolved.
7. Verification status and fitness-for-purpose are separate dimensions.
8. Original observations and evidence are immutable or append-only.
9. Mission Core admission requires cross-domain evidence, an extension attempt and an ADR.
10. Claim, Delegated Authority, Constraint, Uncertainty and Commitment remain candidates until tested.

## Required next work

### Framework

- Replace local redefinitions with links to the canonical glossary.
- Map all existing loop diagrams to the canonical Mission Loop.
- reconcile overlapping principle sets and normative language.
- Create ADRs for Experimental Core candidates.

### Platform

- Remove or clearly mark duplicated semantic definitions.
- Define stable identifiers, lifecycle states, temporal fields and typed relationship contracts.
- Add conformance tests for unsupported claims, evidence mutation, contradiction preservation, authority transitions and extension isolation.

### Solar Eclipse

Create one narrow scenario:

> Determine whether to publish viewing guidance for a specified observation site and time window.

The scenario must include sample observations, evidence, conflicting claims or uncertainty, policy, authority, decision, action, outcome criteria and a reproducible replay test.

## Deferred subjects

The following remain valuable but should not block the first vertical slice:

- Mission DSL and compiler
- broad policy engine
- graph visualisation
- aggregate trust dashboards
- advanced AI-assisted reasoning
- additional domain reference models

## Governance note

Acceptance in this document is not proof that an implementation is correct. Each change remains subject to reference-mission validation, conformance tests and future review.