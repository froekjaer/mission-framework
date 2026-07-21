# Mission Core Admission

Mission Core is the smallest stable set of concepts required to model missions coherently across domains.

## Working principle

A concept belongs in Mission Core only when it is demonstrably required across domains and cannot be represented through extensions without unacceptable distortion, duplication or loss of interoperability.

This principle is procedural rather than intuitive. No concept enters Core merely because it appears important.

## Admission criteria

A candidate concept may enter Mission Core only when all of the following are satisfied:

1. **Cross-domain evidence** — at least three materially different domain models require the concept or an equivalent semantic construct.
2. **Extension attempt** — the concept has been modelled as a domain extension or composition of existing Core concepts.
3. **Documented inadequacy** — the extension approach creates recorded semantic distortion, repeated incompatibility, unsafe ambiguity or disproportionate implementation cost.
4. **Stable definition** — the candidate has a definition, purpose, boundaries, relationships, ownership, lifecycle and invariants.
5. **Conformance value** — placing the concept in Core enables meaningful cross-domain validation or interoperability.
6. **Explicit decision** — admission is approved through an Architecture Decision Record that cites the evidence and rejected alternatives.

## Provisional concepts

A concept may be marked **Experimental Core** while evidence is accumulated. Experimental concepts:

- must have a versioned definition;
- must not be treated as permanently stable;
- must be tested in at least one reference mission;
- must include an exit or revision path.

## Removal and change

Core concepts are not immutable. A concept may be revised, demoted to an extension or removed when evidence shows that it is not universal, is better represented through other concepts or creates more ambiguity than value.

Changes must preserve historical interpretation through versioning. Existing records must not be silently reinterpreted under a new definition.

## Current candidates for structured evaluation

The external review round identified the following candidates for formal evaluation:

- Claim
- Delegated Authority
- Constraint
- Uncertainty
- Commitment

Their appearance here is not admission. Each must pass the process above.