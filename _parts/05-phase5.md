<a id="phase-5"></a>
## Phase 5: Cloud Platform Architecture & Operations — Azure (months 28–33, 108 h + 37 h Appendix A)

**Goal:** turn the laptop platform into a cloud-shaped one: Azure reference architecture (WAF/CAF), infrastructure as code, Kubernetes as the runtime substrate, the Azure data services at evaluation depth, and the operations disciplines (observability, DR, FinOps) that keep a regulated platform alive and affordable.
**Entry prerequisites:** Phases 2–4 (a real multi-service stack worth provisioning); Appendix A items A.3 (networking), A.4 (Fabric), A.5 (KQL), A.6 (Kubernetes), A.22 (relational HA), A.25 (warehouse performance), A.26 (chaos/resilience testing) are scheduled inside this phase.
**Exit criteria:** you can (1) run a Well-Architected review of your own design and find real findings; (2) provision and tear down the platform from code alone; (3) state RTO/RPO for each platform tier and the topology that delivers it; (4) produce a defensible monthly-cost model for the Azure target architecture; (5) operate the stack on Kubernetes locally and explain what AKS changes.

### T1/T2 topics

#### 8.1.1 Azure reference architecture (WAF + CAF landing zones) — T1
- **Why:** the Well-Architected pillars and CAF landing zones are the daily design language on the primary cloud — reviews, RFPs, and audits are all conducted in it.
- **Learn:** WAF's five pillars and the data-platform-specific lenses; CAF landing zones: management groups, subscriptions-as-units, policy-driven governance (Azure Policy), hub-spoke network topology; identity baseline (Entra ID, managed identities); Azure analytics reference architectures (Synapse/Fabric/Databricks patterns in the Architecture Center); region pairs & availability zones for EU data residency.
- **Resource:** Microsoft Learn: Well-Architected Framework (data workload guidance) + CAF "Ready" methodology / enterprise-scale landing zone docs.
- **Tools:** FOSS: — (conceptual; exercised via IaC below) · Corp: Azure (primary), AWS Well-Architected as the comparison vocabulary.
- **Do:** run a written WAF review of your Capstone-4 architecture as if it ran on Azure: one finding + remediation per pillar.
- **Done when:** you can sketch a CSSF-friendly landing zone (mgmt groups → subscriptions → networks → identities) on a whiteboard and justify each boundary.
- Est. hours: 14

#### 9.10.1 Infrastructure as code (OpenTofu/Terraform) — T1
- **Why:** a named weak spot, and the medium in which every platform you design will actually ship; "architecture" that isn't in code is a slide.
- **Learn:** HCL: providers, resources, data sources, variables/outputs; state: backends, locking, drift, import; modules and composition; plan/apply discipline and CI integration; workspaces vs directory-per-env; secrets handling in IaC; Terraform↔OpenTofu split (BSL vs MPL) and what it means for vendor selection; azurerm provider patterns.
- **Resource:** OpenTofu docs (language + state) + *Terraform: Up & Running* 3rd ed. (concept chapters; commands transfer).
- **Tools:** FOSS: OpenTofu (↔ Terraform Cloud/Enterprise, Azure-native Bicep below) · Corp: Terraform Enterprise (evaluation level).
- **Do:** put the entire compose-era platform under OpenTofu using the docker, kubernetes, and helm providers: one `tofu apply` builds the full local stack; plus an azurerm module for the target architecture validated with `tofu plan` against a free-trial subscription (plan-only — no spend).
- **Done when:** `tofu destroy && tofu apply` reproduces the platform byte-for-byte, and you can explain every line of a teammate's plan output.
- Est. hours: 16

