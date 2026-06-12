<a id="appendix-a"></a>
## Appendix A — Gap Additions

Topics that the INPUT-2 cross-check sources treat as significant but that are absent from the taxonomy. Each is scheduled into a phase and counted in the budget (`A.x` IDs). All nine source groups were verified by live web cross-check (June 2026), marked ✓. A.27–A.31 were added on the learner's instruction to assume **zero prior knowledge** — their sources are the verified roadmaps that treat them as foundational.

### Foundations (scheduled in Phase 0; each skippable via its Skip List test)

| ID | Topic | Source | Tier | Phase | Primary resource | Est. h |
|---|---|---|---|---|---|---|
| A.27 | Linux, the command line & shell scripting — the substrate beneath Docker, Kubernetes, CI, cloud shells, and log forensics | roadmap.sh postgresql-dba + devops ✓ | T2 | 0 | MIT *The Missing Semester* (free) — https://missing.csail.mit.edu/ | 12 |
| A.28 | Python from zero — control flow, functions, files, environments (uv-first), debugging, a first CLI | roadmap.sh data-engineer ✓ | T2 | 0 | *Python for Everybody* (py4e, free full course); alt: *Automate the Boring Stuff* (free online) | 36 |
| A.29 | SQL from zero — joins, aggregation, NULL semantics, CTEs, window functions | roadmap.sh data-engineer ✓ | T2 | 0 | SQLBolt + PgExercises (free, browser-based) | 26 |
| A.30 | Docker & containers from zero — images, Dockerfiles, Compose, volumes, debugging | roadmap.sh devops ✓ | T2 | 0 | Docker official "Get Started" guide | 8 |
| A.31 | Networking & how the web works — IP/TCP, DNS, HTTP, TLS, proxies/firewalls at literacy level | roadmap.sh devops + system-design ✓ | T2 | 0 | MDN "How the web works" + Cloudflare Learning Center (DNS, TLS) | 8 |

### Platform & cloud (scheduled in Phases 1 and 5)

| ID | Topic | Source | Tier | Phase | Primary resource | Est. h |
|---|---|---|---|---|---|---|
| A.1 | Distributed consensus & replication protocols (Raft/Paxos, quorum replication, coordination services) — the layer beneath the taxonomy's consistency/CAP/2PC coverage; what HA/RPO claims of Kafka, Cosmos DB, zone-redundant Azure services rest on | MIT 6.5840 ✓ | T2 | 1 | MIT 6.5840 lectures 4, 6–9, 13 + the extended Raft paper — https://pdos.csail.mit.edu/6.824/schedule.html | 5 |
| A.2 | Byzantine fault tolerance & DLT fundamentals — trust models behind tokenized fund shares, which Luxembourg is actively piloting | MIT 6.5840 ✓ | T3 | 1 | MIT 6.5840 lectures 20–21 (Bitcoin, PBFT) | 1.5 |
| A.3 | Cloud networking & private connectivity (VNets, Private Link, ExpressRoute, NSG/Azure Firewall, private DNS, L4/L7 load balancing) — fund-industry Azure estates are network-isolated by policy; every integration design crosses this layer | roadmap.sh software-architect + system-design ✓ | T2 | 5 | Microsoft Learn AZ-700 path (free) — https://learn.microsoft.com/en-us/training/paths/design-implement-microsoft-azure-networking-solutions-az-700/ | 6 |
| A.4 | Microsoft Fabric / OneLake platform architecture (capacities, domains, shortcuts, Direct Lake, deployment pipelines) — Microsoft's strategic successor to Synapse; the default evaluation target for an Azure-primary architect | DP-700/DP-600 ✓ | T2 | 5 | Microsoft Learn "Get started with Microsoft Fabric" path (free) — https://learn.microsoft.com/en-us/training/paths/get-started-fabric/ | 5 |
| A.5 | KQL & the Kusto engine stack (Eventhouse / Azure Data Explorer / Azure Monitor logs) — pervasive in Azure observability, Sentinel SIEM, and audit-evidence queries; absent from the taxonomy | DP-700/DP-600 ✓ | T2 | 5 | Microsoft Learn "Write your first query with KQL" + KQL path (free) — https://learn.microsoft.com/en-us/training/modules/write-first-query-kusto-query-language/ | 4 |
| A.6 | Kubernetes & container orchestration (pods/services/ingress, Helm, operators, AKS; GitOps with Argo CD; service mesh at awareness) — named weak spot, substrate for Spark/Flink/Airflow executors and every CNCF tool in this plan; the taxonomy assumes it silently | roadmap.sh devops ✓ (GitOps/service-mesh nodes subsumed here) | T2 | 5 | Official Kubernetes tutorials + a local kind/k3d cluster; "Kubernetes: Up & Running" as alternate | 12 |
| A.22 | Relational database administration & HA depth (streaming/logical replication topologies, Patroni-style failover, connection pooling, PITR, vacuum/WAL operations) — complements the internals entry 3.2.1: how the engines behind TA/fund-accounting systems behave under load and failover | roadmap.sh postgresql-dba ✓ | T2 | 5 | *The Internals of PostgreSQL* (Suzuki, free) — https://www.interdb.jp/pg/ — replication/WAL/vacuum chapters | 4 |
| A.25 | Warehouse performance engineering (query-profile analysis, compute sizing, clustering keys & micro-partition pruning, search optimization, materialized views) — a full scored domain in both architect exams; the cost/deadline lever for regulatory reporting windows | SnowPro Adv Architect + AWS SAP-C02 ✓ | T2 | 5 | Snowflake "Exploring and optimizing performance" guide (concepts transfer to any MPP warehouse) — https://docs.snowflake.com/en/guides-overview-performance | 4 |
| A.26 | Resilience testing & chaos engineering (failure injection, game days, DR exercises) — DORA mandates operational-resilience *testing*, not just planning; the hands-on complement to A.15 | AWS SAP-C02 ✓ | T3 | 5 | Principles of Chaos Engineering — https://principlesofchaos.org/ + Azure Chaos Studio docs | 2 |

