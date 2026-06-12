<a id="phase-3"></a>
## Phase 3: Distributed Compute, Orchestration & Engineering Practice (months 17–21, 118 h)

**Goal:** close the two biggest gaps that block scale — Spark and orchestration — and wrap the platform in software-engineering discipline: CI/CD for data, data versioning with write-audit-publish, integration testing, and managed schema change.
**Entry prerequisites:** Phase 2 (lakehouse running; dbt project to orchestrate).
**Exit criteria:** you can (1) explain a Spark job's stages and fix a skewed join from the UI; (2) defend Airflow vs Dagster vs ADF for a given team; (3) ship a pipeline change through CI with tests, data diff, and an audited publish; (4) run schema change in a regulated estate without downtime (expand–contract).

### T1/T2 topics

#### 4.1.1 Distributed batch compute (Spark) — T1
- **Why:** Spark is the named weak spot and the default heavy-lift engine in every fund-data estate (Databricks, Synapse, Fabric all sell it); architects who can't read the Spark UI can't review the platform's biggest bills.
- **Learn:** architecture: driver/executors, jobs→stages→tasks, the shuffle; DataFrame API and lazy evaluation; Catalyst optimizer + AQE; partitioning, skew, salting; join strategies (broadcast vs sort-merge) and when the planner picks wrong; caching/persistence levels; memory model and OOM debugging; writing to Iceberg; deployment modes (local, standalone, K8s, Databricks) at decision level.
- **Resource:** *Learning Spark, 2nd ed.* (Damji et al., free PDF from Databricks) ch. 1–7 + 12 (tuning) + official "Tuning" and "SQL Performance" docs. *Alternate:* *Spark: The Definitive Guide* pt. II.
- **Tools:** FOSS: Apache Spark (local + compose, ↔ Databricks / Synapse Spark / EMR) · Corp: Databricks (the de-facto enterprise Spark; evaluation level incl. Photon, cluster pricing).
- **Do:** generate a 50M-row holdings/prices dataset; compute per-fund daily NAV and rolling performance in PySpark against MinIO/Iceberg; engineer a skewed join, diagnose it in the Spark UI, fix it with broadcast + salting; document before/after stage timings.
- **Done when:** given an unfamiliar slow job, you go UI → stages → shuffle/skew → fix, and can explain each step to a junior; you can also argue when Spark is the *wrong* tool (DuckDB-size data).
- Est. hours: 36

#### 5.3.2 DataFrame transformation layer (PySpark / Polars / Ibis) — T2
- **Why:** the code half of the transformation layer; choosing SQL vs DataFrames (and which DataFrame runtime) is a standards decision you'll own.
- **Learn:** PySpark idioms vs pandas habits (no row loops, window specs); Polars lazy frames and when it replaces Spark below ~100GB; Ibis as portable dataframe API over 20+ engines; UDF cost model (Python UDF vs pandas UDF vs native).
- **Resource:** Polars user guide (lazy API) + Ibis "Why Ibis" docs.
- **Tools:** FOSS: Polars, Ibis, PySpark · Corp: Snowpark, Databricks (same concepts rebranded).
- **Do:** implement one silver transformation three ways (PySpark, Polars, dbt SQL); write a half-page standards note: which layer owns which transformation type and why.
- **Done when:** your standards note survives the question "why not do everything in SQL?"
- Est. hours: 8

#### 5.6.1 + 5.6.3 Orchestration (Airflow + Dagster, task- vs asset-oriented) — T1
- **Why:** orchestration is in the explicit mastery bias: the scheduler is the platform's nervous system, and the task-vs-asset paradigm choice shapes team workflow for years.
- **Learn:** Airflow: DAGs, operators, sensors, idempotent task design, backfills/catchup, executors (Local/Celery/K8s), datasets; Dagster: software-defined assets, partitions, asset checks, declarative automation — and why asset-orientation gives lineage for free; failure handling: retries, SLAs, alerting; orchestrator anti-patterns (business logic in DAG files, XCom abuse); Prefect/Mage awareness; ADF + Managed Airflow as the Azure reality.
- **Resource:** Dagster docs "Concepts" (assets, partitions) + *Data Pipelines with Apache Airflow* 2nd ed. (Harenslak & de Ruiter) ch. 1–6, 12.
- **Tools:** FOSS: Dagster (primary hands-on), Airflow (market fluency) · Corp: Azure Data Factory / MWAA / Cloud Composer (evaluation level).
- **Do:** orchestrate the Capstone-2 pipeline as Dagster assets with daily partitions and asset checks; rebuild one branch of it as an Airflow DAG; write a comparison memo (dev loop, backfills, lineage, ops burden).
- **Done when:** you can run a clean 30-day backfill after a logic fix and explain exactly which partitions recomputed and why.
- Est. hours: 20

