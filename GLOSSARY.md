# Mission Framework Glossary

> This document is the canonical source for Mission Framework terminology.

Normative definitions belong here. Other documents may explain, illustrate or apply these concepts, but should link to this glossary rather than silently redefine them.

## Normative language

- **Must / shall** — a conformance requirement.
- **Should** — a recommended default that may be departed from with an explicit reason.
- **May** — an optional choice.

## Core concepts

### Reality

That which exists or occurs independently of the framework's models, records or beliefs.

Reality is not directly available to a mission in full. It is approached through observation and evidence. Operationally, the Reality Principle requires models and decisions to yield to credible contradictory evidence or to preserve the contradiction explicitly until it can be resolved.

### Need

A condition affecting people, organisations, society or the physical world that provides a justified reason for action.

A need is treated as **genuine** when its existence is supported by evidence from or about those affected, rather than solely by the assertion of those proposing the mission. This status remains revisable.

A mission may also arise from an opportunity, obligation or externally imposed condition. These must be made explicit rather than being forced into the word "need".

### Value

A beneficial change in reality for identified stakeholders, assessed against the mission's stated need, objectives, consequences and evidence.

Value is not assumed because an output was produced. It must be demonstrated through outcomes.

### Mission

A governed undertaking established to create a defined change in reality in response to a need, opportunity, obligation or condition.

A Mission has an accountable authority, objectives, scope, lifecycle and evidence of progress and outcome. A standing organisational purpose may sponsor multiple Missions but is not itself automatically a bounded Mission.

### Objective

A defined, assessable outcome that contributes to a Mission.

### Outcome

An observed or assessable change in reality resulting wholly or partly from mission activity.

An Objective is desired; an Outcome is what occurred.

### Actor

A person, organisation, system or mechanism capable of performing an action or participating in a relationship.

Being an Actor does not itself confer authority or accountability.

### Stakeholder

A person, group or organisation affected by, interested in or able to affect a Mission.

### Capability

The ability to produce an outcome or effect under specified conditions.

### Service

A governed means by which a Capability is made available to a consumer or another Capability.

### Workflow

An organised sequence or network of activities performed to produce an output or outcome.

### Observation

A recorded result of perceiving, measuring or detecting some aspect of reality through an identified observer, sensor, method or process.

An Observation is not the same as the reality observed.

### Evidence

An Observation, record or artefact placed in mission context and accompanied by sufficient provenance, integrity information and relevance to support or challenge a Claim.

Evidence is not truth by declaration. Original Evidence must be preserved as immutable or append-only; corrections and interpretations must be recorded as new, linked records.

### Claim

A reviewable statement about reality, a Mission, an Objective, an Outcome or another model element that may be supported, challenged or qualified by Evidence or explicit assumptions.

A material Claim must identify its provenance, status and applicable time.

### Knowledge

A structured and reviewable relationship between Evidence, Claims, context, time and uncertainty that has survived an appropriate challenge process for a stated purpose.

### Decision

An authorised selection among alternatives, including a decision to act, not act, continue, stop, delegate or revise.

A consequential Decision must identify its accountable authority, time, basis and applicable policy. A mechanism may execute a delegated decision but is not thereby the ultimate accountable authority.

### Delegated Authority

A recorded Decision by an accountable human or organisational authority that permits another Actor or mechanism to act within explicit bounds.

Delegated Authority must define scope, permitted actions, validity period, conditions, oversight, revocation criteria and accountability path. Organisational accountability must resolve to an identifiable role.

### Action

An intentional change, intervention or execution performed by an Actor under direct or delegated authority.

### Learning

A justified change to knowledge, policy, capability, architecture or behaviour resulting from reviewed Evidence and Outcomes.

### Trust

A purpose-relative judgement that reliance is justified under stated conditions and consequences.

Trust is not an intrinsic property of a person, system or Evidence item. It is assessed for a specific use, stakeholder, time and consequence.

### Verification status

A factual description of what validation activity has occurred, for example Unknown, Observed, Verified or Corroborated.

Verification status must not be confused with fitness for use.

### Fitness for purpose

A Decision that Evidence, a Claim, Capability or other element is fit, not fit or not yet assessed for a stated purpose at a stated time.

### Provenance

Information sufficient to understand where something came from, who or what produced it, when and under which method, version, configuration and custody history.

### Relationship

A typed, directional and potentially temporal association between model elements.

A material Relationship must have its own identity, provenance, status and validity interval where applicable. Relationships must not be reduced to unqualified generic edges when their semantics affect decisions.

### Constraint

A condition that limits permitted states, choices, actions, designs or outcomes.

### Uncertainty

A recognised limitation in knowledge about reality, including incomplete observation, ambiguity, variability, model limitation or unresolved contradiction.

Unknown values must remain unknown rather than being fabricated or silently converted to certainty.

## Load-bearing qualifiers

### Material

Significant enough to affect a mission objective, decision, stakeholder, risk, legal duty, evidence interpretation or outcome.

Materiality thresholds are defined by mission policy and must be proportional to consequence.

### Consequential

Capable of producing material effects on people, rights, safety, obligations, resources, mission outcomes or irreversible states.

Decisions are treated as consequential by default unless an approved policy explicitly delegates or classifies them otherwise.

### Sufficient

Meeting the explicitly stated evidence, assurance and authority requirements for a defined purpose and consequence at a defined time.

### Justified

Supported by Evidence and reasoning that have survived the challenge and approval process required for the stated purpose and consequence.

## Canonical Mission Loop

The canonical Mission Loop is:

```text
Reality
  ↓
Need / Opportunity / Obligation / Condition
  ↓
Mission
  ↓
Objective
  ↓
Capability and Action
  ↓
Observation
  ↓
Evidence
  ↓
Claim and Knowledge
  ↓
Decision
  ↓
Action
  ↓
Outcome
  ↓
Learning
  ↓
Reality
```

Other diagrams may present architectural, operational, evidence or intelligence views of this loop. Such views must state what they expand, omit or aggregate and must not redefine the underlying concepts.

## Governance

Changes to a Core definition require an Architecture Decision Record and evidence that the change improves cross-domain coherence. Platform schemas and domain extensions must conform to the versioned definitions in this glossary.