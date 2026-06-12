<a id="phase-4"></a>
## Phase 4: Streaming & Event-Driven Integration (months 22–27, 119 h)

**Goal:** close the streaming gap end-to-end: Kafka as the integration backbone, CDC off operational systems, the Beam-model semantics (event time, watermarks, windows), Flink for stateful processing, schema governance on the wire, and the event-driven patterns (outbox, saga, event sourcing) that regulated trade lifecycles are built from.
**Entry prerequisites:** Phases 1–3 (integration-pattern theory from DDIA; lakehouse + orchestrator to land streams into).
**Exit criteria:** you can (1) design a CDC-to-lakehouse flow with stated delivery guarantees and prove them; (2) explain watermarks well enough to debug a wrong window result; (3) own a schema-compatibility policy and show the registry enforcing it; (4) choose among Kafka/Event Hubs/Service Bus/Temporal/Camunda for a given fund workflow and defend it.

### T1/T2 topics

#### 2.4.1 Distributed logs (Kafka) — T1
- **Why:** Kafka is the backbone of modern financial data integration; the architect sizes it, secures it, sets its guarantees, and debugs it when settlement events go missing.
- **Learn:** log abstraction: topics, partitions, offsets, segments, retention/compaction; producers: acks, idempotent producer, transactions; consumers: groups, rebalancing (cooperative), lag; replication: ISR, min.insync.replicas, unclean elections; KRaft (no more ZooKeeper); partitioning/key design and ordering guarantees; compacted topics as changelog tables; Kafka-API-compatible alternatives (Redpanda) and Azure Event Hubs Kafka surface.
- **Resource:** *Kafka: The Definitive Guide* 2nd ed. (free PDF via Confluent), ch. 1–7 + 10 (cross-cluster) — skim ops chapters.
- **Tools:** FOSS: Apache Kafka or Redpanda in compose (↔ Confluent Cloud, Azure Event Hubs, AWS MSK) · Corp: Confluent Cloud & Event Hubs (evaluation level: pricing units, quotas, Kafka-compat limits).
- **Do:** stand up single-broker KRaft Kafka; produce fund-order events keyed by ISIN; demonstrate ordering per key, consumer-group rebalance behavior, and a compacted `fund-reference` topic serving as a table.
- **Done when:** you can answer "can we lose or duplicate an order event?" for a given producer/consumer config matrix, correctly, every time.
- Est. hours: 14

#### 1.8.2 Delivery semantics (at-most/at-least/exactly-once) — T1
- **Why:** "exactly-once" claims must be audited, not believed, when the payload is a settlement instruction or a NAV correction.
- **Learn:** what each guarantee costs; where duplication enters (producer retry, consumer reprocess); Kafka EOS: idempotent producer + transactions + read_committed — and its boundaries (within-Kafka, not end-to-end); end-to-end exactly-once = at-least-once + idempotent/transactional sink; the Flink two-phase-commit sink connection.
- **Resource:** *Kafka: The Definitive Guide* ch. 8 (exactly-once semantics) + Confluent EOS blog series (verify link at assembly).
- **Do:** kill your consumer mid-batch in three configurations (auto-commit, manual commit-after-process, transactional) and tabulate observed duplicates/losses against prediction.
- **Done when:** you can mark, on any pipeline diagram, every point where the guarantee degrades and what restores it.
- Est. hours: 4

#### 2.3.1 + 1.8.10 Log-based CDC (Debezium) — T1
- **Why:** CDC is how regulated estates go event-driven without touching fragile core systems — the highest-leverage integration pattern in the fund back office.
- **Learn:** logical decoding (Postgres WAL → events); Debezium architecture on Kafka Connect; snapshot modes and re-snapshotting; event envelope (before/after/op/ts, tombstones); schema-change events; ordering & transaction boundaries downstream; outbox-via-CDC; delivery guarantees of the whole chain; landing CDC into Iceberg (merge vs append+dedupe).
- **Resource:** Debezium official documentation (architecture + Postgres connector + outbox event router). *Alternate:* DDIA ch. 11 (rereading "keeping systems in sync" with practitioner eyes).
- **Tools:** FOSS: Debezium + Kafka Connect (↔ Qlik Replicate, GoldenGate, ADF CDC, Fivetran HVR) · Corp: Qlik Replicate / GoldenGate (the EU bank incumbents; evaluation level).
- **Do:** stream the Phase-1 Postgres `orders` and `nav` tables through Debezium into Kafka, land them in Iceberg via a merge job, and prove end-state equality after a mid-stream connector restart.
- **Done when:** you can explain to an auditor why the lakehouse copy is complete and ordered, including the restart story.
- Est. hours: 9

