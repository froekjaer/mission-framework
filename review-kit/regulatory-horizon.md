# Regulatory Horizon

**Version:** 0.1 (initial scan)
**Status:** Governed horizon-scanning artefact — **not legal advice**
**Last verified date:** 2026-07-25 (initial population)
**Owner:** Mission Owner (Peter Frøkjær)

## Purpose

This artefact is a governed, versioned horizon scan of regulations, directives, and authoritative guidance that **may** apply to the Mission Platform, its payloads, or its customers. It exists so that reviewers and architects assess applicability against a shared, maintained list instead of from memory.

It is **not legal advice** and **not a compliance claim**. Applicability depends on the specific deployment, customer, sector, data processed, and jurisdiction. Uncertain applicability SHALL NOT be presented as fact.

## How to use this artefact

- Reviewers and architects SHALL **assess applicability** of each instrument against the specific review scope. They SHALL NOT assume every listed instrument applies.
- Each entry has an `applicability` field. Treat the labels literally:
  - **confirmed** — applicability has been verified for a concrete case.
  - **potentially applicable** — plausible relevance; requires case-specific verification.
  - **monitoring only** — tracked because it may become relevant; no current action.
  - **not currently applicable** — considered and judged out of scope; rationale recorded.
- Because laws, deadlines, and implementing acts change, any substantive legal content MUST be verified against authoritative current sources before publication or reliance. The `last_verified_date` field supports this.
- When in doubt, escalate to a qualified lawyer. AI-generated summaries in this file SHALL NOT be treated as authoritative.

## Fields

Each entry records:

- `jurisdiction` — EU / DK / DE / CN / AU / US / cross-jurisdictional.
- `instrument` — short name.
- `status` — in force / phased in / proposal / transposed / future application / maintained guidance.
- `relevant_dates` — key dates and next deadlines.
- `potential_mission_applicability` — plain-language note on why it may matter.
- `affected_repository_platform_payload` — where it bites (framework / platform / specific payload / customer deployment).
- `required_evidence` — what artefact demonstrates compliance (DPIA, SBOM, DPA, risk assessment, etc.).
- `responsible_owner` — accountable role.
- `last_verified_date` — when the entry was last checked against an authoritative source.
- `primary_authoritative_source` — the official text or register.
- `applicability` — confirmed / potentially applicable / monitoring only / not currently applicable.

---

## European Union

### GDPR — General Data Protection Regulation
- **jurisdiction:** EU
- **status:** in force (since 2018-05-25)
- **relevant_dates:** applies from 2018-05-25
- **potential_mission_applicability:** Personal data in images, access logs, AI tags, and cloud processing. Direct relevance for any payload capturing images of people or processing personal data.
- **affected:** platform (data layer, retention), payloads (image capture, AI tagging), customer deployments.
- **required_evidence:** DPIA per customer/site; retention policy; DPA with subprocessors; breach procedure (Art. 33/34).
- **responsible_owner:** Mission Owner + legal counsel.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Regulation (EU) 2016/679.
- **applicability:** confirmed (for image/personal-data payloads).

### EU AI Act — Artificial Intelligence Act
- **jurisdiction:** EU
- **status:** phased in
- **relevant_dates:** from 2024-08-01; next deadline 2026-08-02 (further phases follow).
- **potential_mission_applicability:** AI provider/deployer roles, prohibited practices, transparency, oversight, post-market evidence. Relevant for AI tagging, edge AI QA, and any future AI-assisted payload.
- **affected:** platform (AI runtime governance), payloads (AI tagging, edge QA).
- **required_evidence:** provider/deployer role determination; transparency records; post-market monitoring.
- **responsible_owner:** Mission Owner + legal counsel.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Regulation (EU) 2024/1689.
- **applicability:** potentially applicable (depends on AI use classification).