#### 9.10.2 Cloud-native IaC (Bicep) — T2
- **Why:** Microsoft shops mandate Bicep/ARM for Azure-only estates; you must hold a reasoned Bicep-vs-Terraform position in vendor-aligned organizations.
- **Learn:** Bicep syntax, modules, what-if deployments; ARM deployment model (incremental/complete); when Bicep wins (day-0 Azure features, no state file) vs Terraform (multi-cloud, ecosystem); AVM (Azure Verified Modules).
- **Resource:** Microsoft Learn Bicep fundamentals path (free).
- **Do:** rewrite one OpenTofu module (storage account + key vault + VNet) in Bicep; run `what-if`; write the 10-line comparison.
- **Done when:** you can recommend Bicep or Terraform for a given org and defend it against the other camp.
- Est. hours: 4

#### 2.1.2 + 5.6.2 Azure Data Factory (bulk movement + orchestration) — T2
- **Why:** ADF is the incumbent Azure data-movement and orchestration service you will meet in every Luxembourg estate — evaluation fluency is mandatory even if you'd choose Dagster.
- **Learn:** pipelines, activities, triggers; copy activity & integration runtimes (incl. self-hosted IR for on-prem); mapping data flows (Spark under the hood); ADF vs Synapse pipelines vs Fabric Data Factory lineage; pricing model (DIU-hours, activity runs); CI/CD for ADF (ARM/Git mode); where ADF orchestration breaks down vs code-first orchestrators.
- **Resource:** ADF official docs (concepts + copy activity + self-hosted IR).
- **Tools:** Corp: ADF/Fabric DF (↔ FOSS: Airbyte + Dagster from earlier phases).
- **Do:** design (on paper + pricing calculator) the ADF implementation of your Airbyte+Dagster ingestion: pipeline sketch, IR placement for an on-prem TA system, monthly cost estimate.
- **Done when:** you can argue ADF-vs-code-first for three scenarios (lift-and-shift shop, product team, hybrid estate) with costs.
- Est. hours: 6

#### 4.2.2 Cloud-native streaming (Event Hubs, Stream Analytics) — T2
- **Why:** Event Hubs is what "Kafka on Azure" usually means in practice; knowing its limits against real Kafka is a recurring design question.
- **Learn:** Event Hubs model: namespaces, throughput units/processing units, partitions, capture; Kafka-protocol surface and its gaps (no compaction, transactions limits); Azure Stream Analytics SQL jobs vs Flink; Service Bus vs Event Hubs vs Event Grid triage.
- **Resource:** Event Hubs docs (features + Kafka compatibility page).
- **Do:** map every Capstone-4 Kafka feature you used to Event Hubs; flag the ones that don't translate and their workarounds.
- **Done when:** you can answer "can we just use Event Hubs?" with a feature-by-feature verdict.
- Est. hours: 3

#### 4.1.2 Serverless compute (Azure Functions) — T2
- **Why:** functions are the glue tier of cloud data platforms (event handlers, light transforms, API shims); the architect decides where glue ends and engines begin.
- **Learn:** triggers/bindings, hosting plans (consumption/premium), cold starts; Durable Functions (ties to 5.6.4); when functions become an anti-pattern (long-running, stateful, heavy data movement).
- **Resource:** Azure Functions docs (concepts + hosting options).
- **Do:** local-run (Functions Core Tools, free) an event-triggered function that validates an incoming EMT file drop and emits an event; document its Azure cost profile at 10k files/month.
- **Done when:** you can draw the line between function-glue and pipeline-engine for five workloads.
- Est. hours: 3

#### 4.3.2 Cloud query services — T2
- **Why:** serverless SQL over the lake (Synapse serverless, Athena) is the cheap-and-cheerful tier of lakehouse consumption; knowing its price/perf envelope completes the engine matrix.
- **Learn:** per-TB-scanned pricing mechanics and the partitioning/pruning economics it creates; OPENROWSET/external tables; Athena/Trino lineage; when serverless SQL beats a running warehouse and when it bankrupts you.
- **Resource:** Synapse serverless SQL docs (best practices page).
- **Do:** estimate query cost for your gold layer at three partitioning strategies; one paragraph on the design pressure per-TB pricing creates.
- **Done when:** you can explain why file layout *is* the cost model in serverless SQL.
- Est. hours: 2