#### 2.2.2 Stream connectors (Kafka Connect) — T2
- **Why:** Connect is the operational workhorse around Kafka — connectors, converters, and transforms are where streaming integrations actually live or die.
- **Learn:** workers/tasks/distributed mode; source vs sink connectors; converters (Avro/JSON/Protobuf) vs SMTs; offset management; error handling + DLQ topics; connector operations (pause/resume/restart).
- **Resource:** Kafka Connect official documentation (concepts + worker config).
- **Tools:** FOSS: Kafka Connect (↔ Confluent managed connectors, Event Hubs Capture).
- **Do:** configure an S3/MinIO sink connector with DLQ; poison one message and show it parked with headers explaining why.
- **Done when:** you can size a Connect cluster (workers/tasks) for a given connector load and explain failure recovery.
- Est. hours: 4

#### 8.3.1 + 8.3.2 + 1.11.2 Schema registry, schema languages & serialization — T2
- **Why:** the registry is the contract-enforcement point of the streaming estate; Avro vs Protobuf vs JSON Schema is a recurring standards decision the architect owns.
- **Learn:** registry model (subjects, versions, compatibility levels); Avro: schemas, logical types, evolution rules; Protobuf: field numbers, unknown fields; JSON Schema's weaker evolution story; wire format (magic byte + schema ID); subject naming strategies; Apicurio vs Confluent SR licensing.
- **Resource:** Confluent Schema Registry docs (fundamentals + compatibility) + Avro spec (evolution section).
- **Tools:** FOSS: Apicurio or Confluent SR Community (↔ Confluent Cloud SR, Azure Schema Registry, AWS Glue SR).
- **Do:** register the fund-order schema in Avro; evolve it three ways (add optional, rename, type change) under `BACKWARD` and `FULL` modes; record what the registry rejects and why.
- **Done when:** you can write the org's schema-evolution policy and justify each compatibility level per topic class.
- Est. hours: 6

#### 1.9.7 Schema evolution compatibility (the policy) — T1
- **Why:** forward/backward compatibility is a governance decision with org-wide blast radius — the architect writes this policy and arbitrates exceptions.
- **Learn:** backward/forward/full/transitive semantics precisely; who upgrades first (consumers vs producers) under each; default-value discipline; breaking-change playbook (new subject vs dual-write vs upcaster); how the same policy applies to Iceberg table schemas and API payloads — one mental model across batch, stream, and API.
- **Resource:** Confluent compatibility docs + Iceberg schema-evolution docs (read as one policy domain).
- **Do:** write a one-page "Schema Evolution Policy" covering Kafka topics, Iceberg tables, and REST payloads: levels, exception process, breaking-change playbook.
- **Done when:** given any proposed field change, you can rule allow/deny/migrate in under a minute, with the rule cited.
- Est. hours: 4

#### 1.9.1 + 1.9.2 + 1.9.4 (with 1.9.3, 1.9.5, 1.9.6) Streaming semantics — the Beam model — T1
- **Why:** event time, watermarks, and windows are the conceptual machinery that make streaming results *correct*, not just fast — and restatement-heavy finance demands event-time rigor.
- **Learn:** event time vs processing time; the what/where/when/how framing; windowing (tumbling/sliding/session); watermarks: perfect vs heuristic, propagation, and why they're a tradeoff between latency and completeness; triggers & accumulation modes; late data: allowed lateness, side outputs, restatements; stateful processing: keyed state, checkpoints (T2 depth, deepened in Flink below).
- **Resource:** Akidau et al., *Streaming Systems*, ch. 1–4 (+ ch. 7 state, skim) — the canonical text, per the taxonomy.
- **Do:** on paper (Beam-model diagrams), design the windowing/watermark/trigger strategy for "intraday fund-flow totals per share class, restated as late orders arrive" — then implement it in Flink in the next entry.
- **Done when:** you can explain to a junior why a count was wrong yesterday and exactly which knob (watermark, lateness, trigger) fixes it — and what that costs.
- Est. hours: 10

