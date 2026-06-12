<a id="phase-2"></a>
## Phase 2: Lakehouse & Analytics Engineering (months 12–16, 123 h)

**Goal:** master the open lakehouse stack — object storage, columnar formats, ACID table formats, federated SQL, dbt — and ground the whole plan in the fund-data domain by learning the financial standards the platform will carry (ISO 20022, EMT/EPT, instrument identifiers).
**Entry prerequisites:** Phase 1 (modeling discipline, Postgres internals vocabulary, Docker Compose stack).
**Exit criteria:** you can (1) explain a Parquet footer and an Iceberg snapshot to a skeptic; (2) defend Iceberg vs Delta for a given estate; (3) run a tested, documented dbt project with layered models; (4) design a raw vault for an audit-driven warehouse; (5) read an ISO 20022 message and an EMT file and say where each field lands in your model.

### T1/T2 topics

#### 1.4.3 Medallion architecture — T1
- **Why:** bronze/silver/gold is the default layering of every lakehouse you'll design; the architect's job is making the layer contracts explicit instead of folklore.
- **Learn:** what each layer guarantees (immutability/replayability in bronze; conformance, dedup, DQ-checked in silver; consumption-modeled gold); schema-on-read→write transition point; when medallion is cargo cult (3 layers is a default, not a law); reprocessing strategy per layer.
- **Resource:** Databricks medallion architecture docs + *Fundamentals of Data Engineering* ch. 8 (transformation patterns).
- **Do:** write the layer contract sheet for a fund-data lakehouse: per layer — owner, schema policy, DQ gate, retention, consumer promise.
- **Done when:** you can answer "why not query bronze directly?" with consequences, not dogma.
- Est. hours: 4

#### 3.1.4 Data lakehouse — T1
- **Why:** the lake-with-ACID-tables-plus-warehouse-SQL pattern is the target architecture for fund platforms; you must design one and defend it against both "just use Snowflake" and "just use files."
- **Learn:** lakehouse = object store + open table format + catalog + query engines; what the warehouse still does better (concurrency, fine-grained security, ergonomics); decoupling storage/format/catalog/engine and why open formats de-risk vendor lock-in; Databricks vs Snowflake-with-Iceberg vs Fabric positioning.
- **Resource:** Inmon et al., *Building the Data Lakehouse* (skim for the warehouse-veteran perspective) + the CIDR 2021 "Lakehouse" paper (Armbrust et al.) as the technical core.
- **Tools:** FOSS: MinIO + Iceberg + Trino + DuckDB · Corp: Databricks, Microsoft Fabric/OneLake, Snowflake (evaluation level).
- **Do:** write a 2-page build-vs-buy memo: open lakehouse vs Databricks vs Fabric for a 50-person Luxembourg fund administrator — cost, skills, lock-in, compliance.
- **Done when:** you can name, for each lakehouse component, what breaks if you swap vendors.
- Est. hours: 10

#### 3.1.3 + 3.3.1 Data lake on object storage — T2
- **Why:** object stores are the physical substrate of everything analytical; their semantics (no rename, eventual listing, request pricing) leak into every design above.
- **Learn:** S3 API semantics; durability vs availability tiers; prefixes/partitioning and request costs; multipart upload; lifecycle policies; ADLS Gen2's hierarchical namespace and why it exists.
- **Resource:** MinIO docs (core concepts) + ADLS Gen2 introduction (Microsoft Learn).
- **Tools:** FOSS: MinIO (↔ ADLS Gen2 / S3) · Corp: ADLS Gen2 (primary), S3 (awareness).
- **Do:** run MinIO in compose; write NAV Parquet files into a date-partitioned layout via `uv run` + pyarrow; set a lifecycle rule to expire bronze after 30 days.
- **Done when:** you can explain why "rename a folder" is a problem on S3 but not ADLS Gen2.
- Est. hours: 4

#### 3.1.1 Cloud data warehouse — T2
- **Why:** even lakehouse-first shops keep a warehouse; you'll be asked to compare Snowflake/BigQuery/Synapse credibly in vendor selection.
- **Learn:** Snowflake's three-layer architecture (services/compute/storage), credits and warehouses; BigQuery's serverless slots model; Synapse dedicated vs serverless; micro-partitions and clustering vs partitioning; what each prices and how runaway cost happens.
- **Resource:** Snowflake "Key Concepts & Architecture" docs + BigQuery "Under the hood" architecture docs.
- **Tools:** FOSS: DuckDB as a stand-in for exercises · Corp: Snowflake, BigQuery, Synapse/Fabric Warehouse (evaluation level).
- **Do:** one-page comparison table (architecture, pricing unit, workload isolation, Iceberg story, EU-region/compliance posture) for the three.
- **Done when:** you can explain to a CFO why Snowflake costs are workload-shaped, not data-shaped.
- Est. hours: 4

