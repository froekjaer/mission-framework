# Mission Framework

> **From Need to Value**

**Foundation Release v1.0**

Mission Framework is the semantic core of the [Collaborative Intelligence](https://github.com/froekjaer/collaborative-intelligence) research programme. It provides an open architectural foundation for understanding, designing and improving governed missions that seek to create meaningful, trustworthy value.

Its purpose is simple:

> **Create what is needed, and make it accessible to those who need it.**

Architecture, governance, security and technology are essential, but they are means rather than ends. They exist to help justified needs, opportunities and obligations become sustainable value.

## Role in the research programme

Mission Framework owns the programme's normative semantics: canonical terms, foundational principles, the Mission Loop, evidence and trust concepts, governance semantics and the rules by which the semantic core may change.

The framework is intentionally separated from its implementations:

- [Collaborative Intelligence](https://github.com/froekjaer/collaborative-intelligence) provides the programme-level research vision and architecture.
- [Mission Solar Eclipse](https://github.com/froekjaer/mission-solar-eclipse) is the first reference implementation and empirical challenge to the framework.
- [Publication Pipeline](https://github.com/froekjaer/-Publication-Pipeline) transforms reviewed Markdown sources into reproducible publication formats.

Implementations may extend, test or challenge the framework, but they should not silently redefine canonical meaning.

## Foundation and review status

Foundation v1.0 establishes a coherent semantic baseline for reference implementation and publication. It does not claim theoretical completeness or empirical validation.

The existing v0.2 review material remains part of the project history and review record. Independent review continues through the [review package](review/README.md), including the [invitation](review/INVITATION.md), [review guide](review/REVIEW_GUIDE.md), [known limitations](review/KNOWN_LIMITATIONS.md) and [known open questions](review/KNOWN_OPEN_QUESTIONS.md).

Participation should not be interpreted as endorsement of Mission Framework, its contributors or its conclusions.

## Why Mission Framework?

People, organisations and societies continuously face the same fundamental challenge:

> **How do we create beneficial change in reality in response to a justified need, opportunity, obligation or condition?**

Technology changes. Organisations change. Methods change.

The underlying challenge remains.

Mission Framework therefore begins with purpose, grounds decisions in observable reality, justifies reliance through evidence and uses architecture to enable governed missions.

## Canonical semantics

The [`GLOSSARY.md`](GLOSSARY.md) is the canonical source for Mission Framework terminology and the Mission Loop.

Normative semantic definitions belong in `mission-framework`. Reference implementations exercise those definitions through scenarios, evidence and acceptance cases. Publication artefacts communicate them but do not become canonical merely by being published.

The procedural rule for admitting concepts to Mission Core is defined in [`docs/MISSION_CORE_ADMISSION.md`](docs/MISSION_CORE_ADMISSION.md).

## Framework Findings

Observations from reference missions, reviews and implementations may reveal ambiguity, contradiction, incompleteness or unnecessary complexity in the semantic core. Such observations are returned through the [`Framework Findings process`](docs/FRAMEWORK_FINDINGS.md).

The process distinguishes direct observation from interpretation, requires traceable evidence and provides explicit dispositions such as clarify, revise, extend, reject, defer or return to implementation scope.

```text
Reference observation
        ↓
Framework Finding
        ↓
Semantic and evidence review
        ↓
Canonical disposition
        ↓
Propagation to implementations and publications
```

A local implementation issue does not automatically become a framework change, and a framework ambiguity should not be concealed through an undocumented local interpretation.

## Purpose before Architecture

Mission Framework was not created to define architecture, governance or technology for their own sake.

It exists to help people create beneficial, accessible change in reality—responsibly, transparently and sustainably.

## Trust by Design

Trust is a purpose-relative judgement that reliance is justified under stated conditions and consequences.

Every material component, workflow, AI interaction and architectural decision should therefore be evaluated across the relevant trust dimensions, stakeholders and mission policy:

> **Does this design create sufficiently justified reliance for its stated purpose and consequence?**

Trust is not assumed. It is supported through evidence, competence, transparency, consistency, challenge and accountable authority.

Verification history and fitness-for-purpose are separate judgements. Something may be well verified yet unfit for a particular decision, or relied upon provisionally under explicit uncertainty and time pressure.

## Reality before Models

Reality is the final authority, but missions encounter reality only through fallible observation and evidence.

Operationally, this means that when credible evidence contradicts a model, the model must change or the contradiction must be explicitly recorded and held open. Evidence must not be dismissed merely to protect an existing conclusion.

Models, architectures, claims and decisions must remain traceable to observations, evidence, provenance, time and uncertainty.

## Knowledge before Intelligence

Data alone has limited value. Observations become evidence when placed in context with provenance and integrity. Evidence supports or challenges claims. Knowledge emerges when evidence, claims, context, time and uncertainty survive an appropriate challenge process.

AI may accelerate discovery, analysis, reasoning and documentation. AI output is evidence or a proposal, not authority by declaration.

Humans and accountable organisational roles remain responsible for consequential decisions. Mechanisms may act under explicit, bounded and revocable delegated authority.

## Foundational Documents

The current conceptual foundation is documented in:

- [Canonical Glossary and Mission Loop](GLOSSARY.md) — normative definitions and the common semantic model
- [Mission Core Admission](docs/MISSION_CORE_ADMISSION.md) — the evidence-based procedure for changing Mission Core
- [Framework Findings Process](docs/FRAMEWORK_FINDINGS.md) — controlled feedback from implementation and review to canonical semantics
- [Purpose, Values and Philosophy](docs/PURPOSE_VALUES_PHILOSOPHY.md) — why Mission Framework exists and the values that guide it
- [Principia Missionis](docs/PRINCIPIA_MISSIONIS.md) — foundational principles
- [Mission Theory](docs/MISSION_THEORY.md) — missions, dependency descent and the operational layer
- [Reality Model](docs/REALITY_MODEL.md) — the reality gap, observability and evidence revision
- [Evidence Model](docs/EVIDENCE_MODEL.md) — evidence, provenance, contradiction and reviewability
- [Computational Trust Engineering](docs/COMPUTATIONAL_TRUST_ENGINEERING.md) — a proposed discipline for justified operational trust
- [Architecture](docs/ARCHITECTURE.md) — architectural layers and the Mission Kernel
- [External Review Synthesis](reviews/REVIEW-SYNTHESIS.md) — consolidated findings and dispositions from independent reviews

## The Canonical Mission Loop

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

Other diagrams in the body of knowledge may show architectural, operational, evidence or intelligence views of this loop. They must state what they expand, omit or aggregate and must not redefine the underlying concepts.

## Design Goals

- Begin with a justified need, opportunity, obligation or condition
- Define accountable purpose and assessable objectives
- Create beneficial and accessible value
- Respect the reality gap
- Earn justified reliance through evidence and challenge
- Preserve provenance, contradiction and explainability
- Maintain identifiable accountability and explicit delegation
- Share knowledge responsibly
- Reduce unnecessary complexity
- Remain independent of specific AI and cloud providers
- Design for longevity, reuse and continuous improvement

## Reference missions

[Mission Solar Eclipse](https://github.com/froekjaer/mission-solar-eclipse) is the first reference implementation. Additional candidate missions include:

- Mission Maritime
- Mission Timelapse
- Mission Governance
- Mission OSINT

Each mission shares the canonical foundation while remaining independently governed and operated. Findings with semantic consequences are returned to Mission Framework through the Framework Findings process.

## What Mission Framework Is

Mission Framework is not limited to Enterprise Architecture, Information Security or Artificial Intelligence. Each is an important application area.

Mission Framework seeks to describe something more fundamental:

> **How governed missions create justified, evidence-grounded change in reality.**

## Current direction

The next technical and empirical step is a deliberately small, versioned and testable vertical slice using Mission Solar Eclipse. Broad ontology and platform services will not be frozen before that reference case has challenged the model.

## Philosophy

We begin with purpose.

We respect reality.

We preserve evidence and uncertainty.

We exercise accountable authority.

We learn from outcomes.

We leave things better.