#### 4.2.1 Stateful stream processing (Flink) — T1
- **Why:** Flink is the reference stateful engine (and what AWS/Azure managed streaming runs underneath); real-time NAV estimates and exposure monitoring are Flink-shaped problems.
- **Learn:** dataflow graph, keyed streams, state backends (RocksDB); checkpointing & exactly-once internals (aligned barriers, unaligned); event-time operators: window/process functions, timers; watermark strategies in code; Flink SQL & Table API; savepoints, upgrades, state evolution; Kafka source/sink with EOS; Spark Structured Streaming compared (micro-batch model, when it's enough).
- **Resource:** Flink official docs ("Learn Flink" track + "Stateful Stream Processing" concepts) — current and free; book alternatives are dated.
- **Tools:** FOSS: Apache Flink (↔ AWS Managed Flink, Azure HDInsight/Flink, Confluent Flink, GCP Dataflow) · Corp: Confluent Flink SQL / Azure Stream Analytics (evaluation level).
- **Do:** implement the 1.9 design: Flink job consuming order events, computing per-share-class windowed flow totals with heuristic watermarks, allowed lateness + side output for stragglers, checkpointed to MinIO, EOS into Iceberg; kill/restore from checkpoint and savepoint-upgrade once.
- **Done when:** the restored job produces byte-identical results, and you can narrate the checkpoint barrier mechanism from memory.
- Est. hours: 14

#### 1.8.3 + 1.8.4 Outbox & saga (implemented) — T1
- **Why:** dual-write is the classic event-driven corruption bug and sagas are the bedrock of multi-service trade lifecycles — these two patterns turn theory into production-shaped reflexes.
- **Learn:** outbox: same-transaction event capture, Debezium outbox router, idempotent consumers; saga: choreography vs orchestration, compensation design, isolation anomalies (dirty compensations), timeout/dead-man handling; where Temporal/Camunda fit as saga orchestrators; Azure Cloud Design Patterns catalog entries for both.
- **Resource:** microservices.io pattern pages (Outbox, Saga) + Azure Architecture Center pattern catalog (Saga) — https://learn.microsoft.com/en-us/azure/architecture/patterns/.
- **Do:** add an outbox table to the Phase-1 order service; route it through Debezium's outbox SMT; build a 3-step subscription saga (reserve cash → book units → confirm) with a deliberate step-2 failure compensating cleanly.
- **Done when:** the saga's failure path leaves the system consistent and the audit log tells the whole story without manual digging.
- Est. hours: 7

#### 1.8.5 + 1.8.6 Event sourcing & CQRS — T1/T2
- **Why:** audit-by-construction (1.8.5, T1) is the killer feature for regulated finance — the event log *is* the regulator's evidence; CQRS (1.8.6, T2) is its usual companion and over-application hazard.
- **Learn:** state as fold over events; commands vs events; snapshots; replay & temporal queries ("position as-known-at"); schema evolution of events (upcasting); when ES is wrong (CRUD apps, weak invariants); CQRS read models from the event log; eventual consistency between write/read sides; the Kafka-as-event-store debate (and its caveats).
- **Resource:** Stopford, *Designing Event-Driven Systems* (free Confluent PDF), ch. on event sourcing/CQRS + Fowler's Event Sourcing essay.
- **Do:** event-source the share-register: order/allocation/transfer events → fold to positions; answer "investor X's position as known on date D" from replay; write a half-page ADR on where ES applies in a TA system and where it must not.
- **Done when:** you can defend the as-known-at vs as-of distinction (bitemporality) with a fund example, and say no to ES somewhere.
- Est. hours: 5

#### 1.8.7 + 1.8.8 Dead-letter queues & backpressure — T2
- **Why:** these two decide whether a bad message or a slow consumer takes down the flow or just a metric.
- **Learn:** DLQ design: park with diagnostic headers, replay procedure, poison-pill detection; backpressure: bounded buffers, consumer lag as signal, Flink's credit-based flow control; alerting on lag/DLQ depth.
- **Resource:** Confluent error-handling blog/docs + Flink network-stack docs section (backpressure monitoring).
- **Do:** define the DLQ + replay runbook for the CDC pipeline (who triages, how to replay safely, idempotency requirement).
- **Done when:** a poisoned message at 2am pages no one and is replayable at 9am without data loss.
- Est. hours: 2.5

#### 2.4.2 Message brokers vs logs — T2
- **Why:** queue semantics (RabbitMQ/Service Bus) and log semantics (Kafka) solve different problems; picking wrong is expensive in both directions.
- **Learn:** competing consumers vs consumer groups; per-message ack/redelivery vs offsets; routing (exchanges) vs partitioning; when a queue wins (task distribution, request/reply, per-message TTL) vs a log (replay, fan-out, ordering, retention); AMQP basics; Azure Service Bus as the corp queue.
- **Resource:** RabbitMQ "Concepts" docs + a queue-vs-log comparison from the Kafka guide ch. 1.
- **Tools:** FOSS: RabbitMQ (↔ Azure Service Bus, AWS SQS) — short hands-on only.
- **Do:** decision table: 6 fund-platform messaging needs → queue or log, one line of why each.
- **Done when:** you never propose Kafka for request/reply or RabbitMQ for replayable integration again.
- Est. hours: 3

#### 5.6.4 Durable execution (Temporal) — T2
- **Why:** trade lifecycle, KYC, and corporate-actions workflows are long-running, stateful, and retry-heavy — durable execution is the modern saga orchestrator and FS adoption is real.
- **Learn:** workflow-as-code model: deterministic workflow code, activities, event-history replay; retries/timeouts/heartbeats; signals & queries; versioning running workflows; where Temporal vs a BPM engine vs a queue fits; Azure Durable Functions as the corp-native analogue.
- **Resource:** Temporal docs ("Core concepts" + Python SDK tutorial).
- **Tools:** FOSS: Temporal OSS in compose (↔ Temporal Cloud, Azure Durable Functions, AWS Step Functions).
- **Do:** reimplement the Phase-4 saga as a Temporal workflow with retries and a compensation path; kill the worker mid-run and watch it resume.
- **Done when:** you can explain event-history replay and why workflow code must be deterministic.
- Est. hours: 4

#### 5.6.5 BPM / process orchestration (Camunda, BPMN/DMN) — T2
- **Why:** banks and fund administrators run BPMN engines for settlement, onboarding, and exception handling; the architect must speak BPMN/DMN and know when model-driven beats code-driven orchestration.
- **Learn:** BPMN 2.0 working subset: tasks, gateways, events (timer/message/error), pools/lanes; DMN decision tables + FEEL; Camunda 7 vs 8/Zeebe architecture & licensing; human-task workflows and exception queues; BPM vs Temporal vs Airflow — three orchestration species, one decision framework.
- **Resource:** Camunda 8 docs (BPMN + DMN references) + bpmn.io tutorials.
- **Tools:** FOSS: Camunda (Zeebe) or Flowable (↔ Camunda Enterprise, Pega, IBM BPM).
- **Do:** model the subscription-order lifecycle in BPMN with an error-handling path to a human task; encode the "compliance review required?" rule as a DMN table; run both in Camunda.
- **Done when:** you can defend orchestration-tool choice (BPM vs durable execution vs scheduler) for three different fund workflows.
- Est. hours: 5

#### 1.11.1 + 1.11.3 Data protocols & async API standards — T2
- **Why:** protocol literacy (gRPC vs REST vs Arrow Flight; AsyncAPI/CloudEvents) is the architect's interface-design toolkit across the estate.
- **Learn:** gRPC/HTTP2 + Protobuf contract-first; REST maturity in practice; Arrow Flight/ADBC for bulk analytical transfer (vs JDBC/ODBC row-marshaling); WebSocket/MQTT/AMQP placement; AsyncAPI as OpenAPI-for-events; CloudEvents envelope; SOAP/OData literacy for the legacy estate you'll meet.
- **Resource:** AsyncAPI docs (concepts) + Arrow Flight introduction + CloudEvents spec overview.
- **Do:** write the AsyncAPI document for your fund-order Kafka topics (channels, messages, schemas) and render its docs.
- **Done when:** you can pick the transfer protocol for: BI extract, microservice call, market-data feed, file drop — with numbers, not vibes.
- Est. hours: 3

#### 1.4.1 + 1.4.2 Lambda vs Kappa — T2
- **Why:** the batch/speed-layer debate frames every "do we need streaming?" conversation; medallion-with-streaming is today's synthesis.
- **Learn:** Lambda's dual-codebase tax; Kappa's replay-the-log answer and its storage/retention implications; how table formats + streaming ingestion (your Phase-2/4 stack) dissolve most of the dichotomy.
- **Resource:** Kreps' "Questioning the Lambda Architecture" (O'Reilly radar essay) + *Streaming Systems* ch. 1 framing.
- **Do:** one-page position note: which architecture your capstone platform actually is, and why that's the right call for fund data.
- **Done when:** you can articulate what you'd change if regulators demanded sub-minute NAV-error detection.
- Est. hours: 2

