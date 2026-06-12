<a id="phase-6"></a>
## Phase 6: Governance, Security & Compliance (months 34–39, 120 h + 14 h Appendix A)

**Goal:** build the control plane of a regulated data platform: catalog + lineage as the metadata backbone, data quality as an engineering discipline, MDM/RDM for the entities the fund industry lives on, fine-grained access control and masking, and the regulatory frameworks (GDPR, DORA, DCAM) that decide what "good" means in Luxembourg.
**Entry prerequisites:** Phases 2–5 (a platform worth governing; OTel/observability foundations).
**Exit criteria:** you can (1) stand up a catalog with end-to-end lineage and answer an impact-analysis question from it; (2) design a DQ framework from profiling to alerting with rules tied to the six dimensions; (3) design a security-master MDM with match/merge and survivorship; (4) implement RLS/CLS and policy-as-code on the lakehouse; (5) map your platform to GDPR/DORA obligations and lead a DCAM self-assessment.
**Appendix A items scheduled here:** A.14 data strategy & operating model, A.15 architecture risk management, A.16 data risk & controls, A.17 ethics, A.18 purpose-based sharing, A.19 records management, A.20 organizational change management (14 h).

### T1/T2 topics

#### 10.1.1 Metadata management & active catalogs — T1
- **Why:** governance-and-lineage is an explicit mastery bias: the catalog is the control plane — ownership, glossary, lineage, quality, and policy all hang off it.
- **Learn:** metadata kinds (technical/business/operational) and active vs passive metadata; OpenMetadata architecture (ingestion framework, connectors, APIs); entity model: domains, owners, tiers, glossary links; automated ingestion from Postgres/Trino/dbt/Kafka/Dagster; catalog-driven workflows (announcements, tasks, approval flows); DataHub as the alternative (event-sourced metadata, also OpenLineage-friendly); what makes metadata "active" (policies and alerts firing *from* metadata).
- **Resource:** OpenMetadata official docs (concepts + ingestion) . *Alternate:* DataHub docs (architecture).
- **Tools:** FOSS: OpenMetadata (↔ Microsoft Purview, Collibra, Alation) · Corp: Purview (Azure default) + Collibra (EU FS incumbent) at evaluation level.
- **Do:** deploy OpenMetadata; ingest Postgres, Trino/Iceberg, dbt, and Kafka metadata; assign owners/tiers to every gold asset; wire one active workflow (schema-change announcement to consumers).
- **Done when:** "who owns this, who consumes it, what breaks if I change it?" is answerable from the catalog in under two minutes.
- Est. hours: 10

#### 10.3.1 Data lineage (OpenLineage standard) — T1
- **Why:** BCBS-239-grade traceability — every regulatory number must walk back to its sources; lineage is also the architect's impact-analysis weapon.
- **Learn:** OpenLineage spec: runs/jobs/datasets, facets; emitters: Dagster, Spark, dbt integrations; Marquez as reference backend; column-level vs table-level lineage (what dbt/SQL parsing gives vs what Spark gives); lineage into the catalog (OpenMetadata/DataHub ingestion); designing for lineage (naming, job granularity); limits — lineage of black-box SaaS steps.
- **Resource:** OpenLineage docs (spec + integrations) + Marquez getting-started.
- **Tools:** FOSS: OpenLineage + Marquez, surfaced in OpenMetadata (↔ Purview lineage, Collibra lineage, Manta) · Corp: Purview/Collibra lineage (evaluation level).
- **Do:** emit OpenLineage events from Dagster and dbt for the full NAV path (Postgres → Debezium → Iceberg → Spark → dbt → EMT output); render end-to-end lineage and answer one impact query ("which reports break if `orders.amount` changes?") from it.
- **Done when:** the EMT output's lineage back to source tables is demonstrable to an auditor, column-level where the tooling allows.
- Est. hours: 7

