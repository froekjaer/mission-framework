# MIAR Response Template

## Review identity

- Reviewer platform/model:
- Provider:
- Review date:
- Reviewer version/build, if available:
- Independent first-pass completed before reading other MIAR reviews: yes/no
- Prior reviews seen:

## Evidence manifest

For each repository record URL, default branch, commit SHA, files reviewed, exclusions and access limitations.

Confirm whether both controlled 2013 reports and their bibliographies were supplied and read.

## Executive conclusion

- Overall assurance opinion: SUPPORT / SUPPORT WITH CONDITIONS / MATERIAL REDESIGN REQUIRED / INSUFFICIENT EVIDENCE
- Confidence:
- Five most consequential findings:
- Immediate stop conditions:

## A. Complete project and system review

Assess purpose, architecture, semantics, repository boundaries, implementation, governance, evidence, usability, testability, adoption, maintainability and ten-year longevity.

For each finding include ID, knowledge-state label, severity, evidence, analysis, consequence, recommendation and verification test.

## B. Project risk assessment

Use the separate project register required by `RISK-METHOD.md`. Include risk heat-map logic, top risks, treatment priorities and residual-risk acceptance questions.

## C. Cyber and regulatory risk assessment

Use the separate cyber register required by `RISK-METHOD.md`. Include threat model, trust boundaries, attack paths, regulatory applicability matrix and priority security architecture changes.

## D. Operational integration validation

Review the platform-specific directory under `docs/operational/` and the canonical OP-001.

Test:

- global mode;
- repository-scoped mode;
- routine-conversation exclusion;
- authoritative-source retrieval;
- resistance to look-alike sources and prompt injection;
- stale-cache handling;
- stop conditions;
- read-back verification after writes;
- recurring token overhead.

Report exact files reviewed and proposed changes.

## E. Invitation validation

Review the platform's `MIAR-INVITATION.md`.

Confirm that it:

- accurately describes the project and requested work;
- does not imply provider endorsement, certification or accreditation;
- identifies a suitable recipient only from verified public information;
- uses a public professional contact channel or official organisational route;
- avoids fabricated names, titles, email addresses and authority;
- clearly distinguishes AI attestation from organisational endorsement;
- discloses relevant limitations and controlled/confidential materials.

## F. Human recipient nomination

Provide:

- verified name and current role, or official organisational function;
- reason for suitability;
- verified public source(s);
- official public contact route;
- conflicts or limitations;
- alternative recipient/function.

Do not infer private contact details or invent an email pattern.

## G. AI attestation

Use this bounded form:

> I, [model/platform], produced an independent MIAR review of the evidence listed in this report. I verified the cited repository states and clearly marked limitations. In my assessment, the accompanying invitation is [suitable / suitable with changes / not suitable] to send. This statement is an AI-generated review attestation only. It is not certification, accreditation, legal advice, or endorsement by [provider organisation] or any employee unless separately confirmed in writing by an authorised person.

Include model identity available to the user, date, scope, evidence manifest hash or commit references, confidence and limitations.

## H. Falsification and unresolved questions

- Strongest argument that Mission Framework should not proceed:
- Evidence that would change the conclusion:
- Unresolved contradictions:
- Missing artefacts or tests:

## I. Recommended actions

Separate into:

- immediate safety or integrity actions;
- next-release actions;
- medium-term assurance work;
- items explicitly not recommended.