#### 1.2.2 + 1.2.3 Micro-batch vs true streaming — T2
- **Why:** Spark Structured Streaming (micro-batch) vs Flink (event-at-a-time) is a real engine decision with latency, state, and ops consequences.
- **Learn:** micro-batch mechanics & latency floor; continuous processing; state handling differences; ops profile (Spark cluster reuse vs Flink job clusters); decision rubric by latency class (minutes/seconds/sub-second).
- **Resource:** Spark Structured Streaming programming guide (overview) read against Flink's "Stateful Stream Processing" concepts page.
- **Do:** rebuild one Flink aggregation in Spark Structured Streaming on the existing cluster; compare latency, code, and ops burden in a half-page note.
- **Done when:** you can place any fund use case in the right latency class and name the engine.
- Est. hours: 3

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.2.4 | Real-time / low-latency paradigm | Sub-second serving paths; mostly out of fund-admin scope | *Streaming Systems* ch. 1 sidebar | 15 |
| 1.3.4 | RT / user-facing analytics workload | High-concurrency sub-second dashboards (Pinot/Druid class) | StarTree "what is user-facing analytics" blog | 25 |
| 1.8.12 | Bulkhead | Resource isolation so one consumer can't sink the ship | Azure patterns catalog: Bulkhead | 15 |
| 1.8.13 | Circuit breaker | Fail-fast wrapper for flaky dependencies | Azure patterns catalog: Circuit Breaker | 15 |
| 2.3.2 | Trigger-based CDC | DB triggers populate change tables; intrusive legacy approach | Debezium FAQ comparison section | 15 |
| 2.3.3 | Snapshot-based CDC | Periodic diffing (Fivetran-style); simple, lossy between snapshots | Fivetran docs: sync modes | 15 |
| 2.4.3 | Event mesh | Federated brokers across sites/clouds (Solace; big in capital markets) | Solace "what is an event mesh" page | 25 |
| 4.3.4 | RT analytics engines | Pinot/Druid/ClickHouse serving layer for 1.3.4 workloads | Pinot docs intro | 25 |
| 4.3.5 | Streaming databases | Incrementally-maintained materialized views (Materialize/RisingWave) | RisingWave "why" docs page | 25 |

