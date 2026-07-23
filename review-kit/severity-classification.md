# Severity Classification Standard

## Purpose

This standard defines a shared severity model for findings recorded during Mission Framework reviews.

The objective is to ensure that reviewers, contributors, and decision-makers classify findings consistently, explain their reasoning, and apply proportionate responses.

## Core Principles

Severity is determined by risk, not by reviewer preference.

Every classification should consider:

- potential impact
- likelihood of occurrence
- urgency
- scope of exposure
- reversibility
- available controls or mitigations
- confidence in the supporting evidence

A severity level must be supported by a concise rationale and traceable evidence.

## Severity Levels

### Critical

A Critical finding represents an immediate or potentially catastrophic risk.

Typical characteristics include:

- serious threat to life, safety, legality, security, or mission viability
- a condition that can cause severe and widespread harm
- absence or failure of an essential control
- confirmed exploitation, compromise, or material breach
- a release or operational blocker
- no acceptable temporary workaround

Required response:

- escalate immediately
- stop affected release, deployment, publication, or activity where appropriate
- assign an accountable owner
- define urgent containment and remediation actions
- obtain explicit approval before accepting residual risk

Default review effect:

- Changes required
- Rejected, when the risk cannot be reduced to an acceptable level

### Major

A Major finding represents a significant weakness that can materially affect objectives, quality, compliance, security, reliability, or trust.

Typical characteristics include:

- substantial impact if the condition occurs
- plausible likelihood of occurrence
- incomplete or ineffective control coverage
- important requirement not met
- significant evidence gap
- defect likely to produce incorrect, unsafe, or misleading outcomes
- workaround exists but is costly, fragile, or temporary

Required response:

- assign an owner and target date
- remediate before release or approval unless risk is formally accepted
- document compensating controls where remediation is deferred
- verify closure through follow-up review

Default review effect:

- Changes required
- Approved with observations only when risk acceptance is explicit and justified

### Minor

A Minor finding represents a limited weakness with low or moderate impact.

Typical characteristics include:

- narrow scope
- low likelihood or limited consequence
- non-critical inconsistency
- documentation weakness that does not invalidate the work
- small process deviation
- improvement that should be scheduled but does not block release

Required response:

- record the finding
- assign corrective action where proportionate
- track remediation through normal maintenance or improvement work

Default review effect:

- Approved with observations
- Approved when the issue is accepted as negligible

### Observation

An Observation identifies a useful insight, emerging concern, or improvement opportunity that does not currently constitute a defect or material risk.

Typical characteristics include:

- potential future issue
- opportunity for clarification, simplification, or stronger practice
- positive practice worth preserving
- uncertainty that should be monitored
- recommendation without an immediate requirement

Required response:

- consider for future planning
- record when it adds meaningful context
- do not present it as a confirmed defect

Default review effect:

- Approved
- Approved with observations

## Determining Severity

Reviewers should evaluate both impact and likelihood.

### Impact

Impact describes the consequence if the issue occurs.

| Level | Description |
|---|---|
| 1 — Negligible | Little or no measurable effect |
| 2 — Limited | Localized disruption or small quality reduction |
| 3 — Moderate | Noticeable operational, financial, compliance, or trust impact |
| 4 — Significant | Serious harm to important objectives or stakeholders |
| 5 — Severe | Catastrophic, irreversible, unlawful, or mission-threatening consequence |

### Likelihood

Likelihood describes the probability that the issue will occur or already exists.

| Level | Description |
|---|---|
| 1 — Rare | Highly unlikely under expected conditions |
| 2 — Unlikely | Possible, but not expected |
| 3 — Plausible | Could reasonably occur |
| 4 — Likely | Expected to occur in relevant conditions |
| 5 — Almost certain | Already occurring or expected repeatedly |

## Indicative Risk Matrix

The matrix is a decision aid, not a substitute for professional judgment.

| Impact × Likelihood | Indicative classification |
|---|---|
| 1–3 | Observation or Minor |
| 4–7 | Minor |
| 8–14 | Major |
| 15–25 | Critical |

A reviewer may raise or lower the indicative classification when justified by factors such as:

- legal or regulatory obligations
- safety implications
- vulnerable affected groups
- systemic or cascading effects
- detectability
- reversibility
- time sensitivity
- strong compensating controls
- low confidence or incomplete evidence

Any adjustment must be explained in the finding rationale.

## Classification Rules

1. Classify the risk of the finding, not the effort required to fix it.
2. Do not reduce severity merely because remediation is difficult or expensive.
3. Do not increase severity merely because a reviewer strongly prefers a different design.
4. Separate confirmed facts from assumptions and forecasts.
5. State when severity is provisional because evidence is incomplete.
6. Use the highest applicable severity when one finding creates several linked risks.
7. Split findings when separate issues require different owners, evidence, or classifications.
8. Reassess severity after remediation or when material new evidence becomes available.

## Mandatory Finding Fields

Every Critical, Major, or Minor finding must include:

- finding identifier
- title
- severity
- affected scope
- condition observed
- expected condition or requirement
- evidence
- impact assessment
- likelihood assessment
- rationale for classification
- recommended action
- accountable owner, when known
- target date, when applicable
- status

Observations should include enough context to distinguish them from confirmed defects.

## Escalation

Critical findings must be communicated immediately to the responsible decision-maker or governance role.

Major findings must be included prominently in the review summary and tracked to resolution or formal risk acceptance.

A reviewer must escalate any situation where:

- the responsible owner disputes a Critical classification without evidence
- material risk is being concealed or understated
- legal, ethical, safety, or security obligations may be breached
- review independence is compromised
- an unresolved finding is being omitted from the final decision record

## Risk Acceptance

Risk acceptance does not remove or downgrade a finding.

An accepted risk record should identify:

- the original finding and severity
- the accountable risk owner
- the decision and rationale
- compensating controls
- acceptance period or review date
- conditions that trigger reassessment

Critical risk acceptance requires explicit governance approval.

## Examples

### Example: Critical

A published operational procedure directs users to disable a mandatory safety control, creating a credible risk of severe harm.

### Example: Major

A decision model relies on an undocumented data source whose accuracy materially affects the recommendation, and no independent validation has been performed.

### Example: Minor

A procedure contains inconsistent terminology, but the intended action remains clear and operationally safe.

### Example: Observation

A review identifies an opportunity to automate an existing manual evidence check in a future release.

## Review Outcome Relationship

Severity informs, but does not automatically determine, the final review outcome.

As a general rule:

- unresolved Critical findings prevent approval
- unresolved Major findings normally require changes before approval
- Minor findings may be accepted with tracked actions
- Observations do not block approval

The reviewer must document any justified exception.

## Maintenance

This standard should be reviewed when:

- repeated classification disagreements occur
- new legal, safety, security, or governance requirements emerge
- the framework expands into materially different risk domains
- review retrospectives identify inconsistent application

Changes to this standard must preserve backward traceability for existing review records.
