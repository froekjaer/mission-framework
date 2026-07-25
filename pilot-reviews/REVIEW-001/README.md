# REVIEW-001 — Mission Platform Transformation Lab

REVIEW-001 is the first controlled, independent architecture-and-build exercise under Mission Framework.

## Purpose

Use the existing `froekjaer/timelapse-pro` repository as a strictly read-only source of documentation, code, decisions, tests, operating evidence and migration knowledge.

Each reviewer must then design and build an independent modular successor in their assigned branch of `froekjaer/Mission-Platform`.

In operational terms:

> Read and evaluate `froekjaer/timelapse-pro`; build the new modular solution in `froekjaer/Mission-Platform`.

## Canonical invitation

- [REVIEW-001 Invitation](INVITATION.md)

The invitation is binding for all reviewers and defines:

- the frozen TimeLapse Pro baseline;
- the read-only boundary around `froekjaer/timelapse-pro`;
- the destination repository and isolated reviewer branches;
- the business-first architecture process;
- required outputs;
- independence rules;
- submission and meta-review requirements.

## Repositories

### Source — read only

- Repository: `froekjaer/timelapse-pro`
- Frozen baseline: `eed9e3c8c67369e1924c25a11908616220c3c753`
- Purpose: evaluation, evidence and migration input only

No reviewer may commit, push, branch, change configuration, modify issues or pull requests, or otherwise write to this repository as part of REVIEW-001.

### Destination — all new work

- Repository: `froekjaer/Mission-Platform`
- Purpose: architecture, ADRs, schemas, documentation, implementation, tests, tooling, migration and proof-of-concepts

## Reviewer branches

- `review/review-001-chatgpt`
- `review/review-001-claude`
- `review/review-001-gemini`
- `review/review-001-codex`
- `review/review-001-zai`
- `review/review-001-human`

Each reviewer works independently and must not inspect or reuse another reviewer’s work before submission.

## Target outcome

The result is not a direct modification of TimeLapse Pro.

The result is a new modular Mission Platform in which timelapse becomes the first functional payload rather than the architectural boundary of the system.

## Authority

Peter Frøkjær is Mission Owner and retains final authority over whether a proposal serves the mission.