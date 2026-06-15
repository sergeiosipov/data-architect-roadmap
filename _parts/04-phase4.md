<a id="phase-4"></a>
## Phase 4: Streaming & Event-Driven Integration (months 22–27, 119 h)

*Phase 4 of 8 · months 22–27 · 119 h · capstone: Real-time price/flow CDC streaming.*  ← [Phase 3](#phase-3) · [Phase 5](#phase-5) →

**Goal:** close the streaming gap end-to-end: Kafka as the integration backbone, CDC off operational systems, the Beam-model semantics (event time, watermarks, windows), Flink for stateful processing, schema governance on the wire, and the event-driven patterns (outbox, saga, event sourcing) that regulated trade lifecycles are built from.
**Entry prerequisites:** Phases 1–3 (integration-pattern theory from DDIA; lakehouse + orchestrator to land streams into).
**Exit criteria:** you can (1) design a CDC-to-lakehouse flow with stated delivery guarantees and prove them; (2) explain watermarks well enough to debug a wrong window result; (3) own a schema-compatibility policy and show the registry enforcing it; (4) choose among Kafka/Event Hubs/Service Bus/Temporal/Camunda for a given fund workflow and defend it.

### T1/T2 topics

#### 2.4.1 Distributed logs (Kafka) — T1
- **Why:** Kafka is the backbone of modern financial data integration, and as architect you size it, secure it, set its guarantees, and debug it when settlement events go missing. Get partitioning or replication wrong and you silently reorder trade events or lose an entire broker's worth of unflushed orders — the kind of failure auditors trace back to a design decision, not an operator. Knowing the log abstraction cold is what lets you answer capacity, durability, and ordering questions in a design review without hand-waving.
- **Learn:**
    - the log abstraction — topics, partitions, offsets, segments, and retention vs compaction as two different cleanup policies *(Kafka docs: Design)*
    - producer semantics — acks=all, the idempotent producer, and transactions, and what each buys for ordering and duplicates *(Kafka docs: Design — message delivery semantics)*
    - consumer groups — partition assignment, cooperative-sticky rebalancing, and lag as the core health signal *(Kafka docs: Implementation — consumer)*
    - replication internals — ISR, min.insync.replicas, and why unclean leader election trades durability for availability *(Kafka docs: Design — replication)*
    - KRaft mode — the metadata quorum replacing ZooKeeper, and why single-binary clusters are now the norm *(Kafka docs: KRaft)*
    - key design and ordering — ordering is per-partition only, so the partition key is a data-model decision (ISIN here) *(Kafka: Definitive Guide ch. 3–4)*
    - compacted topics as tables — a changelog topic keyed by entity becomes a queryable reference table *(Kafka: Definitive Guide ch. 6)*
    - API-compatible alternatives — Redpanda and the Event Hubs Kafka surface, where compatibility ends *(Kafka: Definitive Guide ch. 1)*
- **Resources:**
    - **[Kafka: The Definitive Guide, 2nd ed. (free via Confluent)](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/)** ch. 1–7 + 10 (cross-cluster) — the practitioner narrative on producers, consumers, replication, and ops (primary)
    - [Apache Kafka documentation](https://kafka.apache.org/documentation/) — Design, Implementation, and KRaft sections; the authoritative semantics you cite in reviews (reference)
- **Tools:**
    - FOSS (hands-on): [Apache Kafka](https://kafka.apache.org/documentation/) — single-broker KRaft cluster in compose is the whole lab (↔ Confluent Cloud / Event Hubs / MSK)
    - FOSS (hands-on): [Redpanda](https://docs.redpanda.com/) — drop-in Kafka-API broker, lighter to run locally (↔ Confluent Cloud)
    - Corp (evaluate): [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/) — Kafka-compat surface, throughput units, partition limits at build-vs-buy level
- **Do:**
    1. Stand up a single-broker KRaft Kafka (no ZooKeeper) in compose and create a `fund-orders` topic with 3 partitions.
    2. Produce order events keyed by ISIN and prove ordering holds per key but not across partitions.
    3. Run two consumers in one group; trigger a cooperative rebalance and observe which partitions move and how lag behaves.
    4. Create a compacted `fund-reference` topic, write several updates per ISIN, and show only the latest survives compaction — a table served from a log.
- **Done when:**
    - [ ] You can answer "can we lose or duplicate an order event?" for a given producer/consumer config matrix, correctly, every time.
    - [ ] You can state the ordering guarantee for a given key and partition count and justify the partition key choice.
    - [ ] You can explain what min.insync.replicas plus acks=all costs and protects against.
- Est. hours: 14

#### 1.8.2 Delivery semantics (at-most/at-least/exactly-once) — T1
- **Why:** "exactly-once" claims must be audited, not believed, when the payload is a settlement instruction or a NAV correction. As architect you sign off on guarantee diagrams, and a single mislabelled edge — claiming exactly-once where it is really at-least-once into a non-idempotent sink — becomes a duplicated settlement that compliance discovers downstream. The skill is reading any pipeline and marking precisely where the guarantee holds, degrades, and is restored.
- **Learn:**
    - the three guarantees and their cost — at-most-once (may lose), at-least-once (may duplicate), exactly-once (expensive) *(Kafka docs: Design — message delivery semantics)*
    - where duplication enters — producer retries and consumer reprocess after a crash before commit *(Kafka: Definitive Guide ch. 8)*
    - Kafka EOS mechanics — idempotent producer + transactions + read_committed consumers, and that it is within-Kafka only *(Kafka: Definitive Guide ch. 8)*
    - end-to-end exactly-once — at-least-once delivery plus an idempotent or transactional sink, framed as effectively-once *(Streaming Systems ch. 5)*
    - the two-phase-commit sink — how Flink coordinates a transactional sink with checkpoints *(Flink docs: Stateful Stream Processing)*
- **Resources:**
    - **[Kafka: The Definitive Guide, 2nd ed. (free via Confluent)](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/)** ch. 8 "Exactly-Once Semantics" — the canonical walk-through of idempotent producer and transactions (primary)
    - [Apache Kafka documentation: message delivery semantics](https://kafka.apache.org/documentation/#semantics) — the authoritative definition of each guarantee (reference)
    - [Streaming Systems](https://www.streamingsystems.net/) ch. 5 — effectively-once across the whole pipeline, not just the broker (deepening)
- **Do:**
    1. Build a small consumer that writes each order to a downstream store, in three configurations: auto-commit, manual commit-after-process, and Kafka transactional EOS.
    2. Kill the consumer mid-batch in each configuration and restart it.
    3. Tabulate observed duplicates and losses against your prediction for each configuration.
    4. Mark on a diagram exactly where the guarantee degrades when the downstream store is not idempotent.
- **Done when:**
    - [ ] You can mark, on any pipeline diagram, every point where the guarantee degrades and what restores it.
    - [ ] You can explain why Kafka EOS is within-Kafka and what an end-to-end claim additionally requires.
    - [ ] Your duplicate/loss tabulation matches your prior prediction for all three configs.
- Est. hours: 4

#### 2.3.1 + 1.8.10 Log-based CDC (Debezium) — T1
- **Why:** CDC is how regulated estates go event-driven without touching fragile core systems — it is the highest-leverage integration pattern in the fund back office, turning a transfer-agency database into an event stream nobody had to re-engineer. Get the snapshot, ordering, or restart story wrong and the lakehouse copy silently diverges from the source of record, which is exactly the discrepancy an auditor will surface. The architect must be able to prove completeness and ordering of the whole chain, including after a connector crash.
- **Learn:**
    - logical decoding — how Postgres WAL becomes a stream of row-level change events *(Debezium docs: Postgres connector)*
    - Debezium on Kafka Connect — connectors, tasks, and offset storage as the runtime *(Debezium docs: Architecture)*
    - snapshot modes — initial vs incremental snapshots and when a re-snapshot is forced *(Debezium docs: Postgres connector)*
    - the change envelope — before/after/op/ts_ms fields and tombstones for deletes *(Debezium docs: Architecture)*
    - schema-change events and ordering — per-table ordering and transaction boundaries downstream *(Debezium docs: Postgres connector)*
    - outbox-via-CDC — capturing an application's outbox table as the event source *(Debezium docs: Outbox Event Router)*
    - landing into Iceberg — merge (upsert) vs append-plus-dedupe for the lakehouse copy *(DDIA ch. 11)*
- **Resources:**
    - **[Debezium reference documentation](https://debezium.io/documentation/reference/stable/index.html)** — architecture, the [Postgres connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html), and the [outbox event router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) (primary)
    - [Designing Data-Intensive Applications](https://dataintensive.net/) ch. 11 "Stream Processing" — "keeping systems in sync" reread with practitioner eyes (deepening)
- **Tools:**
    - FOSS (hands-on): [Debezium](https://debezium.io/documentation/reference/stable/index.html) + [Kafka Connect](https://kafka.apache.org/documentation/#connect) — the CDC capture and transport layer (↔ Qlik Replicate / GoldenGate / ADF CDC / Fivetran HVR)
    - Corp (evaluate): [Qlik Replicate](https://www.qlik.com/us/products/qlik-replicate) — an EU-bank incumbent; what to know at build-vs-buy level
    - Corp (evaluate): [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/) — the other incumbent for heterogeneous CDC
- **Do:**
    1. Configure Debezium to capture the Phase-1 Postgres `orders` and `nav` tables into Kafka topics.
    2. Build a merge job that lands those change streams into Iceberg tables on MinIO (upsert on primary key, apply tombstones as deletes).
    3. Mid-stream, restart the Debezium connector and let it resume from its stored offset.
    4. Run a full row-by-row comparison and prove the Iceberg end-state equals the Postgres source after the restart.
- **Done when:**
    - [ ] You can explain to an auditor why the lakehouse copy is complete and ordered, including the restart story.
    - [ ] You can describe what triggers a re-snapshot and how it interacts with already-streamed changes.
    - [ ] Your post-restart comparison shows zero divergence between source and lakehouse.
- Est. hours: 9

#### 2.2.2 Stream connectors (Kafka Connect) — T2
- **Why:** Connect is the operational workhorse around Kafka — connectors, converters, and transforms are where streaming integrations actually live or die, and most CDC and sink plumbing in a fund estate runs on it. Misconfigure a converter or skip the DLQ and a single malformed market-data message stalls an entire connector at 2am. The architect must size Connect clusters and design their failure handling, not just wire up a connector once.
- **Learn:**
    - workers, tasks, and distributed mode — how Connect parallelises and rebalances work *(Kafka docs: Connect)*
    - source vs sink connectors — direction of flow and where offsets are tracked *(Kafka docs: Connect)*
    - converters vs SMTs — serialization (Avro/JSON/Protobuf) versus single-message transforms *(Kafka docs: Connect)*
    - offset management — how Connect stores progress and what an offset reset means *(Kafka docs: Connect)*
    - error handling and DLQ — tolerance settings and dead-letter topics with diagnostic headers *(Kafka: Definitive Guide ch. 9)*
    - connector operations — pause/resume/restart and what each does to in-flight tasks *(Kafka: Definitive Guide ch. 9)*
- **Resources:**
    - **[Apache Kafka documentation: Kafka Connect](https://kafka.apache.org/documentation/#connect)** — concepts, worker config, converters, and transforms (primary)
    - [Kafka: The Definitive Guide, 2nd ed. (free via Confluent)](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/) ch. 9 — Connect in practice, error handling and DLQ patterns (reference)
- **Tools:**
    - FOSS (hands-on): [Kafka Connect](https://kafka.apache.org/documentation/#connect) — distributed-mode workers running a MinIO sink (↔ Confluent managed connectors, Event Hubs Capture)
    - FOSS (hands-on): [MinIO](https://docs.min.io/index.html) — S3-compatible object store as the sink target (↔ Azure Blob / ADLS)
- **Do:**
    1. Run Connect in distributed mode and configure an S3/MinIO sink connector with a dead-letter topic enabled.
    2. Send a poison message (wrong schema) through the source topic.
    3. Show the bad record parked in the DLQ with headers explaining why it failed.
    4. Size the cluster: estimate workers and tasks for a stated connector load and write down the failure-recovery behaviour.
- **Done when:**
    - [ ] You can size a Connect cluster (workers/tasks) for a given connector load and explain failure recovery.
    - [ ] You can show a poisoned message parked in the DLQ with diagnostic headers.
    - [ ] You can explain what pause/resume/restart each do to running tasks and offsets.
- Est. hours: 4

#### 8.3.1 + 8.3.2 + 1.11.2 Schema registry, schema languages & serialization — T2
- **Why:** the registry is the contract-enforcement point of the streaming estate, and Avro vs Protobuf vs JSON Schema is a recurring standards decision the architect owns. Without a registry, a producer renaming a field silently breaks every downstream consumer and corrupts the NAV pipeline before anyone notices. Knowing the wire format and evolution rules is what lets you make the registry a hard gate rather than a suggestion.
- **Learn:**
    - the registry model — subjects, versions, and per-subject compatibility levels *(Confluent Schema Registry docs)*
    - Avro fundamentals — schemas, logical types (decimal/date), and field-level evolution rules *(Avro spec: Schema Resolution)*
    - Protobuf trade-offs — field numbers, unknown-field preservation, and forward-compat behaviour *(Confluent Schema Registry docs)*
    - JSON Schema's weaker story — why its evolution semantics are looser and riskier *(Confluent Schema Registry docs)*
    - the wire format — magic byte plus schema ID prefixing every payload *(Confluent Schema Registry docs)*
    - subject naming strategies — TopicName vs RecordName vs TopicRecordName and their blast radius *(Confluent Schema Registry docs)*
    - FOSS vs licensed registries — Apicurio vs Confluent SR licensing at build-vs-buy level *(Confluent Schema Registry docs)*
- **Resources:**
    - **[Confluent Schema Registry documentation](https://docs.confluent.io/platform/current/schema-registry/index.html)** — fundamentals, subjects/versions, wire format, and naming strategies (primary)
    - [Apache Avro specification](https://avro.apache.org/docs/1.12.0/specification/) — the Schema Resolution section is the authoritative evolution-rules reference (reference)
- **Tools:**
    - FOSS (hands-on): [Apicurio Registry](https://www.apicur.io/registry/docs/) — open-source registry with Confluent-compatible API (↔ Confluent Cloud SR / Azure Schema Registry / Glue SR)
    - Corp (evaluate): [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/index.html) — Community vs licensed editions and what the managed cloud adds
- **Do:**
    1. Register the fund-order schema in Avro against a subject with `BACKWARD` compatibility.
    2. Attempt three evolutions: add an optional field, rename a field, and change a field's type.
    3. Repeat under `FULL` compatibility and record which evolutions the registry accepts or rejects and the exact error.
    4. Inspect a serialized message and identify the magic byte and schema ID in the wire format.
- **Done when:**
    - [ ] You can write the org's schema-evolution policy and justify each compatibility level per topic class.
    - [ ] You can predict, before submitting, which of the three evolutions the registry will reject under each mode.
    - [ ] You can point to the schema ID inside a raw serialized record.
- Est. hours: 6

#### 1.9.7 Schema evolution compatibility (the policy) — T1
- **Why:** forward/backward compatibility is a governance decision with org-wide blast radius — the architect writes this policy and arbitrates exceptions across Kafka topics, Iceberg tables, and API payloads. Without one mental model, teams upgrade producers and consumers in the wrong order and break the EMT feed or a transfer-agency integration in production. The payoff is being able to rule allow/deny/migrate on any proposed field change in under a minute, with the rule cited.
- **Learn:**
    - the four semantics precisely — backward, forward, full, and the transitive variants across all versions *(Confluent docs: Schema Evolution & Compatibility)*
    - upgrade order — who upgrades first (consumers vs producers) under each compatibility mode *(Confluent docs: Schema Evolution & Compatibility)*
    - default-value discipline — why defaults are what make adding/removing fields safe *(Avro spec: Schema Resolution)*
    - the breaking-change playbook — new subject vs dual-write vs upcaster when a change is genuinely incompatible *(Confluent docs: Schema Evolution & Compatibility)*
    - one model across surfaces — the same rules govern Iceberg table evolution and REST payloads, not just Kafka *(Iceberg docs: Evolution)*
- **Resources:**
    - **[Confluent docs: Schema Evolution & Compatibility Types](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html)** — backward/forward/full/transitive defined precisely, with upgrade-order rules (primary)
    - [Apache Iceberg documentation: Evolution](https://iceberg.apache.org/docs/latest/evolution/) — schema and partition evolution as the table-side of the same policy (reference)
    - [Apache Avro specification](https://avro.apache.org/docs/1.12.0/specification/) — Schema Resolution rules that underpin default-value discipline (reference)
- **Do:**
    1. Write a one-page "Schema Evolution Policy" covering Kafka topics, Iceberg tables, and REST payloads.
    2. State the chosen compatibility level per topic class (reference data vs transactional events) and justify each.
    3. Define the exception process and a breaking-change playbook (new subject / dual-write / upcaster).
    4. Test the policy against five proposed field changes and record the allow/deny/migrate ruling with the rule cited for each.
- **Done when:**
    - [ ] Given any proposed field change, you can rule allow/deny/migrate in under a minute, with the rule cited.
    - [ ] Your policy explicitly covers Kafka, Iceberg, and REST under one model.
    - [ ] You can state the safe upgrade order (producer-first vs consumer-first) for each compatibility level.
- Est. hours: 4

#### 1.9.1 + 1.9.2 + 1.9.4 (with 1.9.3, 1.9.5, 1.9.6) Streaming semantics — the Beam model — T1
- **Why:** event time, watermarks, and windows are the conceptual machinery that make streaming results *correct*, not just fast — and restatement-heavy finance demands event-time rigor. A late trade that arrives after a window closes will quietly understate an intraday fund-flow total unless you have chosen the watermark, lateness, and trigger knobs deliberately. The architect must be able to explain why a count was wrong yesterday and which exact knob fixes it, and what that fix costs in latency.
- **Learn:**
    - event time vs processing time — the central distinction and why event time is the regulated-finance default *(Streaming Systems ch. 1)*
    - the what/where/when/how framing — transformations, windowing, triggers, accumulation as four questions *(Streaming Systems ch. 2)*
    - windowing types — tumbling, sliding, and session windows and when each fits a fund metric *(Streaming Systems ch. 1)*
    - watermarks — perfect vs heuristic, how they propagate, and the latency-vs-completeness tradeoff *(Streaming Systems ch. 3)*
    - triggers and accumulation — early/on-time/late firings and discarding vs accumulating vs retracting *(Streaming Systems ch. 2)*
    - late data handling — allowed lateness, side outputs, and restatements for corrected results *(Streaming Systems ch. 2)*
    - stateful processing preview — keyed state and checkpoints, deepened in the Flink entry below *(Streaming Systems ch. 7)*
- **Resources:**
    - **[Streaming Systems (Akidau, Chernyak, Lax)](https://www.streamingsystems.net/)** — ch. 1–4 plus ch. 7 (state, skim); the canonical, engine-agnostic treatment of the Beam model (primary)
    - [Apache Flink documentation: event-time and watermarks](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) — the same concepts in the engine you will implement them in (reference)
- **Do:**
    1. On paper, draw Beam-model diagrams (event-time axis, watermark line, window bounds) for "intraday fund-flow totals per share class, restated as late orders arrive".
    2. Choose the windowing type, watermark strategy, trigger, and accumulation mode and write one sentence justifying each.
    3. Annotate where a late order lands relative to the watermark and what the trigger does with it.
    4. State the latency cost of your allowed-lateness choice — what you give up to catch stragglers.
- **Done when:**
    - [ ] You can explain to a junior why a count was wrong yesterday and exactly which knob (watermark, lateness, trigger) fixes it — and what that costs.
    - [ ] You can distinguish event time from processing time with a fund example for each.
    - [ ] Your paper design names a concrete windowing/watermark/trigger/accumulation choice ready to implement in Flink.
- Est. hours: 10

#### 4.2.1 Stateful stream processing (Flink) — T1
- **Why:** Flink is the reference stateful engine (and what AWS/Azure managed streaming runs underneath), and real-time NAV estimates and exposure monitoring are Flink-shaped problems. Get checkpointing or state evolution wrong and a job restart produces different numbers than before the crash — unacceptable when those numbers feed a regulated NAV. The architect must be able to narrate the checkpoint-barrier mechanism from memory and reason about state backends, exactly-once sinks, and upgrades.
- **Learn:**
    - the dataflow graph — keyed streams, operators, and parallelism *(Flink docs: Stateful Stream Processing)*
    - state backends — heap vs RocksDB and the size/latency tradeoff *(Flink docs: Stateful Stream Processing)*
    - checkpointing and EOS internals — aligned vs unaligned barriers and how they enable exactly-once *(Flink docs: Stateful Stream Processing)*
    - event-time operators — window and process functions, timers, and watermark strategies in code *(Flink docs: Learn Flink)*
    - Flink SQL and Table API — the declarative path for windowed aggregations *(Flink docs: Learn Flink)*
    - savepoints and upgrades — state evolution and how to redeploy a job without losing state *(Flink docs: Stateful Stream Processing)*
    - Kafka source/sink with EOS — the two-phase-commit sink wiring *(Flink docs: Stateful Stream Processing)*
    - Spark Structured Streaming compared — the micro-batch model and when it is enough *(Spark Structured Streaming guide)*
- **Resources:**
    - **[Apache Flink documentation: Stateful Stream Processing](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/)** — checkpoints, barriers, state backends, exactly-once internals (primary)
    - [Apache Flink: Learn Flink track](https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/overview/) — guided hands-on for operators, timers, and watermarks (reference)
    - [Spark Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) — the micro-batch alternative for the comparison (alternate)
- **Tools:**
    - FOSS (hands-on): [Apache Flink](https://nightlies.apache.org/flink/flink-docs-stable/) — the stateful engine for the windowed flow-total job (↔ Managed Flink / HDInsight Flink / Confluent Flink / Dataflow)
    - Corp (evaluate): [Azure Stream Analytics](https://learn.microsoft.com/en-us/azure/stream-analytics/) — the Azure-native managed streaming option, at build-vs-buy level
- **Do:**
    1. Implement the 1.9 design: a Flink job consuming order events and computing per-share-class windowed flow totals with heuristic watermarks.
    2. Add allowed lateness plus a side output for stragglers; checkpoint state to MinIO.
    3. Write the results exactly-once into Iceberg via the transactional (two-phase-commit) sink.
    4. Kill the job and restore from checkpoint; separately, take a savepoint and perform one upgrade redeploy.
    5. Verify the restored job produces byte-identical results to the pre-crash run.
- **Done when:**
    - [ ] The restored job produces byte-identical results, and you can narrate the checkpoint barrier mechanism from memory.
    - [ ] You can explain aligned vs unaligned checkpoints and when each matters.
    - [ ] You can perform a savepoint-based upgrade without losing state.
- Est. hours: 14

#### 1.8.3 + 1.8.4 Outbox & saga (implemented) — T1
- **Why:** dual-write is the classic event-driven corruption bug and sagas are the bedrock of multi-service trade lifecycles — these two patterns turn theory into production-shaped reflexes. Without the outbox, a service that updates its database and then publishes an event can crash between the two and leave the order booked but never announced. Without a disciplined saga and compensation design, a half-completed subscription leaves cash reserved against units never issued — a reconciliation nightmare the architect must design out.
- **Learn:**
    - the outbox pattern — capture the event in the same transaction as the state change, relay separately *(microservices.io: Transactional Outbox)*
    - the Debezium outbox router — turning the outbox table into clean event topics *(Debezium docs: Outbox Event Router)*
    - idempotent consumers — deduplicating on event ID so replays are safe *(microservices.io: Transactional Outbox)*
    - choreography vs orchestration — distributed vs centrally-directed sagas and their trade-offs *(microservices.io: Saga)*
    - compensation design — semantic undo steps and the dirty-compensation anomaly *(microservices.io: Saga)*
    - timeouts and dead-man handling — what happens when a saga step never replies *(Azure patterns: Saga)*
    - where orchestrators fit — Temporal/Camunda as saga engines (previewing later entries) *(Azure patterns: Saga)*
- **Resources:**
    - **[microservices.io: Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html)** and [Saga](https://microservices.io/patterns/data/saga.html) — the canonical pattern pages with problem, solution, and trade-offs (primary)
    - [Azure Architecture Center: Saga pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) — the cloud-pattern framing and Azure service mapping (reference)
    - [Debezium documentation: Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — the concrete SMT you will wire up (reference)
- **Tools:**
    - FOSS (hands-on): [Debezium Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — relays the outbox table into Kafka topics (↔ application-level outbox relays)
    - FOSS (hands-on): [Apache Kafka](https://kafka.apache.org/documentation/) — the event backbone the saga coordinates over (↔ Event Hubs / Service Bus)
- **Do:**
    1. Add an outbox table to the Phase-1 order service and write events into it inside the same transaction as the order.
    2. Configure Debezium's outbox SMT to route those rows into event topics.
    3. Build a 3-step subscription saga: reserve cash → book units → confirm.
    4. Force a step-2 failure and implement compensation that releases the reserved cash cleanly.
    5. Verify the audit log alone explains the whole failure-and-compensation sequence.
- **Done when:**
    - [ ] The saga's failure path leaves the system consistent and the audit log tells the whole story without manual digging.
    - [ ] You can explain why the outbox eliminates the dual-write race.
    - [ ] Your consumers are idempotent and survive a replayed event without double-effect.
- Est. hours: 7

#### 1.8.5 + 1.8.6 Event sourcing & CQRS — T1/T2
- **Why:** audit-by-construction (1.8.5, T1) is the killer feature for regulated finance — the event log *is* the regulator's evidence, and "what was investor X's position as known on date D?" becomes a replay, not a forensic reconstruction. CQRS (1.8.6, T2) is its usual companion and its main over-application hazard: split read/write models everywhere and you inflict eventual consistency on teams that needed none. The architect must know exactly where event sourcing earns its complexity in a transfer-agency system and where it must not be used.
- **Learn:**
    - state as a fold over events — current state is derived, the event log is the source of truth *(Fowler: Event Sourcing)*
    - commands vs events — intent (may be rejected) vs fact (already happened) *(Designing Event-Driven Systems)*
    - snapshots — materialising state periodically so replay does not start from zero *(Fowler: Event Sourcing)*
    - replay and temporal queries — "position as-known-at date D" from the log *(Fowler: Event Sourcing)*
    - event schema evolution — upcasting old events to new shapes during replay *(Designing Event-Driven Systems)*
    - when ES is wrong — CRUD apps and weak-invariant domains where it adds only cost *(Designing Event-Driven Systems)*
    - CQRS read models — building query-optimised views off the event log, with eventual consistency *(Designing Event-Driven Systems)*
- **Resources:**
    - **[Designing Event-Driven Systems (Ben Stopford, free via Confluent)](https://www.confluent.io/designing-event-driven-systems/)** — the chapters on event sourcing, CQRS, and Kafka-as-event-store (primary)
    - [Martin Fowler: Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) — the foundational essay on fold-over-events, snapshots, and replay (reference)
    - [Azure Architecture Center: Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) — the cloud-pattern framing and CQRS pairing (reference)
- **Do:**
    1. Event-source the share-register: model order, allocation, and transfer events and fold them to current positions.
    2. Answer "investor X's position as known on date D" purely by replaying events up to D.
    3. Add a snapshot so replay does not always start from the first event.
    4. Write a half-page ADR stating where event sourcing applies in a TA system and where it must not.
- **Done when:**
    - [ ] You can defend the as-known-at vs as-of distinction (bitemporality) with a fund example, and say no to ES somewhere.
    - [ ] You can reconstruct a historical position from the event log alone.
    - [ ] Your ADR names a concrete case where ES would be the wrong choice and why.
- Est. hours: 5

#### 1.8.7 + 1.8.8 Dead-letter queues & backpressure — T2
- **Why:** these two decide whether a bad message or a slow consumer takes down the flow or just a metric. Without a DLQ, one malformed settlement message poison-pills the CDC pipeline and stops every downstream consumer; without backpressure handling, a slow Iceberg sink quietly blows out memory until the job dies. The architect designs the runbook so that a 2am poison pill pages no one and is replayable at 9am with no data loss.
- **Learn:**
    - DLQ design — parking failed messages with diagnostic headers and a defined replay procedure *(Kafka: Definitive Guide ch. 9)*
    - poison-pill detection — distinguishing a one-off bad record from a systemic failure *(Kafka: Definitive Guide ch. 9)*
    - backpressure mechanics — bounded buffers and consumer lag as the early-warning signal *(Flink docs: Stateful Stream Processing)*
    - Flink credit-based flow control — how backpressure propagates upstream without dropping data *(Flink docs: Stateful Stream Processing)*
    - alerting — lag and DLQ-depth thresholds that page the right person at the right time *(Kafka: Definitive Guide ch. 9)*
- **Resources:**
    - **[Kafka: The Definitive Guide, 2nd ed. (free via Confluent)](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/)** ch. 9 — Connect error handling, DLQ topics, and replay (primary)
    - [Apache Flink documentation: Stateful Stream Processing](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/) — backpressure and credit-based flow control (reference)
- **Do:**
    1. Define the DLQ-plus-replay runbook for the CDC pipeline: who triages, the replay command, and the idempotency requirement that makes replay safe.
    2. Specify the diagnostic headers a parked message must carry to be triageable cold.
    3. Set lag and DLQ-depth alert thresholds and state who they page.
    4. Dry-run the runbook: park a poison message, then follow your own steps to replay it without loss.
- **Done when:**
    - [ ] A poisoned message at 2am pages no one and is replayable at 9am without data loss.
    - [ ] Your runbook names the triage owner, the replay procedure, and the idempotency precondition.
    - [ ] You can point to backpressure in a running Flink job and explain why it is not dropping data.
- Est. hours: 2.5

#### 2.4.2 Message brokers vs logs — T2
- **Why:** queue semantics (RabbitMQ/Service Bus) and log semantics (Kafka) solve different problems, and picking wrong is expensive in both directions. Use Kafka for request/reply and you fight its consumer-group model; use RabbitMQ for a replayable integration backbone and you lose the replay that auditors and reprocessing depend on. The architect must place each fund-platform messaging need on the right side of this line and defend it.
- **Learn:**
    - competing consumers vs consumer groups — per-message distribution vs partition-bound consumption *(RabbitMQ docs: AMQP Concepts)*
    - ack/redelivery vs offsets — per-message acknowledgment vs replayable offset tracking *(RabbitMQ docs: AMQP Concepts)*
    - routing vs partitioning — exchanges and bindings vs partition keys *(RabbitMQ docs: AMQP Concepts)*
    - when a queue wins — task distribution, request/reply, per-message TTL *(Kafka: Definitive Guide ch. 1)*
    - when a log wins — replay, fan-out, ordering, and long retention *(Kafka: Definitive Guide ch. 1)*
    - AMQP basics and the corp queue — Azure Service Bus as the enterprise queue *(RabbitMQ docs: AMQP Concepts)*
- **Resources:**
    - **[RabbitMQ documentation: AMQP 0-9-1 Concepts](https://www.rabbitmq.com/tutorials/amqp-concepts)** — exchanges, queues, bindings, acks, competing consumers (primary)
    - [Kafka: The Definitive Guide, 2nd ed. (free via Confluent)](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/) ch. 1 — the log model framed against queues (reference)
- **Tools:**
    - FOSS (hands-on): [RabbitMQ](https://www.rabbitmq.com/docs) — short hands-on with exchanges and queues (↔ Azure Service Bus / AWS SQS)
    - Corp (evaluate): [Azure Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/) — the corp-native queue: sessions, dead-lettering, TTL
- 🐘 **Postgres-native alternative — [pgmq](https://github.com/pgmq/pgmq) (SQS-style queues) + `LISTEN`/`NOTIFY` (lightweight pub/sub):** *Better when* you already run Postgres, volumes are low-to-moderate, and you want transactional enqueue — the message and the business row commit in one transaction — with a single system to operate, secure and back up. *Worse when* you need high-throughput fan-out, topic routing/exchanges, very long retention with replay, or a broker protocol ecosystem: reach for RabbitMQ (routing) or Kafka (replayable log).
- **Do:**
    1. Stand up RabbitMQ and run a small competing-consumers task-distribution example.
    2. Contrast it with a Kafka consumer-group example over the same workload.
    3. Build a decision table: 6 fund-platform messaging needs → queue or log, one line of why each.
    4. Identify which of the 6 would be actively harmed by the wrong choice and how.
- **Done when:**
    - [ ] You never propose Kafka for request/reply or RabbitMQ for replayable integration again.
    - [ ] Your decision table covers 6 concrete fund needs with a one-line rationale each.
    - [ ] You can explain ack/redelivery vs offset replay and which an audit-reprocessing use case needs.
- Est. hours: 3

#### 5.6.4 Durable execution (Temporal) — T2
- **Why:** trade lifecycle, KYC, and corporate-actions workflows are long-running, stateful, and retry-heavy — durable execution is the modern saga orchestrator and FS adoption is real. Hand-rolled retry-and-timeout logic across services is where these workflows rot; a worker crash mid-corporate-action leaves the process in an unknown state. Temporal makes the workflow itself durable, and the architect must know when that beats a BPM engine or a plain queue.
- **Learn:**
    - workflow-as-code — deterministic workflow functions plus side-effecting activities *(Temporal docs: Understanding Temporal)*
    - event-history replay — how Temporal reconstructs workflow state after a crash *(Temporal docs: Understanding Temporal)*
    - retries, timeouts, heartbeats — built-in reliability primitives for activities *(Temporal docs: Understanding Temporal)*
    - signals and queries — sending input to and reading state from a running workflow *(Temporal docs: Understanding Temporal)*
    - versioning running workflows — changing code without breaking in-flight executions *(Temporal docs: Understanding Temporal)*
    - placement — Temporal vs BPM vs queue, and Azure Durable Functions as the corp analogue *(Temporal docs: Understanding Temporal)*
- **Resources:**
    - **[Temporal documentation: Understanding Temporal](https://docs.temporal.io/evaluate/understanding-temporal)** — core concepts: workflows, activities, event history, retries (primary)
    - [Temporal documentation root](https://docs.temporal.io/) — the Python SDK tutorial path for the hands-on build (reference)
- **Tools:**
    - FOSS (hands-on): [Temporal](https://docs.temporal.io/) — OSS server in compose running the durable saga (↔ Temporal Cloud / Durable Functions / Step Functions)
    - FOSS (Postgres-native): [DBOS](https://docs.dbos.dev/) — durable execution as a library with workflow/queue state in Postgres (↔ Hatchet, pgflow)
    - Corp (evaluate): [Azure Durable Functions](https://learn.microsoft.com/azure/azure-functions/durable/durable-functions-overview) — the Azure-native durable-execution analogue
- 🐘 **Postgres-native alternative — [DBOS](https://docs.dbos.dev/) (also Hatchet, pgflow):** *Better when* you already run Postgres and want durable workflows without operating a Temporal cluster — workflow and queue state live in your DB, commit transactionally with your business data, far lighter ops and lower latency. *Worse when* you need Temporal's maturity at scale: massive parallel fan-out, very long-lived workflows, rich signals/queries and visibility tooling, or multi-language/multi-region — there a single Postgres becomes the bottleneck and Temporal's ecosystem wins.
- **Do:**
    1. Run Temporal OSS in compose with a worker.
    2. Reimplement the Phase-4 subscription saga as a Temporal workflow with activities for each step.
    3. Add retries and a compensation path for the step-2 failure.
    4. Kill the worker mid-run and watch the workflow resume from event history on restart.
- **Done when:**
    - [ ] You can explain event-history replay and why workflow code must be deterministic.
    - [ ] Your workflow resumes correctly after a mid-run worker kill.
    - [ ] You can state when Temporal beats a BPM engine and when it does not.
- Est. hours: 4

#### 5.6.5 BPM / process orchestration (Camunda, BPMN/DMN) — T2
- **Why:** banks and fund administrators run BPMN engines for settlement, onboarding, and exception handling, so the architect must speak BPMN/DMN and know when model-driven beats code-driven orchestration. A compliance officer can read and sign off a BPMN diagram in a way they never could read Temporal code — that auditability is exactly why these engines persist in regulated shops. The decision the architect owns is BPM vs durable execution vs scheduler, per workflow, with reasons.
- **Learn:**
    - BPMN 2.0 working subset — tasks, gateways, and events (timer/message/error) *(Camunda 8 docs)*
    - pools and lanes — modelling responsibility boundaries across teams/systems *(Camunda 8 docs)*
    - DMN decision tables and FEEL — externalising business rules from process flow *(Camunda 8 docs)*
    - Camunda 7 vs 8/Zeebe — the architecture and licensing shift *(Camunda 8 docs)*
    - human-task workflows — exception queues and manual review steps *(Camunda 8 docs)*
    - the orchestration trichotomy — BPM vs Temporal vs Airflow under one decision framework *(Camunda 8 docs)*
- **Resources:**
    - **[Camunda 8 documentation](https://docs.camunda.io/)** — BPMN and DMN references, Zeebe architecture, human tasks (primary)
    - [bpmn.io](https://bpmn.io/) — the open-source modelling toolkit and tutorials for drawing the diagrams (reference)
- **Tools:**
    - FOSS (hands-on): [Camunda 8 / Zeebe](https://docs.camunda.io/) — runs the BPMN process and DMN table (↔ Camunda Enterprise / Pega / IBM BPM)
    - FOSS (hands-on): [bpmn.io](https://bpmn.io/) — browser-based BPMN/DMN modeller for authoring the diagrams
- **Do:**
    1. Model the subscription-order lifecycle in BPMN with a normal path and an error-handling path to a human task.
    2. Encode the "compliance review required?" rule as a DMN decision table with FEEL expressions.
    3. Deploy and run both in Camunda, triggering the error path at least once.
    4. Write a short comparison of this BPMN solution against the Temporal version of the same saga.
- **Done when:**
    - [ ] You can defend orchestration-tool choice (BPM vs durable execution vs scheduler) for three different fund workflows.
    - [ ] Your BPMN process routes a failure to a human task and resumes correctly.
    - [ ] Your DMN table produces the right review decision for several test inputs.
- Est. hours: 5

#### 1.11.1 + 1.11.3 Data protocols & async API standards — T2
- **Why:** protocol literacy (gRPC vs REST vs Arrow Flight; AsyncAPI/CloudEvents) is the architect's interface-design toolkit across the estate — choosing the transfer mechanism for a BI extract, a microservice call, a market-data feed, or a file drop with numbers, not vibes. Default everything to REST/JDBC and you marshal millions of rows one at a time when Arrow Flight would move columnar batches in a fraction of the time. Async standards (AsyncAPI, CloudEvents) are what make an event estate documentable and interoperable rather than tribal knowledge.
- **Learn:**
    - gRPC over HTTP/2 with Protobuf — contract-first, low-overhead service calls *(AsyncAPI docs)*
    - REST maturity in practice — where REST is the pragmatic default and where it is not *(AsyncAPI docs)*
    - Arrow Flight and ADBC — columnar bulk transfer vs row-marshaling JDBC/ODBC *(Arrow Flight docs)*
    - WebSocket/MQTT/AMQP placement — which transport fits push, IoT-style, and queue use cases *(AsyncAPI docs)*
    - AsyncAPI — OpenAPI-for-events: channels, messages, schemas *(AsyncAPI docs)*
    - CloudEvents — a vendor-neutral event envelope for interop *(CloudEvents spec)*
    - legacy literacy — SOAP/OData you will meet in the existing fund estate *(AsyncAPI docs)*
- **Resources:**
    - **[AsyncAPI documentation](https://www.asyncapi.com/docs)** — concepts, channels, messages; the standard you will author against (primary)
    - [Apache Arrow Flight RPC](https://arrow.apache.org/docs/format/Flight.html) — the columnar bulk-transfer protocol for analytical extracts (reference)
    - [CloudEvents specification](https://cloudevents.io/) — the common event-envelope standard (reference)
- **Tools:**
    - FOSS (hands-on): [AsyncAPI](https://www.asyncapi.com/docs) — author and render the event-API document for your topics
    - FOSS (hands-on): [Apache Arrow Flight](https://arrow.apache.org/docs/format/Flight.html) — columnar transport for the BI-extract comparison (↔ JDBC/ODBC)
- **Do:**
    1. Write the AsyncAPI document for your fund-order Kafka topics: channels, messages, and schema references.
    2. Render its HTML docs from the spec.
    3. Map four transfer needs (BI extract, microservice call, market-data feed, file drop) to a protocol each.
    4. Justify each mapping with a concrete factor (payload size, latency, ordering, schema) — numbers where you have them.
- **Done when:**
    - [ ] You can pick the transfer protocol for: BI extract, microservice call, market-data feed, file drop — with numbers, not vibes.
    - [ ] Your AsyncAPI document renders and accurately describes the order topics.
    - [ ] You can explain why Arrow Flight beats JDBC for a large analytical extract.
- Est. hours: 3

#### 1.4.1 + 1.4.2 Lambda vs Kappa — T2
- **Why:** the batch/speed-layer debate frames every "do we need streaming?" conversation, and medallion-with-streaming is today's synthesis. Reach for Lambda and you pay the dual-codebase tax — maintaining the same NAV-flow logic twice in two systems that must agree — when a replayable log usually makes that second codebase unnecessary. The architect must be able to name which architecture the capstone platform actually is and defend it for fund data.
- **Learn:**
    - the Lambda architecture — batch plus speed layers and the dual-codebase maintenance tax *(Kreps: Questioning the Lambda Architecture)*
    - the Kappa answer — replay the log through one stream framework instead of two systems *(Kreps: Questioning the Lambda Architecture)*
    - retention implications — what Kappa demands of log storage and reprocessing *(Kreps: Questioning the Lambda Architecture)*
    - the modern synthesis — table formats plus streaming ingestion dissolving most of the dichotomy *(Streaming Systems ch. 1)*
- **Resources:**
    - **[Jay Kreps: Questioning the Lambda Architecture](https://www.oreilly.com/radar/questioning-the-lambda-architecture/)** — the essay that defined the Kappa alternative (primary)
    - [Streaming Systems (Akidau, Chernyak, Lax)](https://www.streamingsystems.net/) ch. 1 — the streams-and-tables framing behind the synthesis (reference)
- **Do:**
    1. Write a one-page position note stating which architecture (Lambda, Kappa, or the table-format synthesis) your capstone platform actually is.
    2. Justify why that is the right call for fund data specifically.
    3. State what you would change if regulators demanded sub-minute NAV-error detection.
    4. Name the dual-codebase risk in your design and how you avoid or accept it.
- **Done when:**
    - [ ] You can articulate what you'd change if regulators demanded sub-minute NAV-error detection.
    - [ ] Your note names the platform's actual architecture and defends it for fund data.
    - [ ] You can explain the dual-codebase tax with a concrete fund example.
- Est. hours: 2

#### 1.2.2 + 1.2.3 Micro-batch vs true streaming — T2
- **Why:** Spark Structured Streaming (micro-batch) vs Flink (event-at-a-time) is a real engine decision with latency, state, and ops consequences. Pick micro-batch for a sub-second exposure monitor and you cannot meet the latency floor; pick event-at-a-time for a minute-grained reconciliation and you take on operational complexity you did not need. The architect must place any fund use case in the right latency class and name the engine.
- **Learn:**
    - micro-batch mechanics — the trigger interval and the latency floor it imposes *(Spark Structured Streaming guide)*
    - continuous processing — Spark's lower-latency mode and its limitations *(Spark Structured Streaming guide)*
    - state handling differences — how Spark and Flink each manage and checkpoint state *(Flink docs: Stateful Stream Processing)*
    - ops profile — long-lived Spark cluster reuse vs per-job Flink clusters *(Spark Structured Streaming guide)*
    - the latency-class rubric — minutes vs seconds vs sub-second and which engine each implies *(Flink docs: Stateful Stream Processing)*
- **Resources:**
    - **[Spark Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)** — micro-batch model, triggers, and state (primary)
    - [Apache Flink documentation: Stateful Stream Processing](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/) — the event-at-a-time contrast (reference)
- **Do:**
    1. Rebuild one Flink aggregation in Spark Structured Streaming on the existing Spark cluster.
    2. Measure end-to-end latency for both implementations.
    3. Compare code volume and operational burden in a half-page note.
    4. Place three fund use cases (intraday flow totals, sub-second exposure alert, nightly reconciliation) in a latency class and name the engine for each.
- **Done when:**
    - [ ] You can place any fund use case in the right latency class and name the engine.
    - [ ] Your note compares measured latency, code, and ops burden for both engines.
    - [ ] You can explain why micro-batch has a latency floor that event-at-a-time does not.
- Est. hours: 3

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.2.4 | Real-time / low-latency paradigm | Sub-second serving paths (in-memory, push); mostly out of fund-admin scope but appears in trading-adjacent systems | [*Streaming Systems* ch. 1 sidebar](https://www.streamingsystems.net/) | 15 |
| 1.3.4 | RT / user-facing analytics workload | High-concurrency, sub-second dashboards served to many external users (Pinot/Druid class) | [StarTree: what is user-facing analytics](https://startree.ai/blog/what-is-user-facing-analytics) | 25 |
| 1.8.12 | Bulkhead | Resource isolation so one slow consumer can't sink the whole flow | [Azure patterns catalog: Bulkhead](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead) | 15 |
| 1.8.13 | Circuit breaker | Fail-fast wrapper that stops hammering a flaky dependency | [Azure patterns catalog: Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) | 15 |
| 2.3.2 | Trigger-based CDC | DB triggers populate change tables; an intrusive legacy approach with write overhead | [Debezium FAQ](https://debezium.io/documentation/faq/) | 15 |
| 2.3.3 | Snapshot-based CDC | Periodic diffing (Fivetran-style); simple but lossy between snapshots | [Fivetran docs: sync modes](https://fivetran.com/docs/core-concepts/sync-modes) | 15 |
| 2.4.3 | Event mesh | Federated brokers routing events across sites/clouds (Solace; big in capital markets) | [Solace: what is an event mesh](https://solace.com/resources/event-mesh/what-is-an-event-mesh) | 25 |
| 4.3.4 | RT analytics engines | Pinot/Druid/ClickHouse serving layer for the 1.3.4 user-facing workloads | [Apache Pinot docs: intro](https://docs.pinot.apache.org/) | 25 |
| 4.3.5 | Streaming databases | Incrementally-maintained materialized views over streams (Materialize/RisingWave) | [RisingWave docs: architecture](https://docs.risingwave.com/get-started/architecture) | 25 |

*T3 subtotal: 3 h*

### Capstone 4 — Real-time fund-flow & price CDC streaming

- **Goal:** the platform gains a streaming spine: operational changes flow as events, stateful aggregations stay correct under late data, and every guarantee is stated and demonstrated.
- **Stack (100% free):** [Kafka KRaft](https://kafka.apache.org/documentation/) or [Redpanda](https://docs.redpanda.com/) (↔ Confluent Cloud / Event Hubs), [Kafka Connect](https://kafka.apache.org/documentation/#connect) + [Debezium](https://debezium.io/documentation/reference/stable/index.html) with [outbox router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) (↔ Qlik Replicate / GoldenGate / ADF), [Apicurio](https://www.apicur.io/registry/docs/) or [Confluent SR](https://docs.confluent.io/platform/current/schema-registry/index.html) with [Avro](https://avro.apache.org/docs/1.12.0/specification/) (↔ Confluent Cloud SR / Azure Schema Registry), [Flink](https://nightlies.apache.org/flink/flink-docs-stable/) (↔ Confluent Flink / Managed Flink / ASA), [Iceberg](https://iceberg.apache.org/docs/latest/) sink on [MinIO](https://docs.min.io/index.html), [Temporal](https://docs.temporal.io/) saga + [Camunda](https://docs.camunda.io/) BPMN process from the entries above, [Dagster](https://docs.dagster.io/) supervising batch reconciliation, all in compose.
- **Build:** (1) Debezium streams orders/NAV + the outbox topic; (2) Flink computes per-share-class windowed flow totals (heuristic watermarks, allowed lateness, late-event side output) exactly-once into Iceberg; (3) nightly Dagster batch reconciles streamed totals against batch recompute and alerts on drift; (4) schema registry enforces the 1.9.7 policy (one rejected evolution kept as evidence); (5) the subscription saga (Temporal) and BPMN process (Camunda) run against the same events; (6) chaos drills: kill broker, connector, Flink job — document recovery and guarantee held. Capture the recovery narrative for each drill as you run it, naming the mechanism that restored correctness.
- **Architecture deliverables:** C4 updated with the streaming spine; ADR-010 log platform choice (Kafka vs Event Hubs vs Redpanda), ADR-011 delivery-guarantee design (where exactly-once is real and where idempotent-at-least-once is the honest answer), ADR-012 orchestration species (BPM vs durable execution vs scheduler, per workflow). Each ADR states the decision, the alternatives weighed, and the EU/fund-industry constraint that drove it.
- **Acceptance criteria:** reconciliation drift = 0 over a 3-day simulated run incl. injected late/duplicate events; each chaos drill has a written recovery narrative naming the mechanism (ISR, checkpoint, offset commit); schema policy violation is blocked by the registry and the evidence archived; saga failure path leaves consistent state with full audit trail.
- Est. hours: 16

*Phase 4 total: 119 h (T1/T2 entries 99.5 h + T3 3 h + capstone 16 h ≈ 119)*
