# Reviewer Mission

## Purpose

The reviewer mission defines how a Mission Framework component is assessed before it is accepted, released, or used as a dependency by other components.

The objective is not to reward complexity or style. The objective is to determine whether the component is clear, justified, usable, and sufficiently supported by evidence.

## Reviewer responsibility

A reviewer SHALL:

1. Evaluate the submitted component independently.
2. Separate verified facts from assumptions, inferences, and opinions.
3. Identify material risks, omissions, and contradictions.
4. Confirm that claims are traceable to appropriate evidence.
5. Assess whether the component can be implemented or applied as written.
6. Record findings in a reproducible form.
7. Avoid approving work that has not been reviewed in substance.
8. Disclose conflicts of interest and competence limitations.
9. Protect confidential, personal, and security-sensitive information.

The reviewer is accountable for the quality of the review, not for the authorship of the component.

## Review principles

### Evidence before opinion

Findings SHALL be based on observable content, documented requirements, test results, references, or explicit reasoning.

### Clarity before complexity

A reviewer SHALL prefer understandable, testable, and maintainable content over unnecessary abstraction. Complexity must be justified by the problem it solves.

### Risk before cosmetics

Material correctness, safety, security, legality, and mission viability take priority over stylistic preferences.

### Proportionality

Review depth SHALL reflect potential impact, uncertainty, novelty, exposure, and reversibility.

### Traceability

A competent third party should be able to understand what was reviewed, which evidence was used, what was found, and why the decision followed.

### Constructive independence

The reviewer SHALL challenge content honestly without becoming adversarial. The objective is to improve decision quality, not to defend or defeat the author.

## Mandatory review questions

The reviewer SHALL determine:

1. Is the purpose explicit and appropriate?
2. Is the scope clear, including exclusions?
3. Are requirements, guidance, and examples distinguishable?
4. Are terms defined and used consistently?
5. Are claims supported by suitable evidence?
6. Are assumptions and limitations visible?
7. Are dependencies and interfaces identified?
8. Is the content internally consistent?
9. Can the intended audience apply it as written?
10. Are material legal, ethical, safety, security, privacy, and operational risks addressed?
11. Is AI use disclosed and human accountability preserved where relevant?
12. Is the proposed decision justified by the evidence and findings?

## Finding severity

Findings SHALL use the shared severity classification:

- **Critical** — immediate or potentially catastrophic risk; approval blocked.
- **Major** — significant weakness that normally blocks approval.
- **Minor** — limited weakness that should be corrected or scheduled.
- **Observation** — non-blocking improvement opportunity or useful note.

Severity SHALL reflect risk and evidence, not tone or reviewer preference.

## Evidence requirements

A finding SHALL identify:

- the observed condition;
- the expected condition or review criterion;
- the affected location;
- supporting evidence;
- impact and severity rationale;
- recommended action.

Where evidence is incomplete, the reviewer SHALL state the uncertainty and avoid presenting inference as verified fact.

## Review outcomes

The reviewer SHALL recommend one of:

- **Approve**
- **Approve with conditions**
- **Changes required**
- **Reject**
- **Unable to conclude**

The recommendation SHALL follow from the recorded findings. Critical findings require `Changes required` or `Reject`. Major findings normally require `Changes required` unless explicitly accepted by an authorized decision-maker.

## AI-assisted review

AI MAY be used to:

- compare documents;
- identify inconsistencies and omissions;
- summarize evidence;
- propose tests and review questions;
- draft findings.

The reviewer SHALL independently verify material AI output. AI SHALL NOT be the accountable approver, and fabricated or unverifiable citations SHALL be rejected.

## Reviewer conduct

A reviewer SHALL:

- be specific and respectful;
- criticize the content rather than the person;
- avoid hidden criteria;
- acknowledge uncertainty;
- correct errors in the review record;
- avoid using confidential information beyond the authorized scope.

## Review record

The final review record SHALL include:

- component and exact version or commit;
- reviewer and review date;
- scope and exclusions;
- review level and criteria;
- evidence considered;
- findings and severity;
- owner responses and remediation;
- recommendation;
- final decision, decision-maker, and residual risk.

## Completion rule

The reviewer mission is complete only when the review is sufficiently documented for another competent person to reproduce the reasoning and understand the resulting decision.
