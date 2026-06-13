<a id="phase-1"></a>
## Phase 1: Distributed Data Systems & Modeling Core (months 7–11, 118 h)

*Phase 1 of 8 · months 7–11 · 118 h · capstone: Fund reference OLTP + reporting mart.*  ← [Phase 0](#phase-0) · [Phase 2](#phase-2) →

**Goal:** rebuild the theoretical foundation an architect reasons from — transaction guarantees, consistency, distribution tradeoffs, database internals — and turn existing modeling intuition into formal, teachable practice (conceptual→logical→physical, dimensional), documented with C4 and ADRs from day one.
**Entry prerequisites:** Phase 0 — or its skip tests passed (Linux/shell, Python, SQL, Git, Docker, networking).
**Exit criteria:** you can (1) explain isolation anomalies and pick an isolation level for a fund-order workload; (2) argue a replication/partitioning choice with PACELC, not folklore; (3) read a Postgres `EXPLAIN ANALYZE` and fix the plan; (4) produce a 3-level model + star schema for a fund domain and defend every key and SCD choice; (5) ship C4 diagrams + ADRs as a matter of habit.

### T1/T2 topics

#### 1.6.1 ACID & isolation levels — T1
- **Why:** Transaction guarantees underpin every regulated-data design review — "is this exactly-once and serializable?" is a question the architect must answer, not delegate. Getting isolation wrong in a fund platform means double-booked orders and unexplainable NAV corrections that auditors will find before you do.
- **Learn:**
    - atomicity and durability mechanics — how the WAL makes a commit survive a crash *(DDIA ch. 7)*
    - isolation anomalies — dirty/non-repeatable/phantom reads and write skew, with a concrete failure story for each *(DDIA ch. 7)*
    - ANSI levels vs snapshot isolation — why READ COMMITTED is the common default and what it silently permits *(Postgres docs: Transaction Isolation)*
    - serializability vs SSI — what `SERIALIZABLE` buys and costs in Postgres *(CMU 15-445 concurrency-control lectures)*
    - vendor defaults — how Postgres, SQL Server (RCSI), and Oracle differ, and why that matters in migrations *(Postgres docs: Transaction Isolation)*
    - idempotent retry vs transactional retry — what the application must do when a serialization failure (SQLSTATE 40001) surfaces *(DDIA ch. 7)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 7 "Transactions" (latest ed.)** — the canonical treatment: anomalies, weak isolation levels, serializability, retry semantics (primary)
    - [PostgreSQL docs: Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — the exact semantics you will demonstrate hands-on, including how Postgres's levels map to ANSI (reference)
    - [CMU 15-445: concurrency-control lectures](https://15445.courses.cs.cmu.edu/) — 2PL, timestamp ordering, MVCC internals behind the levels (deepening)
- **Tools:**
    - FOSS (hands-on): [PostgreSQL](https://www.postgresql.org/docs/) in Docker — two psql sessions are the whole lab (↔ Azure SQL)
    - Corp (evaluate): [Azure SQL](https://learn.microsoft.com/azure/azure-sql/) / [Oracle Database](https://docs.oracle.com/en/database/) — default isolation (RCSI in Azure SQL, statement-level read consistency in Oracle) and TDE-era differences at evaluation level
- **Do:**
    1. Start the Phase-1 Postgres container and open two psql sessions side by side.
    2. At `READ COMMITTED`, reproduce a non-repeatable read, a phantom, and write skew on a two-row "fund cash balance" table; save the exact statement interleavings as scripts.
    3. Re-run the same interleavings at `REPEATABLE READ` and `SERIALIZABLE`; record which anomaly each level prevents and which error (40001) the client receives instead.
    4. Write a half-page note on retry behavior: which isolation level a fund-order workload needs, and how the application must respond to a serialization failure.
- **Done when:**
    - [ ] Reproduce write skew and a phantom on demand and explain why snapshot isolation permits write skew.
    - [ ] Explain to a reviewer a fund-accounting scenario where write skew corrupts data, and name the isolation level that prevents it.
    - [ ] State the default isolation level of Postgres, SQL Server, and Oracle, and one migration consequence of the differences.
- Est. hours: 8

#### 1.6.3 + 1.6.4 + 1.6.5 The consistency spectrum — T2
- **Why:** Replicated platforms — read replicas, geo-DR, caches — silently downgrade consistency, and the architect must name the guarantee actually delivered rather than assume "strong". In a fund platform, an investor seeing a confirmed order vanish on refresh is a read-your-writes violation, not a UI bug, and the fix is architectural.
- **Learn:**
    - eventual vs strong consistency — what "eventually" actually promises and what it never does *(DDIA ch. 5)*
    - read-your-writes and monotonic reads — the session guarantees replica reads break first *(DDIA ch. 5)*
    - causal consistency — preserving "question before answer" ordering across replicas *(DDIA ch. 9)*
    - linearizability vs serializability — single-object recency vs multi-object transaction ordering; they answer different questions *(DDIA ch. 9)*
    - where lag bites in practice — replica reads after writes, cross-region failover and the lost-write window *(DDIA ch. 5)*
    - a worked commercial spectrum — Cosmos DB's five levels as the vocabulary Azure design reviews will use *(Cosmos DB docs: consistency levels)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 5 "Replication" + ch. 9 "Consistency and Consensus" (linearizability sections)** — replication-lag anomalies and the formal guarantees behind them (primary)
    - [Jepsen: Consistency Models](https://jepsen.io/consistency) — the definitive map of guarantee names and how they relate (reference)
    - [Azure Cosmos DB: consistency levels](https://learn.microsoft.com/azure/cosmos-db/consistency-levels) — strong → bounded staleness → session → consistent prefix → eventual, productized (Azure framing)
- **Do:**
    1. List the read paths of a fund platform (order-status API, NAV-history dashboard, transfer-agency register lookup) and the replication topology each would realistically sit on.
    2. For each path, name the minimum guarantee it needs (read-your-writes? monotonic? linearizable?) and the user-visible bug if it is violated.
    3. Write the 1-page memo: which consistency level a fund-order status API needs vs a NAV-history dashboard, and what each choice costs in latency and availability.
- **Done when:**
    - [ ] Give a concrete user-visible bug for each violated guarantee (read-your-writes, monotonic reads, causal).
    - [ ] Defend in one sentence why NAV history tolerates staleness but order status does not.
    - [ ] Map each Cosmos DB consistency level to the textbook guarantee it implements.
- Est. hours: 5

#### 1.7.1 + 1.7.2 CAP & PACELC — T1
- **Why:** Every design review invokes CAP, usually wrongly; the architect corrects the record and uses PACELC's latency half, which is what actually drives cloud database selection. Choosing a fund-data store on "CP vs AP" folklore buys either needless latency or unexplained stale reads in regulated reporting.
- **Learn:**
    - what CAP actually states — the narrow definitions of C (linearizability) and A (every non-failed node answers), and why most systems are neither CP nor AP *(DDIA ch. 9: "The Unhelpfulness of CAP")*
    - partition behavior of common systems — what Postgres, Cassandra, and quorum systems each do when the network splits *(DDIA ch. 9)*
    - PACELC — the Else case: latency vs consistency under normal operation, the tradeoff you pay every day *(Abadi PACELC paper)*
    - classifying real systems — PA/EL vs PC/EC labels for Postgres, Cassandra, Cosmos DB, Spanner-style stores *(Abadi PACELC paper)*
    - how the inventor reframed it — Brewer's own corrections twelve years on *(Brewer: CAP Twelve Years Later)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 9** — including "The Unhelpfulness of CAP" (primary)
    - [Abadi, "Consistency Tradeoffs in Modern Distributed Database System Design"](https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf) — the PACELC paper, IEEE Computer 2012 (source)
    - [Brewer, "CAP Twelve Years Later: How the Rules Have Changed"](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/) — the theorem's author on what people get wrong (reference)
- **Do:**
    1. Re-read the CAP definitions and write one paragraph on why a single-region Azure SQL deployment sits outside CAP's frame entirely.
    2. Build the one-table PACELC classification of the 8 stores you'll meet in this plan (Postgres, Cassandra, Kafka, Cosmos DB, DynamoDB, Spanner, Redis, MongoDB) with a one-line justification per row.
    3. Sanity-check the Cosmos DB row against Microsoft's own consistency documentation and note the nuance (per-level tradeoffs) a single label hides.
- **Done when:**
    - [ ] Explain why "CP vs AP" is the wrong frame for a single-region Azure SQL deployment.
    - [ ] Defend each of the 8 PACELC classifications in one sentence without notes.
    - [ ] State the latency cost of choosing consistency in the Else case, with one concrete example.
- Est. hours: 3

#### 1.8.1 Idempotency — T1
- **Why:** Retry-safety is the single biggest reliability lever in pipelines; non-idempotent loads are how funds double-book trades. An architect who cannot point to where idempotency holds in a design has not finished the design — every regulated rerun, replay, and disaster-recovery story depends on it.
- **Learn:**
    - idempotency keys — client-supplied identifiers that make "did this already apply?" answerable *(DDIA ch. 11)*
    - natural vs synthetic dedup — when a business key (order ref, ISIN+date) suffices and when you must mint one *(DDIA ch. 11)*
    - idempotent writes — MERGE/upsert and `INSERT … ON CONFLICT` as the sink-side mechanism *(Postgres docs: INSERT)*
    - idempotent pipeline runs — the overwrite-partition pattern: a rerun rewrites a deterministic slice, never appends *(DDIA ch. 10–11)*
    - effective exactly-once — at-least-once delivery + idempotent consumer; why true exactly-once delivery is a myth *(DDIA ch. 11)*
    - rerun semantics in managed orchestrators — what actually re-executes on failure recovery *(ADF docs)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 10–11** — fault-tolerance and exactly-once sections; rerunnable batch output; taxonomy concept entry as checklist (primary)
    - [PostgreSQL docs: INSERT … ON CONFLICT](https://www.postgresql.org/docs/current/sql-insert.html) — upsert syntax and conflict-handling semantics for the loader (reference)
    - [Azure Data Factory documentation](https://learn.microsoft.com/azure/data-factory/) — pipeline rerun and retry behavior at evaluation level (Azure framing)
- **Tools:**
    - FOSS (hands-on): [PostgreSQL](https://www.postgresql.org/docs/) upserts — the sink for the provably rerunnable loader (↔ ADF + Azure SQL)
    - Corp (evaluate): [Azure Data Factory](https://learn.microsoft.com/azure/data-factory/) — rerun semantics: what state a re-executed activity sees
- **Do:**
    1. Generate a trades CSV (a few thousand rows with order refs and ISINs) and decide the natural dedup key.
    2. Write a Python loader (via `uv run`) that ingests it into Postgres using `INSERT … ON CONFLICT` (or a staged MERGE) so a second run changes nothing.
    3. Prove it: run twice; compare row counts and a whole-table checksum (e.g. `md5(string_agg(…))`) after each run, and commit the evidence to the repo.
    4. Break it deliberately — kill the loader mid-run — then rerun and show the end state is still identical.
- **Done when:**
    - [ ] List the three places idempotency must hold in a pipeline (source read, transform, sink write) and how to get each.
    - [ ] Show identical row counts and checksums after a double run and after a kill-and-rerun.
    - [ ] Explain why "exactly-once" in practice means at-least-once delivery plus an idempotent consumer.
- Est. hours: 4

#### 1.8.9 Distributed transactions & 2PC — T2
- **Why:** You must recognize when someone proposes a distributed transaction and steer to outbox/saga instead — with reasons, not taste. In a fund platform, a blocked 2PC coordinator between an order service and a position service is an outage that holds locks across the books at the worst possible moment.
- **Learn:**
    - the 2PC protocol — prepare and commit phases, and what each participant promises at "prepared" *(DDIA ch. 9)*
    - the blocking failure mode — in-doubt transactions holding locks while the coordinator is down *(DDIA ch. 9)*
    - XA in practice — why heterogeneous distributed transactions rot in real systems *(DDIA ch. 9)*
    - consensus ≠ 2PC — what Raft solves that 2PC does not (no single blocking point) *(Raft site)*
    - modern alternatives preview — transactional outbox and saga, implemented in Phase 4 *(microservices.io: Outbox / Saga)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 9 "Distributed Transactions and Consensus"** — 2PC, in-doubt transactions, XA, consensus (primary)
    - [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html) and [Saga](https://microservices.io/patterns/data/saga.html) — the alternatives your ADR will name (reference)
    - [The Raft consensus algorithm](https://raft.github.io/) — visualization and paper; why consensus is a different problem (deepening)
- **Do:**
    1. Sketch the 2PC message flow for an order-service + position-service write; mark the exact point where coordinator death leaves participants in doubt.
    2. Write down what happens to the participants' locks at that point and who is able to release them.
    3. Write a half-page ADR rejecting 2PC for this hypothetical consistency requirement, naming outbox or saga as the alternative and stating what you give up (atomic visibility) and gain (availability).
- **Done when:**
    - [ ] Explain what happens to locks when a 2PC coordinator dies mid-commit.
    - [ ] Name the alternative pattern in your ADR and the tradeoff it accepts.
    - [ ] Distinguish in two sentences what Raft guarantees that 2PC cannot.
- Est. hours: 5

#### 1.5.1–1.5.4 Storage paradigms — T2
- **Why:** Row vs columnar, shared-nothing vs shared-disk, and storage/compute separation are the axes along which every warehouse/lakehouse vendor differentiates — this is the vocabulary of vendor selection. An architect who cannot derive cost and failure behavior from these decisions ends up reading vendor slides instead of auditing them.
- **Learn:**
    - row vs columnar layouts — why analytical scans love columns and OLTP point-writes love rows *(DDIA ch. 3)*
    - compression and late materialization — why columnar compresses so well and defers row reconstruction *(DDIA ch. 3)*
    - MPP partitioning and data skew — how one hot key turns a 16-node cluster into a 1-node job *(CMU 15-445 storage lectures)*
    - shared-nothing vs shared-disk — which failures stay isolated and which are global *(Snowflake docs: Key Concepts)*
    - separation of storage and compute — the Snowflake/BigQuery model and its cost/elasticity consequences *(Snowflake docs: Key Concepts)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 3 "Storage and Retrieval" (column-store sections)** — layout, compression, materialization (primary)
    - [CMU 15-445: storage lectures 3–5](https://15445.courses.cs.cmu.edu/) — page layout, buffer management, the physical substrate (deepening)
    - [Snowflake docs: Key Concepts & Architecture](https://docs.snowflake.com/en/user-guide/intro-key-concepts) — the canonical storage/compute-separation design, an explicit hybrid of shared-disk and shared-nothing (reference)
- **Tools:**
    - FOSS (hands-on): [DuckDB](https://duckdb.org/docs/) — columnar engine for the CSV-vs-Parquet experiment (↔ Synapse/Snowflake)
    - Corp (evaluate): [Azure Synapse Analytics](https://learn.microsoft.com/azure/synapse-analytics/) — MPP distribution choices (hash / round-robin / replicated) at evaluation level
- **Do:**
    1. Generate a 10M-row trades table (Faker or DuckDB's range functions) and store it as both CSV and Parquet.
    2. Run the same aggregate (e.g. sum of amount grouped by ISIN) over both files in DuckDB; record timings and bytes scanned.
    3. Explain the timing difference in terms of layout, compression, and I/O — not "Parquet is faster" but why.
    4. Sketch the Snowflake-style three-layer architecture and annotate which cost and failure behaviors follow from each separation decision.
- **Done when:**
    - [ ] Sketch the Snowflake-style architecture and say which failure/cost behaviors follow from each separation decision.
    - [ ] Explain the CSV-vs-Parquet timing gap in terms of columnar layout and I/O, with your measured numbers.
    - [ ] Describe one workload where shared-nothing MPP beats storage/compute separation, and one where it loses.
- Est. hours: 4

#### 3.2.1 Relational internals (the database under everything) — T1
- **Why:** Indexing, query planning, MVCC, and recovery ground every storage decision an architect makes; this is the deepest single investment in the plan. Without it you negotiate with DBAs and vendors on faith — with it you can read any engine's documentation and predict its behavior under fund-platform load.
- **Learn:**
    - pages, heap files, and the buffer pool — why the database manages its own cache instead of trusting the OS *(CMU 15-445 storage lectures)*
    - B+trees vs hash vs GIN/BRIN — which Postgres index answers which predicate shape *(Database Internals Part I)*
    - join algorithms and cardinality estimation — how a misestimate produces a nested-loop disaster *(CMU 15-445 joins/optimization lectures)*
    - MVCC, vacuum, and bloat — why updates copy rows and what unchecked bloat does to NAV-history tables *(Postgres docs: MVCC)*
    - WAL, checkpoints, crash recovery — ARIES-style logging and what fsync actually buys *(CMU 15-445 logging/recovery lectures)*
    - reading `EXPLAIN (ANALYZE, BUFFERS)` — where time and I/O go in a real plan *(Postgres docs: Using EXPLAIN)*
    - connection pooling — why a fund platform fronts Postgres with a pooler, and pooling modes *(PgBouncer docs)*
    - table partitioning — when partition pruning helps and when it just adds planning cost *(Postgres docs: Table Partitioning)*
- **Resources:**
    - **[CMU 15-445/645 (latest year)](https://15445.courses.cs.cmu.edu/)** — lectures + notes for storage, buffer pool, indexes, sorting/joins, query optimization, MVCC, logging/recovery (~14 of 26 lectures) (primary)
    - [*Database Internals* (Petrov), Part I](https://www.databass.dev/) — storage-engine and B-tree internals in book form (alternate/deepening)
    - [PostgreSQL docs: Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — plus the [MVCC](https://www.postgresql.org/docs/current/mvcc.html) and [Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html) chapters — the exact engine you tune (reference)
    - [PgBouncer docs](https://www.pgbouncer.org/) — session vs transaction pooling and their gotchas (reference)
- **Tools:**
    - FOSS (hands-on): [PostgreSQL 16](https://www.postgresql.org/docs/) with `EXPLAIN (ANALYZE, BUFFERS)` and [pgbench](https://www.postgresql.org/docs/current/pgbench.html) — the lab engine (↔ Azure SQL)
    - Corp (evaluate): [Azure SQL](https://learn.microsoft.com/azure/azure-sql/) / [Oracle Database](https://docs.oracle.com/en/database/) — planner-hint culture and licensing economics at evaluation level
- **Do:**
    1. Build (or reuse the capstone seed of) a 5-table fund-holdings schema in Postgres and load enough Faker data that scans hurt — millions of rows in holdings and NAV history.
    2. Write a deliberately slow 5-table fund-holdings query; capture its plan with `EXPLAIN (ANALYZE, BUFFERS)`.
    3. Fix it step by step — indexes, statistics targets, rewrites — to a 10× improvement, re-capturing the plan after every change.
    4. Run pgbench before and after to show the throughput effect, and write up the before/after plans narrating where time went.
    5. Demonstrate MVCC bloat on the side: update a large table in a loop, watch the table size grow, VACUUM, and explain what happened.
- **Done when:**
    - [ ] Read an unfamiliar `EXPLAIN ANALYZE` and narrate where time goes and why the planner chose the join order it did.
    - [ ] Show a documented 10× improvement with before/after plans and the reasoning behind each fix.
    - [ ] Explain MVCC bloat and vacuum using your own measured table sizes.
    - [ ] Pick the right index type (B+tree / hash / GIN / BRIN) for four different predicate shapes and justify each.
- Est. hours: 30

#### 8.2.1 + 8.2.2 + 8.2.3 Conceptual → logical → physical modeling — T1
- **Why:** The three-level discipline is the architect's signature artifact chain — business entities to keys/normal forms to engine-specific DDL — and the basis for every review you'll run. Skip a level and you get ISIN-as-primary-key databases that cannot survive a corporate action, or "logical" models silently welded to one engine.
- **Learn:**
    - conceptual entity modeling — naming the business things (fund, share class, investor) and knowing when to stop *(DMBOK ch. 5)*
    - logical keys — candidate vs natural vs surrogate, and why ISIN is an attribute, not a primary key *(DMBOK ch. 5)*
    - normalization 1NF–BCNF — what each form forbids, plus deliberate, documented denormalization *(Hoberman)*
    - physical design — data types, partitioning, and indexes chosen per target engine *(Postgres docs: Table Partitioning)*
    - forward/reverse engineering — round-tripping between model and DDL without drift *(DMBOK ch. 5)*
    - notation fluency — write Crow's Foot, read IDEF1X *(Hoberman)*
- **Resources:**
    - **[DAMA-DMBOK](https://www.dama.org/cpages/body-of-knowledge) ch. 5 "Data Modeling and Design"** — the three-level discipline in the governance framing EU institutions recognize (primary)
    - [Hoberman, *Data Modeling Made Simple* (Technics Publications)](https://technicspublications.com/) — keys, normal forms, and notations in plain language (alternate)
    - [PostgreSQL docs: Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html) — the physical-level mechanics for the NAV-history design (reference)
- **Tools:**
    - FOSS (hands-on): [draw.io](https://www.drawio.com/) / [DBeaver](https://dbeaver.io/) ERD — conceptual/logical diagrams and reverse engineering (↔ erwin)
    - Corp (evaluate): [erwin Data Modeler](https://www.quest.com/erwin/) / [ER/Studio](https://www.idera.com/) / [SqlDBM](https://sqldbm.com/) — what EU banks actually license: model repositories, round-trip engineering, governance hooks
- **Do:**
    1. Model the fund domain conceptually — fund, share class, investor, order, NAV — entities and relationships only, one page.
    2. Derive the logical model: candidate keys per entity, surrogate-key decisions justified in writing, normal form stated and defended per table.
    3. Produce the physical model as Postgres DDL — types, constraints, declarative partitioning for NAV history; reverse-engineer it in DBeaver and diff against your logical model.
    4. Self-review the chain after a week against one test: could a colleague implement from the logical model alone?
- **Done when:**
    - [ ] Hand a colleague the logical model and they can implement it without asking you questions.
    - [ ] State a reason for every surrogate-key choice — including why ISIN is not your PK.
    - [ ] Name the normal form of each table and where you denormalized deliberately, and why.
- Est. hours: 12

#### 8.2.4 Dimensional modeling — T1
- **Why:** Kimball stars remain the dominant analytical model in regulated reporting marts; fund NAV/holdings/fees reporting is textbook dimensional territory. An architect who cannot state a fact table's grain in one sentence cannot review a mart — and ungrained fact tables are where double-counted AUM reports come from.
- **Learn:**
    - fact table grain — declare it first, always; every other decision follows from it *(DWT ch. 1–2)*
    - fact types — transaction, periodic snapshot, accumulating snapshot; NAV is a periodic snapshot *(Kimball techniques: fact tables)*
    - conformed dimensions and the bus matrix — how marts stay joinable across business processes *(DWT ch. 4)*
    - SCD types 1/2/3/6 — security/fund reference data is SCD2 country *(Kimball techniques: SCDs)*
    - junk and degenerate dimensions — where order numbers and flag clusters belong *(Kimball techniques)*
    - star vs snowflake — and why snowflaking is usually a modeling smell in marts *(DWT ch. 1)*
    - financial-services patterns — accounts, heterogeneous products, fee facts *(DWT ch. 19)*
- **Resources:**
    - **[Kimball & Ross, *The Data Warehouse Toolkit* 3rd ed.](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/) ch. 1–4 + ch. 19 (financial services)** — grain, fact types, SCDs, bus matrix, finance patterns (primary)
    - [Kimball Group: Dimensional Modeling Techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/) — the full technique catalog, free, for lookup during design (reference)
    - [Corr & Stagnitto, *Agile Data Warehouse Design*](https://books.google.com/books/about/Agile_Data_Warehouse_Design.html?id=TRWFmnv8jP0C) — BEAM workshops for modeling with business stakeholders (alternate)
- **Tools:**
    - FOSS (hands-on): [dbt Core](https://docs.getdbt.com/) + [DuckDB](https://duckdb.org/docs/) — implement the star and SCD2 logic as versioned models (↔ Synapse/Snowflake marts)
    - Corp (evaluate): [Azure Synapse](https://learn.microsoft.com/azure/synapse-analytics/) / [Snowflake](https://docs.snowflake.com/) — the same patterns on licensed mart engines
- **Do:**
    1. Design the bus matrix for a fund administrator — processes: orders, NAV calculation, fee accrual, transfer agency — against conformed dimensions (fund, share class, investor, date).
    2. Declare the grain of each fact table in one written sentence before touching any column list.
    3. Implement the NAV periodic-snapshot star in SQL (dbt + DuckDB) with an SCD2 fund dimension (valid_from / valid_to + current flag).
    4. Write the point-in-time query joining the snapshot fact to the SCD2 dimension as of an arbitrary historical date; test it across at least one attribute change.
- **Done when:**
    - [ ] State the grain of each fact table in one sentence.
    - [ ] Show an SCD2 query returning point-in-time-correct fund attributes for any historical date.
    - [ ] Justify each dimension in the bus matrix as conformed, junk, or degenerate.
- Est. hours: 16

#### 8.5.1 Architecture notations & decision records (C4, ADR) — T1
- **Why:** C4 diagrams and ADRs are the artifacts that define the architect role in practice — they make your reasoning reviewable and your decisions auditable, which is exactly what a regulated fund administrator's IT governance expects. Without them, your designs live in slide decks and hallway memory, and the audit trail for "why is NAV history partitioned this way?" is you.
- **Learn:**
    - C4 levels — context, container, component, code; why most architecture work stops at container *(c4model.com)*
    - diagrams-as-code — text-defined models that diff and review in Git like everything else *(c4model.com)*
    - ADR anatomy — context, decision, consequences; short enough that people actually write them *(adr.github.io)*
    - ADR lifecycle — proposed / accepted / superseded; never rewrite history, supersede it *(adr.github.io: MADR)*
    - lightweight RFC processes — when a decision needs review before an ADR records it *(FoSA: decision chapters)*
    - what reviewers look for — boundaries, data flows, and the decisions you didn't write down *(FoSA: decision chapters)*
- **Resources:**
    - **[c4model.com](https://c4model.com/) (full read)** — levels, notation, diagrams-as-code guidance (primary)
    - [adr.github.io](https://adr.github.io/) — ADR formats including the [MADR template](https://adr.github.io/madr/) and lifecycle conventions (reference)
    - [Richards & Ford, *Fundamentals of Software Architecture*](https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/) — the chapters on diagramming and architecture decisions (alternate/deepening)
- **Tools:**
    - FOSS (hands-on): [Structurizr Lite](https://docs.structurizr.com/lite) (Docker) or [Mermaid C4](https://mermaid.js.org/syntax/c4.html) — diagrams-as-code in the repo (↔ Sparx EA)
    - Corp (evaluate): [Sparx Enterprise Architect](https://sparxsystems.com/) / [Visual Paradigm](https://www.visual-paradigm.com/) — the EA suites EU institutions license: model repositories, traceability, governance
- **Do:**
    1. Pick an existing system you know from work and draw its C4 context diagram: actors, system boundary, external dependencies.
    2. Add the container diagram: deployable units, datastores, and the protocol on every arrow.
    3. Express both as code (Structurizr DSL or Mermaid C4) committed to Git — not a drawing export.
    4. Write 2 retroactive ADRs (MADR format) for that system's key decisions, including one that was later superseded, to model the lifecycle.
    5. Set up the `adr/` directory convention you will reuse in every capstone from here on.
- **Done when:**
    - [ ] Ship C4 + ADRs with every capstone from here on without thinking about it (the capstones enforce this).
    - [ ] Explain when to stop at container level and what would force a component diagram.
    - [ ] Show an ADR pair where one supersedes the other with the status trail intact.
- Est. hours: 8

#### 1.10.1 Modeling notations overview — T2
- **Why:** You need reading fluency across UML/BPMN/DMN/ArchiMate before Phase 4 (BPM) and Phase 8 (ArchiMate practice) go deep. In fund-industry workshops the BA brings BPMN, the vendor brings ArchiMate, and the DBA brings ERDs — the architect is the one who reads all of them without a translator.
- **Learn:**
    - UML class/sequence — system structure and interaction behavior, reading level only *(OMG spec: UML)*
    - BPMN — executable business-process notation (order lifecycle, transfer-agency flows) *(OMG spec: BPMN)*
    - DMN — decision tables and logic, separated from process flow *(OMG spec: DMN)*
    - ArchiMate — business/application/technology layers in one enterprise language *(Open Group: ArchiMate overview)*
    - ERD / IDEF1X — data-modeling notations and where each is still mandated *(DMBOK ch. 5)*
    - C4 — software architecture; which question each notation answers and which it cannot *(c4model.com)*
- **Resources:**
    - **[OMG spec: UML](https://www.omg.org/spec/UML/), [BPMN](https://www.omg.org/spec/BPMN/), [DMN](https://www.omg.org/spec/DMN/)** — read the intro/overview sections of each spec, plus one example diagram each; not the full documents (primary)
    - [The Open Group: ArchiMate overview](https://www.opengroup.org/archimate-forum/archimate-overview) — the enterprise-layer language Phase 8 practices (reference)
    - [c4model.com](https://c4model.com/) — the software-architecture notation already in your toolkit, for contrast (reference)
    - [DAMA-DMBOK](https://www.dama.org/cpages/body-of-knowledge) ch. 5 — ERD/IDEF1X grounding on the data side (reference)
- **Do:**
    1. Collect one example diagram of each notation (from the spec intros and c4model.com) into a reference folder.
    2. Make the one-page "notation chooser" cheat sheet: question → notation → tool, with a fund-industry example question per row (e.g. "how does an order get from EMT file to register?" → BPMN).
    3. Test yourself: take three unfamiliar diagrams, identify each notation, and narrate what the diagram says.
- **Done when:**
    - [ ] Name the notation and read it correctly when shown a diagram cold.
    - [ ] Produce the one-page cheat sheet mapping question → notation → tool.
    - [ ] Give a fund-industry example question for each notation.
- Est. hours: 2

#### 9.1.3 Local data sandboxes — T2
- **Why:** The entire 4-year lab runs on reproducible local stacks; compose fluency is the substrate for every capstone. A stack a stranger cannot bring up identically is a lab you cannot trust — the same discipline that later makes your Azure environments reviewable.
- **Learn:**
    - Compose service graphs — `depends_on`, startup ordering, and what Compose does not guarantee *(Compose docs)*
    - healthchecks — gating dependents on actual readiness (`service_healthy`), not container start *(Compose docs)*
    - volumes and networks — named volumes for state, isolated networks per stack *(Compose docs)*
    - image pinning — exact tags (or digests) so the stack reproduces across machines and months *(Compose docs)*
    - the Testcontainers idea — programmatic throwaway infrastructure for tests *(testcontainers.com)*
    - DuckDB as a zero-infra warehouse — when a file beats a service *(DuckDB docs)*
- **Resources:**
    - **[Docker Compose docs](https://docs.docker.com/compose/)** — top-level concepts, healthchecks, volumes, networks; builds directly on Phase 0's module 0.5 (primary)
    - [Testcontainers](https://testcontainers.com/) — the programmatic throwaway-infra pattern, for awareness (reference)
    - [DuckDB docs](https://duckdb.org/docs/) — the zero-infra analytical engine in the same stack (reference)
- **Tools:**
    - FOSS (hands-on): [Docker Compose](https://docs.docker.com/compose/), [PostgreSQL](https://www.postgresql.org/docs/), [MinIO](https://github.com/minio/minio), [DuckDB](https://duckdb.org/docs/), [Testcontainers](https://testcontainers.com/) — the lab substrate (↔ Azure dev environments)
    - Corp (awareness): [GitHub Codespaces](https://docs.github.com/codespaces) / dev containers — the managed equivalent of the same reproducibility idea
- **Do:**
    1. Write the `docker-compose.yml` you'll grow all four years: Postgres + MinIO + a placeholder service.
    2. Add healthchecks to every service and make dependents wait on `service_healthy`, not just `service_started`.
    3. Put all state on named volumes and pin every image to a specific version tag.
    4. Test from a fresh clone on a clean Docker (prune first): time `docker compose up` until everything reports healthy.
- **Done when:**
    - [ ] Run `docker compose up` on a fresh clone and get a clean, healthy stack in under 2 minutes.
    - [ ] Show every image pinned and every stateful service on a named volume.
    - [ ] Explain the difference between `service_started` and `service_healthy` and why a loader needs the latter.
- Est. hours: 4

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.3.3 | HTAP (workload) | One system serving OLTP + OLAP; niche but recurring vendor pitch | [DDIA ch. 3 (closing section)](https://dataintensive.net/) | 30 |
| 1.6.2 | BASE | Marketing-era label for eventual-consistency systems; know it to translate it in vendor decks | [DDIA ch. 5 intro](https://dataintensive.net/) | 15 |
| 3.2.2 | NoSQL document stores | JSON-document storage (MongoDB); flexible schema, integrity owned by the app | [DDIA ch. 2 (document model)](https://dataintensive.net/) | 45 |
| 3.2.3 | NoSQL key-value | High-throughput KV (Redis/Valkey, DynamoDB); caching + session state | [DDIA ch. 3 (hash indexes)](https://dataintensive.net/) | 30 |
| 3.2.4 | NoSQL wide-column | Sparse-column distributed stores (Cassandra); write-heavy, query-first design | [DDIA ch. 2](https://dataintensive.net/) + [Cassandra docs "data modeling" intro](https://cassandra.apache.org/doc/latest/cassandra/developing/data-modeling/intro.html) | 45 |
| 3.2.10 | HTAP stores | TiDB/SingleStore implementations of 1.3.3 | [TiDB docs](https://docs.pingcap.com/tidb/stable/) + [SingleStore docs](https://docs.singlestore.com/) | 15 |

*T3 subtotal: 3 h*

### Capstone 1 — Fund reference OLTP + reporting mart

- **Goal:** a correct, documented foundation: operational fund reference database + dimensional reporting mart, the seed every later phase builds on.
- **Stack (100% free):** [PostgreSQL 16](https://www.postgresql.org/docs/) (↔ [Azure SQL](https://learn.microsoft.com/azure/azure-sql/) / [Oracle DB](https://docs.oracle.com/en/database/)), [DuckDB](https://duckdb.org/docs/) (↔ [Synapse](https://learn.microsoft.com/azure/synapse-analytics/)/[Snowflake](https://docs.snowflake.com/) mart), [dbt Core](https://docs.getdbt.com/) seed/models for the mart (↔ [dbt Cloud](https://www.getdbt.com/)), [Structurizr Lite](https://docs.structurizr.com/lite) (↔ [Sparx EA](https://sparxsystems.com/)), [Docker Compose](https://docs.docker.com/compose/), Python via [uv](https://docs.astral.sh/uv/), [Faker](https://faker.readthedocs.io/) for sample data (↔ [Tonic.ai](https://www.tonic.ai/)/[Delphix](https://www.delphix.com/)).
- **Build:** (1) implement the Phase-1 physical model in Postgres: funds, share classes, ISIN-keyed securities, investors, orders, NAV history (declaratively partitioned by date, per 8.2.1); (2) load Faker-generated but referentially consistent data with the idempotent loader from 1.8.1, using order refs as the natural dedup key; (3) build the NAV periodic-snapshot star + SCD2 fund dimension in DuckDB as dbt models (per 8.2.4); (4) one deliberately slow query, tuned with the 3.2.1 method, with before/after `EXPLAIN (ANALYZE, BUFFERS)` plans committed to the repo.
- **Architecture deliverables:** C4 context + container diagrams; ADR-001 (surrogate vs natural keys — why ISIN is not your PK), ADR-002 (SCD2 for fund attributes), ADR-003 (partitioning scheme for NAV history).
- **Acceptance criteria:** loader runs twice with identical end state (row counts + checksums committed as evidence); point-in-time query returns correct fund attributes for any historical date, demonstrated across at least one SCD2 attribute change; tuned query ≥10× faster with written plan analysis; a stranger can run `docker compose up && uv run load.py` from the README and get the same numbers — verified on a clean clone before calling it done.
- Est. hours: 14

*Phase 1 total: 118 h (T1/T2 entries 101 h + T3 3 h + capstone 14 h)*