#### 3.4.1 File formats — T1
- **Why:** Parquet internals (row groups, encodings, statistics, pushdown) are where storage cost and query latency are actually decided; architects who can't read a footer argue from vibes.
- **Learn:** Parquet structure: row groups, column chunks, pages, dictionary/RLE encodings, min/max stats, predicate & projection pushdown; compression tradeoffs (snappy/zstd); Avro as row-oriented schema-evolution format and where it fits (Kafka, landing); Arrow as the in-memory interchange standard; ORC awareness.
- **Resource:** Parquet official format docs + DuckDB blog posts on Parquet internals. *Alternate:* *Fundamentals of Data Engineering* ch. 6.
- **Tools:** FOSS: pyarrow, DuckDB, `parquet-tools` · Corp: same formats everywhere (this knowledge is vendor-neutral by design).
- **Do:** with pyarrow via `uv run`, write the same 10M-row holdings table at three row-group sizes and two compressions; measure file size and a filtered-scan time in DuckDB; inspect footers and explain results.
- **Done when:** given a slow lake query, you check row-group pruning before blaming the engine.
- Est. hours: 8

#### 3.4.2 Table formats (Iceberg, Delta) — T1
- **Why:** the ACID metadata layer is the heart of the lakehouse — snapshots, schema evolution, time travel, and compaction are what you'll design, operate, and debug.
- **Learn:** Iceberg metadata tree (metadata file → manifest list → manifests → data files); snapshots & time travel; hidden partitioning and partition evolution; copy-on-write vs merge-on-read; compaction/maintenance; schema evolution rules; Delta log model and UniForm; Hudi at awareness level; format-war state of play.
- **Resource:** Iceberg official docs (spec + "Maintenance") + Tabular/Iceberg blog series. *Alternate:* *Apache Iceberg: The Definitive Guide* (O'Reilly, free via Dremio).
- **Tools:** FOSS: Iceberg on MinIO via Trino; Delta via DuckDB/`delta-rs` · Corp: Databricks Delta, Snowflake managed Iceberg, Fabric OneLake (evaluation level).
- **Do:** create an Iceberg NAV table via Trino; run UPDATE/DELETE/MERGE; time-travel to pre-update; evolve schema (add column, change partition spec); inspect the metadata JSON/manifests on MinIO and narrate the tree.
- **Done when:** you can debug "why is this table slow/huge" from manifests alone, and write the Iceberg-vs-Delta ADR for a given estate.
- Est. hours: 12

#### 3.4.3 Table-format catalogs — T2
- **Why:** the catalog is the new lock-in battleground; whoever owns the catalog owns the lakehouse — a vendor-selection conversation you must lead.
- **Learn:** what a catalog tracks (namespaces, table pointers, snapshots); Iceberg REST catalog spec as the decoupling standard; Polaris, Unity Catalog OSS, Lakekeeper, Nessie positioning; credential vending; why engine-bundled catalogs recreate lock-in.
- **Resource:** Iceberg REST catalog spec + Apache Polaris docs (overview).
- **Tools:** FOSS: Lakekeeper or Polaris in compose · Corp: Unity Catalog (Databricks), AWS Glue, Snowflake Open Catalog (evaluation level).
- **Do:** swap your capstone's catalog (e.g., Trino's Hive-style catalog → Lakekeeper REST) and document what changed and what didn't.
- **Done when:** you can explain credential vending and why the catalog, not the format, decides openness.
- Est. hours: 4

#### 4.3.1 MPP/federated SQL engines (Trino) — T2
- **Why:** Trino is the open federation engine (and the heart of Starburst/Athena); it queries the lakehouse and Postgres in one statement — the practical face of "decoupled compute."
- **Learn:** coordinator/worker architecture; connectors and pushdown; memory model and spill; Iceberg connector specifics; cost-based optimizer basics; when federation is an anti-pattern (chatty joins across stores).
- **Resource:** Trino official docs ("Overview" + "Iceberg connector") . *Alternate:* *Trino: The Definitive Guide* (free via Starburst).
- **Tools:** FOSS: Trino (↔ Starburst Enterprise, AWS Athena) · Corp: Starburst, Athena, Synapse serverless (evaluation level).
- **Do:** add Trino to compose; join Postgres fund reference data to Iceberg NAV history in one query; compare with copying the dimension into Iceberg first.
- **Done when:** you can predict which predicates push down to each source and verify with EXPLAIN.
- Est. hours: 5

