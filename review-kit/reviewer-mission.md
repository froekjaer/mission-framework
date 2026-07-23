# Reviewer Mission

## Purpose

The reviewer mission defines how a Mission Framework component is assessed before it is accepted, released, or used as a dependency by other components.

The objective is not to reward complexity or style. The objective is to determine whether the component is clear, justified, usable, and sufficiently supported by evidence.

## Reviewer Responsibility

A reviewer SHALL:

1. Evaluate the submitted component independently.
2. Separate verified facts from assumptions and opinions.
3. Identify material risks, omissions, and contradictions.
4. Confirm that claims are traceable to appropriate evidence.
5. Assess whether the component can be implemented or applied as written.
6. Record findings in a reproducible form.
7. Avoid approving work that has not been reviewed in substance.

The reviewer is accountable for the quality of the review, not for the authorship of the component.

## Review Principles

### Evidence before opinion

Findings SHALL be based on observable content, documented requirements, test results, references, or explicit reasoning.

### Clarity before complexity

A simpler component that is understandable and usable is preferable to a sophisticated component that cannot be interpreted consistently.

### Materiality

Review effort SHALL focus first on issues that could cause incorrect decisions, unsafe implementation, invalid conclusions, loss of traceability, or failure of the component's stated purpose.

### Independence

The reviewer SHALL challenge unsupported assumptions, including assumptions introduced by the author, previous reviewers, or AI systems.

### Reproducibility

Another competent reviewer SHOULD be able to understand how each material finding was reached.

## Required Review Questions

The reviewer SHALL determine:

1. What is the component intended to achieve?
2. Is the scope explicit and internally consistent?
3. Are normative requirements distinguishable from guidance?
4. Are important terms defined or referenced?
5. Are claims supported by suitable evidence?
6. Are dependencies, assumptions, and limitations visible?
7. Can the component be applied without undocumented knowledge?
8. Are risks and failure modes addressed proportionately?
9. Does the component conflict with existing Mission Framework material?
10. Is the proposed review status justified?

## Finding Classification

Each finding SHALL use one of the following classifications.

### Critical

A defect that makes the component unsafe, fundamentally invalid, misleading, or unusable for its intended purpose.

Critical findings block approval.

### Major

A substantial defect that could produce incorrect implementation, inconsistent interpretation, weak assurance, or material loss of traceability.

Major findings normally block approval until resolved or explicitly accepted by an authorized maintainer.

### Minor

A limited defect that reduces clarity, precision, consistency, or maintainability without invalidating the component's main purpose.

Minor findings SHOULD be corrected but do not automatically block approval.

### Observation

A non-blocking improvement, question, or future consideration that may strengthen the component.

Observations SHALL NOT be presented as mandatory corrections unless they are reclassified.

## Evidence Requirements

For every Critical or Major finding, the reviewer SHALL include:

- the affected section or requirement;
- a concise description of the defect;
- the evidence or reasoning supporting the finding;
- the likely consequence if unresolved;
- the minimum condition required for closure.

Minor findings and observations SHOULD include the same information where practical.

## Review Outcome

The reviewer SHALL assign one outcome:

### Approved

No unresolved Critical or Major findings remain, and the component is suitable for its stated use.

### Approved with minor changes

No unresolved Critical or Major findings remain, but identified Minor findings should be corrected before or shortly after integration.

### Changes required

One or more unresolved Major findings remain, or the evidence is insufficient to support approval.

### Rejected

The component contains a fundamental defect, falls outside the project scope, or cannot be made acceptable without substantial redesign.

## Human and AI-Assisted Review

AI systems MAY assist with consistency checks, comparison, summarization, test generation, and identification of possible omissions.

AI-generated findings SHALL be treated as unverified until supported by inspectable evidence or validated reasoning.

An accountable human maintainer SHALL make the final approval decision for normative releases unless the project governance explicitly defines another accountable authority.

## Standard Review Record

A completed review SHALL contain:

- component name and version or commit reference;
- reviewer identity or review agent identifier;
- review date;
- scope of review;
- evidence examined;
- findings with classifications;
- unresolved questions;
- review outcome;
- conditions for approval, where applicable.

## Completion Rule

A review is complete only when its conclusion is traceable to the evidence examined and all blocking findings have an explicit disposition.
