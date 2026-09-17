# Architecture Principles — Candidate Backlog

**Status:** Backlog — candidates only. **Not approved.**
**Purpose:** Record candidate architecture principles surfaced during REVIEW-001 so they are not lost, without silently approving a final principles standard.

These principles emerged from REVIEW-001 work (including the gap review of the framework's own governance). They are recorded here as **candidates requiring separate governance review and approval** before they become normative Mission Framework standards. None of them is in force as a result of being listed here.

A principle is promoted from this backlog to a normative standard only through the Mission Framework decision process (an ADR or an equivalent governance decision), with rationale, alternatives considered, and Mission Owner acceptance recorded.

---

## Candidate principles

1. **Mission before technology.** Technology is the means; the mission is the end. A technology choice is justified only by the mission value it creates.

2. **Business before architecture.** Architecture follows business need, not the other way around. Every architectural layer traces to a business attribute or stakeholder need.

3. **Evidence before opinion.** Claims SHALL be supported by evidence. The burden of proof lies with the claimant. Absence of evidence is not evidence of absence.

4. **Why, because, for whom.** Every material decision preserves a traceable answer to *why* it serves the mission, *because* of what evidence or constraint, and *for whom* the capability is delivered.

5. **Payloads before products.** The functional mission capability is a swappable payload, not the boundary of the platform. The first payload does not define the platform forever.

6. **Replaceable components.** No component is load-bearing in a way that makes it irreplaceable. Contracts and boundaries make replacement possible, even if not always exercised.

7. **Loose coupling.** Platform and payload, control plane and data plane, are coupled only through versioned contracts. Tight coupling is a debt to be paid down, not a feature.

8. **Observable by design.** Every component emits standardised telemetry and audit. If it cannot be observed, it cannot be trusted in production.

9. **Security by design.** Least privilege, fail-closed, defence in depth, and signed artifacts are default. Security is not added later.

10. **Sovereignty by design.** Data ownership, classification, retention, and jurisdiction stay with the mission and the customer. The platform enables sovereignty; it does not absorb it.

11. **Proportionate capability and intelligence.** Capability and AI are delivered proportionate to need, consequence, cost, sovereignty, and accountability — not maximised for their own sake.

---

## Governance notes

- Listing a principle here does **not** make it a standard. It makes it visible so it can be debated, refined, accepted, modified, or rejected through proper governance.
- Some candidates overlap (e.g. "Mission before technology" and "Business before architecture"). The eventual standard MAY merge or restructure them.
- Each promotion SHOULD record: the principle's origin (which review surfaced it), alternatives considered, and examples of how it would bind.
- A principle that is accepted SHALL be moved out of this backlog into the normative standards location and referenced from `DECISION_PRINCIPLES.md` or equivalent.

## Origin

These candidates were distilled from the REVIEW-001 body of work — the invitation's three mandatory questions, the SABSA business attributes, the accepted TimeLapse Pro ADRs (especially ADR-001), and the gap review of Mission Framework governance. They are not new inventions; they are the principles the work already assumes, made explicit so they can be governed rather than implied.