#### 8.1.2 Vendor reference architectures — T2
- **Why:** Databricks/Snowflake/Fabric blueprints are the shapes vendors will pitch at your employer; you need to read them critically, not learn them reverently.
- **Learn:** Databricks lakehouse reference (Unity Catalog-centric, medallion); Snowflake data cloud patterns (shares, zero-copy); Fabric end-to-end (OneLake-centric, capacity-based); what each blueprint optimizes for the *vendor*; mapping all three onto your open-stack mental model.
- **Resource:** each vendor's official reference-architecture page (one sitting each).
- **Do:** annotate one vendor blueprint: circle every lock-in point and every place your open stack has an equivalent.
- **Done when:** you can translate any vendor diagram into open-component vocabulary live in a meeting.
- Est. hours: 3

#### 11.8.1 Secrets management — T2
- **Why:** pipelines hold credentials to everything; secrets architecture is a prerequisite to the Phase-6 security work and every audit.
- **Learn:** secret stores (Key Vault, OpenBao/Vault) vs env vars vs files; rotation; managed identities as the no-secret ideal; secret injection into K8s (CSI driver) and CI; the Vault→OpenBao licensing fork.
- **Resource:** OpenBao docs (concepts) + Azure Key Vault + managed identities overview.
- **Tools:** FOSS: OpenBao (↔ Azure Key Vault, AWS Secrets Manager) · Corp: Key Vault (primary).
- **Do:** move every credential in the compose/K8s stack out of files into OpenBao; document the rotation runbook.
- **Done when:** `git grep -i password` returns nothing real, and rotation is a 5-minute documented operation.
- Est. hours: 3

#### 12.7.2 Observability stack (OpenTelemetry, Prometheus, Grafana) — T2
- **Why:** logs/metrics/traces with OTel is the CNCF-standard nervous system; data platforms without it are debugged by archaeology.
- **Learn:** three pillars + OTel signals model (traces/metrics/logs, collector, OTLP); Prometheus: scrape model, PromQL basics, alerting rules; Grafana dashboards; Loki for logs; instrumenting a Python pipeline with OTel; SLI/SLO/error-budget vocabulary (deepened in Phase 8 for data SLAs); Azure Monitor/App Insights as the corp mapping (ties to A.5 KQL).
- **Resource:** OpenTelemetry docs (concepts + Python) + Prometheus "Overview"/PromQL basics.
- **Tools:** FOSS: OTel + Prometheus + Grafana + Loki (↔ Azure Monitor, Datadog) · Corp: Datadog/Azure Monitor (evaluation level).
- **Do:** instrument the Dagster→Spark→Iceberg path with OTel traces and pipeline metrics (rows, lag, duration); build the platform-health Grafana dashboard with two alert rules (freshness, consumer lag).
- **Done when:** a seeded failure is diagnosable from the dashboard alone in under five minutes, traces included.
- Est. hours: 8

#### 12.2.2 Disaster-recovery patterns — T1
- **Why:** RTO/RPO design is a DORA-driven architect deliverable; "what happens if the region dies?" now has regulatory teeth in EU financial services.
- **Learn:** RTO/RPO/RCO definitions and how to elicit honest numbers from the business; topology ladder: backup-restore → pilot light → warm standby → active-active, with cost curves; data-layer DR specifics: storage replication (LRS/ZRS/GRS), database geo-replication & failover groups, Kafka cross-cluster (MirrorMaker/Geo-DR), lakehouse DR (re-derivable vs source-of-truth tiers); DR testing discipline (game days, failover drills); region pairs & EU residency constraints.
- **Resource:** Azure Architecture Center DR guidance + WAF reliability pillar (data workload sections).
- **Do:** write the DR design for your platform: tier every store by RPO/RTO class, choose a topology per tier, cost the delta vs single-region, and script one tabletop failover drill.
- **Done when:** you can defend why gold marts get warm standby but bronze gets backup-restore, with numbers.
- Est. hours: 7

