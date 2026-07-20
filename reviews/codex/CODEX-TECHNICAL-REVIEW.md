# Codex Technical Review

## Reviewer

- System/version: Codex / GPT-5
- Review date: 2026-07-21
- Repositories and revisions reviewed:
  - `froekjaer/mission-framework` — `9b78a233fcdf041547e94c171289b964deb624ee`
  - `froekjaer/Mission-Platform` — `48e1cfc5a6d71e043f503f776239d849664502c3`
  - `froekjaer/mission-solar-eclipse` — `dd531374084d6ffc75c361c51c062a646e912bf0`
- Important limitations: Review of documentation and repository structure only. No schemas, APIs, executable reference implementation, or Solar Eclipse scenario data currently exist to validate.

## Executive assessment

The strongest architectural quality is the disciplined semantic chain from reality through observation and evidence to decisions and learning. The most serious weakness is that the terms that must carry this chain in software are not yet sufficiently formalised, and canonical semantic ownership is ambiguous between Framework and Platform. The most important next action is to define and test a deliberately small Mission Core vertical slice, using Solar Eclipse as its first reference case, before freezing broad schemas or platform services.

## Observations

### Repository responsibilities

**Question 1: Are the repositories separated according to clear architectural responsibilities?**

Mostly, yes:

- `mission-framework` should own principles, canonical semantics, and normative invariants.
- `Mission-Platform` should own formal schemas, API contracts, validators, tools, and reference implementations.
- `mission-solar-eclipse` should own the domain vocabulary, scenario data, evidence, and acceptance cases for one real mission.

There is an important inconsistency to resolve. `Mission-Platform/docs/adr/ADR-0001-mission-platform-vision.md` says Mission Framework defines the reference and meta models, while those documents currently reside in Mission Platform. One repository must be declared the canonical semantic source; Platform should implement or formalise that source rather than silently redefine it.

### Mission Core semantics

**Question 2: Which concepts require precise identifiers, lifecycle states or invariants?**

The minimum cross-domain concepts needing stable identifiers are Mission, Objective, Capability, Actor, Observation, Evidence, Claim, Decision, Policy Evaluation, and Relationship. A `Claim` is indispensable: the Framework distinguishes evidence from claims and conclusions, but the Platform reference model currently omits it.

The following should have explicit state/lifecycle rules:

- Observation: recorded, rejected, preserved.
- Evidence: acquired, integrity-checked, contextualised, challenged, retained/archived/disposed.
- Claim: proposed, supported, contested, superseded, withdrawn.
- Decision: proposed, authorised, executed, revoked/superseded.
- Policy exception: requested, approved, expired, revoked.

Original observations and evidence should be immutable or append-only. Corrections and later interpretations must be new records with new provenance, not edits that change history.

**Question 3: Which relationships should be mandatory, optional, directional or temporal?**

- A material Claim must have either supporting/challenging Evidence or an explicit recorded assumption; `supports` and `challenges` are directional.
- A Decision must identify an accountable authority, decision time, and its basis; use of particular evidence may be optional but must be explicit when material.
- Evidence must have source/provenance and acquisition/observation context when known; unknown fields must remain unknown rather than be fabricated.
- Mission-to-Objective and Objective-to-Capability links are directional contribution/requirement relationships, but reverse traversal should be supported.
- Every material relationship needs its own identifier, provenance, status, and validity interval. Relationship validity is not necessarily the same as record creation time.
- A Reality Anchor should be a verifiable relationship from a model element to observable reality, not merely a descriptive label.

### Platform architecture

**Question 4: Where could a premature schema freeze the ontology too early?**

The main risk points are:

- turning all relations into generic `source`, `target`, `type` edges without relation-specific semantics;
- treating State as a universal entity rather than a state transition under an explicit lifecycle;
- flattening multiple trust dimensions into one score;
- modelling absence of detection as proof of absence;
- making Reality Anchor a mandatory object type before deciding whether it is better represented as an evidence-backed relation;
- encoding present organisational roles as permanent universal categories.

The Mission Core admission rule is sound under implementation pressure: a concept belongs in Core only if it is needed across domains and cannot be represented faithfully as an extension. Claim passes this test. Eclipse-specific conditions, observation geometry, cloud taxonomy, and forecasting models do not.

**Question 5: What minimum machine-readable representation would preserve the semantics?**

The minimum is not a universal schema; it is a small typed record model containing stable IDs, typed relationships, bitemporal fields, provenance, and immutable revisions. An illustrative experiment appears below.

### Solar Eclipse reference mission

**Question 8: Can the Solar Eclipse mission serve as a useful executable or testable reference case?**

Yes, but not in its present form. It is currently a repository with only a one-line README. It can become an excellent first reference case because it requires time, location, weather/sensor observations, uncertainty, evidence freshness, decisions, public guidance, and outcome evaluation. It should begin with one narrow scenario, for example: determine whether to publish viewing guidance for a specified observation site and time window.

## Implementation risks