#### 9.4.2 + 10.4.1 Data quality engineering (Great Expectations / Soda) — T1
- **Why:** non-negotiable in regulated data: DQ rules are how "accuracy, completeness, timeliness" stop being audit prose and start being code.
- **Learn:** the six DQ dimensions mapped to executable rule types; Great Expectations: suites, checkpoints, data docs; Soda Core: SodaCL checks, scan integration in orchestration; dbt tests vs dedicated DQ frameworks (layering, not either/or); severity & circuit-breaking (block publish vs warn — ties to your WAP gates); DQ result routing to catalog/alerts; writing rules from profiling output, not imagination.
- **Resource:** *Data Quality Fundamentals* (Moses et al.) ch. 1–4 + Soda Core docs (SodaCL).
- **Tools:** FOSS: Soda Core + Great Expectations + dbt tests (↔ Informatica DQ, Talend DQ) · Corp: Informatica DQ (EU FS incumbent; evaluation level).
- **Do:** define the DQ rulebook for the NAV pipeline: per dataset, rules across all six dimensions with severities; wire Soda scans into the WAP gate so criticals block publish and warnings page the catalog.
- **Done when:** a seeded completeness failure blocks publish, appears in the catalog, and pages with a link to the failing expectation — and you can justify every rule's dimension and severity.
- Est. hours: 10

#### 10.4.3 Data profiling — T2
- **Why:** profiling is the evidence-gathering step before DQ rules — discover distributions, cardinalities, and surprises rather than assuming them.
- **Learn:** profiling outputs (distributions, nulls, uniqueness, patterns, drift over time); ydata-profiling for one-shot EDA; whylogs for continuous statistical profiles; profiling as DQ-rule generator; PII discovery overlap (ties to 11.4.1).
- **Resource:** ydata-profiling docs + whylogs concepts page.
- **Tools:** FOSS: ydata-profiling, whylogs (↔ Informatica/Collibra profiling modules).
- **Do:** profile the silver holdings table; turn the five most surprising findings into Soda rules; schedule a weekly whylogs profile and diff alert.
- **Done when:** at least three of your DQ rules exist *because* profiling falsified an assumption.
- Est. hours: 3

#### 10.4.2 Managed data observability platforms — T2
- **Why:** Monte Carlo-class tools are the buy side of the DQ build-vs-buy; their ML-anomaly pitch needs informed evaluation.
- **Learn:** anomaly-detection-on-metadata model (freshness/volume/schema drift without rules); incident workflow & lineage-aware blast radius; pricing models; where rule-based and anomaly-based DQ complement each other.
- **Resource:** Monte Carlo docs/architecture overview (vendor source, read critically).
- **Do:** half-page build-vs-buy: your Soda+Elementary stack vs Monte Carlo for a 200-pipeline estate.
- **Done when:** you can state which failure classes anomaly detection catches that your rules never will, and vice versa.
- Est. hours: 2

#### 10.9.1 + 10.9.2 Data observability (pipeline health) — T2
- **Why:** freshness/volume/schema-drift monitoring is the data plane's heartbeat — distinct from infra observability (Phase 5) and from DQ rules (above).
- **Learn:** the five data-observability pillars (freshness, volume, schema, distribution, lineage); Elementary as dbt-native observability (anomaly tests, report UI); wiring data incidents into the same alerting path as infra; data incident triage runbook.
- **Resource:** Elementary docs + *Data Quality Fundamentals* ch. on observability pillars.
- **Tools:** FOSS: Elementary + OpenLineage events (↔ Monte Carlo, Databand, Bigeye).
- **Do:** add Elementary to the dbt project; enable volume/freshness anomaly tests on gold; route one synthetic incident through Grafana alerting with a runbook link.
- **Done when:** silent-failure classes (stale, shrunken, schema-drifted) each have a detector and an owner.
- Est. hours: 3