#### 12.1.1 Backup & recovery (cloud-native) — T2
- **Why:** backups are the bottom rung of the DR ladder and the part auditors actually test; lakehouse-era backup is mostly *not* file copies.
- **Learn:** Azure Backup model (vaults, policies, soft delete, immutability for ransomware); database PITR windows; object-store versioning + lifecycle as backup; Iceberg snapshot retention vs backup (and why snapshots ≠ backups when the catalog dies); restore testing.
- **Resource:** Azure Backup docs (overview + blob/database sections).
- **Do:** define the backup policy matrix for every store in the platform (what, frequency, retention, immutability, restore test cadence); run one real restore from MinIO versioning.
- **Done when:** you can answer "when did we last *restore* successfully?" with a date, not a shrug.
- Est. hours: 2

#### 12.3.1 FinOps / cloud cost management — T1
- **Why:** explicit mastery bias: cost models decide architectures, and the architect who can't price a design loses the vendor-selection argument to whoever can.
- **Learn:** FinOps lifecycle (inform/optimize/operate) and unit economics (€ per pipeline run, per report, per GB served); Azure pricing mechanics for data: storage tiers, egress, compute SKUs, reservations/savings plans, spot; tagging & cost allocation (showback/chargeback); the big levers: storage-format efficiency, cluster right-sizing, serverless-vs-provisioned crossover, egress avoidance; Azure Cost Management + budgets/alerts; FOCUS billing-data standard (awareness).
- **Resource:** FinOps Foundation framework docs (free) + Azure Cost Management docs; Azure pricing calculator as the lab bench.
- **Tools:** FOSS: OpenCost (K8s cost, awareness) · Corp: Azure Cost Management (primary), Vantage/Cloudability (awareness).
- **Do:** build the full monthly cost model of your target Azure architecture (calculator-based) at 1× and 10× data volume; identify the three biggest levers and re-price after pulling them.
- **Done when:** you can state € per daily NAV pipeline run and defend every line of the model to a CFO.
- Est. hours: 9

#### 12.3.2 Data-specific FinOps — T2
- **Why:** warehouse credits and per-query economics behave differently from VM bills; data FinOps is its own discipline with its own levers.
- **Learn:** Snowflake credit burn anatomy (warehouse size × uptime; auto-suspend discipline); Databricks DBU model & cluster policies; BigQuery on-demand vs capacity; per-query attribution; the query-cost review as a governance practice.
- **Resource:** Snowflake cost-management docs + Databricks cluster-policy docs (read as patterns).
- **Do:** write the "cost guardrails" standard for a warehouse estate: auto-suspend, size caps, query tagging, monthly review ritual.
- **Done when:** you can spot the three classic credit-burn anti-patterns in a usage report.
- Est. hours: 3

