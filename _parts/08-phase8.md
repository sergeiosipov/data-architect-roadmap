<a id="phase-8"></a>
## Phase 8: Data Products, Semantic Layer & the Architect's Practice (months 44–48, 103 h + 18.5 h Appendix A)

**Goal:** convert the governed platform into *products* — contracted, SLA-backed, semantically defined, consumable — and consolidate the formal architect's practice: DDD for boundaries, TOGAF/ArchiMate for the enterprise conversation, regulatory reporting as the domain's flagship deliverable, and the build-vs-buy fluency that Appendix D distills.
**Entry prerequisites:** Phases 1–7 (everything; this phase productizes the accumulated platform).
**Exit criteria:** you can (1) cut data-product boundaries with DDD and defend them; (2) publish a data product with an enforced contract, SLOs, and a semantic layer; (3) design a submission-grade regulatory reporting pipeline; (4) speak TOGAF/ArchiMate fluently in an EA forum; (5) win a build-vs-buy argument in any taxonomy domain with named tools and costs.
**Appendix A items scheduled here:** A.7 architecture styles & trade-off analysis, A.8 business architecture, A.9 EA governance, A.10 roadmapping & migration planning, A.11 agile EA, A.12 OWASP API security, A.13 ITSM/delivery frameworks (18.5 h).

### T1/T2 topics

#### 8.4.1 Domain-driven design — T1
- **Why:** bounded contexts are how you cut data-product and team boundaries that survive reorgs; DDD's strategic patterns are the intellectual foundation under data mesh — and the difference between domain-oriented design and folder renaming.
- **Learn:** strategic DDD only, deeply: ubiquitous language; bounded contexts & context mapping (partnership, customer-supplier, conformist, ACL, published language); subdomain types (core/supporting/generic) and investment logic; EventStorming as the discovery workshop (your BA superpower, formalized); aggregates at concept level; applying it to data: source-aligned vs aggregate vs consumer-aligned products; the fund-administration domain map (TA, fund accounting, custody, regulatory reporting, client reporting).
- **Resource:** Vlad Khononov, *Learning Domain-Driven Design* (strategic chapters 1–11) . *Alternate:* Evans for reference; *Data Mesh* ch. 2 for the data application.
- **Tools:** FOSS: EventStorming (paper/Miro-free-tier) + Context Mapper DSL (↔ — no corp equivalent; this is method).
- **Do:** run a solo EventStorming of the subscription-order-to-NAV flow; derive the context map for a fund administrator (5–7 contexts with relationship types); mark which contexts own which data products.
- **Done when:** your context map survives the challenge "why is fund accounting not part of the TA context?" with a domain answer, not an org-chart answer.
- Est. hours: 10

#### 13.1.1 + 13.1.2 Data contracts (ODCS, enforcement) — T1
- **Why:** contracts operationalize everything Phase 6 built — they are the mechanism that turns "governed dataset" into "product a consumer can rely on," and the EU fund-data world (EMT files between manufacturers and distributors!) has run on implicit contracts for years.
- **Learn:** contract anatomy: schema, semantics, quality guarantees, SLAs, ownership, terms of use; ODCS (Bitol/Linux Foundation) structure and the Data Contract Specification; datacontract-cli: authoring, validation, breaking-change detection, tests against live data; enforcement points: producer CI (schema diff), registry (Kafka), WAP gate (lakehouse), dbt model contracts; contract-first vs contract-extracted adoption paths; versioning & deprecation policy (ties to your 1.9.7 evolution policy — same policy, now productized).
- **Resource:** Andrew Jones, *Driving Data Quality with Data Contracts* + ODCS spec (bitol-io.github.io) + datacontract-cli docs.
- **Tools:** FOSS: datacontract-cli + dbt model contracts + Confluent SR (↔ Gable, DataHub contracts, Confluent data contracts).
- **Do:** write the ODCS contract for your gold NAV mart and the EMT output (schema + DQ guarantees + freshness SLO + owner + license terms); wire `datacontract test` into CI against the live lakehouse; demonstrate a breaking change being caught pre-merge.
- **Done when:** a consumer can subscribe to your product knowing exactly what is guaranteed, and a producer cannot break it silently — both demonstrated, not asserted.
- Est. hours: 10

