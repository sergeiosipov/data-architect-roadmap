<a id="phase-3"></a>
## Phase 3: Distributed Compute, Orchestration & Engineering Practice (months 17–21, 118 h)

**Goal:** close the two biggest gaps that block scale — Spark and orchestration — and wrap the platform in software-engineering discipline: CI/CD for data, data versioning with write-audit-publish, integration testing, and managed schema change.
**Entry prerequisites:** Phase 2 (lakehouse running; dbt project to orchestrate).
**Exit criteria:** you can (1) explain a Spark job's stages and fix a skewed join from the UI; (2) defend Airflow vs Dagster vs ADF for a given team; (3) ship a pipeline change through CI with tests, data diff, and an audited publish; (4) run schema change in a regulated estate without downtime (expand–contract).

### T1/T2 topics

#### 4.1.1 Distributed batch compute (Spark) — T1
- **Why:** Spark is the named weak spot and the default heavy-lift engine in every fund-data estate — Databricks, Synapse and Fabric all sell it, so the architect signs off on Spark designs whether or not they chose Spark. An architect who can't read the Spark UI can't review the platform's biggest bills, can't challenge a vendor's "just add nodes" answer, and will rubber-stamp a skewed NAV-calculation job that burns four hours nightly when twenty minutes would do.
- **Learn:**
  - architecture: driver/executors, jobs→stages→tasks — how one action fans out into stages split by shuffles, and why the shuffle is where money goes *(Learning Spark ch. 1–2)*
  - DataFrame API and lazy evaluation — transformations build a plan, actions trigger it; what that means for debugging *(Learning Spark ch. 3–4)*
  - Catalyst optimizer + AQE — how the planner rewrites your query and what adaptive execution fixes at runtime *(Spark docs: SQL Performance Tuning)*
  - partitioning, skew, salting — why one hot ISIN or fund ID stalls a 200-task stage at task 199 *(Spark docs: SQL Performance Tuning)*
  - join strategies — broadcast vs sort-merge, the autoBroadcastJoinThreshold, and when the planner picks wrong *(Learning Spark ch. 7)*
  - caching/persistence levels and the memory model — executor memory regions, spill, and OOM debugging from the error upward *(Spark docs: Tuning)*
  - writing to Iceberg from Spark — catalogs, `MERGE INTO`, and the WAP hooks you'll use in 9.2.2 *(Iceberg docs: Spark)*
  - deployment modes at decision level — local, standalone, K8s, Databricks; what changes operationally between them *(Learning Spark ch. 1)*
