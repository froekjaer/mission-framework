# Audience-Adaptive Knowledge Delivery

## Status

Draft normative specification for review.

## Purpose

Mission Framework shall deliver governed knowledge in forms that respect the capabilities, context and interaction model of the intended audience.

Knowledge is not successfully delivered merely because it is technically available. It is successfully delivered when the intended audience can locate it, access it, interpret it and act on it without avoidable cognitive, cultural or technical barriers.

The same canonical knowledge may therefore require different representations for humans, machines and collaborative human–AI teams.

## Core principle

> Knowledge shall be published in a form that respects the cognitive capabilities, cultural context, accessibility needs and interaction model of its intended audience, whether that audience is human, machine or a collaborative human–AI team.

Audience adaptation may change presentation, navigation, language, sequencing, density, format and interaction. It shall not silently change meaning, provenance, uncertainty, evidence maturity, review state or normative force.

## Audience classes

### Human audiences

Human audiences commonly require orientation, hierarchy, narrative, visual structure, examples, progressive disclosure and language appropriate to their culture, role and expertise.

Human-facing delivery should minimise unnecessary search, decoding and reconstruction. A technically complete but disordered export may be usable by a machine while remaining practically inaccessible to a person.

### Machine audiences

Machine audiences commonly require explicit structure, stable identifiers, metadata, consistent terminology, typed relationships, deterministic access paths and formats suitable for parsing and validation.

Machine-readable delivery should avoid relying exclusively on visual layout, undocumented conventions or implicit human interpretation.

### Collaborative human–AI audiences

In collaborative use, the machine may inspect a large or irregular source set while the human consumes an explanation, recommendation, visualisation or decision interface.

The system shall preserve the relationship between machine interpretation and canonical evidence so the human can inspect material assumptions, limitations and sources.

## Audience profiles

Each significant publication or interface should declare one or more audience profiles. A profile should consider:

- purpose and expected decisions;
- role, expertise and domain vocabulary;
- preferred language and cultural context;
- expected reading time and information density;
- accessibility and assistive-technology needs;
- device, bandwidth and interaction constraints;
- human, machine or hybrid consumption mode;
- required evidence, traceability and confidence detail.

Audience profiles describe delivery needs. They shall not be used to stereotype individuals or to remove material facts that are necessary for informed understanding.

## Cultural and linguistic adaptation

Translation alone is not sufficient cultural adaptation.

Communication conventions differ across regions, countries, professions, organisations, generations and communities. Adaptation may therefore include tone, examples, argument order, directness, terminology, visual conventions, date and number formats, legal context and expectations about authority or uncertainty.

Cultural adaptation shall preserve semantic integrity and shall identify material localisation choices when they could affect interpretation.

## Diversity and accessibility

Audience-aware delivery shall account for relevant dimensions of human diversity, including sensory, physical, cognitive, linguistic and neurodiverse needs.

Accessibility includes, but is not limited to:

- semantic headings and meaningful navigation;
- keyboard operation and visible focus;
- sufficient contrast and non-colour-only meaning;
- alternative text and textual equivalents;
- readable typography and responsive layout;
- plain-language orientation and progressive disclosure;
- captions, transcripts and accessible document formats;
- avoidance of unnecessary cognitive load.

Compliance with a technical accessibility standard is an important control, but it does not by itself prove that the intended audience can understand the material.

## Cognitive accessibility

Cognitive accessibility asks not only whether content can be opened or read, but whether the intended audience can form an accurate and useful mental model with reasonable effort.

A delivery should therefore provide appropriate entry points, summaries, signposting, examples, definitions and paths to deeper evidence.

Complexity inherent in the subject shall not be hidden. Accidental complexity introduced by poor structure, unexplained terminology or unsuitable presentation should be removed.

## Adaptive rendering

A governed publication system may derive multiple audience-specific representations from one canonical knowledge base, including:

- a complete book for sustained reading;
- an executive brief for rapid orientation;
- a presentation for facilitated communication;
- an accessible website for exploration;
- a review package for independent assurance;
- structured JSON, manifests or APIs for machines;
- localised language and culture profiles;
- assisted views for human–AI collaboration.

Each transformation shall remain traceable to canonical sources and shall disclose its audience, purpose and material limitations.

## Findability and interaction

Users should not need to understand repository internals, build systems or file naming conventions to obtain an approved publication.

A human-facing publication hub should provide:

- a clear project introduction;
- visible publication status and freshness;
- direct access to the latest book, brief, presentation and review package;
- format choices explained in human terms;
- an online reading path;
- provenance and source access without making them the primary navigation burden.

Machine-facing discovery should provide stable URLs, structured metadata, checksums and explicit media types.

## Validation

Audience-adaptive delivery should be evaluated through evidence appropriate to the audience, such as:

- task completion and findability tests;
- comprehension and decision-quality checks;
- accessibility testing with automated and human methods;
- localisation review by relevant cultural and linguistic competence;
- machine-schema validation and deterministic retrieval tests;
- feedback from actual users, including people using assistive technologies;
- inspection of semantic equivalence across representations.

A successful build proves that an artefact was generated. It does not prove that the artefact is understandable, culturally appropriate or usable.

## Governance requirements

Audience adaptation is a governed semantic transformation, not merely visual styling.

Every material audience-specific representation shall expose or link to:

- its intended audience and purpose;
- its canonical source revision;
- its review and evidence status;
- relevant accessibility or localisation profile;
- material omissions, compression or interpretation;
- a feedback or correction path.

Adaptation shall never be used to obscure uncertainty, suppress inconvenient evidence or create unjustified confidence.

## Relationship to Mission Framework

Audience-Adaptive Knowledge Delivery supports:

- **Trust Bootstrap**, by giving each audience an understandable and inspectable entry point;
- **Credibility Onboarding**, by reducing avoidable barriers to initial comprehension;
- **Evidence Maturity**, by presenting maturity information at an appropriate level without removing traceability;
- **Publication Governance**, by defining audience adaptation as a controlled transformation;
- **Independent Assurance**, by making review material both navigable for people and parseable for machines;
- **Operational Adoption**, by enabling knowledge to fit real human and machine workflows.

## Governing statement

> Availability is not usability, and usability is not understanding. Governed knowledge delivery shall respect the audience while preserving the evidence.