#### 10.5.1 Master data management — T1
- **Why:** the security/fund/counterparty master *is* the fund-industry data problem — every NAV error story ends at reference data; the architect designs the master, even when the tool is bought.
- **Learn:** MDM styles (registry, consolidation, coexistence, centralized) and their org costs; match/merge: deterministic vs probabilistic (Fellegi–Sunter intuition), blocking, thresholds; survivorship rules and golden-record assembly; hierarchy management (fund → sub-fund → share class; issuer trees); stewardship workflow (review queues); integration patterns (MDM as publisher to the platform); security-master specifics: identifier cascade (ISIN/FIGI/internal), vendor-feed precedence (Bloomberg vs Refinitiv), corporate-action survivorship.
- **Resource:** DAMA-DMBOK ch. 10 (Reference & Master Data) + Splink documentation (probabilistic linkage, MoJ open source).
- **Tools:** FOSS: Splink for match/merge + Postgres for the hub (↔ Informatica MDM, Reltio, Semarchy, Tamr) · Corp: Informatica MDM / Semarchy (EU FS shortlist; evaluation level).
- **Do:** build a mini security master: ingest two overlapping "vendor" feeds with conflicting attributes; Splink match/merge with explicit blocking + thresholds; survivorship rules in SQL; publish the golden record + cross-reference table to the lakehouse.
- **Done when:** you can walk a steward through *why* two records merged (match weights) and *why* each golden attribute won (survivorship rule), and defend registry-vs-centralized for a fund administrator.
- Est. hours: 9

#### 10.6.1 Reference data management — T2
- **Why:** code lists (countries, currencies, MICs, fund legal forms, CFI codes) are small data with outsized blast radius; RDM is governance's unglamorous core.
- **Learn:** internal vs external reference data; versioning & effective dating of code lists; distribution patterns (publish-subscribe from one source of truth); mapping tables between vendor codes; ISO list maintenance cadence (4217, 3166, 10383 MIC); ties back to SCD2 discipline from Phase 1.
- **Resource:** DAMA-DMBOK ch. 10 (reference-data half) + Collibra RDM product docs (as the corp pattern).
- **Tools:** FOSS: dbt seeds + a governed Postgres schema (↔ Collibra RDM, CluedIn).
- **Do:** build the governed code-list schema (effective-dated, approved-by, source) for currencies/countries/MICs; wire one mapping table (vendor country codes → ISO) into the silver layer.
- **Done when:** a code-list change is traceable (who/when/why) and consumed everywhere from one place.
- Est. hours: 3

#### 7.3.1 Business glossary — T2
- **Why:** "NAV", "AUM", "dealing date" mean different things across teams until the glossary pins them; glossary-to-asset linkage is what makes catalogs business-readable.
- **Learn:** term lifecycle (draft → approved, owners, stewards); term-to-asset linkage; glossary vs data dictionary vs semantic layer (and the coming convergence); seeding from regulation (AIFMD/PRIIPs definitions) vs from analytics.
- **Resource:** OpenMetadata glossary docs + DAMA-DMBOK ch. 13 (metadata, glossary sections).
- **Tools:** FOSS: OpenMetadata glossary (↔ Collibra, Purview glossary).
- **Do:** create a 25-term fund glossary (NAV, swing price, AUM, dealing cut-off, …) with owners; link every gold table column that carries one of those terms.
- **Done when:** clicking "NAV" in the catalog shows its definition, its owner, and every asset that carries it.
- Est. hours: 3

#### 1.12.6 + 3.2.6 FIBO & knowledge graphs / RDF — T2
- **Why:** FIBO is the finance ontology (EDM Council) and RDF/SPARQL is its native stack; semantic master data is a real pattern in EU regulators and large institutions.
- **Learn:** RDF triples, RDFS/OWL basics, SPARQL reading fluency; SHACL validation idea; FIBO's structure (domains: securities, funds, legal entities) and pragmatic use (vocabulary + relationships source, not a deployment mandate); property graphs vs RDF (when each); GLEIF Level-2 as a ready-made entity graph.
- **Resource:** FIBO primer at spec.edmcouncil.org + Apache Jena tutorial (RDF/SPARQL basics).
- **Tools:** FOSS: Apache Jena/Fuseki (↔ Stardog, Ontotext GraphDB, Neptune).
- **Do:** load GLEIF Level-2 ownership for 50 entities into Fuseki; SPARQL the ultimate-parent chains; map five of your security-master attributes to FIBO terms.
- **Done when:** you can say where FIBO genuinely helps (shared vocabulary, entity relationships) and where it's academic for your estate.
- Est. hours: 4

