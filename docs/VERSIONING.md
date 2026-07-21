# Versioning and Release Interpretation

**Status:** Foundation Release v1.0

## Purpose

Mission Framework participates in a coordinated programme release while also maintaining its own semantic maturity and review history. These are different version dimensions and must not be conflated.

## Programme foundation version

`Foundation Release v1.0` identifies the first coordinated baseline across:

- Collaborative Intelligence
- Mission Framework
- Mission Solar Eclipse
- Publication Pipeline

It means that repository responsibilities, cross-references and the feedback loop between semantics, implementation and publication have been established.

It does **not** assert that:

- the semantic theory is complete
- the framework has been empirically validated
- Mission Solar Eclipse is operationally complete
- schemas or software APIs are stable at version 1.0
- the publication toolchain is implemented end to end

## Framework semantic version

Mission Framework semantic versions describe the maturity of the canonical vocabulary, models and normative rules.

Earlier `v0.2 Review Candidate` material remains part of the review history. Foundation v1.0 incorporates a reviewed baseline from that work but does not erase the earlier review designation or imply that all open questions have been resolved.

Until a separate semantic release is explicitly declared, readers should interpret the current state as:

```text
Programme architecture: Foundation v1.0
Framework semantics: reviewed baseline under continuing validation
Reference implementation: initial vertical slice pending
Publication tooling: architecture defined, implementation pending
```

## Compatibility

A normative semantic change must state:

- affected canonical terms or relationships
- reason and supporting evidence
- disposition of the relevant Framework Finding
- compatibility effect on reference missions, schemas and publications
- migration or reinterpretation guidance where required

Editorial clarification without changed normative meaning should be identified as such.

## Release rule

A future release label must identify its scope. Ambiguous labels such as `v1.1` without a named scope should be avoided.

Recommended forms include:

- `Programme Foundation v1.1`
- `Mission Framework Semantics v0.3`
- `Mission Solar Eclipse Mission Baseline v0.1`
- `Publication Pipeline Tooling v0.1`

## Reality rule

Release status never overrides evidence. **Reality wins:** when credible evidence from a reference mission contradicts a released model, the contradiction must be preserved and reviewed through the Framework Findings process rather than hidden to protect the release label.
