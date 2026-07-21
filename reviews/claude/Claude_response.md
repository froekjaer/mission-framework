[CLAUDE-RESPONSE.md](https://github.com/user-attachments/files/30207556/CLAUDE-RESPONSE.md)
# Claude Conceptual Review

## Reviewer

- System/version: Claude (Anthropic), Claude Fable 5, operating in Cowork mode
- Review date: 2026-07-21
- Repositories and revisions reviewed:
  - `froekjaer/mission-framework` @ `9b78a23` (main) — all Markdown documents
  - `froekjaer/Mission-Platform` @ `48e1cfc` (main) — all Markdown documents
  - `froekjaer/mission-solar-eclipse` @ `dd53137` (main) — all content (README, reviews)
- Important limitations:
  - This is a conceptual, semantic and editorial review as requested in `reviews/claude/INVITATION.md`. It is not an implementation or security review.
  - I reviewed only the repository contents at the revisions above. I had no access to the project conversation, the Manifesto or the Constitution referenced in `HISTORY.md` (they do not exist in the repositories).
  - I am an AI system. Per the framework's own principles, treat this review as evidence, not authority. Findings should be independently checked before acting on them.

## Executive assessment

**Clearest strength.** The evidence layer is unusually disciplined. `docs/EVIDENCE_MODEL.md` and `docs/REALITY_MODEL.md` are the best documents in the project: they make the reality gap explicit, treat negative and contradictory evidence as first-class, separate confidence from truth, and repeatedly warn against exactly the epistemic mistakes ("a database with reality… evidence with truth… confidence with correctness") that most architecture frameworks make silently. The project is also admirably self-aware: Principle 15 ("Reported progress is itself a claim and therefore requires evidence") is a rule most projects would not dare adopt.

**Deepest conceptual weakness.** The framework's central terms are held together by cascading near-synonyms rather than stable definitions. *Trust* is defined through *justified confidence*, which is defined through *sufficient evidence*, whose sufficiency is assessed through *trust thresholds* — a circle. *Need*, *genuine*, *value*, *material*, *consequential*, *sufficient* and *justified* carry most of the normative weight in the project and none of them is defined. The canonical process loop — the framework's spine — appears in at least seven non-identical versions across the two repositories, with stages (Information, Understanding, Intelligence, Reasoning, Claim, Outcome, Architecture) appearing and disappearing without explanation.

**Most important clarification required.** Decide, per concept, which document is canonical, and make everything else a reference to it. Concretely: publish a single glossary and a single canonical Mission Loop in `mission-framework`, restate nothing, and link everything. Until that exists, the three repositories cannot be shown to "express the same underlying model," because there is no single stated model to compare them against. Two urgent instances: (1) the Mission Core admission rule quoted in all four review invitations exists **only** in the invitations — it appears in no canonical document; (2) `docs/architecture/mission-reference-model.md` defines a Decision as made by "an authorised actor **or mechanism**," which quietly contradicts "AI proposes. Humans decide."

## Textual observations

These are observations about wording and text, prior to interpretation.

### T1. The canonical loop exists in at least seven non-identical versions

- `README.md` (framework), "The Mission Cycle": Reality → Need → Mission → **Architecture** → Capability → **Operation** → Observation → Evidence → Knowledge → **Understanding** → Decision → **Improvement** → Reality. (Identical in `docs/PURPOSE_VALUES_PHILOSOPHY.md`.)
- `docs/PRINCIPIA_MISSIONIS.md`, Principle 13, "The Mission Loop": Reality → Need → Mission → Observation → Evidence → Knowledge → Decision → Action → **Outcome** → **Learning** → Reality. (No Architecture, Capability, Understanding.)
- `docs/MISSION_THEORY.md`, "The Mission Loop": Mission → Operational Reality → Physical Reality → Observation → Evidence → Knowledge → **Reasoning** → Decision → Mission. (Starts at Mission; introduces Reasoning; no Need, Action, Learning.)
- `docs/ARCHITECTURE.md`, "Architectural flow": Reality → Observation → Evidence → Knowledge → Reasoning → Decision → Action → Outcome → Learning.
- `docs/COMPUTATIONAL_TRUST_ENGINEERING.md`, "The mission equation": Reality → Observation → Evidence → Knowledge → **Understanding** → Decision → Action → Outcome → Learning. (Reasoning replaced by Understanding.)
- `MISSION_INTELLIGENCE.md`, "Lifecycle": Observation → **Information** → Knowledge → Understanding → **Intelligence** → Decision → Action → Learning. (Information and Intelligence appear nowhere else; Evidence is absent from the diagram.)
- `docs/EVIDENCE_MODEL.md`: Reality → Observation → Evidence → **Claim** → Knowledge → Decision. (Claim appears as a stage only here.)
- `Mission-Platform/docs/principles/reality-principle.md`, "The continuous loop": Reality ⇅ Mission ⇅ Objectives ⇅ Capabilities ⇅ Services ⇅ Components ⇅ Infrastructure ⇅ Operations ⇅ Evidence ⇅ Reality.

Each version is individually reasonable. Collectively they leave the reader — and any machine agent — unable to answer basic questions: Is Understanding a stage or not? Is Reasoning distinct from Understanding? Where do Claims live? Is Evidence part of the intelligence lifecycle? If these are deliberate *views* of one underlying model at different zoom levels, no document says so and no mapping exists.

### T2. The Mission Core admission rule is not in the repository

The rule — "A concept belongs in Mission Core only when it is indispensable across domains and cannot be represented adequately through a domain extension" — is quoted in all four review invitations (`reviews/*/INVITATION.md`) as "the current working rule," but it appears in no canonical document in either `mission-framework` or `Mission-Platform`. A rule that governs the most important boundary in the architecture currently lives only in letters to reviewers. This is the clearest instance of text depending on hidden context.

### T3. `HISTORY.md` records the adoption of documents that do not exist

`HISTORY.md` states "Manifesto published — The Manifesto established the values and aspirations…" and "Constitution adopted — The Constitution established the enduring principles and governance foundation…". Neither a Manifesto nor a Constitution exists in any of the three repositories. Under the project's own Principle 15 ("No person, system or AI shall claim progress… that cannot be independently demonstrated"), these entries are currently unverifiable claims. Either the documents were adopted elsewhere (then link them) or they are aspirational (then they do not belong in institutional memory yet).

Similarly, `HISTORY.md` states Mission Solar Eclipse "became an early mission **demonstrating** how Mission Framework can organize knowledge and action around a real-world objective." The `mission-solar-eclipse` repository contains a one-sentence README and a CI workflow. Nothing has yet been demonstrated. "Accepted as an early mission intended to demonstrate…" would be accurate.

### T4. `MISSION.md` reads as a document from an earlier stratum

`MISSION.md` describes "an open framework for planning, executing, documenting and preserving complex missions" with the motto "Build once. Reuse forever." It does not use the Reality/Evidence/Trust vocabulary that defines the rest of the repository, and its motto sits awkwardly beside Principle 11 ("no mission architecture is ever complete") and Project Principle 10 ("Everything Evolves"). A reader following the `00_START_HERE.md` reading order encounters this older voice second, before the current conceptual foundation. It should be revised or explicitly marked as historical.

### T5. Three overlapping principle sets with no mapping

The framework repo contains 11 Project Principles (`PROJECT_PRINCIPLES.md`) and 16 Principia (`docs/PRINCIPIA_MISSIONIS.md`, numbered 0–15); the Platform contains 12 Guiding Principles (`docs/principles/guiding-principles.md`). They overlap heavily but not exactly (e.g., "Everything Has an Owner" exists only in the Platform set; "Unknown is Better than Wrong" only in the Project set). No document states which set is canonical, how they relate, or why the Platform restates rather than references. Which is *the* first principle is also unclear: `PROJECT_PRINCIPLES.md` says "Trust is the primary architectural principle"; `guiding-principles.md` puts "Mission First" first; `README.md` says "Reality is the final authority."

### T6. Naming drift and near-collisions

- "Mission Eclipse" (`README.md`, `MISSION.md`) vs. "Mission Solar Eclipse" (`HISTORY.md`, the repository name, the invitations).
- "Reality Anchor Principle" (`docs/REALITY_MODEL.md`, Principle 5) vs. "The Reality Principle" / "Reality Traceability" (`Mission-Platform/docs/principles/reality-principle.md`). Both are attributed to the same Danish expression by Morten Thrane, but they are scoped differently — the framework version governs *claims, models and decisions*; the Platform version governs *architectural elements*. Are these one principle or two? No document says.
- "Mission Kernel" (`docs/ARCHITECTURE.md`: common runtime services) vs. "Mission Core" (`Mission-Platform/docs/architecture/overview.md`: the stable concept set). These are different things with confusably similar names.
- "Living Body of Knowledge" is capitalised as a proper noun in `FOUNDING.md`, `CULTURE.md`, `HISTORY.md` and `SUSTAINABILITY.md` but is defined only in passing ("something that can grow through evidence, experience, curiosity, collaboration, and stewardship").

### T7. Undefined load-bearing qualifiers

The following words carry decisive normative weight and are never defined: **genuine** (need), **material** (evidence, AI involvement, transformation), **consequential** (decision), **sufficient** (evidence), **justified** (trust, confidence), **credible** (evidence), **meaningful** (value, problem). Nearly every rule in the project is gated by one of them ("Material AI involvement should be visible"; "Humans remain accountable for consequential decisions"). Because the gate words are undefined, the rules are currently untestable. Note that `docs/ARCHITECTURE.md`'s policy engine ("evidence quality thresholds… human approval requirements") implicitly answers this — thresholds are mission policy, not framework constants — but no document says so explicitly.

### T8. Hedged normativity

Framework documents systematically hedge: "should… whenever possible," "where appropriate," "where practical" (e.g., `TRUST.md`: trust states "may" be used "where appropriate"; `docs/EVIDENCE_MODEL.md`: hash "where practical"). The Platform documents use "shall" far more consistently. The framework should decide which of its statements are requirements, defaults, or aspirations — otherwise conformance (which Codex is asked to test) has no target.

## Semantic analysis

### Reality

The strongest and most carefully guarded concept — with one significant internal tension.

`docs/REALITY_MODEL.md` largely avoids naïve realism: the reality gap is declared unclosable, observation is relativised to observer capability, "unknown does not mean false," and the engineering-consequences list explicitly forbids confusing "evidence with truth" and "consensus with fact."

The tension: slogans elsewhere personify reality as an *agent* that adjudicates — "Reality is the final authority" (`README.md`), "Reality has the final vote" (`CULTURE.md`), "Reality—not administration—is the ultimate authority" (Principle 10). But by the framework's own Reality Model, no one has access to reality except through observation and evidence — the fallible layer. Operationally, the "final authority" is always *current best evidence about reality*, which is revisable. The Reality Model knows this; the slogans don't. This matters practically: when two parties disagree, "reality decides" gives no procedure; "the party whose position survives the evidence-challenge procedure decides, pending further evidence" does. The Reality Principle should be explicitly restated as an *evidence-revision rule* (models must yield to credible contradicting evidence via a defined contradiction-handling procedure) rather than as direct arbitration by reality.

Also unresolved: `reviews/claude/INVITATION.md` itself asks how "uncertainty, incomplete observation and conflicting evidence should be handled." The Evidence Model preserves contradictions ("Contradictions are preserved, not averaged away") but no document supplies a decision rule for when contradiction *forces* model revision versus remaining open — especially under time pressure, when a decision cannot wait for resolution.

### Need and value

The weakest semantic area, and the one the whole edifice rests on.

*Need* is never defined. *Genuine need* does heavy gatekeeping ("Every meaningful mission exists because…"; "Begin with genuine need") with no criteria: Whose need? Recognised by whom? What distinguishes a genuine need from a manufactured, perceived, or conflicting one? What happens when the needs of two populations conflict — which mission is "genuine"?

*Value* is defined mostly negatively (`docs/PURPOSE_VALUES_PHILOSOPHY.md`: "Complexity is not value… Value exists only when a genuine need has been fulfilled"). This creates a closed pair: value = fulfilment of genuine need; a need's genuineness is, in practice, evidenced by whether fulfilling it created value. The circle is escapable — but only by defining "genuine" independently (see Recommended revisions, R6).

There is also a quiet cross-repo drift: the framework insists missions begin with *need*, while the Platform's Mission definition (`mission-reference-model.md`) widens the trigger to "a real-world need, **opportunity, obligation or condition**." That widening is probably correct (a legal obligation is not naturally a "need") — but then the framework's "We Begin with Need" story needs qualification, or "need" needs to be defined broadly enough to absorb obligation and opportunity.

### Mission and objective

*Mission* is used in three distinct senses without acknowledgment:

1. **A purpose** — "a meaningful purpose pursued in response to a real-world need…" (`mission-reference-model.md`).
2. **An undertaking/project** — Mission Solar Eclipse, "planning, executing, documenting and preserving complex missions" (`MISSION.md`).
3. **An organisational raison d'être** — "Every organisation exists to accomplish missions" (`docs/MISSION_THEORY.md`).

Sense 1 is a *reason*; sense 2 is a *bounded activity with lifecycle and participants*; sense 3 is a *standing function*. A schema will have to choose (does a Mission have a start and end date? Sense 2 says yes; sense 3 says no). This is precisely where a premature schema would freeze an ambiguity.

*Objective* is defined only in the Platform ("a defined outcome that contributes to a mission") and never appears in the framework's own loops — the framework's Mission Stack (`docs/MISSION_THEORY.md`) instead inserts an undefined stage, **Outcome**, between Mission and Capabilities. Outcome and Objective are presumably related (an Objective is a desired Outcome?) but no document says so.

*Mission Gravity* ("Capabilities form around missions. Processes form around capabilities…") is a metaphor presented as mechanism. As description it is falsified daily (technology frequently precedes and generates missions — the framework's own AI collaboration is an example); as a *design norm* ("components should be justified by missions") it is sound. The passage should be marked as normative, not observational.

### Capability, service and operation

*Capability* has the best definition in the project ("the ability to produce an outcome or effect under specified conditions") — operational and testable.

*Service* ("a defined means of delivering value or enabling a capability") is vague and overlaps both Capability and Workflow. In the Platform's chain (Mission ⇅ Objective ⇅ Capability ⇅ Service ⇅ Workflow or Component…) Service sits between Capability and Workflow, but nothing distinguishes "a means of enabling a capability" from "an organised progression of activities intended to produce an outcome" (Workflow). This boundary will not survive schema design as written.

*Operational Reality Layer* (`docs/MISSION_THEORY.md`) is defined as "everything directly required to deliver mission outcomes," followed by a list (people, knowledge, processes, technology, automation, facilities, energy, communications, suppliers, information, physical assets) that covers essentially everything an organisation contains. The only boundary word is "directly," which is undefined. A layer that contains everything distinguishes nothing. The concept becomes useful only when paired with a method for deciding what is *not* in a given mission's ORL.

*Operational Integrity* is declared "a **measurable** emergent property" — but no measurement, even sketched, is proposed anywhere. "Measurable" is currently an unsupported claim; under Principle 15 it should read "intended to become measurable" until a measurement exists.

*Dependency Descent* has an undefined stopping rule: "the descent continues until the organisation has reached the lowest material dependency **relevant to mission survival**." Both "material" and "relevant" are undefined, so the descent has no principled bottom (every mission transitively depends on the power grid, global shipping, and the sun).

### Evidence and trust

The most mature area; the problems here are of grounding, not construction.

**The central circularity.** `TRUST.md`: trust is "justified confidence that information… [is] supported by **sufficient evidence**…". Sufficiency of evidence is assessed against consequence via "trust thresholds" (`docs/COMPUTATIONAL_TRUST_ENGINEERING.md`: "set trust thresholds proportional to consequence"). And the evidence object itself carries a "trust assessment" in its required metadata (`docs/EVIDENCE_MODEL.md`). So: trust is defined by evidence sufficiency, sufficiency is defined by trust thresholds, and evidence carries trust assessments as input. The circle is closeable — by making *"justified"* the primitive and defining it procedurally (justification = surviving a defined challenge process before a defined authority, for a defined purpose) — but currently "justified" is the most-used and least-defined word in the project.

**Trust states conflate process and verdict.** The 0–5 ladder in `TRUST.md` mixes *verification events* (Observed, Verified, Corroborated — things that happened to the evidence) with *fitness judgements* (Trusted, Highly Trusted — decisions about use). An item can be Corroborated yet not fit for a given purpose, and (rarely) singly-Observed yet rightly relied on under time pressure. Two orthogonal dimensions — verification status and fitness-for-purpose — are compressed into one scale.

**Physics metaphors, unevenly hedged.** `docs/COMPUTATIONAL_TRUST_ENGINEERING.md` commendably flags the "trust field" as "an engineering hypothesis rather than established physical law." But trust *potential*, *momentum*, *inertia* and *debt* receive no such hedge, and they are equally metaphorical. Trust debt and trust inertia are the two with clearest operational content (both describe evidence staleness relative to reliance); potential and momentum add little beyond the field metaphor. One hedge, stated once for the whole metaphor family, would suffice.

**An unargued asymmetry.** "AI output is evidence, never fact by declaration" (`docs/EVIDENCE_MODEL.md`) — correct. But human evidence ("statements, observations, expert assessments and testimony") receives no equivalent warning, though testimony is among the most failure-prone evidence classes known. The asymmetry may be justified (accountability attaches to humans), but the *epistemic* treatment of human and AI evidence should be symmetrical even where the *accountability* treatment is not. Currently the documents read as if AI evidence is uniquely suspect.

### Decision and accountability

This is where the invitation asks the hardest question, and where the texts are least aligned.

The slogans are absolute: "AI proposes. Humans decide." (`README.md`); "Humans remain accountable for consequential decisions" (`PROJECT_PRINCIPLES.md`). But:

1. `Mission-Platform/docs/architecture/mission-reference-model.md` defines Decision as "a selection among alternatives made by an authorised actor **or mechanism**." "Mechanism" licenses automated decision-making inside the canonical concept set, directly against the slogans. Either the slogans need qualification or the definition needs the word removed.
2. `docs/ARCHITECTURE.md` widens the accountable party: "Consequential decisions remain attributable to accountable human **or organisational** authorities." An organisation is not a human; in distributed organisations, "the organisation is accountable" is frequently how *no individual* is accountable. This may be a deliberate concession to reality — but it contradicts "identifiable people" (`Mission-Platform/docs/book/mission-book.md`: "Responsibility must always remain with identifiable people or organisations" — which contains the same widening inside one sentence).
3. The Policy Engine (`docs/ARCHITECTURE.md`) "evaluates whether proposed operations are permitted, required or prohibited." An engine that determines that an operation is *required* is making decisions in every ordinary sense. The coherent reading — humans decide *policy*, mechanisms *execute* policy, and accountability flows through the policy's author and approver — is nowhere stated.
4. "Consequential" is undefined, and classifying a decision as consequential is itself a consequential act (a regress that must be cut by policy: e.g., "decisions are consequential by default unless a policy explicitly delegates them").

The framework's current position ("AI may recommend while humans remain accountable") is, as the invitation suspects, not yet sufficient for automation and delegation. What is missing is a concept of **delegated authority**: a human-accountable act of authorising a mechanism to act within bounds, itself recorded as a decision with an owner, scope, validity period and revocation condition. The Meta Model's relationship properties (owner, validity period, provenance) already contain everything needed to express this; the concept just has to be named.

A smaller point: the Meta Model's ownership roles ("accountable, responsible, consulted, informed…") are RACI in all but name; the borrowing should be acknowledged and the terms defined, since RACI's own ambiguity (accountable vs. responsible) is well documented.

## Circular or unstable definitions

1. **Trust ↔ evidence sufficiency ↔ trust thresholds ↔ trust assessment.** Files: `TRUST.md`, `docs/EVIDENCE_MODEL.md`, `docs/COMPUTATIONAL_TRUST_ENGINEERING.md`. Described above (Evidence and trust). Break the circle by defining *justified* procedurally.
2. **Need ↔ value ↔ mission.** Files: `PURPOSE.md`, `docs/PURPOSE_VALUES_PHILOSOPHY.md`, `README.md`. Value is fulfilment of genuine need; missions transform needs into value; genuineness has no independent criterion. Break by defining "genuine" via evidence from the affected population (see R6).
3. **Knowledge — three competing definitions.** (a) `docs/PRINCIPIA_MISSIONIS.md` P3: "Knowledge emerges when evidence is placed in context and survives scrutiny." (b) `MISSION_INTELLIGENCE.md`: "Knowledge emerges when information is connected, tested and placed within a useful model of the mission." (c) `docs/ARCHITECTURE.md`: "a structured and reviewable relationship between evidence, claims, context, time and uncertainty." (a) builds knowledge from evidence, (b) from information (a stage that exists only in this document), (c) makes it a relationship rather than a state. Pick one; make the others references.
4. **Evidence — boundary instability across repos.** `docs/EVIDENCE_MODEL.md` is strict: evidence = observation + mission context + "sufficient provenance, integrity and relevance." `mission-reference-model.md` is loose: "an observation, measurement, record or artefact used to evaluate a claim…" — the Platform's definition drops the provenance/integrity conditions that are the framework's whole point. Under the Platform definition, an unprovenanced rumour used to evaluate a claim is evidence; under the framework definition it is not.
5. **Understanding / Intelligence / Reasoning.** `MISSION_INTELLIGENCE.md` distinguishes Knowledge → Understanding → Intelligence, but Intelligence is defined as "knowledge and understanding shaped for a defined decision" — a packaging step, not a new epistemic level; meanwhile `docs/MISSION_THEORY.md` and `docs/ARCHITECTURE.md` use *Reasoning* where CTE uses *Understanding*. Three documents, three middle layers, no mapping.
6. **Mission — three senses** (purpose / undertaking / organisational function), described above.
7. **Mission Kernel vs. Mission Core** — not circular, but an unstable near-collision that will produce durable confusion if both names survive into implementation.

## Conceptual objections

Objections to internal coherence (not preferences):

**O1. The metaphysical/epistemic slide.** The project states a metaphysical axiom (Principle 0: reality exists independently) and then uses it as if it were an epistemic procedure ("reality is the final authority"). Internally incoherent as written, because the project's own Reality Model denies procedural access to reality except via evidence. Fix is cheap (see Reality section) and does not weaken the principle — it strengthens it against the "naïve realism" charge the invitation itself anticipates.

**O2. The single-question test cannot bear its load.** "Every component, workflow, AI interaction and architectural decision should be evaluated by one question: Does it increase or decrease justified trust?" (`README.md`, `TRUST.md`). Without a trust metric, decomposition rule, or comparison procedure, this question cannot actually be answered for real design alternatives (most alternatives increase some trust dimensions and decrease others — the project's own list of ten dimensions guarantees this). As a cultural prompt it is valuable; as "the architectural test" it is currently unfalsifiable. Either supply the procedure (evaluate per dimension, per stakeholder, against the mission's trust policy) or present it as orientation, not test.

**O3. Teleological overreach stated as observation.** "Everything exists because something must be accomplished" / "Every organisational component exists because a mission requires it" (`docs/MISSION_THEORY.md`). As empirical claims these are false — components routinely exist for historical, political and accidental reasons, which is precisely why the document's own "Organisational Fallacy" section is needed. The claims are good *norms* disguised as *facts*. The framework elsewhere insists on separating normative from descriptive claims; it should comply here.

**O4. The Mission Core admission rule is not operational.** Beyond not being in the repository (T2), the rule cannot be applied as written: "indispensable across domains" cannot be tested prospectively (indispensability is only demonstrated by failed attempts to do without), and "cannot be represented adequately through a domain extension" is almost never strictly true — with enough machinery, nearly anything can be pushed to an extension, which means the rule as written admits *nothing*. Under implementation pressure the rule will be quietly ignored (as the invitation fears). It needs a procedural form — e.g.: *a concept enters Mission Core when (a) at least N independent domain models have each been shown to require it, (b) an extension-based representation has been attempted and documented, and (c) the cost/distortion of the extension representation is recorded and judged unacceptable by an explicit decision (ADR).* That converts "indispensable" from an adjective into an evidence trail — which is exactly the project's own method.

**O5. Unverified self-claims.** `HISTORY.md`'s Manifesto/Constitution/Solar-Eclipse entries (T3) and Operational Integrity's "measurable" (Semantic analysis) violate Principle 15 within the project's own documents. This is worth fixing quickly, less because of the individual claims than because the framework's credibility rests on being seen to obey its own strictest rule.

Alternative-preference disclosures (not objections): the framework's epistemology is foundationalist (a one-directional chain from reality upward). A coherentist would build differently, but the chain is a legitimate design stance and I do not press it. Likewise, grounding the framework in mind-independent reality (Principle 0) is a defensible choice that merely deserves the qualification O1 describes.

## Cross-repository consistency

**Division of responsibility: mostly respected, with leakage.** The declared split (framework = canonical semantics; Platform = architecture/tooling; Solar Eclipse = validation) is real: the Platform does not contradict the framework so much as *restate* it with drift. Restatement is the problem — every restated definition is a fork waiting to happen. Specific drifts: Evidence (finding 4 above), Mission trigger ("need" vs. "need, opportunity, obligation or condition"), Decision ("or mechanism"), principle sets (T5), Reality principle naming (T6). The Platform also introduces canonical-feeling semantics that arguably belong in the framework: the fifteen MRM concept definitions are the closest thing to a glossary the project has, yet they live in the implementation repo. If mission-framework "owns canonical semantics," the concept definitions must live there.

**Emphasis tension.** `docs/MISSION_THEORY.md`: "Dependency before ownership… Ownership is important. Dependency is fundamental." Platform Guiding Principle 7: "Everything Has an Owner" (with no dependency counterpart in the list). Not a contradiction, but the two repos would triage the same modelling effort differently.

**mission-solar-eclipse cannot yet participate in consistency checking.** It contains one sentence of content. Nothing can be validated against it; it neither confirms nor contradicts the model. Its current function is aspirational, and `HISTORY.md`'s claim about it should be softened (T3). I note the z.ai review in that repository reached the same conclusion; I reached it independently from the repository contents.

**Verdict:** the three repositories are *compatible in intent* but do not yet demonstrably "express the same underlying model," because the model has no single canonical statement to be consistent *with*. Consistency is currently a property of the author's mind, not of the text.

## Recommended revisions

Ordered by leverage.

**R1. Create `GLOSSARY.md` in mission-framework as the single canonical definition point.** One entry per concept (Mission, Need, Value, Objective, Outcome, Capability, Service, Workflow, Evidence, Observation, Claim, Knowledge, Understanding/Reasoning, Decision, Trust, justified, material, consequential, sufficient…). Every other document — in all three repositories — links to it and restates nothing. Move the MRM's fifteen definitions here (the Platform keeps relationship semantics). Consequence: cross-repo drift becomes structurally impossible rather than editorially policed.

**R2. Declare one canonical Mission Loop; demote the rest to labelled views.** Choose the stage list once (Principle 13's version is the best candidate: it is the most complete cycle with the fewest undefined stages). Then add one short document or section: "Views of the Loop," mapping each other diagram to it (e.g., "MISSION_INTELLIGENCE expands the Knowledge→Decision segment"; "ARCHITECTURE's flow is the loop minus Need/Mission, as seen by the runtime"). Consequence: the seven variants become features (zoom levels) instead of bugs (contradictions).

**R3. Restate the Reality Principle as an evidence-revision rule.** Suggested language for `docs/REALITY_MODEL.md` / `README.md`: "Reality is the final authority — but reality speaks only through evidence. Operationally this principle means: when credible evidence contradicts a model, the model must change or the contradiction must be explicitly recorded and held open; a model may never be defended by dismissing evidence without procedure." Consequence: closes the naïve-realism exposure and gives disagreements a procedure instead of a slogan.

**R4. Repair the Decision/accountability semantics.** (a) In `mission-reference-model.md`, delete "or mechanism" from the Decision definition. (b) Add a Mission Core concept **Delegation** (or *Delegated Authority*): a recorded, human-accountable decision that authorises a mechanism or subordinate actor to act within explicit bounds, with owner, scope, validity period, revocation condition and evidence trail. (c) Replace "human or organisational authorities" with a rule that organisational accountability must resolve to an identifiable role. Consequence: "AI proposes, humans decide" becomes compatible with automation instead of being falsified by it.

**R5. Put the Mission Core admission rule into the repository, in procedural form** (per O4), as an ADR or a section of the future glossary. Consequence: the rule can actually be applied and audited under implementation pressure.

**R6. Define "genuine need" or drop "genuine."** Suggested: "A need is treated as genuine when its existence is supported by evidence from or about those who have it — not solely by the assertion of those proposing the mission. Genuineness is an evidentiary status, and like all such statuses it is revisable." Consequence: the framework's foundation stone becomes testable by its own evidence machinery, and the need/value circle opens.

**R7. Split the trust ladder.** Replace the 0–5 scale in `TRUST.md` with two explicit dimensions: *verification status* (Unknown / Observed / Verified / Corroborated — facts about process history) and *fitness decision* (fit / not fit / not assessed, always relative to a stated purpose and date). Consequence: removes the false implication that verification level entails usability, and vice versa.

**R8. Housekeeping with outsized signalling value:** amend `HISTORY.md` (T3) to Principle-15-compliant wording; add or link Manifesto and Constitution or remove the entries; revise or archive `MISSION.md` (T4); unify "Mission Eclipse"/"Mission Solar Eclipse"; rename either Mission Kernel or Mission Core; state whether the Reality Anchor Principle and the Reality Principle are one principle (recommended: one principle, two scopes — claims and architecture); state which principle set is canonical and derive the others; extend "hedged as hypothesis" from the trust field to the whole metaphor family; change "measurable emergent property" to "intended to become measurable"; state explicitly (once) that material/consequential/sufficient thresholds are mission-policy parameters set via the policy engine, not framework constants.

## Open questions

1. Who arbitrates when two candidate "genuine needs" (or two missions) conflict over the same reality — and is that arbitration itself a Mission Core concern (authority, mandate) or out of scope?
2. What is the decision rule when contradictory evidence remains unresolved but a decision cannot wait? (The framework preserves contradiction admirably; it does not yet say how to *act under* it.)
3. Is Mission Framework itself a mission? If so, does it pass its own Architecture Tests and Principle 15 — and should the repositories carry their own Reality Anchors (e.g., evidence that anyone outside the project uses it)? Reflexivity would be a powerful demonstration; its absence is currently conspicuous.
4. What is the unit of a trust assessment — a claim, an evidence object, a source, a dependency edge? The documents apply trust to all four without saying whether the same scale applies.
5. How does human accountability function when no accountable human can fully understand the evidence chain (e.g., AI-correlated evidence across thousands of items)? Is "reviewable in principle" sufficient, or must review be feasible in practice at decision speed?
6. How will canonical semantics be versioned? Documents carry version numbers (Platform) or none (framework); nothing describes how a change to a canonical definition propagates to dependent repos, schemas and past evidence — yet "Everything Evolves" guarantees such changes.
7. Are Understanding and Reasoning the same stage? (Smallest question on this list; would resolve three diagram discrepancies at once.)

## Overall conclusion

**Coherent with conditions.**

The conceptual core — reality gap, evidence as first-class engineering object, preserved contradiction, trust as earned/decaying/multidimensional, humans accountable — is sound, internally motivated and unusually self-critical. Nothing found in this review indicates a foundation that must be torn up. The Evidence Model and Reality Model in particular are close to schema-ready.

But the project is not yet coherent *as a text*: its spine (the loop) exists in seven versions, its keystone terms (genuine, justified, material, consequential) are undefined, its most important boundary rule (Mission Core admission) exists only in letters to reviewers, and its accountability slogan is contradicted by its own canonical Decision definition. None of these is deep; all of them are exactly the kind of ambiguity a schema will freeze permanently if Sprint 1 begins first.

Conditions for proceeding to Sprint 1, in order: R1 (glossary as single definition point), R2 (one canonical loop), R4 (Decision/Delegation repair), R5 (admission rule in-repo, procedural). R3 and R6–R8 can proceed in parallel with early implementation without freezing risk.

The framework's closing axiom promises systems that know "exactly why they believe what they believe." The fastest way to honour that promise is for the documents to apply it to themselves: one definition per concept, one canonical loop, no claim without its anchor.

---

Submitted as review text for human evaluation, per `reviews/README.md`: no finding herein is canonical unless adopted through an explicit decision or pull request.

**Claude (Anthropic)**
Conceptual, semantic and editorial reviewer