#### 4.3.3 Embedded analytical engines (DuckDB) — T2
- **Why:** DuckDB is the architect's pocket warehouse — local development, testing, and a legitimate production pattern for mid-size workloads; knowing its limits sharpens every "do we need a cluster?" conversation.
- **Learn:** in-process model; out-of-core execution; reading Parquet/Iceberg/Delta directly; extension ecosystem; single-writer constraint; MotherDuck awareness; ClickHouse as the server-side single-node speed king (awareness).
- **Resource:** DuckDB official docs ("Why DuckDB" + Parquet/extensions pages).
- **Tools:** FOSS: DuckDB · Corp: MotherDuck, ClickHouse Cloud (awareness).
- **Do:** benchmark the Phase-1 mart queries: DuckDB-over-Parquet vs Postgres; write 5 bullets on when each wins.
- **Done when:** you can articulate the data size/concurrency envelope where "no cluster" is the right architecture.
- Est. hours: 3

#### 5.2.1 + 5.3.1 dbt & the SQL transformation layer — T1
- **Why:** dbt is the modeling-to-production bridge you already started; mastery (not usage) is what lets you set standards for a whole analytics team.
- **Learn:** project structure conventions (staging/intermediate/marts mirroring medallion); ref graph & materializations (view/table/incremental/snapshot — incremental strategies and their failure modes); tests (generic, singular, unit tests); dbt snapshots = SCD2; docs & exposures; packages (dbt-utils, dbt-expectations); semantic conventions; SQLMesh as the challenger (virtual environments, column-level lineage) at evaluation level.
- **Resource:** Cyr & Dorsey, *Analytics Engineering with SQL and dbt* (full) + official dbt best-practice guides.
- **Tools:** FOSS: dbt Core + dbt-duckdb/dbt-trino; SQLMesh (eval) · Corp: dbt Cloud, Coalesce, Dataform (evaluation level).
- **Do:** rebuild the Phase-1 mart as a layered dbt project on DuckDB: sources with freshness checks, staging→marts, snapshot-based SCD2 fund dimension, tests on every model, generated docs.
- **Done when:** `dbt build` is green from scratch, the DAG is readable by a stranger, and you can explain why each model has its materialization.
- Est. hours: 14

#### 5.2.2 Orchestrated ELT (build-vs-buy) — T2
- **Why:** "Fivetran + dbt" is the default managed pattern; you must price it against self-hosted connectors for a regulated EU estate.
- **Learn:** MAR-based pricing mechanics; connector reliability economics; when managed ELT wins (long-tail SaaS sources) vs loses (core banking, mainframe, data sovereignty).
- **Resource:** Fivetran pricing/architecture docs + Airbyte deployment docs (comparison read).
- **Do:** half-page build-vs-buy note for a fund admin with 6 internal systems and 4 SaaS sources.
- **Done when:** you can state the crossover point where Fivetran's cost beats an engineer maintaining Airbyte.
- Est. hours: 2

#### 2.1.1 Batch ELT connectors — T2
- **Why:** connector platforms are the workhorse of non-streaming ingestion; hands-on Airbyte makes the managed-vendor conversation concrete.
- **Learn:** connector model (source/destination/spec/state); incremental sync modes and cursor fields; CDC-flavored connectors vs true CDC; schema-change handling; operating cost of self-hosted connectors.
- **Resource:** Airbyte docs (core concepts + incremental sync).
- **Tools:** FOSS: Airbyte OSS (↔ Fivetran, Stitch, ADF copy activity) · Corp: Fivetran (evaluation level).
- **Do:** stand up Airbyte in compose; sync the Phase-1 Postgres to MinIO Parquet incrementally; break the cursor on purpose and repair it.
- **Done when:** you can explain how state is kept and what happens on a re-sync after schema change.
- Est. hours: 4

