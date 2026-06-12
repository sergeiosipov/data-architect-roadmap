<a id="appendix-b"></a>
## Appendix B — Reading Order

Consolidated book/course list with chapter→phase mapping. **Primary** = the one resource for its topic entries; **Alternate** = named substitute; **Parallel** = domain reading recommended alongside (commute-grade, drawn from the plan's slack, not the entry budget).

| # | Phase | Resource | What to read | Role |
|---|---|---|---|---|
| 1 | 1 | Kleppmann, *Designing Data-Intensive Applications* (latest ed.) | ch. 2–3 (models, storage), 5 (replication), 7 (transactions), 9 (consistency & consensus) | Primary (1.5.x, 1.6.x, 1.7.x, 1.8.9) |
| 2 | 1 | CMU 15-445 Database Systems (free course) — https://15445.courses.cs.cmu.edu/spring2025/schedule.html | ~14 lectures: storage, buffer pool, indexes, joins, optimization, MVCC, recovery | Primary (3.2.1) |
| 3 | 1 | Petrov, *Database Internals* | Part I | Alternate to #2 |
| 4 | 1 | Kimball & Ross, *The Data Warehouse Toolkit* 3rd ed. | ch. 1–4 + ch. 19 (financial services) | Primary (8.2.4) |
| 5 | 1 | Corr & Stagnitto, *Agile Data Warehouse Design* | BEAM workshop chapters | Alternate to #4 |
| 6 | 1 | DAMA-DMBOK (2nd/Revised ed.) | ch. 5 (modeling) | Primary (8.2.1–8.2.3) |
| 7 | 1 | MIT 6.5840 Distributed Systems (free) — https://pdos.csail.mit.edu/6.824/schedule.html | lectures 4, 6–9, 13 (+ 20–21 for A.2); Raft paper | Primary (A.1, A.2) |
| 8 | 2 | Cyr & Dorsey, *Analytics Engineering with SQL and dbt* | full | Primary (5.2.1/5.3.1) |
| 9 | 2 | Linstedt & Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0* | ch. 1–7 (modeling), 11–12 (loading) | Primary (8.2.5) |
| 10 | 2 | Inmon et al., *Building the Data Lakehouse* | skim, warehouse-veteran perspective | Primary (3.1.4, paired with the CIDR Lakehouse paper) |
| 11 | 2 | *Apache Iceberg: The Definitive Guide* (free via Dremio) | format + maintenance chapters | Alternate (3.4.2) |
| 12 | 2 | *Trino: The Definitive Guide* (free via Starburst) | core + Iceberg connector chapters | Alternate (4.3.1) |
| 13 | 2 | Pozen & Hamacher, *The Fund Industry* | full | Parallel (domain grounding) |
| 14 | 2 | Fowler & David, *The Informed Company* | maturity-stages chapters | Optional (3.1.x context) |
| 15 | 3 | Damji et al., *Learning Spark* 2nd ed. (free PDF, Databricks) | ch. 1–7 + 12 (tuning) | Primary (4.1.1) |
| 16 | 3 | Harenslak & de Ruiter, *Data Pipelines with Apache Airflow* 2nd ed. | ch. 1–6, 12 | Primary (5.6.1, with Dagster docs) |
| 17 | 3 | Forsgren et al., *Accelerate* | part I | Optional (9.3.x culture; DORA-metrics vocabulary) |
| 18 | 4 | Shapira et al., *Kafka: The Definitive Guide* 2nd ed. (free PDF, Confluent) | ch. 1–8 + 10 | Primary (2.4.1, 1.8.2) |
| 19 | 4 | Akidau et al., *Streaming Systems* | ch. 1–4 (+ ch. 7 skim) | Primary (1.9.x) |
| 20 | 4 | Stopford, *Designing Event-Driven Systems* (free PDF, Confluent) | event sourcing/CQRS + Kafka-patterns chapters | Primary (1.8.5/1.8.6) |
| 21 | 4 | Weiss, *After the Trade Is Made* 3rd ed. | settlement/custody chapters | Parallel (domain grounding for streams you model) |
| 22 | 4 | Simmons, *Securities Operations* | trade lifecycle + corporate actions chapters | Alternate to #21 |
| 23 | 5 | Brikman, *Terraform: Up & Running* 3rd ed. | concept chapters (state, modules, testing) | Primary (9.10.1, with OpenTofu docs) |
| 24 | 5 | Dotson, *Practical Cloud Security* 2nd ed. | IAM + network + encryption chapters | Optional (bridges P5→P6 security) |
| 25 | 5 | Google SRE Book / Workbook (free online) | postmortem, capacity, SLO chapters | Primary (12.4.1 in P8; T3 reads in P5) |
| 26 | 6 | Moses et al., *Data Quality Fundamentals* | ch. 1–4 + observability chapters | Primary (9.4.2/10.4.1, 10.9.x) |
| 27 | 6 | DAMA-DMBOK (Revised ed.) | ch. 10 (R&MD), 13 (metadata), 15 (maturity); ch. 1, 2, 9, 17 for A.14/17/19/20 | Primary (10.5.1, 10.6.1; A items) |
| 28 | 6 | Bhajaria, *Data Privacy: A Runbook for Engineers* | PII handling + consent chapters | Alternate (11.3.x–11.5.x) |
| 29 | 6 | Seiner, *Non-Invasive Data Governance* | operating-model chapters | Optional (A.14 counterweight — low-friction governance) |
| 30 | 6 | Loader, *Fund Custody and Administration* | NAV calc + transfer agency chapters | Parallel (domain grounding for MDM/reporting) |
| 31 | 7 | Huyen, *Designing Machine Learning Systems* | ch. 1–2, 7–9 | Primary (6.4.1) |
| 32 | 7 | Bouchard & Peters, *Building LLMs for Production* | RAG + evaluation chapters | Alternate (6.6.2/6.8.2) |
| 33 | 7 | Burkov, *Machine Learning Engineering* | lifecycle chapters | Optional (compact 6.4.x refresher) |
| 34 | 8 | Khononov, *Learning Domain-Driven Design* | ch. 1–11 (strategic) | Primary (8.4.1) |
| 35 | 8 | Jones, *Driving Data Quality with Data Contracts* | full | Primary (13.1.1) |
| 36 | 8 | Dehghani, *Data Mesh* | parts I–II (skim III) | Primary (1.4.4) |
| 37 | 8 | Strengholt, *Data Management at Scale* 2nd ed. | architecture-survey + federated-governance chapters | Primary counterweight to #36 (also 1.4.6 T3 read in P2) |
| 38 | 8 | Ford et al., *Software Architecture: The Hard Parts* | parts I–II | Primary (A.7) |
| 39 | 8 | Ford et al., *Building Evolutionary Architectures* 2nd ed. | fitness-functions chapters | Optional (evolution lens on your ADR/exit-criteria practice) |
| 40 | 8 | TOGAF 10 Fundamental Content + ArchiMate 3.2 spec (free, Open Group registration) | Core Concepts + ADM; ArchiMate ch. on layers + ch. 12 | Primary (8.1.3, A.8–A.11) |
| 41 | 8 | Knaflic, *Storytelling with Data* | ch. 1–2 | T3 read (14.2.1) |

Course-shaped extras already embedded in entries: Microsoft Learn paths (AZ-700 → A.3, Fabric → A.4, KQL → A.5, Bicep → 9.10.2), DataTalksClub DE Zoomcamp as a free hands-on pattern library (Phases 2–5, GCP-centric — substitute Azure equivalents), *The Internals of PostgreSQL* (free, A.22), MIT *Missing Semester* (unscheduled refresher).