### Architecture practice (scheduled in Phase 8)

| ID | Topic | Source | Tier | Phase | Primary resource | Est. h |
|---|---|---|---|---|---|---|
| A.7 | Architecture styles & trade-off analysis as a discipline (layered/SOA/microservices/event-driven; quantifying trade-offs; presenting and defending decisions) | roadmap.sh software-architect ✓ | T2 | 8 | *Software Architecture: The Hard Parts* (Ford et al.) pt. I–II + Software Architecture Monday lessons — https://www.developertoarchitect.com/lessons/ | 4 |
| A.8 | Business architecture: capability maps, value streams, information mapping — how an architect scopes data domains/products (NAV, TA, regulatory reporting) and ties investment to business outcomes | TOGAF 10 Series Guides ✓ | T2 | 8 | TOGAF Series Guides: Business Capabilities; Value Streams; Information Mapping (free with Open Group registration) — https://www.opengroup.org/togaf/series-guides | 4 |
| A.9 | EA governance & the architecture operating model (architecture boards, architecture contracts, compliance reviews, maturity, roles) — the process through which designs get approved and funded in CSSF-regulated entities | TOGAF 10 ✓ | T2 | 8 | TOGAF 10 Fundamental Content: "EA Capability and Governance" (free with registration) | 3 |
| A.10 | Architecture roadmapping & migration planning (transition architectures, plateaus/gaps, work packages) — how multi-year platform modernizations are sold and steered | TOGAF ADM E–F + ArchiMate 3.2 ch. 12 ✓ | T2 | 8 | ArchiMate 3.2 spec ch. 12 + TOGAF ADM Phases E–F (free with registration) | 3 |
| A.11 | Agile EA practice (intentional vs emergent architecture; architecture runway in sprint-based delivery) | TOGAF Series Guides ✓ | T3 | 8 | TOGAF Series Guide: Enabling Enterprise Agility (free with registration) | 1 |
| A.12 | API/application security basics (OWASP API Top 10: BOLA, injection; PKI/hashing literacy) — data products exposing regulated fund data must survive AppSec review | roadmap.sh software-architect ✓ | T3 | 8 | OWASP API Security Top 10 (2023) — https://owasp.org/API-Security/ | 2 |
| A.13 | ITSM & delivery frameworks (ITIL change/incident/release; SAFe awareness) — change advisory boards are how platform changes ship in Luxembourg institutions, reinforced by DORA | roadmap.sh software-architect ✓ | T3 | 8 | Atlassian ITIL 4 primer — https://www.atlassian.com/itsm/itil | 1.5 |

### Governance, risk & organizational practice (scheduled in Phase 6)

| ID | Topic | Source | Tier | Phase | Primary resource | Est. h |
|---|---|---|---|---|---|---|
| A.14 | Data strategy, business case, funding & target operating model (DCAM components 1–4: roles, RACI, stewardship org) — half of DCAM is program-building, not technology | EDM Council DCAM v3 ✓ | T2 | 6 | DCAM v3 overview — https://edmcouncil.org/frameworks/dcam/ + DAMA-DMBOK ch. 1 | 4 |
| A.15 | Architecture-level risk management (TOGAF risk technique, Open FAIR flavor; DORA ICT-risk framing) — designs must be justified in risk language to second-line functions | TOGAF 10 ✓ | T2 | 6 | TOGAF Series Guide: Integrating Risk and Security (free with registration) | 3 |
| A.16 | Data risk & control environment (control inventories, three lines of defense, evidence/attestation; CDMC 14 Key Controls) | DCAM/CDMC ✓ | T3 | 6 | CDMC 14 Key Controls & Automations (free request) — https://edmcouncil.org/frameworks/cdmc/14-key-controls/ | 2 |
| A.17 | Data handling ethics (bias, responsible use; GDPR fairness, EU AI Act expectations) | DAMA-DMBOK2 ch. 2 ✓ | T3 | 6 | DAMA-DMBOK2 Revised, ch. 2 | 1 |
| A.18 | Purpose-based consumption & data sharing agreements (CDMC "Data Consumption Purpose" control) — distributor/TA data sharing needs documented purpose beyond GDPR consent | CDMC ✓ | T3 | 6 | CDMC v1.1, Data Accessibility & Usage component (free download) — https://edmcouncil.org/frameworks/cdmc/ | 1 |
| A.19 | Records & content management as a discipline (retention of prospectuses/KIDs/board minutes under CSSF & MiFID rules; e-discovery) | DAMA-DMBOK2 ch. 9 ✓ | T3 | 6 | DAMA-DMBOK2 Revised, ch. 9 | 1.5 |
| A.20 | Organizational change management for data initiatives (adoption of catalogs/governance; Kotter-style change practice) | DAMA-DMBOK2 ch. 17 ✓ | T3 | 6 | DAMA-DMBOK2 Revised, ch. 17 | 1.5 |