#### 8.2.5 Data Vault modeling (+ 1.4.7 pattern) — T1
- **Why:** Data Vault is the financial-services-favored EDW pattern — auditability by construction, multi-source integration without re-modeling — and Luxembourg shops ask for it by name.
- **Learn:** hubs (business keys), links (relationships), satellites (history & context); raw vault vs business vault; hash keys & hashdiffs; loading patterns (parallel, insert-only); PIT and bridge tables for query performance; when Vault is overkill (single-source, small team); Vault-on-lakehouse with dbt (AutomateDV).
- **Resource:** Linstedt & Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0*, ch. 1–7 (modeling) + ch. 11–12 (loading).
- **Tools:** FOSS: dbt + AutomateDV package · Corp: VaultSpeed, WhereScape, Datavault Builder (evaluation level).
- **Do:** model fund/share-class/administrator from two conflicting source systems as a raw vault (hubs/links/sats) with AutomateDV; build one PIT table; show that a late-arriving correction is fully auditable.
- **Done when:** you can defend hub key choices for messy real-world identifiers (ISIN reuse, internal codes) and explain insert-only loading to an auditor.
- Est. hours: 12

#### 1.12.1 ISO 20022 — T1
- **Why:** the lingua franca of EU payments and securities messaging — fund platforms ingest and emit it; post-MT migration it is *the* message standard your models must align to.
- **Learn:** message taxonomy (pacs/camt/sese/semt/setr business areas — which matter for funds: setr orders, semt statements, sese settlement); XSD structure, business components, external code sets; the e-Repository and Message Definition Reports; mapping messages to canonical models; MX-over-SWIFT context.
- **Resource:** iso20022.org — Message Definition Report for setr (investment funds) + the "ISO 20022 for Dummies" SWIFT booklet (free PDF).
- **Do:** parse a sample `setr.010` (subscription order) with Python/lxml via `uv run`; map every business field onto your Phase-1 model; document gaps your model can't hold.
- **Done when:** you can sketch the message flow (order → status → confirmation → settlement) for a fund subscription and name the message types at each hop.
- Est. hours: 6

#### 1.12.7 EMT / EPT (FinDatEx) — T1
- **Why:** EMT (MiFID target market/costs) and EPT (PRIIPs KID data) are the fund-data dissemination templates of the EU industry — the exact artifacts a Luxembourg fund-data platform produces and consumes daily.
- **Learn:** FinDatEx governance and template lifecycle/versioning; EMT structure (manufacturer target market, costs & charges blocks); EPT structure (KID inputs: SRI, performance scenarios, costs); CEPT/delta templates; how distributors consume them; data-quality pain points (versioning, partial files, code lists).
- **Resource:** findatex.eu — current EMT and EPT template specifications (free downloads).
- **Do:** build a dbt model set that produces a valid EMT V4-shaped output from your fund mart; validate column-by-column against the spec.
- **Done when:** you can explain to a product manager which upstream attributes block EMT completion and what "regulatory data product" means concretely.
- Est. hours: 5

#### 1.12.2 + 1.12.3 LEI & ISIN (entity and instrument identity) — T2
- **Why:** identifier discipline is the difference between a fund platform and a data swamp; LEI and ISIN are the join keys of the industry.
- **Learn:** ISIN structure/allocation (and why ISIN ≠ listing — venue-level FIGI/MIC); LEI structure, GLEIF registry, Level 1/Level 2 (who-owns-whom) data; validation (check digits); identifier lifecycle events (corporate actions renaming ISINs).
- **Resource:** GLEIF site (LEI intro + Level 2 data docs) + ANNA ISIN guidelines.
- **Do:** download the GLEIF golden copy (free), load it to your lakehouse bronze, and link your Faker funds to real LEIs of their (fictive) management companies.
- **Done when:** you can explain why a security master needs both ISIN and an internal surrogate, with a concrete corporate-action scenario.
- Est. hours: 2

#### 1.12.8 SWIFT MT / MX — T2
- **Why:** legacy MT messages still flow through fund operations (TA, custody); architects must read both worlds during the long MX coexistence.
- **Learn:** MT message anatomy (blocks, tags) for the fund-relevant set (MT502/509/515 orders, MT535/536 statements); MX = ISO 20022 over SWIFT; translation/coexistence rules; what SWIFT network membership means operationally.
- **Resource:** SWIFT standards documentation (MT category 5 overview) — free with registration.
- **Do:** hand-translate an MT535 holdings statement into your model's terms; note the lossy fields.
- **Done when:** you can read an MT message with the spec open and know which MX message replaces it.
- Est. hours: 2