#### 14.4.2 Regulatory reporting — T1
- **Why:** submission-grade reporting (AIFMD Annex IV, PRIIPs KID/EPT, MiFID/EMT) is the fund-data domain's flagship deliverable — deadline-driven, auditor-reviewed, and the workload your whole platform exists to serve.
- **Learn:** what makes reporting "submission-grade": completeness gates, plausibility checks, four-eyes approval, resubmission/correction workflow, full lineage to source, immutable filing archive; the EU fund reporting landscape concretely: AIFMD Annex IV (scope, frequency, XML), PRIIPs KID data (EPT — your Phase-2 work), EMT distribution, SFDR templates (ESG data sourcing pain); report calendars & deadline orchestration (your Dagster schedules grow teeth); the vendor landscape: Workiva/AxiomSL(Adenza)/Wolters Kluwer/Vermeg — what they actually sell (forms engines + rule updates + filing connectivity) and what stays your problem (the data); build-vs-buy economics (rule-maintenance burden is the buy argument).
- **Resource:** ESMA AIFMD reporting guidelines page (IT technical guidance + Annex IV templates, free) + your Phase-2 FinDatEx specs, reread as a producer.
- **Tools:** FOSS: the platform you built + Dagster scheduling (↔ Workiva, AxiomSL, Wolters Kluwer OneSumX — evaluation level).
- **Do:** design and implement the Annex-IV-shaped pipeline: gold marts → validation gates (completeness/plausibility) → XML rendering against the published schema → four-eyes approval step (Dagster sensor + manual gate) → immutable filing archive with lineage snapshot; write the build-vs-buy memo for the forms-engine layer.
- **Done when:** a deliberately incomplete dataset cannot reach the filing stage; a resubmission is traceable end-to-end; and your memo prices the vendor option honestly.
- Est. hours: 10

#### 8.1.3 Industry frameworks (TOGAF & ArchiMate, working fluency) — T2
- **Why:** TOGAF/ArchiMate is the lingua franca of EA departments in EU financial institutions; the architect who can't speak it gets translated by someone who can.
- **Learn:** TOGAF 10 shape: ADM cycle (what each phase produces — focus on B/C data architecture, E/F via A.10), architecture repository/landscape, building blocks; what to take seriously (deliverable discipline, governance hooks) vs hold lightly (the full ceremony); ArchiMate 3.2: core layers (business/application/technology), the data-relevant elements (business object ↔ data object ↔ artifact), viewpoints; modeling your platform in Archi; mapping C4 ↔ ArchiMate (when each audience needs which).
- **Resource:** TOGAF 10 Fundamental Content: Introduction & Core Concepts + ADM (free with Open Group registration) + Archi tool + its "hello ArchiMate" tutorial.
- **Tools:** FOSS: Archi (↔ Sparx EA, BiZZdesign — the licensed EA suites).
- **Do:** model your entire capstone platform in ArchiMate (application + technology layers, data objects for the products) and produce two viewpoints: one for the COO (business-application), one for security (technology).
- **Done when:** you can walk an EA review board through the ArchiMate model and translate any element to/from your C4 diagrams live.
- Est. hours: 10

