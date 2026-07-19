# Evidence Model

> **Evidence is the currency of trust.**

Evidence is information that supports, weakens or contradicts a claim. It is not identical to data, truth, knowledge or conclusion.

Mission Framework treats evidence as a first-class engineering object.

## Core principles

1. Preserve originals.
2. Record provenance before interpretation.
3. Make material evidence independently reviewable.
4. Preserve contradictions and negative evidence.
5. Separate confidence from truth.
6. Make transformations reproducible where practical.
7. Do not silently replace historical evidence with later conclusions.

## Observation and evidence

An **observation** is a recorded encounter with reality.

Evidence is an observation placed in a mission context with sufficient provenance, integrity and relevance to support or challenge a claim.

```text
Reality → Observation → Evidence → Claim → Knowledge → Decision
```

The arrows represent transformations. Each material transformation must be attributable and reviewable.

## Evidence classes

### Sensor evidence

Measurements or signals from physical or digital sensors, including associated calibration, configuration and environmental context.

### Visual and acoustic evidence

Images, video, audio and other media. Originals should be retained together with metadata and hashes.

### Documentary evidence

Documents, records, messages, logs, contracts, policies and external publications.

### Human evidence

Statements, observations, expert assessments and testimony. Human evidence must preserve identity, role, context, time and potential limitations.

### System evidence

Events, transactions, configuration states, audit records and outputs produced by operational systems.

### AI-generated evidence

Classifications, summaries, detections, correlations, hypotheses and generated explanations produced by AI.

AI output is evidence, never fact by declaration.

## Required metadata

A material evidence object should include, where applicable:

- evidence identifier
- mission identifier
- source identity
- observation time
- ingestion time
- location or context
- original format
- cryptographic hash
- integrity status
- acquisition method
- transformation history
- access classification
- retention requirements
- confidence indicators
- trust assessment
- related claims
- contradictions or challenges
- reviewer and review status

## Provenance

Provenance describes where evidence came from and what happened to it.

A useful provenance chain answers:

- Who or what observed it?
- When and where was it observed?
- How was it recorded?
- Has it been transformed?
- Which tools, models or people performed the transformation?
- Can the transformation be repeated?
- Has integrity been verified?

## Chain of evidence

Evidence frequently depends upon other evidence. A report may cite a measurement; a conclusion may depend upon several reports; an AI assessment may depend upon images and metadata.

Mission Framework models these relationships as a graph rather than flattening them into one confidence score.

A chain is weakened by:

- missing source material
- unknown transformations
- broken identity
- unverified time
- unverifiable model output
- circular citation
- stale evidence
- concealed contradiction

## Evidence quality

Evidence quality is multidimensional. Relevant dimensions include:

- authenticity
- integrity
- relevance
- precision
- completeness
- timeliness
- independence
- reproducibility
- representativeness
- interpretability

A single aggregate score may be useful operationally, but it must not conceal the dimensions from which it was derived.

## Negative evidence

The absence of an expected observation may itself be evidence, but only when the observation process was capable of detecting the expected condition.

Therefore:

> **Unknown does not mean false, and not observed does not automatically mean absent.**

Negative evidence must document detection capability, observation window and relevant limitations.

## Contradictory evidence

Contradictions are preserved, not averaged away.

The framework should support:

- competing observations
- source disagreement
- temporal change
- unresolved anomalies
- alternative explanations

A contradiction is a signal that the current model may be incomplete.

## AI provenance

Material AI evidence should include:

- model name and version
- provider or execution environment
- prompt, system instruction or task definition
- referenced inputs
- retrieval sources
- tools invoked
- generation parameters where relevant
- output timestamp
- validation method
- human reviewer

A later model must not overwrite an earlier output. It creates new evidence.

## Evidence lifecycle

```text
Acquire
  ↓
Preserve
  ↓
Validate
  ↓
Contextualise
  ↓
Relate to claims
  ↓
Review and challenge
  ↓
Use in decisions
  ↓
Retain, archive or dispose
```

Lifecycle actions must follow policy and remain auditable.

## Engineering rules

- Store metadata before conclusions.
- Keep originals separate from derivatives.
- Use stable identifiers.
- Hash material evidence where practical.
- Record time as a first-class property.
- Preserve uncertainty and contradiction.
- Distinguish source confidence from conclusion confidence.
- Never claim verification that did not occur.

## Closing statement

Trust does not appear at the end of analysis by declaration.

It accumulates one reviewable piece of evidence at a time.