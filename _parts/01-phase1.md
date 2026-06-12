<a id="phase-1"></a>
## Phase 1: Distributed Data Systems & Modeling Core (months 7–11, 118 h)

**Goal:** rebuild the theoretical foundation an architect reasons from — transaction guarantees, consistency, distribution tradeoffs, database internals — and turn existing modeling intuition into formal, teachable practice (conceptual→logical→physical, dimensional), documented with C4 and ADRs from day one.
**Entry prerequisites:** Phase 0 — or its skip tests passed (Linux/shell, Python, SQL, Git, Docker, networking).
**Exit criteria:** you can (1) explain isolation anomalies and pick an isolation level for a fund-order workload; (2) argue a replication/partitioning choice with PACELC, not folklore; (3) read a Postgres `EXPLAIN ANALYZE` and fix the plan; (4) produce a 3-level model + star schema for a fund domain and defend every key and SCD choice; (5) ship C4 diagrams + ADRs as a matter of habit.

### T1/T2 topics

#### 1.6.1 ACID & isolation levels — T1
- **Why:** transaction guarantees underpin every regulated-data design review; "is this exactly-once and serializable?" is a question you must answer, not delegate.
- **Learn:** atomicity vs durability mechanics (WAL); isolation anomalies (dirty/non-repeatable/phantom reads, write skew); ANSI levels vs snapshot isolation; serializability vs SSI; how Postgres, SQL Server, and Oracle differ in defaults; idempotent retry vs transactional retry.
- **Resource:** DDIA ch. 7 "Transactions" (latest ed.). *Alternate:* CMU 15-445 concurrency-control lectures.
- **Tools:** FOSS: PostgreSQL (in Docker) · Corp: Azure SQL / Oracle DB (defaults + TDE-era differences at evaluation level).
- **Do:** reproduce write skew and a phantom in Postgres with two psql sessions at `READ COMMITTED`, then fix both with `REPEATABLE READ`/`SERIALIZABLE`; note retry behavior.
- **Done when:** you can explain to a reviewer why snapshot isolation permits write skew and name a fund-accounting scenario where that corrupts data.
- Est. hours: 8

#### 1.6.3 + 1.6.4 + 1.6.5 The consistency spectrum — T2
- **Why:** replicated platforms (read replicas, geo-DR, caches) silently downgrade consistency; the architect must name the guarantee actually delivered.
- **Learn:** eventual vs strong; read-your-writes, monotonic reads, causal consistency; linearizability vs serializability (they answer different questions); where lag bites: replica reads after writes, cross-region failover.
- **Resource:** DDIA ch. 5 "Replication" + ch. 9 "Consistency and Consensus" (linearizability sections).
- **Do:** write a 1-page memo: which consistency level a fund-order status API needs vs a NAV-history dashboard, and what each costs.
- **Done when:** you can give a concrete user-visible bug for each violated guarantee.
- Est. hours: 5

