# Framework Findings

## Purpose

A **Framework Finding** records evidence that a real mission cannot be represented, governed or improved cleanly using the current Mission Framework semantics.

Framework Findings are the formal feedback path from mission reality back into framework evolution.

They prevent domain missions from hiding semantic gaps through undocumented local conventions.

## Core rule

> **Do not make a mission fit the framework by force. Record the mismatch.**

A Framework Finding does not automatically prove that the framework is wrong or that a new Core concept is required. It creates a traceable claim that must be examined.

## When to create a Framework Finding

Create one when a mission reveals, for example:

- a necessary concept that cannot be expressed cleanly;
- an existing canonical concept that has two materially different meanings in practice;
- a required relationship that the ontology cannot represent;
- a lifecycle or state transition that violates an existing invariant;
- an authority or accountability path that cannot be traced;
- evidence that contradicts a normative assumption in the framework;
- a domain workaround that would silently redefine Core;
- a recurring ambiguity that causes materially different interpretations.

Do not create one merely because a domain needs additional vocabulary. Domain extensions are expected.

## Minimum record

Each Framework Finding should contain:

### Finding
A concise description of the mismatch.

### Mission context
Where and under what conditions it was discovered.

### Observation
What was actually observed.

### Evidence
The evidence supporting the finding, including provenance where available.

### Claim
What is being claimed about the framework.

### Impact
What becomes ambiguous, impossible, unsafe, misleading or unnecessarily difficult if the finding is not addressed.

### Attempted modelling
How the mission attempted to use existing Core concepts or extension mechanisms.

### Workaround
Any temporary local workaround, clearly marked as non-canonical.

### Candidate disposition
One or more hypotheses, such as:

- clarify documentation;
- refine an existing definition;
- add or change a relationship;
- create a domain extension;
- evaluate a new Core candidate;
- change an invariant;
- reject the finding with rationale.

## Disposition

A Framework Finding should eventually receive one of these dispositions:

- **Accepted — documentation**
- **Accepted — semantic refinement**
- **Accepted — extension**
- **Accepted — Core candidate**
- **Deferred — more evidence required**
- **Rejected — framework already expresses the case adequately**
- **Rejected — outside framework scope**

A Core candidate still must pass the Mission Core admission procedure.

## Traceability

Where practical, the chain should remain visible:

```text
Mission Reality
    ↓
Observation
    ↓
Evidence
    ↓
Framework Finding / Claim
    ↓
Review and Decision
    ↓
Framework Change or Rejection
    ↓
Validation in Mission Reality
```

This is the framework applying its own principles to itself.

## Independence from predicted gaps

Potential missing concepts such as Constraint, Communication or Failure may be useful hypotheses.

A real mission must not be instructed to manufacture evidence for them.

If they are genuinely necessary, the mission should expose that necessity through actual modelling pressure and evidence.

## Principle

Framework evolution is not driven by vocabulary accumulation.

It is driven by demonstrated semantic need.