### AI Omnibus — Digital Omnibus (AI Act amendments)
- **jurisdiction:** EU
- **status:** proposal (political agreement)
- **relevant_dates:** horizon
- **potential_mission_applicability:** May change AI Act high-risk timelines and implementation details. Final Official Journal text must govern.
- **affected:** platform (AI runtime governance).
- **required_evidence:** none until finalised.
- **responsible_owner:** Mission Owner.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** European Commission proposals tracker.
- **applicability:** monitoring only.

### CRA — Cyber Resilience Act
- **jurisdiction:** EU
- **status:** phased in
- **relevant_dates:** from 2024-12-10; next deadline 2026-09-11.
- **potential_mission_applicability:** Secure product lifecycle, SBOM, coordinated vulnerability disclosure, support period, reporting, conformity, CE marking. Likely direct for any productised edge hardware/software.
- **affected:** platform (lifecycle, SBOM, signing), payloads (packaging), edge hardware.
- **required_evidence:** SBOM per release; vulnerability handling process; support-period declaration; conformity assessment.
- **responsible_owner:** Mission Owner + engineering.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Regulation (EU) 2024/2847.
- **applicability:** likely direct (if productised).

### Data Act
- **jurisdiction:** EU
- **status:** in force (from 2025-09-12)
- **relevant_dates:** applies from 2025-09-12
- **potential_mission_applicability:** Connected-product data access, metadata, portability, contracts, secure export. Relevant because edge nodes are connected products generating data.
- **affected:** platform (data access APIs, export), payloads (data ownership).
- **required_evidence:** data access mechanism; contract terms.
- **responsible_owner:** Mission Owner + legal counsel.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Regulation (EU) 2023/2854.
- **applicability:** potentially applicable.

### NIS2 — Network and Information Systems Directive 2
- **jurisdiction:** EU
- **status:** transposed
- **relevant_dates:** from 2023-01-16 (directive); national transposition deadlines vary.
- **potential_mission_applicability:** Risk governance, incident reporting, continuity, supply chain, vulnerability handling, management accountability. Customer-driven or conditional.
- **affected:** platform (incident response, supply chain), customer deployments.
- **required_evidence:** risk measures; incident reporting procedure; supply-chain controls.
- **responsible_owner:** Mission Owner + customer compliance function.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Directive (EU) 2022/2555.
- **applicability:** customer driven or conditional.

### CER — Critical Entities Resilience Directive
- **jurisdiction:** EU
- **status:** transposed by sector
- **relevant_dates:** from 2023-01-16
- **potential_mission_applicability:** Physical and operational resilience requirements for critical customers and dependencies. Customer-driven.
- **affected:** customer deployments (critical sectors).
- **required_evidence:** resilience measures (customer-side).
- **responsible_owner:** customer compliance function.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Directive (EU) 2022/2557.
- **applicability:** customer driven.

### Product Liability Directive (revised)
- **jurisdiction:** EU
- **status:** transposition pending
- **relevant_dates:** next deadline 2026-12-09
- **potential_mission_applicability:** Software and AI product liability, updates, related services, preservation of technical evidence. Likely direct for productised software/AI.
- **affected:** platform, payloads (productised components).
- **required_evidence:** evidence preservation (technical records); update records.
- **responsible_owner:** Mission Owner + legal counsel.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Directive (EU) 2024/2853.
- **applicability:** likely direct (if productised).

### Cybersecurity Act (EU)
- **jurisdiction:** EU
- **status:** in force (since 2019-06-27)
- **relevant_dates:** from 2019-06-27
- **potential_mission_applicability:** European certification framework for ICT products, services, processes, managed security services. Market- or customer-driven.
- **affected:** productised platform components (certification path).
- **required_evidence:** certification if required by customer/market.
- **responsible_owner:** Mission Owner.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Regulation (EU) 2019/881.
- **applicability:** market or customer driven.

