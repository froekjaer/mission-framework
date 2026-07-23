# Mission Framework Review Template

## Purpose

Use this template to produce a consistent, traceable review of a Mission Framework component.

A review SHALL be evidence-based, proportionate to risk, and understandable to a reader who did not participate in the review.

## Review metadata

- **Review ID:**
- **Component:**
- **Version or commit:**
- **Owner or author:**
- **Reviewer:**
- **Review date:**
- **Review level:** Editorial / Technical / Independent assurance
- **Review type:** Human / AI-assisted / Combined
- **Scope:**
- **Out of scope:**
- **Related issue or pull request:**
- **Applicable standards or criteria:**

## Executive summary

Summarize the component, review approach, most important findings, overall risk, and recommended decision.

## Component purpose and context

Describe:

- the intended purpose;
- target audience;
- expected use;
- dependencies;
- relevant constraints;
- why the review is required.

## Review criteria

Evaluate the component against the following criteria:

1. Purpose and scope are clear.
2. Requirements are internally consistent.
3. Claims are supported by evidence where required.
4. Risks, assumptions, and limitations are explicit.
5. Terminology is used consistently.
6. The component is practical and implementable.
7. Dependencies and traceability are documented.
8. Human accountability is preserved when AI is used.
9. Applicable legal, ethical, security, privacy, safety, and operational concerns are addressed.
10. The component is suitable for its intended reuse or release.

Add component-specific criteria where needed.

## Review approach

Describe the methods used, such as:

- document inspection;
- source verification;
- requirements tracing;
- consistency analysis;
- technical testing;
- implementation walkthrough;
- threat or risk analysis;
- comparison with authoritative standards;
- AI-assisted analysis followed by human verification.

## Evidence register

| Evidence ID | Source or artifact | Version/date | Relevance | Reliability | Location or reference |
|---|---|---|---|---|---|
| E-001 |  |  |  |  |  |

## Findings summary

| Finding ID | Title | Severity | Status | Owner | Target disposition |
|---|---|---|---|---|---|
| F-001 |  |  | Open |  |  |

## Detailed findings

### F-001 — Finding title

- **Severity:** Critical / Major / Minor / Observation
- **Status:** Open / Accepted / Remediated / Verified / Deferred / Rejected
- **Affected location:**
- **Criterion or expected condition:**
- **Observed condition:**
- **Evidence:**
- **Impact:**
- **Likelihood:**
- **Severity rationale:**
- **Confidence:** High / Medium / Low
- **Recommendation:**
- **Owner response:**
- **Planned action:**
- **Target date:**
- **Verification:**
- **Residual risk:**

Repeat this section for each finding.

## Assumptions and limitations

Record assumptions, unavailable evidence, excluded areas, time constraints, tool limitations, reviewer competence boundaries, and unresolved uncertainty.

## Positive observations

Record material strengths that support the conclusion. Do not use positive observations to offset unresolved blocking findings.

## Risk assessment

Summarize:

- principal risks;
- affected stakeholders or assets;
- likelihood and impact;
- existing controls;
- residual risk;
- uncertainty;
- whether risk is acceptable for the intended use.

## Recommendations

Prioritize recommended actions:

1. Immediate or blocking actions.
2. Actions required before release or approval.
3. Planned improvements.
4. Optional enhancements.

## Reviewer recommendation

Select one:

- [ ] Approve
- [ ] Approve with conditions
- [ ] Changes required
- [ ] Reject
- [ ] Unable to conclude

### Recommendation rationale

Explain how the evidence and findings support the recommendation.

### Conditions

List any conditions, owners, deadlines, and required verification.

## Decision

- **Decision:** Approved / Approved with conditions / Changes required / Rejected / Deferred
- **Decision-maker:**
- **Decision date:**
- **Accepted residual risk:**
- **Conditions:**
- **Rationale:**

## Remediation verification

| Finding ID | Remediation reference | Verified by | Verification date | Result |
|---|---|---|---|---|
| F-001 |  |  |  |  |

## Traceability

- **Reviewed component commit or immutable version:**
- **Review record location:**
- **Evidence locations:**
- **Related decisions:**
- **Related remediation commits or pull requests:**
- **Supersedes:**
- **Superseded by:**

## Sign-off

### Reviewer

- **Name:**
- **Date:**
- **Statement:** I confirm that this review record accurately represents the scope, evidence, findings, uncertainty, and recommendation.

### Decision-maker

- **Name:**
- **Date:**
- **Statement:** I accept responsibility for the recorded decision, conditions, and residual risk.

## Completion checklist

- [ ] Exact component version identified.
- [ ] Scope and exclusions recorded.
- [ ] Criteria and approach documented.
- [ ] Evidence is traceable.
- [ ] Findings use the severity standard.
- [ ] Blocking findings are resolved or formally accepted.
- [ ] Remediation has been verified where required.
- [ ] Recommendation and decision are recorded separately.
- [ ] Residual risk and conditions are explicit.
- [ ] Human accountability is identifiable.

A review is complete only when every applicable item is satisfied or an explicit, approved exception is recorded.
