# Working list — parse + tiering (scratch; not the deliverable)

Canonical counting scheme: subcategory = bold bullet item under a category; concept-list
categories 1.8/1.9 counted per concept; 1.10 as one unit; 1.11 as 3 groups; 1.12 per
standard; cross-reference pointers (5.5, 6.5, 10.8) get IDs and go to Excluded.
Total: 252 IDs. Tiers: T1=48 (19.0%), Skip=13, Excluded=5, rest T2/T3.

Phases: P1 Distributed data systems & modeling core · P2 Lakehouse & analytics engineering
(+ fin-data standards) · P3 Distributed compute, orchestration & engineering practice ·
P4 Streaming & integration · P5 Cloud platform architecture (Azure) & operations ·
P6 Governance, security & compliance · P7 AI/ML & LLM platforms · P8 Data products,
semantic, consumption & architect practice. Skip = covered by profile.

| ID | Subcategory | Tier | Phase | Note / T1 justification |
|---|---|---|---|---|
| 1.1.1 | Structured data | T3 | P0 | taught from zero (0.7) |
| 1.1.2 | Semi-structured data | T3 | P0 | taught from zero (0.7) |
| 1.1.3 | Unstructured data | T3 | P0 | taught from zero (0.7) |
| 1.1.4 | Vector / embeddings | T2 | P7 | |
| 1.2.1 | Batch paradigm | T3 | P0 | taught from zero (0.8) |
| 1.2.2 | Micro-batch | T2 | P4 | |
| 1.2.3 | Streaming paradigm | T2 | P4 | depth via 1.9/4.2 |
| 1.2.4 | Real-time / low-latency | T3 | P4 | |
| 1.3.1 | OLTP | T2 | P0 | taught from zero (0.8) |
| 1.3.2 | OLAP | T2 | P0 | taught from zero (0.8) |
| 1.3.3 | HTAP | T3 | P1 | |
| 1.3.4 | RT / user-facing analytics | T3 | P4 | |
| 1.4.1 | Lambda architecture | T2 | P4 | |
| 1.4.2 | Kappa architecture | T2 | P4 | |
| 1.4.3 | Medallion | T1 | P2 | T1: default layering of every lakehouse he will design; must defend layer contracts |
| 1.4.4 | Data Mesh | T2 | P8 | |
| 1.4.5 | Data Fabric | T3 | P8 | |
| 1.4.6 | Hub-and-Spoke | T3 | P2 | |
| 1.4.7 | Data Vault (pattern) | T2 | P2 | deep at 8.2.5 |
| 1.5.1 | Row vs columnar | T2 | P1 | |
| 1.5.2 | MPP | T2 | P1 | |
| 1.5.3 | Shared-nothing vs shared-disk | T2 | P1 | |
| 1.5.4 | Storage/compute separation | T2 | P1 | |
| 1.6.1 | ACID & isolation levels | T1 | P1 | T1: transaction guarantees underpin every regulated-data design review; must teach isolation anomalies |
| 1.6.2 | BASE | T3 | P1 | |
| 1.6.3 | Eventual consistency | T2 | P1 | |
| 1.6.4 | Strong consistency | T2 | P1 | |
| 1.6.5 | RYW / monotonic / causal | T2 | P1 | |
| 1.7.1 | CAP | T1 | P1 | T1: invoked in every distributed design tradeoff; architect must correct misuse |
| 1.7.2 | PACELC | T1 | P1 | T1: the latency half is what actually drives cloud DB selection |
| 1.8.1 | Idempotency | T1 | P1 | T1: retry-safety is the #1 pipeline reliability lever; must design and review for it |
| 1.8.2 | Delivery semantics | T1 | P4 | T1: exactly-once claims must be audited for settlement/NAV flows |
| 1.8.3 | Outbox pattern | T1 | P4 | T1: the standard answer to dual-write in event-driven fund platforms |
| 1.8.4 | Saga pattern | T1 | P4 | T1: trade lifecycle = long-running distributed transaction; sagas are the bedrock |
| 1.8.5 | Event sourcing | T1 | P4 | T1: audit-by-construction is the killer feature for regulated finance |
| 1.8.6 | CQRS | T2 | P4 | |
| 1.8.7 | Dead-letter queue | T2 | P4 | |
| 1.8.8 | Backpressure | T2 | P4 | |
| 1.8.9 | Two-phase commit | T2 | P1 | know why it is avoided |
| 1.8.10 | CDC (pattern) | T1 | P4 | T1: primary integration pattern off core banking/TA systems; designs hinge on it |
| 1.8.11 | Strangler fig | T2 | P8 | |
| 1.8.12 | Bulkhead | T3 | P4 | |
| 1.8.13 | Circuit breaker | T3 | P4 | |
| 1.9.1 | Watermarks | T1 | P4 | T1: correctness of event-time aggregation rests on watermark reasoning |
| 1.9.2 | Windowing | T1 | P4 | T1: must design window strategy for price/flow aggregation and debug wrong results |
| 1.9.3 | Late data handling | T2 | P4 | |
| 1.9.4 | Event vs processing time | T1 | P4 | T1: the conceptual core of streaming; restatements in finance demand event-time rigor |
| 1.9.5 | Triggers | T2 | P4 | |
| 1.9.6 | Stateful vs stateless | T2 | P4 | |
| 1.9.7 | Schema evolution compatibility | T1 | P4 | T1: forward/backward compat policy is a governance decision the architect owns |
| 1.10.1 | Modeling notations (overview) | T2 | P1 | deep at 8.5.1 |
| 1.11.1 | Data protocols (HTTP…ADBC) | T2 | P4 | |
| 1.11.2 | Serialization formats | T2 | P4 | w/ 8.3.2 |
| 1.11.3 | Async API standards | T2 | P4 | AsyncAPI/CloudEvents |
| 1.12.1 | ISO 20022 | T1 | P2 | T1: the lingua franca of EU securities/payments messaging; fund platforms ingest/emit it |
| 1.12.2 | LEI (ISO 17442) | T2 | P2 | |
| 1.12.3 | ISIN | T2 | P2 | |
| 1.12.4 | CFI | T3 | P2 | |
| 1.12.5 | FIGI | T3 | P2 | |
| 1.12.6 | FIBO | T2 | P6 | w/ KG/RDF |
| 1.12.7 | EMT/EPT (FinDatEx) | T1 | P2 | T1: core fund-data dissemination templates in Lux fund industry (Kneip domain) |
| 1.12.8 | SWIFT MT/MX | T2 | P2 | |
| 1.12.9 | FpML | T3 | P2 | |
| 1.12.10 | FIX | T3 | P2 | |
| 1.12.11 | IBAN / SEPA | T3 | P2 | |
| 1.12.12 | DCAM | T1 | P6 | T1: the FS data-management capability model; architects lead DCAM assessments |
| 2.1.1 | ELT connectors | T2 | P2 | Airbyte / Fivetran |
| 2.1.2 | Bulk load utilities | T2 | P5 | ADF |
| 2.2.1 | Log/metric shippers | T3 | P5 | |
| 2.2.2 | Stream connectors | T2 | P4 | Kafka Connect |
| 2.3.1 | Log-based CDC | T1 | P4 | T1: Debezium-class CDC is how regulated estates go event-driven without touching sources |
| 2.3.2 | Trigger-based CDC | T3 | P4 | |
| 2.3.3 | Snapshot-based CDC | T3 | P4 | |
| 2.4.1 | Distributed logs (Kafka) | T1 | P4 | T1: backbone of modern financial data integration; must size, secure, debug it |
| 2.4.2 | Message brokers | T2 | P4 | queue vs log semantics |
| 2.4.3 | Event mesh | T3 | P4 | Solace aware |
| 2.5.1 | iPaaS | T3 | P5 | |
| 2.5.2 | ESB (legacy) | T3 | P5 | |
| 2.6.1 | API gateways | T2 | P8 | w/ 13.4 |
| 2.6.2 | GraphQL layers | T3 | P8 | |
| 2.7.1 | Reverse ETL | T3 | P8 | |
| 3.1.1 | Cloud data warehouse | T2 | P2 | |
| 3.1.2 | On-prem MPP warehouse | T3 | P2 | |
| 3.1.3 | Data lake | T2 | P2 | |
| 3.1.4 | Data lakehouse | T1 | P2 | T1: the target architecture for fund data platforms; he must design and defend one |
| 3.2.1 | OLTP / relational internals | T1 | P1 | T1: indexing, planners, MVCC ground every storage decision; CMU 15-445 depth |
| 3.2.2 | NoSQL document | T3 | P1 | |
| 3.2.3 | NoSQL key-value | T3 | P1 | |
| 3.2.4 | NoSQL wide-column | T3 | P1 | |
| 3.2.5 | Property graph | T3 | P6 | |
| 3.2.6 | Knowledge graph / RDF | T2 | P6 | FIBO |
| 3.2.7 | Time-series | T3 | P5 | |
| 3.2.8 | Search | T3 | P7 | hybrid search w/ RAG |
| 3.2.9 | Vector storage | T2 | P7 | pgvector/Qdrant |
| 3.2.10 | HTAP stores | T3 | P1 | |
| 3.2.11 | Geospatial | T3 | P2 | |
| 3.3.1 | Object storage | T2 | P2 | MinIO ↔ ADLS |
| 3.3.2 | Block storage | T3 | P5 | |
| 3.3.3 | File storage | T3 | P5 | |
| 3.3.4 | Caching | T2 | P5 | |
| 3.4.1 | File formats | T1 | P2 | T1: Parquet internals (row groups, encodings, pushdown) drive cost/perf reasoning |
| 3.4.2 | Table formats | T1 | P2 | T1: Iceberg/Delta ACID metadata is the heart of lakehouse design and debugging |
| 3.4.3 | Table-format catalogs | T2 | P2 | REST spec, Polaris/Unity |
| 4.1.1 | Distributed batch engines | T1 | P3 | T1: Spark is the listed weak spot and the default engine he must implement and tune |
| 4.1.2 | Serverless compute | T2 | P5 | Azure Functions |
| 4.2.1 | Stateful stream processing | T1 | P4 | T1: Flink-class engines power real-time NAV/risk; must build and checkpoint one |
| 4.2.2 | Cloud-native streaming | T2 | P5 | Event Hubs/ASA |
| 4.3.1 | MPP SQL engines | T2 | P2 | Trino hands-on |
| 4.3.2 | Cloud query services | T2 | P5 | Synapse serverless |
| 4.3.3 | Embedded / single-node | T2 | P2 | DuckDB |
| 4.3.4 | RT/user-facing analytics engines | T3 | P4 | |
| 4.3.5 | Streaming databases | T3 | P4 | |
| 4.4.1 | General distributed frameworks | T3 | P3 | Ray/Dask |
| 4.4.2 | Specialized frameworks | T3 | P3 | |
| 5.1.1 | Visual ETL | T3 | P5 | Informatica/SSIS aware (EU FS legacy) |
| 5.1.2 | Code-first ETL | T3 | P3 | NiFi aware |
| 5.2.1 | In-warehouse SQL ELT (dbt) | T1 | P2 | T1: already adopting; dbt mastery is the modeling-to-production bridge he owns |
| 5.2.2 | ELT orchestrated | T2 | P2 | Fivetran+dbt build-vs-buy |
| 5.3.1 | SQL transformation layer | T1 | P2 | T1: merged with 5.2.1 — model graphs, testing, docs as one discipline |
| 5.3.2 | Code transformation (DataFrames) | T2 | P3 | PySpark/Polars |
| 5.3.3 | Alternative query languages | T3 | P2 | PRQL/Malloy |
| 5.4.1 | Interactive prep | T3 | P2 | |
| 5.4.2 | Code-first wrangling | T2 | P0 | pandas from zero (0.9) |
| 5.5.1 | Reverse ETL (pointer) | — | Excluded | duplicate of 2.7.1 |
| 5.6.1 | Workflow orchestrators | T1 | P3 | T1: orchestration is in the explicit T1 bias; Airflow/Dagster mastery req'd |
| 5.6.2 | Cloud-native orchestration | T2 | P5 | ADF |
| 5.6.3 | Data-aware orchestration | T2 | P3 | Dagster assets (w/ 5.6.1) |
| 5.6.4 | Durable execution | T2 | P4 | Temporal |
| 5.6.5 | BPM / process orchestration | T2 | P4 | Camunda, BPMN/DMN |
| 6.1.1 | OS feature stores | T2 | P7 | Feast |
| 6.1.2 | Managed feature stores | T3 | P7 | |
| 6.2.1 | Training frameworks | T3 | P7 | |
| 6.2.2 | Distributed training | T3 | P7 | |
| 6.2.3 | Managed training | T3 | P7 | |
| 6.3.1 | OS model serving | T3 | P7 | |
| 6.3.2 | Managed endpoints | T3 | P7 | |
| 6.4.1 | E2E MLOps platforms | T2 | P7 | MLflow |
| 6.4.2 | Managed MLOps | T2 | P7 | Azure ML eval |
| 6.5.1 | Vector DBs (pointer) | — | Excluded | duplicate of 3.2.9 |
| 6.6.1 | Embedding models | T2 | P7 | |
| 6.6.2 | RAG frameworks | T2 | P7 | LlamaIndex |
| 6.6.3 | RAG platforms | T2 | P7 | Azure AI Search eval |
| 6.7.1 | OS experiment tracking | T3 | P7 | in MLflow entry |
| 6.7.2 | Managed tracking | T3 | P7 | |
| 6.8.1 | Prompt mgmt & tracing | T2 | P7 | Langfuse |
| 6.8.2 | LLM evaluation | T2 | P7 | Ragas |
| 7.1.1 | OS semantic layer | T2 | P8 | Cube/MetricFlow |
| 7.1.2 | Platform semantic layers | T2 | P8 | Power BI |
| 7.2.1 | Metrics layer | T2 | P8 | w/ 7.1.1 |
| 7.3.1 | Business glossary | T2 | P6 | |
| 7.3.2 | Glossary in catalogs | T3 | P6 | |
| 8.1.1 | Cloud provider reference arch | T1 | P5 | T1: Azure WAF/CAF is the daily design language on the primary cloud |
| 8.1.2 | Vendor reference arch | T2 | P5 | Databricks/Fabric |
| 8.1.3 | Industry reference (TOGAF/DMBOK) | T2 | P8 | |
| 8.2.1 | Conceptual modeling | T1 | P1 | T1: data modeling is the first bias item; business-entity models are his signature artifact |
| 8.2.2 | Logical modeling | T1 | P1 | T1: keys, normalization, vendor-agnostic rigor — must teach |
| 8.2.3 | Physical modeling | T1 | P1 | T1: DDL-level decisions (partitioning, types) he must own per engine |
| 8.2.4 | Dimensional modeling | T1 | P1 | T1: Kimball is the dominant analytical model in regulated reporting marts |
| 8.2.5 | Data Vault modeling | T1 | P2 | T1: the FS-favored auditable EDW pattern; raw vault on lake is common in Lux |
| 8.2.6 | Anchor / 6NF | T3 | P2 | |
| 8.3.1 | Schema registries | T2 | P4 | |
| 8.3.2 | Schema languages | T2 | P4 | w/ 1.11.2 |
| 8.4.1 | Domain-driven design | T1 | P8 | T1: bounded contexts define data-product boundaries; foundation of mesh designs |
| 8.5.1 | Architecture notations & tools | T1 | P1 | T1: C4 + ADRs are the explicit bias; the artifacts that define the role |
| 9.1.1 | IDEs | T3 | P0 | taught from zero (0.10) |
| 9.1.2 | Notebooks | T3 | P0 | taught from zero (0.10) |
| 9.1.3 | Local data sandboxes | T2 | P1 | capstone substrate |
| 9.2.1 | Git & hosting | T2 | P0 | taught from zero (0.4) |
| 9.2.2 | Data versioning | T2 | P3 | lakeFS/Nessie |
| 9.3.1 | CI/CD pipelines | T2 | P3 | |
| 9.3.2 | Data-specific CI | T2 | P3 | |
| 9.4.1 | Unit testing | T2 | P0 | taught from zero (0.11) |
| 9.4.2 | Data quality testing | T1 | P6 | T1: merged w/ 10.4.1 — DQ engineering is non-negotiable in regulated data |
| 9.4.3 | Integration testing | T2 | P3 | Testcontainers |
| 9.4.4 | Load/perf testing | T3 | P3 | |
| 9.5.1 | Code review | T3 | P0 | taught from zero (0.12) |
| 9.5.2 | Data diff | T3 | P3 | |
| 9.6.1 | Code docs | T3 | P3 | |
| 9.6.2 | Data docs | T2 | P2 | dbt docs |
| 9.7.1 | Schema migrations | T2 | P3 | Flyway/Liquibase |
| 9.8.1 | Synthetic data | T2 | P6 | SDV/Faker |
| 9.8.2 | Test data management | T3 | P6 | |
| 9.9.1 | Notebooks in production | T3 | P3 | |
| 9.10.1 | Cloud-agnostic IaC | T1 | P5 | T1: listed weak spot; every platform he designs ships as Terraform/OpenTofu |
| 9.10.2 | Cloud-native IaC | T2 | P5 | Bicep |
| 9.10.3 | Configuration management | T3 | P5 | |
| 10.1.1 | Active metadata platforms | T1 | P6 | T1: governance & lineage bias; catalog is the control plane of a governed platform |
| 10.1.2 | Enterprise catalogs | T2 | P6 | Purview/Collibra eval |
| 10.2.1 | AI-native discovery | T3 | P6 | |
| 10.2.2 | Catalog-embedded discovery | T3 | P6 | |
| 10.3.1 | Lineage (standards) | T1 | P6 | T1: BCBS-239-grade traceability is a regulatory expectation; OpenLineage hands-on |
| 10.3.2 | Lineage in catalogs | T3 | P6 | |
| 10.4.1 | OS data quality | T1 | P6 | T1: see 9.4.2 — design DQ rules from profiling to alerting |
| 10.4.2 | Managed/enterprise DQ | T2 | P6 | |
| 10.4.3 | Data profiling | T2 | P6 | |
| 10.5.1 | Master data management | T1 | P6 | T1: security/fund/counterparty master is THE fund-industry data problem |
| 10.5.2 | Modern / cloud MDM | T3 | P6 | |
| 10.6.1 | Reference data management | T2 | P6 | ISIN/LEI code lists |
| 10.6.2 | RDM inside MDM | T3 | P6 | |
| 10.7.1 | Lifecycle / retention (cloud) | T2 | P6 | |
| 10.7.2 | Enterprise ILM | T3 | P6 | |
| 10.8.1 | Audit & compliance (pointer) | — | Excluded | duplicate of §11 |
| 10.9.1 | Pipeline observability | T2 | P6 | |
| 10.9.2 | OS data observability | T2 | P6 | w/ 10.9.1 |
| 11.1.1 | Identity providers | T2 | P6 | Keycloak/Entra |
| 11.1.2 | Fine-grained access control | T1 | P6 | T1: RLS/CLS/ABAC on fund data is a regulatory requirement he must design and prove |
| 11.1.3 | Policy-as-code | T2 | P6 | OPA |
| 11.2.1 | Key management | T2 | P6 | Key Vault |
| 11.2.2 | Database encryption / TDE | T3 | P6 | |
| 11.3.1 | Masking / tokenization | T2 | P6 | |
| 11.3.2 | Built-in DB masking | T2 | P6 | w/ 11.3.1 |
| 11.4.1 | PII detection & redaction | T2 | P6 | Presidio |
| 11.5.1 | Privacy / consent mgmt | T3 | P6 | |
| 11.6.1 | Audit logging / SIEM | T2 | P6 | |
| 11.7.1 | Regulatory compliance frameworks | T1 | P6 | T1: GDPR/DORA/SOC2 shape every architecture decision in Lux financial services |
| 11.8.1 | Secrets management | T2 | P5 | |
| 12.1.1 | Cloud-native backup | T2 | P5 | |
| 12.1.2 | Enterprise backup | T3 | P5 | |
| 12.2.1 | DR tooling | T3 | P5 | |
| 12.2.2 | DR patterns | T1 | P5 | T1: RTO/RPO and multi-region design are DORA-driven architect deliverables |
| 12.3.1 | FinOps / cost mgmt | T1 | P5 | T1: explicit bias; cost models decide architectures in vendor selection |
| 12.3.2 | Data-specific FinOps | T2 | P5 | |
| 12.4.1 | SLA/SLO management | T2 | P8 | data SLAs w/ contracts |
| 12.5.1 | On-call / paging | T3 | P5 | |
| 12.5.2 | Postmortems | T3 | P5 | |
| 12.6.1 | Capacity planning | T3 | P5 | |
| 12.7.1 | Commercial APM | T3 | P5 | |
| 12.7.2 | OS observability stack | T2 | P5 | OTel/Prom/Grafana |
| 13.1.1 | Data contracts (tools) | T1 | P8 | T1: contracts operationalize governance; the mechanism behind productized fund data |
| 13.1.2 | Data contract standards | T2 | P8 | ODCS (w/ 13.1.1) |
| 13.2.1 | Mesh enabling platforms | T2 | P8 | Trino/Starburst |
| 13.3.1 | Internal marketplaces | T3 | P8 | |
| 13.3.2 | Cross-org sharing | T2 | P8 | Delta Sharing |
| 13.3.3 | Commercial data marketplaces | T3 | P8 | market-data feeds |
| 13.4.1 | GraphQL data APIs | T3 | P8 | |
| 13.4.2 | REST data APIs | T2 | P8 | PostgREST/FastAPI |
| 13.5.1 | Standalone CDPs | — | Excluded | B2C martech; no fund-data relevance |
| 13.5.2 | Composable CDPs | — | Excluded | B2C martech; no fund-data relevance |
| 14.1.1 | Modern cloud BI | T2 | P8 | Power BI |
| 14.1.2 | On-prem / legacy BI | T3 | P8 | |
| 14.1.3 | Open-source BI | T2 | P8 | Superset/Metabase (w/ 14.1.1) |
| 14.2.1 | Viz libraries | T3 | P8 | |
| 14.3.1 | Embedded analytics | T3 | P8 | |
| 14.4.1 | Operational reporting | T3 | P8 | |
| 14.4.2 | Regulatory reporting | T1 | P8 | T1: AIFMD/PRIIPs/MiFID submission pipelines are the domain's flagship deliverable |
| 14.5.1 | Cloud notebooks | T3 | P8 | |
| 14.5.2 | Self-hosted notebooks | T3 | P0 | taught from zero (0.9) |
| 14.6.1 | Data app frameworks | T2 | P8 | Streamlit |
| 14.6.2 | Internal tool builders | T3 | P8 | |
| 14.7.1 | Anomaly alerting | T3 | P6 | w/ DQ |
| 14.7.2 | Reverse-ETL activation | T3 | P8 | |
| 14.7.3 | Notification tools | T3 | P5 | |

Tier counts (script-verified): T1=48 (19.0%) · T2=109 (43.3%) · T3=90 (35.7%) · Excluded=5 · Total=252 · 0 duplicate IDs.
Per-phase T1 (script-verified): P0=0 · P1=10 · P2=9 · P3=2 · P4=12 · P5=4 · P6=8 · P7=0 · P8=3.
Phase rows: P0=13 · P1=26 · P2=33 · P3=16 · P4=40 · P5=31 · P6=38 · P7=19 · P8=31 · Excluded=5.
Phase 0 added on user instruction (2026-06-12): no profile-based skipping; each P0 module
carries a skip test. Non-taxonomy basics live in Appendix A as A.27-A.31.
