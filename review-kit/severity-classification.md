# Severity Classification Standard

## Purpose

This standard defines a shared severity model for findings recorded during Mission Framework reviews.

The objective is to ensure that reviewers, contributors, and decision-makers classify findings consistently, explain their reasoning, and apply proportionate responses.

## Core principles

Severity is determined by risk, not by reviewer preference.

Every classification should consider:

- potential impact;
- likelihood of occurrence;
- urgency;
- scope of exposure;
- reversibility;
- available controls or mitigations;
- confidence in the supporting evidence.

A severity level SHALL be supported by a concise rationale and traceable evidence.

## Severity levels

### Critical

A Critical finding represents an immediate or potentially catastrophic risk.

Typical characteristics include:

- serious threat to life, safety, legality, security, or mission viability;
- a condition that can cause severe and widespread harm;
- absence or failure of an essential control;
- confirmed exploitation, compromise, or material breach;
- a release or operational blocker;
- no acceptable temporary workaround.

**Required response:** Approval and release are blocked. The issue SHALL be escalated immediately, assigned an accountable owner, and remediated before approval. Risk acceptance is exceptional and requires explicit authorization at the highest appropriate level.

### Major

A Major finding represents a significant weakness that can materially affect correctness, security, compliance, reliability, usability, or intended outcomes.

Typical characteristics include:

- substantial requirement or control failure;
- material contradiction or omission;
- unsupported claim central to the component;
- high-impact risk with a plausible path to occurrence;
- implementation cannot reliably proceed as written;
- a workaround exists but is incomplete, fragile, or costly.

**Required response:** Approval is normally blocked until remediation is verified. An authorized decision-maker MAY accept the residual risk when the rationale, conditions, owner, and deadline are recorded.

### Minor

A Minor finding represents a limited weakness that does not materially prevent the component from fulfilling its intended purpose.

Typical characteristics include:

- localized ambiguity or inconsistency;
- incomplete non-critical traceability;
- low-impact control weakness;
- maintainability or usability issue with limited exposure;
- correction is straightforward and does not change the overall conclusion.

**Required response:** The issue SHOULD be corrected before release where practical. It MAY be deferred with an owner and documented disposition.

### Observation

An Observation is a non-blocking note, improvement opportunity, positive control, or emerging concern that does not currently constitute a defect.

Typical characteristics include:

- optional enhancement;
- future risk worth monitoring;
- useful clarification;
- good practice that should be preserved;
- insufficient evidence to assert a defect, with uncertainty clearly stated.

**Required response:** No mandatory corrective action. The owner SHOULD consider and record whether the observation will be adopted, monitored, or closed without action.

## Impact scale

### 1 — Low

Limited effect on a small area. Easily reversible. No material effect on mission, safety, legality, security, or release suitability.

### 2 — Moderate

Noticeable effect on quality, usability, cost, schedule, or a limited control objective. Recovery is practical.

### 3 — High

Material effect on important outcomes, stakeholders, controls, compliance, security, or operational reliability. Recovery may be difficult or costly.

### 4 — Severe

Catastrophic, widespread, irreversible, unlawful, life-safety, mission-ending, or systemic impact.

## Likelihood scale

### 1 — Unlikely

Requires unusual conditions or has little supporting evidence.

### 2 — Possible

Could occur under credible conditions, but is not expected frequently.

### 3 — Likely

Expected to occur or recur in normal or foreseeable conditions.

### 4 — Almost certain

Already occurring, repeatedly observed, actively exploited, or expected without immediate intervention.

## Risk matrix

The matrix is a decision aid, not a substitute for judgment.

| Impact \ Likelihood | 1 Unlikely | 2 Possible | 3 Likely | 4 Almost certain |
|---|---:|---:|---:|---:|
| **1 Low** | Observation | Minor | Minor | Major |
| **2 Moderate** | Minor | Minor | Major | Major |
| **3 High** | Minor | Major | Major | Critical |
| **4 Severe** | Major | Major | Critical | Critical |

Reviewers MAY adjust the matrix outcome when urgency, exposure, reversibility, legal obligation, control failure, or evidence confidence materially changes the risk. The rationale SHALL be recorded.

## Classification rules

1. Classify the risk created by the finding, not the amount of work required to fix it.
2. Use the highest credible severity when one finding creates several impacts.
3. Do not lower severity solely because a problem has not yet caused harm.
4. Consider existing controls only when their effectiveness is evidenced.
5. Separate severity from remediation priority where necessary.
6. Record uncertainty and confidence.
7. Split findings that contain unrelated conditions with different risks.
8. Do not combine multiple Minor findings into a Major finding unless their interaction creates a material combined risk.
9. Positive observations SHALL NOT offset blocking findings.
10. The final decision-maker may change a classification only with documented rationale.

## Required finding fields

Every classified finding SHALL include:

- finding ID and title;
- severity;
- affected component or location;
- observed condition;
- expected condition or criterion;
- supporting evidence;
- impact;
- likelihood;
- severity rationale;
- confidence level;
- recommendation;
- status and owner where applicable.

## Confidence

- **High:** direct, authoritative, reproducible evidence.
- **Medium:** credible evidence with limited uncertainty or incomplete reproduction.
- **Low:** indirect, incomplete, conflicting, or largely inferential evidence.

Low confidence SHALL NOT automatically reduce severity. It may instead require additional investigation or an `Unable to conclude` outcome.

## Escalation

- Critical findings SHALL be escalated immediately to the accountable maintainer and decision-maker.
- Major findings SHALL be visible to the decision-maker before approval.
- Security, privacy, legal, ethical, or life-safety findings SHALL be shared only with appropriately authorized people when disclosure could increase harm.
- Unresolved disputes about severity SHALL be recorded and decided through the governance process.

## Risk acceptance

Risk acceptance does not remove a finding. It records a decision to proceed despite residual risk.

An acceptance SHALL identify:

- the finding;
- decision-maker;
- rationale;
- affected scope;
- residual risk;
- compensating controls;
- conditions and deadline;
- review or expiry date where applicable.

Critical risk acceptance should be exceptional. Major risk acceptance requires explicit authorization. Minor findings may be deferred through normal ownership and planning.

## Relationship to review outcomes

| Highest unresolved severity | Normal reviewer recommendation |
|---|---|
| Critical | Changes required or Reject |
| Major | Changes required |
| Minor | Approve with conditions or Approve |
| Observation only | Approve |
| Evidence insufficient | Unable to conclude |

The final decision SHALL consider the number, interaction, and context of findings, not only the single highest severity.

## Examples

### Critical example

A release process exposes active credentials that permit unauthorized modification of normative artifacts, with no effective revocation or containment control.

### Major example

A core standard requires a control but provides contradictory implementation requirements that make compliant deployment unreliable.

### Minor example

A template omits a non-critical traceability field, while the remaining process still preserves the principal decision record.

### Observation example

A reviewer identifies an opportunity to automate link checking, but no broken or misleading references are currently present.

## Review and maintenance

This severity model SHALL be reviewed when repeated classification disputes, new risk domains, or material governance changes show that it no longer produces consistent decisions.
