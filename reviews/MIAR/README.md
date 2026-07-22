# Mission Framework Independent Assurance Review (MIAR)

**Status:** Review programme specification  
**Version:** 1.0  
**Owner:** Mission Framework governance  
**Applies to:** Independent AI and human reviewers

MIAR is a common assurance programme for independent examination of the Mission Framework ecosystem. Every participating AI receives the same core assignment and must work independently before cross-review or synthesis.

## Required repository scope

Review the complete authoritative default branch of all five repositories:

1. `https://github.com/froekjaer/-Publication-Pipeline`
2. `https://github.com/froekjaer/collaborative-intelligence`
3. `https://github.com/froekjaer/Mission-Platform`
4. `https://github.com/froekjaer/mission-solar-eclipse`
5. `https://github.com/froekjaer/mission-framework`

Do not limit the review to README files. Inspect all material files, history needed to understand current state, open design dependencies, governance, reviews, implementation artefacts and cross-repository references.

Record the branch, commit SHA and review date for every repository. A repository that cannot be accessed or fully inspected must be marked as a scope limitation.

## Required review products

Each reviewer shall deliver:

1. **Project and system review** — purpose, coherence, architecture, semantics, implementation, governance, evidence, adoption and maintainability.
2. **Project risk assessment** — strategic, governance, delivery, research, resource, competence, dependency, adoption, financial, legal, longevity and AI-assisted working risks.
3. **Cyber and regulatory risk assessment** — architecture, operational controls, software supply chain, AI security, privacy, resilience, incident handling and applicable regulatory obligations.
4. **Operational integration review** — review the reviewer platform's own directory under `docs/operational/`, including its README and loader files.
5. **Invitation assurance review** — review the invitation intended for a suitable person in the reviewer's organisation and assess its accuracy, legitimacy, clarity and non-deceptive presentation.
6. **Human recipient nomination** — identify a suitable real person or official organisational function that may receive the invitation, using only verified public information.
7. **AI attestation** — provide a bounded statement describing which AI produced the review, what it examined, its limitations and whether it considers the invitation suitable to send.

Mistral shall treat this as its first complete Mission Framework review. All other reviewers shall also perform the complete project review rather than relying on earlier partial reviews.

## Mandatory evidence discipline

Use these labels throughout:

- **VERIFIED** — directly supported by an authoritative source inspected during the review.
- **DERIVED** — reproducibly inferred from verified evidence.
- **ASSUMED** — not yet verified; never use as operational fact.
- **JUDGEMENT** — professional or model assessment, clearly distinguished from fact.

Cite repository paths, commit SHAs and external primary sources. Separate current fact from historical material, proposals and reviewer opinion.

## Independence

Reviewers must not read other reviewers' MIAR conclusions before completing their own first version. They may inspect prior project artefacts and historical reviews when needed to understand the system, but shall disclose any such exposure.

The task is not to endorse the project. Attempt falsification, identify contradictions, test failure modes and recommend stopping or redesign where evidence supports it.

## Confidential legacy evidence

Two 2013 Executive MBA reports by Peter Frøkjær are part of the controlled review package:

- `Documentation report - Peter Frøkjær-dkv-froekjap1.pdf`
- `Excecutive report-Peter Frøkjær.pdf`

They are marked confidential and shall not be committed to a public repository without explicit authorisation. A reviewer must confirm whether the reports and their bibliographies were supplied and read. Findings based on them must be labelled as controlled-source findings and paraphrased unless publication permission exists.

The legacy reports are relevant to process design, stakeholder ownership, management buy-in, capability and competence gaps, scenario-based research, market segmentation, iterative testing, financial viability and organisational adoption. They are historical evidence, not automatically current authority.

## Required outputs and file names

Place completed reviews under the relevant reviewer directory:

- `reviews/<reviewer>/MIAR-PROJECT-REVIEW-v1.md`
- `reviews/<reviewer>/MIAR-PROJECT-RISK-v1.md`
- `reviews/<reviewer>/MIAR-CYBER-RISK-v1.md`
- `reviews/<reviewer>/MIAR-OPERATIONAL-VALIDATION-v1.md`
- `reviews/<reviewer>/MIAR-INVITATION-VALIDATION-v1.md`
- `reviews/<reviewer>/MIAR-AI-ATTESTATION-v1.md`

Use `RESPONSE-TEMPLATE.md` and `RISK-METHOD.md` in this directory. Proposed canonical changes shall be submitted through reviewable pull requests, not written silently to `main`.

## Token and cost discipline

Read each canonical artefact once per review session where tooling permits, cache hashes and summaries, and retrieve only changed files on subsequent passes. Do not duplicate full canonical documents inside prompts or review files. Evidence citations and concise summaries are preferred over copied text.

Token economy must never be achieved by skipping required repositories, source validation, adverse findings or write verification.