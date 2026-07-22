# Publication Pipeline

## Status

Draft normative specification for review.

## Purpose

Mission Framework shall maintain a single canonical knowledge base while supporting multiple publication forms for different audiences and operational purposes.

The Publication Pipeline preserves provenance, review status, evidence maturity and semantic integrity when reviewed source material is transformed into books, articles, briefs, presentations, websites and stable distribution formats.

A publication is a traceable transformation of canonical knowledge.

## Canonical source principle

Markdown source files in the governed repository set are canonical unless a document explicitly declares another canonical source.

Generated artefacts are derived outputs. They shall not become independent editing sources.

Semantic corrections shall return to the canonical source and trigger regeneration of affected publications.

## Permitted transformation

A publication profile may change structure, ordering, level of detail, layout, visual presentation, audience framing, navigation and selection of reviewed material.

A publication shall not silently change meaning, evidence, normative force, review status, provenance, declared uncertainty or evidence maturity.

Any new claim, interpretation, diagram or synthesis introduced during publication shall be identified and reviewed as publication-specific content.

## Publication metadata

Every generated publication shall expose, directly or through an accompanying manifest:

- publication type, title and version;
- publication date, audience and profile;
- source repository or repository set;
- source commit or immutable revision identifiers;
- canonical source files;
- generator name, version and profile revision;
- review status and evidence maturity information;
- licence;
- content hash or release checksum.

## Publication types

### Book

A book assembles a sustained argument or body of knowledge from multiple reviewed source files. It may include front matter, chapters, appendices, references, figures, glossary and indexes.

A book shall declare its source revision and distinguish canonical source content from publication-specific connective text, synthesis or illustration.

### Article

An article selects and reframes a bounded proposition for a defined audience and publication context.

The article shall identify its source revision and distinguish synthesis from new claims. Publication-specific claims require their own evidence and review status.

### Executive Brief

An Executive Brief provides rapid orientation for decision-makers and other readers who cannot initially engage with the complete source set.

It shall remain linked to canonical sources, state material limitations and avoid presenting compressed conclusions with greater confidence than their supporting evidence.

### Review Package

A Review Package assembles the minimum sufficient material for a defined independent review or assurance activity.

It may contain a project extract, repository map, source register, evidence summary, review questions, known limitations and relevant publications. Omission of unrelated material shall be explicit rather than misleading.

### PDF

PDF is a stable distribution and archival format generated from an approved source set.

Page layout is a presentation concern. Semantic corrections shall return to the Markdown source rather than being made only in the generated PDF.

### GitHub Pages

GitHub Pages provides navigable web publication directly related to repository content.

Web navigation, summaries and landing pages may be generated or curated, but shall preserve links to canonical sources and clearly identify generated or interpretive material.

### Presentation

Presentations are audience-specific interpretations of reviewed source material. They necessarily compress and sequence content.

Material omissions, simplifications, newly created diagrams and presenter interpretations shall therefore be reviewable and traceable.

Slides shall not become normative documentation solely because they are easier to consume.

### EPUB and DOCX

EPUB may provide a long-form reading edition. DOCX may support organisational workflows requiring office-document formats.

Both remain convenience outputs unless explicitly governed otherwise. Neither replaces the canonical source.

## Publication profiles

The generator shall use explicit publication profiles. Initial profiles are:

- `book`;
- `article`;
- `executive-brief`;
- `review-package`;
- `presentation`;
- `github-pages`;
- `pdf`;
- `epub`;
- `docx`.

A profile should declare its audience and purpose, included and excluded source sets, ordering rules, permitted synthesis, rendering rules, branding and accessibility requirements, required metadata, validation gates and outputs.

## Validation and release gates

Publication shall stop when required validation fails.

The pipeline should validate at least source existence, declared inclusion, links, cross-references, profile syntax, provenance metadata, review-state requirements, unresolved placeholders, reproducibility where technically practical, checksums and release manifests.

A successful build demonstrates that the configured transformation completed. It does not by itself prove the truth, fitness or independent validation of the published claims.

## Traceability and reproducibility

Given the repository set, immutable source revisions, publication profile and generator version, another party should be able to reproduce materially equivalent output.

Byte-for-byte reproducibility is preferred for archival outputs but may require controlled fonts, timestamps, rendering engines and build environments. Where exact reproduction is not yet achieved, the limitation shall be documented.

## Relationship to trust operations

The Publication Pipeline supports:

- **Trust Bootstrap**, by exposing provenance, limitations and reproducible source relationships;
- **Credibility Onboarding**, by providing appropriate entry points for different audiences;
- **Evidence Maturity**, by preserving the maturity and review status of claims through transformation;
- **Independent Assurance**, by producing bounded, source-linked review packages.

Publication does not create credibility merely through visual polish. It makes the basis, limits and transformation of claims inspectable.

## Governance rule

Publication is a governed operation, not a cosmetic afterthought.

No generated artefact may silently acquire canonical or normative authority. Any proposed semantic change discovered during publication shall be returned to the canonical source governance process.