#### 9.2.2 Data versioning & write-audit-publish — T2
- **Why:** branch-merge workflows for data are how regulated platforms ship changes without bad data reaching consumers; WAP is the pattern auditors love.
- **Learn:** Iceberg branching/tagging natively; write-audit-publish flow; lakeFS Git-like model (repos, branches, merges over object storage); Nessie catalog-level versioning; DVC for ML-ish file versioning (awareness); choosing between table-level and lake-level versioning.
- **Resource:** Iceberg branching docs + lakeFS docs ("How it works" + WAP tutorial).
- **Tools:** FOSS: Iceberg branches, lakeFS (↔ no direct corp equivalent — Databricks/Snowflake time travel + clones) · Corp: Snowflake zero-copy clones (evaluation level).
- **Do:** implement WAP in the Dagster pipeline: write to an Iceberg branch, run DQ checks, fast-forward publish on green, alert-and-hold on red.
- **Done when:** a deliberately corrupted load never becomes visible to the gold consumer, and you can show the audit trail.
- Est. hours: 8

#### 9.3.1 CI/CD for data platforms — T2
- **Why:** the deployment pipeline is where engineering standards become enforceable; data teams without CI ship regressions to regulators.
- **Learn:** GitHub Actions: workflows, environments, secrets, matrix jobs; what to run per PR vs per merge for a data repo (lint/ruff, unit tests, dbt build on prod-like sample, docs publish); deployment gates and approvals; GitOps concept (Argo CD awareness for later K8s phase).
- **Resource:** GitHub Actions official docs (core concepts) + dbt "CI in practice" guide.
- **Tools:** FOSS: GitHub Actions (↔ Azure DevOps Pipelines, GitLab CI) · Corp: Azure DevOps (EU enterprise default; evaluation level).
- **Do:** add CI to the capstone repo: ruff + pytest + `dbt build --select state:modified+` on PR, docs site publish on merge.
- **Done when:** a PR that breaks a dbt test cannot merge, and you can explain every job in the workflow file.
- Est. hours: 8

#### 9.3.2 Data-aware CI — T2
- **Why:** code-green/data-wrong is the classic data regression; data-aware CI (state deferral, data diff) catches what unit tests can't.
- **Learn:** dbt slim CI (state:modified, defer); SQLMesh virtual environments and automatic change categorization (breaking vs non-breaking); data-diff concept (row/column-level diffs between prod and PR build); Datafold as the managed version.
- **Resource:** SQLMesh docs ("Plans" + virtual environments) + dbt slim CI guide.
- **Tools:** FOSS: SQLMesh (eval hands-on), dbt slim CI · Corp: Datafold (evaluation level).
- **Do:** run the same breaking change through dbt slim CI and SQLMesh plan; record which caught what, and at what compute cost.
- **Done when:** you can tell a team when slim CI is enough and when diff-based CI pays for itself.
- Est. hours: 5

#### 9.4.3 Integration testing for pipelines — T2
- **Why:** pipelines fail at the seams (connections, schemas, permissions); throwaway-infra tests are the only honest test of the seams.
- **Learn:** Testcontainers-python (Postgres/MinIO/Kafka containers per test); test pyramid for data (unit SQL → component → end-to-end on sample); golden datasets and snapshot testing; contract tests preview (Pact concept; full data contracts in Phase 8).
- **Resource:** Testcontainers-python docs + one well-known reference blog on data pipeline testing pyramids (verify link at assembly).
- **Tools:** FOSS: Testcontainers, pytest · Corp: same (this layer is tool-agnostic).
- **Do:** write an integration test that spins Postgres + MinIO, runs the idempotent loader twice, and asserts end-state invariants.
- **Done when:** `uv run pytest -m integration` passes on a machine with only Docker installed.
- Est. hours: 5

