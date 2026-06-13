<a id="phase-5"></a>
## Phase 5: Cloud Platform Architecture & Operations — Azure (months 28–33, 108 h + 37 h Appendix A)

*Phase 5 of 8 · months 28–33 · 145 h (108 h + 37 h Appendix A) · capstone: IaC platform on Kubernetes + Well-Architected review.*  ← [Phase 4](#phase-4) · [Phase 6](#phase-6) →

**Goal:** turn the laptop platform into a cloud-shaped one: Azure reference architecture (WAF/CAF), infrastructure as code, Kubernetes as the runtime substrate, the Azure data services at evaluation depth, and the operations disciplines (observability, DR, FinOps) that keep a regulated platform alive and affordable.
**Entry prerequisites:** Phases 2–4 (a real multi-service stack worth provisioning); Appendix A items A.3 (networking), A.4 (Fabric), A.5 (KQL), A.6 (Kubernetes), A.22 (relational HA), A.25 (warehouse performance), A.26 (chaos/resilience testing) are scheduled inside this phase.
**Exit criteria:** you can (1) run a Well-Architected review of your own design and find real findings; (2) provision and tear down the platform from code alone; (3) state RTO/RPO for each platform tier and the topology that delivers it; (4) produce a defensible monthly-cost model for the Azure target architecture; (5) operate the stack on Kubernetes locally and explain what AKS changes.

### T1/T2 topics

#### 8.1.1 Azure reference architecture (WAF + CAF landing zones) — T1
- **Why:** the Well-Architected pillars and CAF landing zones are the daily design language on the primary cloud — reviews, RFPs, and audits are all conducted in it. In a Luxembourg fund-administration estate, the architect who can't map a design to landing-zone boundaries and the five WAF pillars can't get a design through an architecture review board or a CSSF-aligned governance gate. Without this, designs leak across subscription/identity boundaries and you lose the data-residency and segregation arguments before you start.
- **Learn:**
    - WAF's five pillars (reliability, security, cost, operational excellence, performance) and the data-workload lens — what each pillar asks of a data platform specifically *(WAF docs: pillars)*
    - CAF landing zones — management groups → subscriptions-as-units → policy-driven governance via Azure Policy *(CAF docs: What is a landing zone)*
    - hub-spoke vs Virtual WAN network topology — why shared services (identity, connectivity) live in a platform landing zone *(CAF docs: landing zone architecture)*
    - identity baseline — Entra ID, managed identities as the no-secret default for service-to-service auth *(Entra docs: managed identities)*
    - region pairs & availability zones — how to keep EU fund data inside a residency boundary while surviving a zone/region loss *(WAF docs: reliability)*
- **Resources:**
    - **[Microsoft Learn: Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)** — the five pillars, the review/assessment tool, and per-service guidance you'll run your design against (primary)
    - [CAF: What is an Azure landing zone?](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) — management-group hierarchy, platform vs application landing zones, hub-spoke reference (reference)
    - [Entra: managed identities overview](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview) — the identity baseline that makes the landing zone credential-free (deepening)
- **Tools:**
    - Corp (evaluate): [Azure](https://learn.microsoft.com/azure/) — the primary cloud; landing zones and WAF are how its governance is expressed
    - Corp (evaluate): [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) — the comparison vocabulary so you can read multi-cloud RFPs
- **Do:**
    1. Take your Capstone-4 architecture and run a written WAF review as if it ran on Azure: one finding plus a remediation per pillar (five findings minimum).
    2. Sketch a CSSF-friendly landing zone: management groups → subscriptions → VNets → identities, naming the boundary at each level.
    3. For each pillar finding, name the Azure control that closes it (e.g. Azure Policy for governance, Private Link for security, ZRS for reliability).
    4. Write a one-paragraph data-residency note: which region pair you chose and why it keeps fund data in-boundary.
- **Done when:**
    - [ ] You can sketch the landing zone (mgmt groups → subscriptions → networks → identities) on a whiteboard and justify each boundary.
    - [ ] You can name one concrete finding and remediation per WAF pillar for your own design.
    - [ ] You can state the region-pair and zone topology that meets EU residency without single-region risk.
- Est. hours: 14

#### 9.10.1 Infrastructure as code (OpenTofu/Terraform) — T1
- **Why:** a named weak spot, and the medium in which every platform you design will actually ship; "architecture" that isn't in code is a slide. In a regulated estate, IaC is also the audit trail and the reproducibility guarantee — reviewers want to see the exact resources, policies, and network rules as version-controlled code, not portal screenshots. Without it, environments drift, DR rebuilds are guesswork, and there is no four-eyes review on infrastructure change.
- **Learn:**
    - HCL building blocks — providers, resources, data sources, variables/outputs and how they compose *(OpenTofu docs: language)*
    - state mechanics — remote backends, locking, drift detection, `import` for brownfield estates *(OpenTofu docs: state)*
    - modules and composition — reusable units (a VNet module, a storage module) and workspaces vs directory-per-env *(OpenTofu docs: language)*
    - plan/apply discipline and CI integration — why `plan` is the review artifact and `apply` is gated *(Terraform Up & Running: workflow chapters)*
    - secrets handling in IaC — never in state in clear; reference Key Vault/OpenBao instead *(OpenTofu docs: state, sensitive values)*
    - Terraform↔OpenTofu split (BSL vs MPL) — what the licence fork means for vendor selection *(Terraform Up & Running)*
- **Resources:**
    - **[OpenTofu documentation](https://opentofu.org/docs/)** — language, [state](https://opentofu.org/docs/language/state/), CLI; the FOSS engine you build on (primary)
    - [Terraform: Up & Running, 3rd ed.](https://www.terraformupandrunning.com/) — the concept chapters (state, modules, workflow, testing); commands transfer one-to-one to OpenTofu (reference)
- **Tools:**
    - FOSS (hands-on): [OpenTofu](https://opentofu.org/docs/) — the MPL-licensed engine; drives the compose-era stack and a plan-only azurerm module (↔ Terraform Cloud/Enterprise)
    - Corp (evaluate): [Terraform Enterprise / HCP Terraform](https://developer.hashicorp.com/terraform) — what state backend, policy-as-code (Sentinel), and run governance buy at build-vs-buy level
- **Do:**
    1. Put the entire compose-era platform under OpenTofu using the docker, kubernetes, and helm providers so that one `tofu apply` builds the full local stack.
    2. Factor shared infrastructure (network, storage) into reusable modules; configure a remote state backend with locking.
    3. Write an azurerm module for the target architecture and validate it with `tofu plan` against a free-trial subscription — plan-only, no spend.
    4. Run `tofu destroy && tofu apply` and confirm the platform comes back identically; capture the plan output as the review artifact.
- **Done when:**
    - [ ] Reproduce the platform byte-for-byte with `tofu destroy && tofu apply`.
    - [ ] Explain every line of a teammate's plan output, including what a replace vs in-place update means.
    - [ ] Show that no secret value is stored in clear in state.
- Est. hours: 16

#### 9.10.2 Cloud-native IaC (Bicep) — T2
- **Why:** Microsoft shops mandate Bicep/ARM for Azure-only estates; you must hold a reasoned Bicep-vs-Terraform position in vendor-aligned organizations. Many Luxembourg fund-tech teams are Azure-only and will hand you Bicep, so evaluation fluency is the difference between recommending the right tool and being overruled. Without it, you cannot read the incumbent's deployment code or argue the trade-off credibly.
- **Learn:**
    - Bicep syntax and modules — declarative resource authoring that compiles to ARM JSON *(Bicep docs: file structure)*
    - `what-if` deployments and the ARM deployment model (incremental vs complete) — preview-before-apply on Azure *(Bicep docs: what-if)*
    - when Bicep wins (day-0 Azure features, no state file to manage) vs Terraform (multi-cloud, ecosystem, providers) *(Bicep docs: overview)*
    - Azure Verified Modules (AVM) — the curated module library Microsoft ships for landing zones *(Bicep docs: best practices)*
- **Resources:**
    - **[Microsoft Learn: Bicep documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/)** — fundamentals, file structure, `what-if`, AVM; the free path that covers every Learn bullet (primary)
    - [Fundamentals of Bicep (training path)](https://learn.microsoft.com/en-us/training/paths/fundamentals-bicep/) — hands-on guided modules (reference)
- **Tools:**
    - Corp (evaluate): [Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/) — Azure-native IaC; no state file, day-0 resource coverage (↔ OpenTofu/Terraform)
- **Do:**
    1. Rewrite one OpenTofu module (storage account + key vault + VNet) in Bicep.
    2. Run `az deployment group what-if` and read the predicted change set.
    3. Write a 10-line comparison: where Bicep was simpler, where Terraform's multi-cloud/state model wins.
- **Done when:**
    - [ ] Recommend Bicep or Terraform for a given org and defend it against the other camp.
    - [ ] Produce a working `what-if` output for your rewritten module.
- Est. hours: 4

#### 2.1.2 + 5.6.2 Azure Data Factory (bulk movement + orchestration) — T2
- **Why:** ADF is the incumbent Azure data-movement and orchestration service you will meet in every Luxembourg estate — evaluation fluency is mandatory even if you'd choose Dagster. The architect is constantly asked "why not just use ADF?" by stakeholders who already pay for it, and needs costed, scenario-specific answers. Without this, you either rubber-stamp ADF where it breaks down or reject it without being able to say why.
- **Learn:**
    - pipelines, activities, triggers — ADF's orchestration primitives and their limits vs code-first DAGs *(ADF docs: introduction)*
    - copy activity & integration runtimes, including self-hosted IR for on-prem transfer-agency systems *(ADF docs: introduction, integration runtime)*
    - mapping data flows — Spark under the hood, and when that is the right or wrong engine *(ADF docs: introduction)*
    - ADF vs Synapse pipelines vs Fabric Data Factory — the lineage and which one a given estate is on *(ADF docs: introduction)*
    - pricing model — DIU-hours, activity runs, IR hours, and where the bill surprises you *(Azure Cost Management docs)*
- **Resources:**
    - **[Azure Data Factory: Introduction](https://learn.microsoft.com/en-us/azure/data-factory/introduction)** — pipelines, activities, copy activity, integration runtimes, CI/CD (primary)
    - [Azure Cost Management overview](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview) — the mechanics behind DIU-hour and activity-run pricing (reference)
- **Tools:**
    - Corp (evaluate): [Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/introduction) — incumbent bulk movement + orchestration; self-hosted IR for on-prem (↔ FOSS: Airbyte + Dagster from earlier phases)
    - FOSS (hands-on): [Dagster](https://docs.dagster.io/) — the code-first orchestrator you compare ADF against
- **Do:**
    1. On paper plus the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/), design the ADF implementation of your Airbyte+Dagster ingestion: pipeline sketch, IR placement for an on-prem TA system.
    2. Produce a monthly cost estimate (DIU-hours + activity runs + self-hosted IR).
    3. Identify two places where ADF orchestration breaks down vs a code-first orchestrator and note the workaround or the line you'd draw.
- **Done when:**
    - [ ] Argue ADF-vs-code-first for three scenarios (lift-and-shift shop, product team, hybrid estate) with costs.
    - [ ] Place a self-hosted IR correctly for an on-prem source and explain why.
- Est. hours: 6

#### 4.2.2 Cloud-native streaming (Event Hubs, Stream Analytics) — T2
- **Why:** Event Hubs is what "Kafka on Azure" usually means in practice; knowing its limits against real Kafka is a recurring design question. In a fund platform that streams order/trade events, choosing Event Hubs where you needed log compaction or full transactions corrupts the design quietly. The architect must give a feature-by-feature verdict, not a vibe.
- **Learn:**
    - Event Hubs model — namespaces, throughput/processing units, partitions, Capture to ADLS *(Event Hubs docs: about)*
    - Kafka-protocol surface and its gaps — no log compaction, transaction limits vs open-source Kafka *(Event Hubs docs: Kafka compatibility)*
    - Azure Stream Analytics SQL jobs vs Flink — the SQL-temporal model and where it stops *(Stream Analytics docs: introduction)*
    - Service Bus vs Event Hubs vs Event Grid triage — streaming vs enterprise messaging vs reactive routing *(Event Hubs docs: choosing messaging services)*
- **Resources:**
    - **[Azure Event Hubs: What is Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about)** — model, partitions, Capture, Kafka compatibility, messaging-service triage (primary)
    - [Azure Stream Analytics: Introduction](https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction) — SQL streaming jobs, exactly-once semantics, vs Flink (reference)
- **Tools:**
    - Corp (evaluate): [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about) — managed Kafka-protocol streaming (↔ FOSS: Apache Kafka/Redpanda)
    - Corp (evaluate): [Azure Stream Analytics](https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction) — managed SQL stream processing (↔ FOSS: Apache Flink)
- **Do:**
    1. List every Kafka feature you used in Capstone-4 (compaction, transactions, consumer groups, retention).
    2. Map each to Event Hubs; flag the ones that don't translate and write the concrete workaround.
    3. Pick one transform and note whether Stream Analytics SQL or Flink fits, with the reason.
- **Done when:**
    - [ ] Answer "can we just use Event Hubs?" with a feature-by-feature verdict.
    - [ ] Name at least one Kafka feature that does not translate and its workaround.
- Est. hours: 3

#### 4.1.2 Serverless compute (Azure Functions) — T2
- **Why:** functions are the glue tier of cloud data platforms (event handlers, light transforms, API shims); the architect decides where glue ends and engines begin. Misplacing that line — running heavy data movement or long stateful jobs in Functions — produces cold-start latency, timeouts, and surprise bills in a fund platform that drops EMT/NAV files on a schedule. Without a clear rule, glue silently grows into an unmaintainable shadow pipeline.
- **Learn:**
    - triggers and bindings — the event-to-code wiring (blob trigger on a file drop, output binding to an event) *(Functions docs: overview)*
    - hosting plans — Flex Consumption/Premium/Dedicated and the cold-start trade-off *(Functions docs: hosting options)*
    - Durable Functions — orchestration for multi-step serverless workflows (ties to 5.6.4) *(Functions docs: overview)*
    - when functions become an anti-pattern — long-running, stateful, heavy data movement *(Functions docs: scenarios)*
- **Resources:**
    - **[Azure Functions overview](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview)** — triggers/bindings, hosting options, Durable Functions, the cost model (primary)
    - [Azure Functions scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios) — the file-upload, stream-processing, and scheduled-task patterns that show where functions fit and where they don't (reference)
- **Tools:**
    - FOSS (hands-on): [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) — run and debug functions locally for free (↔ the managed Functions service)
    - Corp (evaluate): [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview) — the hosted serverless tier; know its cost profile at scale
- **Do:**
    1. Locally run (Core Tools, free) an event-triggered function that validates an incoming EMT file drop and emits an event.
    2. Document its Azure cost profile at 10k files/month (executions + GB-seconds + plan).
    3. Write the rule that separates function-glue from pipeline-engine, with one example on each side.
- **Done when:**
    - [ ] Draw the line between function-glue and pipeline-engine for five workloads.
    - [ ] Produce a working local function that validates a file and emits an event.
- Est. hours: 3

#### 4.3.2 Cloud query services — T2
- **Why:** serverless SQL over the lake (Synapse serverless, Athena) is the cheap-and-cheerful tier of lakehouse consumption; knowing its price/perf envelope completes the engine matrix. With per-TB-scanned pricing, a badly partitioned gold layer turns an ad-hoc query into a four-figure bill — the architect who doesn't understand this signs off file layouts that bankrupt the consumption tier. File layout literally is the cost model here.
- **Learn:**
    - per-TB-scanned pricing mechanics — and the partitioning/pruning economics it forces *(Synapse serverless docs: best practices)*
    - OPENROWSET / external tables — querying Parquet/Delta in place without a running warehouse *(Synapse serverless docs: best practices)*
    - Athena/Trino lineage — the same serverless-SQL-over-object-store pattern across clouds *(Synapse serverless docs: best practices)*
    - when serverless SQL beats a running warehouse vs when it bankrupts you — query frequency × scan size crossover *(Synapse serverless docs: best practices)*
- **Resources:**
    - **[Synapse serverless SQL pool: best practices](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/best-practices-serverless-sql-pool)** — partitioning, Parquet conversion, predicate pushdown, statistics; the cost-model mechanics (primary)
    - [Trino documentation: overview](https://trino.io/docs/current/overview.html) — the open serverless-SQL-over-object-store engine that Athena/Synapse serverless descend from (reference)
- **Tools:**
    - Corp (evaluate): [Synapse serverless SQL](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/best-practices-serverless-sql-pool) — per-TB query over the lake (↔ FOSS: Trino over MinIO from earlier phases)
    - FOSS (hands-on): [Trino](https://trino.io/docs/current/) — the open serverless-SQL engine that makes the pricing trade-off concrete
- **Do:**
    1. Estimate query cost for your gold layer at three partitioning strategies (none, by date, by date+ISIN).
    2. Convert one CSV gold table to partitioned Parquet and re-estimate the scan.
    3. Write one paragraph on the design pressure per-TB pricing creates on file layout.
- **Done when:**
    - [ ] Explain why file layout *is* the cost model in serverless SQL.
    - [ ] Show the cost delta across your three partitioning strategies.
- Est. hours: 2

#### 8.1.2 Vendor reference architectures — T2
- **Why:** Databricks/Snowflake/Fabric blueprints are the shapes vendors will pitch at your employer; you need to read them critically, not learn them reverently. Each blueprint is optimized for the vendor's lock-in, and the architect's job is to translate it into open-component vocabulary and circle the lock-in points live in a meeting. Without this, the org buys the diagram and discovers the exit cost three years later.
- **Learn:**
    - Databricks lakehouse reference — Unity Catalog-centric, medallion layering, DBU-priced compute *(Databricks docs: well-architected lakehouse)*
    - Snowflake data-cloud patterns — secure data sharing, zero-copy clones, listings/exchanges *(Snowflake docs: data sharing)*
    - Fabric end-to-end — OneLake-centric, capacity-based, experiences stitched together *(Fabric docs: end-to-end tutorials)*
    - what each blueprint optimizes for the vendor, and mapping all three onto your open-stack mental model *(Databricks docs: well-architected lakehouse)*
- **Resources:**
    - **[Databricks: well-architected lakehouse](https://docs.databricks.com/aws/en/lakehouse-architecture/)** — the Unity-Catalog/medallion reference and its design principles (primary)
    - [Snowflake: data sharing and collaboration](https://docs.snowflake.com/en/guides-overview-sharing) — shares, listings, zero-copy collaboration patterns (reference)
    - [Microsoft Fabric: end-to-end tutorials](https://learn.microsoft.com/en-us/fabric/get-started/end-to-end-tutorials) — the OneLake-centric, capacity-based blueprint end to end (reference)
- **Do:**
    1. Read one vendor blueprint in a single sitting and annotate it.
    2. Circle every lock-in point (proprietary catalog, proprietary format, capacity SKU, egress trap).
    3. For each lock-in point, write the open-stack equivalent (Iceberg, a catalog, Trino, MinIO).
- **Done when:**
    - [ ] Translate any vendor diagram into open-component vocabulary live in a meeting.
    - [ ] Name the single biggest lock-in point in each of the three blueprints.
- Est. hours: 3

#### 11.8.1 Secrets management — T2
- **Why:** pipelines hold credentials to everything; secrets architecture is a prerequisite to the Phase-6 security work and every audit. A fund platform connecting to transfer-agency systems, market-data feeds, and the warehouse cannot have passwords in env vars or config files — that is an immediate audit finding and a breach waiting to happen. Get this wrong and rotation becomes impossible, so leaked credentials live forever.
- **Learn:**
    - secret stores vs env vars vs files — why a vault with access policies and audit logs is the only acceptable answer *(OpenBao docs: concepts)*
    - rotation — short-lived dynamic secrets and the rotation runbook *(OpenBao docs)*
    - managed identities as the no-secret ideal — eliminate the credential entirely where Azure supports it *(Entra docs: managed identities)*
    - secret injection into K8s (CSI driver) and CI — getting secrets to workloads without writing them to disk *(Azure Key Vault docs: overview)*
    - the Vault→OpenBao licensing fork — what the BSL change means for tool selection *(OpenBao docs: concepts)*
- **Resources:**
    - **[OpenBao documentation](https://openbao.org/docs/)** — concepts, secret engines, dynamic secrets, rotation; the MPL fork of Vault (primary)
    - [Azure Key Vault overview](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) — the corp store, HSM tiers, RBAC, integration with K8s/CI (reference)
    - [Entra: managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview) — the no-secret pattern that beats any store (deepening)
- **Tools:**
    - FOSS (hands-on): [OpenBao](https://openbao.org/docs/) — self-hosted secret store with dynamic secrets (↔ Azure Key Vault, AWS Secrets Manager)
    - Corp (evaluate): [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) — managed store + HSM; pairs with managed identities
- **Do:**
    1. Move every credential in the compose/K8s stack out of files into OpenBao.
    2. Wire one service to fetch its secret at runtime (CSI driver or API), not from disk.
    3. Document the rotation runbook and time a rotation end to end.
- **Done when:**
    - [ ] Confirm `git grep -i password` returns nothing real.
    - [ ] Rotate a credential as a 5-minute documented operation.
    - [ ] Name one service where a managed identity removes the secret entirely.
- Est. hours: 3

#### 12.7.2 Observability stack (OpenTelemetry, Prometheus, Grafana) — T2
- **Why:** logs/metrics/traces with OTel is the CNCF-standard nervous system; data platforms without it are debugged by archaeology. When a NAV pipeline misses its cut-off, the architect must point to a dashboard that shows where lag or failure occurred — not start a forensic dig through logs. Without observability there are no data SLAs, no error budgets, and no honest answer to "is the platform healthy right now?".
- **Learn:**
    - the three pillars and the OTel signals model — traces/metrics/logs, the collector, OTLP *(OpenTelemetry docs: concepts)*
    - instrumenting a Python pipeline with OTel — spans across a Dagster→Spark→Iceberg run *(OpenTelemetry docs: Python)*
    - Prometheus — the scrape model, PromQL basics, alerting rules *(Prometheus docs: overview)*
    - Grafana dashboards and Loki for logs — the visualization and log-aggregation layer *(Grafana docs: contact points)*
    - SLI/SLO/error-budget vocabulary — deepened in Phase 8 for data SLAs *(OpenTelemetry docs: concepts)*
    - Azure Monitor/App Insights as the corp mapping — ties to A.5 KQL *(OpenTelemetry docs: concepts)*
- **Resources:**
    - **[OpenTelemetry documentation](https://opentelemetry.io/docs/concepts/)** — [concepts](https://opentelemetry.io/docs/concepts/) and [Python instrumentation](https://opentelemetry.io/docs/languages/python/); the signals model and how to emit it (primary)
    - [Prometheus: Overview](https://prometheus.io/docs/introduction/overview/) — scrape model, PromQL, alerting (reference)
    - [Grafana: configure contact points](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/) — dashboards and alert routing (reference)
- **Tools:**
    - FOSS (hands-on): [OpenTelemetry](https://opentelemetry.io/docs/) + [Prometheus](https://prometheus.io/docs/) + [Grafana](https://grafana.com/docs/grafana/latest/) + [Loki](https://grafana.com/docs/loki/latest/) — the open observability stack (↔ Azure Monitor, Datadog)
    - Corp (evaluate): [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/) / [Datadog](https://docs.datadoghq.com/) — managed observability; know the build-vs-buy line
- **Do:**
    1. Instrument the Dagster→Spark→Iceberg path with OTel traces and pipeline metrics (rows processed, lag, run duration).
    2. Stand up Prometheus to scrape the metrics and Grafana to visualize them.
    3. Build the platform-health Grafana dashboard with two alert rules: data freshness and consumer lag.
    4. Seed a failure and confirm it shows up on the dashboard with the trace attached.
- **Done when:**
    - [ ] Diagnose a seeded failure from the dashboard alone in under five minutes, traces included.
    - [ ] Show a single trace spanning the full Dagster→Spark→Iceberg run.
    - [ ] Demonstrate both alert rules firing on real conditions.
- Est. hours: 8

#### 12.2.2 Disaster-recovery patterns — T1
- **Why:** RTO/RPO design is a DORA-driven architect deliverable; "what happens if the region dies?" now has regulatory teeth in EU financial services. A fund administrator must be able to recover NAV-relevant data within stated objectives, and the architect owns the topology that delivers them tier by tier. Without an explicit, tested DR design, the org discovers its real RTO during the outage — and explains the gap to a regulator afterwards.
- **Learn:**
    - RTO/RPO/RCO definitions and how to elicit honest numbers from the business *(Azure reliability docs: BC/HA/DR)*
    - topology ladder — backup-restore → pilot light → warm standby → active-active, with cost curves *(Azure reliability docs: BC/HA/DR)*
    - data-layer DR specifics — storage replication (LRS/ZRS/GRS), database geo-replication & failover groups *(Azure reliability docs: BC/HA/DR)*
    - Kafka cross-cluster (MirrorMaker/Geo-DR) and lakehouse DR — re-derivable vs source-of-truth tiers *(Azure reliability docs: BC/HA/DR)*
    - DR testing discipline — game days, failover drills, region pairs & EU residency constraints *(Azure reliability docs: BC/HA/DR)*
- **Resources:**
    - **[Azure reliability: Business continuity, HA & DR](https://learn.microsoft.com/en-us/azure/reliability/concept-business-continuity-high-availability-disaster-recovery)** — RTO/RPO, the topology ladder, failover/failback, residency-bound DR (primary)
    - [PostgreSQL: log-shipping standby servers](https://www.postgresql.org/docs/current/warm-standby.html) — concrete warm-standby/geo-replication mechanics for the database tier (reference)
- **Tools:**
    - Corp (evaluate): [Azure Site Recovery](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview) — orchestrated failover for VM/on-prem tiers
    - FOSS (hands-on): [PostgreSQL streaming replication](https://www.postgresql.org/docs/current/warm-standby.html) — warm-standby you can demonstrate locally
- **Do:**
    1. Tier every store in your platform by RPO/RTO class (e.g. gold marts vs bronze raw).
    2. Choose a topology per tier (backup-restore, pilot light, warm standby, active-active) and justify it.
    3. Cost the delta of each chosen topology vs single-region.
    4. Script and run one tabletop failover drill, recording the achieved RTO/RPO.
- **Done when:**
    - [ ] Defend why gold marts get warm standby but bronze gets backup-restore, with numbers.
    - [ ] State RTO/RPO per tier and the topology that meets it.
    - [ ] Produce a tabletop drill writeup with achieved vs target objectives.
- Est. hours: 7

#### 12.1.1 Backup & recovery (cloud-native) — T2
- **Why:** backups are the bottom rung of the DR ladder and the part auditors actually test; lakehouse-era backup is mostly *not* file copies. A fund platform must answer "when did we last successfully restore?" with a date, and Iceberg snapshots are not a backup when the catalog itself is lost. Without immutable, tested backups, a ransomware event or a bad catalog migration is unrecoverable.
- **Learn:**
    - Azure Backup model — vaults, policies, soft delete, immutability for ransomware *(Azure Backup docs: overview)*
    - database PITR windows — point-in-time restore and its retention limits *(Azure Backup docs: overview)*
    - object-store versioning + lifecycle as backup — and its limits *(Azure Backup docs: overview)*
    - Iceberg snapshot retention vs backup — why snapshots ≠ backups when the catalog dies *(Azure Backup docs: overview)*
- **Resources:**
    - **[Azure Backup: overview](https://learn.microsoft.com/en-us/azure/backup/backup-overview)** — vaults, policies, immutability, blob/database backup, ransomware protection (primary)
    - [Reliability in Azure Backup](https://learn.microsoft.com/en-us/azure/reliability/reliability-backup) — soft delete, immutable vaults, ZRS/GRS for the backups themselves, and the restore-RPO/RTO mechanics (reference)
- **Tools:**
    - Corp (evaluate): [Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-overview) — vault-based backup with immutability (↔ FOSS object-store versioning)
    - FOSS (hands-on): [MinIO versioning](https://min.io/docs/minio/linux/administration/object-management/object-versioning.html) — the local stand-in for object-store backup/restore
- **Do:**
    1. Define a backup policy matrix for every store: what, frequency, retention, immutability, restore-test cadence.
    2. Run one real restore from MinIO versioning and time it.
    3. Note for each store whether a snapshot is a backup, and what additional protection the catalog needs.
- **Done when:**
    - [ ] Answer "when did we last *restore* successfully?" with a date, not a shrug.
    - [ ] Produce a complete backup policy matrix for the platform.
- Est. hours: 2

#### 12.3.1 FinOps / cloud cost management — T1
- **Why:** explicit mastery bias: cost models decide architectures, and the architect who can't price a design loses the vendor-selection argument to whoever can. In a fund business, a defensible "€ per daily NAV pipeline run" is what wins or loses the build-vs-buy debate with the CFO. Without a cost model, designs are chosen on aesthetics and the bill is discovered in production.
- **Learn:**
    - FinOps lifecycle (inform/optimize/operate) and unit economics — € per pipeline run, per report, per GB served *(FinOps Foundation framework)*
    - Azure pricing mechanics for data — storage tiers, egress, compute SKUs, reservations/savings plans, spot *(Azure Cost Management docs)*
    - tagging & cost allocation — showback/chargeback so costs land on the right business unit *(Azure Cost Management docs)*
    - the big levers — storage-format efficiency, cluster right-sizing, serverless-vs-provisioned crossover, egress avoidance *(FinOps Foundation framework)*
    - Azure Cost Management + budgets/alerts and the FOCUS billing standard (awareness) *(Azure Cost Management docs)*
- **Resources:**
    - **[FinOps Foundation: Framework](https://www.finops.org/framework/)** — the lifecycle, personas, capabilities, and unit-economics discipline (primary)
    - [Azure Cost Management overview](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview) — pricing mechanics, allocation, budgets/alerts (reference)
    - [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) — the lab bench for the cost model (reference)
- **Tools:**
    - Corp (evaluate): [Azure Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview) — the primary tool for analysis, budgets, allocation
    - FOSS (hands-on): [OpenCost](https://www.opencost.io/docs/) — Kubernetes cost allocation (awareness; ↔ Vantage/Cloudability)
- **Do:**
    1. Build the full monthly cost model of your target Azure architecture (calculator-based) at 1× data volume.
    2. Re-price the same model at 10× volume and note which lines scale and which step.
    3. Identify the three biggest levers and re-price after pulling them.
- **Done when:**
    - [ ] State € per daily NAV pipeline run and defend every line of the model to a CFO.
    - [ ] Show the 1× vs 10× cost shape and name what drives the difference.
    - [ ] Quantify the saving from your top three levers.
- Est. hours: 9

#### 12.3.2 Data-specific FinOps — T2
- **Why:** warehouse credits and per-query economics behave differently from VM bills; data FinOps is its own discipline with its own levers. A Snowflake or Databricks estate can burn its budget on idle warehouses and oversized clusters that a VM-centric FinOps view never catches. The architect who can spot credit-burn anti-patterns in a usage report is the one who keeps the analytics bill defensible.
- **Learn:**
    - Snowflake credit-burn anatomy — warehouse size × uptime, and auto-suspend discipline *(Snowflake docs: cost)*
    - Databricks DBU model & cluster policies — capping size/idle to control DBU spend *(Databricks docs: compute policies)*
    - BigQuery on-demand vs capacity — per-TB-scanned vs reserved slots *(Databricks docs: pricing)*
    - per-query attribution and the query-cost review as a governance practice *(Snowflake docs: cost)*
- **Resources:**
    - **[Snowflake: understanding overall cost](https://docs.snowflake.com/en/guides-overview-cost)** — credit anatomy, warehouse uptime, auto-suspend, attribution (primary)
    - [Databricks: create and manage compute policies](https://docs.databricks.com/aws/en/admin/clusters/policies) — cluster policies that cap DBU burn (reference)
    - [BigQuery pricing](https://cloud.google.com/bigquery/pricing) — on-demand vs capacity model for the cross-warehouse comparison (reference)
- **Tools:**
    - Corp (evaluate): [Snowflake](https://docs.snowflake.com/) — credit-based warehouse economics
    - Corp (evaluate): [Databricks](https://www.databricks.com/product/pricing) — DBU model and cluster policies
- **Do:**
    1. Write the "cost guardrails" standard for a warehouse estate: auto-suspend, size caps, query tagging, monthly review ritual.
    2. Map each guardrail to the mechanism that enforces it (warehouse setting, cluster policy, tag policy).
    3. List the three classic credit-burn anti-patterns and how the standard prevents each.
- **Done when:**
    - [ ] Spot the three classic credit-burn anti-patterns in a usage report.
    - [ ] Produce a guardrails standard with an enforcement mechanism per rule.
- Est. hours: 3

#### 3.3.4 Caching — T2
- **Why:** caches (Redis/Valkey) sit in front of every serving layer; the architect mostly decides *whether* and *where*, not *how*. For fund NAV data — computed once daily — caching is almost free wins, but for intraday positions a stale cache is a correctness bug. The architect who can't articulate the staleness-vs-load trade-off either over-caches and serves wrong numbers or under-caches and melts the serving layer.
- **Learn:**
    - cache-aside vs read/write-through — who owns the write and when the cache updates *(Azure caching guidance)*
    - invalidation & TTL discipline — the hard part; TTL choice as a correctness decision *(Azure caching guidance)*
    - what to cache in a data platform — API responses, semantic-layer results, feature lookups *(Azure caching guidance)*
    - Valkey/Redis licensing fork and Azure Cache for Redis / Azure Managed Redis *(Azure Cache for Redis docs: overview)*
- **Resources:**
    - **[Azure Architecture Center: Caching guidance](https://learn.microsoft.com/en-us/azure/architecture/best-practices/caching)** — cache-aside, write-through, invalidation, TTL, what to cache (primary)
    - [Azure Cache for Redis: overview](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview) — the managed cache tiers and patterns (reference)
- **Tools:**
    - FOSS (hands-on): [Valkey](https://valkey.io/documentation/) — the open Redis fork for the serving-layer cache (↔ Azure Cache for Redis)
    - Corp (evaluate): [Azure Cache for Redis](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview) — managed cache; note the retirement/Managed Redis migration path
- **Do:**
    1. Decide cache placement for the Phase-8 data API: yes/no, where in the path, and TTL.
    2. Write the 10-line justification anchored to the staleness-vs-load trade-off.
- **Done when:**
    - [ ] Articulate the staleness-vs-load tradeoff for fund NAV data specifically (hint: NAVs are daily — cache hard).
    - [ ] State the TTL you chose and why it is correct for that data's update cadence.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 2.2.1 | Log/metric shippers | Fluent Bit/Vector agents that collect, transform, and route logs/metrics into observability pipelines | [Vector docs "Concepts"](https://vector.dev/docs/introduction/concepts/) | 20 |
| 2.5.1 | iPaaS | Workato/Boomi/Power Automate low-code integration aimed at business users rather than data engineers | [Power Automate overview](https://learn.microsoft.com/en-us/power-automate/getting-started) | 20 |
| 2.5.2 | ESB (legacy) | Central-bus integration era (TIBCO/IBM); the "smart pipes" estate you'll be strangling toward smart-endpoints | [Fowler: Microservices (ESB/SOA retrospective)](https://martinfowler.com/articles/microservices.html) | 20 |
| 3.2.7 | Time-series databases | Prometheus/InfluxDB/kdb+ for timestamp-keyed data (kdb+ = the market-data niche in finance) | [InfluxDB "What is time series data"](https://www.influxdata.com/what-is-time-series-data/) | 20 |
| 3.3.2 | Block storage | VM disks (Azure Managed Disks); the substrate databases and VMs sit on | [Azure Managed Disks overview](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview) | 15 |
| 3.3.3 | File storage | NFS/SMB shares (Azure Files) for legacy app integration and lift-and-shift workloads | [Azure Files introduction](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction) | 15 |
| 5.1.1 | Visual ETL suites | Informatica/SSIS/DataStage — the installed base you'll meet across EU financial services | [Informatica PowerCenter product page](https://www.informatica.com/products/data-integration/powercenter.html) | 25 |
| 9.10.3 | Configuration management | Ansible/Chef VM-era config; mostly displaced by immutable containers but alive in on-prem banks | [Ansible "Getting started"](https://docs.ansible.com/ansible/latest/getting_started/index.html) | 20 |
| 12.1.2 | Enterprise backup suites | Veeam/Commvault/Rubrik estates protecting on-prem bank infrastructure | [Veeam Data Platform overview](https://www.veeam.com/products/veeam-data-platform.html) | 15 |
| 12.2.1 | DR tooling | Azure Site Recovery/Zerto for orchestrated failover of VM and on-prem workloads | [Azure Site Recovery overview](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview) | 20 |
| 12.5.1 | On-call/paging | PagerDuty/Opsgenie rotations & escalation that route incidents to a human | [PagerDuty on-call management](https://www.pagerduty.com/platform/incident-management/on-call-management/) | 15 |
| 12.5.2 | Postmortems | Blameless incident review that fixes systems, not people | [Google SRE: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) | 30 |
| 12.6.1 | Capacity planning | Forecasting growth against provisioning so the platform neither starves nor wastes | [Google SRE: Software Engineering in SRE (Auxon/capacity planning)](https://sre.google/sre-book/software-engineering-in-sre/) | 20 |
| 12.7.1 | Commercial APM | Datadog/Dynatrace full-stack suites — the build-vs-buy alternative to the OTel stack | [Datadog product overview](https://www.datadoghq.com/product/) | 15 |
| 14.7.3 | Notification tools | Routing data-signal alerts to paging/chat from observability tooling | [Grafana alerting: contact points](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/) | 10 |

*T3 subtotal: 4.5 h*

### Capstone 5 — IaC-provisioned platform on Kubernetes + Well-Architected review

- **Goal:** the platform becomes infrastructure-as-code on a cloud-shaped runtime, with observability, a DR position, and a cost model — everything an architecture review board would demand.
- **Stack (100% free):** [kind](https://kind.sigs.k8s.io/docs/) or [k3d](https://k3d.io/) local Kubernetes (↔ AKS), [Helm](https://helm.sh/docs/) charts for [Kafka](https://kafka.apache.org/documentation/)/[Flink](https://nightlies.apache.org/flink/flink-docs-stable/)/[Trino](https://trino.io/docs/current/)/[Dagster](https://docs.dagster.io/)/[MinIO](https://min.io/docs/minio/kubernetes/upstream/)/[Postgres](https://www.postgresql.org/docs/) (↔ managed PaaS equivalents), [OpenTofu](https://opentofu.org/docs/) with kubernetes/helm/azurerm providers (↔ Terraform Enterprise), [Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/) comparison module, [OpenBao](https://openbao.org/docs/) (↔ [Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)), [OTel](https://opentelemetry.io/docs/) + [Prometheus](https://prometheus.io/docs/) + [Grafana](https://grafana.com/docs/grafana/latest/) + [Loki](https://grafana.com/docs/loki/latest/) (↔ [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/)), [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) + free-trial `tofu plan` (no spend).
- **Build:** (1) migrate the compose stack to kind via Helm, OpenTofu-managed end to end; (2) secrets via OpenBao with documented rotation; (3) full observability: traces through one pipeline run, platform dashboard, two alerts (freshness, consumer lag); (4) azurerm module expressing the target Azure architecture (landing-zone slice: VNet/Private Link per A.3, ADLS, AKS, Event Hubs, Key Vault) — validated plan-only; (5) WAF review of the result (one finding per pillar, remediated or accepted in writing); (6) DR design + tabletop drill; (7) monthly cost model at 1×/10×.
- **Architecture deliverables:** C4 deployment diagram (new level for this phase); ADR-013 Kubernetes vs managed-PaaS-per-service, ADR-014 OpenTofu vs Bicep for this estate, ADR-015 DR topology per data tier.
- **Acceptance criteria:** fresh machine → `tofu apply` → healthy platform → one full pipeline run → `tofu destroy`, all documented; seeded failure diagnosed from dashboards in <5 min; WAF review yields ≥5 genuine findings with dispositions; cost model withstands a "what if volumes 10×?" challenge; DR drill writeup names RTO/RPO per tier.
- Est. hours: 18

*Phase 5 total: 107.5 h (T1/T2 entries 85 h + T3 4.5 h + capstone 18 h) + Appendix A items A.3–A.6, A.22, A.25, A.26 (37 h) scheduled in this phase*