- **Resources:**
  - **[Learning Spark, 2nd ed.](https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/) (Damji et al.) ch. 1–7 + 12** — architecture, DataFrame API, Spark SQL, joins, and tuning in one pass (primary)
  - [Spark docs: Tuning](https://spark.apache.org/docs/latest/tuning.html) + [SQL Performance Tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — memory model, caching, AQE, skew-join handling — the exact knobs you'll turn in the lab (reference)
  - [Iceberg docs: Spark](https://iceberg.apache.org/docs/latest/) — Spark reads/writes into Iceberg tables, the lakehouse seam this phase exercises (reference)
  - [Spark: The Definitive Guide](https://www.oreilly.com/library/view/spark-the-definitive/9781491912201/) pt. II — alternate treatment of the structured APIs if Learning Spark's pace doesn't suit (alternate)
- **Tools:**
  - FOSS (hands-on): [Apache Spark](https://spark.apache.org/docs/latest/) — local mode + compose cluster is the whole lab (↔ Databricks / Synapse Spark / EMR)
  - Corp (evaluate): [Databricks](https://docs.databricks.com/) — the de-facto enterprise Spark; know Photon, cluster types and pricing well enough to challenge a quote
- **Do:**
  1. Generate a 50M-row holdings/prices dataset (PySpark or DuckDB export) with realistic skew: a handful of mega-funds holding most positions.
  2. Compute per-fund daily NAV and rolling 30-day performance in PySpark against MinIO/Iceberg from the Phase-2 stack; note wall-clock and shuffle volumes from the Spark UI.
  3. Engineer a skewed join (positions × fund reference data keyed on the hot fund IDs); diagnose it in the UI — find the straggler task, its shuffle read size, and the stage timeline.
  4. Fix it twice: once with a broadcast hint, once with salting; compare against AQE's automatic skew-join handling.
  5. Document before/after stage timings with UI screenshots, and finish with a one-paragraph rule of thumb for when DuckDB on one node beats the cluster.
- **Done when:**
  - [ ] Given an unfamiliar slow job, you go UI → stages → shuffle/skew → fix, and can explain each step to a junior.
  - [ ] You can explain why the skewed join stalled (one straggler task, not "Spark is slow") and show the evidence in the UI.
  - [ ] You can state the broadcast threshold trade-off and what AQE does and doesn't rescue.
  - [ ] You can argue when Spark is the *wrong* tool (DuckDB-size data) with numbers from your own runs.
- Est. hours: 36

#### 5.3.2 DataFrame transformation layer (PySpark / Polars / Ibis) — T2
- **Why:** the code half of the transformation layer; choosing SQL vs DataFrames — and which DataFrame runtime — is a standards decision the architect owns and every team inherits. Get it wrong and you end up with NAV logic duplicated in three dialects, pandas row loops melting the cluster, and no answer when an auditor asks where a number was computed.
- **Learn:**
  - PySpark idioms vs pandas habits — no row loops, window specs over groupby-apply, columnar thinking *(PySpark docs)*
  - Polars lazy frames — the query optimizer behind `LazyFrame`, and when Polars on one node replaces Spark below ~100GB *(Polars guide: Lazy API)*
  - Ibis as a portable dataframe API — one expression language compiled to 20+ engines, and what that buys a multi-engine estate *(Ibis docs: Why Ibis)*
  - UDF cost model — Python UDF vs pandas/Arrow UDF vs native expression, and why serialization is the hidden tax *(PySpark docs)*
  - layer ownership as a standard — which transformation types belong in dbt SQL vs DataFrame code, and who enforces it *(Ibis docs: Why Ibis)*
- **Resources:**
  - **[Polars user guide: Lazy API](https://docs.pola.rs/user-guide/lazy/)** — lazy frames, optimization, query plans (primary)
  - [Ibis: Why Ibis](https://ibis-project.org/why) — the portability argument and the backend model (reference)
  - [PySpark documentation](https://spark.apache.org/docs/latest/api/python/) — idioms, window functions, pandas-on-Spark and Arrow/pandas UDFs (reference)
- **Tools:**
  - FOSS (hands-on): [Polars](https://docs.pola.rs/), [Ibis](https://ibis-project.org/), [PySpark](https://spark.apache.org/docs/latest/api/python/) — three runtimes, one transformation, run via uv (↔ Snowpark)
  - Corp (evaluate): [Snowpark](https://docs.snowflake.com/en/developer-guide/snowpark/index) / [Databricks](https://docs.databricks.com/) — the same concepts rebranded; know the lock-in trade-off
- **Do:**
  1. Pick one silver transformation from the Phase-2 lakehouse (e.g. EMT-style share-class enrichment of holdings).
  2. Implement it three ways: PySpark, Polars (lazy), and dbt SQL; verify all three produce identical output on the same input sample.
  3. Time each on the 50M-row dataset and on a 1M-row sample; record where each wins.
  4. Write a half-page standards note: which layer owns which transformation type (set-based joins/aggregations vs procedural enrichment vs ML feature prep) and why, citing your timings.
- **Done when:**
  - [ ] Your standards note survives the question "why not do everything in SQL?"
  - [ ] You can name the dataset size and shape where Polars beats Spark, with your own numbers.
  - [ ] You can explain to a reviewer what a Python UDF costs versus a native expression and how you'd detect the difference in a job profile.
- Est. hours: 8

#### 5.6.1 + 5.6.3 Orchestration (Airflow + Dagster, task- vs asset-oriented) — T1
- **Why:** orchestration is in the explicit mastery bias: the scheduler is the platform's nervous system, and the task-vs-asset paradigm choice shapes team workflow for years. In a fund platform the orchestrator is what guarantees the NAV pipeline ran, in order, exactly once per valuation day — without that discipline, a missed upstream file silently produces yesterday's prices in today's report and the transfer agent finds out from a client.
- **Learn:**
  - Airflow core — DAGs, operators, sensors, and idempotent task design so reruns are safe *(Data Pipelines with Airflow ch. 1–4)*
  - backfills and catchup — how scheduled intervals, `catchup`, and `backfill` interact, and the executors (Local/Celery/K8s) that run it all *(Data Pipelines with Airflow ch. 12)*
  - Airflow datasets / data-aware scheduling — triggering on data readiness instead of clock time *(Airflow docs)*
  - Dagster software-defined assets — assets, partitions, asset checks; why asset-orientation gives lineage and freshness for free *(Dagster docs)*
  - declarative automation — letting the orchestrator derive "what needs to run" from asset state rather than hand-wired triggers *(Dagster docs)*
  - failure handling — retries, SLAs/freshness alerts, and what a sane on-call page contains *(Data Pipelines with Airflow ch. 12)*
  - orchestrator anti-patterns — business logic in DAG files, XCom abuse, non-idempotent tasks *(Airflow docs)*
  - the market map — Prefect/Mage awareness; ADF + Workflow Orchestration Manager (managed Airflow) as the Azure reality *(ADF docs)*
- **Resources:**
  - **[Dagster documentation](https://docs.dagster.io/)** — assets, partitions, asset checks, declarative automation (primary)
  - [Data Pipelines with Apache Airflow, 2nd ed.](https://www.manning.com/books/data-pipelines-with-apache-airflow-second-edition) (Harenslak, de Ruiter et al.) ch. 1–6, 12 — task-oriented orchestration done properly, incl. backfills and operations (reference)
  - [Apache Airflow documentation](https://airflow.apache.org/docs/) — executors, data-aware scheduling, best-practices section on anti-patterns (reference)
  - [Azure Data Factory documentation](https://learn.microsoft.com/azure/data-factory/) — the corp baseline you'll be asked to compare against (evaluation)
- **Tools:**
  - FOSS (hands-on): [Dagster](https://docs.dagster.io/) — primary orchestrator for the capstone (↔ Dagster+ / ADF)
  - FOSS (market fluency): [Apache Airflow](https://airflow.apache.org/docs/) — one comparison DAG; the incumbent in most fund-admin shops (↔ MWAA / Cloud Composer)
  - Corp (evaluate): [Azure Data Factory](https://learn.microsoft.com/azure/data-factory/), [MWAA](https://docs.aws.amazon.com/mwaa/), [Cloud Composer](https://cloud.google.com/composer/docs) — managed offerings at build-vs-buy level: pricing model, upgrade cadence, lock-in
- **Do:**
  1. Orchestrate the Capstone-2 pipeline as Dagster assets with daily partitions; add asset checks for row counts and NAV-total reconciliation.
  2. Wire declarative automation so the gold layer rebuilds when silver assets materialize, not on a cron guess.
  3. Rebuild one branch of the pipeline as an Airflow DAG with a sensor, idempotent tasks, and catchup configured deliberately.
  4. Break a transformation, fix it, then run a 30-day backfill in each tool; record which partitions recomputed and how you proved it.
  5. Write a comparison memo (dev loop, backfills, lineage, ops burden, team skill demands) ending in a recommendation for a 6-person fund-data team on Azure.
- **Done when:**
  - [ ] You can run a clean 30-day backfill after a logic fix and explain exactly which partitions recomputed and why.
  - [ ] You can articulate task- vs asset-oriented orchestration in two minutes with one fund-industry example each.
  - [ ] Your memo defends Dagster vs Airflow vs ADF for a named team profile and survives "but ADF is already included in our Azure agreement".
- Est. hours: 20

#### 9.2.2 Data versioning & write-audit-publish — T2
- **Why:** branch-merge workflows for data are how regulated platforms ship changes without bad data reaching consumers; WAP is the pattern auditors love because the audit step is structural, not a promise. Without it, a corrupted price file lands directly in the gold layer, the NAV goes out wrong, and the remediation is a restatement letter instead of a quietly deleted branch.
- **Learn:**
  - Iceberg branches and tags natively — snapshot lineage, branch retention, and tags as immutable audit markers *(Iceberg docs: Branching and Tagging)*
  - the write-audit-publish flow — write to a staging branch, run checks, fast-forward main only on green *(Iceberg docs: Branching and Tagging)*
  - lakeFS Git-like model — repos, branches, merges over object storage, when you need versioning across many tables at once *(lakeFS docs)*
  - Nessie — catalog-level versioning as an alternative seam for multi-table transactions *(Project Nessie)*
  - DVC — file-oriented versioning for ML-ish artifacts; awareness only *(DVC docs)*
  - choosing the granularity — table-level (Iceberg) vs lake-level (lakeFS/Nessie) versioning, and what each costs operationally *(lakeFS docs)*
- **Resources:**
  - **[Iceberg docs: Branching and Tagging](https://iceberg.apache.org/docs/latest/branching/)** — branch/tag semantics, audit-branch use case, the WAP building blocks (primary)
  - [lakeFS documentation](https://docs.lakefs.io/) — the Git-for-data model, how it works, and the WAP tutorial (reference)
  - [Project Nessie](https://projectnessie.org/) — catalog-level versioning concept (awareness)
  - [DVC documentation](https://dvc.org/doc) — file/artifact versioning for completeness (awareness)
- **Tools:**
  - FOSS (hands-on): [Apache Iceberg](https://iceberg.apache.org/docs/latest/) branches, [lakeFS](https://docs.lakefs.io/) — (↔ no direct corp equivalent — Databricks/Snowflake time travel + clones approximate it)
  - Corp (evaluate): [Snowflake zero-copy cloning](https://docs.snowflake.com/en/user-guide/object-clone) — what clones give you and where they fall short of true branch-merge
- **Do:**
  1. Add a WAP stage to the Dagster pipeline: every load writes to an Iceberg `audit` branch instead of main.
  2. Run the existing DQ asset checks against the branch; on green, fast-forward publish to main; on red, alert and hold the branch for inspection.
  3. Inject a deliberately corrupted load (e.g. prices off by 100x for one ISIN) and walk the failure path end to end.
  4. Tag each published snapshot with the valuation date; demonstrate time-travel back to a prior tag as the audit story.
- **Done when:**
  - [ ] A deliberately corrupted load never becomes visible to the gold consumer, and you can show the audit trail.
  - [ ] You can demonstrate which snapshot a given day's NAV report was computed from, using tags alone.
  - [ ] You can explain to a CAB when table-level branching suffices and when lakeFS-style lake-level versioning is worth the extra moving part.
- Est. hours: 8

#### 9.3.1 CI/CD for data platforms — T2
- **Why:** the deployment pipeline is where engineering standards become enforceable; data teams without CI ship regressions to regulators. The architect defines what "cannot merge" means — without that gate, a broken dbt test rides into production on a Friday and the Monday NAV run is the test environment.
- **Learn:**
  - GitHub Actions core — workflows, jobs, environments, secrets, matrix builds *(GitHub Actions docs)*
  - what to run per PR vs per merge for a data repo — ruff lint, unit tests, dbt build on a prod-like sample, docs publish on merge *(dbt docs: Continuous integration)*
  - deployment gates and approvals — environments with required reviewers as the change-advisory checkpoint *(GitHub Actions docs)*
  - secrets hygiene — OIDC over long-lived keys, least-privilege tokens for the warehouse *(GitHub Actions docs)*
  - GitOps concept — declarative desired state, Argo CD awareness for the later K8s phase *(Argo CD docs)*
- **Resources:**
  - **[GitHub Actions documentation](https://docs.github.com/en/actions)** — workflows, environments, secrets, matrix jobs (primary)
  - [dbt docs: Continuous integration](https://docs.getdbt.com/docs/deploy/continuous-integration) — what a dbt CI job builds and tests, and why only modified assets (reference)
  - [Argo CD documentation](https://argo-cd.readthedocs.io/) — GitOps mechanics at awareness level (deepening)
- **Tools:**
  - FOSS (hands-on): [GitHub Actions](https://docs.github.com/en/actions) + [ruff](https://docs.astral.sh/ruff/) — the CI runner and linter for the capstone repo (↔ Azure DevOps Pipelines, GitLab CI)
  - Corp (evaluate): [Azure DevOps](https://learn.microsoft.com/azure/devops/) — the EU enterprise default; know pipelines, environments and approvals well enough to map your GitHub Actions design across
- **Do:**
  1. Add a PR workflow to the capstone repo: ruff check, `uv run pytest` (unit), then `dbt build --select state:modified+` against a prod-like sample schema.
  2. Add a merge workflow: full dbt build plus dbt docs site publish.
  3. Configure a protected environment with a required reviewer for the publish step, and store warehouse credentials as environment secrets.
  4. Open a PR that deliberately breaks a dbt test; confirm the merge is blocked and the failure is legible in the PR checks.
- **Done when:**
  - [ ] A PR that breaks a dbt test cannot merge, and you can explain every job in the workflow file.
  - [ ] You can justify the PR-vs-merge split (what runs where, and what each minute of CI costs).
  - [ ] You can sketch the equivalent Azure DevOps pipeline on a whiteboard for an enterprise that mandates it.
- Est. hours: 8

#### 9.3.2 Data-aware CI — T2
- **Why:** code-green/data-wrong is the classic data regression; data-aware CI (state deferral, data diff) catches what unit tests can't. A WHERE-clause tweak that passes every schema test can still drop 3% of share classes from the EMT feed — only comparing the data before and after the change catches that.
- **Learn:**
  - dbt slim CI — `state:modified` selection so CI builds only what changed plus downstream *(dbt docs: state method)*
  - defer — resolving unselected refs to prod artifacts instead of rebuilding the world *(dbt docs: Defer)*
  - SQLMesh virtual environments and plans — automatic change categorization (breaking vs non-breaking) and what it decides to backfill *(SQLMesh docs: Plans)*
  - data-diff concept — row/column-level diffs between prod and the PR build, and Datafold as the managed version *(data-diff README)*
  - cost model — when slim CI is enough and when diff-based CI pays for itself in warehouse spend avoided *(SQLMesh docs: Plans)*
- **Resources:**
  - **[SQLMesh docs: Plans](https://sqlmesh.readthedocs.io/en/stable/concepts/plans/)** — plans, virtual environments, breaking vs non-breaking categorization (primary)
  - [dbt docs: state:modified method](https://docs.getdbt.com/reference/node-selection/methods) — state comparison and its sub-selectors (reference)
  - [dbt docs: Defer](https://docs.getdbt.com/reference/node-selection/defer) — the deferral mechanics slim CI depends on (reference)
  - [data-diff README](https://github.com/datafold/data-diff) — the open-source diff tool and the Datafold context around it (reference)
- **Tools:**
  - FOSS (hands-on): [SQLMesh](https://sqlmesh.readthedocs.io/en/stable/) (eval hands-on), [dbt](https://docs.getdbt.com/) slim CI — two philosophies of change safety (↔ Datafold)
  - Corp (evaluate): [Datafold](https://www.datafold.com/) — managed column-level diffs in CI; know its pricing logic for a build-vs-buy memo
- **Do:**
  1. Craft one genuinely breaking change (a filter that silently drops rows) and one non-breaking change (an added column) in the capstone dbt project.
  2. Run both through dbt slim CI (`state:modified+` with `--defer`); record what was built, what passed, and what slipped through.
  3. Mirror the same two changes in a small SQLMesh project; run `sqlmesh plan` and record its categorization and proposed backfill.
  4. Tabulate: change × tool × caught/missed × compute cost; close with a one-paragraph recommendation.
- **Done when:**
  - [ ] You can tell a team when slim CI is enough and when diff-based CI pays for itself.
  - [ ] You can show one concrete change that dbt tests passed but a data diff would have caught.
  - [ ] You can explain SQLMesh's breaking/non-breaking decision for both of your changes.
- Est. hours: 5

#### 9.4.3 Integration testing for pipelines — T2
- **Why:** pipelines fail at the seams (connections, schemas, permissions); throwaway-infra tests are the only honest test of the seams. Mocked unit tests pass forever while the real loader fails on the first NUMERIC overflow from the actual Postgres — in a regulated shop, "it worked against the mock" is not a defence.
- **Learn:**
  - Testcontainers-python — real Postgres/MinIO/Kafka containers per test, lifecycle and port wiring *(Testcontainers docs)*
  - the test pyramid for data — unit SQL → component → end-to-end on a sample, and why the top is thin *(Fowler: Practical Test Pyramid)*
  - golden datasets and snapshot testing — fixture-driven known-good inputs/outputs and asserting end-state invariants *(pytest docs)*
  - idempotency as a testable property — run the loader twice, assert identical end state *(Testcontainers docs)*
  - contract tests preview — Pact's consumer-driven idea, mapped to data contracts coming in Phase 8 *(Pact docs)*
- **Resources:**
  - **[Testcontainers for Python documentation](https://testcontainers-python.readthedocs.io/)** — container fixtures for Postgres, MinIO, Kafka (primary)
  - [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) — the canonical layering argument, adapted here to data *(reference)*
  - [pytest documentation](https://docs.pytest.org/) — fixtures, markers, parametrization for golden-dataset tests (reference)
  - [Pact documentation](https://docs.pact.io/) — contract-testing concept at awareness level (deepening)
- **Tools:**
  - FOSS (hands-on): [Testcontainers](https://testcontainers-python.readthedocs.io/), [pytest](https://docs.pytest.org/) — run via uv against local Docker (↔ same)
  - Corp: same — this layer is tool-agnostic; the discipline, not the vendor, is the deliverable
- **Do:**
  1. Add a `tests/integration` package with pytest fixtures that spin up Postgres and MinIO via Testcontainers.
  2. Load a golden dataset (small holdings file with known NAV totals) and run the idempotent loader once; assert row counts, checksums and the NAV reconciliation.
  3. Run the loader a second time against the same containers; assert the end state is byte-identical (the idempotency proof).
  4. Mark the suite `-m integration`, exclude it from the default run, and wire it into the CI workflow from 9.3.1.
- **Done when:**
  - [ ] `uv run pytest -m integration` passes on a machine with only Docker installed.
  - [ ] Demonstrate the double-run idempotency assertion failing when you deliberately break the loader's upsert.
  - [ ] Explain where the integration layer sits in your test pyramid and what stays in unit tests below it.
- Est. hours: 5

#### 9.7.1 Schema migrations & change management — T2
- **Why:** regulated estates change schemas under change-advisory scrutiny; expand–contract and versioned migrations are how you do it without downtime or drama. A column rename done naively takes the transfer-agency feed down mid-dealing-window; done as parallel change, nobody notices — and the migration history table is the CAB evidence.
- **Learn:**
  - Flyway's model — versioned vs repeatable/declarative migrations, checksums, the schema history table *(Flyway docs)*
  - Alembic — the Python-shop equivalent: autogenerate, review, and the offline SQL mode for DBA sign-off *(Alembic docs)*
  - expand–contract (parallel change) — add-new, migrate-writes, backfill, contract-old as separate deployable steps *(Fowler: Parallel Change)*
  - deployment ordering — DB before code, every migration backward-compatible with the running release *(Fowler: Evolutionary Database Design)*
  - rollback reality — why you roll forward, and what a tested down-path is actually for *(Flyway docs)*
- **Resources:**
  - **[Flyway documentation](https://documentation.red-gate.com/fd)** — concepts, versioned migrations, history table (primary)
  - [Martin Fowler: Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) — the expand–contract pattern itself (reference)
  - [Martin Fowler: Evolutionary Database Design](https://martinfowler.com/articles/evodb.html) — migrations as the unit of database change in a delivery pipeline (deepening)
  - [Alembic documentation](https://alembic.sqlalchemy.org/) — the Python alternative you may standardize on instead (alternate)
- **Tools:**
  - FOSS (hands-on): [Flyway](https://documentation.red-gate.com/fd) or [Alembic](https://alembic.sqlalchemy.org/) — pick one for the lab (↔ Liquibase enterprise, Redgate)
  - Corp (evaluate): [Liquibase](https://docs.liquibase.com/) Pro / Azure DevOps-integrated change flows — what the governed-pipeline tier adds: drift detection, targeted rollback, approvals
- **Do:**
  1. Put the Phase-1 Postgres schema under Flyway (or Alembic) control: baseline migration plus history table.
  2. Plan a column rename on a table the loader writes to, as three migrations: V2 expand (add new column + sync trigger or dual-write), V3 backfill + switch reads, V4 contract (drop old column).
  3. Keep the loader running on a schedule throughout; apply each migration live and watch for failed loads.
  4. Record the migration history and write a five-line CAB-style change record: risk, rollback stance (roll forward), evidence.
- **Done when:**
  - [ ] Zero failed loads during the rename, and the migration history table tells the full story.
  - [ ] Explain why the contract step shipped last and what would break if V2 and V4 were one migration.
  - [ ] Defend "roll forward" to a change board that asks for a rollback script.
- Est. hours: 5

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 4.4.1 | General distributed frameworks | Ray/Dask — Python-native distributed compute beyond Spark; ML-leaning, actor-based scaling | [Ray "Overview" docs page](https://docs.ray.io/en/latest/ray-overview/index.html) | 30 |
| 4.4.2 | Specialized frameworks | Modin etc. — drop-in pandas acceleration on Ray/Dask; niche in practice | [Modin README](https://github.com/modin-project/modin) | 10 |
| 5.1.2 | Code-first ETL (NiFi) | Visual flow-based ingestion engine; common in banks' legacy ingestion estates you may inherit | [NiFi "Overview" doc](https://nifi.apache.org/documentation/) | 25 |
| 9.4.4 | Load/performance testing | k6/Locust/JMeter — throughput and latency testing for data APIs and query engines | [k6 "What is k6" page](https://grafana.com/docs/k6/latest/) | 25 |
| 9.5.2 | Data diff tools | Row-level diffs across model changes (data-diff, Datafold); seen hands-on in 9.3.2 | [Datafold data-diff README](https://github.com/datafold/data-diff) | 20 |
| 9.6.1 | Code documentation | MkDocs/Sphinx static docs sites; you'll publish dbt docs instead | [MkDocs getting started](https://www.mkdocs.org/getting-started/) | 20 |
| 9.9.1 | Notebooks in production | Papermill/Ploomber parameterized notebook jobs; contested practice in regulated shops | [Papermill README](https://github.com/nteract/papermill) | 20 |

*T3 subtotal: 2.5 h*

### Capstone 3 — Orchestrated Spark NAV pipeline

- **Goal:** the lakehouse grows an industrial-strength compute and delivery layer: Spark for scale, Dagster for orchestration, WAP for safety, CI for discipline.
- **Stack (100% free):** [Apache Spark](https://spark.apache.org/docs/latest/) (↔ [Databricks](https://docs.databricks.com/) / [Synapse Spark](https://learn.microsoft.com/azure/synapse-analytics/)), [Dagster OSS](https://docs.dagster.io/) (↔ Dagster+ / [ADF](https://learn.microsoft.com/azure/data-factory/)), [Airflow](https://airflow.apache.org/docs/) (one comparison DAG; ↔ [MWAA](https://docs.aws.amazon.com/mwaa/) / [Composer](https://cloud.google.com/composer/docs)), [Iceberg](https://iceberg.apache.org/docs/latest/branching/) branches for WAP (↔ [Snowflake clones](https://docs.snowflake.com/en/user-guide/object-clone)), [lakeFS](https://docs.lakefs.io/) optional layer (↔ —), [GitHub Actions](https://docs.github.com/en/actions) (↔ [Azure DevOps](https://learn.microsoft.com/azure/devops/)), [Testcontainers](https://testcontainers-python.readthedocs.io/) + [pytest](https://docs.pytest.org/) via [uv](https://docs.astral.sh/uv/), [Flyway](https://documentation.red-gate.com/fd) (↔ [Liquibase Pro](https://docs.liquibase.com/)), all on the Phase-2 compose stack.
- **Build:** (1) Spark job computes daily NAV + rolling performance from 50M-row holdings/prices into silver Iceberg, reusing the skew fixes from 4.1.1; (2) Dagster assets wrap ingestion → Spark → dbt gold with daily partitions and asset checks (row counts + NAV reconciliation); (3) WAP: every load lands on an Iceberg audit branch, publishes to main only on green checks, holds and alerts on red; (4) CI runs lint (ruff), unit, integration (Testcontainers), and slim dbt build (`state:modified+` with defer) per PR; (5) Flyway manages the Postgres source schema, demonstrated with a live expand–contract change under a running loader; (6) 30-day backfill executed and timed, with the recomputed partition set documented.
- **Architecture deliverables:** C4 container diagram updated with compute/orchestration layer; ADR-007 orchestrator selection (Dagster vs Airflow vs ADF), ADR-008 WAP via Iceberg branches, ADR-009 Spark-vs-DuckDB engine threshold (when the cluster is justified).
- **Acceptance criteria:** full pipeline green from `dagster dev` + one CLI command; corrupted-load drill leaves gold untouched with an audit trail (branch held, alert fired, snapshot evidence); skewed-join fix documented with before/after Spark-UI screenshots and stage timings; backfill recomputes exactly the intended partitions and nothing else; CI blocks a breaking PR in under 10 minutes with a legible failure; expand–contract change applied with zero failed loads.
- Est. hours: 20

*Phase 3 total: 118 h (T1/T2 entries 95 h + T3 2.5 h + capstone 20 h ≈ 118)*