#### 9.6.2 Data documentation — T2
- **Why:** generated, always-current documentation is a governance deliverable; dbt docs is the gateway drug before Phase 6 catalogs.
- **Learn:** dbt docs generation/persistence (`persist_docs`); exposures to declare downstream consumers; what belongs in model YAML vs the catalog; docs-as-code review flow.
- **Resource:** dbt docs documentation + "exposures" guide.
- **Tools:** FOSS: dbt docs (↔ catalog-generated docs in Phase 6) · Corp: dbt Cloud docs / Purview-generated lineage views.
- **Do:** fully document the capstone dbt project (every model + column description, one exposure for the EMT output) and publish the static site from CI later in Phase 3.
- **Done when:** a business analyst can answer "where does this EMT field come from?" without asking you.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.4.6 | Hub-and-spoke | Centralized hub feeding domain marts; the pre-mesh enterprise default | *Data Management at Scale* ch. 2 (architecture survey) | 20 |
| 1.12.4 | CFI (ISO 10962) | 6-char instrument classification code carried in reference data | ANNA CFI overview page | 20 |
| 1.12.5 | FIGI | Bloomberg's open venue-level instrument identifier; ISIN complement | openfigi.com overview | 20 |
| 1.12.9 | FpML | ISDA XML for OTC derivatives; appears at fund boundaries (hedging) | fpml.org "What is FpML" | 20 |
| 1.12.10 | FIX | Trading-venue messaging protocol; upstream of fund data, rarely modeled by you | fixtrading.org online spec intro | 20 |
| 1.12.11 | IBAN / SEPA | Payment-account identity standard underpinning EU cash legs | ECB SEPA overview | 15 |
| 3.1.2 | On-prem MPP warehouses | Teradata/Vertica/Netezza estates you'll migrate *from* | Teradata architecture overview | 30 |
| 3.2.11 | Geospatial storage | PostGIS/GeoParquet/H3; ESG & real-asset edge cases in funds | PostGIS "What is" + GeoParquet README | 30 |
| 5.3.3 | PRQL / Malloy | Composable query-language challengers to SQL | prql-lang.org tour | 20 |
| 5.4.1 | Interactive data prep | Visual cleanup tools (Alteryx/DataBrew) bought by business teams | Alteryx product overview | 15 |
| 8.2.6 | Anchor modeling / 6NF | Fully temporal modeling; Data Vault's stricter cousin | anchormodeling.com intro | 30 |

*T3 subtotal: 4 h*

### Capstone 2 — Fund-document lakehouse

- **Goal:** a working open lakehouse carrying real fund-data shapes (NAV series, holdings, EMT outputs, GLEIF entities) through bronze→silver→gold, with the format/catalog decisions documented like a vendor selection.
- **Stack (100% free):** MinIO (↔ ADLS Gen2), Apache Iceberg (↔ Databricks Delta / Snowflake managed Iceberg), Lakekeeper or Polaris REST catalog (↔ Unity Catalog / Glue), Trino (↔ Starburst / Athena / Synapse serverless), DuckDB + dbt Core (↔ dbt Cloud on a warehouse), Airbyte OSS (↔ Fivetran / ADF), AutomateDV raw-vault slice (↔ VaultSpeed), Docker Compose throughout.
- **Build:** (1) Airbyte lands Phase-1 Postgres + GLEIF golden copy into bronze (Parquet on MinIO); (2) silver Iceberg tables: cleansed NAV/holdings with DQ-checked conformance, raw vault for fund/share-class from two "source systems"; (3) gold: dbt marts incl. the EMT-shaped output and the SCD2 dimensional mart; (4) Trino federates a live Postgres dimension against Iceberg facts; (5) demonstrate time travel + schema evolution + a compaction run.
- **Architecture deliverables:** C4 context/container for the lakehouse; ADR-004 Iceberg vs Delta (estate-specific), ADR-005 REST catalog choice (lock-in analysis), ADR-006 medallion layer contracts (the sheet from 1.4.3 made binding).
- **Acceptance criteria:** end-to-end rebuild from empty MinIO via documented commands; `dbt build` green with tests + docs published; EMT output validates against the FinDatEx column spec; time-travel query reproduces yesterday's NAV report after a correction lands; every stack component annotated with its corporate equivalent in the README.
- Est. hours: 16

*Phase 2 total: 123 h (T1/T2 entries 103 h + T3 4 h + capstone 16 h)*