#### 11.1.2 Fine-grained access control (RLS/CLS on the platform) — T1
- **Why:** "who may see which fund's data at which column grain" is a regulatory requirement you must design *and prove* — Chinese walls between sub-funds and clients are access-control problems.
- **Learn:** RBAC→ABAC→ReBAC ladder and where each fits data; row-level security mechanics (Postgres RLS policies; warehouse equivalents) and their performance/leak caveats; column-level security & masking interplay; lakehouse access control reality (Trino/engine-level vs catalog-level enforcement; Ranger/Lake Formation/Unity models — who actually enforces at the file layer); attribute sources (Entra groups, catalog tags); access request/review workflows (recertification — an audit staple).
- **Resource:** Postgres RLS docs + Trino security docs + Unity Catalog privilege model docs (read as three enforcement archetypes).
- **Tools:** FOSS: Postgres RLS + Trino with file-based/OPA rules (↔ Immuta, Privacera, Unity Catalog, Lake Formation) · Corp: Immuta + Purview policies (evaluation level).
- **Do:** implement "TA agents see only their management company's funds" as Postgres RLS *and* as Trino rules over Iceberg; tag PII columns in the catalog and enforce CLS for a restricted role; write the recertification procedure.
- **Done when:** you can demonstrate the same policy at two enforcement layers, name where each can be bypassed, and explain the residual risk in writing.
- Est. hours: 7

#### 11.1.3 Policy-as-code (OPA) — T2
- **Why:** externalized, testable authorization is the modern answer to policy sprawl; OPA/Rego is its lingua franca and shows up across the platform (APIs, K8s, data).
- **Learn:** OPA architecture (PDP/PEP separation); Rego basics (rules, data documents); policy testing; bundles & distribution; Trino-OPA integration; Cedar as the typed alternative; where policy-as-code beats per-system grants (consistency, auditability, CI for policies).
- **Resource:** OPA docs ("Policy language" + "Philosophy") .
- **Tools:** FOSS: OPA (↔ Immuta policies, Apache Ranger, Cedar/AVP).
- **Do:** express the fund-visibility policy from 11.1.2 in Rego with unit tests; enforce it for Trino via the OPA plugin; change the policy in git and watch enforcement follow.
- **Done when:** a policy change is a reviewed PR with passing policy tests — not a ticket to three different admins.
- Est. hours: 3

#### 11.1.1 Identity providers & SSO — T2
- **Why:** every access decision starts with identity; the architect wires platforms into the IdP and reads OIDC/SAML flows fluently.
- **Learn:** OIDC flows (auth code + PKCE, client credentials for services) vs SAML; tokens (ID/access/refresh, claims, audiences); groups-to-roles mapping into data tools; SCIM provisioning; managed identities recap; Keycloak realm/client model.
- **Resource:** Keycloak docs (getting started + OIDC) + OIDC spec overview (openid.net primer).
- **Tools:** FOSS: Keycloak (↔ Entra ID, Okta) · Corp: Entra ID (primary).
- **Do:** put Keycloak in front of OpenMetadata, Grafana, and Trino (OIDC); map a "data-steward" group claim to in-tool roles.
- **Done when:** one identity, one group change, three tools' permissions move together — and you can narrate the token flow.
- Est. hours: 3

#### 11.2.1 Encryption & key management — T2
- **Why:** "who controls the keys" is the question behind every cloud-data compliance review (and the Schrems-flavored sovereignty debate).
- **Learn:** envelope encryption; KMS hierarchies (key vault → KEK → DEK); customer-managed keys (CMK) vs platform-managed — what CMK actually buys (revocation, audit) and doesn't; TLS everywhere as table stakes; key rotation mechanics; HSM tiers; client-side encryption tradeoffs for analytics (it breaks pushdown).
- **Resource:** Azure Key Vault + storage-encryption docs (CMK sections) .
- **Do:** write the key-management design for the Azure target: which stores get CMK, where keys live, rotation cadence, revocation drill.
- **Done when:** you can answer "if we revoke the key, what actually happens and how fast?" per store.
- Est. hours: 2