#### 1.7.1 + 1.7.2 CAP & PACELC — T1
- **Why:** every design review invokes CAP, usually wrongly; the architect corrects the record and uses PACELC's latency half, which is what actually drives cloud database selection.
- **Learn:** what CAP actually states (and what it doesn't — A and C definitions are narrow); partition behavior of common systems; PACELC: latency–consistency tradeoff under normal operation; classify Postgres, Cassandra, Cosmos DB, Spanner-style systems.
- **Resource:** DDIA ch. 9 (incl. "The Unhelpfulness of CAP") + Abadi's PACELC paper (IEEE Computer 2012).
- **Do:** build a one-table PACELC classification of 8 stores you'll meet in this plan (Postgres, Cassandra, Kafka, Cosmos DB, DynamoDB, Spanner, Redis, MongoDB) with one-line justifications.
- **Done when:** you can explain why "CP vs AP" is the wrong frame for a single-region Azure SQL deployment.
- Est. hours: 3

#### 1.8.1 Idempotency — T1
- **Why:** retry-safety is the single biggest reliability lever in pipelines; non-idempotent loads are how funds double-book trades.
- **Learn:** idempotency keys; natural vs synthetic dedup; idempotent writes (MERGE/upsert, INSERT … ON CONFLICT); idempotent pipeline runs (overwrite-partition pattern); at-least-once delivery + idempotent consumer = effective exactly-once.
- **Resource:** DDIA ch. 11 (fault-tolerance/exactly-once sections); taxonomy concept entry as checklist.
- **Tools:** FOSS: PostgreSQL upserts · Corp: ADF rerun semantics (evaluation level).
- **Do:** write a Python loader (via `uv run`) that ingests a trades CSV into Postgres and is provably safe to run twice — demonstrate with row counts and checksums.
- **Done when:** you can list the three places idempotency must hold in a pipeline (source read, transform, sink write) and how to get each.
- Est. hours: 4

#### 1.8.9 Distributed transactions & 2PC — T2
- **Why:** you must recognize when someone proposes a distributed transaction and steer to outbox/saga instead — with reasons, not taste.
- **Learn:** 2PC protocol and its blocking failure mode; coordinator failure; XA in practice; why consensus (Raft) ≠ 2PC; modern alternatives preview (outbox, saga — implemented in Phase 4).
- **Resource:** DDIA ch. 9 ("Distributed Transactions and Consensus").
- **Do:** write a half-page ADR rejecting 2PC for a hypothetical order-service + position-service consistency requirement, naming the alternative.
- **Done when:** you can explain what happens to locks when a 2PC coordinator dies mid-commit.
- Est. hours: 5

#### 1.5.1–1.5.4 Storage paradigms — T2
- **Why:** row vs columnar, shared-nothing vs shared-disk, and storage/compute separation are the axes along which every warehouse/lakehouse vendor differentiates — this is the vocabulary of vendor selection.
- **Learn:** row vs columnar layouts and why scans love columns; compression + late materialization; MPP partitioning and data skew; shared-nothing vs shared-disk; separation of storage and compute (Snowflake/BigQuery model) and its cost/elasticity consequences.
- **Resource:** DDIA ch. 3 "Storage and Retrieval" (column-store sections) + CMU 15-445 storage lectures 3–5.
- **Do:** in DuckDB, run the same aggregate over a 10M-row table stored as CSV vs Parquet; explain the timing difference in terms of layout and I/O.
- **Done when:** you can sketch the Snowflake-style architecture and say which failure/cost behaviors follow from each separation decision.
- Est. hours: 4

#### 3.2.1 Relational internals (the database under everything) — T1
- **Why:** indexing, query planning, MVCC, and recovery ground every storage decision an architect makes; this is the deepest single investment in the plan.
- **Learn:** pages/heap files and buffer pool; B+trees vs hash vs GIN/BRIN; query planner: cardinality estimation, join algorithms (nested-loop/hash/merge); MVCC and vacuum; WAL, checkpoints, crash recovery; connection pooling; partitioning and when it helps.
- **Resource:** CMU 15-445 (latest year) — lectures + notes for: storage, buffer pool, indexes, sorting/joins, query optimization, MVCC, logging/recovery (~14 of 26 lectures). *Alternate:* *Database Internals* (Petrov) Part I.
- **Tools:** FOSS: PostgreSQL 16 + `EXPLAIN (ANALYZE, BUFFERS)`, pgbench · Corp: Azure SQL / Oracle (planner-hint culture, licensing economics — evaluation level).
- **Do:** take a deliberately slow 5-table fund-holdings query; capture the plan, fix it with indexes/statistics/rewrites to a 10× improvement; write up before/after plans.
- **Done when:** you can read an unfamiliar `EXPLAIN ANALYZE` and narrate where time goes and why the planner chose the join order it did.
- Est. hours: 30

#### 8.2.1 + 8.2.2 + 8.2.3 Conceptual → logical → physical modeling — T1
- **Why:** the three-level discipline is the architect's signature artifact chain — business entities to keys/normal forms to engine-specific DDL — and the basis for every review you'll run.
- **Learn:** conceptual entity modeling (and when to stop); logical: candidate/natural/surrogate keys, 1NF–BCNF and deliberate denormalization; physical: data types, partitioning, indexes per target engine; forward/reverse engineering; notation fluency (Crow's Foot; read IDEF1X).
- **Resource:** DAMA-DMBOK ch. 5 "Data Modeling and Design". *Alternate:* Hoberman, *Data Modeling Made Simple*.
- **Tools:** FOSS: draw.io / DBeaver ERD · Corp: erwin / ER/Studio / SqlDBM (what EU banks actually license — evaluation level).
- **Do:** model the fund domain three ways: conceptual (fund, share class, investor, order, NAV), logical (keys + normal forms justified), physical (Postgres DDL with partitioning for NAV history).
- **Done when:** a colleague can implement your logical model without asking you questions; every surrogate-key choice has a stated reason.
- Est. hours: 12

#### 8.2.4 Dimensional modeling — T1
- **Why:** Kimball stars remain the dominant analytical model in regulated reporting marts; fund NAV/holdings/fees reporting is textbook dimensional territory.
- **Learn:** fact table grain (declare it first, always); fact types (transaction, periodic snapshot, accumulating snapshot — NAV is a periodic snapshot); conformed dimensions and the bus matrix; SCD types 1/2/3/6 (security/fund reference data is SCD2 country); junk/degenerate dimensions; star vs snowflake.
- **Resource:** Kimball & Ross, *The Data Warehouse Toolkit* 3rd ed., ch. 1–4 + ch. 19 (financial services). *Alternate:* Corr & Stagnitto, *Agile Data Warehouse Design* (BEAM workshops).
- **Tools:** FOSS: dbt + DuckDB for implementation · Corp: same patterns in Synapse/Snowflake marts.
- **Do:** design the bus matrix for a fund administrator (processes: orders, NAV calculation, fee accrual, transfer agency); implement the NAV periodic-snapshot star with an SCD2 fund dimension in SQL.
- **Done when:** you can state the grain of each fact table in one sentence and show an SCD2 query returning point-in-time-correct fund attributes for any historical date.
- Est. hours: 16

#### 8.5.1 Architecture notations & decision records (C4, ADR) — T1
- **Why:** C4 diagrams and ADRs are the artifacts that define the architect role in practice — they make your reasoning reviewable and your decisions auditable.
- **Learn:** C4 levels (context, container, component, code — and when to stop at container); diagrams-as-code; ADR anatomy (context, decision, consequences) and lifecycle (proposed/accepted/superseded); lightweight RFC processes; what reviewers actually look for.
- **Resource:** c4model.com (full read) + adr.github.io (MADR template). *Alternate:* Richards & Ford, *Fundamentals of Software Architecture* ch. on diagramming & decisions.
- **Tools:** FOSS: Structurizr Lite (Docker) or Mermaid C4 · Corp: Sparx Enterprise Architect / Visual Paradigm (the EA suites EU institutions license).
- **Do:** document an existing system you know from work as C4 context + container diagrams, plus 2 retroactive ADRs for its key decisions.
- **Done when:** every capstone from here on ships C4 + ADRs without you thinking about it (the capstones enforce this).
- Est. hours: 8

#### 1.10.1 Modeling notations overview — T2
- **Why:** you need reading fluency across UML/BPMN/DMN/ArchiMate before Phase 4 (BPM) and Phase 8 (ArchiMate practice) go deep.
- **Learn:** which notation answers which question — UML class/sequence (system structure/behavior), BPMN (executable process), DMN (decision logic), ArchiMate (enterprise layers), ERD/IDEF1X (data), C4 (software) — and reading-level literacy in each.
- **Resource:** taxonomy's standards reference list entries + one example diagram of each from the linked OMG/Open Group spec intros.
- **Do:** make a one-page "notation chooser" cheat sheet: question → notation → tool.
- **Done when:** shown a diagram cold, you can name the notation and read it correctly.
- Est. hours: 2

#### 9.1.3 Local data sandboxes — T2
- **Why:** the entire 4-year lab runs on reproducible local stacks; compose fluency is the substrate for every capstone.
- **Learn:** Docker Compose service graphs, healthchecks, volumes/networks; Testcontainers idea (programmatic throwaway infra); DuckDB as a zero-infra warehouse; pinning images for reproducibility.
- **Resource:** Docker Compose official docs (top-level concepts + healthchecks) — builds directly on Phase 0's module 0.5.
- **Tools:** FOSS: Docker Compose, DuckDB, Testcontainers · Corp: dev-container/codespace equivalents (awareness).
- **Do:** write the `docker-compose.yml` you'll grow all four years: Postgres + MinIO + a placeholder service, with healthchecks and named volumes.
- **Done when:** `docker compose up` gives a clean, healthy stack on a fresh clone in under 2 minutes.
- Est. hours: 4

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.3.3 | HTAP (workload) | One system serving OLTP + OLAP; niche but recurring vendor pitch | DDIA ch. 3 (closing section) | 30 |
| 1.6.2 | BASE | Marketing-era label for eventual-consistency systems; know it to translate it | DDIA ch. 5 intro | 15 |
| 3.2.2 | NoSQL document stores | JSON-document storage (MongoDB); flexible schema, app-owned integrity | DDIA ch. 2 (document model) | 45 |
| 3.2.3 | NoSQL key-value | High-throughput KV (Redis/Valkey, DynamoDB); caching + session state | DDIA ch. 3 (hash indexes) | 30 |
| 3.2.4 | NoSQL wide-column | Sparse-column distributed stores (Cassandra); write-heavy, query-first design | DDIA ch. 2 + Cassandra docs "data modeling" intro | 45 |
| 3.2.10 | HTAP stores | TiDB/SingleStore implementations of 1.3.3 | vendor architecture pages | 15 |

*T3 subtotal: 3 h*

### Capstone 1 — Fund reference OLTP + reporting mart

- **Goal:** a correct, documented foundation: operational fund reference database + dimensional reporting mart, the seed every later phase builds on.
- **Stack (100% free):** PostgreSQL 16 (↔ Azure SQL / Oracle), DuckDB (↔ Synapse/Snowflake mart), dbt Core seed/models for the mart (↔ dbt Cloud), Structurizr Lite (↔ Sparx EA), Docker Compose, Python via uv, Faker for sample data (↔ Tonic.ai/Delphix).
- **Build:** (1) implement the Phase-1 physical model in Postgres: funds, share classes, ISIN-keyed securities, investors, orders, NAV history (partitioned); (2) load Faker-generated but referentially consistent data with the idempotent loader from 1.8.1; (3) build the NAV periodic-snapshot star + SCD2 fund dimension in DuckDB; (4) one deliberately slow query, tuned, with before/after plans.
- **Architecture deliverables:** C4 context + container diagrams; ADR-001 (surrogate vs natural keys — why ISIN is not your PK), ADR-002 (SCD2 for fund attributes), ADR-003 (partitioning scheme for NAV history).
- **Acceptance criteria:** loader runs twice with identical end state; point-in-time query returns correct fund attributes for any historical date; tuned query ≥10× faster with written plan analysis; a stranger can run `docker compose up && uv run load.py` from the README and get the same numbers.
- Est. hours: 14

*Phase 1 total: 118 h (T1/T2 entries 101 h + T3 3 h + capstone 14 h)*
