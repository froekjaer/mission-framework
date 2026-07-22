# MIAR dual-invitation protocol

**Status:** Common assurance protocol  
**Version:** 1.0  
**Applies to:** `reviews/chatgpt/`, `reviews/claude/`, `reviews/codex/`, `reviews/mistral/`, and `reviews/z-ai/`

Each AI reviewer directory contains two invitations with different recipients, purposes and completion gates.

## 1. AI-agent invitation

**File:** `MIAR-AGENT-INVITATION.md`

This invitation is addressed to the focal AI agent. It activates the complete MIAR assignment and requires the agent to:

- read and review all five repositories;
- perform the complete project, project-risk, cyber/regulatory and falsification work;
- follow the four MIAR phases and preserve independence;
- review its own platform directory under `docs/operational/`;
- review and complete the separate organisational invitation;
- return review artefacts and a send-ready organisational invitation for human approval.

The agent invitation is a project instruction. It is not intended to be sent to the AI provider as external correspondence.

## 2. Organisational invitation

**File:** `MIAR-INVITATION.md`

This invitation is intended for a suitable human recipient or official function in the organisation responsible for the focal AI agent.

The focal AI agent MUST complete and validate this invitation but MUST NOT send it.

### Completion requirements

After freezing its independent Phase 1 conclusions, the focal AI agent MUST:

1. identify a suitable current person or official organisational function;
2. verify the organisation, recipient name, current title or function and a legitimate public professional contact route using authoritative current sources;
3. record the sources and access date in `MIAR-INVITATION-VALIDATION-v1.md`;
4. insert the verified recipient and contact information into `MIAR-INVITATION.md`;
5. adapt tone, terminology, salutation, length and presentation where appropriate to the organisation's culture;
6. state what was adapted and why;
7. remove all unresolved placeholders before recommending that the invitation be sent;
8. return the invitation for human approval.

A guessed email pattern, inferred private address, stale role, scraped personal contact detail or unverified social-media profile is not an acceptable contact route.

## Permitted cultural adaptation

The focal AI agent MAY adapt:

- salutation and degree of formality;
- terminology familiar to the recipient organisation;
- ordering and concision of explanatory material;
- emphasis on research, safety, engineering, public interest, European context or another relevant organisational concern;
- the proposed recipient, provided the selection is verified and justified.

## Invariants that MUST NOT be weakened

Cultural adaptation MUST NOT alter or remove:

- the complete five-repository scope;
- reviewer independence;
- the governing falsification requirement;
- disclosure of limitations and unresolved risks;
- the distinction between AI attestation and organisational endorsement;
- the statement that no accreditation, certification or approval by the provider is implied;
- the invitation to report adverse findings or recommend stopping or redesigning the project;
- human approval before transmission;
- evidence and contact-verification requirements.

## Attestation boundary

The focal AI agent may attest that it produced specified review artefacts, examined specified sources, applied the MIAR method and considers the invitation suitable or unsuitable to send.

It MUST NOT claim that its provider, developers, employees or named recipient have:

- accredited Mission Framework;
- certified the review;
- endorsed the project;
- authorised the invitation;
- accepted responsibility for the AI's conclusions.

Only an authorised human or organisational response may establish such a relationship.

## Timing and independence

During Phase 1, the reviewer may assess the organisational invitation's structure, truthfulness, scope and safeguards. Recipient nomination, current-contact verification and final cultural adaptation MUST occur only after the independent Phase 1 conclusions are frozen, so external-recipient research does not influence the initial project conclusions.

## Naming rule

Every focal reviewer directory therefore contains:

```text
MIAR-AGENT-INVITATION.md   # addressed to the AI agent
MIAR-INVITATION.md         # addressed to the human/organisation
```

The corresponding validation output remains:

```text
MIAR-INVITATION-VALIDATION-v1.md
```