#### 1.4.4 Data mesh (and 13.2.1 enabling platforms) — T2
- **Why:** mesh is the organizational scaling answer you'll be asked about in every large-firm interview; the architect's job is knowing when its costs are justified — and what "federated computational governance" means after Phase 6.
- **Learn:** the four principles (domain ownership, data as product, self-serve platform, federated computational governance) read against your build: you have already built principles 2–4 single-domain; what changes multi-domain; mesh failure modes (mesh-washing, platform-team starvation, premature decentralization); enabling platforms: Starburst/Trino federation, Databricks UC domains, your OpenMetadata domains; sizing test: when a 50-person fund admin should *not* mesh.
- **Resource:** Dehghani, *Data Mesh* (part I–II; skim III) + *Data Management at Scale* 2nd ed. (Strengholt's pragmatic counterweight).
- **Do:** write the two-page memo: "Should a 300-person fund administrator adopt mesh?" — org sizing, domain map (from your DDD work), platform prerequisites, and an honest no/not-yet/yes-partially recommendation.
- **Done when:** you can argue both for and against mesh for the same firm, and name the organizational precondition that decides it.
- Est. hours: 5

#### 7.1.1 + 7.2.1 Semantic & metrics layer (Cube, MetricFlow) — T2
- **Why:** "one definition of AUM" is a governance promise only a semantic layer can keep across BI tools, APIs, and notebooks; headless BI is the architectural pattern behind it.
- **Learn:** semantic-layer anatomy: dimensions, measures, joins, access control at the semantic level; Cube: data models, pre-aggregations, REST/SQL APIs, caching; MetricFlow/dbt Semantic Layer: metric definitions in the dbt DAG; metrics layer vs BI-tool-local definitions (the consistency argument); semantic layer vs glossary (definition *executed* vs definition *documented* — link them); when the semantic layer is premature.
- **Resource:** Cube docs (data modeling section) + dbt Semantic Layer/MetricFlow docs.
- **Tools:** FOSS: Cube + MetricFlow (↔ Looker/LookML, AtScale, Power BI semantic models).
- **Do:** define NAV, AUM, and net-flows once in Cube over the gold marts; consume them from three clients (Superset, a REST call, a notebook) and show identical numbers; link each metric to its glossary term.
- **Done when:** changing the AUM definition in one place changes it everywhere, with an audit trail.
- Est. hours: 7

#### 7.1.2 Platform semantic layers (Power BI semantic models) — T2
- **Why:** in Azure shops the Power BI semantic model *is* the de-facto semantic layer; you must know when it suffices and when headless wins.
- **Learn:** Power BI semantic models: import vs DirectQuery vs Direct Lake (Fabric tie to A.4); star-schema expectations (your Kimball work pays off); RLS in the model; deployment pipelines & XMLA endpoint; the "semantic model sprawl" failure mode and certified-dataset governance; Power BI vs headless decision rubric.
- **Resource:** Microsoft Learn: Power BI semantic model guidance (star schema + model management pages).
- **Tools:** Corp: Power BI (primary; free Desktop suffices for the exercise) (↔ FOSS: Cube from previous entry).
- **Do:** build the NAV mart semantic model in Power BI Desktop (free) with RLS by management company; document where its definitions and your Cube definitions could drift and the governance rule preventing it.
- **Done when:** you can rule "Power BI model vs headless layer" for three org shapes and defend it.
- Est. hours: 4

#### 12.4.1 Data SLAs & SLO management — T2
- **Why:** the SLO machinery (Phase 5 vocabulary) becomes contractual here: freshness/completeness targets with error budgets are what "productized" means operationally.
- **Learn:** data SLIs (freshness, completeness, accuracy proxy, availability of the serving layer); setting SLOs consumers actually need (interview them — BA skills) vs vanity nines; error budgets for data (when to freeze risky pipeline changes); SLO surfacing in catalog + contract; alerting on burn rate, not point failures.
- **Resource:** Google SRE Workbook SLO chapters (free online), translated to data in your contract from 13.1.1.
- **Do:** define SLOs for the NAV product (e.g., 99% of business days fresh by 08:00 CET), instrument them from the Phase-5/6 telemetry, and add a burn-rate alert; record one month of synthetic compliance.
- **Done when:** the product page shows measured SLO attainment, and a simulated bad week visibly consumes error budget with a documented response.
- Est. hours: 3

#### 13.3.2 Cross-org data sharing (Delta Sharing) — T2
- **Why:** fund data is *disseminated* — to distributors, platforms, regulators; open sharing protocols are the modern alternative to the SFTP-and-CSV folklore the industry still runs on.
- **Learn:** Delta Sharing protocol (open, REST-based, format-level); shares/recipients/governance; Snowflake shares & Databricks marketplace as the walled-garden equivalents; egress economics; sharing vs API vs file-drop decision rubric (volume, latency, consumer sophistication); contractual overlay (ties 13.1.1, A.18).
- **Resource:** Delta Sharing docs (open protocol) + Snowflake secure-sharing docs (comparison read).
- **Tools:** FOSS: delta-sharing reference server (↔ Databricks Delta Sharing, Snowflake shares, Fabric external sharing).
- **Do:** stand up the reference sharing server over a gold Delta table; consume it from a separate "distributor" environment with pandas; write the rubric: when sharing protocol vs API vs EMT file-drop.
- **Done when:** you can design the dissemination architecture for a fund manufacturer with 40 distributor relationships and defend the channel per consumer class.
- Est. hours: 3

#### 13.4.2 + 2.6.1 Data APIs & gateways (data-as-a-service) — T2
- **Why:** the API is the product surface for operational consumers (websites, partner systems); the gateway is where auth, quotas, and versioning live — an architect's checklist, not a developer's tutorial.
- **Learn:** productized data API design: resource modeling for fund data (funds/share-classes/navs), pagination, filtering, versioning policy (ties 1.9.7), OpenAPI as the contract; gateway duties: OIDC token validation (your Keycloak), rate limiting/quotas per consumer tier, usage analytics for chargeback; PostgREST/FastAPI as instant serving over gold views; caching policy (your 3.3.4 decision); when GraphQL earns its complexity (2.6.2 stays T3).
- **Resource:** Kong OSS docs (gateway concepts) + PostgREST docs.
- **Tools:** FOSS: PostgREST or FastAPI + Kong OSS (↔ Azure API Management, Apigee).
- **Do:** expose the NAV product as a read-only REST API (PostgREST over a gold view) behind Kong with OIDC + rate limits; publish its OpenAPI document; run the OWASP API Top-10 checklist (A.12) against it.
- **Done when:** an external consumer can onboard from the OpenAPI doc + contract alone, and the gateway proves quota enforcement in logs.
- Est. hours: 5

#### 14.1.1 + 14.1.3 Business intelligence (Superset hands-on, Power BI fluency) — T2
- **Why:** BI is where your platform meets its judges; the architect doesn't build dashboards for a living but must design the BI tier (tooling, governance, self-service boundaries) and read the vendor market.
- **Learn:** Superset: datasets/charts/dashboards, semantic-ish layer, RLS, embedding; Power BI ecosystem economics (per-user vs capacity/Fabric licensing — the real selection driver in Azure shops); Tableau/Looker/Qlik positioning in one sitting; governed self-service: certified datasets, sandbox vs production content, the "300 unowned dashboards" failure mode; BI-on-semantic-layer (consume Cube, don't re-model).
- **Resource:** Superset docs (creating charts/dashboards + security) + Power BI licensing/deployment guidance page.
- **Tools:** FOSS: Apache Superset, Metabase (↔ Power BI [Azure default], Tableau, Looker) · Corp: Power BI (primary evaluation).
- **Do:** build the fund-board dashboard (NAV trend, flows, DQ status) in Superset *on top of Cube*; write the BI governance one-pager (certification workflow, ownership, sandbox policy).
- **Done when:** the dashboard consumes only semantic-layer metrics (zero local SQL definitions), and your governance pager answers "who may publish what, where".
- Est. hours: 7

#### 14.6.1 Data app frameworks (Streamlit) — T2
- **Why:** data apps are the fast path from platform to stakeholder value (review queues, what-if tools); Streamlit is the de-facto standard and your Phase-7 review UI already used it.
- **Learn:** Streamlit execution model (rerun-on-interaction, caching, session state) and its scaling limits; when Streamlit vs Dash vs a real frontend; deployment & auth patterns behind the gateway; the internal-tools landscape (Retool-class) at a glance.
- **Resource:** Streamlit docs (main concepts + caching).
- **Tools:** FOSS: Streamlit (↔ Snowflake-Streamlit, Retool, Power Apps).
- **Do:** build the "fund data product console": SLO status, contract version, DQ results, lineage link, sample data preview — one screen per product, served behind Kong.
- **Done when:** a product owner can answer "is my product healthy and who consumes it?" from the console without touching the platform.
- Est. hours: 3

#### 1.8.11 Strangler fig (legacy replacement strategy) — T2
- **Why:** every Luxembourg estate has a legacy core (TA system, reporting engine) that can only be replaced incrementally; strangler-fig discipline is how migrations avoid big-bang death — and it operationalizes your A.10 roadmapping.
- **Learn:** facade/routing layer placement for data systems (views, CDC-fed parallel run, dual-write avoidance — use your outbox/CDC instead); parallel-run reconciliation as the trust-builder (your Phase-4 reconciliation pattern, reused); cutover & rollback criteria; anti-pattern: strangler that never finishes (sunset discipline).
- **Resource:** Fowler's Strangler Fig article + Azure Architecture Center strangler-fig pattern page.
- **Do:** write the migration ADR for replacing a legacy reporting mart with your gold layer: facade, parallel-run period, reconciliation gates, cutover criteria, rollback plan, sunset date.
- **Done when:** the plan has measurable gates (reconciliation drift thresholds) instead of dates-and-hope.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.4.5 | Data fabric | Metadata-driven unified-access vision (vendor-led counterpoint to mesh) | Gartner-adjacent vendor explainer, read critically | 20 |
| 2.6.2 | GraphQL data layers | Schema-driven query APIs (Hasura); complexity rarely earned for fund data | Hasura "how it works" page | 20 |
| 2.7.1 | Reverse ETL | Warehouse → SaaS sync (Hightouch/Census); CRM-enrichment use cases | Hightouch docs intro | 20 |
| 13.3.1 | Internal data marketplaces | Catalog-with-checkout UX over data products | Atlan/DataHub marketplace blog | 15 |
| 13.3.3 | Commercial data marketplaces | Buying market/ESG data feeds (Snowflake Marketplace, Datarade) | Snowflake Marketplace overview | 20 |
| 13.4.1 | GraphQL DaaS | Productized GraphQL endpoints; see 2.6.2 | covered there | 5 |
| 14.1.2 | Legacy enterprise BI | BusinessObjects/Cognos/MicroStrategy estates you'll migrate from | one vendor-positioning overview | 20 |
| 14.2.1 | Visualization libraries | Plotly/Vega/D3 programmatic charting; Storytelling-with-Data principles | *Storytelling with Data* ch. 1–2 skim | 45 |
| 14.3.1 | Embedded analytics | BI inside products (Superset/Cube embed, Looker embed) | Cube embedding docs page | 20 |
| 14.4.1 | Operational/paginated reporting | Pixel-perfect statements (Power BI paginated, Jasper) | Power BI paginated reports overview | 20 |
| 14.5.1 | Cloud notebooks | Hex/Deepnote collaborative analysis; governance angle (where results live) | Hex product overview | 15 |
| 14.6.2 | Low-code internal tools | Retool/Appsmith CRUD builders on governed APIs | Appsmith overview | 15 |
| 14.7.2 | Reverse-ETL activation | Acting on data signals in operational tools; see 2.7.1 | covered there | 5 |

*T3 subtotal: 4 h*

### Capstone 8 — The fund data product (end state)

- **Goal:** the four-year arc closes: one fund data product, productized end-to-end — contracted, SLO-backed, semantically defined, multi-channel (BI, API, sharing, EMT file), regulator-ready, and documented like the portfolio piece it is.
- **Stack (100% free):** everything already running, plus Cube + MetricFlow (↔ Looker/AtScale/Power BI semantic models), datacontract-cli + ODCS (↔ Gable/Collibra contracts), PostgREST + Kong (↔ Azure API Management), delta-sharing server (↔ Databricks/Snowflake sharing), Superset (↔ Power BI), Streamlit console, Archi for the ArchiMate model (↔ Sparx EA).
- **Build:** (1) the "Fund NAV & Flows" data product: ODCS contract, SLOs with burn-rate alerting, semantic metrics, owner & glossary links — all visible in the catalog; (2) four consumption channels from one gold source: Superset board dashboard, REST API behind Kong, Delta Share to a "distributor", EMT/Annex-IV regulatory outputs with validation gates and four-eyes approval; (3) the product console (Streamlit); (4) the architect's portfolio: full C4 set, ArchiMate model + 2 viewpoints, the complete ADR log (001–022+), DDD context map, DCAM assessment + roadmap, build-vs-buy memos, migration (strangler) plan; (5) a 30-minute "architecture walkthrough" deck/script — the artifact you'd present to an interview panel or review board.
- **Architecture deliverables:** ADR-022 product-boundary definition (from the context map), ADR-023 consumption-channel architecture (why four channels, one source), ADR-024 semantic-layer placement (headless vs Power BI, final position).
- **Acceptance criteria:** a cold-start reviewer can: read the contract → consume all four channels → verify an SLO claim from telemetry → trace one EMT figure to source via lineage → find every decision in an ADR; the breaking-change drill fails CI at the contract; the walkthrough survives 10 hard questions you've scripted answers to (CAP misuse, mesh timing, Iceberg-vs-Delta, build-vs-buy × 3, DR cost, GDPR erasure, exactly-once honesty, vendor lock-in).
- Est. hours: 20

*Phase 8 total: 103 h (T1/T2 entries 79 h + T3 4 h + capstone 20 h) + Appendix A items A.7–A.13 (18.5 h) scheduled in this phase*
