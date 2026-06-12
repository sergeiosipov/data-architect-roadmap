<a id="appendix-d"></a>
## Appendix D — Tool Equivalence Map

Build-vs-buy cheat sheet, one table per taxonomy domain, derived from the taxonomy's `(OS)/(SA)/(C)/(E)` tags and this plan's selections. **FOSS pick** = what you practice on (always free to run); **Corp/cloud leader** = what EU financial-services job ads and vendor selections name; the last column is the honest one-liner for when buying wins.

### 1 Fundamentals
| Category | FOSS pick (hands-on) | Corp/cloud leader (evaluate) | When the corporate option wins |
|---|---|---|---|
| Modeling notations (1.10) | draw.io, Mermaid, Structurizr Lite | Sparx EA, Visual Paradigm | regulated EA repository, multi-user model governance, traceability mandates |
| Financial standards tooling (1.12) | Python/lxml validators + free specs (ISO 20022, FinDatEx) | SWIFT tooling, vendor message libraries | filing connectivity and standard-version maintenance must be vendor-backed |

### 2 Connectivity
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Batch ELT connectors (2.1) | Airbyte OSS | Fivetran; Azure Data Factory | long-tail SaaS connectors with SLAs beat the ops cost of self-hosting |
| Streaming ingestion / shippers (2.2) | Fluent Bit, Vector, Kafka Connect | Datadog agents, Event Hubs Capture | bundled into a licensed observability/streaming estate |
| CDC (2.3) | Debezium | Qlik Replicate, Oracle GoldenGate, Fivetran HVR | exotic legacy sources (mainframe, large Oracle) + vendor accountability |
| Event streaming (2.4) | Apache Kafka / Redpanda | Confluent Cloud, Azure Event Hubs | scarce ops headcount, enterprise SLAs, Azure-native networking/identity |
| Message brokers (2.4) | RabbitMQ | Azure Service Bus | cloud-native sessions/dedup/DLQ features plus zero broker ops |
| Event mesh (2.4) | NATS (lightweight) | Solace PubSub+ | multi-site capital-markets WAN routing with governance |
| iPaaS / ESB (2.5) | n8n (SA) | Power Automate, Boomi, MuleSoft | citizen-integrator demand + certified SaaS connector catalogs |
| API gateways (2.6) | Kong OSS, Tyk | Azure API Management, Apigee | Azure policy/identity integration and enterprise developer portals |
| Reverse ETL (2.7) | custom SQL + API scripts | Hightouch, Census | many SaaS destinations with maintained, monitored connectors |

### 3 Storage
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Cloud DW (3.1) | DuckDB (dev proxy) | Snowflake, BigQuery, Synapse/Fabric | org-scale concurrency, governance, zero-ops elasticity |
| Data lake / object storage (3.1/3.3) | MinIO | ADLS Gen2, S3 | durability SLAs, lifecycle tiers, integrated IAM/audit |
| Lakehouse (3.1/3.4) | Iceberg + Trino on MinIO | Databricks, Snowflake-Iceberg, Fabric OneLake | managed optimization, bundled catalog/governance, vendor support |
| Table-format catalogs (3.4) | Lakekeeper, Apache Polaris, Nessie | Unity Catalog, AWS Glue, Snowflake Open Catalog | credential vending + governance bundled into the licensed estate |
| OLTP relational (3.2) | PostgreSQL | Azure SQL, Oracle, SQL Server | vendor app certification, incumbent DBA estate, HA SLAs |
| NoSQL document/KV/wide-column (3.2) | MongoDB-compatible, Valkey, Cassandra | Cosmos DB, DynamoDB | multi-region guarantees with zero ops |
| Graph / knowledge graph (3.2) | Neo4j CE; Apache Jena/Fuseki | Neo4j Aura, Stardog, Ontotext GraphDB | reasoning at scale, enterprise security, support contracts |
| Time-series (3.2) | Prometheus, TimescaleDB, QuestDB | InfluxDB Cloud; kdb+ | kdb+ remains the tick-data desk standard; managed retention at scale |
| Search (3.2) | OpenSearch, Meilisearch | Elastic Cloud, Algolia | managed relevance + SIEM bundling |
| Vector (3.2) | pgvector, Qdrant | Azure AI Search, Pinecone | ACL-aware retrieval (security trimming) + integrated RAG platform |
| Caching (3.3) | Valkey, Memcached | Azure Cache for Redis, ElastiCache | managed failover + compliance posture |

### 4 Compute
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Batch engines (4.1) | Apache Spark | Databricks, Synapse/Fabric Spark, EMR | Photon-class performance, notebook+governance bundle, support |
| Serverless (4.1) | Functions Core Tools (local) | Azure Functions, AWS Lambda | spiky event-scale pay-per-use with managed triggers |
| Stream processing (4.2) | Apache Flink, Kafka Streams | Confluent Flink, AWS Managed Flink, Azure Stream Analytics | SQL-first teams; managed checkpoints/scaling/upgrades |
| Federated SQL (4.3) | Trino | Starburst, Athena | connector breadth, fine-grained security add-ons, support |
| Embedded OLAP (4.3) | DuckDB | MotherDuck, ClickHouse Cloud | shared state and concurrency beyond one node |
| Real-time analytics (4.3) | ClickHouse, Pinot, Druid | Imply, Tinybird | RT cluster ops complexity at scale |
| Streaming databases (4.3) | RisingWave, Proton | Materialize | managed incremental views with SLAs |
| Distributed frameworks (4.4) | Ray, Dask | Anyscale, Coiled | managed autoscaling GPU fleets |

