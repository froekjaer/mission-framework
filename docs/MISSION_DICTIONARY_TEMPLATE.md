# Mission Dictionary — Canonical Entry Template

## Purpose

The Mission Dictionary is the normative semantic reference for canonical Mission Framework concepts.

A dictionary entry should make a concept understandable to a human reader, implementable by a technical team and interpretable by an AI system without requiring private conversation history.

This template defines the expected structure.

---

# `<Concept Name>`

## Status

Choose one:

- Canonical Core
- Canonical non-Core
- Candidate Core
- Domain Extension
- Deprecated
- Experimental

Include version introduced and, where applicable, the decision/ADR that established the status.

## Definition

A concise normative definition.

The definition should:

- avoid circular dependency on undefined terms;
- distinguish the concept from its neighbours;
- avoid implementation-specific wording unless implementation is intrinsic to the concept;
- be understandable outside the document in which it appears.

## Purpose

Why does this concept exist in Mission Framework?

What semantic problem does it solve?

## Not to be confused with

List neighbouring concepts that are commonly conflated with this concept and state the distinction.

Example:

```text
Evidence is not Claim.
Observation is not Reality.
Actor is not necessarily Accountable Authority.
```

## Identity

What makes one instance of this concept the same or different from another?

If identity is not meaningful for the concept, state why.

## Lifecycle

Describe meaningful states or transitions where applicable.

Example structure:

```text
Proposed → Active → Superseded → Retired
```

Do not invent lifecycle states merely to fill the template.

## Attributes

List semantic attributes, not database fields.

For each important attribute describe:

- meaning;
- whether it is required conceptually;
- constraints or invariants.

## Relationships

Use explicit verbs.

Example:

```text
Evidence SUPPORTS Claim
Evidence CONTRADICTS Claim
Decision AUTHORISES Action
Authority DELEGATES_TO Actor
```

For each relationship identify:

- source concept;
- verb/relation;
- target concept;
- cardinality if semantically important;
- provenance/temporal requirements if important.

## Invariants

Rules that must remain true for a conforming interpretation.

Examples:

- an Observation is not identical to Reality;
- original Evidence must not be silently rewritten;
- delegated consequential authority must remain traceable to accountable authority.

Invariants should eventually be candidates for conformance tests where machine-testable.

## Temporal semantics

Describe whether the concept distinguishes:

- occurrence/observation time;
- recording time;
- validity time;
- effective period;
- supersession.

## Provenance requirements

What must be known about origin, authorship, observation, transformation or custody?

## Verification and uncertainty

Describe how verification status, confidence, uncertainty or fitness-for-purpose apply, if at all.

Do not use a universal trust score where multiple dimensions are semantically distinct.

## Authority and accountability

If the concept can influence consequential decisions or actions, explain how authority and accountability relate to it.

## Examples

Provide examples from more than one domain where possible.

Examples should demonstrate the definition rather than quietly expand it.

## Counterexamples

Show cases that may look similar but are not instances of the concept.

## Anti-patterns

Document common modelling errors or dangerous simplifications.

## Extension rules

Explain what domain extensions may add without redefining the canonical concept.

## Core admission evidence

Required for Core or Candidate Core concepts.

Record:

- domains examined;
- demonstrated semantic need;
- attempted extension-only modelling;
- failure or insufficiency of that modelling;
- supporting Framework Findings;
- decision/ADR.

## Open questions

List unresolved semantic questions explicitly.

Uncertainty should be visible rather than hidden behind premature definitions.

## References

Link to:

- canonical principles;
- ontology sections;
- ADRs;
- Framework Findings;
- review evidence;
- domain examples.

---

## Dictionary quality test

Before a concept is considered stable, ask an independent human and an independent machine to answer:

1. What does this concept mean?
2. What does it explicitly not mean?
3. How is it identified?
4. What can it relate to?
5. What rules must always hold?
6. How may a domain extend it?
7. Could two independent implementations represent it compatibly?

If materially different answers arise, the entry is not yet semantically stable.
