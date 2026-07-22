# MIAR Risk Assessment Method

## 1. General requirements

Produce two separate risk analyses:

1. **Project Risk Assessment** — risks to the project, system, implementation, governance, adoption and long-term viability.
2. **Cyber and Regulatory Risk Assessment** — risks arising from architecture, software, AI, data, operations, supply chain, privacy, resilience and legal obligations.

Do not merge the two registers. Cross-reference related risks where useful.

For every risk record include:

- unique ID;
- risk statement in cause-event-impact form;
- affected repositories and artefacts;
- evidence and provenance;
- threat or cause;
- affected mission objectives/assets;
- existing controls;
- likelihood and impact with scale definitions;
- inherent risk;
- control effectiveness;
- residual risk;
- recommended treatment;
- accountable role, if defined;
- target date or trigger;
- verification test;
- confidence and knowledge-state label.

State the selected assessment framework and explain any deviations. ISO 31000, ISO/IEC 27005, NIST CSF 2.0, NIST SP 800-30, IEC 62443, SABSA, COBIT and comparable methods may inform the work, but labels must not imply certification.

## 2. Project Risk Assessment minimum domains

Evaluate at least:

- mission, value proposition and success criteria;
- scope and architectural boundaries;
- cross-repository coherence and ownership;
- semantic integrity and ontology drift;
- governance, authority and decision latency;
- evidence quality, research design and source bias;
- roadmap, delivery, finance and sustainability;
- stakeholder ownership, communication and adoption;
- competence, capacity, succession and key-person dependency;
- technology and vendor dependency;
- AI hallucination, context loss, model drift and prompt dependence;
- open-source contribution and maintainer risks;
- legal, ethical and reputational risks;
- testability, validation and failure recovery;
- ten-year longevity and migration risk.

The assessment shall explicitly test whether process complexity, assurance overhead or token cost could exceed the value created.

## 3. Cyber and Regulatory Risk Assessment minimum domains

Evaluate at least:

- system and trust-boundary architecture;
- identity, authentication, authorisation and privileged access;
- repository governance, branch protection and change approval;
- provenance, signatures, hashes, releases and trust bootstrap;
- prompt injection, indirect prompt injection and context poisoning;
- malicious or compromised canonical sources;
- model, tool, connector and agent substitution;
- secrets, credentials and key management;
- software supply chain, dependencies, SBOM, build provenance and CVD;
- secure development lifecycle and vulnerability handling;
- logging, monitoring, evidence integrity and non-repudiation;
- incident response, reporting and forensic preservation;
- availability, backup, continuity, disaster recovery and exit;
- data classification, minimisation, retention and deletion;
- personal data in images, access logs, AI tags and cloud processing;
- cross-border processing and processor/subprocessor governance;
- physical, camera, radio, edge, IoT and OT risks where applicable;
- customer and sector assurance obligations.

## 4. Minimum regulatory and assurance horizon

The following list is a minimum review horizon, not a conclusion that every instrument applies. For each item, verify current official text, status, dates, territorial reach, role definitions, applicability and implementation guidance. Distinguish law from proposal, standard, guidance, voluntary programme and customer requirement.

### European Union and Denmark

- General Data Protection Regulation (GDPR)
- EU Artificial Intelligence Act
- proposed or adopted AI Act amendment packages, including the AI Omnibus / Digital Omnibus where relevant
- Cyber Resilience Act (CRA)
- Data Act
- NIS2 Directive
- Danish NIS 2 legislation and implementing rules
- Critical Entities Resilience Directive (CER)
- revised Product Liability Directive
- EU Cybersecurity Act and relevant certification schemes
- Cyber Solidarity Act
- Danish TV surveillance legislation
- Digital Operational Resilience Act (DORA)
- Machinery Regulation
- Radio Equipment Directive (RED), including delegated cybersecurity requirements where applicable
- ENISA technical guidance relevant to NIS2, secure development, incidents, supply chain, cryptography, access and asset management

### Germany and European implementation references

- BSI IT-Grundschutz
- BSI ICS Security Compendium and relevant IEC 62443 alignment

### Australia

- Security of Critical Infrastructure Act 2018 and applicable rules
- Cyber Security Act 2024 and subsequent rules or amendments
- ASD Essential Eight Maturity Model
- Australian Government Information Security Manual (ISM)

### China

- Cybersecurity Law
- Data Security Law
- Personal Information Protection Law (PIPL)
- relevant cross-border transfer and critical-information-infrastructure rules
- GB/T 39204 and other lawfully accessible applicable standards

Concrete Chinese scope conclusions require authoritative Chinese sources and qualified local legal interpretation.

### United States and North American energy

- NERC Critical Infrastructure Protection standards
- FERC Order No. 887 and resulting approved NERC standards and implementation plans
- U.S. Cyber Trust Mark programme where relevant

### Additional sources

Reviewers shall add other relevant laws, standards and frameworks discovered during the review. Consider at least ISO/IEC 27001, 27002, 27005, 27701, 42001, 23894; NIST CSF 2.0; NIST AI RMF; NIST SSDF; OWASP guidance for LLM and agentic systems; SLSA; OpenSSF; IEC 62443; ETSI EN 303 645; and sector/customer requirements.

## 5. Legal accuracy rule

A reviewer shall not present legal applicability as established merely because a technology appears in scope. Use one of:

- **DIRECT** — clearly applies on verified facts;
- **CONDITIONAL** — may apply if stated conditions are met;
- **CUSTOMER/SECTOR DRIVEN** — arises through customer, contract or regulated-sector context;
- **HORIZON** — monitor for future relevance;
- **NOT ESTABLISHED** — insufficient evidence.

Legal conclusions must cite current official sources and clearly state that the review is not a substitute for qualified legal advice.

## 6. Adversarial trust-bootstrap analysis

The cyber review must model at least these attack paths:

1. attacker compromises or impersonates the repository owner;
2. attacker changes a canonical file on an authorised branch;
3. malicious pull request receives accidental approval;
4. AI follows a look-alike repository, branch, path or domain;
5. canonical document contains indirect prompt injection;
6. review invitation or operational loader is altered to redirect trust;
7. stale cached content defeats a security update;
8. signed content is valid but maliciously authorised;
9. governance roles collude or a single maintainer becomes compromised;
10. a connector or AI falsely claims that a read/write was verified.

Assess preventive, detective, corrective and recovery controls. Do not treat a URL, commit hash or signature alone as sufficient proof of legitimacy; evaluate the complete governance and provenance chain.