#### 11.3.1 + 11.3.2 Data masking & tokenization — T2
- **Why:** masking is how production-shaped data becomes usable in lower environments and how analysts see funds without seeing investors.
- **Learn:** static vs dynamic masking; technique zoo (redaction, substitution, shuffling, format-preserving encryption, tokenization with vault); referential consistency under masking (same investor → same token everywhere); warehouse-native dynamic masking; masking vs synthesis decision (ties to 9.8.1).
- **Resource:** Microsoft dynamic-data-masking docs + a tokenization-pattern overview (Skyflow/Protegrity whitepaper class — read critically).
- **Tools:** FOSS: Postgres views/functions + Presidio transforms (↔ Delphix, Protegrity, Immuta masking).
- **Do:** build the masked replica of the Phase-1 investor tables (deterministic tokenization preserving joins); prove referential integrity holds and reversibility is access-controlled.
- **Done when:** a full pipeline run on masked data produces correct aggregates with zero real PII downstream.
- Est. hours: 3

#### 11.4.1 PII detection & redaction (Presidio) — T2
- **Why:** you can't protect what you haven't found; automated PII discovery feeds classification tags that drive masking and access policy.
- **Learn:** detection approaches (regex/checksums, NER models, context words); Presidio analyzer/anonymizer pipeline; precision-recall tuning for EU identifiers (IBANs, national IDs); scanning at rest (lake) vs in motion; classification tags flowing into the catalog (ties to 10.1.1, A.18).
- **Resource:** Microsoft Presidio docs.
- **Tools:** FOSS: Presidio (↔ Macie, GCP DLP, BigID, Purview classifiers).
- **Do:** scan bronze + a synthetic free-text "client notes" set with Presidio; push findings as catalog tags; tune one recognizer (Luxembourg phone/IBAN) and measure precision change.
- **Done when:** new PII landing in bronze gets discovered, tagged, and policy-covered without a human noticing it first.
- Est. hours: 3

#### 11.6.1 Audit logging & SIEM — T2
- **Why:** "show me who accessed fund X's investor data in March" is a question you must answer from logs designed in advance, not reconstructed in panic.
- **Learn:** audit-event taxonomy for data platforms (access, policy change, export, admin); query-log capture per engine (Postgres pgAudit, Trino event listener); centralization & tamper-evidence (immutability, retention); SIEM role (correlation/alerting — Sentinel/Splunk); KQL ties (A.5); what auditors actually sample.
- **Resource:** pgAudit docs + Microsoft Sentinel overview (architecture page).
- **Tools:** FOSS: pgAudit + Trino event listener + Loki (↔ Splunk, Sentinel, Elastic SIEM).
- **Do:** enable audit capture on Postgres and Trino; ship to Loki with retention + immutability notes; answer one "who touched what when" query end-to-end.
- **Done when:** the March-access question is a five-minute query with a documented chain of custody.
- Est. hours: 2

#### 11.7.1 Regulatory & compliance frameworks (GDPR, DORA, and the fund stack) — T1
- **Why:** in Luxembourg financial services, regulation shapes architecture more than technology does — the architect translates legal obligations into platform controls.
- **Learn:** GDPR for platform builders: lawful basis, minimization, purpose limitation, DSAR/erasure in a lakehouse (delete in Iceberg, backups, event logs!), records of processing, DPIA triggers, processor chains & SCCs; DORA: ICT risk framework, incident reporting timelines, resilience testing, the register of ICT third parties and exit strategies (cloud concentration!); the fund regulatory stack at orientation level: UCITS/AIFMD (incl. Annex IV reporting), MiFID II product governance (→ EMT), PRIIPs (→ EPT/KID), SFDR (ESG data demands); CSSF expectations for cloud outsourcing (notification, audit rights — aligned to EBA/ESMA guidelines); SOC 2 / ISO 27001 as vendor-evidence vocabulary.
- **Resource:** gdpr.eu practitioner guides + the DORA regulation summary on EIOPA/ESMA sites + CSSF cloud-outsourcing circular page (orientation read; verify current circular number at assembly).
- **Tools:** Corp context: OneTrust/Vanta-class compliance platforms (awareness).
- **Do:** build the obligation→control matrix for your platform: 12 concrete obligations (e.g., "DSAR erasure within 30 days", "DORA major-incident report in 4h", "AIFMD Annex IV quarterly") each mapped to an implemented or planned control, with gaps flagged honestly.
- **Done when:** you can brief a compliance officer on how the platform meets each obligation — and where it doesn't yet — without hand-waving; the erasure path through Iceberg + backups + Kafka is concretely designed.
- Est. hours: 9