#### 9.7.1 Schema migrations & change management — T2
- **Why:** regulated estates change schemas under change-advisory scrutiny; expand–contract and versioned migrations are how you do it without downtime or drama.
- **Learn:** Flyway/Liquibase models (versioned vs declarative); Alembic for Python shops; expand–contract (parallel change) pattern; backward-compatible deployment ordering (DB before code); migration review and rollback reality (roll forward).
- **Resource:** Flyway docs (concepts) + Martin Fowler "Parallel Change" / "Evolutionary Database Design" articles.
- **Tools:** FOSS: Flyway or Alembic (↔ Liquibase enterprise, Redgate) · Corp: Liquibase Pro / Azure DevOps-integrated change flows (evaluation level).
- **Do:** rename a column on the live Phase-1 Postgres via expand–contract across three migration versions, with the loader running throughout.
- **Done when:** zero failed loads during the rename, and the migration history table tells the full story.
- Est. hours: 5

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 4.4.1 | General distributed frameworks | Ray/Dask — Python-native distributed compute beyond Spark (ML-leaning) | Ray "Overview" docs page | 30 |
| 4.4.2 | Specialized frameworks | Modin etc. — drop-in pandas acceleration; niche | Modin README | 10 |
| 5.1.2 | Code-first ETL (NiFi) | Visual flow-based ingestion engine; common in banks' legacy ingestion | NiFi "Overview" doc | 25 |
| 9.4.4 | Load/performance testing | k6/Locust/JMeter — throughput testing for data APIs and engines | k6 "What is k6" page | 25 |
| 9.5.2 | Data diff tools | Row-level diffs across model changes (data-diff, Datafold) | Datafold data-diff README | 20 |
| 9.6.1 | Code documentation | MkDocs/Sphinx static docs; you'll publish dbt docs instead | MkDocs getting started | 20 |
| 9.9.1 | Notebooks in production | Papermill/Ploomber parameterized notebook jobs; contested practice | Papermill README | 20 |

*T3 subtotal: 2.5 h*

### Capstone 3 — Orchestrated Spark NAV pipeline

- **Goal:** the lakehouse grows an industrial-strength compute and delivery layer: Spark for scale, Dagster for orchestration, WAP for safety, CI for discipline.
- **Stack (100% free):** Apache Spark (↔ Databricks / Synapse Spark), Dagster OSS (↔ Dagster+ / ADF), Airflow (one comparison DAG; ↔ MWAA / Composer), Iceberg branches for WAP (↔ Snowflake clones), lakeFS optional layer (↔ —), GitHub Actions (↔ Azure DevOps), Testcontainers + pytest via uv, Flyway (↔ Liquibase Pro), all on the Phase-2 compose stack.
- **Build:** (1) Spark job computes daily NAV + rolling performance from 50M-row holdings/prices into silver Iceberg; (2) Dagster assets wrap ingestion → Spark → dbt gold with daily partitions and asset checks; (3) WAP: every load lands on a branch, publishes only on green checks; (4) CI runs lint, unit, integration (Testcontainers), and slim dbt build per PR; (5) Flyway manages the Postgres source schema, demonstrated with a live expand–contract change; (6) 30-day backfill executed and timed.
- **Architecture deliverables:** C4 container diagram updated with compute/orchestration layer; ADR-007 orchestrator selection (Dagster vs Airflow vs ADF), ADR-008 WAP via Iceberg branches, ADR-009 Spark-vs-DuckDB engine threshold (when the cluster is justified).
- **Acceptance criteria:** full pipeline green from `dagster dev` + one CLI command; corrupted-load drill leaves gold untouched with an audit trail; skewed-join fix documented with UI screenshots; backfill recomputes exactly the intended partitions; CI blocks a breaking PR in under 10 minutes.
- Est. hours: 20

*Phase 3 total: 118 h (T1/T2 entries 95 h + T3 2.5 h + capstone 20 h ≈ 118)*