#### 3.3.4 Caching — T2
- **Why:** caches (Redis/Valkey) sit in front of every serving layer; the architect mostly decides *whether* and *where*, not *how*.
- **Learn:** cache-aside vs read/write-through; invalidation & TTL discipline; what to cache in a data platform (API responses, semantic-layer results, feature lookups); Valkey/Redis licensing fork; Azure Cache for Redis.
- **Resource:** Azure Architecture Center caching guidance page.
- **Do:** decide cache placement for the Phase-8 data API (yes/no, where, TTL) and write the 10-line justification.
- **Done when:** you can articulate the staleness-vs-load tradeoff for fund NAV data specifically (hint: NAVs are daily — cache hard).
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 2.2.1 | Log/metric shippers | Fluent Bit/Vector agents feeding observability pipelines | Vector docs "concepts" | 20 |
| 2.5.1 | iPaaS | Workato/Boomi/Power Automate business-user integration | Power Automate overview | 20 |
| 2.5.2 | ESB (legacy) | Central-bus integration era (TIBCO/IBM); what you'll be strangling | one architecture-blog ESB retrospective | 20 |
| 3.2.7 | Time-series databases | Prometheus/InfluxDB/kdb+ (kdb+ = market-data niche) | InfluxDB "what is time series" page | 20 |
| 3.3.2 | Block storage | VM disks (Azure Managed Disks); database substrate | Azure Disks overview | 15 |
| 3.3.3 | File storage | NFS/SMB shares (Azure Files); legacy app integration | Azure Files overview | 15 |
| 5.1.1 | Visual ETL suites | Informatica/SSIS/DataStage — the installed base in EU FS | Informatica PowerCenter product page | 25 |
| 9.10.3 | Configuration management | Ansible/Chef VM-era config; mostly displaced by containers | Ansible "how it works" | 20 |
| 12.1.2 | Enterprise backup suites | Veeam/Commvault/Rubrik estates in on-prem banks | Veeam product overview | 15 |
| 12.2.1 | DR tooling | Azure Site Recovery/Zerto orchestrated failover | ASR overview | 20 |
| 12.5.1 | On-call/paging | PagerDuty/Opsgenie rotations & escalation | PagerDuty "what is on-call" | 15 |
| 12.5.2 | Postmortems | Blameless incident review practice | Google SRE book postmortem chapter (free online) | 30 |
| 12.6.1 | Capacity planning | Forecasting growth vs provisioning | Google SRE book capacity chapter intro | 20 |
| 12.7.1 | Commercial APM | Datadog/Dynatrace full-stack suites | Datadog product tour | 15 |
| 14.7.3 | Notification tools | Paging/chat alert routing from data signals | Grafana alerting → contact points docs | 10 |

*T3 subtotal: 4.5 h*

### Capstone 5 — IaC-provisioned platform on Kubernetes + Well-Architected review

- **Goal:** the platform becomes infrastructure-as-code on a cloud-shaped runtime, with observability, a DR position, and a cost model — everything an architecture review board would demand.
- **Stack (100% free):** kind or k3d local Kubernetes (↔ AKS), Helm charts for Kafka/Flink/Trino/Dagster/MinIO/Postgres (↔ managed PaaS equivalents), OpenTofu with kubernetes/helm/azurerm providers (↔ Terraform Enterprise), Bicep comparison module, OpenBao (↔ Key Vault), OTel + Prometheus + Grafana + Loki (↔ Azure Monitor), Azure pricing calculator + free-trial `tofu plan` (no spend).
- **Build:** (1) migrate the compose stack to kind via Helm, OpenTofu-managed end to end; (2) secrets via OpenBao with documented rotation; (3) full observability: traces through one pipeline run, platform dashboard, two alerts; (4) azurerm module expressing the target Azure architecture (landing-zone slice: VNet/Private Link per A.3, ADLS, AKS, Event Hubs, Key Vault) — validated plan-only; (5) WAF review of the result (one finding per pillar, remediated or accepted in writing); (6) DR design + tabletop drill; (7) monthly cost model at 1×/10×.
- **Architecture deliverables:** C4 deployment diagram (new level for this phase); ADR-013 Kubernetes vs managed-PaaS-per-service, ADR-014 OpenTofu vs Bicep for this estate, ADR-015 DR topology per data tier.
- **Acceptance criteria:** fresh machine → `tofu apply` → healthy platform → one full pipeline run → `tofu destroy`, all documented; seeded failure diagnosed from dashboards in <5 min; WAF review yields ≥5 genuine findings with dispositions; cost model withstands a "what if volumes 10×?" challenge; DR drill writeup names RTO/RPO per tier.
- Est. hours: 18

*Phase 5 total: 107.5 h (T1/T2 entries 85 h + T3 4.5 h + capstone 18 h) + Appendix A items A.3–A.6, A.22, A.25, A.26 (37 h) scheduled in this phase*