### 5 Processing
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Visual ETL (5.1) | Apache NiFi | Informatica, Talend, SSIS, ADF data flows | installed base, citizen-ETL mandates, governance integration |
| ELT / transformation (5.2/5.3) | dbt Core, SQLMesh | dbt Cloud, Coalesce, Dataform | bundled scheduler/IDE/semantic layer; faster team onboarding |
| Wrangling (5.4) | pandas, Polars (+ ydata-profiling) | Alteryx, Tableau Prep, Glue DataBrew | analyst self-service mandates |
| Orchestration (5.6) | Airflow, Dagster | ADF, MWAA, Cloud Composer, Dagster+ | managed control plane; hybrid runtimes (self-hosted IR) |
| Durable execution (5.6) | Temporal OSS | Temporal Cloud, Azure Durable Functions, Step Functions | ops burden of self-hosted state clusters |
| BPM (5.6) | Camunda 7 CE, Flowable | Camunda 8 Enterprise, Pega, Appian | human-task UX, audit packs, vendor support for regulated workflows |

### 6 AI/ML
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Feature stores (6.1) | Feast | Databricks FS, Tecton, SageMaker FS | low-latency online serving with SLAs |
| Training & serving (6.2/6.3) | PyTorch, sklearn; vLLM, BentoML | Azure ML, SageMaker, Vertex; Azure OpenAI | managed GPU fleets, RBAC/compliance integration |
| MLOps / registry (6.4/6.7) | MLflow | Azure ML registry, W&B, Databricks | enterprise RBAC, lineage integration, hosted collaboration |
| Embeddings & RAG (6.6) | sentence-transformers + LlamaIndex + Ollama | Azure OpenAI + Azure AI Search, Bedrock KBs | model quality, security trimming, scale, support |
| LLMOps (6.8) | Langfuse + Ragas/DeepEval | LangSmith, Azure AI Foundry | enterprise SSO/compliance and integrated eval suites |

### 7 Semantic
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Semantic / metrics layer (7.1/7.2) | Cube, MetricFlow | Power BI semantic models, Looker/LookML, AtScale | BI-suite gravity — licensing and skills already in-house |
| Business glossary (7.3) | OpenMetadata glossary | Collibra, Purview, Alation | stewardship workflows + attestation auditors recognize |

### 8 Architecture
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Reference frameworks (8.1) | WAF/CAF docs, TOGAF (free w/ registration) | — (frameworks are free; consulting is the product) | — |
| Data modeling tools (8.2) | draw.io, DBeaver ERD, Mermaid | erwin, ER/Studio, SqlDBM, Hackolade | model repository/governance and forward-engineering at enterprise scale |
| Data Vault automation (8.2) | dbt + AutomateDV | VaultSpeed, WhereScape | generated loading code at estate scale with vendor accountability |
| Schema registries (8.3) | Apicurio | Confluent SR, Azure Schema Registry | bundled with the managed Kafka estate |
| EA / process modeling (8.5) | Archi, Structurizr Lite, bpmn.io | Sparx EA, BiZZdesign, Visual Paradigm | multi-user EA repository, TOGAF tooling, audit trails |

### 9 Engineering Practice
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Data versioning (9.2) | lakeFS, Nessie, Iceberg branches | Snowflake clones, Databricks | versioning must live inside the licensed warehouse |
| CI/CD (9.3) | GitHub Actions, GitLab CI | Azure DevOps | org standard + enterprise compliance gates |
| Data-aware CI (9.3) | dbt slim CI, SQLMesh | Datafold, dbt Cloud CI | column-level diffs at scale with support |
| Testing (9.4) | pytest, Testcontainers, k6 | enterprise QA suites | regulated test-evidence management |
| Schema migrations (9.7) | Flyway CE, Alembic | Liquibase Pro, Redgate | policy checks, governance dashboards, DBA workflows |
| Synthetic / test data (9.8) | Faker, SDV | Mostly AI, Tonic, Gretel, Delphix | vendor-attested privacy guarantees; TDM across a legacy estate |
| IaC (9.10) | OpenTofu, Pulumi | Terraform Enterprise; Bicep (Azure-only) | org-scale state/policy management (Sentinel); Azure-mandate shops |
| Documentation (9.6) | MkDocs, dbt docs | Confluence stack | org standard, permissions, non-engineer authoring |

