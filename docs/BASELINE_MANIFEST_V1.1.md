# Foundation v1.1 Baseline Manifest

**Status:** Release candidate manifest  
**Purpose:** Identify the repository state and evidence corpus used to prepare Foundation v1.1.

## Reviewed baseline

The independent baseline review recorded the following repository commits:

| Repository | Reviewed commit | Role |
|---|---:|---|
| `froekjaer/mission-framework` | `e9644ba` | Canonical semantics |
| `froekjaer/Mission-Platform` | `48e1cfc` | Platform proposition |
| `froekjaer/mission-solar-eclipse` | `43dcc5d` | First reference mission |
| `froekjaer/collaborative-intelligence` | `4ed96fc` | Programme and review archive |
| `froekjaer/-Publication-Pipeline` | `5b616ee` | Publication transformation |

These commits describe the baseline reviewed by Claude, Codex and Mistral/Vibe Code as recorded in their metadata. Any reviewer-specific deviation shall remain visible in the archived metadata.

## Review corpus

The permanent review corpus is held in `froekjaer/collaborative-intelligence` and consists of original, unmodified reviewer artefacts:

```text
Review/<Reviewer>/Executive_Summary.md
Review/<Reviewer>/Findings.md
Review/<Reviewer>/Recommendations.md
Review/<Reviewer>/Metadata.md
```

The synthesis is held separately under:

```text
Analysis/Baseline-v0.1/
```

Original reviews are evidence. The synthesis is derived analysis and does not replace them.

## Foundation v1.1 change set

Foundation v1.1 adds or updates the following release-controlled material:

- `docs/FOUNDATION_V1.1_VALIDATION_UPDATE.md`
- `docs/VALIDATION_AND_SCIENTIFIC_METHOD.md`
- `docs/EXISTENCE_AND_VALUE_TEST.md`
- `docs/FRAMEWORK_STABILISATION_CRITERIA.md`
- `docs/BASELINE_MANIFEST_V1.1.md`
- `docs/CONFORMANCE_ROADMAP_V1.1.md`
- `docs/FOUNDATION_V1.1_RELEASE_PLAN.md`
- `README.md`

## Reproducibility rule

A release or validation result shall identify exact repository commits or immutable tags. Branch names alone are insufficient because they may move.

Generated publications shall identify the reviewed source commit and Publication Pipeline version used to create them.

## Manifest completion

Before Foundation v1.1 is tagged, this document shall be updated with:

- the final Mission Framework commit
- the final Collaborative Intelligence review-archive commit
- the final synthesis commit
- the first validation-plan commit in Mission Solar Eclipse
- the Publication Pipeline commit used for release artefacts

Unresolved entries shall be marked `PENDING`; they shall not be guessed.