#### 1.12.12 DCAM (and leading a self-assessment) — T1
- **Why:** DCAM is the financial-services data-management capability model; architects at fund firms are expected to *lead* assessments and turn scores into roadmaps.
- **Learn:** DCAM v3 structure: 8 components, 34 capabilities, scoring on engagement/process/evidence; how assessments run (evidence-based scoring, stakeholder interviews); from scores to a sequenced capability roadmap; DCAM vs DMBOK (assessment model vs body of knowledge) and CDMC as the cloud profile (ties to A.16); what "evidence" means per capability — artifacts you've actually built in this plan.
- **Resource:** EDM Council DCAM v3 overview (framework page) + DAMA-DMBOK ch. 15 (maturity assessment) as the open companion; full DCAM is member-gated — note this in client conversations.
- **Do:** run a DCAM-style self-assessment of your capstone platform across all 8 components: score each with named evidence, then write the 12-month capability roadmap the scores imply.
- **Done when:** every score cites an artifact (catalog, lineage graph, DQ rulebook, ADR…) and the roadmap sequences capabilities by dependency, not vibes.
- Est. hours: 7

#### 9.8.1 Synthetic & test data — T2
- **Why:** privacy-preserving development is a compliance requirement (GDPR minimization) and synthetic data is its engineering answer.
- **Learn:** rule-based fakes (Faker) vs statistically-fitted synthesis (SDV: copulas/CTGAN); fidelity-privacy tradeoff (and membership-inference risk in over-fitted synthesis); referential integrity across synthesized tables; when masking beats synthesis (ties 11.3); evaluating synthetic quality (SDMetrics).
- **Resource:** SDV docs (single + multi-table synthesis).
- **Tools:** FOSS: SDV + Faker (↔ Mostly AI, Tonic, Gretel) · Corp: Mostly AI (EU; evaluation level).
- **Do:** fit SDV to the (masked) investor+orders tables; generate a synthetic dev dataset; compare aggregate fidelity vs the real data and document the privacy argument.
- **Done when:** dev/test environments run on data with a written justification of why it's safe.
- Est. hours: 3

