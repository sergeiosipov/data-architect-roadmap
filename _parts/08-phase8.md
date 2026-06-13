<a id="phase-8"></a>
## Phase 8: Data Products, Semantic Layer & the Architect's Practice (months 44–48, 103 h + 18.5 h Appendix A)

*Phase 8 of 8 · months 44–48 · 121.5 h (103 h + 18.5 h Appendix A) · capstone: Productized fund data product.*  ← [Phase 7](#phase-7) · finish →

**Goal:** convert the governed platform into *products* — contracted, SLA-backed, semantically defined, consumable — and consolidate the formal architect's practice: DDD for boundaries, TOGAF/ArchiMate for the enterprise conversation, regulatory reporting as the domain's flagship deliverable, and the build-vs-buy fluency that Appendix D distills.
**Entry prerequisites:** Phases 1–7 (everything; this phase productizes the accumulated platform).
**Exit criteria:** you can (1) cut data-product boundaries with DDD and defend them; (2) publish a data product with an enforced contract, SLOs, and a semantic layer; (3) design a submission-grade regulatory reporting pipeline; (4) speak TOGAF/ArchiMate fluently in an EA forum; (5) win a build-vs-buy argument in any taxonomy domain with named tools and costs.
**Appendix A items scheduled here:** A.7 architecture styles & trade-off analysis, A.8 business architecture, A.9 EA governance, A.10 roadmapping & migration planning, A.11 agile EA, A.12 OWASP API security, A.13 ITSM/delivery frameworks (18.5 h).

### T1/T2 topics

#### 8.4.1 Domain-driven design — T1
- **Why:** Bounded contexts are how a data architect cuts product and team boundaries that survive reorgs — strategic DDD is the intellectual foundation under data mesh, and the difference between domain-oriented design and folder renaming. Without it, "NAV" means three different things in three systems, integrations rot into a big ball of mud, and every reorg redraws your data landscape along org-chart lines instead of domain lines.
- **Learn:**
  - ubiquitous language — one term, one precise meaning *inside* a context; why "NAV" in fund accounting and "NAV" in client reporting are legitimately different objects *(Learning DDD ch. 2)*
  - bounded contexts — boundaries of language and model consistency, not deployment units; how to spot one in conversation *(Learning DDD ch. 3)*
  - context mapping — partnership, customer–supplier, conformist, anticorruption layer, published language, separate ways, and what each implies for data flows *(Learning DDD ch. 4)*
  - subdomain types — core/supporting/generic and the investment logic that follows: build the core, buy the generic *(Learning DDD ch. 1)*
  - EventStorming — big-picture workshop mechanics (domain events, hotspots, pivotal events): your BA superpower, formalized *(Learning DDD ch. 12)*
  - aggregates at concept level — the consistency-boundary idea you need for design reviews, without the tactical code patterns *(Learning DDD ch. 6)*
  - applying DDD to data — source-aligned vs aggregate vs consumer-aligned data products, and which context owns which *(Data Mesh ch. 2)*
  - the fund-administration domain map — TA, fund accounting, custody, regulatory reporting, client reporting as candidate contexts, with EMT/EPT as published languages *(Learning DDD ch. 4, applied)*
- **Resources:**
  - **[Learning Domain-Driven Design](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/) (Khononov), strategic chapters 1–11 plus ch. 12 on EventStorming** — ubiquitous language, bounded contexts, context mapping, subdomains, aggregates (primary)
  - [Data Mesh](https://www.oreilly.com/library/view/data-mesh/9781492092384/) (Dehghani) ch. 2 — domain ownership and the data-product alignment types (the data application)
  - [Domain Language — Eric Evans](https://www.domainlanguage.com/) — the original DDD source and free DDD Reference for terminology disputes (reference)
- **Tools:**
  - FOSS (hands-on): [EventStorming](https://www.eventstorming.com/) on paper or a [Miro](https://miro.com/) free-tier board — the discovery workshop (↔ no corp equivalent; this is method)
  - FOSS (hands-on): [Context Mapper](https://contextmapper.org/) — a DSL that turns the context map into a versionable, reviewable artifact
- **Do:**
  1. Run a solo big-picture EventStorming of the subscription-order-to-NAV flow: domain events on orange stickies left to right, hotspots flagged, pivotal events (order accepted, trade settled, NAV struck) marked.
  2. Cluster the events into 5–7 candidate bounded contexts for a fund administrator (TA, fund accounting, custody, regulatory reporting, client reporting at minimum) and classify each subdomain as core/supporting/generic.
  3. Draw the context map with an explicit relationship type per edge — e.g. custody-to-fund-accounting as customer–supplier, EMT to distributors as published language, a legacy TA feed behind an ACL.
  4. Encode the map in Context Mapper DSL and commit it alongside your ADR log.
  5. Annotate which contexts own which data products and whether each product is source-aligned, aggregate, or consumer-aligned.
- **Done when:**
  - [ ] Defend the context map against the challenge "why is fund accounting not part of the TA context?" with a domain answer (different language, different invariants), not an org-chart answer.
  - [ ] Name the core subdomain of a fund administrator and justify where you would build rather than buy.
  - [ ] Point to one ACL on the map and explain exactly what model corruption it prevents.
- Est. hours: 10

#### 13.1.1 + 13.1.2 Data contracts (ODCS, enforcement) — T1
- **Why:** Contracts operationalize everything Phase 6 built — they are the mechanism that turns "governed dataset" into "product a consumer can rely on", and what the architect points to when a producer asks "can I rename this column?". The EU fund-data world (EMT files between manufacturers and distributors!) has run on implicit contracts for years; without explicit ones, breaking changes ship silently and surface as failed distributor loads and NAV-report corrections.
- **Learn:**
  - contract anatomy — schema, semantics, quality guarantees, SLAs, ownership, and terms of use as one negotiated document *(Driving Data Quality pt. 1–2)*
  - ODCS structure — the Bitol/Linux Foundation YAML standard: fundamentals, schema, quality, team/roles, and SLA blocks *(ODCS spec)*
  - datacontract-cli workflow — authoring, `lint`, `test` against live data, and breaking-change detection between versions *(Data Contract CLI docs)*
  - enforcement points — producer CI schema diff, schema registry on Kafka, WAP gate in the lakehouse, dbt model contracts in the warehouse *(dbt docs: Model contracts)*
  - contract-first vs contract-extracted adoption — greenfield negotiation vs retro-fitting contracts onto existing feeds, and when each path wins *(Driving Data Quality pt. 3)*
  - versioning & deprecation policy — semver for data, notice periods, migration paths; ties to your 1.9.7 evolution policy — same policy, now productized *(ODCS spec)*
- **Resources:**
  - **[Driving Data Quality with Data Contracts](https://www.oreilly.com/library/view/driving-data-quality/9781837635009/) (Andrew Jones)** — contract anatomy, adoption paths, producer accountability (primary)
  - [Open Data Contract Standard (ODCS)](https://bitol-io.github.io/open-data-contract-standard/) — the specification your contracts are written in (reference)
  - [Data Contract CLI docs](https://cli.datacontract.com/) — authoring, validation, tests against live data, breaking-change detection (hands-on reference)
  - [dbt docs: Model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts) — warehouse-side enforcement of contracted models (reference)
- **Tools:**
  - FOSS (hands-on): [datacontract-cli](https://cli.datacontract.com/) — contract authoring and CI testing (↔ [Gable](https://www.gable.ai/))
  - FOSS (hands-on): [dbt model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts) + [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/index.html) — enforcement at the model and at the topic (↔ Confluent data contracts)
  - Corp (evaluate): [Gable](https://www.gable.ai/), [DataHub](https://datahubproject.io/) contracts — what commercial contract platforms add (code-level lineage, workflow) at build-vs-buy level
- **Do:**
  1. Write the ODCS contract for your gold NAV mart: schema with per-field semantics (ISIN, NAV-per-share precision), DQ guarantees, freshness SLO, named owner, license terms.
  2. Write the equivalent contract for the EMT output, treating distributors as the consumers and the FinDatEx field semantics as the published language.
  3. Wire `datacontract test` into CI so every merge validates both contracts against the live lakehouse tables.
  4. Add dbt model contracts on the underlying gold models so a type change fails the producer's build, not the consumer's load.
  5. Demonstrate a breaking change (rename a NAV column) being caught pre-merge, and a compatible change (new nullable column) passing with a version bump.
- **Done when:**
  - [ ] Show that a consumer can subscribe to your product knowing exactly what is guaranteed, and a producer cannot break it silently — both demonstrated in CI, not asserted.
  - [ ] Explain where each enforcement point (CI, registry, WAP gate, dbt) catches what the others miss.
  - [ ] Produce the deprecation notice you would send for a breaking change, with version, timeline, and migration path.
- Est. hours: 10

#### 14.4.2 Regulatory reporting — T1
- **Why:** Submission-grade reporting (AIFMD Annex IV, PRIIPs KID/EPT, MiFID/EMT) is the fund-data domain's flagship deliverable — deadline-driven, auditor-reviewed, and the workload your whole platform exists to serve. An architect who cannot design completeness gates and four-eyes approval ships late or wrong filings, and in Luxembourg a wrong Annex IV is a CSSF conversation, not a bug ticket.
- **Learn:**
  - what makes reporting "submission-grade" — completeness gates, plausibility checks, four-eyes approval, resubmission/correction workflow, full lineage to source, immutable filing archive *(ESMA IT guidance, applied)*
  - AIFMD Annex IV concretely — scope, reporting frequency by AUM threshold, the XML format, XSDs, and validation rules *(ESMA IT guidance)*
  - the rest of the EU landscape — PRIIPs KID data via EPT (your Phase-2 work), EMT distribution, SFDR templates and their ESG-data sourcing pain *(FinDatEx)*
  - report calendars & deadline orchestration — filing windows become schedules, sensors, and escalation paths; your Dagster schedules grow teeth *(Dagster docs)*
  - the vendor landscape — what Workiva/AxiomSL (Adenza)/Wolters Kluwer/Vermeg actually sell: forms engines + rule-update subscriptions + filing connectivity; the data stays your problem *(Workiva site)*
  - build-vs-buy economics — rule-maintenance burden is the buy argument; the pipeline feeding the forms engine is never outsourceable *(Workiva site, read critically)*
- **Resources:**
  - **[ESMA: AIFMD reporting IT technical guidance](https://www.esma.europa.eu/document/aifmd-reporting-it-technical-guidance-rev-6-updated)** — Annex IV templates, XSD schemas, validation rules (primary, free)
  - [FinDatEx](https://findatex.eu/) — your Phase-2 EMT/EPT specs (and the SFDR EET), reread as a producer (reference)
  - [Dagster docs](https://docs.dagster.io/) — schedules and sensors for deadline orchestration and the manual approval gate (hands-on reference)
  - [Workiva](https://www.workiva.com/) — one vendor-positioning read for the forms-engine layer (evaluation, not adoption)
- **Tools:**
  - FOSS (hands-on): the platform you built + [Dagster](https://docs.dagster.io/) scheduling and sensors — orchestrates gates, approvals, and deadlines
  - Corp (evaluate): [Workiva](https://www.workiva.com/), [Wolters Kluwer](https://www.wolterskluwer.com/) OneSumX, [Vermeg](https://www.vermeg.com/) — forms engines + rule updates + filing connectivity; know what they do and don't solve
- **Do:**
  1. Design the Annex-IV-shaped pipeline on paper first: gold marts → validation gates → XML rendering → four-eyes approval → immutable filing archive, in one diagram.
  2. Implement the validation gates as hard stops in Dagster: completeness (every required template field populated) and plausibility (AUM within tolerance of last period).
  3. Render the XML against the published ESMA schema and validate it; deliberately corrupt one field and show schema validation failing the run.
  4. Add the four-eyes step: a Dagster sensor that holds the filing until a second identity approves, logging who approved what and when.
  5. Archive each filing immutably (object-lock/WORM-style) with a lineage snapshot pinned to the run, and exercise the resubmission path once.
  6. Write the build-vs-buy memo for the forms-engine layer: rule-maintenance cost, vendor price ballpark, and what stays in-house either way.
- **Done when:**
  - [ ] Demonstrate that a deliberately incomplete dataset cannot reach the filing stage.
  - [ ] Trace a resubmission end-to-end: correction, re-approval, new archive entry linked to the superseded filing.
  - [ ] Defend the memo's honest pricing of the vendor option, including what buying does *not* solve (your data quality).
- Est. hours: 10

#### 8.1.3 Industry frameworks (TOGAF & ArchiMate, working fluency) — T2
- **Why:** TOGAF/ArchiMate is the lingua franca of EA departments in EU financial institutions; the architect who can't speak it gets translated by someone who can. Without working fluency your data architecture never lands in the enterprise repository on its own terms, and your designs lose governance-board arguments to a well-drawn ArchiMate view of a worse idea.
- **Learn:**
  - TOGAF 10 shape — the ADM cycle and what each phase produces, focusing on B/C (data architecture) with E/F covered via A.10 *(TOGAF Standard)*
  - architecture repository & landscape — building blocks, standards, and where your artifacts formally live *(TOGAF Standard)*
  - what to take seriously vs hold lightly — deliverable discipline and governance hooks yes; the full ceremony no *(TOGAF Standard, read critically)*
  - ArchiMate 3.2 core — business/application/technology layers and the core relationship set *(ArchiMate overview)*
  - the data-relevant elements — business object ↔ data object ↔ artifact, and how realization crosses layers *(ArchiMate overview)*
  - modeling in Archi — one model, many views; viewpoints as audience-specific projections *(Archi user guide)*
  - C4 ↔ ArchiMate mapping — which audience needs which notation, and how to translate between them live *(C4 model site)*
- **Resources:**
  - **[The TOGAF Standard](https://www.opengroup.org/togaf)** — Fundamental Content: Introduction & Core Concepts + ADM, free with Open Group registration (primary)
  - [ArchiMate — The Open Group](https://www.opengroup.org/archimate-forum/archimate-overview) — entry point to the 3.2 language specification (reference)
  - [Archi](https://www.archimatetool.com/) — the FOSS modelling tool, its user guide, and "hello ArchiMate" resources (hands-on)
  - [C4 model](https://c4model.com/) — the developer-facing notation you map to and from (deepening)
- **Tools:**
  - FOSS (hands-on): [Archi](https://www.archimatetool.com/) — full ArchiMate 3.2 modelling (↔ [Sparx EA](https://sparxsystems.com/), [BiZZdesign](https://bizzdesign.com/) — the licensed EA suites)
- **Do:**
  1. Read the TOGAF Core Concepts and ADM chapters; write a one-page "what I will actually use" note (phase B/C deliverables, repository discipline, governance hooks).
  2. Model your entire capstone platform in Archi: application layer (services, data products) and technology layer (clusters, storage), with data objects for the products realized by artifacts and linked to business objects (NAV, order, holding).
  3. Produce the COO viewpoint: a business-application view showing which business capabilities each data product serves.
  4. Produce the security viewpoint: a technology view showing zones, the gateway, and where PII-bearing artifacts live.
  5. Translate one ArchiMate application view into a C4 container diagram and record the mapping rules you used.
- **Done when:**
  - [ ] Walk an EA review board through the ArchiMate model and translate any element to/from your C4 diagrams live.
  - [ ] Place any of your existing artifacts (context map, technology standard, roadmap) in the correct ADM phase without looking it up.
  - [ ] State which TOGAF artifacts you would skip on a 10-person programme, and why that is defensible.
- Est. hours: 10

#### 1.4.4 Data mesh (and 13.2.1 enabling platforms) — T2
- **Why:** Mesh is the organizational scaling answer you'll be asked about in every large-firm interview; the architect's job is knowing when its costs are justified — and what "federated computational governance" means after Phase 6. Adopt it too early and you starve the platform team while shattering a small firm's estate into unowned fragments; dismiss it outright and a 3,000-person group keeps its central-team bottleneck forever.
- **Learn:**
  - the four principles — domain ownership, data as a product, self-serve platform, federated computational governance — read against your own build *(Data Mesh pt. I)*
  - what you have already built — principles 2–4 exist single-domain in your platform; what changes when domains multiply *(Data Mesh pt. II)*
  - federated computational governance — global policies executed by the platform (your policy-as-code and catalog work) vs local domain autonomy *(Data Mesh pt. II)*
  - mesh failure modes — mesh-washing, platform-team starvation, premature decentralization *(Data Management at Scale 2e)*
  - enabling platforms — Starburst/Trino federation, Databricks UC domains, your OpenMetadata domains as the technical substrate *(Data Management at Scale 2e)*
  - the sizing test — why a 50-person fund admin should *not* mesh, and the threshold signals that change the answer *(Data Mesh pt. III skim)*
- **Resources:**
  - **[Data Mesh](https://www.oreilly.com/library/view/data-mesh/9781492092384/) (Dehghani), parts I–II, skim III** — the principles and target operating model (primary)
  - [Data Management at Scale, 2nd ed.](https://www.oreilly.com/library/view/data-management-at/9781098138851/) (Strengholt) — the pragmatic counterweight: domains without dogma (alternate)
  - [Data Mesh Principles (martinfowler.com)](https://martinfowler.com/articles/data-mesh-principles.html) — free condensed statement of the four principles (reference)
- **Tools:**
  - FOSS (evaluate): [Trino](https://trino.io/) federation + [OpenMetadata](https://docs.open-metadata.org/) domains — the self-serve substrate you already run
  - Corp (evaluate): [Starburst](https://www.starburst.io/), [Databricks Unity Catalog](https://docs.databricks.com/) domains — what the commercial enabling platforms package
- **Do:**
  1. Re-read your Phase-6/7 platform inventory and mark which mesh principle each component serves; note the gaps (multi-domain ownership, federated policy execution).
  2. Take the DDD context map from 8.4.1 as the candidate domain decomposition for a 300-person fund administrator.
  3. Write the two-page memo: "Should a 300-person fund administrator adopt mesh?" — org sizing, domain map, platform prerequisites, and an honest no/not-yet/yes-partially recommendation with trigger conditions.
  4. Stress-test the memo by writing the strongest one-paragraph counter-argument to your own recommendation, then answer it.
- **Done when:**
  - [ ] Argue both for and against mesh for the same firm, and name the organizational precondition that decides it.
  - [ ] Define federated computational governance in one sentence, with a concrete policy example from your own build.
  - [ ] List three mesh failure modes and the early-warning signal for each.
- Est. hours: 5

#### 7.1.1 + 7.2.1 Semantic & metrics layer (Cube, MetricFlow) — T2
- **Why:** "One definition of AUM" is a governance promise only a semantic layer can keep across BI tools, APIs, and notebooks; headless BI is the architectural pattern behind it. Without it every dashboard and board pack re-derives AUM in its own SQL, the numbers drift, and the architect spends review meetings arbitrating whose figure is right instead of designing.
- **Learn:**
  - semantic-layer anatomy — dimensions, measures, joins, and access control defined once at the semantic level *(Cube docs: data modeling)*
  - Cube specifics — data model files, pre-aggregations, REST and SQL APIs, caching tiers *(Cube docs)*
  - MetricFlow — metric definitions living in the dbt DAG; simple, derived, ratio, and cumulative metric types *(dbt docs: About MetricFlow)*
  - the consistency argument — a metrics layer vs BI-tool-local definitions, and why the latter always drifts *(dbt docs: About MetricFlow)*
  - semantic layer vs glossary — definition *executed* vs definition *documented*, and how to link the two so neither rots *(Cube docs, applied)*
  - when the semantic layer is premature — one consumer, one tool, no contested metrics *(Cube docs: introduction)*
- **Resources:**
  - **[Cube docs](https://docs.cube.dev/)** — data modeling, pre-aggregations, REST/SQL APIs, caching (primary)
  - [dbt docs: About MetricFlow](https://docs.getdbt.com/docs/build/about-metricflow) — metric specification inside the dbt DAG (alternate stack)
  - [Apache Superset](https://superset.apache.org/) — the consuming BI client for the three-client demo (hands-on reference)
- **Tools:**
  - FOSS (hands-on): [Cube](https://docs.cube.dev/) — headless semantic layer (↔ [Looker](https://cloud.google.com/looker)/LookML, [AtScale](https://www.atscale.com/))
  - FOSS (hands-on): [MetricFlow](https://docs.getdbt.com/docs/build/about-metricflow) — dbt-native metrics (↔ [Power BI semantic models](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand) — next entry)
- **Do:**
  1. Define NAV, AUM, and net-flows once in Cube's data model over the gold marts, including the join topology and a management-company access rule at the semantic level.
  2. Mirror the same three metrics as MetricFlow definitions in the dbt project; note where the two specification styles diverge.
  3. Consume the Cube metrics from three clients — a Superset chart, a raw REST call, and a notebook via the SQL API — and show identical numbers.
  4. Link each metric to its glossary term in both directions (glossary entry → semantic-layer reference, metric description → glossary URL).
  5. Change the AUM definition (e.g. exclude side-pocket share classes) in one place and demonstrate all three clients updating, with the change visible in version control.
- **Done when:**
  - [ ] Demonstrate that changing the AUM definition in one place changes it everywhere, with an audit trail.
  - [ ] Explain pre-aggregations: what they cache, when they invalidate, and the freshness trade-off they buy.
  - [ ] State the rule for when a metric belongs in the semantic layer vs a local dashboard calculation.
- Est. hours: 7

#### 7.1.2 Platform semantic layers (Power BI semantic models) — T2
- **Why:** In Azure shops the Power BI semantic model *is* the de-facto semantic layer; you must know when it suffices and when headless wins. Rule wrongly and you either pay for a redundant headless layer nobody queries, or watch certified AUM definitions fork across forty workspace models — the sprawl failure mode that CFOs and auditors both eventually notice.
- **Learn:**
  - storage modes — import vs DirectQuery vs Direct Lake (the Fabric tie to A.4) and their latency/cost/freshness trade-offs *(MS Learn: semantic model modes)*
  - star-schema expectations — why your Kimball work is the prerequisite for a healthy model *(MS Learn: star schema)*
  - RLS in the model — roles, DAX filters, and management-company isolation *(MS Learn: semantic models in the service)*
  - lifecycle management — deployment pipelines and the XMLA endpoint for pro-grade ALM *(MS Learn: semantic models in the service)*
  - sprawl & certified datasets — endorsement, discovery, and the governance that prevents forty AUM definitions *(MS Learn: semantic models in the service)*
  - the decision rubric — Power BI model vs headless layer by org shape, tool mix, and consumer diversity *(MS Learn: semantic model modes, applied)*
- **Resources:**
  - **[Understand star schema and the importance for Power BI](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)** — the model-design guidance the exercise follows (primary)
  - [Semantic models in the Power BI service](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand) — creation, management, endorsement, and sharing of models (reference)
  - [Semantic model modes in the Power BI service](https://learn.microsoft.com/en-us/power-bi/connect-data/service-dataset-modes-understand) — import vs DirectQuery vs composite, the Direct Lake context (reference)
- **Tools:**
  - Corp (hands-on, free Desktop): [Power BI](https://learn.microsoft.com/en-us/power-bi/) — Desktop suffices for the exercise (↔ FOSS: [Cube](https://docs.cube.dev/) from the previous entry)
- **Do:**
  1. Build the NAV mart semantic model in Power BI Desktop (free): a star schema with fund/share-class/date dimensions and explicit measures for NAV, AUM, and net-flows.
  2. Implement RLS by management company and verify it with the "view as role" feature.
  3. Compare definitions with your Cube model measure by measure; document every place the two could drift (measure logic, filters, timezone handling).
  4. Write the governance rule preventing drift: which layer is authoritative for which metric, and the review step that enforces it.
  5. Write the one-page rubric ruling "Power BI model vs headless layer" for three org shapes (Azure-only 50-person admin, multi-tool 300-person admin, multi-cloud group).
- **Done when:**
  - [ ] Rule "Power BI model vs headless layer" for three org shapes and defend it.
  - [ ] Demonstrate RLS isolating two management companies inside one model.
  - [ ] Name the semantic-model-sprawl failure mode and the certified-dataset control that contains it.
- Est. hours: 4

#### 12.4.1 Data SLAs & SLO management — T2
- **Why:** The SLO machinery (Phase 5 vocabulary) becomes contractual here: freshness/completeness targets with error budgets are what "productized" means operationally. Without measured SLOs, the contract's "fresh by 08:00 CET" is marketing copy — and the first missed NAV deadline becomes finger-pointing instead of a burn-rate alert with a documented response.
- **Learn:**
  - data SLIs — freshness, completeness, accuracy proxies, and serving-layer availability as measurable indicators *(SRE Workbook ch. 2)*
  - setting SLOs consumers actually need — interview them (BA skills) instead of declaring vanity nines *(SRE Workbook ch. 2)*
  - error budgets for data — when a burned budget freezes risky pipeline changes *(SRE Workbook ch. 2)*
  - burn-rate alerting — multiwindow, multi-burn-rate alerts instead of paging on point failures *(SRE Workbook ch. 5)*
  - SLO surfacing — attainment published on the catalog product page and in the ODCS contract's SLA block *(ODCS spec)*
- **Resources:**
  - **[Google SRE Workbook ch. 2: Implementing SLOs](https://sre.google/workbook/implementing-slos/)** — SLI/SLO/error-budget mechanics, translated to data in your 13.1.1 contract (primary, free online)
  - [Google SRE Workbook ch. 5: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) — burn-rate alert design (deepening)
  - [ODCS spec](https://bitol-io.github.io/open-data-contract-standard/) — where the SLA properties live in the contract you already wrote (reference)
- **Do:**
  1. Interview yourself as three consumers (board-pack analyst, distributor ops, regulatory deadline owner) and derive the SLOs each actually needs from the NAV product.
  2. Define the SLOs (e.g., 99% of business days fresh by 08:00 CET; 100% of active share classes present) and encode them in the ODCS contract's SLA block.
  3. Instrument the SLIs from your Phase-5/6 telemetry and store daily attainment.
  4. Add a burn-rate alert (fast + slow window) on the freshness SLO.
  5. Replay one month of synthetic history including one bad week; record attainment, the alert firing, and the error-budget response (a change-freeze note).
- **Done when:**
  - [ ] Show the product page displaying measured SLO attainment, and a simulated bad week visibly consuming error budget with a documented response.
  - [ ] Explain why burn-rate alerting beats alerting on individual late runs.
  - [ ] Justify each SLO target with a named consumer need, not a round number.
- Est. hours: 3

#### 13.3.2 Cross-org data sharing (Delta Sharing) — T2
- **Why:** Fund data is *disseminated* — to distributors, platforms, regulators; open sharing protocols are the modern alternative to the SFTP-and-CSV folklore the industry still runs on. The architect who can't compare sharing protocol vs API vs file-drop ends up rebuilding forty bespoke SFTP feeds, each with its own format drift and no revocation story.
- **Learn:**
  - the Delta Sharing protocol — open, REST-based, format-level access to Delta tables without copying *(Delta Sharing page)*
  - shares, recipients, governance — how access is granted, scoped, audited, and revoked *(delta-sharing GitHub)*
  - the walled gardens — Snowflake secure shares and the Databricks marketplace as in-ecosystem equivalents *(Snowflake docs: Secure Data Sharing)*
  - egress economics — who pays for reads, and why no-copy sharing changes the cost conversation *(Snowflake docs: Secure Data Sharing)*
  - the channel rubric — sharing protocol vs API vs file-drop, scored by volume, latency, and consumer sophistication *(Delta Sharing page, applied)*
  - the contractual overlay — a share is still a product: contract, SLOs, and license terms ride along (ties 13.1.1, A.18) *(delta-sharing GitHub, applied)*
- **Resources:**
  - **[Delta Sharing](https://delta.io/sharing/)** — the open protocol: overview and ecosystem (primary)
  - [delta-sharing on GitHub](https://github.com/delta-io/delta-sharing) — protocol spec, the reference server you will run, client libraries (hands-on)
  - [Snowflake docs: About Secure Data Sharing](https://docs.snowflake.com/en/user-guide/data-sharing-intro) — the walled-garden comparison read (reference)
- **Tools:**
  - FOSS (hands-on): [delta-sharing reference server](https://github.com/delta-io/delta-sharing) — serves a gold Delta table over the open protocol (↔ [Databricks Delta Sharing](https://docs.databricks.com/), [Snowflake shares](https://docs.snowflake.com/en/user-guide/data-sharing-intro), Fabric external sharing)
- **Do:**
  1. Stand up the reference sharing server over a gold Delta table, with a share config exposing one schema to one recipient token.
  2. Consume the share from a separate "distributor" environment with the pandas client; verify the data matches source with no copy pipeline in between.
  3. Rotate and then revoke the recipient credential and show access ending — the revocation story SFTP never had.
  4. Write the rubric: when sharing protocol vs API vs EMT file-drop, scored by volume, latency, consumer sophistication, and audit needs.
- **Done when:**
  - [ ] Design the dissemination architecture for a fund manufacturer with 40 distributor relationships and defend the channel per consumer class.
  - [ ] Explain what the open protocol buys over Snowflake/Databricks-native shares, and what it costs you to run.
  - [ ] Show the revocation demo and name the governance evidence it produces.
- Est. hours: 3

#### 13.4.2 + 2.6.1 Data APIs & gateways (data-as-a-service) — T2
- **Why:** The API is the product surface for operational consumers (websites, partner systems); the gateway is where auth, quotas, and versioning live — an architect's checklist, not a developer's tutorial. Skip the gateway discipline and every consumer hits the database directly: no quotas, no usage attribution for chargeback, and an OWASP-API-Top-10 incident waiting on the NAV endpoint.
- **Learn:**
  - resource modeling for fund data — funds/share-classes/navs as resources, pagination, filtering, consistent error shapes *(Azure AC: Web API design)*
  - versioning policy — URI vs header versioning, deprecation paths; ties to your 1.9.7 evolution policy *(Azure AC: Web API design)*
  - OpenAPI as the contract — the machine-readable spec consumers onboard from, kept in version control *(Azure AC: Web API design)*
  - gateway duties — OIDC token validation (your Keycloak), rate limiting and quotas per consumer tier, usage analytics for chargeback *(Kong Gateway docs)*
  - instant serving — PostgREST (or FastAPI) turning a gold view into a read-only REST API in minutes *(PostgREST docs)*
  - caching policy at the edge — your 3.3.4 decision applied at the gateway tier *(Kong Gateway docs)*
  - API security — the OWASP API Top-10 as the review checklist (A.12) *(OWASP API Security Project)*
  - when GraphQL earns its complexity — many consumers with shape-shifting reads; rarely for fund data (2.6.2 stays T3) *(Azure AC: Web API design)*
- **Resources:**
  - **[Kong Gateway docs](https://developer.konghq.com/gateway/)** — gateway concepts: auth plugins, rate limiting, usage analytics (primary)
  - [PostgREST docs](https://docs.postgrest.org/) — serving Postgres views as REST, roles and JWT integration (hands-on)
  - [Azure Architecture Center: Web API design best practices](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design) — resource modeling, versioning, pagination, filtering (reference)
  - [OWASP API Security Project](https://owasp.org/www-project-api-security/) — the Top-10 checklist you will run against your own API (reference)
- **Tools:**
  - FOSS (hands-on): [PostgREST](https://docs.postgrest.org/) or [FastAPI](https://fastapi.tiangolo.com/) — the serving layer over gold views
  - FOSS (hands-on): [Kong Gateway OSS](https://developer.konghq.com/gateway/) + [Keycloak](https://www.keycloak.org/documentation) — OIDC validation, quotas, usage logs (↔ [Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/), [Apigee](https://cloud.google.com/apigee))
- **Do:**
  1. Expose the NAV product as a read-only REST API: PostgREST over a gold view, with `/funds`, `/share-classes`, `/navs` resources, pagination, and filtering.
  2. Put Kong in front: OIDC plugin validating Keycloak tokens, and two consumer tiers with different rate limits.
  3. Publish the OpenAPI document — generate it, then hand-edit descriptions until a stranger could onboard from it.
  4. Drive traffic past a quota and show enforcement (HTTP 429s) plus per-consumer usage in the gateway logs — the chargeback evidence.
  5. Run the OWASP API Top-10 checklist (A.12) against the API; fix or explicitly risk-accept each finding.
- **Done when:**
  - [ ] Prove an external consumer can onboard from the OpenAPI doc + contract alone, and the gateway proves quota enforcement in logs.
  - [ ] State your API versioning policy and show where a breaking change would surface for consumers.
  - [ ] Present the completed OWASP API Top-10 checklist with each item fixed or risk-accepted.
- Est. hours: 5

#### 14.1.1 + 14.1.3 Business intelligence (Superset hands-on, Power BI fluency) — T2
- **Why:** BI is where your platform meets its judges; the architect doesn't build dashboards for a living but must design the BI tier (tooling, governance, self-service boundaries) and read the vendor market. Get the governance wrong and you inherit the "300 unowned dashboards" estate — contradictory numbers in front of the fund board, with nobody accountable for any of them.
- **Learn:**
  - Superset mechanics — datasets/charts/dashboards, its semantic-ish layer, row-level security, embedding *(Superset docs)*
  - Power BI ecosystem economics — per-user vs capacity/Fabric licensing as the real selection driver in Azure shops *(MS Learn: Power BI licensing)*
  - vendor positioning — Tableau/Looker/Qlik read in one sitting: who sells what, to whom *(Tableau site)*
  - governed self-service — certified datasets, sandbox vs production content, explicit ownership rules *(Superset docs: security)*
  - the sprawl failure mode — how 300 unowned dashboards happen and the certification workflow preventing it *(MS Learn: Power BI licensing, applied)*
  - BI-on-semantic-layer — consume Cube; never re-model metrics inside the BI tool *(Cube docs)*
- **Resources:**
  - **[Apache Superset](https://superset.apache.org/)** — docs: creating charts/dashboards, security and RLS, embedding (primary)
  - [MS Learn: Power BI license types](https://learn.microsoft.com/en-us/power-bi/fundamentals/service-features-license-type) — features by license, the economics read (reference)
  - [Tableau](https://www.tableau.com/) — one vendor-positioning read; skim Looker and Qlik the same way (market scan)
  - [Cube docs](https://docs.cube.dev/) — connecting BI tools to the semantic layer (reference)
- **Tools:**
  - FOSS (hands-on): [Apache Superset](https://superset.apache.org/), [Metabase](https://www.metabase.com/) (↔ [Power BI](https://learn.microsoft.com/en-us/power-bi/) [Azure default], [Tableau](https://www.tableau.com/), [Looker](https://cloud.google.com/looker))
  - Corp (evaluate): [Power BI](https://learn.microsoft.com/en-us/power-bi/) — primary evaluation: licensing tiers, capacity planning, Fabric direction
- **Do:**
  1. Build the fund-board dashboard (NAV trend, net flows, DQ status) in Superset *on top of Cube* — every figure sourced from semantic-layer metrics, zero local SQL definitions.
  2. Apply RLS in Superset by management company and verify with two test users.
  3. Skim Power BI, Tableau, and Looker positioning/pricing pages; write a half-page market map of who wins in which org shape.
  4. Write the BI governance one-pager: certification workflow, ownership, sandbox-vs-production policy, and a decommissioning rule for unowned content.
- **Done when:**
  - [ ] Verify the dashboard consumes only semantic-layer metrics (zero local SQL definitions).
  - [ ] Present the governance pager answering "who may publish what, where" — including the path from sandbox to certified.
  - [ ] Explain Power BI per-user vs capacity licensing well enough to size a 300-user deployment.
- Est. hours: 7

#### 14.6.1 Data app frameworks (Streamlit) — T2
- **Why:** Data apps are the fast path from platform to stakeholder value (review queues, what-if tools); Streamlit is the de-facto standard and your Phase-7 review UI already used it. Without understanding its execution model and scaling limits, the architect green-lights a 200-user Streamlit "application" that reruns the world on every widget click and falls over at the first board demo.
- **Learn:**
  - the execution model — rerun-on-interaction, `st.cache_data`/`st.cache_resource`, session state *(Streamlit docs)*
  - scaling limits — the single-process model and the user-count/interactivity point where it breaks *(Streamlit docs)*
  - the decision line — Streamlit vs Dash vs a real frontend, by interactivity, state complexity, and audience size *(Dash docs, compared)*
  - deployment & auth — running behind your Kong gateway with OIDC instead of public-internet defaults *(Streamlit docs)*
  - the internal-tools landscape — what the Retool class sells: CRUD on governed APIs with RBAC, at a glance *(Retool site)*
- **Resources:**
  - **[Streamlit docs](https://docs.streamlit.io/)** — main concepts, caching, session state, deployment (primary)
  - [Dash docs](https://dash.plotly.com/) — the main FOSS alternative, read for the comparison (alternate)
  - [Retool](https://retool.com/) — the commercial internal-tools class at a glance (market scan)
- **Tools:**
  - FOSS (hands-on): [Streamlit](https://docs.streamlit.io/) — the product console (↔ Snowflake-Streamlit, [Retool](https://retool.com/), [Power Apps](https://learn.microsoft.com/en-us/power-apps/))
- **Do:**
  1. Build the "fund data product console": one screen per product showing SLO status, contract version, latest DQ results, lineage link, and a sample-data preview.
  2. Pull each panel from existing services (SLO telemetry, contract repo, DQ store, OpenMetadata link) — no new data paths.
  3. Cache expensive calls correctly and prove a widget interaction does not refetch the world (log the cache hits).
  4. Serve the console behind Kong with OIDC, so access uses the same identity plane as everything else.
- **Done when:**
  - [ ] Confirm a product owner can answer "is my product healthy and who consumes it?" from the console without touching the platform.
  - [ ] Explain the rerun-on-interaction model and show where caching saved you.
  - [ ] State the user-count/interactivity threshold where you would leave Streamlit, and for what.
- Est. hours: 3

#### 1.8.11 Strangler fig (legacy replacement strategy) — T2
- **Why:** Every Luxembourg estate has a legacy core (TA system, reporting engine) that can only be replaced incrementally; strangler-fig discipline is how migrations avoid big-bang death — and it operationalizes your A.10 roadmapping. Without it, replacement programmes run as multi-year parallel estates with dual-write drift, and the legacy system never dies — it just gains a twin.
- **Learn:**
  - the pattern — incrementally route functionality through a facade until the legacy core is hollow, then switch it off *(Fowler: Strangler Fig Application)*
  - facade placement for data systems — views, CDC-fed parallel runs, routing at the consumption layer *(Azure AC: Strangler Fig pattern)*
  - dual-write avoidance — use your outbox/CDC patterns instead of writing to both systems *(Azure AC: Strangler Fig pattern)*
  - parallel-run reconciliation — your Phase-4 reconciliation pattern reused as the trust-builder before cutover *(Fowler: Strangler Fig Application, applied)*
  - cutover & rollback criteria — measurable gates (drift thresholds, consumer migration counts), not dates *(Azure AC: Strangler Fig pattern)*
  - the anti-pattern — the strangler that never finishes; sunset discipline and funded decommissioning *(Fowler: Strangler Fig Application)*
- **Resources:**
  - **[Strangler Fig Application (Martin Fowler)](https://martinfowler.com/bliki/StranglerFigApplication.html)** — the pattern and its rationale (primary)
  - [Azure Architecture Center: Strangler Fig pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) — cloud-migration framing, context, and issues to watch (reference)
- **Do:**
  1. Pick the target: a legacy reporting mart to be replaced by your gold layer; inventory its consumers and inbound feeds.
  2. Write the migration ADR: facade design (views/routing), CDC-fed parallel-run period, reconciliation gates, cutover criteria, rollback plan, sunset date.
  3. Define the reconciliation checks concretely (row counts, NAV-per-share tolerance, aggregate AUM) and the drift threshold that blocks cutover.
  4. Add the sunset milestone with a named decommission deliverable — what gets switched off, and who signs.
- **Done when:**
  - [ ] Verify the plan has measurable gates (reconciliation drift thresholds) instead of dates-and-hope.
  - [ ] Explain why dual-write is forbidden in your design and what replaces it.
  - [ ] Name the organizational forces that produce never-finishing stranglers, and your counter for each.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.4.5 | Data fabric | Metadata-driven unified-access vision (vendor-led counterpoint to mesh) | [IBM: What is a data fabric?](https://www.ibm.com/think/topics/data-fabric) — read critically | 20 |
| 2.6.2 | GraphQL data layers | Schema-driven query APIs (Hasura); complexity rarely earned for fund data | [Hasura docs](https://hasura.io/docs/) — "how it works" intro | 20 |
| 2.7.1 | Reverse ETL | Warehouse → SaaS sync (Hightouch/Census); CRM-enrichment use cases | [Hightouch docs](https://hightouch.com/docs) — intro | 20 |
| 13.3.1 | Internal data marketplaces | Catalog-with-checkout UX over data products | [Atlan: Data Marketplace](https://atlan.com/data-marketplace/) | 15 |
| 13.3.3 | Commercial data marketplaces | Buying market/ESG data feeds (Snowflake Marketplace, Datarade) | [About Snowflake Marketplace](https://docs.snowflake.com/collaboration/collaboration-marketplace-about) | 20 |
| 13.4.1 | GraphQL DaaS | Productized GraphQL endpoints; see 2.6.2 | [covered there — Hasura docs](https://hasura.io/docs/) | 5 |
| 14.1.2 | Legacy enterprise BI | BusinessObjects/Cognos/MicroStrategy estates you'll migrate from | [IBM Cognos Analytics](https://www.ibm.com/products/cognos-analytics) — one vendor-positioning overview | 20 |
| 14.2.1 | Visualization libraries | Plotly/Vega/D3 programmatic charting; Storytelling-with-Data principles | [*Storytelling with Data*](https://www.storytellingwithdata.com/) — ch. 1–2 skim | 45 |
| 14.3.1 | Embedded analytics | BI inside products (Superset/Cube embed, Looker embed) | [Cube docs](https://docs.cube.dev/) — embedding pages | 20 |
| 14.4.1 | Operational/paginated reporting | Pixel-perfect statements (Power BI paginated, Jasper) | [Power BI paginated reports overview](https://learn.microsoft.com/en-us/power-bi/paginated-reports/paginated-reports-report-builder-power-bi) | 20 |
| 14.5.1 | Cloud notebooks | Hex/Deepnote collaborative analysis; governance angle (where results live) | [Hex](https://hex.tech/) — product overview | 15 |
| 14.6.2 | Low-code internal tools | Retool/Appsmith CRUD builders on governed APIs | [Appsmith](https://www.appsmith.com/) — overview | 15 |
| 14.7.2 | Reverse-ETL activation | Acting on data signals in operational tools; see 2.7.1 | [covered there — Hightouch docs](https://hightouch.com/docs) | 5 |

*T3 subtotal: 4 h*

### Capstone 8 — The fund data product (end state)

- **Goal:** the four-year arc closes: one fund data product, productized end-to-end — contracted, SLO-backed, semantically defined, multi-channel (BI, API, sharing, EMT file), regulator-ready, and documented like the portfolio piece it is.
- **Stack (100% free):** everything already running, plus [Cube](https://docs.cube.dev/) + [MetricFlow](https://docs.getdbt.com/docs/build/about-metricflow) (↔ [Looker](https://cloud.google.com/looker)/[AtScale](https://www.atscale.com/)/[Power BI semantic models](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand)), [datacontract-cli](https://cli.datacontract.com/) + [ODCS](https://bitol-io.github.io/open-data-contract-standard/) (↔ [Gable](https://www.gable.ai/)/[Collibra](https://www.collibra.com/) contracts), [PostgREST](https://docs.postgrest.org/) + [Kong](https://developer.konghq.com/gateway/) (↔ [Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/)), [delta-sharing server](https://github.com/delta-io/delta-sharing) (↔ [Databricks](https://docs.databricks.com/)/[Snowflake](https://docs.snowflake.com/en/user-guide/data-sharing-intro) sharing), [Superset](https://superset.apache.org/) (↔ [Power BI](https://learn.microsoft.com/en-us/power-bi/)), [Streamlit](https://docs.streamlit.io/) console, [Archi](https://www.archimatetool.com/) for the ArchiMate model (↔ [Sparx EA](https://sparxsystems.com/)).
- **Build:** (1) the "Fund NAV & Flows" data product: ODCS contract, SLOs with burn-rate alerting, semantic metrics, owner & glossary links — all visible in the catalog; (2) four consumption channels from one gold source: Superset board dashboard, REST API behind Kong (OIDC + quotas), Delta Share to a "distributor" environment, and EMT/Annex-IV regulatory outputs with validation gates and four-eyes approval; (3) the product console (Streamlit) surfacing health, contract version, and consumers; (4) the architect's portfolio: full C4 set, ArchiMate model + 2 viewpoints, the complete ADR log (001–022+), DDD context map, DCAM assessment + roadmap, build-vs-buy memos, migration (strangler) plan; (5) a 30-minute "architecture walkthrough" deck/script — the artifact you'd present to an interview panel or review board.
- **Architecture deliverables:** ADR-022 product-boundary definition (from the context map), ADR-023 consumption-channel architecture (why four channels, one source), ADR-024 semantic-layer placement (headless vs Power BI, final position).
- **Acceptance criteria:** a cold-start reviewer can: read the contract → consume all four channels → verify an SLO claim from telemetry → trace one EMT figure to source via lineage → find every decision in an ADR; the breaking-change drill fails CI at the contract; the walkthrough survives 10 hard questions you've scripted answers to (CAP misuse, mesh timing, Iceberg-vs-Delta, build-vs-buy × 3, DR cost, GDPR erasure, exactly-once honesty, vendor lock-in).
- Est. hours: 20

*Phase 8 total: 103 h (T1/T2 entries 79 h + T3 4 h + capstone 20 h) + Appendix A items A.7–A.13 (18.5 h) scheduled in this phase*
