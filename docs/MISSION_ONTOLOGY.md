# Mission Ontology

> A semantic foundation needs more than definitions. It needs explicit relationships, boundaries and invariants.

## Status

This document defines the **conceptual ontology foundation** for Mission Framework v0.2.

It is intentionally technology-neutral. It is not yet an OWL ontology, RDF vocabulary, database schema or API contract.

The ontology describes meaning first. Machine-readable representations may implement it later without becoming the owner of that meaning.

Canonical term definitions are owned by the Mission Dictionary / canonical glossary. This document focuses on how concepts relate.

## Ontological discipline

Mission Framework distinguishes between:

- **Reality** — what exists or occurs independently of the framework's representation;
- **Representation** — models, records and claims about reality;
- **Purpose** — what motivates intentional change or preservation;
- **Agency** — who or what can act;
- **Authority** — who is permitted to decide or act, and under what bounds;
- **Evidence** — traceable information used to support or contradict claims;
- **Action** — intervention in reality;
- **Learning** — revision caused by outcomes and new evidence.

These distinctions must not be collapsed merely for implementation convenience.

## Canonical mission flow

The Mission Loop is a semantic flow, not a claim that every mission executes as a simple linear process.

```text
Reality
    ↓
Need
    ↓
Mission
    ↓
Objective
    ↓
Capability
    ↓
Operation / Action
    ↓
Observation
    ↓
Evidence
    ↓
Claim
    ↓
Decision
    ↓
Action / Change
    ↓
Outcome
    ↓
Learning
    ↓
Changed understanding and/or changed Reality
```

Feedback may occur between any stages. Named views may show only a subset of this flow, but must not redefine canonical concepts.

## Foundational relationships

The following relationships are provisional semantic invariants for v0.2 and must be tested against real missions.

### Reality and Observation

```text
Reality
  is partially observed through
Observation
```

An Observation is not Reality itself.

No model is assumed to provide complete access to Reality.

### Observation and Evidence

```text
Observation
  may produce
Evidence
```

Not every observation automatically becomes useful evidence.

Evidence must retain sufficient provenance to permit review of what was observed, how, when and by whom or what.

### Evidence and Claim

```text
Evidence
  supports or contradicts
Claim
```

Evidence and Claim are distinct.

Evidence should be describable without requiring acceptance of the Claim it is used to assess.

A Claim may be:

- supported;
- contradicted;
- unresolved;
- superseded.

A Claim may have multiple pieces of supporting and contradicting Evidence.

### Claim and Decision

```text
Claim + Context + Authority
  inform
Decision
```

A Decision must not be represented as an inevitable consequence of Evidence alone.

Judgement, uncertainty, objectives, constraints, authority and consequence may influence a decision.

### Decision and Action

```text
Decision
  authorises, selects or declines
Action
```

Some actions occur without an explicit contemporaneous human decision because authority was delegated earlier. The delegation itself must remain traceable to accountable authority.

### Action and Outcome

```text
Action
  contributes to
Outcome
```

An Outcome must not automatically be attributed solely to an Action. External conditions and other causes may contribute.

### Outcome and Learning

```text
Outcome + Observation + Evidence
  may produce
Learning
```

Learning may revise:

- Claims;
- Decisions;
- models;
- plans;
- capabilities;
- policies;
- the framework itself.

## Mission structure

A Mission is intentional and exists in relation to a perceived Need and desired change or preservation of Value.

A provisional structural view is:

```text
Need
  motivates
Mission

Mission
  pursues
Objective(s)

Objective
  requires
Capability

Capability
  is realised through
People / Process / Information / Technology / Resources

Capability
  enables
Operation and Action
```

This structure is not yet a declaration that every noun shown belongs in Mission Core.

## Agency, authority and accountability

### Actor

An Actor is an entity capable of participating in a mission through observation, reasoning, communication, decision support or action.

Actors may include humans, organisations, teams, software agents, AI systems and mechanisms where appropriate.

Agency does not imply accountability.

### Accountable Authority

Consequential authority must remain traceable to an accountable human or human-governed institution.

### Delegated Authority

```text
Accountable Authority
  grants
Delegation
  to
Actor / Mechanism
  within
Scope + Conditions + Duration
```

Delegation must be:

- explicit enough to inspect;
- bounded in scope;
- revocable where operationally possible;
- attributable to accountable authority;
- auditable through decisions and actions.

Automation does not remove accountability by hiding the original delegation.

## Evidence integrity

Evidence records should preserve original observations and provenance.

Interpretations may change without rewriting the underlying evidence.

Where correction is necessary, the correction should be additive and traceable rather than silently replacing history.

This supports the distinction:

```text
Evidence
    ≠
Interpretation of Evidence
    ≠
Claim
    ≠
Decision
```

## Time

Mission semantics must be able to distinguish at least:

- when something occurred or was observed;
- when it was recorded;
- when a statement or condition is considered valid.

Implementations may use bitemporal or richer temporal models where required.

The ontology must not assume that recording time and reality time are identical.

## Relations as first-class semantic objects

A meaningful relation may require more than `source`, `type`, `target`.

Where consequence requires it, a relation may carry:

- identity;
- provenance;
- creator/observer;
- assertion time;
- validity interval;
- confidence or verification state;
- supporting evidence;
- lifecycle/history.

This is especially important for claims, delegations, dependencies and changing mission conditions.

## Verification and fitness for purpose

Mission Framework separates:

### Verification status

What has been done to establish the integrity, origin or corroboration of information?

from

### Fitness for purpose

Is the information sufficiently relevant, timely, complete and appropriate for a specific use or decision?

Highly verified evidence may be unfit for a particular decision.

Partially verified evidence may still need to inform urgent action when consequences and uncertainty are explicitly understood.

Trust must therefore not be reduced to a single universal scalar.

## Candidate concepts under investigation

The following concepts have emerged through independent review or anticipated mission pressure:

- Claim;
- Delegated Authority;
- Constraint;
- Uncertainty;
- Communication;
- Failure;
- Value;
- Commitment.

Their presence in this ontology does **not** automatically admit them to Mission Core.

Each must be tested through the Core admission procedure and real mission evidence.

## Domain extensions

A domain may introduce concepts that do not belong in Core.

For example, a solar eclipse mission may require domain concepts such as:

- totality;
- cloud cover;
- observation site;
- solar filter;
- contact times.

These concepts can participate in canonical relationships without becoming universal Mission Core concepts.

Domain extensions must not silently redefine canonical terms.

## Framework self-application

Mission Framework is itself subject to its ontology.

```text
Framework use
    ↓
Observation
    ↓
Evidence
    ↓
Framework Finding / Claim
    ↓
Decision
    ↓
Framework Change
    ↓
Validation
    ↓
Learning
```

If credible mission evidence contradicts the ontology, the ontology must be revised or the contradiction explicitly preserved as unresolved.

## Open questions for v0.2

1. Is Need a Core concept, or contextual motivation for Mission?
2. Is Value primitive, derived or relational?
3. Is Objective indispensable across all domains?
4. Is Claim required in Core or only in evidence-governed missions?
5. Is Constraint universal enough for Core?
6. Is Communication a Core concept, a capability, a relation or a domain concern?
7. Is Failure a first-class concept, an event/state, or a relationship between expectation and outcome?
8. How should Uncertainty be represented without collapsing distinct epistemic and operational uncertainties?
9. Which relations require first-class identity and lifecycle?
10. What minimum temporal semantics are mandatory for conformance?

These questions should be answered through evidence, cross-domain testing and explicit decisions — not intuition alone.