### 10 Governance
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Catalogs / metadata (10.1) | OpenMetadata, DataHub | Microsoft Purview, Collibra, Alation | connector coverage of closed SaaS + stewardship workflows + audit attestation |
| Lineage (10.3) | OpenLineage + Marquez | Purview, Collibra, Manta | parsing lineage out of closed tools (Informatica, SSIS, vendor ETL) |
| Data quality (10.4) | Soda Core, Great Expectations, Elementary | Informatica DQ, Monte Carlo, Soda Cloud | ML anomaly coverage at estate scale + managed incident workflows |
| Profiling (10.4) | ydata-profiling, whylogs | Informatica/Collibra profiling | embedded in the governance suite the org already runs |
| MDM (10.5) | Splink + Postgres hub | Informatica MDM, Semarchy, Reltio, Tamr | stewardship UI, survivorship governance, vendor accountability to regulators |
| Reference data (10.6) | dbt seeds + governed schema | Collibra RDM, CluedIn | approval workflow + audit for code-list changes at org scale |
| Retention / lifecycle (10.7) | MinIO/ADLS lifecycle + Iceberg maintenance | Veritas, Commvault ILM | legal-hold workflows across hybrid legacy estates |
| Data observability (10.9) | Elementary + OpenLineage | Monte Carlo, Acceldata, Databand | rule-free anomaly coverage + on-call integration |

### 11 Security & Compliance
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Identity (11.1) | Keycloak | Microsoft Entra ID, Okta | managed SSO, conditional access, compliance certifications |
| Fine-grained access (11.1) | Postgres RLS, Trino rules, Apache Ranger, OPA | Immuta, Privacera, Unity Catalog, Lake Formation | policy UX for non-engineers + cross-engine enforcement + audit reports |
| Policy-as-code (11.1) | OPA, Cedar | Immuta, PlainID | business-user policy authoring |
| Encryption / KMS (11.2) | OpenBao | Azure Key Vault, AWS KMS | HSM backing + attestations auditors accept |
| Masking / tokenization (11.3) | Postgres functions + Presidio transforms | Delphix, Protegrity, warehouse-native DDM | format-preserving tokenization at estate scale with key governance |
| PII detection (11.4) | Microsoft Presidio | AWS Macie, GCP DLP, BigID, Purview classifiers | coverage of SaaS/closed stores + classification governance |
| Audit / SIEM (11.6) | pgAudit + Loki/Elastic OSS | Microsoft Sentinel, Splunk | SOC integration, correlation content, regulatory reporting |
| Secrets (11.8) | OpenBao, SOPS | Azure Key Vault, AWS Secrets Manager | managed HSM + rotation integrations |
| Compliance automation (11.7) | — (manual evidence binders) | Vanta, Drata, OneTrust | continuous evidence collection once audits become annual rituals |

### 12 Operations
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Backup & DR (12.1/12.2) | pgBackRest, MinIO versioning, Velero | Azure Backup + ASR, Veeam, Rubrik, Zerto | enterprise estates, ransomware vaulting, compliance reporting |
| FinOps (12.3) | OpenCost + calculator-based models | Azure Cost Management, Cloudability, Vantage | multi-cloud chargeback and commitment management |
| SLO management (12.4) | Grafana SLO + Prometheus | Nobl9, Datadog SLOs | SLO governance across dozens of teams |
| Incident management (12.5) | Grafana OnCall | PagerDuty, Opsgenie | enterprise escalation policies + ecosystem integrations |
| Observability (12.6/12.7) | OTel + Prometheus + Grafana + Loki + Tempo | Azure Monitor, Datadog, Dynatrace | single-vendor APM depth and ML insights at enterprise scale |

### 13 Data Products
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Data contracts (13.1) | ODCS + datacontract-cli + dbt contracts | Gable, Collibra contract features | producer-team UX and enterprise workflow integration |
| Mesh enablement (13.2) | Trino + OpenMetadata domains | Starburst, Databricks UC, Nextdata OS | federation governance and support at organization scale |
| Sharing (13.3) | delta-sharing reference server | Databricks Delta Sharing, Snowflake shares, Fabric sharing | recipient management, marketplace reach, egress engineering |
| Data APIs (13.4) | PostgREST/FastAPI + Kong | Azure APIM + managed backends | enterprise API governance and monetization features |

### 14 Consumption
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| BI (14.1) | Apache Superset, Metabase, Lightdash | Power BI (Azure default), Tableau, Looker | licensing gravity, self-service maturity, certified-content governance |
| Viz libraries (14.2) | Plotly, Vega-Lite, ECharts | Highcharts (commercial license) | embedding in commercial products with license/legal needs |
| Embedded analytics (14.3) | Cube embed, Superset embedding | Sigma, Looker Embed, Luzmo | multi-tenant security + vendor SLAs |
| Reporting (14.4) | JasperReports, BIRT | Power BI paginated; Workiva, AxiomSL, Wolters Kluwer (regulatory) | regulatory rule maintenance + filing connectivity outweigh build cost |
| Notebooks (14.5) | JupyterHub, Zeppelin | Hex, Deepnote, Databricks notebooks | collaboration + governance for mixed SQL/Python teams |
| Data apps (14.6) | Streamlit, Gradio, Dash | Power Apps, Retool | citizen-developer mandates + enterprise auth out of the box |
| Alerting & activation (14.7) | Grafana alerting | PagerDuty, Monte Carlo alerts, Hightouch | bundled with the observability/DQ/activation suite already licensed |
