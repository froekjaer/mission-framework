# Framework Findings Process

**Status:** Foundation v1.0  
**Scope:** Mission Framework and its reference implementations

## Purpose

The Framework Findings process provides a controlled path for observations from reference missions, reviews, experiments and implementations to challenge the semantic core of Mission Framework.

A finding is not automatically a defect and does not automatically change the framework. It is a traceable claim that an observed condition may reveal ambiguity, incompleteness, contradiction, unnecessary complexity or a useful extension in the canonical semantics.

The process protects two requirements at the same time:

1. reference implementations must be able to challenge the framework with evidence; and
2. local implementation choices must not silently redefine canonical meaning.

## Sources of findings

Framework Findings may originate from:

- reference missions, beginning with Mission Solar Eclipse
- academic, practitioner, engineering or AI-assisted review
- attempted implementation of a canonical concept
- comparison with established research, standards or professional methods
- contradictory evidence or observed failure
- publication review that reveals semantic inconsistency

## Minimum finding record

Each finding should contain:

| Field | Requirement |
|---|---|
| Identifier | Stable identifier, for example `FF-0001`. Findings hosted outside `mission-framework` should use a repository-indicating prefix (for example `FF-PUB-001`) to avoid collision with another repository's local numbering. |
| Title | Concise statement of the issue |
| Source | Repository, mission, review or experiment where it arose |
| Context | Conditions under which the observation was made |
| Canonical reference | Relevant glossary term, principle, model or document |
| Observation | What was directly observed |
| Interpretation | Why the observation may matter to the framework |
| Evidence | Traceable material supporting or challenging the finding |
| Consequence | What could fail or become misleading if unresolved |
| Proposed disposition | Clarify, revise, extend, reject, defer or request more evidence |
| Confidence | Confidence in the observation and interpretation |
| Status | Proposed, under review, accepted, rejected, deferred or superseded |
| Owner | The individual or role accountable for the finding's disposition and any resulting propagation until it is closed, reassigned or superseded |
| Affected repositories/artefacts | Authoritative and derived repositories, implementations or publications known or suspected to be affected, where known |
| Propagation targets | Where the disposition requires action outside the repository the finding was raised in, the specific downstream repositories, artefacts or publications that must still be assessed or updated, where known |
| Verification/closure evidence | Reference to the evidence that propagation was completed and independently verified; recorded when the finding is closed |

Observations and interpretations must be distinguishable. AI-generated analysis must retain provenance and must not be represented as independent empirical evidence.

A finding's presence in this process, or in the index below, records that it *exists* and has been raised through the process. It does not by itself mean the finding has been *accepted*: acceptance is recorded only through the Status field, set through the review below, by an accountable human (see "Authority and accountability").

## Lifecycle

```text
Observation
    ↓
Finding proposed
    ↓
Semantic and evidence review
    ↓
Disposition
    ├── Clarify existing meaning
    ├── Revise canonical meaning
    ├── Extend the framework
    ├── Reject with rationale
    ├── Defer pending evidence
    └── Return to implementation scope
    ↓
Canonical change, recorded decision or closure
    ↓
Propagation to affected repositories and publications
```

## Review criteria

A finding should be evaluated against the following questions:

1. Is the observation traceable to a real review, implementation or mission condition?
2. Does the issue concern canonical meaning rather than a local design choice?
3. Is the existing definition genuinely ambiguous, incomplete or contradicted?
4. Would the proposed change improve explanatory or operational value?
5. Could the change introduce semantic distortion elsewhere?
6. Is there sufficient evidence for a normative change?
7. Which documents, examples, schemas or publications would be affected?

## Dispositions

### Clarify

The canonical meaning remains unchanged, but explanatory text or examples are improved.

### Revise

Existing normative meaning changes. The revision must identify compatibility consequences and update the canonical glossary or relevant normative document.

### Extend

A new concept or relationship is admitted through the Mission Core admission process. Extension requires evidence that the concept is foundational rather than merely domain-specific.

### Reject

The finding is closed because the evidence does not support a framework change, the issue is implementation-specific, or the proposal conflicts with stronger principles. The rationale remains visible.

### Defer

The finding remains open because available evidence is insufficient or the relevant reference mission has not yet tested the proposition adequately.

### Return to implementation scope

