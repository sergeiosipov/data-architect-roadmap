<a id="appendix-c"></a>
## Appendix C — Coverage Matrix

All 252 taxonomy subcategory IDs, each exactly once. IDs follow the canonical parse:
subcategory = bold bullet item; concept categories 1.8/1.9 per concept; 1.10 as one
unit; 1.11 as 3 groups; 1.12 per standard; the taxonomy's own cross-reference pointers
(5.5, 6.5, 10.8) carry IDs and are resolved in [Excluded](#excluded). Gap additions
A.1–A.31 are tracked in [Appendix A](#appendix-a). Tier `—` = excluded item. Phase 0
items are taught from zero and individually skippable via the Skip List tests.

| Taxonomy ID | Topic | Tier | Phase |
|---|---|---|---|
| 1.1.1 | Structured data | T3 | Phase 0 |
| 1.1.2 | Semi-structured data | T3 | Phase 0 |
| 1.1.3 | Unstructured data | T3 | Phase 0 |
| 1.1.4 | Vector / embeddings | T2 | Phase 7 |
| 1.2.1 | Batch paradigm | T3 | Phase 0 |
| 1.2.2 | Micro-batch | T2 | Phase 4 |
| 1.2.3 | Streaming paradigm | T2 | Phase 4 |
| 1.2.4 | Real-time / low-latency | T3 | Phase 4 |
| 1.3.1 | OLTP | T2 | Phase 0 |
| 1.3.2 | OLAP | T2 | Phase 0 |
| 1.3.3 | HTAP | T3 | Phase 1 |
| 1.3.4 | RT / user-facing analytics | T3 | Phase 4 |
| 1.4.1 | Lambda architecture | T2 | Phase 4 |
| 1.4.2 | Kappa architecture | T2 | Phase 4 |
| 1.4.3 | Medallion | T1 | Phase 2 |
| 1.4.4 | Data Mesh | T2 | Phase 8 |
| 1.4.5 | Data Fabric | T3 | Phase 8 |
| 1.4.6 | Hub-and-Spoke | T3 | Phase 2 |
| 1.4.7 | Data Vault (pattern) | T2 | Phase 2 |
| 1.5.1 | Row vs columnar | T2 | Phase 1 |
| 1.5.2 | MPP | T2 | Phase 1 |
| 1.5.3 | Shared-nothing vs shared-disk | T2 | Phase 1 |
| 1.5.4 | Storage/compute separation | T2 | Phase 1 |
| 1.6.1 | ACID & isolation levels | T1 | Phase 1 |
| 1.6.2 | BASE | T3 | Phase 1 |
| 1.6.3 | Eventual consistency | T2 | Phase 1 |
| 1.6.4 | Strong consistency | T2 | Phase 1 |
| 1.6.5 | RYW / monotonic / causal | T2 | Phase 1 |
| 1.7.1 | CAP | T1 | Phase 1 |
| 1.7.2 | PACELC | T1 | Phase 1 |
| 1.8.1 | Idempotency | T1 | Phase 1 |
| 1.8.2 | Delivery semantics | T1 | Phase 4 |
| 1.8.3 | Outbox pattern | T1 | Phase 4 |
| 1.8.4 | Saga pattern | T1 | Phase 4 |
| 1.8.5 | Event sourcing | T1 | Phase 4 |
| 1.8.6 | CQRS | T2 | Phase 4 |
| 1.8.7 | Dead-letter queue | T2 | Phase 4 |
| 1.8.8 | Backpressure | T2 | Phase 4 |
| 1.8.9 | Two-phase commit | T2 | Phase 1 |
| 1.8.10 | CDC (pattern) | T1 | Phase 4 |
| 1.8.11 | Strangler fig | T2 | Phase 8 |
| 1.8.12 | Bulkhead | T3 | Phase 4 |
| 1.8.13 | Circuit breaker | T3 | Phase 4 |
| 1.9.1 | Watermarks | T1 | Phase 4 |
| 1.9.2 | Windowing | T1 | Phase 4 |
| 1.9.3 | Late data handling | T2 | Phase 4 |
| 1.9.4 | Event vs processing time | T1 | Phase 4 |
| 1.9.5 | Triggers | T2 | Phase 4 |
| 1.9.6 | Stateful vs stateless | T2 | Phase 4 |
| 1.9.7 | Schema evolution compatibility | T1 | Phase 4 |
| 1.10.1 | Modeling notations (overview) | T2 | Phase 1 |
| 1.11.1 | Data protocols (HTTP…ADBC) | T2 | Phase 4 |
| 1.11.2 | Serialization formats | T2 | Phase 4 |
| 1.11.3 | Async API standards | T2 | Phase 4 |
| 1.12.1 | ISO 20022 | T1 | Phase 2 |
| 1.12.2 | LEI (ISO 17442) | T2 | Phase 2 |
| 1.12.3 | ISIN | T2 | Phase 2 |
| 1.12.4 | CFI | T3 | Phase 2 |
| 1.12.5 | FIGI | T3 | Phase 2 |
| 1.12.6 | FIBO | T2 | Phase 6 |
| 1.12.7 | EMT/EPT (FinDatEx) | T1 | Phase 2 |
| 1.12.8 | SWIFT MT/MX | T2 | Phase 2 |
| 1.12.9 | FpML | T3 | Phase 2 |
| 1.12.10 | FIX | T3 | Phase 2 |
| 1.12.11 | IBAN / SEPA | T3 | Phase 2 |
| 1.12.12 | DCAM | T1 | Phase 6 |
| 2.1.1 | ELT connectors | T2 | Phase 2 |
| 2.1.2 | Bulk load utilities | T2 | Phase 5 |
| 2.2.1 | Log/metric shippers | T3 | Phase 5 |
| 2.2.2 | Stream connectors | T2 | Phase 4 |
| 2.3.1 | Log-based CDC | T1 | Phase 4 |
| 2.3.2 | Trigger-based CDC | T3 | Phase 4 |
| 2.3.3 | Snapshot-based CDC | T3 | Phase 4 |
| 2.4.1 | Distributed logs (Kafka) | T1 | Phase 4 |
| 2.4.2 | Message brokers | T2 | Phase 4 |
| 2.4.3 | Event mesh | T3 | Phase 4 |
| 2.5.1 | iPaaS | T3 | Phase 5 |
| 2.5.2 | ESB (legacy) | T3 | Phase 5 |
| 2.6.1 | API gateways | T2 | Phase 8 |
| 2.6.2 | GraphQL layers | T3 | Phase 8 |
| 2.7.1 | Reverse ETL | T3 | Phase 8 |
| 3.1.1 | Cloud data warehouse | T2 | Phase 2 |
| 3.1.2 | On-prem MPP warehouse | T3 | Phase 2 |
| 3.1.3 | Data lake | T2 | Phase 2 |
| 3.1.4 | Data lakehouse | T1 | Phase 2 |
| 3.2.1 | OLTP / relational internals | T1 | Phase 1 |
| 3.2.2 | NoSQL document | T3 | Phase 1 |
| 3.2.3 | NoSQL key-value | T3 | Phase 1 |
| 3.2.4 | NoSQL wide-column | T3 | Phase 1 |
| 3.2.5 | Property graph | T3 | Phase 6 |
| 3.2.6 | Knowledge graph / RDF | T2 | Phase 6 |
| 3.2.7 | Time-series | T3 | Phase 5 |
| 3.2.8 | Search | T3 | Phase 7 |
| 3.2.9 | Vector storage | T2 | Phase 7 |
| 3.2.10 | HTAP stores | T3 | Phase 1 |
| 3.2.11 | Geospatial | T3 | Phase 2 |
| 3.3.1 | Object storage | T2 | Phase 2 |
| 3.3.2 | Block storage | T3 | Phase 5 |
| 3.3.3 | File storage | T3 | Phase 5 |
| 3.3.4 | Caching | T2 | Phase 5 |
| 3.4.1 | File formats | T1 | Phase 2 |
| 3.4.2 | Table formats | T1 | Phase 2 |
| 3.4.3 | Table-format catalogs | T2 | Phase 2 |
| 4.1.1 | Distributed batch engines | T1 | Phase 3 |
| 4.1.2 | Serverless compute | T2 | Phase 5 |
| 4.2.1 | Stateful stream processing | T1 | Phase 4 |
| 4.2.2 | Cloud-native streaming | T2 | Phase 5 |
| 4.3.1 | MPP SQL engines | T2 | Phase 2 |
| 4.3.2 | Cloud query services | T2 | Phase 5 |
| 4.3.3 | Embedded / single-node | T2 | Phase 2 |
| 4.3.4 | RT/user-facing analytics engines | T3 | Phase 4 |
| 4.3.5 | Streaming databases | T3 | Phase 4 |
| 4.4.1 | General distributed frameworks | T3 | Phase 3 |
| 4.4.2 | Specialized frameworks | T3 | Phase 3 |
| 5.1.1 | Visual ETL | T3 | Phase 5 |
| 5.1.2 | Code-first ETL | T3 | Phase 3 |
| 5.2.1 | In-warehouse SQL ELT (dbt) | T1 | Phase 2 |
| 5.2.2 | ELT orchestrated | T2 | Phase 2 |
| 5.3.1 | SQL transformation layer | T1 | Phase 2 |
| 5.3.2 | Code transformation (DataFrames) | T2 | Phase 3 |
| 5.3.3 | Alternative query languages | T3 | Phase 2 |
| 5.4.1 | Interactive prep | T3 | Phase 2 |
| 5.4.2 | Code-first wrangling | T2 | Phase 0 |
| 5.5.1 | Reverse ETL (pointer) | — | Excluded |
| 5.6.1 | Workflow orchestrators | T1 | Phase 3 |
| 5.6.2 | Cloud-native orchestration | T2 | Phase 5 |
| 5.6.3 | Data-aware orchestration | T2 | Phase 3 |
| 5.6.4 | Durable execution | T2 | Phase 4 |
| 5.6.5 | BPM / process orchestration | T2 | Phase 4 |
| 6.1.1 | OS feature stores | T2 | Phase 7 |
| 6.1.2 | Managed feature stores | T3 | Phase 7 |
| 6.2.1 | Training frameworks | T3 | Phase 7 |
| 6.2.2 | Distributed training | T3 | Phase 7 |
| 6.2.3 | Managed training | T3 | Phase 7 |
| 6.3.1 | OS model serving | T3 | Phase 7 |
| 6.3.2 | Managed endpoints | T3 | Phase 7 |
| 6.4.1 | E2E MLOps platforms | T2 | Phase 7 |
| 6.4.2 | Managed MLOps | T2 | Phase 7 |
| 6.5.1 | Vector DBs (pointer) | — | Excluded |
| 6.6.1 | Embedding models | T2 | Phase 7 |
| 6.6.2 | RAG frameworks | T2 | Phase 7 |
| 6.6.3 | RAG platforms | T2 | Phase 7 |
| 6.7.1 | OS experiment tracking | T3 | Phase 7 |
| 6.7.2 | Managed tracking | T3 | Phase 7 |
| 6.8.1 | Prompt mgmt & tracing | T2 | Phase 7 |
| 6.8.2 | LLM evaluation | T2 | Phase 7 |
| 7.1.1 | OS semantic layer | T2 | Phase 8 |
| 7.1.2 | Platform semantic layers | T2 | Phase 8 |
| 7.2.1 | Metrics layer | T2 | Phase 8 |
| 7.3.1 | Business glossary | T2 | Phase 6 |
| 7.3.2 | Glossary in catalogs | T3 | Phase 6 |
| 8.1.1 | Cloud provider reference arch | T1 | Phase 5 |
| 8.1.2 | Vendor reference arch | T2 | Phase 5 |
| 8.1.3 | Industry reference (TOGAF/DMBOK) | T2 | Phase 8 |
| 8.2.1 | Conceptual modeling | T1 | Phase 1 |
| 8.2.2 | Logical modeling | T1 | Phase 1 |
| 8.2.3 | Physical modeling | T1 | Phase 1 |
| 8.2.4 | Dimensional modeling | T1 | Phase 1 |
| 8.2.5 | Data Vault modeling | T1 | Phase 2 |
| 8.2.6 | Anchor / 6NF | T3 | Phase 2 |
| 8.3.1 | Schema registries | T2 | Phase 4 |
| 8.3.2 | Schema languages | T2 | Phase 4 |
| 8.4.1 | Domain-driven design | T1 | Phase 8 |
| 8.5.1 | Architecture notations & tools | T1 | Phase 1 |
| 9.1.1 | IDEs | T3 | Phase 0 |
| 9.1.2 | Notebooks | T3 | Phase 0 |
| 9.1.3 | Local data sandboxes | T2 | Phase 1 |
| 9.2.1 | Git & hosting | T2 | Phase 0 |
| 9.2.2 | Data versioning | T2 | Phase 3 |
| 9.3.1 | CI/CD pipelines | T2 | Phase 3 |
| 9.3.2 | Data-specific CI | T2 | Phase 3 |
| 9.4.1 | Unit testing | T2 | Phase 0 |
| 9.4.2 | Data quality testing | T1 | Phase 6 |
| 9.4.3 | Integration testing | T2 | Phase 3 |
| 9.4.4 | Load/perf testing | T3 | Phase 3 |
| 9.5.1 | Code review | T3 | Phase 0 |
| 9.5.2 | Data diff | T3 | Phase 3 |
| 9.6.1 | Code docs | T3 | Phase 3 |
| 9.6.2 | Data docs | T2 | Phase 2 |
| 9.7.1 | Schema migrations | T2 | Phase 3 |
| 9.8.1 | Synthetic data | T2 | Phase 6 |
| 9.8.2 | Test data management | T3 | Phase 6 |
| 9.9.1 | Notebooks in production | T3 | Phase 3 |
| 9.10.1 | Cloud-agnostic IaC | T1 | Phase 5 |
| 9.10.2 | Cloud-native IaC | T2 | Phase 5 |
| 9.10.3 | Configuration management | T3 | Phase 5 |
| 10.1.1 | Active metadata platforms | T1 | Phase 6 |
| 10.1.2 | Enterprise catalogs | T2 | Phase 6 |
| 10.2.1 | AI-native discovery | T3 | Phase 6 |
| 10.2.2 | Catalog-embedded discovery | T3 | Phase 6 |
| 10.3.1 | Lineage (standards) | T1 | Phase 6 |
| 10.3.2 | Lineage in catalogs | T3 | Phase 6 |
| 10.4.1 | OS data quality | T1 | Phase 6 |
| 10.4.2 | Managed/enterprise DQ | T2 | Phase 6 |
| 10.4.3 | Data profiling | T2 | Phase 6 |
| 10.5.1 | Master data management | T1 | Phase 6 |
| 10.5.2 | Modern / cloud MDM | T3 | Phase 6 |
| 10.6.1 | Reference data management | T2 | Phase 6 |
| 10.6.2 | RDM inside MDM | T3 | Phase 6 |
| 10.7.1 | Lifecycle / retention (cloud) | T2 | Phase 6 |
| 10.7.2 | Enterprise ILM | T3 | Phase 6 |
| 10.8.1 | Audit & compliance (pointer) | — | Excluded |
| 10.9.1 | Pipeline observability | T2 | Phase 6 |
| 10.9.2 | OS data observability | T2 | Phase 6 |
| 11.1.1 | Identity providers | T2 | Phase 6 |
| 11.1.2 | Fine-grained access control | T1 | Phase 6 |
| 11.1.3 | Policy-as-code | T2 | Phase 6 |
| 11.2.1 | Key management | T2 | Phase 6 |
| 11.2.2 | Database encryption / TDE | T3 | Phase 6 |
| 11.3.1 | Masking / tokenization | T2 | Phase 6 |
| 11.3.2 | Built-in DB masking | T2 | Phase 6 |
| 11.4.1 | PII detection & redaction | T2 | Phase 6 |
| 11.5.1 | Privacy / consent mgmt | T3 | Phase 6 |
| 11.6.1 | Audit logging / SIEM | T2 | Phase 6 |
| 11.7.1 | Regulatory compliance frameworks | T1 | Phase 6 |
| 11.8.1 | Secrets management | T2 | Phase 5 |
| 12.1.1 | Cloud-native backup | T2 | Phase 5 |
| 12.1.2 | Enterprise backup | T3 | Phase 5 |
| 12.2.1 | DR tooling | T3 | Phase 5 |
| 12.2.2 | DR patterns | T1 | Phase 5 |
| 12.3.1 | FinOps / cost mgmt | T1 | Phase 5 |
| 12.3.2 | Data-specific FinOps | T2 | Phase 5 |
| 12.4.1 | SLA/SLO management | T2 | Phase 8 |
| 12.5.1 | On-call / paging | T3 | Phase 5 |
| 12.5.2 | Postmortems | T3 | Phase 5 |
| 12.6.1 | Capacity planning | T3 | Phase 5 |
| 12.7.1 | Commercial APM | T3 | Phase 5 |
| 12.7.2 | OS observability stack | T2 | Phase 5 |
| 13.1.1 | Data contracts (tools) | T1 | Phase 8 |
| 13.1.2 | Data contract standards | T2 | Phase 8 |
| 13.2.1 | Mesh enabling platforms | T2 | Phase 8 |
| 13.3.1 | Internal marketplaces | T3 | Phase 8 |
| 13.3.2 | Cross-org sharing | T2 | Phase 8 |
| 13.3.3 | Commercial data marketplaces | T3 | Phase 8 |
| 13.4.1 | GraphQL data APIs | T3 | Phase 8 |
| 13.4.2 | REST data APIs | T2 | Phase 8 |
| 13.5.1 | Standalone CDPs | — | Excluded |
| 13.5.2 | Composable CDPs | — | Excluded |
| 14.1.1 | Modern cloud BI | T2 | Phase 8 |
| 14.1.2 | On-prem / legacy BI | T3 | Phase 8 |
| 14.1.3 | Open-source BI | T2 | Phase 8 |
| 14.2.1 | Viz libraries | T3 | Phase 8 |
| 14.3.1 | Embedded analytics | T3 | Phase 8 |
| 14.4.1 | Operational reporting | T3 | Phase 8 |
| 14.4.2 | Regulatory reporting | T1 | Phase 8 |
| 14.5.1 | Cloud notebooks | T3 | Phase 8 |
| 14.5.2 | Self-hosted notebooks | T3 | Phase 0 |
| 14.6.1 | Data app frameworks | T2 | Phase 8 |
| 14.6.2 | Internal tool builders | T3 | Phase 8 |
| 14.7.1 | Anomaly alerting | T3 | Phase 6 |
| 14.7.2 | Reverse-ETL activation | T3 | Phase 8 |
| 14.7.3 | Notification tools | T3 | Phase 5 |

**Coverage: 252/252 IDs.** Excluded: 5 · Phase 0: 13 · Phase 1: 26 · Phase 2: 33 · Phase 3: 16 · Phase 4: 40 · Phase 5: 31 · Phase 6: 38 · Phase 7: 19 · Phase 8: 31.
