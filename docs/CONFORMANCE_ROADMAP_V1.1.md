# Conformance Roadmap — Foundation v1.1

**Status:** Release roadmap  
**Scope:** Minimum reproducible controls, not a complete platform specification

## Objective

Create the smallest useful set of repeatable checks that can detect drift, missing release artefacts and broken traceability across the Mission Framework ecosystem.

Conformance checks support governance. They do not replace accountable review.

## Phase 1 — Document integrity

Required for Foundation v1.1 release:

- verify required normative documents exist
- verify Markdown links within Mission Framework
- verify every release-controlled document declares status or version where required
- verify canonical terminology points to `GLOSSARY.md`
- verify no generated publication is presented as canonical source

## Phase 2 — Cross-repository baseline

Required before the first validation result is accepted:

- machine-readable or consistently parseable baseline manifest
- exact commit identifiers for all participating repositories
- named ownership of canonical semantics, implementation and publication concerns
- checks for unresolved repository references and renamed paths

## Phase 3 — Reference-mission conformance

Required for Mission Solar Eclipse vertical-slice completion:

- mission purpose, objectives and accountable owner are present
- tested propositions and falsification conditions are recorded
- evidence locations and provenance are declared
- Framework Findings use the canonical process
- local terms do not silently redefine Mission Core
- validation disposition is present

## Phase 4 — Publication traceability

Required for public Foundation v1.1 publications:

- generated artefact identifies source commit
- transformation identifies Publication Pipeline version
- generated files are distinguishable from reviewed Markdown sources
- publication failure or warning does not silently produce an apparently authoritative artefact

## Phase 5 — Independent reconstruction

Target during stabilisation:

- provide a clean-room reconstruction checklist
- measure missing assumptions and inaccessible dependencies
- verify that private chat context is not required for critical reasoning
- record original-author interventions needed to complete reconstruction

## Initial implementation approach

The first checks should remain simple and inspectable:

1. repository scripts or GitHub Actions
2. Markdown link checking
3. manifest validation
4. required-file validation
5. lightweight schema validation where structured records exist

A large ontology service or platform dependency is not required for Foundation v1.1.

## Failure policy

Conformance failures shall be classified as:

- **Blocker** — release or validation result is not trustworthy without correction
- **Warning** — material weakness requiring disposition
- **Advisory** — improvement opportunity without current release impact

Checks shall state what they prove and what they do not prove.

## Ownership

Mission Framework owns semantic conformance rules.

Reference missions own implementation evidence.

Publication Pipeline owns transformation traceability.

Collaborative Intelligence owns programme-level baseline and review archive visibility.

## Completion criterion

The roadmap succeeds when the ecosystem can detect basic drift and missing traceability automatically or through a documented repeatable procedure, without requiring a future full Mission Platform implementation.