#### 10.1.2 Enterprise catalogs (Purview, Collibra) — T2
- **Why:** the buy side of the catalog decision; Purview is the Azure default and Collibra the EU-FS incumbent — you'll evaluate or inherit one.
- **Learn:** Purview: Data Map scans, classification, glossary, policy ambitions — strengths (M365/Azure integration) and gaps (lineage depth, cost model per scanned asset); Collibra: operating-model strength (workflows, stewardship), implementation weight; catalog TCO realities (connector coverage decides everything); migration/coexistence patterns (open catalog + enterprise catalog).
- **Resource:** Purview docs (Data Map + governance overview) + Collibra resource library (architecture overview).
- **Do:** write the catalog vendor-selection memo: OpenMetadata vs Purview vs Collibra for a 300-person fund administrator — connector coverage table, TCO sketch, recommendation.
- **Done when:** the memo names the deciding factor (it's almost always connector coverage + stewardship workflow, not features).
- Est. hours: 3

#### 10.7.1 Retention & lifecycle — T2
- **Why:** regulated retention (10-year fund records) and GDPR minimization pull opposite directions; lifecycle design is where they reconcile.
- **Learn:** retention-schedule design by record class (ties A.19); storage-tier lifecycle (hot→cool→archive economics); legal hold vs deletion pipelines; Iceberg snapshot expiry vs business retention (different layers!); deletion that actually deletes (compaction, backups, logs).
- **Resource:** Azure Blob lifecycle-management docs + Iceberg `expire_snapshots` docs.
- **Do:** write the retention schedule for five record classes (orders, NAV, investor KYC, logs, EMT outputs) and implement it as MinIO lifecycle + Iceberg maintenance jobs.
- **Done when:** "when does this data actually disappear, everywhere?" has a per-class answer you can prove.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 3.2.5 | Property graph databases | Neo4j/Cypher for relationship-heavy ops use (fraud, ownership) | Neo4j "what is a graph DB" page | 25 |
| 7.3.2 | Glossary embedded in catalogs | Same discipline as 7.3.1, as a feature of Collibra/Purview | covered by 10.1.2 reading | 10 |
| 9.8.2 | Test data management | Subset/mask/refresh tooling (Delphix-class) for legacy estates | Delphix TDM overview | 20 |
| 10.2.1 | AI-native data discovery | LLM-assisted search/Q&A over catalog metadata | Atlan AI or DataHub smart-search blog | 20 |
| 10.2.2 | Catalog-embedded discovery | Search/browse UX as a catalog feature | covered by 10.1.1 hands-on | 10 |
| 10.3.2 | Lineage embedded in catalogs | Lineage as a catalog feature vs the open standard | covered by 10.1.1/10.3.1 | 10 |
| 10.5.2 | Modern/cloud MDM | ML-first MDM (Tamr) and lighter cloud MDM (Reltio) | Tamr product overview | 20 |
| 10.6.2 | RDM inside MDM suites | Code-list management bundled in MDM products | covered by 10.6.1 reading | 10 |
| 10.7.2 | Enterprise ILM suites | Heavyweight lifecycle tooling (Veritas/IBM) in legacy estates | Veritas ILM overview | 15 |
| 11.2.2 | Database encryption / TDE | At-rest encryption inside engines; table stakes, rarely a decision | SQL Server TDE docs intro | 20 |
| 11.5.1 | Privacy/consent platforms | OneTrust-class consent, DSAR automation | OneTrust product overview | 20 |
| 14.7.1 | Anomaly alerting | DQ/observability-triggered alerting; implemented via Elementary above | covered by 10.9.x hands-on | 10 |

*T3 subtotal: 3 h*

### Capstone 6 — The governed platform (catalog, lineage, DQ, policy, DCAM)

- **Goal:** wrap the entire platform in a working control plane and prove it to an imaginary auditor: every asset owned and classified, every number traceable, every access decision policy-driven, every obligation mapped.
- **Stack (100% free):** OpenMetadata (↔ Purview/Collibra), OpenLineage + Marquez (↔ Purview/Manta lineage), Soda Core + Great Expectations + Elementary (↔ Informatica DQ / Monte Carlo), Splink + Postgres security master (↔ Informatica MDM / Semarchy), Keycloak (↔ Entra ID), OPA + Trino rules + Postgres RLS (↔ Immuta/Privacera), Presidio (↔ Macie/Purview classifiers), pgAudit + Loki (↔ Sentinel/Splunk), SDV (↔ Mostly AI), Apache Jena/Fuseki FIBO/GLEIF slice (↔ Stardog/GraphDB).
- **Build:** (1) catalog ingests every platform component; owners/tiers/classifications complete for gold; (2) end-to-end lineage for the EMT path, demonstrable; (3) DQ rulebook live in the WAP gate + Elementary anomaly watch; (4) security master publishing golden records with steward-explainable merges; (5) fund-visibility policy enforced via RLS + OPA-Trino from one Rego source, identities from Keycloak; (6) PII auto-discovered → tagged → masked replica for dev; (7) audit trail answering the "March access" question; (8) the obligation→control matrix (11.7.1) and the DCAM self-assessment + roadmap (1.12.12) as governing documents.
- **Architecture deliverables:** C4 updated with the control plane; ADR-016 catalog selection (open vs Purview vs Collibra), ADR-017 enforcement architecture (where policy is decided vs enforced, and residual bypass risk), ADR-018 MDM style for the security master (registry vs centralized).
- **Acceptance criteria:** the auditor drill passes: pick any number in the EMT output → lineage to sources, owner, DQ status, access policy, and audit log, each in minutes; a seeded DQ failure blocks publish and reaches the catalog; the same policy change propagates to both enforcement layers via one PR; DCAM scores all cite artifacts; obligation matrix has zero unexamined rows (gaps allowed, but named).
- Est. hours: 16

*Phase 6 total: 120 h (T1/T2 entries 101 h + T3 3 h + capstone 16 h) + Appendix A items A.14–A.20 (14 h) scheduled in this phase*