### Cyber Solidarity Act
- **jurisdiction:** EU
- **status:** in force (from 2025-02-04)
- **relevant_dates:** from 2025-02-04
- **potential_mission_applicability:** EU preparedness, cyber reserve, coordinated response, post-incident review. Horizon or customer-driven.
- **affected:** incident response coordination (rare).
- **required_evidence:** none generally; situational awareness.
- **responsible_owner:** Mission Owner.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Regulation (EU) 2024/1739.
- **applicability:** horizon or customer driven.

### DORA — Digital Operational Resilience Act
- **jurisdiction:** EU
- **status:** in force (from 2025-01-17)
- **relevant_dates:** from 2025-01-17
- **potential_mission_applicability:** Financial-customer ICT third-party risk, contracts, registers, testing, exit plans. Sector-conditional.
- **affected:** customer deployments in financial sector.
- **required_evidence:** ICT third-party register (customer-side).
- **responsible_owner:** customer compliance function.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Regulation (EU) 2022/2554.
- **applicability:** sector conditional.

### Machinery Regulation
- **jurisdiction:** EU
- **status:** future application
- **relevant_dates:** from 2027-01-20
- **potential_mission_applicability:** Future OT payloads that control machinery or become safety components. Vertical-conditional.
- **affected:** future OT payloads (e.g. waterworks actuators).
- **required_evidence:** conformity assessment (when such a payload is built).
- **responsible_owner:** payload owner.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Regulation (EU) 2023/1230.
- **applicability:** vertical conditional.

### RED — Radio Equipment Directive
- **jurisdiction:** EU
- **status:** in force (from 2016-06-13)
- **relevant_dates:** from 2016-06-13
- **potential_mission_applicability:** Relevant if TimeLapse Pro / Mission Platform becomes manufacturer or integrator of marketed radio equipment.
- **affected:** edge hardware (if marketed as radio equipment).
- **required_evidence:** conformity (if in scope).
- **responsible_owner:** Mission Owner.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** EUR-Lex Directive 2014/53/EU.
- **applicability:** hardware conditional.

### ENISA NIS2 guidance
- **jurisdiction:** EU
- **status:** current guidance (from 2025-06-26)
- **relevant_dates:** maintained
- **potential_mission_applicability:** Practical measures for risk, incidents, continuity, supply chain, secure development, cryptography, access, assets. Implementation reference — not legislation.
- **affected:** platform (implementation guidance).
- **required_evidence:** none (reference only).
- **responsible_owner:** engineering.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** ENISA publications.
- **applicability:** implementation reference.

---

## Denmark

### Dansk NIS2-lov (Lov om foranstaltninger til sikring af et højt cybersikkerhedsniveau)
- **jurisdiction:** DK
- **status:** in force (from 2025-07-01)
- **relevant_dates:** from 2025-07-01
- **potential_mission_applicability:** Danish scope, section 6 controls, management duties, supervision, reporting. Customer-driven or conditional.
- **affected:** customer deployments in Denmark.
- **required_evidence:** risk assessment; controls; management approval.
- **responsible_owner:** customer compliance function.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** Retsinformation.
- **applicability:** customer driven or conditional.

### TV-overvågningsloven (CCTV Act)
- **jurisdiction:** DK
- **status:** in force (from 2023-02-24, consolidated)
- **relevant_dates:** from 2023-02-24
- **potential_mission_applicability:** Repeated camera monitoring of persons, public areas, workplaces; signage and disclosure. Site-conditional — directly relevant to timelapse image capture of people/areas.
- **affected:** timelapse payload; customer sites.
- **required_evidence:** permit/registration if required; signage; disclosure.
- **responsible_owner:** customer site manager + legal counsel.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** Retsinformation.
- **applicability:** site conditional.

---

## Germany