### AI/ML (scheduled in Phase 7)

| ID | Topic | Source | Tier | Phase | Primary resource | Est. h |
|---|---|---|---|---|---|---|
| A.21 | LLM agent patterns & prompt/context-engineering fundamentals (tool use, structured output, ReAct-style agentic workflows, context management) — the taxonomy covers RAG and LLMOps but not agent design, which document-processing platforms increasingly use | roadmap.sh ai-engineer ✓ | T3 | 7 | Anthropic "Building Effective Agents" engineering guide + provider prompt-engineering docs | 2 |
| A.23 | Model Context Protocol (MCP) — the emerging open standard for connecting AI agents to data platforms; Databricks/Snowflake/Microsoft are shipping MCP servers, and "expose governed fund data to AI assistants" will be asked of this architect | roadmap.sh ai-engineer ✓ (dedicated top-level topic) | T2 | 7 | Official MCP documentation (architecture + build-a-server tutorial) — https://modelcontextprotocol.io | 3 |
| A.24 | LLM application security & guardrails (prompt injection, sensitive-data disclosure, excessive agency, adversarial testing) — distinct threat model from A.12; required control vocabulary for GenAI over client/regulatory data under DORA & EU AI Act | roadmap.sh ai-engineer ✓ | T3 | 7 | OWASP Top 10 for LLM & GenAI Applications (2025) — https://genai.owasp.org/llm-top-10/ | 2 |

**Appendix A total: ≈ 173 h** (counted in the budget; of which 90 h are the Phase-0 foundations A.27–A.31, each individually skippable via the Skip List).

### Considered and judged already covered (not gaps)

- **Relational DBMS internals** (CMU 15-445; postgresql-dba roadmap ✓) — the taxonomy names only the databases, but this plan already embeds the internals discipline as the T1 entry 3.2.1; the administration/HA slice that 3.2.1 does *not* cover became A.22.
- **Linux command line & shell craft** (postgresql-dba/devops roadmaps ✓) — initially judged covered by the learner profile; rescheduled as **A.27 in Phase 0** after the learner's instruction to assume nothing.
- **Kafka depth (CCDAK scope ✓: fundamentals, Streams, Connect, testing, observability)** — maps fully onto 2.4.1, 4.2.1, 2.2.2, 9.4.3, 12.7.2 entries; CCDAK adds depth, not breadth. Free prep guide via https://www.confluent.io/certification/.
- **Data-engineer roadmap (✓ via the roadmap content repo) & DE Zoomcamp module list** (Docker/Terraform, orchestration, dbt, Spark, Kafka, warehousing) — maps 1:1 onto Phases 2–5; Zoomcamp repo: https://github.com/DataTalksClub/data-engineering-zoomcamp (GCP-centric; use as pattern reference with Azure equivalents).
- **AWS SAP-C02 scope ✓** (multi-account governance, DR strategy by RTO/RPO, migration) — covered by 8.1.1 (CAF as the Azure analogue), 12.2.2, and A.10; the free exam-guide PDF is a strong professional-architect competency checklist: https://d1.awsstatic.com/training-and-certification/docs-sa-pro/AWS-Certified-Solutions-Architect-Professional_Exam-Guide.pdf.
- **SnowPro Advanced Architect scope ✓** (RBAC/masking/sharing/replication/Iceberg on Snowflake) — covered by 3.1.1, 11.1.2, 11.3.x, 13.3.2 at evaluation level; its performance domain became A.25.
- **GitOps, service mesh, artifact management** (devops roadmap ✓) — subsumed into A.6 (Kubernetes) and 9.3.1 (CI/CD).
- **Azure Cloud Design Patterns catalog** — not a gap (patterns 1.8.x cover the data-relevant set) but adopted as a primary resource in Phase 4: https://learn.microsoft.com/en-us/azure/architecture/patterns/ ✓.
- **DMBOK maturity assessment (ch. 15) / org & roles (ch. 16)** — covered by the DCAM T1 entry (1.12.12) and A.14.
- **Frontend frameworks, enterprise app vendors (SAP/Salesforce), microfrontends** — out of role; excluded.
