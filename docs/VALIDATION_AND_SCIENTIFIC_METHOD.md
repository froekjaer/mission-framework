# Validation and Scientific Method

**Status:** Normative for Foundation v1.1 validation work  
**Applies to:** Mission Framework and reference missions

## 1. Purpose

This document defines how Mission Framework propositions are tested against reality.

The method is designed to prevent internal coherence, documentation volume, reviewer enthusiasm or author authority from being mistaken for empirical validity.

## 2. Unit of validation

A validation concerns a bounded proposition, not the framework as an indivisible whole.

Each proposition shall state:

- the claimed benefit or protective effect
- the context in which the claim is expected to hold
- the affected stakeholders
- the observable indicators
- the credible comparison or counterfactual
- the conditions that would weaken or falsify the claim

Example:

> Using explicit evidence provenance in a reference mission reduces the time required by an independent reviewer to reconstruct why a consequential decision was made.

## 3. Required distinctions

Validation records shall distinguish:

### Observation

A recorded event, state, measurement or artefact with provenance and time.

### Interpretation

A reasoned explanation of one or more observations.

### Claim

A proposition that may be supported, qualified or challenged by evidence.

### Evidence

Information judged relevant to a claim, with sufficient provenance, integrity, context and uncertainty for the intended decision.

### Finding

A documented tension, confirmation, ambiguity, failure or improvement opportunity identified through implementation, review or comparison.

### Decision

An accountable disposition based on claims, evidence, constraints and consequences.

These categories must not be silently collapsed.

## 4. Validation protocol

Each validation cycle shall contain the following sections.

### 4.1 Proposition

State the exact framework proposition being tested.

### 4.2 Context and boundaries

Record mission scope, actors, tools, constraints, dates and excluded concerns.

### 4.3 Baseline or counterfactual

Define a credible comparison. Preferred forms are:

1. the same task performed without the framework control
2. the same task performed with a simpler established method
3. a historical baseline with sufficiently comparable conditions
4. an independent reconstruction benchmark
5. an expert judgement baseline, explicitly marked as weaker evidence

A framework-only implementation without a comparison may demonstrate feasibility, but cannot by itself demonstrate superiority.

### 4.4 Measures

Select the smallest useful set of measures. Measures may include:

- outcome achievement
- decision quality
- traceability completeness
- independent reconstruction success
- error or contradiction detection
- time and effort
- rework
- accessibility
- governance burden
- user comprehension
- operational resilience
- trust calibration

Measures shall include undesirable effects and costs, not only intended benefits.

### 4.5 Evidence plan

Specify in advance:

- what will be captured
- where it will be stored
- who may alter it
- how provenance and integrity are preserved
- how uncertainty and missing evidence are represented
- which evidence is sensitive or restricted

### 4.6 Execution

Run the mission work without silently changing the proposition or success threshold. Deviations shall be recorded.

### 4.7 Analysis

Compare observed results with the baseline and the stated falsification conditions. Separate measured results from interpretation.

### 4.8 Disposition

Use one of the following dispositions:

- **Supported** — evidence supports the proposition in the tested context
- **Partially supported** — some benefits are supported, with material qualifications
- **Inconclusive** — evidence is insufficient or comparison is not credible
- **Challenged** — evidence conflicts with the proposition
- **Falsified in context** — the proposition failed under the stated conditions
- **Not tested** — implementation occurred, but no valid test was performed

A result is never generalised beyond its tested context without an explicit argument and uncertainty statement.

## 5. Framework Findings

Any observation that may affect canonical semantics shall be submitted through the Framework Findings process.

Validation reports do not directly rewrite Mission Core. They produce evidence and findings for accountable disposition.

Rejected findings remain in the historical record with the reason for rejection.

## 6. Independent challenge

At least one validation in each release cycle should permit an independent person or AI system to:

- locate the relevant artefacts
- reconstruct the tested proposition
- reproduce the analysis where feasible
- identify missing assumptions
- challenge the disposition

AI output may accelerate analysis but is not independent authority merely because a different model produced it.

## 7. Negative results

Negative, null and inconclusive results are valid programme outputs.

They shall not be hidden, rewritten as success or excluded solely because they weaken the framework's apparent value.

## 8. Replication

A proposition should not be promoted as broadly validated on the basis of one mission.

Where consequences justify it, seek replication across:

- another mission
- another implementation team
- another toolchain
- another reviewer
- another operational context

## 9. Minimum validation report

Each report shall contain:

```text
Identifier
Version and date
Proposition
Context and boundaries
Baseline or counterfactual
Measures
Evidence locations
Execution deviations
Results
Uncertainty and limitations
Adverse effects and burden
Disposition
Framework Findings raised
Responsible decision owner
Independent review status
```

## 10. Ethical and governance constraints

Validation shall not create disproportionate risk merely to test the framework.

Privacy, safety, legal obligations, consent, security and stakeholder consequences remain governing constraints. Where a stronger experiment would be unethical or impractical, the limitation shall be explicit.

## 11. Scientific posture

Mission Framework does not claim scientific status by using scientific language.

Its claims earn credibility only through precise propositions, observable consequences, credible comparison, preserved evidence, independent challenge and willingness to revise or abandon unsupported concepts.