### IT-Grundschutz (BSI)
- **jurisdiction:** DE
- **status:** maintained
- **relevant_dates:** maintained
- **potential_mission_applicability:** German modular ISMS, risk and audit reference. Useful for German customers; not itself a universal statutory obligation.
- **affected:** customer deployments in Germany.
- **required_evidence:** none statutory; customer-driven.
- **responsible_owner:** customer compliance function.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** BSI IT-Grundschutz.
- **applicability:** market or customer driven.

### BSI ICS Security Compendium
- **jurisdiction:** DE
- **status:** current guidance
- **relevant_dates:** maintained
- **potential_mission_applicability:** OT/ICS architecture and security practice, including IT-Grundschutz IND.1 and IEC 62443 alignment. Implementation reference.
- **affected:** platform (OT guidance).
- **required_evidence:** none (reference).
- **responsible_owner:** engineering.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** BSI publications.
- **applicability:** implementation reference.

---

## China

> Chinese authoritative text and local legal review are required for any concrete scope determination. Entries below flag plausibility only.

### CSL — Cybersecurity Law
- **jurisdiction:** CN
- **status:** in force and evolving (from 2017-06-01)
- **relevant_dates:** from 2017-06-01
- **potential_mission_applicability:** Network-operator and critical-information-infrastructure duties.
- **affected:** any deployment processing data in China.
- **required_evidence:** requires Chinese legal interpretation.
- **responsible_owner:** Mission Owner + Chinese legal counsel.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** NPC official text.
- **applicability:** market or processing conditional.

### DSL — Data Security Law
- **jurisdiction:** CN
- **status:** in force (from 2021-09-01)
- **relevant_dates:** from 2021-09-01
- **potential_mission_applicability:** Data classification, protection, potentially extraterritorial duties.
- **affected:** data processing touching China.
- **required_evidence:** requires Chinese legal interpretation.
- **responsible_owner:** Mission Owner + Chinese legal counsel.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** NPC official text.
- **applicability:** market or processing conditional.

### PIPL — Personal Information Protection Law
- **jurisdiction:** CN
- **status:** in force (from 2021-11-01)
- **relevant_dates:** from 2021-11-01
- **potential_mission_applicability:** Personal-information processing, sensitive data, cross-border transfers. Images and AI metadata may be in scope.
- **affected:** image/AI data touching China.
- **required_evidence:** requires Chinese legal interpretation.
- **responsible_owner:** Mission Owner + Chinese legal counsel.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** NPC official text.
- **applicability:** market or processing conditional.

### GB/T 39204-2022
- **jurisdiction:** CN
- **status:** current (from 2023-05-01)
- **relevant_dates:** from 2023-05-01
- **potential_mission_applicability:** Critical-information-infrastructure protection reference. Catalog use depends on lawful access to the complete standard.
- **affected:** critical-infrastructure deployments.
- **required_evidence:** none (reference).
- **responsible_owner:** customer compliance function.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** Chinese national standards.
- **applicability:** market or customer driven.

---

## Australia

### SOCI Act 2018
- **jurisdiction:** AU
- **status:** in force and evolving (from 2018-07-11)
- **relevant_dates:** from 2018-07-11
- **potential_mission_applicability:** Critical-infrastructure registration, reporting, risk programs, government assistance. Sector-conditional.
- **affected:** customer deployments in critical AU sectors.
- **required_evidence:** registration; risk program (customer-side).
- **responsible_owner:** customer compliance function.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** Office of Parliamentary Counsel (consolidated).
- **applicability:** sector conditional.

### Cyber Security Act 2024 (AU)
- **jurisdiction:** AU
- **status:** in force (from 2024-11-30)
- **relevant_dates:** from 2024-11-30
- **potential_mission_applicability:** Smart-device security, ransomware payment reporting, significant-incident coordination. Market- or entity-conditional.
- **affected:** productised smart devices.
- **required_evidence:** depends on product and entity scope.
- **responsible_owner:** Mission Owner.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** Office of Parliamentary Counsel.
- **applicability:** market or entity conditional.

