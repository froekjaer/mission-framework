# Mission Framework — REVIEW-001 Invitation

## Mission Platform Transformation Lab

You are invited to participate as an independent architect and builder in Mission Framework REVIEW-001.

## Source system — strictly read-only

- Repository: `froekjaer/timelapse-pro`
- Frozen source baseline: commit `eed9e3c8c67369e1924c25a11908616220c3c753`
- You are expected to read and evaluate both the documentation and the source code from this frozen baseline.
- The entire `froekjaer/timelapse-pro` repository is read-only for this exercise.
- Do not commit, push, create branches, open or modify pull requests or issues, change configuration, or otherwise write to `froekjaer/timelapse-pro`.
- Treat its documentation, code, ADRs, tests, runtime evidence and history as source evidence and migration input only.

## Destination — all new work lives here

- Repository: `froekjaer/Mission-Platform`
- All architecture, documentation, ADRs, schemas, code, tests, tooling, migration work and proof-of-concepts created during REVIEW-001 must be written only to your assigned reviewer branch in `froekjaer/Mission-Platform`.
- Your work must remain isolated in the reviewer workspace assigned to you.
- Do not inspect or reuse another reviewer’s work before independent submission.
- Do not merge your reviewer branch directly into `main`.

In operational terms:

> Read and evaluate `froekjaer/timelapse-pro`; build the new modular solution in `froekjaer/Mission-Platform`.

## Mission

Transform the capabilities and experience embodied in TimeLapse Pro into a modular, reusable Mission Platform without losing the ability to deliver the existing timelapse use case.

TimeLapse is the first functional payload, not the boundary of the platform. The architecture must also be credible for future payloads such as:

- small waterworks;
- small power plants and energy installations;
- maritime monitoring;
- environmental and agricultural sensing;
- SDR, AIS, DSC and ADS-B services;
- AI vision and other edge workloads.

Only the timelapse payload must become functionally demonstrable during REVIEW-001. The other domains are architectural test cases against accidental timelapse coupling.

## Start with the mission, not the code

Work from business purpose toward implementation. SABSA is the recommended thinking structure:

1. Business/contextual architecture
2. Conceptual architecture
3. Logical architecture
4. Physical architecture
5. Component architecture
6. Operational architecture

You may choose or combine another method, including TOGAF, domain-driven design, hexagonal architecture, event-driven architecture or C4. A different method is welcome when you document why it is better suited, what it replaces, what risks it introduces and how traceability to business needs is preserved.

## Three mandatory questions

For every material decision, preserve a traceable answer to:

- **Why?** What mission, stakeholder need or necessary value does this serve?
- **Because?** What evidence, constraint, dependency, risk or responsibility justifies it?
- **For whom and according to whose need?** How is capability delivered proportionately to need, consequence, cost, quality, privacy, sovereignty, accessibility and accountability?

Guiding principle:

> Deliver the right intelligence and capability where it creates necessary value, proportionate to need, consequence, cost, sovereignty and accountability.

## Existing architecture is evidence, not an unquestionable answer

Accepted ADRs and current operating evidence in TimeLapse Pro form the baseline. You must understand them before changing direction. You may challenge or replace an accepted architecture decision in your Mission Platform proposal only through a new ADR written in your assigned Mission Platform branch. That ADR must describe:

- the decision being challenged;
- the evidence and reasoning;
- alternatives considered;
- migration and compatibility consequences;
- security, safety, operational and regulatory effects;
- a reversible validation path.

No such challenge authorizes a change to `froekjaer/timelapse-pro` during REVIEW-001.

## Freedom and constraints

Within your assigned `froekjaer/Mission-Platform` branch, you may restructure code, create contracts and schemas, add ADRs, build proof-of-concepts, migrate components and propose new technology.

You must:

- preserve the frozen TimeLapse Pro source baseline reference;
- record which source components were reused, adapted, rewritten or rejected;
- keep changes reversible until validated;
- avoid hard deletion of source evidence;
- separate platform and payload concerns;
- separate control plane and data plane;
- make privilege and capability enforcement fail closed;
- preserve explicit ownership of purpose, prompts, data classification, retention and results for every AI use;
- document uncertainty rather than hide it;
- leave a reproducible decision and evidence trail.

## Collaborative intelligence assessment

In addition to your own solution, recommend who or what type of contributor is best suited to each layer. Consider other AI systems, specialist tools and humans. Do not rely on brand reputation alone; explain the competencies, limitations, validation needs and accountability required for:

- mission and business architecture;
- security, safety and trust;
- OT/ICS and edge engineering;
- data architecture;
- AI and model orchestration;
- software implementation and refactoring;
- test and verification;
- DevSecOps and lifecycle management;
- UX and accessibility;
- regulatory and contractual analysis;
- operations and incident response;
- final decision authority.

## Required outputs

Your Mission Platform workspace must contain at minimum:

- executive summary;
- business and stakeholder architecture;
- business attributes and measurable success criteria;
- conceptual, logical, physical, component and operational architecture;
- platform/payload boundary and versioned contracts;
- security, privacy, safety and compliance architecture;
- AI and capability allocation model;
- target repository structure;
- migration strategy from TimeLapse Pro;
- source-to-target traceability showing reused, adapted, rewritten and rejected elements;
- risk register and assumptions;
- ADRs for material choices;
- implementation roadmap;
- proof-of-concept or executable vertical slice;
- test, evidence and acceptance plan;
- reviewer self-assessment and recommended division of labour.

## Independence and submission

Do not attempt to predict or converge on the work of other reviewers. Divergence is valuable when it is reasoned and evidenced.

When your work is ready:

1. complete the submission checklist in your workspace;
2. freeze the reviewed commit SHA;
3. provide a concise handover;
4. stop implementation until the blind comparison and meta-review begin.

No reviewer solution is merged automatically. Mission Framework will compare the independent results, preserve dissent, select the strongest supported elements and create a separately governed reference architecture.

## Mission owner

Peter Frøkjær is Mission Owner and retains final authority over whether a proposal serves the mission. The Mission Owner does not prescribe the technical solution and should not remove productive diversity before independent submission.

## Prospective improvements (apply from REVIEW-002 onward)

The items below are **prospective** improvements identified after REVIEW-001 was issued. They clarify the standard for future reviews. They do **not** change the requirements that were in force when REVIEW-001 submissions were produced, and a REVIEW-001 submission SHALL NOT be marked non-compliant for not following them.

- **Risk perspectives (from REVIEW-002).** Reviewers SHALL submit two separate risk analyses — project/implementation risk and cyber/regulatory risk — following [`reviews/MIAR/RISK-METHOD.md`](../../reviews/MIAR/RISK-METHOD.md), unless the review invitation explicitly states otherwise. For REVIEW-001, a single combined risk register remains acceptable.
- **Regulatory horizon.** Reviewers SHALL assess applicability of the instruments listed in [`review-kit/regulatory-horizon.md`](../../review-kit/regulatory-horizon.md) rather than assume every listed instrument applies. The horizon is a governed scanning artefact, not legal advice.
- **Framework vs. Platform classification.** The Meta Review SHALL classify every synthesis decision as FRAMEWORK, PLATFORM, BOTH, PAYLOAD-SPECIFIC, or DEFERRED (see [`META-REVIEW.md`](META-REVIEW.md)).

These prospective items are recorded here so future reviewers and the Mission Owner share a single source of truth for what improved and when it takes effect.
