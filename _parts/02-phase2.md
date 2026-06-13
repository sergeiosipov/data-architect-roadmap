<a id="phase-2"></a>
## Phase 2: Lakehouse & Analytics Engineering (months 12–16, 123 h)

*Phase 2 of 8 · months 12–16 · 123 h · capstone: Fund-document lakehouse.*  ← [Phase 1](#phase-1) · [Phase 3](#phase-3) →

**Goal:** master the open lakehouse stack — object storage, columnar formats, ACID table formats, federated SQL, dbt — and ground the whole plan in the fund-data domain by learning the financial standards the platform will carry (ISO 20022, EMT/EPT, instrument identifiers).
**Entry prerequisites:** Phase 1 (modeling discipline, Postgres internals vocabulary, Docker Compose stack).
**Exit criteria:** you can (1) explain a Parquet footer and an Iceberg snapshot to a skeptic; (2) defend Iceberg vs Delta for a given estate; (3) run a tested, documented dbt project with layered models; (4) design a raw vault for an audit-driven warehouse; (5) read an ISO 20022 message and an EMT file and say where each field lands in your model.

### T1/T2 topics

#### 1.4.3 Medallion architecture — T1
- **Why:** Bronze/silver/gold is the default layering of every lakehouse you will design, and as architect your job is to make the layer contracts explicit standards instead of tribal folklore. In a regulated fund platform, an undocumented layer boundary is where lineage breaks and an auditor's "where did this NAV figure come from?" goes unanswered. Get the contracts wrong and silver becomes a dumping ground that nobody trusts and everybody queries anyway.
- **Learn:**
    - what each layer guarantees — bronze immutable/replayable, silver conformed/deduped/DQ-checked, gold consumption-modeled *(Databricks: Medallion architecture)*
    - the schema-on-read → schema-on-write transition point — where you stop tolerating drift and start enforcing it *(FoDE ch. 8)*
    - reprocessing strategy per layer — what you can rebuild from source vs what is the source of truth *(Databricks: Medallion architecture)*
    - when medallion is cargo cult — three layers is a sensible default, not a law; some estates need two or four *(FoDE ch. 8)*
    - layer ownership and consumer promises — who can break what, and the SLA each layer offers downstream *(Databricks: Medallion architecture)*
- **Resources:**
    - **[Databricks: Medallion architecture](https://www.databricks.com/glossary/medallion-architecture)** — the canonical bronze/silver/gold definition with per-layer responsibilities (primary)
    - [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) ch. 8 — transformation patterns and where layering fits the wider lifecycle (reference)
- **Do:**
    1. Write a one-page layer-contract sheet for a fund-data lakehouse with one row per layer: owner, schema policy, DQ gate, retention, consumer promise.
    2. For each layer, state exactly what is rebuildable from the layer below and what is a system of record.
    3. Add a concrete fund example per layer (bronze: raw NAV feed file; silver: conformed NAV per share class; gold: EMT-shaped output).
    4. Mark which layer a late-arriving NAV correction enters and how it propagates upward.
- **Done when:**
    - [ ] You can answer "why not query bronze directly?" with consequences, not dogma.
    - [ ] You can name, for your sheet, which layer owns each DQ rule and why.
    - [ ] You can defend a two-layer or four-layer variant for a specific estate.
- Est. hours: 4

#### 3.1.4 Data lakehouse — T1
- **Why:** The lake-with-ACID-tables-plus-warehouse-SQL pattern is the target architecture for most fund platforms, and you will have to design one and defend it against both "just buy Snowflake" and "just use files on a share." Pick wrong and you either pay warehouse prices for cold regulatory archives or lose the concurrency and security a fund administrator needs at month-end. The architect must articulate which component carries which guarantee.
- **Learn:**
    - lakehouse = object store + open table format + catalog + query engines — the four decoupled layers *(Lakehouse paper, CIDR 2021)*
    - what the warehouse still does better — high concurrency, fine-grained security, ergonomics *(Lakehouse paper, CIDR 2021)*
    - why open formats de-risk vendor lock-in — storage/format/catalog/engine can each be swapped independently *(Lakehouse paper, CIDR 2021)*
    - the warehouse-veteran objections — what Inmon-school practitioners distrust about lakes *(Building the Data Lakehouse)*
    - vendor positioning — Databricks vs Snowflake-with-Iceberg vs Fabric/OneLake at architecture level *(Lakehouse paper, CIDR 2021)*
- **Resources:**
    - **[Lakehouse: A New Generation of Open Platforms (CIDR 2021)](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf)** — Armbrust et al.; the technical core of the lakehouse argument (primary)
    - [Building the Data Lakehouse](https://www.oreilly.com/library/view/building-the-data/9781098117290/) — Inmon et al.; skim for the warehouse-veteran perspective and where lakes earn distrust (reference)
- **Tools:**
    - FOSS (hands-on): [MinIO](https://min.io/docs/minio/linux/index.html) + [Apache Iceberg](https://iceberg.apache.org/docs/latest/) + [Trino](https://trino.io/docs/current/) + [DuckDB](https://duckdb.org/docs/) — the four open layers assembled (↔ a managed lakehouse)
    - Corp (evaluate): [Databricks](https://docs.databricks.com/), [Microsoft Fabric / OneLake](https://learn.microsoft.com/fabric/onelake/), [Snowflake](https://docs.snowflake.com/) — what each bundles and where the lock-in sits
- **Do:**
    1. Write a 2-page build-vs-buy memo: open lakehouse vs Databricks vs Fabric for a 50-person Luxembourg fund administrator.
    2. Score each on cost, in-house skills required, lock-in, and EU compliance/data-residency posture.
    3. For each lakehouse component (storage, format, catalog, engine), state what breaks if you swap that vendor.
    4. Make an explicit recommendation with the one risk that would change it.
- **Done when:**
    - [ ] You can name, for each lakehouse component, what breaks if you swap vendors.
    - [ ] You can rebut both "just use Snowflake" and "just use files" with specific consequences.
    - [ ] You can state which component is the genuine lock-in point in a given vendor's bundle.
- Est. hours: 10

#### 3.1.3 + 3.3.1 Data lake on object storage — T2
- **Why:** Object stores are the physical substrate of everything analytical, and their semantics — no atomic rename, eventually consistent listing, per-request pricing — leak upward into every table format and query engine you design. An architect who treats S3/ADLS like a POSIX filesystem produces designs that corrupt under concurrent writers or cost a fortune in LIST calls. In funds, that is the difference between a lakehouse that survives month-end and one that silently drops a NAV file.
- **Learn:**
    - S3 API object semantics — flat key space, no folders, no atomic rename *(MinIO docs: Core Concepts)*
    - durability vs availability tiers and lifecycle policies — how cold regulatory archives get cheap *(MinIO docs: Object Lifecycle Management)*
    - prefixes, partitioning and request costs — why layout choices are cost choices *(MinIO docs: Core Concepts)*
    - multipart upload mechanics — how large NAV/holdings files land reliably *(MinIO docs: Core Concepts)*
    - ADLS Gen2 hierarchical namespace — why atomic directory rename exists and what it buys *(ADLS Gen2 introduction)*
- **Resources:**
    - **[MinIO documentation](https://min.io/docs/minio/linux/index.html)** — S3-compatible object store: core concepts, lifecycle, multipart upload (primary)
    - [Azure Data Lake Storage Gen2 introduction](https://learn.microsoft.com/azure/storage/blobs/data-lake-storage-introduction) — hierarchical namespace and atomic directory operations on Azure (reference)
- **Tools:**
    - FOSS (hands-on): [MinIO](https://min.io/docs/minio/linux/index.html) — the local S3 substrate for the whole phase (↔ ADLS Gen2 / S3)
    - Corp (evaluate): [ADLS Gen2](https://learn.microsoft.com/azure/storage/blobs/data-lake-storage-introduction) — primary cloud target; [S3](https://docs.aws.amazon.com/s3/) — awareness of the de-facto standard
- **Do:**
    1. Run MinIO in Docker Compose and create a bucket for the fund lakehouse.
    2. With `uv run` + pyarrow, write NAV Parquet files into a `dt=YYYY-MM-DD/` date-partitioned key layout.
    3. Set a lifecycle rule to expire bronze objects after 30 days; verify it appears in the bucket config.
    4. List objects under a prefix and note how many LIST/GET calls a date-range scan would cost.
- **Done when:**
    - [ ] You can explain why "rename a folder" is a problem on S3 but a single atomic operation on ADLS Gen2.
    - [ ] You can predict the request-cost shape of a partitioned scan from the key layout.
    - [ ] You can show a working lifecycle rule expiring bronze objects.
- Est. hours: 4

#### 3.1.1 Cloud data warehouse — T2
- **Why:** Even lakehouse-first shops keep a warehouse for high-concurrency BI and fine-grained security, so you will be asked to compare Snowflake/BigQuery/Synapse credibly during vendor selection. Get the pricing model wrong and a fund administrator's month-end reporting spike turns into a budget incident. The architect must explain to a CFO why costs are workload-shaped, not data-shaped.
- **Learn:**
    - Snowflake's three-layer architecture — separate services, compute (warehouses/credits), storage *(Snowflake: Key Concepts & Architecture)*
    - micro-partitions and clustering vs explicit partitioning — how Snowflake prunes without you partitioning *(Snowflake: Key Concepts & Architecture)*
    - BigQuery's serverless slots model — compute as a fungible pool, not a sized cluster *(BigQuery: Introduction)*
    - Synapse dedicated vs serverless and where Fabric Warehouse lands *(BigQuery: Introduction; Snowflake docs)*
    - how runaway cost happens in each — idle warehouses, full scans, unpartitioned queries *(Snowflake: Key Concepts & Architecture)*
- **Resources:**
    - **[Snowflake: Key Concepts & Architecture](https://docs.snowflake.com/en/user-guide/intro-key-concepts)** — the three-layer model, credits, micro-partitions (primary)
    - [BigQuery: Introduction / overview](https://cloud.google.com/bigquery/docs/introduction) — serverless compute/storage separation and the slots model (reference)
- **Tools:**
    - FOSS (hands-on): [DuckDB](https://duckdb.org/docs/) — a local stand-in for warehouse-style exercises
    - Corp (evaluate): [Snowflake](https://docs.snowflake.com/), [BigQuery](https://cloud.google.com/bigquery/docs/introduction), [Synapse / Fabric Warehouse](https://learn.microsoft.com/fabric/data-warehouse/) — at vendor-selection level
- **Do:**
    1. Build a one-page comparison table covering Snowflake, BigQuery, and Synapse/Fabric.
    2. For each, fill in: architecture, pricing unit, workload isolation mechanism, Iceberg/open-format story, EU-region and compliance posture.
    3. Note for each the single most common way costs run away.
- **Done when:**
    - [ ] You can explain to a CFO why Snowflake costs are workload-shaped, not data-shaped.
    - [ ] You can name each engine's pricing unit and workload-isolation mechanism.
    - [ ] You can state each engine's Iceberg story in one sentence.
- Est. hours: 4

#### 3.4.1 File formats — T1
- **Why:** Parquet internals — row groups, encodings, statistics, predicate pushdown — are where storage cost and query latency are actually decided, and an architect who cannot read a footer argues from vibes. In a fund lakehouse, the difference between a holdings scan that prunes row groups and one that reads every byte is the difference between a sub-second mart and a multi-minute one. This knowledge is vendor-neutral and pays off on every engine.
- **Learn:**
    - Parquet physical structure — file → row groups → column chunks → pages, plus the footer *(Parquet format docs)*
    - encodings and statistics — dictionary/RLE, min/max stats, and how they enable pushdown *(Parquet format docs)*
    - predicate and projection pushdown — how the reader skips row groups and columns *(DuckDB docs: Reading Parquet)*
    - compression tradeoffs — snappy vs zstd, size vs CPU *(Parquet format docs)*
    - Avro as the row-oriented schema-evolution format — where it fits (Kafka, landing) *(Parquet format docs)*
    - Arrow as the in-memory interchange standard and ORC at awareness level *(DuckDB docs: Reading Parquet)*
- **Resources:**
    - **[Apache Parquet format documentation](https://parquet.apache.org/docs/)** — the authoritative description of row groups, encodings, stats (primary)
    - [DuckDB docs: Reading Parquet](https://duckdb.org/docs/data/parquet/overview) — pushdown and projection from the reader's side, used in the lab (reference)
    - [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) ch. 6 — file-format context including Avro/ORC tradeoffs (alternate)
- **Tools:**
    - FOSS (hands-on): [pyarrow](https://arrow.apache.org/docs/python/), [DuckDB](https://duckdb.org/docs/), [parquet-tools](https://github.com/apache/parquet-java/tree/master/parquet-tools-deprecated) — write, inspect, and benchmark Parquet
    - Corp (evaluate): same formats everywhere — this knowledge is vendor-neutral by design
- **Do:**
    1. With pyarrow via `uv run`, write the same 10M-row holdings table at three row-group sizes and two compressions (snappy, zstd).
    2. Record file size for each combination.
    3. In DuckDB, run a filtered scan (e.g. one fund, one date range) over each file and measure time.
    4. Inspect the footers (row-group count, min/max stats) and explain the size and time differences from the structure.
- **Done when:**
    - [ ] Given a slow lake query, you check row-group pruning before blaming the engine.
    - [ ] You can read a Parquet footer and state how many row groups a predicate would skip.
    - [ ] You can justify a row-group size and compression choice for a holdings table.
- Est. hours: 8

#### 3.4.2 Table formats (Iceberg, Delta) — T1
- **Why:** The ACID metadata layer is the heart of the lakehouse — snapshots, schema evolution, time travel, and compaction are exactly what you will design, operate, and debug. In a fund platform, time travel is how you reproduce yesterday's NAV report after a correction lands, and a botched compaction is how a table silently triples in size. The Iceberg-vs-Delta decision is an ADR you will own.
- **Learn:**
    - Iceberg metadata tree — metadata file → manifest list → manifests → data files *(Iceberg docs: spec)*
    - snapshots and time travel — how each commit creates an immutable snapshot you can query *(Iceberg docs: spec)*
    - hidden partitioning and partition evolution — changing partitioning without rewriting queries *(Iceberg docs: Partitioning)*
    - copy-on-write vs merge-on-read — the write-vs-read cost tradeoff for UPDATE/DELETE *(Iceberg docs: Configuration)*
    - compaction and maintenance — expiring snapshots, rewriting manifests, file sizing *(Iceberg docs: Maintenance)*
    - schema evolution rules and the Delta log model / UniForm, with Hudi at awareness level *(Apache Iceberg: The Definitive Guide)*
- **Resources:**
    - **[Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/)** — spec, Maintenance, Partitioning, Configuration: the operational core (primary)
    - [Apache Iceberg: The Definitive Guide](https://hello.dremio.com/wp-apache-iceberg-the-definitive-guide-reg.html) — free via Dremio; format-war context, Delta/Hudi comparison, COW vs MOR (alternate)
- **Tools:**
    - FOSS (hands-on): [Iceberg](https://iceberg.apache.org/docs/latest/) on [MinIO](https://min.io/docs/minio/linux/index.html) via [Trino](https://trino.io/docs/current/connector/iceberg.html); Delta via [DuckDB](https://duckdb.org/docs/) / [delta-rs](https://delta-io.github.io/delta-rs/) — exercise both formats
    - Corp (evaluate): [Databricks Delta](https://docs.databricks.com/delta/), [Snowflake managed Iceberg](https://docs.snowflake.com/en/user-guide/tables-iceberg), [Fabric OneLake](https://learn.microsoft.com/fabric/onelake/) — managed forms
- **Do:**
    1. Create an Iceberg NAV table via Trino on MinIO.
    2. Run UPDATE, DELETE, and MERGE statements simulating a NAV correction and a late-arriving holding.
    3. Time-travel to the snapshot before the correction and confirm the prior NAV report reproduces.
    4. Evolve the schema (add a column) and change the partition spec; query still runs unchanged.
    5. Inspect the metadata JSON, manifest list, and manifests on MinIO and narrate the tree out loud.
- **Done when:**
    - [ ] You can debug "why is this table slow/huge" from the manifests alone.
    - [ ] You can write the Iceberg-vs-Delta ADR for a given estate with concrete reasons.
    - [ ] You can reproduce a pre-correction NAV via time travel on demand.
- Est. hours: 12

#### 3.4.3 Table-format catalogs — T2
- **Why:** The catalog is the new lock-in battleground — whoever owns the catalog owns the lakehouse — so this is a vendor-selection conversation you must lead, not delegate. Pick an engine-bundled catalog and you have quietly recreated the lock-in that open formats were supposed to remove. For a Luxembourg fund administrator, the catalog also decides who can vend credentials to regulated data, which is a governance question, not just a technical one.
- **Learn:**
    - what a catalog tracks — namespaces, table pointers, current snapshot per table *(Iceberg REST catalog spec)*
    - the Iceberg REST catalog spec as the decoupling standard — engines talk one API *(Iceberg REST catalog spec)*
    - credential vending — how the catalog brokers scoped storage access *(Apache Polaris docs)*
    - product positioning — Polaris, Unity Catalog OSS, Lakekeeper, Nessie *(Apache Polaris docs)*
    - why engine-bundled catalogs recreate lock-in even with open table formats *(Iceberg REST catalog spec)*
- **Resources:**
    - **[Iceberg REST catalog specification](https://iceberg.apache.org/docs/latest/)** (REST catalog / spec sections) — the open API that decouples engine from catalog (primary)
    - [Apache Polaris documentation](https://polaris.apache.org/) — a reference REST catalog implementation, credential vending, namespaces (reference)
    - [Lakekeeper documentation](https://docs.lakekeeper.io/) — a lightweight Rust REST catalog, easy to run in compose (alternate)
- **Tools:**
    - FOSS (hands-on): [Lakekeeper](https://docs.lakekeeper.io/) or [Apache Polaris](https://polaris.apache.org/) — a REST catalog in Docker Compose (↔ managed catalog)
    - Corp (evaluate): [Unity Catalog](https://docs.databricks.com/data-governance/unity-catalog/), [AWS Glue](https://docs.aws.amazon.com/glue/), [Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/) — what each bundles
- **Do:**
    1. Swap your capstone's catalog from Trino's Hive-style catalog to a Lakekeeper or Polaris REST catalog.
    2. Re-point Trino at the REST catalog and confirm the existing Iceberg tables resolve unchanged.
    3. Document precisely what changed (the catalog endpoint and config) and what did not (the data files, the format).
    4. Note how credentials are vended to the engine through the catalog.
- **Done when:**
    - [ ] You can explain credential vending and why it is the catalog's job.
    - [ ] You can argue why the catalog, not the format, decides openness.
    - [ ] You can swap the catalog without rewriting a single data file.
- Est. hours: 4

#### 4.3.1 MPP/federated SQL engines (Trino) — T2
- **Why:** Trino is the open federation engine (and the heart of Starburst and AWS Athena), and it queries the lakehouse and Postgres in one statement — the practical face of "decoupled compute." For a fund administrator, that means joining live transfer-agency reference data in Postgres to historical Iceberg NAV facts without an ETL hop. But federation done naively produces chatty cross-store joins, and the architect must know when it is an anti-pattern.
- **Learn:**
    - coordinator/worker architecture — how a query is planned and distributed *(Trino docs: Overview)*
    - connectors and pushdown — what predicates/aggregations get pushed to each source *(Trino docs: Iceberg connector)*
    - the memory model and spill — why big joins fail and how spill helps *(Trino docs: Overview)*
    - Iceberg connector specifics — snapshots, time travel, and maintenance from Trino *(Trino docs: Iceberg connector)*
    - cost-based optimizer basics and when federation is an anti-pattern (chatty cross-store joins) *(Trino: The Definitive Guide)*
- **Resources:**
    - **[Trino documentation](https://trino.io/docs/current/)** (Overview + [Iceberg connector](https://trino.io/docs/current/connector/iceberg.html)) — architecture, connectors, pushdown (primary)
    - [Trino: The Definitive Guide](https://www.starburst.io/info/oreilly-trino-guide/) — free via Starburst; CBO, federation patterns and anti-patterns (alternate)
- **Tools:**
    - FOSS (hands-on): [Trino](https://trino.io/docs/current/) — the federation engine over Iceberg + Postgres (↔ Starburst Enterprise, AWS Athena)
    - Corp (evaluate): [Starburst](https://docs.starburst.io/), [AWS Athena](https://docs.aws.amazon.com/athena/), [Synapse serverless](https://learn.microsoft.com/azure/synapse-analytics/sql/on-demand-workspace-overview) — managed Trino-style options
- **Do:**
    1. Add Trino to your Docker Compose stack with Postgres and Iceberg connectors.
    2. Join Postgres fund reference data to Iceberg NAV history in a single query.
    3. Run the same logical join after copying the dimension into Iceberg first; compare timings.
    4. Use EXPLAIN to verify which predicates push down to Postgres vs Iceberg.
- **Done when:**
    - [ ] You can predict which predicates push down to each source and confirm it with EXPLAIN.
    - [ ] You can state when federating beats copying the dimension, and when it does not.
    - [ ] You can read a Trino query plan and spot a chatty cross-store join.
- Est. hours: 5

#### 4.3.3 Embedded analytical engines (DuckDB) — T2
- **Why:** DuckDB is the architect's pocket warehouse — local development, fast testing, and a legitimate production pattern for mid-size workloads — and knowing its limits sharpens every "do we actually need a cluster?" conversation. For a fund administrator running marts that fit comfortably on one node, "no cluster" can be the right, cheapest, most maintainable architecture. The skill is knowing the data-size and concurrency envelope where that holds.
- **Learn:**
    - the in-process model — DuckDB runs inside your process, not as a server *(DuckDB docs: Why DuckDB)*
    - out-of-core execution — querying data larger than RAM by spilling *(DuckDB docs: Why DuckDB)*
    - reading Parquet/Iceberg/Delta directly from object storage *(DuckDB docs: Reading Parquet)*
    - the extension ecosystem and the single-writer constraint *(DuckDB docs: Why DuckDB)*
    - awareness of MotherDuck (managed) and ClickHouse (server-side single-node speed) *(DuckDB docs: Why DuckDB)*
- **Resources:**
    - **[DuckDB docs: Why DuckDB](https://duckdb.org/why_duckdb)** — the design philosophy, in-process model, and intended workloads (primary)
    - [DuckDB documentation (Parquet / extensions)](https://duckdb.org/docs/) — reading lake formats and the extension ecosystem (reference)
- **Tools:**
    - FOSS (hands-on): [DuckDB](https://duckdb.org/docs/) — the embedded engine for marts and benchmarks
    - Corp (evaluate): [MotherDuck](https://motherduck.com/docs/), [ClickHouse Cloud](https://clickhouse.com/docs) — at awareness level
- 🐘 **Postgres-native alternative — [pg_duckdb](https://github.com/duckdb/pg_duckdb) / [Citus](https://www.citusdata.com/) columnar:** *Better when* you want columnar analytics inside the same Postgres that serves OLTP — DuckDB's engine embedded via `pg_duckdb`, or Citus for distributed/columnar tables — so analysts query live data with no separate warehouse to load. *Worse when* you need true lakehouse scale, open table formats, or storage/compute separation: that's Trino/Spark/warehouse territory.
- **Do:**
    1. Benchmark the Phase-1 mart queries two ways: DuckDB over Parquet vs Postgres.
    2. Record query times and resource use for each.
    3. Repeat with a larger-than-RAM holdings table to observe out-of-core behaviour.
    4. Write 5 bullets stating when DuckDB wins and when Postgres (or a cluster) wins.
- **Done when:**
    - [ ] You can articulate the data-size/concurrency envelope where "no cluster" is the right architecture.
    - [ ] You can show DuckDB querying a larger-than-RAM file successfully.
    - [ ] You can name the single-writer constraint and what it rules out.
- Est. hours: 3

#### 5.2.1 + 5.3.1 dbt & the SQL transformation layer — T1
- **Why:** dbt is the modeling-to-production bridge you already started in Phase 1, and mastery — not mere usage — is what lets you set transformation standards for a whole analytics team. In a fund platform, dbt tests are where data-quality contracts become executable and dbt snapshots are how you keep auditable SCD2 history of share-class attributes. Without disciplined materializations and a readable DAG, the warehouse becomes a pile of views nobody can reason about.
- **Learn:**
    - project structure conventions — staging/intermediate/marts mirroring medallion *(dbt best-practice guides)*
    - the ref graph and materializations — view/table/incremental/snapshot and incremental failure modes *(dbt docs: Materializations)*
    - tests — generic, singular, and unit tests as executable DQ contracts *(dbt docs: Tests)*
    - dbt snapshots = SCD2 — keeping auditable history of dimension attributes *(dbt docs: Snapshots)*
    - docs, exposures, and packages (dbt-utils, dbt-expectations) *(dbt best-practice guides)*
    - SQLMesh as the challenger — virtual environments, column-level lineage, at eval level *(SQLMesh docs)*
- **Resources:**
    - **[dbt best-practice guides](https://docs.getdbt.com/best-practices)** — official structure/style/materialization guidance (primary)
    - [dbt documentation](https://docs.getdbt.com/) — materializations, tests, snapshots, exposures reference (reference)
    - [Analytics Engineering with SQL and dbt (Cyr & Dorsey)](https://www.oreilly.com/library/view/analytics-engineering-with/9781098142377/) — end-to-end project narrative (deepening)
    - [SQLMesh documentation](https://sqlmesh.readthedocs.io/) — the challenger's virtual environments and lineage, for evaluation (alternate)
- **Tools:**
    - FOSS (hands-on): [dbt Core](https://docs.getdbt.com/) + [dbt-duckdb](https://github.com/duckdb/dbt-duckdb) / [dbt-trino](https://github.com/starburstdata/dbt-trino); [SQLMesh](https://sqlmesh.readthedocs.io/) (eval) — the transformation layer (↔ dbt Cloud)
    - Corp (evaluate): [dbt Cloud](https://docs.getdbt.com/docs/cloud/about-cloud/dbt-cloud-features), [Coalesce](https://docs.coalesce.io/), [Dataform](https://cloud.google.com/dataform/docs) — managed options
- **Do:**
    1. Rebuild the Phase-1 mart as a layered dbt project on DuckDB: sources with freshness checks, staging → marts.
    2. Implement a snapshot-based SCD2 fund/share-class dimension.
    3. Add tests on every model (generic + at least one singular/unit test on a NAV invariant).
    4. Generate docs and add an exposure for the EMT-shaped output.
    5. Run `dbt build` from scratch and confirm it is green.
- **Done when:**
    - [ ] `dbt build` is green from scratch with tests and docs.
    - [ ] The DAG is readable by a stranger and layered like medallion.
    - [ ] You can explain why each model has the materialization it has.
- Est. hours: 14

#### 5.2.2 Orchestrated ELT (build-vs-buy) — T2
- **Why:** "Fivetran + dbt" is the default managed ingestion pattern, and as architect you must price it against self-hosted connectors for a regulated EU estate where data sovereignty is a hard constraint. Managed ELT wins for long-tail SaaS sources and loses for core banking and mainframe feeds that need to stay inside the perimeter. Getting the crossover point wrong means either an engineer babysitting Airbyte forever or a surprise MAR bill.
- **Learn:**
    - MAR-based pricing mechanics — Monthly Active Rows and how cost scales with change volume *(Fivetran pricing)*
    - connector reliability economics — what you pay an engineer to maintain self-hosted connectors *(Airbyte deployment docs)*
    - when managed ELT wins — long-tail SaaS sources with maintained connectors *(Fivetran pricing)*
    - when it loses — core banking, mainframe, and data-sovereignty constraints *(Airbyte deployment docs)*
- **Resources:**
    - **[Fivetran pricing & architecture](https://www.fivetran.com/pricing)** — the MAR pricing model you must reason about (primary)
    - [Airbyte deployment documentation](https://docs.airbyte.com/) — self-hosting cost and operational profile for comparison (reference)
- **Do:**
    1. Write a half-page build-vs-buy note for a fund admin with 6 internal systems and 4 SaaS sources.
    2. Estimate Fivetran MAR cost for the SaaS sources and engineer-hours for self-hosting the internal ones.
    3. State the crossover point where managed cost beats maintained-Airbyte cost.
    4. Flag which internal sources cannot leave the EU perimeter at all.
- **Done when:**
    - [ ] You can state the crossover point where Fivetran's cost beats an engineer maintaining Airbyte.
    - [ ] You can name which sources are off-limits to managed ELT for sovereignty reasons.
- Est. hours: 2

#### 2.1.1 Batch ELT connectors — T2
- **Why:** Connector platforms are the workhorse of non-streaming ingestion, and hands-on Airbyte makes the managed-vendor conversation concrete instead of theoretical. For a fund administrator, the operating reality is incremental syncs with cursor fields and schema-change handling — exactly where self-hosted connectors quietly break. Running one yourself is how you learn what you are really paying Fivetran to absorb.
- **Learn:**
    - the connector model — source, destination, spec, and state *(Airbyte docs: Core concepts)*
    - incremental sync modes and cursor fields — append vs dedup, and how state advances *(Airbyte docs: Incremental sync)*
    - CDC-flavored connectors vs true log-based CDC — what each guarantees *(Airbyte docs: Core concepts)*
    - schema-change handling — what happens when a source column appears or changes type *(Airbyte docs: Incremental sync)*
    - the operating cost of self-hosting connectors — the hidden maintenance line item *(Airbyte deployment docs)*
- **Resources:**
    - **[Airbyte documentation](https://docs.airbyte.com/)** — core concepts, incremental sync, and self-hosting (primary)
    - [Airbyte: Incremental sync](https://docs.airbyte.com/using-airbyte/core-concepts/sync-modes/incremental-append-deduped) — cursor fields and state semantics in detail (reference)
- **Tools:**
    - FOSS (hands-on): [Airbyte OSS](https://docs.airbyte.com/) — self-hosted connectors in compose (↔ Fivetran, Stitch, ADF copy activity)
    - Corp (evaluate): [Fivetran](https://fivetran.com/docs) — the managed equivalent at build-vs-buy level
- **Do:**
    1. Stand up Airbyte in Docker Compose.
    2. Configure an incremental sync from the Phase-1 Postgres to MinIO Parquet using a cursor field.
    3. Run an initial sync, then an incremental one, and confirm only changed rows move.
    4. Break the cursor on purpose (e.g. reset/alter the cursor column) and repair the sync.
- **Done when:**
    - [ ] You can explain how state is kept and what happens on a re-sync after a schema change.
    - [ ] You can demonstrate an incremental sync moving only changed rows.
    - [ ] You can recover a broken cursor and explain what broke it.
- Est. hours: 4

#### 8.2.5 Data Vault modeling (+ 1.4.7 pattern) — T1
- **Why:** Data Vault is the financial-services-favored EDW pattern — auditability by construction and multi-source integration without re-modeling — and Luxembourg fund shops ask for it by name in job specs. Its hub/link/satellite split is what lets you absorb a second transfer-agency source without rewriting the warehouse, and its insert-only loading is what makes every change explainable to an auditor. Misuse it on a single small source and you have built ceremony with no payoff.
- **Learn:**
    - hubs, links, satellites — business keys, relationships, and history/context separately *(Data Vault 2.0 ch. 1–4)*
    - raw vault vs business vault — where raw integration ends and computed logic begins *(Data Vault 2.0 ch. 5–7)*
    - hash keys and hashdiffs — deterministic keys and cheap change detection *(Data Vault 2.0 ch. 11)*
    - loading patterns — parallel, insert-only, and why that is auditable *(Data Vault 2.0 ch. 11–12)*
    - PIT and bridge tables — restoring query performance over a normalized vault *(Data Vault 2.0 ch. 7)*
    - when Vault is overkill, and Vault-on-lakehouse with dbt/AutomateDV *(AutomateDV docs)*
- **Resources:**
    - **[Building a Scalable Data Warehouse with Data Vault 2.0 (Linstedt & Olschimke)](https://www.oreilly.com/library/view/building-a-scalable/9780128025109/)** ch. 1–7 (modeling) + ch. 11–12 (loading) (primary)
    - [AutomateDV documentation](https://automate-dv.readthedocs.io/) — the dbt package that generates hub/link/sat loads on the lakehouse (reference)
- **Tools:**
    - FOSS (hands-on): [dbt](https://docs.getdbt.com/) + [AutomateDV package](https://automate-dv.readthedocs.io/) — raw vault generated and tested (↔ VaultSpeed)
    - Corp (evaluate): [VaultSpeed](https://docs.vaultspeed.com/), [WhereScape](https://www.wherescape.com/), [Datavault Builder](https://datavault-builder.com/) — automation vendors
- **Do:**
    1. Model fund / share-class / administrator from two conflicting source systems as a raw vault (hubs/links/sats) with AutomateDV.
    2. Choose hub business keys deliberately for messy identifiers (ISIN reuse, internal codes) and justify them.
    3. Build one PIT table over the satellites for query performance.
    4. Land a late-arriving correction insert-only and show the full audit trail from the satellites.
- **Done when:**
    - [ ] You can defend hub key choices for messy real-world identifiers like reused ISINs.
    - [ ] You can explain insert-only loading and the audit trail it produces to an auditor.
    - [ ] You can show a late correction as a new satellite row, not an overwrite.
- Est. hours: 12

#### 1.12.1 ISO 20022 — T1
- **Why:** ISO 20022 is the lingua franca of EU payments and securities messaging, and fund platforms ingest and emit it daily — post-MT migration it is *the* message standard your canonical model must align to. An architect who cannot map a subscription order message onto the warehouse model will design something that drops fields auditors expect to trace. Knowing the message flow is how you reason about what your platform must capture at each hop.
- **Learn:**
    - message taxonomy — pacs/camt/sese/semt/setr business areas, and which matter for funds (setr orders, semt statements, sese settlement) *(iso20022.org: catalogue)*
    - XSD structure, business components, and external code sets *(iso20022.org: catalogue)*
    - the e-Repository and Message Definition Reports as the authoritative source *(iso20022.org: catalogue)*
    - mapping messages to a canonical model — where each business field lands *(iso20022.org: catalogue)*
    - MX-over-SWIFT context — how these messages travel *(SWIFT: standards)*
- **Resources:**
    - **[ISO 20022 message catalogue](https://www.iso20022.org/iso-20022-message-definitions)** — Message Definition Reports incl. setr (investment funds) (primary)
    - [SWIFT: standards](https://www.swift.com/standards) — MX-over-SWIFT context and the broader standards landscape (reference)
- **Do:**
    1. Obtain a sample `setr.010` (subscription order) message and its schema.
    2. Parse it with Python/lxml via `uv run`.
    3. Map every business field onto your Phase-1 model and record the mapping.
    4. Document the gaps — fields your current model cannot hold — and what they would require.
- **Done when:**
    - [ ] You can sketch the message flow (order → status → confirmation → settlement) and name the message type at each hop.
    - [ ] You can map a `setr.010` onto your model and list the unmappable fields.
- Est. hours: 6

#### 1.12.7 EMT / EPT (FinDatEx) — T1
- **Why:** EMT (MiFID target market and costs) and EPT (PRIIPs KID data) are the fund-data dissemination templates of the EU industry — the exact artifacts a Luxembourg fund-data platform produces and consumes every day. Producing a valid EMT is a regulatory data-product deliverable, and the architect must know which upstream attributes block it from completing. Treat these as afterthoughts and distribution stalls because a costs block is half-populated.
- **Learn:**
    - FinDatEx governance and template lifecycle/versioning — how EMT/EPT versions are released *(FinDatEx: templates)*
    - EMT structure — manufacturer target market and costs & charges blocks *(FinDatEx: templates)*
    - EPT structure — PRIIPs KID inputs (SRI, performance scenarios, costs) *(PRIIPs Regulation 1286/2014)*
    - CEPT and delta templates and how distributors consume them *(FinDatEx: templates)*
    - data-quality pain points — versioning, partial files, code lists *(FinDatEx: templates)*
- **Resources:**
    - **[FinDatEx templates](https://findatex.eu/)** — current EMT and EPT specifications, free downloads (primary)
    - [PRIIPs Regulation (EU) No 1286/2014](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32014R1286) — the KID regulation behind EPT: SRI, performance scenarios, cost disclosure (reference)
- **Do:**
    1. Download the current EMT spec from FinDatEx and read the target-market and costs blocks.
    2. Build a dbt model set that produces an EMT V4-shaped output from your fund mart.
    3. Validate the output column-by-column against the spec, including code-list values.
    4. List the upstream attributes that, if missing, block EMT completion.
- **Done when:**
    - [ ] You can explain which upstream attributes block EMT completion and why.
    - [ ] You can explain what "regulatory data product" means concretely, using EMT as the example.
    - [ ] Your EMT output validates column-by-column against the FinDatEx spec.
- Est. hours: 5

#### 1.12.2 + 1.12.3 LEI & ISIN (entity and instrument identity) — T2
- **Why:** Identifier discipline is the difference between a fund platform and a data swamp — LEI and ISIN are the join keys of the entire industry. Treat an ISIN as a stable primary key and a corporate action that renames it will silently split one instrument into two in your warehouse. The architect must design a security master that survives identifier lifecycle events without losing history.
- **Learn:**
    - ISIN structure and allocation, and why ISIN ≠ listing (venue-level FIGI/MIC) *(ANNA: standards)*
    - LEI structure and the GLEIF registry *(GLEIF: LEI data)*
    - Level 1 (who-is-who) vs Level 2 (who-owns-whom) data *(GLEIF: Level 2 data)*
    - validation via check digits for both identifiers *(ANNA: standards)*
    - identifier lifecycle events — corporate actions that rename or retire ISINs *(ANNA: standards)*
- **Resources:**
    - **[GLEIF: LEI data](https://www.gleif.org/en/lei-data/gleif-golden-copy)** — golden copy, Level 1/Level 2 data, registry concepts (primary)
    - [ANNA — standards (ISIN ISO 6166)](https://www.anna-web.org/standards/) — ISIN structure, allocation, and check digits (reference)
- **Tools:**
    - FOSS (hands-on): [GLEIF golden copy](https://www.gleif.org/en/lei-data/gleif-golden-copy) — free LEI dataset loaded to lakehouse bronze
- **Do:**
    1. Download the GLEIF golden copy (free) and load it to your lakehouse bronze.
    2. Link your Faker funds to real LEIs of their (fictive) management companies.
    3. Add an internal surrogate key alongside ISIN in your security master.
    4. Sketch a corporate-action scenario where the ISIN changes and show your model keeps continuity via the surrogate.
- **Done when:**
    - [ ] You can explain why a security master needs both ISIN and an internal surrogate, with a concrete corporate-action scenario.
    - [ ] You can validate an ISIN and an LEI check digit.
    - [ ] You can distinguish Level 1 from Level 2 GLEIF data and say what each enables.
- Est. hours: 2

#### 1.12.8 SWIFT MT / MX — T2
- **Why:** Legacy MT messages still flow through fund operations — transfer agency and custody — so architects must read both worlds during the long MX coexistence period. A holdings statement arriving as an MT535 has fields that map lossily onto your richer model, and knowing which is which prevents silent data loss at the boundary. You will be the one who explains which MX message eventually replaces each MT.
- **Learn:**
    - MT message anatomy — blocks and tags for the fund-relevant set (MT502/509/515 orders, MT535/536 statements) *(SWIFT: standards)*
    - MX = ISO 20022 over SWIFT and the translation/coexistence rules *(SWIFT: standards)*
    - the MT-to-MX mapping — which MX message replaces a given MT *(iso20022.org: catalogue)*
    - what SWIFT network membership means operationally *(SWIFT: standards)*
- **Resources:**
    - **[SWIFT: standards](https://www.swift.com/standards)** — MT category 5 (securities) and MX/ISO 20022 standards landing (primary)
    - [ISO 20022 message catalogue](https://www.iso20022.org/iso-20022-message-definitions) — the MX messages that replace MT equivalents (reference)
- **Do:**
    1. Obtain a sample MT535 holdings statement (or a documented field layout from the standard).
    2. Hand-translate it into your model's terms, field by field.
    3. Note the lossy fields — where the MT carries less than your model, or vice versa.
    4. Identify the MX (ISO 20022) message that replaces MT535.
- **Done when:**
    - [ ] You can read an MT message with the spec open and know which MX message replaces it.
    - [ ] You can list the lossy fields in an MT535-to-model translation.
- Est. hours: 2

#### 9.6.2 Data documentation — T2
- **Why:** Generated, always-current documentation is a governance deliverable in its own right, and dbt docs is the gateway drug before the Phase 6 catalogs. In a fund platform a business analyst must be able to trace "where does this EMT field come from?" without interrupting you — that traceability is a regulatory expectation, not a nicety. Docs that drift from the models are worse than none because people trust them.
- **Learn:**
    - dbt docs generation and persistence — `persist_docs` to push descriptions into the warehouse *(dbt docs: documentation)*
    - exposures — declaring downstream consumers like the EMT output *(dbt docs: exposures)*
    - what belongs in model YAML vs the enterprise catalog *(dbt docs: documentation)*
    - docs-as-code review flow — descriptions reviewed in PRs alongside SQL *(dbt docs: documentation)*
- **Resources:**
    - **[dbt docs: documentation](https://docs.getdbt.com/docs/build/documentation)** — generating, persisting, and structuring model docs (primary)
    - [dbt docs: exposures](https://docs.getdbt.com/docs/build/exposures) — declaring downstream consumers in the DAG (reference)
- **Tools:**
    - FOSS (hands-on): [dbt docs](https://docs.getdbt.com/docs/build/documentation) — generated lineage and descriptions (↔ catalog-generated docs in Phase 6)
    - Corp (evaluate): [dbt Cloud docs](https://docs.getdbt.com/docs/collaborate/build-and-view-your-docs) / [Purview](https://learn.microsoft.com/purview/) lineage views
- **Do:**
    1. Fully document the capstone dbt project: every model and column description.
    2. Declare one exposure for the EMT output, naming its consumer.
    3. Run `dbt docs generate` and browse the lineage graph for the EMT field path.
    4. Plan to publish the static docs site from CI later in Phase 3.
- **Done when:**
    - [ ] A business analyst can answer "where does this EMT field come from?" without asking you.
    - [ ] Every model and column in the capstone has a description.
    - [ ] The EMT output is declared as an exposure with its consumer named.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.4.6 | Hub-and-spoke | Centralized integration hub feeding domain marts; the pre-mesh enterprise default architecture | [*Data Management at Scale* ch. 2 (architecture survey)](https://www.oreilly.com/library/view/data-management-at/9781098138851/) | 20 |
| 1.12.4 | CFI (ISO 10962) | 6-character instrument classification code carried in reference data, complementing the ISIN | [ANNA standards (CFI ISO 10962)](https://www.anna-web.org/standards/) | 20 |
| 1.12.5 | FIGI | Bloomberg's open venue-level instrument identifier; the ISIN complement for listing-level identity | [OpenFIGI — about FIGI](https://www.openfigi.com/about/figi) | 20 |
| 1.12.9 | FpML | ISDA's XML standard for OTC derivatives; appears at fund boundaries (hedging share classes) | [FpML official site](https://www.fpml.org/) | 20 |
| 1.12.10 | FIX | Trading-venue messaging protocol; upstream of fund data and rarely modeled directly by you | [FIX Trading Community — standards](https://www.fixtrading.org/standards/) | 20 |
| 1.12.11 | IBAN / SEPA | Payment-account identity standard underpinning EU cash legs of fund subscriptions/redemptions | [ECB — SEPA overview](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html) | 15 |
| 3.1.2 | On-prem MPP warehouses | Teradata/Vertica/Netezza estates you will most often migrate *from* into a lakehouse | [Teradata documentation](https://docs.teradata.com/) | 30 |
| 3.2.11 | Geospatial storage | PostGIS/GeoParquet/H3; ESG and real-asset edge cases in fund and alternatives data | [PostGIS — home](https://postgis.net/) + [GeoParquet spec](https://geoparquet.org/) | 30 |
| 5.3.3 | PRQL / Malloy | Composable, pipelined query-language challengers to SQL with an in-browser tour | [PRQL — language site & playground](https://prql-lang.org/) | 20 |
| 5.4.1 | Interactive data prep | Visual cleanup tools (Alteryx/DataBrew) typically bought and owned by business teams | [Alteryx product overview](https://www.alteryx.com/products/alteryx-designer) | 15 |
| 8.2.6 | Anchor modeling / 6NF | Fully temporal, highly normalized modeling; Data Vault's stricter 6NF cousin | [Anchor Modeling — official site](https://anchormodeling.com/) | 30 |

*T3 subtotal: 4 h*

### Capstone 2 — Fund-document lakehouse

- **Goal:** a working open lakehouse carrying real fund-data shapes (NAV series, holdings, EMT outputs, GLEIF entities) through bronze→silver→gold, with the format/catalog decisions documented like a vendor selection.
- **Stack (100% free):** [MinIO](https://min.io/docs/minio/linux/index.html) (↔ ADLS Gen2), [Apache Iceberg](https://iceberg.apache.org/docs/latest/) (↔ Databricks Delta / Snowflake managed Iceberg), [Lakekeeper](https://docs.lakekeeper.io/) or [Apache Polaris](https://polaris.apache.org/) REST catalog (↔ Unity Catalog / Glue), [Trino](https://trino.io/docs/current/) (↔ Starburst / Athena / Synapse serverless), [DuckDB](https://duckdb.org/docs/) + [dbt Core](https://docs.getdbt.com/) (↔ dbt Cloud on a warehouse), [Airbyte OSS](https://docs.airbyte.com/) (↔ Fivetran / ADF), [AutomateDV](https://automate-dv.readthedocs.io/) raw-vault slice (↔ VaultSpeed), [Docker Compose](https://docs.docker.com/compose/) throughout.
- **Build:** (1) Airbyte lands Phase-1 Postgres + GLEIF golden copy into bronze (Parquet on MinIO); (2) silver Iceberg tables: cleansed NAV/holdings with DQ-checked conformance, raw vault for fund/share-class from two "source systems"; (3) gold: dbt marts incl. the EMT-shaped output and the SCD2 dimensional mart; (4) Trino federates a live Postgres dimension against Iceberg facts; (5) demonstrate time travel + schema evolution + a compaction run. Drive every step from documented commands so the whole stack rebuilds from an empty MinIO.
- **Architecture deliverables:** C4 context/container for the lakehouse; ADR-004 Iceberg vs Delta (estate-specific), ADR-005 REST catalog choice (lock-in analysis), ADR-006 medallion layer contracts (the sheet from 1.4.3 made binding).
- **Acceptance criteria:** end-to-end rebuild from empty MinIO via documented commands; `dbt build` green with tests + docs published; EMT output validates against the FinDatEx column spec; time-travel query reproduces yesterday's NAV report after a correction lands; every stack component annotated with its corporate equivalent in the README; the catalog can be swapped (Hive-style → REST) without rewriting data files.
- Est. hours: 16

*Phase 2 total: 123 h (T1/T2 entries 103 h + T3 4 h + capstone 16 h)*
