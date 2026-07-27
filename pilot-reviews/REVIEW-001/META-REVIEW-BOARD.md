# REVIEW-001 Meta-Review Board

## Purpose

This board is the working surface for the REVIEW-001 meta-review described in [`META-REVIEW.md`](META-REVIEW.md). It holds two working tables: a **submission status tracker** (one row per reviewer) and an **architecture comparison matrix** (one row per comparison dimension, one column per reviewer).

It exists so that the meta-review is a structured, uniform process — not a subjective "what do I like best?" review. It operationalises the principle in [`META-REVIEW.md`](META-REVIEW.md): *not a popularity vote*.

Normative words follow the [`terminology-standard`](../../review-kit/terminology-standard.md).

---

## Table 1 — Submission Status

**Population rule:** populate only verified information. Do **not** infer missing data. If a field cannot be verified, write `unverified` and leave the decision to the Mission Owner. A blank row means the submission has not yet been frozen.

| Reviewer | Status | Freeze commit | Freeze date | Immutable reference preserved | Workspace boundary preserved | Independence declaration | Bias declaration | Tests/evidence status | Ready for Meta Review | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| ChatGPT | | | | | | | | | | |
| Claude | | | | | | | | | | |
| Gemini | | | | | | | | | | |
| Codex | | | | | | | | | | |
| Z.ai | | | | | | | | | | |
| Human | | | | | | | | | | |

### Field definitions

- **Status** — `not started` / `in progress` / `frozen` / `withdrawn`.
- **Freeze commit** — the exact commit SHA on the reviewer's branch at freeze.
- **Freeze date** — ISO 8601 date of the freeze commit.
- **Immutable reference preserved** — `yes` if `froekjaer/timelapse-pro` HEAD is unchanged at `eed9e3c8c67369e1924c25a11908616220c3c753` after the submission. `no` is a blocking governance finding.
- **Workspace boundary preserved** — `yes` if the reviewer wrote only inside their assigned workspace (`review-lab/REVIEW-001/<reviewer>/`).
- **Independence declaration** — `yes` if the reviewer declared they did not inspect another reviewer's branch.
- **Bias declaration** — `disclosed` if the reviewer disclosed any conflict of interest (e.g. authoring shared governance). Otherwise `none declared`.
- **Tests/evidence status** — `passing` / `failing` / `not applicable` / `unverified`.
- **Ready for Meta Review** — `yes` only when all gate items in [`SUBMISSION-CHECKLIST.md`](SUBMISSION-CHECKLIST.md) are satisfied or a Mission Owner exception is recorded.
- **Notes** — free text for caveats, exceptions, or observations. Keep factual.

---

## Table 2 — Architecture Comparison Matrix

**Population rule:** leave reviewer cells **empty** until the Meta Review begins. The Meta Review populates these from each frozen submission, not from anticipation. When two reviewers independently converge on the same answer, that convergence is recorded as evidence (see [`META-REVIEW.md`](META-REVIEW.md) § Shared component selection).

The comparison dimensions below are the **minimum** set. The Meta Review MAY add dimensions; it SHALL NOT remove these without a recorded rationale.

| Dimension | ChatGPT | Claude | Gemini | Codex | Z.ai | Human |
|---|---|---|---|---|---|---|
| Architectural thesis | | | | | | |
| Platform/payload boundary | | | | | | |
| Payload contract | | | | | | |
| Isolation model | | | | | | |
| Deployment model | | | | | | |
| Event or messaging model | | | | | | |
| Database strategy | | | | | | |
| Security model | | | | | | |
| Observability | | | | | | |
| Migration strategy | | | | | | |
| Extensibility proof | | | | | | |
| Project risk analysis | | | | | | |
| Cyber/regulatory risk analysis | | | | | | |
| Production blockers | | | | | | |
| Unique contribution | | | | | | |

### Dimension guidance

- **Architectural thesis** — the one-paragraph hypothesis the submission argues for (e.g. "the architecture is good; the code has not caught up").
- **Platform/payload boundary** — how the submission separates reusable core from functional payload.
- **Payload contract** — the mechanism coupling platform to payload (versioned interface, manifest, plugin, etc.).
- **Isolation model** — how payloads are isolated from each other and the platform (process, container, in-process, etc.).
- **Deployment model** — edge/headend topology, environment separation.
- **Event or messaging model** — synchronous/async, event bus, MQTT, etc.
- **Database strategy** — storage choice(s) and multi-tenancy approach.
- **Security model** — trust zones, RBAC, fail-closed posture.
- **Observability** — telemetry, SIEM, audit spine.
- **Migration strategy** — how the existing system is carried forward (additive, big-bang, strangler-fig).
- **Extensibility proof** — whether and how the submission proves a second payload can be added.
- **Project risk analysis** — see [`reviews/MIAR/RISK-METHOD.md`](../../reviews/MIAR/RISK-METHOD.md) §2.
- **Cyber/regulatory risk analysis** — see [`reviews/MIAR/RISK-METHOD.md`](../../reviews/MIAR/RISK-METHOD.md) §3 and the [`regulatory-horizon`](../../review-kit/regulatory-horizon.md).
- **Production blockers** — inherited blockers the submission explicitly does not solve.
- **Unique contribution** — the single strongest idea unique to this submission.

---

## How to use this board

1. As submissions freeze, populate Table 1 only with verified data.
2. When all intended submissions are frozen (or the Mission Owner declares the window closed), begin Meta Review by populating Table 2 from the frozen evidence.
3. For each dimension, look first for **convergence** (multiple reviewers reaching the same answer independently — strong evidence) and then for **divergence** (where reasoning differs — the most valuable input for the synthesis).
4. Record dissent and rejected alternatives in the synthesis, not erased.

## Fairness safeguard (REVIEW-001)

This board SHALL NOT be used to retroactively mark a frozen submission non-compliant for an omission that the original REVIEW-001 invitation did not require. See the fairness notice in [`META-REVIEW.md`](META-REVIEW.md) § Risk perspectives and [`SUBMISSION-CHECKLIST.md`](SUBMISSION-CHECKLIST.md) § Risk perspectives.