| Affected repository or file | Risk and consequence | Likelihood / uncertainty | Recommended mitigation |
|---|---|---|---|
| Framework and Platform model ownership | Competing canonical definitions cause semantic drift. | High unless resolved before schemas are added. | Name one canonical semantic source and define a versioned change process. |
| `Mission-Platform/docs/architecture/mission-reference-model.md` | Missing Claim collapses evidence, interpretation, and conclusion. | High. | Add Claim as a core concept and formalise its provenance and lifecycle. |
| Future schemas/APIs | A generic graph schema loses cardinality, direction, and temporal meaning. | High. | Define typed relationship contracts and invariants before implementation. |
| Future persistence design | Mutable evidence corrupts auditability and reproducibility. | Medium to high. | Preserve originals and use append-only revisions/derivatives. |
| `mission-solar-eclipse` | No executable scenario can challenge the model. | Certain at current revision. | Add scenario, sample evidence, acceptance criteria, and replay tests. |

## Semantic risks introduced by implementation

- A storage-oriented model may confuse database records with reality, observations with events, or evidence with truth.
- A universal confidence number may hide freshness, independence, integrity, detection capability, and contradiction.
- AI outputs may be given authority if their model, version, inputs, prompt/task, configuration, and human review state are not recorded.
- “Owner” may become a substitute for accountable decision authority unless those roles are separated.
- A relation without its own provenance and temporal validity may silently misrepresent a historical or changing reality.

## Proposed architecture and conformance tests

**Question 6: Which architecture tests should fail when a model becomes detached from evidence or reality?**

| Test | Purpose | Expected result | Repository |
|---|---|---|---|
| Claim provenance test | Prevent unsupported material claims. | Fail if a material Claim has neither evidence nor a documented assumption. | Mission-Platform |
| Evidence immutability test | Preserve historical basis. | Fail when original evidence is modified rather than superseded by a new derivative/review. | Mission-Platform |
| Contradiction preservation test | Prevent artificial consensus. | Fail if contradictory evidence is discarded or overwritten without a documented resolution. | Mission-Platform |
| Reality-anchor freshness test | Detect stale decision grounds. | Fail or require escalation when required evidence has exceeded mission-defined freshness limits. | Mission-Platform |
| Temporal traceability test | Separate history from validity. | Fail if a material fact has no applicable event/observation and record/validity time semantics. | Mission-Platform |
| Authority transition test | Prevent unauthorised consequential actions. | Fail if a decision or exception transition lacks authorised accountable approval. | Mission-Platform |
| Extension isolation test | Preserve Core semantics. | Fail if a domain extension changes the meaning or invariants of a Core concept. | Mission-Platform |
| Eclipse replay test | Demonstrate executable reference value. | Same evidence, policy, and configuration reproduce the same decision basis. | mission-solar-eclipse |

## Minimal machine-readable experiment

Experimental syntax only; this is not a canonical schema:

```json
{
  "id": "claim:eclipse-visible-2026-08-12",
  "kind": "Claim",
  "statement": "The observation site is suitable for eclipse viewing.",
  "validDuring": {
    "from": "2026-08-12T16:00:00Z",
    "to": "2026-08-12T18:00:00Z"
  },
  "supportedBy": ["evidence:weather-forecast-01"],
  "challengedBy": ["evidence:cloud-observation-02"],
  "usedBy": ["decision:publish-viewing-guidance-01"],
  "status": "contested"
}
```

## Security, provenance and audit findings

**Question 7: What security, provenance and audit requirements are implicit but undocumented?**

- Cryptographic integrity verification and safe preservation of original artefacts.
- Append-only audit trails for changes, reviews, policy evaluations, and decisions.
- Authenticated identities for both people and technical actors; identity strength proportional to consequence.
- Least privilege and separation between evidence custodian, reviewer, policy authority, and decision authority.
- Access classification, retention, legal basis, redaction, and disposal controls for sensitive or personal data.
- Versioned provenance for sensors, software, policies, AI models, prompts/tasks, configurations, and tools.
- Exportable, independently verifiable decision packages that do not require trusting the platform itself.

## Recommendations

### Required before implementation

1. Resolve canonical ownership of semantics and establish semantic versioning/change governance.
2. Define Core invariants for Observation, Evidence, Claim, Decision, Authority, and typed Relationships.
3. Decide the temporal model: at minimum distinguish event/observation time, recording time, and validity time.
4. Specify immutable evidence, audit, and correction rules.
5. Define an explicit domain-extension mechanism.

### Valuable during Sprint 1

1. Build one narrow evidence-to-claim-to-decision vertical slice.
2. Automate the conformance tests above.
3. Add a Solar Eclipse scenario with sample evidence, policy, expected outcome, and reproducible replay.
4. Publish an initial schema with a clear experimental version label.

### Suitable for a later release

1. Mission DSL, compiler, graph visualisation, and broad policy engine.
2. Advanced trust analysis and aggregate operational dashboards.
3. Further domain reference models and AI-assisted reasoning tools.

## Unresolved questions

1. Is Claim a universal Core concept, or a subtype of Knowledge with explicit evidence relations?
2. What makes a Reality Anchor independently verifiable rather than merely documented?
3. Which relationship types are normative Core vocabulary, and which are extensions?
4. What are the exact differences between ownership, custody, responsibility, authority, and accountability?
5. How should a new policy/schema version affect interpretation of historical records without rewriting history?
6. What level of evidence freshness and authority is proportional to each decision consequence?

## Overall conclusion

The project is **ready with conditions** for its next technical step: a small, versioned, testable Mission Core experiment. It is not yet ready to freeze a broad ontology or build a general platform. Solar Eclipse should become the first executable reference case used to challenge the Core, rather than a demonstration built after the Core has already been fixed.