### ASD Essential Eight Maturity Model
- **jurisdiction:** AU
- **status:** maintained
- **relevant_dates:** maintained
- **potential_mission_applicability:** Prioritised IT mitigations. ASD explicitly notes the model was not designed specifically for OT. Implementation reference.
- **affected:** platform (IT mitigation reference).
- **required_evidence:** none (reference).
- **responsible_owner:** engineering.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** ASD publications.
- **applicability:** implementation reference.

### ASD ISM (Information Security Manual)
- **jurisdiction:** AU
- **status:** maintained
- **relevant_dates:** maintained
- **potential_mission_applicability:** Detailed security controls and guidance, including procurement, supply-chain integrity, OT equipment. Government- or customer-driven.
- **affected:** customer deployments (government).
- **required_evidence:** none statutory generally.
- **responsible_owner:** customer compliance function.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** ASD publications.
- **applicability:** government or customer driven.

---

## United States

### NERC CIP (Critical Infrastructure Protection Standards)
- **jurisdiction:** US
- **status:** in force and evolving
- **relevant_dates:** maintained
- **potential_mission_applicability:** North American bulk electric system cyber controls. Relevant for energy market readiness and supplier evidence.
- **affected:** energy-sector customer deployments.
- **required_evidence:** compliance evidence (customer/supplier).
- **responsible_owner:** customer compliance function.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** NERC standards.
- **applicability:** market or customer driven.

### FERC Order No. 887
- **jurisdiction:** US
- **status:** implementation
- **relevant_dates:** track final standards
- **potential_mission_applicability:** NERC CIP evolution for internal network security monitoring.
- **affected:** energy-sector deployments (monitoring).
- **required_evidence:** none yet.
- **responsible_owner:** customer compliance function.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** FERC orders.
- **applicability:** market or customer driven.

### U.S. Cyber Trust Mark
- **jurisdiction:** US
- **status:** rolling out (voluntary)
- **relevant_dates:** rolling out
- **potential_mission_applicability:** Consumer IoT market signal. Not a substitute for industrial/OT assurance.
- **affected:** consumer-IOT productisation (if any).
- **required_evidence:** none (voluntary).
- **responsible_owner:** Mission Owner.
- **last_verified_date:** 2026-07-25
- **primary_authoritative_source:** FCC / NIST program.
- **applicability:** market optional.

---

## Cross-jurisdictional considerations

- **Cross-border data transfer.** When images, telemetry, or AI processing cross jurisdictions (e.g. EU→US cloud AI), transfer mechanisms (SCCs, adequacy decisions) and the receiving jurisdiction's laws (e.g. CN PIPL for transfers into China) BOTH apply. Record the transfer path in the DPIA.
- **Customer-driven applicability.** Many instruments above are *customer-driven*: the customer's sector and jurisdiction determine whether the instrument applies to a deployment on their site. The Mission Platform provides the evidence artefacts; the customer's compliance function makes the determination.
- **Hardware productisation threshold.** Several instruments (CRA, RED, PLD, AU Cyber Security Act) hinge on whether the platform/hardware is *productised and placed on the market* vs. operated internally. This is a Mission Owner decision that should be made explicitly, not by drift.
- **AI classification drift.** AI Act and PLD scope depends on how AI capabilities are classified (provider vs. deployer; high-risk vs. limited). Re-assess when a new AI capability is added to any payload.
- **Authoritative source rule.** Where this file and an authoritative official source disagree, the official source governs. Update this file and record the change.

---

## Maintenance

- This artefact SHALL be reviewed when: a new payload vertical is scoped; a new customer sector is onboarded; a deadline listed above passes; or annually, whichever is first.
- Every substantive legal change SHALL be verified against an authoritative current source before the `last_verified_date` is updated.
- A retired or superseded instrument SHALL be marked, not silently deleted.
- This file is evidence-grade: changes to it SHOULD be traceable in git history with a rationale.