The issue is valid but belongs in a reference mission, platform, publication or domain extension rather than in canonical semantics.

## Authority and accountability

Mission Framework remains the canonical location for normative semantics. Reference repositories may propose findings and may document temporary local interpretations, but they must link those interpretations to an unresolved finding when canonical ambiguity is involved.

Consequential semantic changes require identifiable human approval. AI systems may discover inconsistencies, compare evidence and propose dispositions, but may not approve normative changes by declaration.

## Relationship to Mission Core admission

A finding that proposes a new foundational concept or a material change to Mission Core must also satisfy [`MISSION_CORE_ADMISSION.md`](MISSION_CORE_ADMISSION.md). The Findings process identifies and evaluates the issue; the admission process governs whether a concept belongs in the stable semantic core.

## Repository practice

Until a dedicated cross-repository registry is established, accepted or actively reviewed findings should be documented in `mission-framework` with links to their source material. Reference missions should preserve their original observations and link to the corresponding framework disposition.

This creates a bidirectional audit trail:

```text
Reference observation ⇄ Framework Finding ⇄ Canonical disposition
```

## Known findings (index)

This index makes findings discoverable centrally, as required above, without moving or restating their content. Listing a finding here records that it exists and is known to Mission Framework; it does **not** by itself change its Status. A finding fully hosted in this repository (Source column links to a file under `docs/findings/`) is the authoritative record for that finding. A finding whose Source column links to another repository remains authoritative there; this table only reproduces its identifier, origin and last-known Status as reported by that repository, and may lag it — the linked source is the source of truth for current status.

| Identifier | Source | Status (last known) | Disposition |
|---|---|---|---|
| [`FF-TLP-0001`](findings/FF-TLP-0001-cross-repository-governance-propagation.md) | `timelapse-pro`, hosted in `mission-framework` | Accepted | Extend (OP-001 Step 7; Framework Findings schema) |
| `FF-PUB-001` | [`-Publication-Pipeline/docs/framework-findings.md`](https://github.com/froekjaer/-Publication-Pipeline/blob/main/docs/framework-findings.md) | Proposed / Open (per source repository) | Not yet dispositioned by Mission Framework |
| `FF-PUB-002` | [`-Publication-Pipeline/docs/framework-findings.md`](https://github.com/froekjaer/-Publication-Pipeline/blob/main/docs/framework-findings.md) | Proposed / Open (per source repository) | Not yet dispositioned by Mission Framework |
| `FF-PUB-003` | [`-Publication-Pipeline/docs/framework-findings.md`](https://github.com/froekjaer/-Publication-Pipeline/blob/main/docs/framework-findings.md) | Proposed / Open (per source repository) | Not yet dispositioned by Mission Framework |
| `FF-PUB-004` | [`-Publication-Pipeline/docs/framework-findings.md`](https://github.com/froekjaer/-Publication-Pipeline/blob/main/docs/framework-findings.md) | Proposed / Open (per source repository) | Not yet dispositioned by Mission Framework |
| `FF-0001` | [`mission-solar-eclipse/docs/findings/FF-0001-sub-agent-delegation.md`](https://github.com/froekjaer/mission-solar-eclipse/blob/main/docs/findings/FF-0001-sub-agent-delegation.md) | Proposed → Deferred (per source repository, self-assessed; "requires external review") | Deferred pending additional mission evidence |
| `FF-0002` | [`mission-solar-eclipse/docs/findings/FF-0002-mission-loop-entry-points.md`](https://github.com/froekjaer/mission-solar-eclipse/blob/main/docs/findings/FF-0002-mission-loop-entry-points.md) | Proposed (per source repository; "Requires: Mission Framework maintainer review") | Not yet dispositioned by Mission Framework |

Entries added 2026-09-15 as part of resolving an observed practice discrepancy: several findings existed in reference/peripheral repositories without being discoverable from `mission-framework` itself, contrary to the repository-practice rule above. This index closes that discoverability gap without altering any finding's substantive content, provenance or status. `FF-PUB-001..004` and `FF-0001`/`FF-0002` remain open items requiring their own substantive review before any disposition beyond what their source repository already records.

## Foundation interpretation

Foundation v1.0 establishes this process as the formal feedback mechanism between Mission Framework and Mission Solar Eclipse. The process is intentionally lightweight at this stage and should be improved from practical use rather than expanded speculatively.