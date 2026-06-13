<a id="phase-6"></a>
## Phase 6: Governance, Security & Compliance (months 34–39, 120 h + 14 h Appendix A)

**Goal:** build the control plane of a regulated data platform: catalog + lineage as the metadata backbone, data quality as an engineering discipline, MDM/RDM for the entities the fund industry lives on, fine-grained access control and masking, and the regulatory frameworks (GDPR, DORA, DCAM) that decide what "good" means in Luxembourg.
**Entry prerequisites:** Phases 2–5 (a platform worth governing; OTel/observability foundations).
**Exit criteria:** you can (1) stand up a catalog with end-to-end lineage and answer an impact-analysis question from it; (2) design a DQ framework from profiling to alerting with rules tied to the six dimensions; (3) design a security-master MDM with match/merge and survivorship; (4) implement RLS/CLS and policy-as-code on the lakehouse; (5) map your platform to GDPR/DORA obligations and lead a DCAM self-assessment.
**Appendix A items scheduled here:** A.14 data strategy & operating model, A.15 architecture risk management, A.16 data risk & controls, A.17 ethics, A.18 purpose-based sharing, A.19 records management, A.20 organizational change management (14 h).

### T1/T2 topics

#### 10.1.1 Metadata management & active catalogs — T1
- **Why:** in a regulated fund platform the catalog is the control plane an architect designs first — ownership, glossary, lineage, quality, and policy all hang off it, and CSSF/DORA reviewers expect a single answer to "who owns this and what depends on it". Without an active catalog, governance lives in stale spreadsheets, impact analysis becomes guesswork, and a schema change silently breaks an EMT feed nobody knew was downstream.
- **Learn:**
  - metadata kinds — technical vs business vs operational, and active vs passive (metadata that just describes vs metadata that fires actions) *(OpenMetadata docs: Main Concepts)*
  - OpenMetadata architecture — ingestion framework, connectors, and the APIs the platform exposes *(OpenMetadata docs: Ingestion)*
  - the entity model — domains, owners, tiers, and glossary links as the governance skeleton *(OpenMetadata docs: Main Concepts)*
  - automated ingestion — pulling metadata from Postgres, Trino/Iceberg, dbt, and Kafka rather than typing it *(OpenMetadata docs: Connectors)*
  - catalog-driven workflows — announcements, tasks, and approval flows triggered from the catalog *(OpenMetadata docs: Governance)*
  - DataHub as the alternative — event-sourced metadata, also OpenLineage-friendly *(DataHub docs: Architecture)*
  - what makes metadata "active" — policies and alerts firing *from* metadata, not a separate system *(OpenMetadata docs: Main Concepts)*