*T3 subtotal: 3 h*

### Capstone 4 — Real-time fund-flow & price CDC streaming

- **Goal:** the platform gains a streaming spine: operational changes flow as events, stateful aggregations stay correct under late data, and every guarantee is stated and demonstrated.
- **Stack (100% free):** Kafka KRaft or Redpanda (↔ Confluent Cloud / Event Hubs), Kafka Connect + Debezium with outbox router (↔ Qlik Replicate / GoldenGate / ADF), Apicurio or Confluent SR with Avro (↔ Confluent Cloud SR / Azure Schema Registry), Flink (↔ Confluent Flink / Managed Flink / ASA), Iceberg sink on MinIO, Temporal saga + Camunda BPMN process from the entries above, Dagster supervising batch reconciliation, all in compose.
- **Build:** (1) Debezium streams orders/NAV + the outbox topic; (2) Flink computes per-share-class windowed flow totals (heuristic watermarks, allowed lateness, late-event side output) exactly-once into Iceberg; (3) nightly Dagster batch reconciles streamed totals against batch recompute and alerts on drift; (4) schema registry enforces the 1.9.7 policy (one rejected evolution kept as evidence); (5) the subscription saga (Temporal) and BPMN process (Camunda) run against the same events; (6) chaos drills: kill broker, connector, Flink job — document recovery and guarantee held.
- **Architecture deliverables:** C4 updated with the streaming spine; ADR-010 log platform choice (Kafka vs Event Hubs vs Redpanda), ADR-011 delivery-guarantee design (where exactly-once is real and where idempotent-at-least-once is the honest answer), ADR-012 orchestration species (BPM vs durable execution vs scheduler, per workflow).
- **Acceptance criteria:** reconciliation drift = 0 over a 3-day simulated run incl. injected late/duplicate events; each chaos drill has a written recovery narrative naming the mechanism (ISR, checkpoint, offset commit); schema policy violation is blocked by the registry and the evidence archived; saga failure path leaves consistent state with full audit trail.
- Est. hours: 16

*Phase 4 total: 119 h (T1/T2 entries 99.5 h + T3 3 h + capstone 16 h ≈ 119)*
