# Mission Framework Independent Assurance Review (MIAR)

**Status:** Review programme specification  
**Version:** 1.1  
**Owner:** Mission Framework governance  
**Applies to:** Independent AI and human reviewers

MIAR is a common assurance programme for independent examination of the Mission Framework ecosystem. Every participating AI receives the same core assignment and must work independently before cross-review or synthesis.

## Governing falsification rule

> **A review is not complete until the reviewer has actively attempted to prove the project wrong.**

This is a normative **MUST** requirement. A reviewer MUST attempt falsification, identify contradictions, test failure modes and recommend stopping, narrowing or redesigning the project where the evidence supports it. A review that only confirms, improves or endorses the current design is incomplete.

The reviewer MUST document:

- the strongest arguments against the project;
- assumptions that were deliberately challenged;
- failure scenarios tested;
- evidence that would invalidate major conclusions;
- claims that survived falsification and why;
- claims that did not survive or remain unresolved.

## Required repository scope

Review the complete authoritative default branch of all five repositories:

1. `https://github.com/froekjaer/-Publication-Pipeline`
2. `https://github.com/froekjaer/collaborative-intelligence`
3. `https://github.com/froekjaer/Mission-Platform`
4. `https://github.com/froekjaer/mission-solar-eclipse`
5. `https://github.com/froekjaer/mission-framework`

Do not limit the review to README files. Inspect all material files, history needed to understand current state, open design dependencies, governance, reviews, implementation artefacts and cross-repository references.

Record the branch, commit SHA and review date for every repository. A repository that cannot be accessed or fully inspected must be marked as a scope limitation.

## Four-phase review protocol

### Phase 1 - Independent public-evidence review

The reviewer MUST use the five public repositories and authoritative external primary sources only.

The reviewer MUST complete and freeze:

- the project and system review;
- the project risk assessment;
- the cyber and regulatory risk assessment;
- the operational integration review;
- the invitation assurance review;
- the AI attestation;
- the falsification record.

The frozen Phase 1 version MUST include repository commit SHAs and a timestamp. It MUST NOT be altered silently after access to historical evidence or other reviewers' conclusions.

### Phase 2 - Historical Evidence Package

Only after Phase 1 is frozen may the reviewer read `evidence/historical/`.

The reviewer MUST produce a delta report identifying:

- every conclusion that changed;
- every conclusion whose confidence increased or decreased;
- every new risk, contradiction or dependency found;
- historical evidence that did not affect the conclusions;
- whether the historical material supports continuity, exposes hindsight bias, or creates a misleading origin narrative.

Phase 2 is not a replacement review. It measures the effect of additional evidence on the frozen Phase 1 conclusions.

### Phase 3 - Independent cross-review

Only after completing Phase 2 may the reviewer read other reviewers' MIAR outputs.

The reviewer MUST identify:

- findings it missed;
- findings it disputes and why;
- common conclusions reached independently;
- possible correlated model or source bias;
- unresolved conflicts requiring human decision.

No reviewer may rewrite its original Phase 1 result to create artificial consensus.

### Phase 4 - Synthesis

A synthesis may be produced only after all available independent reviews and delta reports are preserved.

The synthesis MUST distinguish:

- consensus;
- majority judgement;
- minority findings;
- unresolved contradictions;
- human governance decisions;
- recommended stop, redesign, experiment or proceed decisions.

The synthesis is not permitted to erase adverse findings.

## Required review products

Each reviewer shall deliver:

1. **Project and system review** - purpose, coherence, architecture, semantics, implementation, governance, evidence, adoption and maintainability.
2. **Project risk assessment** - strategic, governance, delivery, research, resource, competence, dependency, adoption, financial, legal, longevity and AI-assisted working risks.
3. **Cyber and regulatory risk assessment** - architecture, operational controls, software supply chain, AI security, privacy, resilience, incident handling and applicable regulatory obligations.
4. **Operational integration review** - review the reviewer platform's own directory under `docs/operational/`, including its README and loader files.
5. **Invitation assurance review** - review the invitation intended for a suitable person in the reviewer's organisation and assess its accuracy, legitimacy, clarity and non-deceptive presentation.
6. **Human recipient nomination** - identify a suitable real person or official organisational function that may receive the invitation, using only verified public information.
7. **AI attestation** - provide a bounded statement describing which AI produced the review, what it examined, its limitations and whether it considers the invitation suitable to send.
8. **Falsification record** - document the active attempt to prove the project wrong.
9. **Historical evidence delta** - document Phase 2 changes against the frozen Phase 1 review.
10. **Cross-review delta** - document Phase 3 changes and conflicts without rewriting Phase 1.

Mistral shall treat this as its first complete Mission Framework review. All other reviewers shall also perform the complete project review rather than relying on earlier partial reviews.

## Mandatory evidence discipline

Use these labels throughout:

- **VERIFIED** - directly supported by an authoritative source inspected during the review.
- **DERIVED** - reproducibly inferred from verified evidence.
- **ASSUMED** - not yet verified; never use as operational fact.
- **JUDGEMENT** - professional or model assessment, clearly distinguished from fact.

Cite repository paths, commit SHAs and external primary sources. Separate current fact from historical material, proposals and reviewer opinion.

## Independence

Reviewers must not read other reviewers' MIAR conclusions before completing Phases 1 and 2. They may inspect prior project artefacts needed to understand the system but shall disclose any exposure that could reduce independence.

## Historical evidence

Two 2013 Executive MBA reports by Peter Frøkjær are published as historical evidence under `evidence/historical/`:

- `CRP-001-Executive-MBA-Documentation-Report-2013.pdf`
- `CRP-001-Executive-MBA-Documentation-Report-2013.md`
- `CRP-002-Executive-MBA-Executive-Report-2013.pdf`
- `CRP-002-Executive-MBA-Executive-Report-2013.md`

The PDFs are authoritative historical sources. The Markdown files are derived, AI-searchable transcriptions. In case of discrepancy, the PDF controls.

The reports are relevant to process design, stakeholder ownership, management buy-in, capability and competence gaps, scenario-based research, market segmentation, iterative testing, financial viability and organisational adoption. They are historical evidence, not current authority, and cannot override canonical governance.

## Required outputs and file names

Place completed reviews under the relevant reviewer directory:

- `reviews/<reviewer>/MIAR-PROJECT-REVIEW-v1.md`
- `reviews/<reviewer>/MIAR-PROJECT-RISK-v1.md`
- `reviews/<reviewer>/MIAR-CYBER-RISK-v1.md`
- `reviews/<reviewer>/MIAR-OPERATIONAL-VALIDATION-v1.md`
- `reviews/<reviewer>/MIAR-INVITATION-VALIDATION-v1.md`
- `reviews/<reviewer>/MIAR-AI-ATTESTATION-v1.md`
- `reviews/<reviewer>/MIAR-FALSIFICATION-RECORD-v1.md`
- `reviews/<reviewer>/MIAR-HISTORICAL-EVIDENCE-DELTA-v1.md`
- `reviews/<reviewer>/MIAR-CROSS-REVIEW-DELTA-v1.md`

Use `RESPONSE-TEMPLATE.md` and `RISK-METHOD.md` in this directory. Proposed canonical changes shall be submitted through reviewable pull requests, not written silently to `main`.

## Token and cost discipline

Read each canonical artefact once per review session where tooling permits, cache hashes and summaries, and retrieve only changed files on subsequent passes. Do not duplicate full canonical documents inside prompts or review files. Evidence citations and concise summaries are preferred over copied text.

Token economy must never be achieved by skipping required repositories, source validation, adverse findings, falsification work or write verification.