- **Resources:**
  - **[OpenMetadata documentation](https://docs.open-metadata.org/)** — concepts, entity model, ingestion, and governance workflows; the hands-on backbone for this entry (primary)
  - [DataHub documentation](https://docs.datahub.com/docs/) — the event-sourced alternative; read for its metadata architecture and connector model (alternate)
- **Tools:**
  - FOSS (hands-on): [OpenMetadata](https://docs.open-metadata.org/) — the catalog you deploy and ingest into (↔ Microsoft Purview, Collibra, Alation)
  - Corp (evaluate): [Microsoft Purview](https://learn.microsoft.com/en-us/purview/) — Azure default; know its Data Map and per-asset cost model at build-vs-buy level
  - Corp (evaluate): [Collibra](https://www.collibra.com/) — EU-FS incumbent; know its operating-model/stewardship strengths
- **Do:**
  1. Deploy OpenMetadata via its Docker quickstart and confirm the UI is reachable.
  2. Configure ingestion connectors for Postgres, Trino/Iceberg, dbt, and Kafka; run each pipeline and confirm assets land.
  3. Assign an owner and a tier to every gold asset; link at least one glossary term.
  4. Wire one active workflow: a schema-change announcement that notifies registered consumers of a gold table.
- **Done when:**
  - [ ] Answer "who owns this, who consumes it, what breaks if I change it?" from the catalog in under two minutes.
  - [ ] Show every gold asset carries an owner and a tier.
  - [ ] Trigger the schema-change announcement and confirm a consumer is notified.
- Est. hours: 10

#### 10.3.1 Data lineage (OpenLineage standard) — T1
- **Why:** BCBS-239-grade traceability means every regulatory number must walk back to its sources, and lineage is the architect's impact-analysis weapon when a source column changes. Without it, an auditor's "prove this NAV figure's provenance" becomes a multi-day archaeology dig, and you cannot safely answer "what breaks if I change this column?"
- **Learn:**
  - the OpenLineage object model — runs, jobs, datasets, and facets as the extensible spine *(OpenLineage docs: Spec)*
  - emitters — Dagster, Spark, and dbt integrations that produce events automatically *(OpenLineage docs: Integrations)*
  - Marquez as the reference backend — collecting and visualising lineage events *(Marquez docs: Quickstart)*
  - column-level vs table-level lineage — what SQL parsing (dbt) gives vs what Spark instrumentation gives *(OpenLineage docs: Spec)*
  - lineage into the catalog — feeding OpenMetadata/DataHub from OpenLineage events *(OpenMetadata docs: Lineage)*
  - designing for lineage — naming and job granularity that keep graphs readable *(OpenLineage docs: Integrations)*
  - limits — black-box SaaS steps that emit nothing and how to annotate the gap *(OpenLineage docs: Spec)*
- **Resources:**
  - **[OpenLineage documentation](https://openlineage.io/docs/)** — the spec (runs/jobs/datasets/facets) plus Dagster, Spark, and dbt integrations (primary)
  - [Marquez](https://marquezproject.ai/) — the reference OpenLineage backend; getting-started and the lineage UI you will render from (reference)
  - [OpenMetadata: Lineage](https://docs.open-metadata.org/) — how lineage surfaces inside the catalog you stood up in 10.1.1 (deepening)
- **Tools:**
  - FOSS (hands-on): [OpenLineage](https://openlineage.io/docs/) + [Marquez](https://marquezproject.ai/) — emit and collect lineage, surfaced in OpenMetadata (↔ Purview lineage, Collibra lineage, Manta)
  - Corp (evaluate): [Microsoft Purview](https://learn.microsoft.com/en-us/purview/) / [Collibra](https://www.collibra.com/) lineage — know their depth and connector limits at evaluation level
- **Do:**
  1. Emit OpenLineage events from Dagster and dbt for the full NAV path (Postgres → Debezium → Iceberg → Spark → dbt → EMT output).
  2. Point the emitters at Marquez and confirm runs/jobs/datasets appear.
  3. Render end-to-end lineage for the EMT output and capture column-level detail where dbt SQL parsing allows.
  4. Answer one impact query — "which reports break if `orders.amount` changes?" — directly from the graph.
- **Done when:**
  - [ ] Demonstrate the EMT output's lineage back to source tables to an auditor, column-level where the tooling allows.
  - [ ] Trace the answer to the `orders.amount` impact query from the graph alone.
  - [ ] Identify and annotate any black-box step where lineage stops.
- Est. hours: 7

#### 9.4.2 + 10.4.1 Data quality engineering (Great Expectations / Soda) — T1
- **Why:** in regulated data, DQ rules are how "accuracy, completeness, timeliness" stop being audit prose and become enforced code that blocks a bad publish. Without engineered DQ, a wrong holdings count or a stale FX rate flows into NAV unchecked, and the architect cannot defend which checks run, at what severity, or why.
- **Learn:**
  - the six DQ dimensions — accuracy, completeness, consistency, timeliness, validity, uniqueness — mapped to executable rule types *(Data Quality Fundamentals ch. 1–4)*
  - Great Expectations — suites, checkpoints, and data docs as the rule-and-report layer *(Great Expectations docs)*
  - Soda Core — SodaCL checks and scans wired into orchestration *(Soda docs: Soda Core)*
  - dbt tests vs dedicated DQ frameworks — layering, not either/or *(Soda docs)*
  - severity & circuit-breaking — block-publish vs warn, tied to your WAP gates *(Data Quality Fundamentals ch. 4)*
  - DQ result routing — pushing pass/fail into the catalog and alerts *(Soda docs)*
  - rules from profiling, not imagination — writing checks against observed distributions *(Data Quality Fundamentals ch. 3)*
- **Resources:**
  - **[Data Quality Fundamentals (Moses, Gavish, Vorwerck)](https://www.oreilly.com/library/view/data-quality-fundamentals/9781098112035/)** ch. 1–4 — the dimensions, rule design, and severity model (primary)
  - [Soda documentation](https://docs.soda.io/) — Soda Core and SodaCL, the check syntax you wire into the WAP gate (reference)
  - [Great Expectations documentation](https://docs.greatexpectations.io/) — suites, checkpoints, and data docs as the alternate framework (alternate)
- **Tools:**
  - FOSS (hands-on): [Soda Core](https://docs.soda.io/) + [Great Expectations](https://docs.greatexpectations.io/) + [dbt tests](https://docs.getdbt.com/docs/build/data-tests) — the layered DQ stack (↔ Informatica DQ, Talend DQ)
  - Corp (evaluate): [Informatica Data Quality](https://docs.informatica.com/) — EU-FS incumbent; evaluate at build-vs-buy level
- **Do:**
  1. Define the DQ rulebook for the NAV pipeline: per dataset, rules across all six dimensions with explicit severities.
  2. Express the rules as SodaCL checks (use Great Expectations for any complex distributional check).
  3. Wire Soda scans into the WAP gate so criticals block publish and warnings page.
  4. Route results to the catalog so each failure links back to the failing expectation.
- **Done when:**
  - [ ] Trigger a seeded completeness failure that blocks publish, appears in the catalog, and pages with a link to the failing expectation.
  - [ ] Justify every rule's dimension and severity in writing.
  - [ ] Show warnings page without blocking while criticals halt the run.
- Est. hours: 10

#### 10.4.3 Data profiling — T2
- **Why:** profiling is the evidence-gathering step before DQ rules — you discover real distributions, cardinalities, and surprises in fund data rather than assuming them. Skip it and your rules encode myths (e.g. assuming an ISIN column is always populated when 2% are vendor placeholders), producing false alarms that erode trust in the DQ gate.
- **Learn:**
  - profiling outputs — distributions, null rates, uniqueness, value patterns, and drift over time *(ydata-profiling docs)*
  - ydata-profiling — one-shot exploratory profile reports from a single line *(ydata-profiling docs)*
  - whylogs — lightweight, mergeable statistical profiles for continuous monitoring *(whylogs docs: Overview)*
  - profiling as DQ-rule generator — turning observed bounds into Soda checks *(ydata-profiling docs)*
  - PII-discovery overlap — profiling surfaces candidate sensitive columns, feeding 11.4.1 *(whylogs docs: Overview)*
- **Resources:**
  - **[ydata-profiling documentation](https://docs.profiling.ydata.ai/)** — one-shot EDA reports: distributions, nulls, correlations, alerts (primary)
  - [whylogs (WhyLabs docs)](https://docs.whylabs.ai/docs/whylogs-overview/) — continuous, mergeable statistical profiles for scheduled drift checks (reference)
- **Tools:**
  - FOSS (hands-on): [ydata-profiling](https://docs.profiling.ydata.ai/) — one-shot profiles (↔ Informatica/Collibra profiling modules)
  - FOSS (hands-on): [whylogs](https://docs.whylabs.ai/docs/whylogs-overview/) — scheduled statistical profiles and diff alerting
- **Do:**
  1. Run ydata-profiling on the silver holdings table and review the alerts section.
  2. Identify the five most surprising findings (unexpected nulls, cardinality, ranges).
  3. Turn each finding into a Soda rule with the right dimension and severity.
  4. Schedule a weekly whylogs profile and configure a diff alert on drift.
- **Done when:**
  - [ ] Show at least three DQ rules that exist *because* profiling falsified an assumption.
  - [ ] Produce a weekly whylogs profile that diffs against the prior week.
- Est. hours: 3

#### 10.4.2 Managed data observability platforms — T2
- **Why:** Monte Carlo-class tools are the buy side of the DQ build-vs-buy decision, and their ML-anomaly pitch needs an architect's informed evaluation, not a sales demo's. Misjudging it means either over-paying for anomaly detection you could rule-encode, or hand-rolling freshness/volume monitoring that a managed tool would catch for less.
- **Learn:**
  - anomaly-detection-on-metadata — flagging freshness/volume/schema drift without hand-written rules *(Monte Carlo docs)*
  - incident workflow & blast radius — lineage-aware incident grouping and downstream impact *(Monte Carlo docs)*
  - pricing models — per-table/per-monitor economics at estate scale *(Monte Carlo docs)*
  - complementarity — where rule-based and anomaly-based DQ each win and lose *(Data Quality Fundamentals ch. on observability)*
- **Resources:**
  - **[Monte Carlo documentation](https://docs.getmontecarlo.com/)** — architecture and the anomaly/incident model (vendor source, read critically) (primary)
  - [Data Quality Fundamentals](https://www.oreilly.com/library/view/data-quality-fundamentals/9781098112035/) — the observability chapters as the vendor-neutral counterweight (reference)
- **Do:**
  1. Outline your current FOSS stack (Soda + Elementary) coverage by failure class.
  2. Map Monte Carlo's anomaly-detection coverage against the same failure classes.
  3. Write a half-page build-vs-buy comparison for a 200-pipeline estate, including a rough cost sketch.
- **Done when:**
  - [ ] State which failure classes anomaly detection catches that your rules never will, and vice versa.
  - [ ] Recommend build, buy, or hybrid with a one-line justification tied to estate size.
- Est. hours: 2

#### 10.9.1 + 10.9.2 Data observability (pipeline health) — T2
- **Why:** freshness/volume/schema-drift monitoring is the data plane's heartbeat, distinct from infra observability (Phase 5) and from DQ rules — it catches the silent failures that produce a NAV from yesterday's prices. Without it, a stalled Debezium connector or a shrunken load lands quietly and surfaces only when a client queries a wrong number.
- **Learn:**
  - the five data-observability pillars — freshness, volume, schema, distribution, lineage *(Data Quality Fundamentals: observability pillars)*
  - Elementary as dbt-native observability — anomaly tests and the report UI on top of your dbt project *(Elementary docs)*
  - unified alerting — routing data incidents through the same path as infra alerts *(Elementary docs)*
  - the data-incident triage runbook — who is paged, what they check, how it is resolved *(Data Quality Fundamentals: observability pillars)*
- **Resources:**
  - **[Elementary documentation](https://docs.elementary-data.com/)** — dbt-native freshness/volume/schema anomaly tests and the observability report (primary)
  - [Data Quality Fundamentals](https://www.oreilly.com/library/view/data-quality-fundamentals/9781098112035/) — the observability-pillars framing (reference)
- **Tools:**
  - FOSS (hands-on): [Elementary](https://docs.elementary-data.com/) + [OpenLineage](https://openlineage.io/docs/) events — anomaly tests plus lineage context (↔ Monte Carlo, Databand, Bigeye)
- **Do:**
  1. Add Elementary to the dbt project and run its on-run-end hooks.
  2. Enable volume and freshness anomaly tests on gold models.
  3. Route one synthetic incident (force a stale/shrunken load) through Grafana alerting with a runbook link.
  4. Assign an owner to each detector.
- **Done when:**
  - [ ] Show silent-failure classes (stale, shrunken, schema-drifted) each have a detector and an owner.
  - [ ] Fire the synthetic incident end-to-end into Grafana with a runbook link attached.
- Est. hours: 3

#### 10.5.1 Master data management — T1
- **Why:** the security/fund/counterparty master *is* the fund-industry data problem — every NAV error story ends at reference data, and the architect designs the master even when the tool is bought. Get match/merge or survivorship wrong and two vendor records for the same instrument double-count a position, or a corporate action applies to the wrong golden record and corrupts every downstream report.
- **Learn:**
  - MDM styles — registry, consolidation, coexistence, centralized — and their org costs *(DAMA-DMBOK ch. 10)*
  - match/merge — deterministic vs probabilistic (Fellegi–Sunter intuition), blocking, thresholds *(Splink docs: Fellegi-Sunter)*
  - survivorship & golden-record assembly — which source wins each attribute and why *(DAMA-DMBOK ch. 10)*
  - hierarchy management — fund → sub-fund → share class, and issuer trees *(DAMA-DMBOK ch. 10)*
  - stewardship workflow — review queues for ambiguous matches *(Splink docs)*
  - integration patterns — MDM as a publisher to the platform, not a silo *(DAMA-DMBOK ch. 10)*
  - security-master specifics — identifier cascade (ISIN/FIGI/internal), vendor precedence (Bloomberg vs Refinitiv), corporate-action survivorship *(DAMA-DMBOK ch. 10)*
- **Resources:**
  - **[DAMA-DMBOK (2nd ed.)](https://technicspub.com/dmbok/)** ch. 10 "Reference & Master Data" — MDM styles, survivorship, hierarchy management (primary)
  - [Splink documentation](https://moj-analytical-services.github.io/splink/) — probabilistic linkage, blocking, thresholds, and the Fellegi-Sunter model (MoJ open source) (reference)
- **Tools:**
  - FOSS (hands-on): [Splink](https://moj-analytical-services.github.io/splink/) for match/merge + [PostgreSQL](https://www.postgresql.org/docs/) for the hub (↔ Informatica MDM, Reltio, Semarchy, Tamr)
  - Corp (evaluate): [Informatica MDM](https://docs.informatica.com/) / [Semarchy](https://www.semarchy.com/) — EU-FS shortlist; evaluate at build-vs-buy level
- **Do:**
  1. Ingest two overlapping "vendor" feeds with conflicting attributes into Postgres.
  2. Run Splink match/merge with explicit blocking rules and tuned thresholds.
  3. Express survivorship rules in SQL to assemble the golden record.
  4. Publish the golden record plus a cross-reference table to the lakehouse.
- **Done when:**
  - [ ] Walk a steward through *why* two records merged (match weights) and *why* each golden attribute won (survivorship rule).
  - [ ] Defend registry-vs-centralized for a fund administrator in writing.
  - [ ] Produce a golden record + cross-reference table on the lakehouse.
- Est. hours: 9

#### 10.6.1 Reference data management — T2
- **Why:** code lists (countries, currencies, MICs, fund legal forms, CFI codes) are small data with outsized blast radius — one wrong currency code mis-prices a whole sub-fund. RDM is governance's unglamorous core, and without effective-dated, single-source code lists, the same "country" maps three ways across silver, gold, and the EMT feed.
- **Learn:**
  - internal vs external reference data — what you own vs what ISO/vendors publish *(DAMA-DMBOK ch. 10)*
  - versioning & effective dating — code lists that change without rewriting history *(DAMA-DMBOK ch. 10)*
  - distribution patterns — publish-subscribe from one source of truth *(DAMA-DMBOK ch. 10)*
  - mapping tables — reconciling vendor codes to your canonical codes *(DAMA-DMBOK ch. 10)*
  - ISO maintenance cadence — 4217 (currency), 3166 (country), 10383 (MIC) update rhythms *(DAMA-DMBOK ch. 10)*
  - SCD2 reuse — effective dating is the Phase-1 SCD2 discipline applied to reference data *(dbt docs: snapshots)*
- **Resources:**
  - **[DAMA-DMBOK (2nd ed.)](https://technicspub.com/dmbok/)** ch. 10 (reference-data half) — versioning, distribution, mapping patterns (primary)
  - [Collibra Reference Data Management](https://www.collibra.com/) — the corp pattern to evaluate against your FOSS build (reference)
  - [dbt snapshots](https://docs.getdbt.com/docs/build/snapshots) — SCD2 mechanics reused for effective-dated code lists (deepening)
- **Tools:**
  - FOSS (hands-on): [dbt seeds](https://docs.getdbt.com/docs/build/seeds) + a governed Postgres schema (↔ Collibra RDM, CluedIn)
- **Do:**
  1. Build a governed code-list schema (effective-dated, approved-by, source) for currencies, countries, and MICs.
  2. Load the ISO lists and record their source/version.
  3. Wire one mapping table (vendor country codes → ISO 3166) into the silver layer.
  4. Make a controlled change and confirm history is preserved.
- **Done when:**
  - [ ] Trace any code-list change to who/when/why.
  - [ ] Show the code list is consumed everywhere from one place.
- Est. hours: 3

#### 7.3.1 Business glossary — T2
- **Why:** "NAV", "AUM", and "dealing date" mean different things across teams until the glossary pins them, and glossary-to-asset linkage is what makes the catalog business-readable for compliance and front office alike. Without it, two reports labelled "AUM" disagree and nobody can say which definition is right.
- **Learn:**
  - term lifecycle — draft → approved, with owners and stewards *(OpenMetadata docs: Glossary)*
  - term-to-asset linkage — connecting a glossary term to every column that carries it *(OpenMetadata docs: Glossary)*
  - glossary vs data dictionary vs semantic layer — and the coming convergence *(DAMA-DMBOK ch. 13)*
  - seeding from regulation — AIFMD/PRIIPs definitions as authoritative term sources *(DAMA-DMBOK ch. 13)*
- **Resources:**
  - **[OpenMetadata: Glossary](https://docs.open-metadata.org/)** — term lifecycle, owners, and term-to-asset linkage (primary)
  - [DAMA-DMBOK (2nd ed.)](https://technicspub.com/dmbok/) ch. 13 (metadata/glossary sections) — glossary vs dictionary vs semantic layer (reference)
- **Tools:**
  - FOSS (hands-on): [OpenMetadata glossary](https://docs.open-metadata.org/) — the glossary you build and link (↔ Collibra, Purview glossary)
- **Do:**
  1. Create a 25-term fund glossary (NAV, swing price, AUM, dealing cut-off, …) with definitions.
  2. Assign an owner to each term.
  3. Link every gold table column that carries one of those terms to its glossary entry.
  4. Seed at least three definitions from regulation (AIFMD/PRIIPs).
- **Done when:**
  - [ ] Click "NAV" in the catalog and see its definition, its owner, and every asset that carries it.
  - [ ] Confirm all 25 terms have owners and at least one linked asset where applicable.
- Est. hours: 3

#### 1.12.6 + 3.2.6 FIBO & knowledge graphs / RDF — T2
- **Why:** FIBO is the finance ontology (EDM Council) and RDF/SPARQL is its native stack; semantic master data is a real pattern at EU regulators and large institutions, so the architect must read it fluently and judge where it earns its keep. Without that judgement you either ignore a shared vocabulary that would harmonise entity data, or over-invest in a triple store where a relational hub would do.
- **Learn:**
  - RDF triples and RDFS/OWL basics — the subject-predicate-object model and class/property vocabulary *(Apache Jena: RDF API tutorial)*
  - SPARQL reading fluency — querying a graph for paths and relationships *(Apache Jena: RDF API tutorial)*
  - SHACL validation — shape constraints over RDF, the graph analogue of DQ rules *(Apache Jena: RDF API tutorial)*
  - FIBO structure & pragmatic use — securities/funds/legal-entity domains as a vocabulary source, not a deployment mandate *(FIBO spec site)*
  - property graphs vs RDF — when Cypher/Neo4j beats triples and vice versa *(Apache Jena: RDF API tutorial)*
  - GLEIF Level-2 as a ready-made entity graph — "who owns whom" ownership relationships *(GLEIF: Level 2 data)*
- **Resources:**
  - **[FIBO (spec.edmcouncil.org)](https://spec.edmcouncil.org/fibo/)** — the finance ontology: structure, vocabulary, and the data dictionary (primary)
  - [Apache Jena: RDF API tutorial](https://jena.apache.org/tutorials/rdf_api.html) — RDF/SPARQL basics and the model API for the hands-on lab (reference)
  - [GLEIF Level 2: Who Owns Whom](https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-2-data-who-owns-whom) — the open ownership dataset you load and query (deepening)
- **Tools:**
  - FOSS (hands-on): [Apache Jena / Fuseki](https://jena.apache.org/documentation/fuseki2/) — triple store and SPARQL endpoint (↔ Stardog, Ontotext GraphDB, Neptune)
- **Do:**
  1. Load GLEIF Level-2 ownership for 50 entities into Fuseki.
  2. Write a SPARQL query that walks the ultimate-parent chains.
  3. Map five of your security-master attributes to FIBO terms.
  4. Note one constraint you could express as SHACL.
- **Done when:**
  - [ ] Return ultimate-parent chains for the loaded entities via SPARQL.
  - [ ] Say where FIBO genuinely helps (shared vocabulary, entity relationships) and where it's academic for your estate.
- Est. hours: 4

#### 11.1.2 Fine-grained access control (RLS/CLS on the platform) — T1
- **Why:** "who may see which fund's data at which column grain" is a regulatory requirement you must design *and prove* — Chinese walls between sub-funds and clients are access-control problems, and CSSF/GDPR reviewers will test them. Get RLS/CLS wrong and a TA agent sees another management company's investors, a reportable breach that no after-the-fact apology undoes.
- **Learn:**
  - the RBAC→ABAC→ReBAC ladder — where each authorization model fits data access *(OPA docs: Introduction)*
  - row-level security mechanics — Postgres RLS policies and their performance/leak caveats *(Postgres docs: Row Security Policies)*
  - column-level security & masking interplay — restricting columns vs obscuring values *(SQL Server: Dynamic Data Masking)*
  - lakehouse enforcement reality — engine-level (Trino) vs catalog-level (Unity) vs file-layer enforcement *(Trino docs: Security)*
  - the Unity/Ranger/Lake Formation models — who actually enforces at the file layer *(Unity Catalog: privileges reference)*
  - attribute sources — Entra groups and catalog tags driving ABAC decisions *(Trino docs: Security)*
  - access request/review workflows — recertification, an audit staple *(Postgres docs: Row Security Policies)*
- **Resources:**
  - **[PostgreSQL: Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)** — RLS policy mechanics and caveats, the first enforcement archetype (primary)
  - [Trino: Security](https://trino.io/docs/current/security.html) — file-based and OPA access control over Iceberg, the engine-level archetype (reference)
  - [Unity Catalog: privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/privileges) — the catalog-level privilege model, the third archetype (deepening)
- **Tools:**
  - FOSS (hands-on): [PostgreSQL RLS](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) + [Trino](https://trino.io/docs/current/security.html) with file-based/OPA rules (↔ Immuta, Privacera, Unity Catalog, Lake Formation)
  - Corp (evaluate): [Immuta](https://documentation.immuta.com/) + [Microsoft Purview](https://learn.microsoft.com/en-us/purview/) policies — evaluate at build-vs-buy level
- **Do:**
  1. Implement "TA agents see only their management company's funds" as Postgres RLS policies.
  2. Implement the same rule as Trino file-based/OPA rules over Iceberg.
  3. Tag PII columns in the catalog and enforce column-level security for a restricted role.
  4. Write the recertification procedure (who reviews access, how often, evidence captured).
- **Done when:**
  - [ ] Demonstrate the same policy at two enforcement layers (Postgres and Trino).
  - [ ] Name where each layer can be bypassed and explain the residual risk in writing.
  - [ ] Show the restricted role sees masked/withheld PII columns.
- Est. hours: 7

#### 11.1.3 Policy-as-code (OPA) — T2
- **Why:** externalized, testable authorization is the modern answer to policy sprawl, and OPA/Rego is its lingua franca across APIs, Kubernetes, and data engines. Without it, the fund-visibility rule lives in three places that drift apart, and changing it becomes three tickets to three admins with no test that the change is correct.
- **Learn:**
  - OPA architecture — PDP/PEP separation (decide vs enforce) *(OPA docs: Philosophy)*
  - Rego basics — rules and data documents as the policy language *(OPA docs: Policy Language)*
  - policy testing — unit tests that prove a policy allows/denies the right cases *(OPA docs: Policy Language)*
  - bundles & distribution — shipping policy to PEPs reproducibly *(OPA docs: Introduction)*
  - Trino-OPA integration — enforcing data access via the OPA plugin *(Trino docs: Security)*
  - Cedar as the typed alternative — when a typed policy language is preferable *(OPA docs: Philosophy)*
  - where policy-as-code wins — consistency, auditability, and CI for policies vs per-system grants *(OPA docs: Philosophy)*
- **Resources:**
  - **[Open Policy Agent documentation](https://www.openpolicyagent.org/docs/)** — Rego, the PDP/PEP philosophy, and policy testing (primary)
  - [Trino: Security](https://trino.io/docs/current/security.html) — the OPA access-control plugin you wire to enforcement (reference)
- **Tools:**
  - FOSS (hands-on): [OPA](https://www.openpolicyagent.org/docs/) — the policy engine and Rego (↔ Immuta policies, Apache Ranger, Cedar/AVP)
- **Do:**
  1. Express the fund-visibility policy from 11.1.2 in Rego.
  2. Write unit tests covering allow and deny cases.
  3. Enforce the policy for Trino via the OPA plugin.
  4. Change the policy in git, run tests, and watch enforcement follow.
- **Done when:**
  - [ ] Make a policy change as a reviewed PR with passing policy tests, not a ticket to three admins.
  - [ ] Show Trino enforcement reflects the latest Rego bundle.
- Est. hours: 3

#### 11.1.1 Identity providers & SSO — T2
- **Why:** every access decision starts with identity, so the architect wires platforms into the IdP and reads OIDC/SAML flows fluently. Get this wrong and group changes don't propagate, leavers keep access, and the audit question "who could see this in March?" has no defensible answer.
- **Learn:**
  - OIDC flows — auth code + PKCE for users, client credentials for services — vs SAML *(OpenID: How Connect Works)*
  - tokens — ID/access/refresh, claims, and audiences *(OpenID: How Connect Works)*
  - groups-to-roles mapping — turning an IdP group claim into in-tool roles *(Keycloak docs)*
  - SCIM provisioning — automated user lifecycle into downstream tools *(Keycloak docs)*
  - managed identities recap — service-to-service auth without secrets *(Keycloak docs)*
  - Keycloak realm/client model — the FOSS IdP's core objects *(Keycloak docs)*
- **Resources:**
  - **[Keycloak documentation](https://www.keycloak.org/documentation)** — realms, clients, OIDC, and group/role mapping for the hands-on lab (primary)
  - [OpenID Connect: How Connect Works](https://openid.net/developers/how-connect-works/) — the OIDC flow and token primer (reference)
- **Tools:**
  - FOSS (hands-on): [Keycloak](https://www.keycloak.org/documentation) — the IdP in front of your tools (↔ Entra ID, Okta)
  - Corp (evaluate): [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/) — the Azure primary IdP
- **Do:**
  1. Stand up Keycloak with a realm and clients for OpenMetadata, Grafana, and Trino (OIDC).
  2. Configure each tool to authenticate via Keycloak.
  3. Create a "data-steward" group and map its claim to in-tool roles.
  4. Add a user to the group and confirm all three tools update.
- **Done when:**
  - [ ] Move one identity's permissions across three tools with one group change.
  - [ ] Narrate the auth-code+PKCE token flow end to end.
- Est. hours: 3

#### 11.2.1 Encryption & key management — T2
- **Why:** "who controls the keys" is the question behind every cloud-data compliance review and the Schrems-flavoured sovereignty debate that EU fund firms must answer. Get key management wrong and either you cannot prove data is protected at rest, or a revoked key bricks a store you didn't realise depended on it.
- **Learn:**
  - envelope encryption — DEKs wrapped by KEKs wrapped by a vault key *(Practical Cloud Security: encryption)*
  - KMS hierarchies — key vault → KEK → DEK and where each lives *(Azure Key Vault docs)*
  - CMK vs platform-managed keys — what customer-managed keys actually buy (revocation, audit) and don't *(Azure Key Vault docs)*
  - TLS everywhere — encryption in transit as table stakes *(Azure Key Vault docs)*
  - key rotation mechanics — automated rotation and its blast radius *(Azure Key Vault docs)*
  - HSM tiers — Managed HSM vs standard vault for higher assurance *(Azure Key Vault docs)*
  - client-side encryption tradeoffs — it breaks query pushdown for analytics *(Azure Key Vault docs)*
- **Resources:**
  - **[Azure Key Vault documentation](https://learn.microsoft.com/en-us/azure/key-vault/)** — keys, secrets, CMK, rotation, and Managed HSM (primary)
  - [Practical Cloud Security, 2nd ed.](https://www.oreilly.com/library/view/practical-cloud-security/9781098148171/) — vendor-neutral envelope encryption, KMS hierarchies, and key-management practice (reference)
- **Do:**
  1. Inventory which Azure stores hold which data classes.
  2. Decide which stores get CMK vs platform-managed keys and justify each.
  3. Specify where keys live, rotation cadence, and the revocation drill.
  4. Document the analytics impact of any client-side encryption choice.
- **Done when:**
  - [ ] Answer "if we revoke the key, what actually happens and how fast?" per store.
  - [ ] Defend each CMK-vs-platform-managed decision in writing.
- Est. hours: 2

#### 11.3.1 + 11.3.2 Data masking & tokenization — T2
- **Why:** masking is how production-shaped fund data becomes usable in lower environments and how analysts see funds without seeing investors — a GDPR minimization requirement. Without referentially-consistent masking, dev runs on real PII (a breach) or on randomised data whose broken joins make every test result meaningless.
- **Learn:**
  - static vs dynamic masking — masking at rest vs masking in the query result *(SQL Server: Dynamic Data Masking)*
  - the technique zoo — redaction, substitution, shuffling, format-preserving encryption, vault tokenization *(Presidio docs)*
  - referential consistency — same investor → same token everywhere so joins survive *(Presidio docs)*
  - warehouse-native dynamic masking — built-in column masking and its inference limits *(SQL Server: Dynamic Data Masking)*
  - masking vs synthesis — when to mask vs generate synthetic data (ties 9.8.1) *(Presidio docs)*
- **Resources:**
  - **[SQL Server: Dynamic Data Masking](https://learn.microsoft.com/en-us/sql/relational-databases/security/dynamic-data-masking)** — warehouse-native dynamic masking, functions, and its inference caveats (primary)
  - [Microsoft Presidio](https://microsoft.github.io/presidio/) — anonymizer operators for deterministic tokenization and the technique zoo (reference)
- **Tools:**
  - FOSS (hands-on): [PostgreSQL](https://www.postgresql.org/docs/) views/functions + [Presidio](https://microsoft.github.io/presidio/) transforms (↔ Delphix, Protegrity, Immuta masking)
- **Do:**
  1. Build a masked replica of the Phase-1 investor tables using deterministic tokenization.
  2. Confirm the same investor maps to the same token across tables.
  3. Prove cross-table joins still resolve on masked data.
  4. Access-control the reversibility (only an authorised role can de-tokenize).
- **Done when:**
  - [ ] Run a full pipeline on masked data and produce correct aggregates with zero real PII downstream.
  - [ ] Demonstrate referential integrity holds and reversibility is access-controlled.
- Est. hours: 3

#### 11.4.1 PII detection & redaction (Presidio) — T2
- **Why:** you can't protect what you haven't found, and automated PII discovery feeds the classification tags that drive masking and access policy. Without it, free-text "client notes" or a new bronze feed lands with un-tagged national IDs and IBANs, and your masking/policy layer never knows to cover them.
- **Learn:**
  - detection approaches — regex/checksums, NER models, and context words *(Presidio docs)*
  - the analyzer/anonymizer pipeline — detect entities, then de-identify them *(Presidio docs)*
  - precision-recall tuning — adjusting recognizers for EU identifiers (IBANs, national IDs) *(Presidio docs)*
  - at-rest vs in-motion scanning — lake scans vs stream interception *(Presidio docs)*
  - classification tags into the catalog — findings flowing to OpenMetadata (ties 10.1.1, A.18) *(OpenMetadata docs: Governance)*
- **Resources:**
  - **[Microsoft Presidio documentation](https://microsoft.github.io/presidio/)** — analyzer/anonymizer, custom recognizers, and tuning (primary)
  - [OpenMetadata: Governance](https://docs.open-metadata.org/) — pushing PII findings as catalog classification tags (reference)
- **Tools:**
  - FOSS (hands-on): [Presidio](https://microsoft.github.io/presidio/) — PII detection and redaction (↔ Macie, GCP DLP, BigID, Purview classifiers)
- **Do:**
  1. Scan bronze plus a synthetic free-text "client notes" set with Presidio.
  2. Push findings as classification tags into the catalog.
  3. Tune one recognizer (Luxembourg phone or IBAN) and measure the precision change.
  4. Confirm tagged columns are picked up by the masking/access layer.
- **Done when:**
  - [ ] Show new PII landing in bronze gets discovered, tagged, and policy-covered without a human noticing it first.
  - [ ] Report the precision change from the tuned recognizer.
- Est. hours: 3

#### 11.6.1 Audit logging & SIEM — T2
- **Why:** "show me who accessed fund X's investor data in March" is a question you must answer from logs designed in advance, not reconstructed in panic during a CSSF inquiry. Without a planned audit taxonomy and tamper-evident retention, the answer is a forensic guess that satisfies no auditor.
- **Learn:**
  - audit-event taxonomy — access, policy change, export, admin events for a data platform *(pgAudit docs)*
  - per-engine query-log capture — Postgres pgAudit and the Trino event listener *(pgAudit docs)*
  - centralization & tamper-evidence — immutability and retention guarantees *(Microsoft Sentinel docs)*
  - the SIEM role — correlation and alerting in Sentinel/Splunk *(Microsoft Sentinel docs)*
  - KQL ties — querying centralized logs (ties A.5) *(Microsoft Sentinel docs)*
  - what auditors actually sample — the access and change events they request *(pgAudit docs)*
- **Resources:**
  - **[pgAudit](https://github.com/pgaudit/pgaudit)** — session and object audit logging for Postgres, the capture layer (primary)
  - [Microsoft Sentinel overview](https://learn.microsoft.com/en-us/azure/sentinel/overview) — the SIEM role: correlation, immutability, and KQL (reference)
- **Tools:**
  - FOSS (hands-on): [pgAudit](https://github.com/pgaudit/pgaudit) + [Trino event listener](https://trino.io/docs/current/develop/event-listener.html) + [Loki](https://grafana.com/docs/loki/latest/) (↔ Splunk, Sentinel, Elastic SIEM)
- **Do:**
  1. Enable pgAudit on Postgres and the event listener on Trino.
  2. Ship both audit streams to Loki with documented retention and immutability notes.
  3. Define the audit-event taxonomy you capture.
  4. Answer one "who touched what when" query end to end.
- **Done when:**
  - [ ] Make the March-access question a five-minute query with a documented chain of custody.
  - [ ] Show audit retention and immutability are configured and recorded.
- Est. hours: 2

#### 11.7.1 Regulatory & compliance frameworks (GDPR, DORA, and the fund stack) — T1
- **Why:** in Luxembourg financial services, regulation shapes architecture more than technology does, and the architect translates legal obligations into platform controls. Miss an obligation — an un-erasable record in Iceberg snapshots, a DORA incident path with no 4-hour reporting hook — and the platform is non-compliant by design, discovered only under examination.
- **Learn:**
  - GDPR for platform builders — lawful basis, minimization, purpose limitation, DSAR/erasure across Iceberg + backups + event logs, RoPA, DPIA triggers, processor chains & SCCs *(gdpr.eu guides)*
  - DORA — ICT risk framework, incident-reporting timelines, resilience testing, the ICT third-party register and exit strategies (cloud concentration) *(EIOPA: DORA)*
  - the fund regulatory stack — UCITS/AIFMD (incl. Annex IV), MiFID II product governance (→ EMT), PRIIPs (→ EPT/KID), SFDR (ESG data) at orientation level *(EIOPA: DORA)*
  - CSSF cloud-outsourcing expectations — notification and audit rights, aligned to EBA/ESMA guidelines (verify current circular at assembly) *(CSSF regulatory framework)*
  - SOC 2 / ISO 27001 — the vendor-evidence vocabulary you read in supplier reviews *(gdpr.eu guides)*
- **Resources:**
  - **[gdpr.eu](https://gdpr.eu/)** — practitioner guides on lawful basis, minimization, DSAR/erasure, and RoPA (primary)
  - [EIOPA: Digital Operational Resilience Act (DORA)](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) — ICT risk, incident reporting, and third-party register (reference)
  - [CSSF regulatory framework](https://www.cssf.lu/en/regulatory-framework/) — cloud-outsourcing circular (verify current circular number at assembly) (deepening)
- **Tools:**
  - Corp (awareness): [OneTrust](https://www.onetrust.com/) / Vanta-class compliance platforms — what they automate (RoPA, DSAR), at awareness level
- **Do:**
  1. List 12 concrete obligations spanning GDPR, DORA, and the fund stack (e.g. "DSAR erasure within 30 days", "DORA major-incident report in 4h", "AIFMD Annex IV quarterly").
  2. Map each obligation to an implemented or planned control on your platform.
  3. Design the erasure path concretely through Iceberg (snapshot expiry/compaction), backups, and Kafka.
  4. Flag gaps honestly where no control exists yet.
- **Done when:**
  - [ ] Brief a compliance officer on how the platform meets each obligation — and where it doesn't yet — without hand-waving.
  - [ ] Show the erasure path through Iceberg + backups + Kafka is concretely designed.
- Est. hours: 9

#### 1.12.12 DCAM (and leading a self-assessment) — T1
- **Why:** DCAM is the financial-services data-management capability model, and architects at fund firms are expected to *lead* assessments and turn scores into roadmaps the board funds. Without the ability to run an evidence-based DCAM assessment, "are we mature?" gets answered by opinion, and the resulting roadmap sequences work by politics rather than dependency.
- **Learn:**
  - DCAM v3 structure — 8 components and the required capabilities, scored on engagement/process/evidence *(EDM Council: DCAM)*
  - how assessments run — evidence-based scoring and stakeholder interviews *(EDM Council: DCAM)*
  - scores to roadmap — sequencing capabilities by dependency *(DAMA-DMBOK ch. 15)*
  - DCAM vs DMBOK — assessment model vs body of knowledge, with CDMC as the cloud profile (ties A.16) *(EDM Council: DCAM)*
  - what "evidence" means — the catalog/lineage/DQ artifacts you actually built in this plan *(DAMA-DMBOK ch. 15)*
- **Resources:**
  - **[EDM Council: DCAM](https://www.edmcouncil.org/frameworks/dcam)** — the v3 framework: components, capabilities, and the engagement/process/evidence scoring model (primary)
  - [DAMA-DMBOK (2nd ed.)](https://technicspub.com/dmbok/) ch. 15 (maturity assessment) — the open companion on running maturity assessments (reference)
- **Do:**
  1. Score your capstone platform across all 8 DCAM components, citing named evidence per capability.
  2. Use engagement/process/evidence dimensions consistently.
  3. Derive the 12-month capability roadmap the scores imply.
  4. Sequence the roadmap by dependency, not by ease.
- **Done when:**
  - [ ] Cite an artifact (catalog, lineage graph, DQ rulebook, ADR…) for every score.
  - [ ] Show the roadmap sequences capabilities by dependency, not vibes.
- Est. hours: 7

#### 9.8.1 Synthetic & test data — T2
- **Why:** privacy-preserving development is a GDPR minimization requirement, and synthetic data is its engineering answer when masking alone isn't enough. Over-fit synthesis leaks via membership inference, and broken referential integrity across synthesized tables makes the dev dataset useless — so the architect must own the fidelity-privacy tradeoff.
- **Learn:**
  - rule-based vs fitted synthesis — Faker fakes vs SDV statistical models (copulas/CTGAN) *(SDV docs)*
  - the fidelity-privacy tradeoff — and membership-inference risk in over-fitted synthesis *(SDV docs)*
  - referential integrity — multi-table synthesis that preserves keys across tables *(SDV docs)*
  - masking vs synthesis — when masking is the safer/simpler choice (ties 11.3) *(SDV docs)*
  - evaluating synthetic quality — fidelity/privacy metrics (SDMetrics) *(SDMetrics docs)*
- **Resources:**
  - **[SDV (Synthetic Data Vault) documentation](https://docs.sdv.dev/sdv/)** — single- and multi-table synthesis, synthesizers, and quality evaluation (primary)
  - [SDMetrics documentation](https://docs.sdv.dev/sdmetrics/) — fidelity and privacy metrics for evaluating synthetic data quality (reference)
- **Tools:**
  - FOSS (hands-on): [SDV](https://docs.sdv.dev/sdv/) + [Faker](https://faker.readthedocs.io/) — fitted synthesis plus rule-based fakes (↔ Mostly AI, Tonic, Gretel)
  - Corp (evaluate): [MOSTLY AI](https://mostly.ai/) — EU synthetic-data vendor; evaluate at build-vs-buy level
- **Do:**
  1. Fit an SDV multi-table synthesizer to the (masked) investor + orders tables.
  2. Generate a synthetic dev dataset preserving referential integrity.
  3. Compare aggregate fidelity against the real data with SDMetrics.
  4. Write the privacy argument (why it's safe to use in dev/test).
- **Done when:**
  - [ ] Run dev/test environments on data with a written justification of why it's safe.
  - [ ] Show referential integrity holds across the synthesized tables.
- Est. hours: 3

#### 10.1.2 Enterprise catalogs (Purview, Collibra) — T2
- **Why:** the buy side of the catalog decision matters because Purview is the Azure default and Collibra the EU-FS incumbent — you'll evaluate or inherit one and must judge it past the demo. Choose on features rather than connector coverage and stewardship workflow, and you buy a catalog that can't see half your estate or that nobody maintains.
- **Learn:**
  - Purview — Data Map scans, classification, glossary, and policy ambitions; M365/Azure integration strengths and lineage/cost gaps *(Microsoft Purview docs)*
  - Collibra — operating-model strength (workflows, stewardship) and implementation weight *(Collibra site)*
  - catalog TCO realities — connector coverage decides everything *(Microsoft Purview docs)*
  - migration/coexistence — open catalog alongside an enterprise catalog *(Collibra site)*
- **Resources:**
  - **[Microsoft Purview documentation](https://learn.microsoft.com/en-us/purview/)** — Data Map, classification, and the governance overview (primary)
  - [Collibra](https://www.collibra.com/) — operating model, stewardship workflows, and architecture overview (reference)
- **Do:**
  1. Build a connector-coverage table for your estate across OpenMetadata, Purview, and Collibra.
  2. Sketch a TCO comparison for a 300-person fund administrator.
  3. Write the vendor-selection memo with a clear recommendation.
- **Done when:**
  - [ ] Name the deciding factor (almost always connector coverage + stewardship workflow, not features).
  - [ ] Produce a memo a sponsor could act on.
- Est. hours: 3

#### 10.7.1 Retention & lifecycle — T2
- **Why:** regulated retention (10-year fund records) and GDPR minimization pull in opposite directions, and lifecycle design is where the architect reconciles them. Without per-class retention that actually deletes across snapshots, backups, and logs, you either keep PII too long (GDPR breach) or expire records a regulator still expects (CSSF breach).
- **Learn:**
  - retention-schedule design by record class — orders vs NAV vs KYC vs logs (ties A.19) *(Azure Blob lifecycle docs)*
  - storage-tier lifecycle — hot → cool → archive economics *(Azure Blob lifecycle docs)*
  - legal hold vs deletion pipelines — suspending deletion when required *(Azure Blob lifecycle docs)*
  - Iceberg snapshot expiry vs business retention — different layers, different controls *(Iceberg docs: expire_snapshots)*
  - deletion that actually deletes — compaction, backups, and logs all cleared *(Iceberg docs: expire_snapshots)*
- **Resources:**
  - **[Azure Blob: lifecycle management](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)** — tiering and deletion policies by rule (primary)
  - [Apache Iceberg: expire_snapshots](https://iceberg.apache.org/docs/latest/spark-procedures/) — snapshot expiry and table maintenance procedures (reference)
- **Tools:**
  - FOSS (hands-on): [MinIO lifecycle](https://min.io/docs/minio/linux/administration/object-management/object-lifecycle-management.html) + [Iceberg maintenance](https://iceberg.apache.org/docs/latest/maintenance/) — tiering and snapshot expiry
- **Do:**
  1. Write the retention schedule for five record classes (orders, NAV, investor KYC, logs, EMT outputs).
  2. Implement it as MinIO lifecycle rules plus Iceberg maintenance jobs (expire_snapshots, remove orphan files).
  3. Account for legal hold and for deletion across backups and logs.
- **Done when:**
  - [ ] Answer "when does this data actually disappear, everywhere?" with a per-class answer you can prove.
  - [ ] Show Iceberg snapshot expiry and storage-tier rules are both configured.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 3.2.5 | Property graph databases | Neo4j/Cypher for relationship-heavy ops use (fraud rings, ownership chains) | [Neo4j: Getting Started](https://neo4j.com/docs/getting-started/current/) | 25 |
| 7.3.2 | Glossary embedded in catalogs | Same discipline as 7.3.1, delivered as a feature of Collibra/Purview | [covered by 10.1.2 reading](https://learn.microsoft.com/en-us/purview/) | 10 |
| 9.8.2 | Test data management | Subset/mask/refresh tooling (Delphix-class) for legacy estates | [Delphix (Perforce) test data management](https://www.perforce.com/products/delphix) | 20 |
| 10.2.1 | AI-native data discovery | LLM-assisted search and Q&A over catalog metadata | [Atlan AI](https://atlan.com/atlan-ai/) | 20 |
| 10.2.2 | Catalog-embedded discovery | Search/browse UX delivered as a catalog feature | [covered by 10.1.1 hands-on](https://docs.open-metadata.org/) | 10 |
| 10.3.2 | Lineage embedded in catalogs | Lineage as a catalog feature vs the open OpenLineage standard | [covered by 10.1.1/10.3.1](https://openlineage.io/docs/) | 10 |
| 10.5.2 | Modern/cloud MDM | ML-first MDM (Tamr) and lighter cloud MDM (Reltio) | [Tamr product overview](https://www.tamr.com/) | 20 |
| 10.6.2 | RDM inside MDM suites | Code-list management bundled into MDM products | [covered by 10.6.1 reading](https://technicspub.com/dmbok/) | 10 |
| 10.7.2 | Enterprise ILM suites | Heavyweight lifecycle tooling (Veritas/IBM) in legacy estates | [Veritas information lifecycle](https://www.veritas.com/) | 15 |
| 11.2.2 | Database encryption / TDE | At-rest encryption inside the engine; table stakes, rarely a decision | [SQL Server: Transparent Data Encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption) | 20 |
| 11.5.1 | Privacy/consent platforms | OneTrust-class consent and DSAR automation | [OneTrust product overview](https://www.onetrust.com/) | 20 |
| 14.7.1 | Anomaly alerting | DQ/observability-triggered alerting; implemented via Elementary above | [covered by 10.9.x hands-on](https://docs.elementary-data.com/) | 10 |

*T3 subtotal: 3 h*

### Capstone 6 — The governed platform (catalog, lineage, DQ, policy, DCAM)

- **Goal:** wrap the entire platform in a working control plane and prove it to an imaginary auditor: every asset owned and classified, every number traceable, every access decision policy-driven, every obligation mapped.
- **Stack (100% free):** [OpenMetadata](https://docs.open-metadata.org/) (↔ Purview/Collibra), [OpenLineage](https://openlineage.io/docs/) + [Marquez](https://marquezproject.ai/) (↔ Purview/Manta lineage), [Soda Core](https://docs.soda.io/) + [Great Expectations](https://docs.greatexpectations.io/) + [Elementary](https://docs.elementary-data.com/) (↔ Informatica DQ / Monte Carlo), [Splink](https://moj-analytical-services.github.io/splink/) + [Postgres](https://www.postgresql.org/docs/) security master (↔ Informatica MDM / Semarchy), [Keycloak](https://www.keycloak.org/documentation) (↔ Entra ID), [OPA](https://www.openpolicyagent.org/docs/) + [Trino rules](https://trino.io/docs/current/security.html) + [Postgres RLS](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) (↔ Immuta/Privacera), [Presidio](https://microsoft.github.io/presidio/) (↔ Macie/Purview classifiers), [pgAudit](https://github.com/pgaudit/pgaudit) + [Loki](https://grafana.com/docs/loki/latest/) (↔ Sentinel/Splunk), [SDV](https://docs.sdv.dev/sdv/) (↔ Mostly AI), [Apache Jena/Fuseki](https://jena.apache.org/documentation/fuseki2/) FIBO/GLEIF slice (↔ Stardog/GraphDB).
- **Build:** (1) catalog ingests every platform component; owners/tiers/classifications complete for gold; (2) end-to-end lineage for the EMT path, demonstrable; (3) DQ rulebook live in the WAP gate + Elementary anomaly watch; (4) security master publishing golden records with steward-explainable merges; (5) fund-visibility policy enforced via RLS + OPA-Trino from one Rego source, identities from Keycloak; (6) PII auto-discovered → tagged → masked replica for dev; (7) audit trail answering the "March access" question; (8) the obligation→control matrix (11.7.1) and the DCAM self-assessment + roadmap (1.12.12) as governing documents.
- **Architecture deliverables:** C4 updated with the control plane; ADR-016 catalog selection (open vs Purview vs Collibra), ADR-017 enforcement architecture (where policy is decided vs enforced, and residual bypass risk), ADR-018 MDM style for the security master (registry vs centralized).
- **Acceptance criteria:** the auditor drill passes: pick any number in the EMT output → lineage to sources, owner, DQ status, access policy, and audit log, each in minutes; a seeded DQ failure blocks publish and reaches the catalog; the same policy change propagates to both enforcement layers via one PR; DCAM scores all cite artifacts; obligation matrix has zero unexamined rows (gaps allowed, but named). Capture each as evidence (screenshots/queries) for the DCAM pack.
- Est. hours: 16

*Phase 6 total: 120 h (T1/T2 entries 101 h + T3 3 h + capstone 16 h) + Appendix A items A.14–A.20 (14 h) scheduled in this phase*
