# Data Architecture Learning Guide

A three-level taxonomy (Domain → Category → Subcategory) with descriptions, book references, and tool/vendor references. Followed by full book and tool reference sections.

**Notation in tool references:** `(OS)` open-source (OSI-approved license), `(SA)` source-available (e.g., BSL, SSPL, CCL, Elastic License v2 — readable but not OSI-approved), `(C)` cloud-managed, `(E)` enterprise/proprietary on-prem. A tool may have several tags.

**Section icons used throughout the taxonomy:** 📚 books · 🛠 tools · 📐 concepts/patterns · 📜 standards/protocols. Concepts and standards have their own reference section after Books.

---

## Table of Contents

1. [Fundamentals](#1-fundamentals)
2. [Connectivity](#2-connectivity)
3. [Storage](#3-storage)
4. [Compute](#4-compute)
5. [Processing](#5-processing)
6. [AI/ML](#6-aiml)
7. [Semantic](#7-semantic)
8. [Architecture](#8-architecture)
9. [Engineering Practice](#9-engineering-practice)
10. [Governance](#10-governance)
11. [Security & Compliance](#11-security--compliance)
12. [Operations](#12-operations)
13. [Data Products](#13-data-products)
14. [Consumption](#14-consumption)
15. [Concepts, Patterns & Standards — Reference List](#concepts-patterns--standards--reference-list)
16. [Books — Reference List](#books--reference-list)
17. [Tools & Vendors — Reference List](#tools--vendors--reference-list)

---

## 1. Fundamentals

The conceptual scaffolding underpinning every other domain — data types, processing paradigms, workload classes, architectural patterns, storage paradigms, consistency models, theorems, modeling notations, integration patterns, streaming semantics, and data protocols. Anchors throughout this guide: 📐 concepts/patterns and 📜 standards/protocols cross-link to the [Concepts, Patterns & Standards reference list](#concepts-patterns--standards--reference-list).

📚 **Primary books:** [Designing Data-Intensive Applications](#b-ddia), [Fundamentals of Data Engineering](#b-fode), [DAMA-DMBOK](#b-dama)

### 1.1 Data Types

How data is shaped before any tool touches it.

- **Structured** — fixed schema, rows and columns (relational tables, CSV).
- **Semi-Structured** — schema embedded in payload (JSON, XML, Avro, Parquet).
- **Unstructured** — no schema (free text, images, audio, video).
- **Vector / Embeddings** — high-dimensional numeric arrays representing learned features; the substrate for similarity search and RAG.

📚 [DDIA](#b-ddia) ch. 2 (data models) · [Fundamentals of Data Engineering](#b-fode) ch. 1

### 1.2 Processing Paradigms

When and how data is processed relative to its arrival.

- **Batch** — bounded datasets processed on a schedule.
- **Micro-Batch** — small frequent batches (e.g., Spark Structured Streaming).
- **Streaming** — unbounded event-by-event processing.
- **Real-Time / Low-Latency** — sub-second response paths.

📚 [Streaming Systems](#b-streaming) · [DDIA](#b-ddia) ch. 10–11

### 1.3 Workload Types

The shape of access patterns that drives storage choice.

- **OLTP** — transactional, row-oriented, high concurrency, short queries.
- **OLAP** — analytical, columnar, scan-heavy, long queries.
- **HTAP** — hybrid systems serving both (TiDB, SingleStore).
- **Real-Time / User-Facing Analytics** — sub-second queries, high concurrency, customer-facing dashboards (Pinot, Druid, ClickHouse, StarRocks).

📚 [DDIA](#b-ddia) ch. 3 · [Data Warehouse Toolkit](#b-kimball)

### 1.4 Architectural Patterns

Reusable structural patterns for whole-platform design.

- **Lambda Architecture** — batch + speed layers reconciled at query time.
- **Kappa Architecture** — stream-only, replay for reprocessing.
- **Medallion (Bronze/Silver/Gold)** — progressive refinement layers in a lakehouse.
- **Data Mesh** — domain-oriented decentralized ownership.
- **Data Fabric** — unified metadata-driven access layer.
- **Hub-and-Spoke** — centralized hub feeding domain marts.
- **Data Vault** — modeling pattern emphasizing auditability (Hubs/Links/Satellites).

📚 [Data Management at Scale](#b-dms) · [Data Mesh](#b-mesh) · [Building the Data Lakehouse](#b-lakehouse) · [Data Vault 2.0](#b-vault)

### 1.5 Storage Paradigms

How bytes are physically organized.

- **Row-Oriented vs Columnar** — row layouts for OLTP, columnar for OLAP scans.
- **MPP (Massively Parallel Processing)** — partitioned data, parallel workers.
- **Shared-Nothing vs Shared-Disk** — node-local data vs shared SAN.
- **Separation of Storage and Compute** — independently scaled (Snowflake/BigQuery model).

📚 [DDIA](#b-ddia) ch. 3 · [Building the Data Lakehouse](#b-lakehouse)

### 1.6 Consistency Models

What guarantees the system gives readers and writers.

- **ACID** — atomicity, consistency, isolation, durability (classical OLTP).
- **BASE** — basically available, soft state, eventual consistency.
- **Eventual Consistency** — replicas converge over time.
- **Strong Consistency** — every read sees the latest write.
- **Read-Your-Writes**, **Monotonic Reads**, **Causal Consistency** — intermediate consistency levels.

📚 [DDIA](#b-ddia) ch. 7, 9

### 1.7 Theorems

The fundamental tradeoffs.

- **CAP** — under partition, choose consistency or availability.
- **PACELC** — extends CAP by also reasoning about latency in the no-partition case.

📚 [DDIA](#b-ddia) ch. 9

### 1.8 Integration Patterns

Reusable patterns for moving data and events between systems reliably.

📐 **Concepts:** [Idempotency](#c-idempotency), [Exactly-Once vs At-Least-Once vs At-Most-Once](#c-delivery-semantics), [Outbox Pattern](#c-outbox), [Saga Pattern](#c-saga), [Event Sourcing](#c-event-sourcing), [CQRS](#c-cqrs), [Dead-Letter Queue](#c-dlq), [Backpressure](#c-backpressure), [Two-Phase Commit](#c-2pc), [Change Data Capture](#c-cdc-pattern), [Strangler Fig](#c-strangler), [Bulkhead](#c-bulkhead), [Circuit Breaker](#c-circuit-breaker)

📚 [Designing Event-Driven Systems](#b-eds) · [DDIA](#b-ddia) ch. 11

### 1.9 Streaming Semantics

The conceptual machinery of stream processing.

📐 **Concepts:** [Watermarks](#c-watermarks), [Windowing (Tumbling/Sliding/Session/Global)](#c-windowing), [Late Data Handling](#c-late-data), [Event Time vs Processing Time](#c-event-time), [Triggers](#c-triggers), [Stateful vs Stateless Processing](#c-stateful), [Schema Evolution Compatibility (forward/backward/full)](#c-schema-compat)

📚 [Streaming Systems](#b-streaming) (canonical)

### 1.10 Modeling Notations

Standard visual languages for modeling data, processes, and behavior.

📜 **Standards:** [UML (Unified Modeling Language)](#s-uml), [BPMN 2.0 (Business Process Model and Notation)](#s-bpmn), [DMN (Decision Model and Notation)](#s-dmn), [CMMN (Case Management Model and Notation)](#s-cmmn), [ArchiMate](#s-archimate), [IDEF1X](#s-idef1x), [ERD (Entity-Relationship Diagram)](#s-erd), [C4 Model](#s-c4)

UML covers structural/behavioral diagrams (class, sequence, state, activity). BPMN models executable business processes. DMN models decision logic separate from process flow. ArchiMate models enterprise architecture. C4 is a lightweight architecture-diagramming method. ERD/IDEF1X are data-modeling notations.

📚 [Building Evolutionary Architectures](#b-evolutionary) · [DAMA-DMBOK](#b-dama)

### 1.11 Data Protocols & Wire Formats

How systems exchange data over the wire.

📜 **Protocols:** [HTTP/HTTPS](#s-http), [gRPC](#s-grpc), [GraphQL](#s-graphql), [WebSocket](#s-websocket), [MQTT](#s-mqtt), [AMQP](#s-amqp), [STOMP](#s-stomp), [JDBC](#s-jdbc), [ODBC](#s-odbc), [Arrow Flight / Flight SQL](#s-arrow-flight), [ADBC](#s-adbc), [Kafka Wire Protocol](#s-kafka-wire), [PostgreSQL Wire Protocol](#s-pg-wire), [SPARQL Protocol](#s-sparql-protocol), [OData](#s-odata), [SOAP](#s-soap)

📜 **Serialization formats:** [JSON](#s-json), [XML](#s-xml), [YAML](#s-yaml), [Protocol Buffers (Protobuf)](#s-protobuf), [Avro](#s-avro-format), [MessagePack](#s-msgpack), [Thrift](#s-thrift), [FlatBuffers](#s-flatbuffers), [Cap'n Proto](#s-capnp), [CBOR](#s-cbor)

📜 **Async API standards:** [AsyncAPI](#s-asyncapi), [CloudEvents](#s-cloudevents), [OpenAPI](#s-openapi)

### 1.12 Financial Services Standards & Protocols

Domain standards directly relevant to Clearstream/Kneip work.

📜 **Standards:** [ISO 20022](#s-iso20022), [ISO 17442 (LEI)](#s-lei), [ISIN](#s-isin), [CFI](#s-cfi), [FIGI](#s-figi), [FIBO](#s-fibo), [EMT/EPT (FinDatEx)](#s-emt-ept), [SWIFT MT/MX](#s-swift), [FpML](#s-fpml), [FIX Protocol](#s-fix), [SEPA / ISO 13616 (IBAN)](#s-iban), [DCAM (EDM Council)](#s-dcam)

DCAM is the **Data Capability Assessment Model** by the EDM Council — financial-services-focused governance framework parallel to (and often used alongside) DAMA-DMBOK.

---

## 2. Connectivity

Moving data between systems — getting it in, getting it out, keeping it in sync.

📚 **Primary books:** [Fundamentals of Data Engineering](#b-fode) ch. 5–8 · [Designing Event-Driven Systems](#b-eds)

### 2.1 Batch Ingestion

Scheduled bulk loads from sources to a destination.

- **ELT/ELT Connectors** — managed connector libraries that extract on a schedule.
  🛠 [Fivetran](#t-fivetran), [Airbyte](#t-airbyte), [Stitch](#t-stitch), [Matillion](#t-matillion), [Talend](#t-talend)
- **Bulk Load Utilities** — provider-native bulk movement tools.
  🛠 [AWS DMS](#t-awsdms), [Azure Data Factory](#t-adf), [GCP Data Transfer Service](#t-gcpdts), [Apache Sqoop](#t-sqoop) (legacy)

### 2.2 Streaming Ingestion

Continuous low-latency pipelines from event-producing sources.

- **Log/Metric Shippers** — agents that tail logs and forward.
  🛠 [Fluentd](#t-fluentd), [Fluent Bit](#t-fluentbit), [Logstash](#t-logstash), [Vector](#t-vector), [Filebeat](#t-filebeat)
- **Stream Connectors** — pluggable adapters between event platforms and sinks.
  🛠 [Kafka Connect](#t-kafkaconnect), [Debezium](#t-debezium), [AWS Kinesis Firehose](#t-firehose)

📚 [Streaming Systems](#b-streaming) · [Kafka: The Definitive Guide](#b-kafka)

### 2.3 CDC (Change Data Capture)

Capturing row-level changes in source databases for downstream replication.

- **Log-Based CDC** — read the database transaction log (lowest impact).
  🛠 [Debezium](#t-debezium), [AWS DMS](#t-awsdms), [Oracle GoldenGate](#t-goldengate), [Qlik Replicate](#t-qlikreplicate), [Striim](#t-striim)
- **Trigger-Based CDC** — DB triggers populate a change table.
  🛠 [HVR](#t-hvr) (now Fivetran HVR)
- **Snapshot-Based** — periodic diff comparisons.
  🛠 [Fivetran](#t-fivetran), [Airbyte](#t-airbyte)

📚 [DDIA](#b-ddia) ch. 11

### 2.4 Event Streaming Platforms

Durable, ordered, replayable event logs and message buses.

- **Distributed Logs** — partitioned append-only logs.
  🛠 [Apache Kafka](#t-kafka), [Confluent Cloud](#t-confluent), [AWS MSK](#t-msk), [Redpanda](#t-redpanda), [Apache Pulsar](#t-pulsar), [Azure Event Hubs](#t-eventhubs), [AWS Kinesis](#t-kinesis), [GCP Pub/Sub](#t-pubsub)
- **Message Brokers** — classical queue/topic semantics.
  🛠 [RabbitMQ](#t-rabbitmq), [ActiveMQ](#t-activemq), [NATS](#t-nats), [AWS SQS](#t-sqs)
- **Event Mesh** — distributed event routing across cloud/on-prem boundaries.
  🛠 [Solace PubSub+](#t-solace), [TIBCO Cloud Messaging](#t-tibco), [AWS EventBridge](#t-eventbridge)

📐 **Concepts:** [Pub/Sub](#c-pubsub), [Event Sourcing](#c-event-sourcing), [CQRS](#c-cqrs), [Outbox Pattern](#c-outbox), [Saga](#c-saga), [Dead-Letter Queue](#c-dlq), [Backpressure](#c-backpressure), [Delivery Semantics](#c-delivery-semantics)
📜 **Standards:** [AsyncAPI](#s-asyncapi) (events what OpenAPI is to REST), [CloudEvents](#s-cloudevents) (CNCF event envelope spec), [MQTT](#s-mqtt), [AMQP](#s-amqp), [Kafka Wire Protocol](#s-kafka-wire)

📚 [Designing Event-Driven Systems](#b-eds) · [Kafka: The Definitive Guide](#b-kafka)

### 2.5 Integration Platforms (iPaaS)

Workflow-style B2B and SaaS integrations.

- **iPaaS** — visual workflow builders for cross-system integration.
  🛠 [MuleSoft](#t-mulesoft), [Boomi](#t-boomi), [Workato](#t-workato), [Zapier](#t-zapier), [Microsoft Power Automate](#t-powerautomate), [n8n](#t-n8n)
- **ESB (legacy)** — enterprise service buses.
  🛠 [IBM Integration Bus](#t-ibmib), [TIBCO BusinessWorks](#t-tibco)

### 2.6 API Management / Data APIs

Exposing data as governed API endpoints.

📜 **Standards:** [OpenAPI](#s-openapi), [GraphQL](#s-graphql), [gRPC](#s-grpc), [JSON:API](#s-jsonapi), [OData](#s-odata), [HATEOAS / REST](#s-rest)

- **API Gateways** — auth, throttling, routing.
  🛠 [Kong](#t-kong), [Apigee](#t-apigee), [AWS API Gateway](#t-awsapigw), [Tyk](#t-tyk)
- **GraphQL Layers** — schema-driven query APIs over data.
  🛠 [Hasura](#t-hasura), [PostGraphile](#t-postgraphile), [Apollo](#t-apollo)

### 2.7 Reverse ETL

Pushing modeled warehouse data back into operational/SaaS tools.

- **Operational Sync** — sync warehouse rows to CRM, support tools, marketing.
  🛠 [Hightouch](#t-hightouch), [Census](#t-census), [Polytomic](#t-polytomic), [RudderStack](#t-rudderstack) (also a CDP)

---

## 3. Storage

Where data lives — analytical, operational, infrastructure layers, and the file/table formats they use.

📚 **Primary books:** [DDIA](#b-ddia) · [The Data Warehouse Toolkit](#b-kimball) · [Building the Data Lakehouse](#b-lakehouse)

### 3.1 Analytical Storage

Optimized for scan-heavy, aggregate-heavy workloads.

- **Cloud Data Warehouse** — managed columnar MPP services.
  🛠 [Snowflake](#t-snowflake), [BigQuery](#t-bigquery), [Redshift](#t-redshift), [Azure Synapse](#t-synapse), [Databricks SQL Warehouse](#t-databricks), [Firebolt](#t-firebolt)
- **On-Prem MPP Warehouse** — classical appliance/software MPP.
  🛠 [Teradata](#t-teradata), [Vertica](#t-vertica), [Greenplum](#t-greenplum), [IBM Netezza](#t-netezza), [Exasol](#t-exasol)
- **Data Lake** — object storage + open formats.
  🛠 [AWS S3](#t-s3) + Parquet, [ADLS Gen2](#t-adls), [GCS](#t-gcs), [HDFS](#t-hdfs), [MinIO](#t-minio)
- **Data Lakehouse** — lake + ACID table format + warehouse-grade SQL.
  🛠 [Databricks](#t-databricks), [Snowflake](#t-snowflake) + Iceberg, [Dremio](#t-dremio), [Onehouse](#t-onehouse)

📚 [Kimball](#b-kimball) · [Inmon Lakehouse](#b-lakehouse)

### 3.2 Operational Storage

Optimized for transactional / low-latency lookup workloads.

- **OLTP / Relational** — row-store ACID databases.
  🛠 [PostgreSQL](#t-postgres), [MySQL](#t-mysql), [Oracle DB](#t-oracle), [SQL Server](#t-sqlserver), [AWS RDS/Aurora](#t-rds), [Azure SQL](#t-azuresql), [Cloud SQL](#t-cloudsql), [CockroachDB](#t-cockroach)
- **NoSQL Document** — JSON-document oriented stores.
  🛠 [MongoDB](#t-mongo), [Couchbase](#t-couchbase), [AWS DocumentDB](#t-docdb), [Firestore](#t-firestore)
- **NoSQL Key-Value** — high-throughput KV stores.
  🛠 [Redis](#t-redis) / [Valkey](#t-valkey), [DynamoDB](#t-dynamodb), [Riak](#t-riak), [Aerospike](#t-aerospike)
- **NoSQL Wide-Column** — distributed sparse-column stores.
  🛠 [Cassandra](#t-cassandra), [ScyllaDB](#t-scylla), [HBase](#t-hbase), [Bigtable](#t-bigtable)
- **Graph** — node/edge native traversal (property graph model).
  🛠 [Neo4j](#t-neo4j), [Amazon Neptune](#t-neptune), [ArangoDB](#t-arango), [TigerGraph](#t-tigergraph), [JanusGraph](#t-janusgraph), [Memgraph](#t-memgraph)
- **Knowledge Graph / RDF Triple Store** — semantic graphs based on RDF/OWL/SPARQL standards. Distinct from property graphs: schemas as ontologies, queries via SPARQL, designed for data integration and semantic interoperability. Used for FIBO-based financial ontologies, master/reference data, knowledge management.
  📜 [RDF / RDFS / OWL](#s-rdf), [SPARQL](#s-sparql), [SHACL](#s-shacl), [FIBO](#s-fibo)
  🛠 [Stardog](#t-stardog), [Ontotext GraphDB](#t-graphdb), [AllegroGraph](#t-allegrograph), [Apache Jena](#t-jena), [Blazegraph](#t-blazegraph), [Amazon Neptune](#t-neptune) (supports both), [Virtuoso](#t-virtuoso)
- **Time-Series** — timestamped metric/event storage.
  🛠 [InfluxDB](#t-influx), [TimescaleDB](#t-timescale), [Prometheus](#t-prometheus), [QuestDB](#t-questdb), [kdb+](#t-kdb)
- **Search** — inverted-index search engines.
  🛠 [Elasticsearch](#t-elastic), [OpenSearch](#t-opensearch), [Apache Solr](#t-solr), [Algolia](#t-algolia), [Typesense](#t-typesense), [Meilisearch](#t-meili)
- **Vector** — similarity search over embeddings.
  🛠 [Pinecone](#t-pinecone), [Weaviate](#t-weaviate), [Milvus](#t-milvus), [Qdrant](#t-qdrant), [Chroma](#t-chroma), [pgvector](#t-pgvector), [Vespa](#t-vespa)

> **Search/Vector convergence note.** Modern search engines (Elasticsearch, OpenSearch, Solr, Vespa) and several relational databases (Postgres via pgvector, ClickHouse, Redis) now offer native vector indexing alongside BM25/keyword search. **Hybrid search** (keyword + vector reranked) is increasingly the default for RAG. The architectural choice is no longer "vector DB vs. search engine" but "single hybrid engine vs. specialized vector + specialized search."
- **HTAP** — hybrid transactional/analytical.
  🛠 [TiDB](#t-tidb), [SingleStore](#t-singlestore), [CockroachDB](#t-cockroach)
- **Geospatial** — spatial indexes, geographic data types, GIS operations.
  🛠 [PostGIS](#t-postgis), [GeoParquet](#t-geoparquet), [Apache Sedona](#t-sedona), [H3](#t-h3) (Uber spatial index), [BigQuery GIS](#t-bigquery), [Snowflake Geospatial](#t-snowflake)

📚 [DDIA](#b-ddia) ch. 2–3

### 3.3 Infrastructure Storage

The base storage primitives data systems are built on.

- **Object Storage** — flat namespace, HTTP API, durable.
  🛠 [AWS S3](#t-s3), [GCS](#t-gcs), [Azure Blob](#t-azureblob), [MinIO](#t-minio), [Ceph](#t-ceph), [Wasabi](#t-wasabi), [Backblaze B2](#t-b2)
- **Block Storage** — raw block devices for VMs/databases.
  🛠 [AWS EBS](#t-ebs), [Azure Disks](#t-azuredisks), [GCP Persistent Disk](#t-gcppd)
- **File Storage** — POSIX-style network file systems.
  🛠 [AWS EFS](#t-efs), [Azure Files](#t-azurefiles), [NFS](#t-nfs), [GlusterFS](#t-gluster)
- **Caching** — hot-data acceleration.
  🛠 [Redis](#t-redis) / [Valkey](#t-valkey), [Memcached](#t-memcached), [ElastiCache](#t-elasticache), [Hazelcast](#t-hazelcast), [Apache Ignite](#t-ignite)

### 3.4 Formats

How bytes are encoded on disk and how tables are tracked.

- **File Formats** — encoding and compression of single files.
  🛠 [Parquet](#t-parquet), [ORC](#t-orc), [Avro](#t-avro), JSON, CSV, [Protobuf](#t-protobuf), [Apache Arrow](#t-arrow) (in-memory)
- **Table Formats** — ACID metadata layer over object stores.
  🛠 [Apache Iceberg](#t-iceberg), [Delta Lake](#t-delta), [Apache Hudi](#t-hudi), Hive ACID
- **Table Format Catalogs (REST/Federated)** — the catalog layer above table formats; tracks tables, namespaces, and snapshots, exposed via the Iceberg REST Catalog spec. The active battleground in lakehouse architecture: every major vendor is staking a position. Open standards here decouple table format from compute engine.
  📜 [Iceberg REST Catalog Spec](#s-iceberg-rest)
  🛠 [Apache Polaris](#t-polaris), [Unity Catalog](#t-unitycatalog) (now OSS), [Lakekeeper](#t-lakekeeper), [Gravitino](#t-gravitino), [Nessie](#t-nessie), [AWS Glue Data Catalog](#t-gluecatalog) (Iceberg REST endpoint)

📚 [Building the Data Lakehouse](#b-lakehouse)

---

## 4. Compute

Engines that actually execute work — batch, streaming, query, distributed.

📚 **Primary books:** [DDIA](#b-ddia) · [Streaming Systems](#b-streaming)

### 4.1 Batch Compute

Process bounded datasets at scale.

- **Distributed Engines** — Spark and friends.
  🛠 [Apache Spark](#t-spark), [Databricks](#t-databricks), [AWS EMR](#t-emr), [GCP Dataproc](#t-dataproc), [Azure HDInsight](#t-hdinsight), [Hadoop MapReduce](#t-hadoop) (legacy)
- **Serverless Compute** — pay-per-invocation runners suitable for batch glue.
  🛠 [AWS Lambda](#t-lambda), [GCP Cloud Functions](#t-gcpcf), [Azure Functions](#t-azfunc), [BigQuery](#t-bigquery)

### 4.2 Stream Processing Engines

Stateful computation over unbounded streams.

- **Stateful Streaming** — windowing, joins, exactly-once.
  🛠 [Apache Flink](#t-flink), [Kafka Streams](#t-kstreams), [Spark Structured Streaming](#t-spark), [ksqlDB](#t-ksqldb), [Apache Beam](#t-beam)
- **Cloud-Native Streaming** — managed equivalents.
  🛠 [AWS Kinesis Data Analytics](#t-kda), [GCP Dataflow](#t-dataflow), [Azure Stream Analytics](#t-asa), [Confluent Cloud](#t-confluent)

📚 [Streaming Systems](#b-streaming)

### 4.3 Query Engines

SQL execution over diverse storage.

- **MPP SQL Engines** — distributed federated SQL.
  🛠 [Trino](#t-trino), [Presto](#t-presto), [Apache Impala](#t-impala), [Apache Drill](#t-drill)
- **Cloud Query Services** — managed serverless SQL over object storage.
  🛠 [AWS Athena](#t-athena), [BigQuery](#t-bigquery), [Snowflake](#t-snowflake), [Redshift Spectrum](#t-redshift), [Azure Synapse Serverless](#t-synapse)
- **Embedded / Single-Node** — fast in-process or single-server engines.
  🛠 [DuckDB](#t-duckdb), [SQLite](#t-sqlite), [ClickHouse](#t-clickhouse), [Apache Pinot](#t-pinot), [StarRocks](#t-starrocks), [Apache Druid](#t-druid)
- **Real-Time / User-Facing Analytics** — sub-second query latency at high concurrency for embedded customer-facing dashboards and operational analytics. Architecturally distinct from traditional warehouses (smaller working sets, indexed for filtered scans, columnar with secondary indexes).
  🛠 [Apache Pinot](#t-pinot), [Apache Druid](#t-druid), [ClickHouse](#t-clickhouse), [StarRocks](#t-starrocks), [Tinybird](#t-tinybird), [Imply](#t-imply)
- **Streaming Databases** — databases that maintain incrementally-updated materialized views over streaming inputs, exposed via SQL/Postgres protocol. A hybrid of stream processing and analytical query — neither warehouse nor pure stream engine.
  🛠 [Materialize](#t-materialize), [RisingWave](#t-risingwave), [Proton (Timeplus)](#t-proton), [Tinybird](#t-tinybird)

### 4.4 Distributed Compute Frameworks

General-purpose frameworks for arbitrary distributed workloads.

- **General Purpose** — DAG schedulers and dataframe runtimes.
  🛠 [Apache Spark](#t-spark), [Ray](#t-ray), [Dask](#t-dask)
- **Specialized** — narrower scope or different model.
  🛠 [Apache Flink](#t-flink), [Modin](#t-modin)

---

## 5. Processing

Transforming and orchestrating data — ETL, ELT, modeling, wrangling, scheduling.

📚 **Primary books:** [Fundamentals of Data Engineering](#b-fode) · [Analytics Engineering with SQL and dbt](#b-aedbt) · [The Informed Company](#b-informed)

### 5.1 ETL

Transform-then-load — historical pattern, still common in regulated/legacy stacks.

- **Visual / GUI** — drag-and-drop pipeline builders.
  🛠 [Informatica PowerCenter](#t-informatica), [Talend](#t-talend), [Microsoft SSIS](#t-ssis), [IBM DataStage](#t-datastage), [Pentaho](#t-pentaho)
- **Code-First** — pipelines as code.
  🛠 custom Python/Spark, [Apache NiFi](#t-nifi)

### 5.2 ELT

Load-then-transform inside the warehouse — modern default.

- **In-Warehouse SQL** — transform with SQL on warehouse compute.
  🛠 [dbt Core](#t-dbt), [dbt Cloud](#t-dbtcloud), [Coalesce](#t-coalesce), [SQLMesh](#t-sqlmesh), [Dataform](#t-dataform)
- **ELT Orchestrated** — connectors plus warehouse SQL transformation.
  🛠 [Matillion](#t-matillion), [Fivetran](#t-fivetran) + [dbt](#t-dbt)

### 5.3 Data Transformation (modeling layer)

Producing modeled, tested, documented analytical tables.

- **SQL Transformation** — SQL-based model graphs.
  🛠 [dbt](#t-dbt), [SQLMesh](#t-sqlmesh), [Dataform](#t-dataform)
- **Code Transformation** — DataFrame APIs.
  🛠 [Spark / PySpark](#t-spark), [Pandas](#t-pandas), [Polars](#t-polars), [Ibis](#t-ibis) (portable across engines)
- **Alternative Query Languages** — SQL alternatives with stronger composability.
  🛠 [PRQL](#t-prql), [Malloy](#t-malloy)

📚 [Analytics Engineering with SQL and dbt](#b-aedbt) · [Kimball](#b-kimball)

### 5.4 Data Wrangling / Preparation

Interactive cleanup and reshaping prior to modeling.

- **Interactive Prep** — visual exploratory cleanup.
  🛠 [Trifacta/Alteryx](#t-alteryx), [AWS Glue DataBrew](#t-databrew), [Tableau Prep](#t-tableauprep)
- **Code-First Wrangling** — notebook-driven prep.
  🛠 [Pandas](#t-pandas), [Polars](#t-polars), [PySpark](#t-spark)

### 5.5 Reverse ETL

(Listed in [§2.7](#27-reverse-etl) — placement debated, conceptually a connector pattern.)

### 5.6 Orchestration

Scheduling and coordinating dependent pipelines.

- **Workflow Orchestrators** — DAG-based scheduling.
  🛠 [Apache Airflow](#t-airflow), [Dagster](#t-dagster), [Prefect](#t-prefect), [Mage](#t-mage), [Argo Workflows](#t-argo), [Luigi](#t-luigi) (legacy)
- **Cloud-Native** — provider-native orchestrators.
  🛠 [AWS Step Functions](#t-stepfunctions), [Azure Data Factory](#t-adf), [GCP Cloud Composer](#t-composer), [AWS MWAA](#t-mwaa)
- **Data-Aware** — asset/dataset-oriented (vs purely task-oriented).
  🛠 [Dagster](#t-dagster)
- **Durable Execution / Workflow-as-Code** — long-running stateful workflows expressed as regular code (Go/Java/Python/TS/.NET) with automatic retries, timeouts, versioning, and exactly-once semantics. Used for trade lifecycle, settlement, corporate actions, KYC, and saga patterns.
  🛠 [Temporal](#t-temporal), [Restate](#t-restate), [Cadence](#t-cadence), [AWS Step Functions](#t-stepfunctions), [Azure Durable Functions](#t-azdurable)
- **BPM / Process Orchestration** — model-driven business process orchestration based on BPMN 2.0 (and DMN for decision tables, CMMN for case management). Heavily used in financial services for trade lifecycle, settlement workflows, KYC/AML, onboarding, exception handling, and corporate actions. Decouples business logic from code.
  📜 [BPMN 2.0](#s-bpmn), [DMN](#s-dmn), [CMMN](#s-cmmn)
  🛠 [Camunda](#t-camunda), [Flowable](#t-flowable), [Activiti](#t-activiti), [jBPM](#t-jbpm), [Zeebe](#t-zeebe), [Netflix Conductor](#t-conductor)

---

## 6. AI/ML

The model lifecycle: features, training, serving, registry, monitoring, plus modern LLM/RAG infrastructure.

📚 **Primary books:** [Designing Machine Learning Systems](#b-dmls) · [Machine Learning Engineering](#b-mle) · [Building LLMs for Production](#b-bllm)

### 6.1 Feature Store

Centralized, versioned, online+offline feature serving.

- **Open-Source** — self-hostable feature stores.
  🛠 [Feast](#t-feast), [Hopsworks](#t-hopsworks), [Chronon](#t-chronon), [Featureform](#t-featureform)
- **Managed** — cloud-native feature stores.
  🛠 [Tecton](#t-tecton), [SageMaker Feature Store](#t-sagemaker), [Databricks Feature Store](#t-databricks), [Vertex AI Feature Store](#t-vertex)

📚 [Designing Machine Learning Systems](#b-dmls)

### 6.2 Model Training

Building models from data.

- **Frameworks** — core libraries for model authoring.
  🛠 [PyTorch](#t-pytorch), [TensorFlow](#t-tensorflow), [JAX](#t-jax), [scikit-learn](#t-sklearn), [XGBoost](#t-xgboost), [LightGBM](#t-lgbm)
- **Distributed Training** — multi-GPU/multi-node training.
  🛠 [Ray Train](#t-ray), [Horovod](#t-horovod), [DeepSpeed](#t-deepspeed), [PyTorch Lightning](#t-lightning)
- **Managed Training** — fully-hosted training services.
  🛠 [SageMaker Training](#t-sagemaker), [Vertex AI Training](#t-vertex), [Azure ML](#t-azureml), [Databricks ML](#t-databricks)

### 6.3 Model Serving / Inference

Exposing trained models for predictions.

- **Open-Source Servers** — self-hosted inference servers.
  🛠 [TorchServe](#t-torchserve), [TF Serving](#t-tfserving), [BentoML](#t-bento), [KServe](#t-kserve), [Triton Inference Server](#t-triton), [Ray Serve](#t-ray), [vLLM](#t-vllm)
- **Managed Endpoints** — pay-per-call hosted inference.
  🛠 [SageMaker Endpoints](#t-sagemaker), [Vertex AI Prediction](#t-vertex), [Azure ML Endpoints](#t-azureml), [Databricks Model Serving](#t-databricks), [Modal](#t-modal), [Replicate](#t-replicate)

### 6.4 MLOps / Model Registry

Versioning, deploying, monitoring models in production.

- **End-to-End Platforms** — open MLOps stacks.
  🛠 [MLflow](#t-mlflow), [Kubeflow](#t-kubeflow), [Metaflow](#t-metaflow), [ZenML](#t-zenml), [ClearML](#t-clearml)
- **Managed MLOps** — vendor-integrated lifecycle.
  🛠 [SageMaker](#t-sagemaker), [Vertex AI](#t-vertex), [Azure ML](#t-azureml), [Databricks MLflow](#t-databricks), [Weights & Biases](#t-wandb), [Neptune.ai](#t-neptune-ai), [Comet](#t-comet)

📚 [Machine Learning Engineering](#b-mle)

### 6.5 Vector Databases

(Listed in [§3.2](#32-operational-storage) — physically a storage class, conceptually AI/ML infrastructure.)

### 6.6 Embeddings & RAG Infrastructure

Retrieval-augmented generation stack.

- **Embedding Models** — text/image → vector encoders.
  🛠 [OpenAI Embeddings](#t-openai), [Cohere](#t-cohere), [sentence-transformers](#t-sbert), [Voyage AI](#t-voyage)
- **RAG Frameworks** — orchestrate retrieve-then-generate flows.
  🛠 [LangChain](#t-langchain), [LlamaIndex](#t-llamaindex), [Haystack](#t-haystack), [Semantic Kernel](#t-semantickernel)
- **RAG Platforms** — turnkey managed RAG.
  🛠 [Vertex AI Search](#t-vertex), [AWS Bedrock Knowledge Bases](#t-bedrock), [Azure AI Search](#t-azureaisearch)

📚 [Building LLMs for Production](#b-bllm)

### 6.7 Experiment Tracking

Recording runs, params, metrics, artifacts.

- **Open-Source** — self-hosted trackers.
  🛠 [MLflow](#t-mlflow), [DVC](#t-dvc), [Aim](#t-aim), [TensorBoard](#t-tensorboard)
- **Managed** — hosted trackers with collaboration.
  🛠 [Weights & Biases](#t-wandb), [Neptune.ai](#t-neptune-ai), [Comet](#t-comet), [ClearML](#t-clearml)

### 6.8 LLMOps

Operating LLM-based applications specifically.

- **Prompt Management & Tracing** — capture, version, evaluate prompts.
  🛠 [LangSmith](#t-langsmith), [PromptLayer](#t-promptlayer), [Helicone](#t-helicone), [Langfuse](#t-langfuse)
- **LLM Evaluation** — measure quality, hallucination, retrieval relevance.
  🛠 [Ragas](#t-ragas), [DeepEval](#t-deepeval), [TruLens](#t-trulens), [Arize Phoenix](#t-phoenix)

---

## 7. Semantic

The layer that turns physical tables into business meaning.

📚 **Primary books:** [Kimball](#b-kimball) · [DAMA-DMBOK](#b-dama)

### 7.1 Semantic Layer / Headless BI

Centralized definitions of dimensions, measures, joins — consumed by any tool.

- **Open-Source** — embeddable semantic engines.
  🛠 [Cube](#t-cube), [MetricFlow](#t-metricflow) (dbt), [Malloy](#t-malloy)
- **Embedded in Platforms** — semantic layer inside a BI/warehouse platform.
  🛠 [LookML (Looker)](#t-looker), [AtScale](#t-atscale), [Kyligence](#t-kyligence), [Power BI Semantic Model](#t-powerbi)

### 7.2 Metrics Layer

Centralized metric definitions consumed by BI/apps/notebooks.

- **Standalone Metrics Layer**
  🛠 [dbt Semantic Layer](#t-dbtcloud), [Cube](#t-cube)

### 7.3 Business Glossary

Human-readable definitions of business terms, owners, lineage to physical assets.

- **Standalone** — dedicated glossary tools.
  🛠 [Collibra](#t-collibra), [Atlan](#t-atlan), [data.world](#t-dataworld)
- **Embedded in Catalogs** — glossary as catalog feature.
  🛠 [Alation](#t-alation), [Informatica EDC](#t-informaticaedc), [Microsoft Purview](#t-purview)

📚 [DAMA-DMBOK](#b-dama)

---

## 8. Architecture

Designing the platform itself — reference architectures, modeling, schema design, DDD.

📚 **Primary books:** [Kimball](#b-kimball) · [Data Vault 2.0](#b-vault) · [Building Evolutionary Architectures](#b-evolutionary) · [Data Management at Scale](#b-dms)

### 8.1 Reference Architecture

Pre-baked blueprints to start from.

- **Cloud Provider Reference** — vendor canonical patterns.
  🛠 [AWS Well-Architected](#t-awswar), [Azure CAF](#t-azurecaf), [GCP Cloud Adoption Framework](#t-gcpcaf)
- **Vendor Reference** — platform-specific blueprints.
  🛠 [Databricks Lakehouse](#t-databricks), [Snowflake Data Cloud](#t-snowflake)
- **Industry Reference** — vendor-neutral frameworks.
  🛠 [TOGAF](#t-togaf), [DAMA-DMBOK](#t-dama)

### 8.2 Data Modeling

Structured representation of data at three abstraction levels.

📐 **Concepts:** [Normalization (1NF–6NF)](#c-normalization), [Denormalization](#c-denormalization), [Slowly Changing Dimensions (SCD Type 1/2/3/6)](#c-scd), [Surrogate vs Natural Keys](#c-keys), [Star vs Snowflake schema](#c-star-snowflake)
📜 **Notations:** [ERD](#s-erd), [IDEF1X](#s-idef1x), [UML class diagrams](#s-uml), [Crow's Foot](#s-crowsfoot)

- **Conceptual Modeling** — entities and relationships at business level.
  🛠 [ERwin](#t-erwin), [ER/Studio](#t-erstudio), [Lucidchart](#t-lucid), [draw.io](#t-drawio)
- **Logical Modeling** — attributes, keys, normalization, vendor-agnostic.
  🛠 [ERwin](#t-erwin), [SqlDBM](#t-sqldbm), [Hackolade](#t-hackolade)
- **Physical Modeling** — DDL specific to a target engine.
  🛠 [DataGrip](#t-datagrip), [DBeaver](#t-dbeaver), [Hackolade](#t-hackolade)
- **Dimensional Modeling** — Kimball star/snowflake schemas.
  📚 [Kimball](#b-kimball) · [Agile Data Warehouse Design](#b-corr)
- **Data Vault Modeling** — Hubs, Links, Satellites for auditability.
  🛠 [Vaultspeed](#t-vaultspeed), [WhereScape](#t-wherescape), [Datavault Builder](#t-dvbuilder)
  📚 [Data Vault 2.0](#b-vault)
- **Anchor Modeling / 6NF** — fully temporal models for historized data.

### 8.3 Schema Design

Designing and governing message/event/table schemas over time.

📐 **Concepts:** [Schema Evolution / Compatibility (forward, backward, full, none)](#c-schema-compat), [Schema-on-Read vs Schema-on-Write](#c-schema-on-read)

- **Schema Registries** — central schema versioning.
  🛠 [Confluent Schema Registry](#t-csr), [AWS Glue Schema Registry](#t-glueregistry), [Apicurio](#t-apicurio)
- **Schema Languages** — [Avro](#s-avro-format), [Protobuf](#s-protobuf), [JSON Schema](#s-json-schema), [GraphQL SDL](#s-graphql), [OpenAPI](#s-openapi), [AsyncAPI](#s-asyncapi)

### 8.4 Domain-Driven Design

Aligning data boundaries with business domains; foundation for Data Mesh.

- Methodology, low tooling — workshops (EventStorming), notation (Context Mapper).
  🛠 [Context Mapper](#t-contextmapper)

📚 [Data Mesh](#b-mesh) · [Data Management at Scale](#b-dms)

### 8.5 Process & Architecture Modeling Notations

Standard notations for modeling processes, decisions, and enterprise architecture. Required reading for anyone working with BPM engines or formal architecture frameworks.

📜 **Notations:** [BPMN 2.0](#s-bpmn) (process models), [DMN](#s-dmn) (decision tables/logic), [CMMN](#s-cmmn) (case management for unstructured work), [UML](#s-uml) (system structure/behavior), [ArchiMate](#s-archimate) (enterprise architecture), [C4 Model](#s-c4) (software architecture)

- **Modeling Tools** — visual editors for BPMN/DMN/UML/ArchiMate.
  🛠 [Camunda Modeler](#t-camunda), [bpmn.io](#t-bpmnio), [Sparx Enterprise Architect](#t-sparx), [Archi (ArchiMate)](#t-archi), [Visual Paradigm](#t-vp), [Structurizr (C4)](#t-structurizr)

---

## 9. Engineering Practice

How data teams actually ship — IDEs, version control, CI/CD, testing, docs.

📚 **Primary books:** [Accelerate](#b-accelerate) · [The DevOps Handbook](#b-devops)

### 9.1 Development Environments

- **IDEs** — code editors and notebook hosts.
  🛠 [VS Code](#t-vscode), [JetBrains](#t-jetbrains), [Cursor](#t-cursor), [Jupyter](#t-jupyter)
- **Notebooks** — interactive analysis environments.
  🛠 [Jupyter](#t-jupyter), [JupyterHub](#t-jupyter), [Databricks Notebooks](#t-databricks), [Hex](#t-hex), [Deepnote](#t-deepnote), [Google Colab](#t-colab), [Zeppelin](#t-zeppelin)
- **Local Data Sandboxes** — reproducible local stacks.
  🛠 Docker Compose, [LocalStack](#t-localstack), [DuckDB](#t-duckdb), [Testcontainers](#t-testcontainers)

### 9.2 Version Control

- **Git Hosting** — code repositories.
  🛠 [GitHub](#t-github), [GitLab](#t-gitlab), [Bitbucket](#t-bitbucket), [Gitea](#t-gitea)
- **Data Versioning** — versioning datasets and lake state.
  🛠 [DVC](#t-dvc), [lakeFS](#t-lakefs), [Pachyderm](#t-pachyderm), [Nessie](#t-nessie), [Git LFS](#t-gitlfs), [Iceberg branching](#t-iceberg) (native), [Delta UniForm](#t-delta) (Iceberg/Delta interop)

### 9.3 CI/CD

- **Pipeline Tools** — generic CI runners.
  🛠 [GitHub Actions](#t-ghactions), [GitLab CI](#t-gitlab), [Jenkins](#t-jenkins), [CircleCI](#t-circleci), [Azure DevOps](#t-azdevops), [Argo CD](#t-argocd)
- **Data-Specific CI** — pipelines aware of data semantics/diff.
  🛠 [dbt Cloud CI](#t-dbtcloud), [Datafold](#t-datafold), [SQLMesh](#t-sqlmesh)

📚 [Accelerate](#b-accelerate) · [DevOps Handbook](#b-devops)

### 9.4 Testing

- **Unit Testing** — code-level tests.
  🛠 [pytest](#t-pytest), [JUnit](#t-junit), [dbt tests](#t-dbt)
- **Data Quality Testing** — assertions on data shape and content.
  🛠 [Great Expectations](#t-ge), [Soda Core](#t-sodacore), [dbt-expectations](#t-dbt), [Deequ](#t-deequ), [Datafold](#t-datafold)
- **Integration Testing** — black-box pipeline validation.
  🛠 [Testcontainers](#t-testcontainers), [Pact](#t-pact)
- **Load / Performance** — throughput / latency testing.
  🛠 [JMeter](#t-jmeter), [Locust](#t-locust), [k6](#t-k6), [Gatling](#t-gatling)

### 9.5 Code Review / Peer Review

- **Platform Features** — PR/MR review.
  🛠 [GitHub PRs](#t-github), [GitLab MRs](#t-gitlab), [Gerrit](#t-gerrit), [Reviewable](#t-reviewable)
- **Data Diff Tools** — show row/column-level diffs across model changes.
  🛠 [Datafold](#t-datafold), [data-diff](#t-datadiff)

### 9.6 Documentation

- **Code Docs** — generated documentation.
  🛠 [Sphinx](#t-sphinx), [MkDocs](#t-mkdocs), [Docusaurus](#t-docusaurus)
- **Data Docs** — generated catalog/lineage documentation.
  🛠 [dbt docs](#t-dbt), [DataHub](#t-datahub), [Backstage](#t-backstage)

### 9.7 Schema Migrations

Tracking versioned DDL changes.

- **Database Migrations** — forward/backward migration tools.
  🛠 [Liquibase](#t-liquibase), [Flyway](#t-flyway), [Alembic](#t-alembic), [Atlas](#t-atlas), [golang-migrate](#t-gomigrate)

### 9.8 Test Data & Synthetic Data

Generating safe, representative test data — increasingly critical for compliance (privacy-preserving development) and ML training-data scarcity.

📐 **Concepts:** [Synthetic Data](#c-synthetic-data), [Data Subsetting](#c-subsetting), [Data Masking vs Synthesis](#c-mask-vs-synth)

- **Synthetic Data Generators** — generate realistic statistically-similar fake data.
  🛠 [Mostly AI](#t-mostlyai), [Gretel.ai](#t-gretel), [Tonic.ai](#t-tonic), [Synthesized](#t-synthesized), [MDClone](#t-mdclone), [Faker](#t-faker) (OS library), [SDV (Synthetic Data Vault)](#t-sdv)
- **Test Data Management** — subset, mask, refresh test data from production.
  🛠 [Delphix](#t-delphix), [Tonic.ai](#t-tonic), [DataMasker](#t-datamasker)

### 9.9 Notebooks in Production

Notebooks promoted from exploration to scheduled production artifacts. Contested practice but real.

- **Parameterized Notebook Execution** — promote notebooks to pipelines.
  🛠 [Papermill](#t-papermill), [Ploomber](#t-ploomber), [Databricks Workflows](#t-databricks), [Jupyter Enterprise Gateway](#t-jeg)

### 9.10 Infrastructure as Code

Provisioning data infrastructure declaratively — cuts across all domains.

📐 **Concepts:** [Idempotency](#c-idempotency), [Drift Detection](#c-drift)

- **Cloud-Agnostic IaC** — multi-cloud declarative provisioning.
  🛠 [OpenTofu](#t-opentofu) (OS), [Terraform](#t-terraform) (SA), [Pulumi](#t-pulumi), [Crossplane](#t-crossplane)
- **Cloud-Native IaC** — provider-native declarative templates.
  🛠 [AWS CloudFormation](#t-cloudformation), [AWS CDK](#t-awscdk), [Azure Bicep / ARM](#t-bicep), [GCP Deployment Manager](#t-gcpdm)
- **Configuration Management** — instance-level config.
  🛠 [Ansible](#t-ansible), [Chef](#t-chef), [Puppet](#t-puppet), [SaltStack](#t-salt)

---

## 10. Governance

Meaning, trust, lineage, quality, ownership — the layer above raw plumbing.

📚 **Primary books:** [DAMA-DMBOK](#b-dama) · [Data Governance: The Definitive Guide](#b-dggtg) · [Data Quality Fundamentals](#b-dqf) · [Non-Invasive Data Governance](#b-niv)

### 10.1 Metadata Management

Active and passive metadata — the connective tissue of governance.

📐 **Concepts:** [Active vs Passive Metadata](#c-active-metadata), [Technical vs Business Metadata](#c-tech-biz-metadata)
📜 **Standards:** [OpenLineage spec](#s-openlineage), [OpenMetadata spec](#s-openmetadata-spec)

- **Active Metadata Platforms** — open standards, programmatic.
  🛠 [DataHub](#t-datahub) / [Acryl Data](#t-acryl), [Atlan](#t-atlan), [OpenMetadata](#t-openmetadata), [Amundsen](#t-amundsen), [Marquez](#t-marquez), [Secoda](#t-secoda)
- **Enterprise Catalogs** — heavy enterprise governance suites.
  🛠 [Collibra](#t-collibra), [Alation](#t-alation), [Informatica EDC](#t-informaticaedc), [Microsoft Purview](#t-purview), [AWS Glue Data Catalog](#t-gluecatalog)

### 10.2 Data Discovery

The user-facing search/browse experience over catalog metadata. Increasingly distinct from cataloging itself: discovery tools optimize for search relevance, embeddings-based semantic search, recommendations, and AI-driven Q&A over assets.

- **AI-Native Discovery** — embeddings/LLM-driven search and chat.
  🛠 [Atlan AI](#t-atlan), [DataHub Smart Search](#t-datahub), [Select Star](#t-selectstar), [Workstream](#t-workstream)
- **Catalog-Embedded Discovery** — discovery as a feature of the catalog (see §10.1).

### 10.3 Data Lineage

Tracking data movement and transformation.

- **Standalone / Standards** — lineage as first-class concern.
  🛠 [OpenLineage](#t-openlineage), [Marquez](#t-marquez), [Manta](#t-manta), [Spline](#t-spline)
- **Embedded in Catalogs** — lineage feature inside catalog tools.
  🛠 [DataHub](#t-datahub), [Atlan](#t-atlan), [Collibra](#t-collibra), [Alation](#t-alation)

### 10.4 Data Quality

Programmatic validation of data shape, freshness, distribution.

📐 **Concepts:** [Data Quality Dimensions (Accuracy, Completeness, Consistency, Timeliness, Uniqueness, Validity)](#c-dq-dimensions), [DQ Rules](#c-dq-rules), [Data Profiling](#c-data-profiling)
📜 **Standards/Frameworks:** [DAMA-DMBOK](#b-dama), [DCAM](#s-dcam) (financial services)

- **Open-Source DQ** — code-first quality frameworks.
  🛠 [Great Expectations](#t-ge), [Soda Core](#t-sodacore), [Deequ](#t-deequ), [dbt tests](#t-dbt), [Elementary](#t-elementary)
- **Managed / Enterprise DQ** — platforms with anomaly detection.
  🛠 [Monte Carlo](#t-montecarlo), [Soda Cloud](#t-soda), [Bigeye](#t-bigeye), [Anomalo](#t-anomalo), [Lightup](#t-lightup), [Informatica DQ](#t-informaticadq), [Talend DQ](#t-talend)
- **Data Profiling** — distinct discipline: discover statistical properties, distributions, cardinality, patterns, outliers (often as a *prerequisite* to writing DQ rules).
  🛠 [ydata-profiling](#t-ydata) (formerly pandas-profiling), [Apache Griffin](#t-griffin), [Whylogs](#t-whylogs), [DataPrep](#t-dataprep), [Sweetviz](#t-sweetviz)

📚 [Data Quality Fundamentals](#b-dqf)

### 10.5 Master Data Management

Single source of truth for core entities (customer, security, fund, instrument).

- **Enterprise MDM** — heavyweight MDM suites.
  🛠 [Informatica MDM](#t-informaticamdm), [IBM InfoSphere MDM](#t-ibmmdm), [SAP MDG](#t-sapmdg), [Reltio](#t-reltio), [Stibo Systems](#t-stibo), [Profisee](#t-profisee)
- **Modern / Cloud MDM** — newer or ML-based MDM.
  🛠 [Tamr](#t-tamr), [Semarchy](#t-semarchy)

📚 [DAMA-DMBOK](#b-dama)

### 10.6 Reference Data Management

Managing slowly-changing code lists (currencies, countries, ISIN, LEI).

- **Standalone** — dedicated RDM tools.
  🛠 [Collibra RDM](#t-collibra), [CluedIn](#t-cluedin)
- **Often inside MDM** — bundled into MDM products.

### 10.7 Data Retention / Lifecycle

Automated tiering, archival, deletion.

- **Cloud-Native Lifecycle** — bucket-level lifecycle policies.
  🛠 [S3 Lifecycle](#t-s3), [Azure Blob Lifecycle](#t-azureblob), [GCS Object Lifecycle](#t-gcs)
- **Enterprise** — heavyweight ILM tools.
  🛠 [Veritas](#t-veritas), [Commvault](#t-commvault), [IBM ILM](#t-ibmilm)

### 10.8 Audit & Compliance

Evidence trails for regulatory review.

- See [§11](#11-security--compliance) — Security & Compliance domain.

### 10.9 Data Observability

Pipeline-level health monitoring.

- **Pipeline Observability** — freshness, volume, schema drift, lineage incidents.
  🛠 [Monte Carlo](#t-montecarlo), [Bigeye](#t-bigeye), [Acceldata](#t-acceldata), [Datadog](#t-datadog), [Databand (IBM)](#t-databand)
- **Open-Source** — DIY observability stacks.
  🛠 [Elementary](#t-elementary), [OpenLineage](#t-openlineage), [Great Expectations](#t-ge)

📚 [Data Quality Fundamentals](#b-dqf)

---

## 11. Security & Compliance

Protecting data and proving compliance — separated from Governance because tooling and concerns are distinct.

📚 **Primary books:** [Data Privacy](#b-privacy) · [Practical Cloud Security](#b-pcs)

### 11.1 Authentication / Authorization

📐 **Concepts:** [RBAC](#c-rbac), [ABAC](#c-abac), [ReBAC](#c-rebac), [Zero Trust](#c-zero-trust), [Least Privilege](#c-least-priv), [Row-Level Security](#c-rls), [Column-Level Security](#c-cls)
📜 **Standards:** [OAuth 2.0](#s-oauth), [OIDC](#s-oidc), [SAML 2.0](#s-saml), [SCIM](#s-scim)

- **Identity Providers** — SSO/IdP.
  🛠 [Okta](#t-okta), [Auth0](#t-auth0), [Azure AD / Entra ID](#t-entra), [AWS IAM](#t-awsiam), [Keycloak](#t-keycloak), [Ping Identity](#t-ping)
- **Access Control** — fine-grained data access policies.
  🛠 [AWS Lake Formation](#t-lakeformation), [Apache Ranger](#t-ranger), [Privacera](#t-privacera), [Immuta](#t-immuta), [Satori](#t-satori)
- **Policy-as-Code** — externalized authorization expressed as policy code, decoupled from application code.
  🛠 [Open Policy Agent (OPA)](#t-opa), [Cedar](#t-cedar) (AWS), [Permit.io](#t-permit), [OSO](#t-oso), [Topaz](#t-topaz), [SpiceDB](#t-spicedb)

### 11.2 Encryption

- **Key Management** — KMS / HSM-backed key hierarchies.
  🛠 [AWS KMS](#t-kms), [Azure Key Vault](#t-keyvault), [GCP KMS](#t-gcpkms), [HashiCorp Vault](#t-vault)
- **Database Encryption** — TDE (Transparent Data Encryption) features in Oracle, SQL Server, Postgres, etc.

### 11.3 Data Masking / Tokenization

- **Standalone** — masking as a service.
  🛠 [Immuta](#t-immuta), [Privacera](#t-privacera), [Protegrity](#t-protegrity), [Delphix](#t-delphix), [Skyflow](#t-skyflow)
- **Built-in DB Features** — dynamic masking inside warehouses.
  🛠 [Snowflake Dynamic Masking](#t-snowflake), [BigQuery Column-Level Security](#t-bigquery)

### 11.4 PII Detection & Redaction

- **Tools** — automated discovery + classification of personal data.
  🛠 [AWS Macie](#t-macie), [GCP DLP](#t-gcpdlp), [Azure Purview Data Map](#t-purview), [BigID](#t-bigid), [OneTrust DataDiscovery](#t-onetrust), [Microsoft Presidio](#t-presidio)

📚 [Data Privacy](#b-privacy)

### 11.5 Privacy / Consent Management

- **Platforms** — consent capture, DSAR, retention enforcement.
  🛠 [OneTrust](#t-onetrust), [TrustArc](#t-trustarc), [Securiti.ai](#t-securiti), [Transcend](#t-transcend), [DataGrail](#t-datagrail)

📚 [Data Privacy](#b-privacy)

### 11.6 Audit Logging

- **SIEM** — centralized security event collection.
  🛠 [Splunk](#t-splunk), [Datadog](#t-datadog), [Elastic SIEM](#t-elastic), [Sumo Logic](#t-sumo), [AWS CloudTrail](#t-cloudtrail), [Azure Monitor](#t-azmonitor)

### 11.7 Regulatory Compliance Frameworks

Methodologies, not tools: GDPR, HIPAA, SOX, PCI-DSS, CCPA, SOC 2. Often supported by **continuous compliance** platforms.

🛠 [OneTrust](#t-onetrust), [Vanta](#t-vanta), [Drata](#t-drata)

### 11.8 Secrets Management

- **Tools** — application-level secret storage.
  🛠 [HashiCorp Vault](#t-vault), [AWS Secrets Manager](#t-secretsmgr), [Azure Key Vault](#t-keyvault), [GCP Secret Manager](#t-gcpsecrets), [Doppler](#t-doppler), [1Password Secrets](#t-1pass)

---

## 12. Operations

Keeping the platform alive — backup, DR, FinOps, on-call, SLOs.

📚 **Primary books:** [Accelerate](#b-accelerate) · [The DevOps Handbook](#b-devops)

### 12.1 Backup & Recovery

- **Cloud-Native** — provider-native snapshots and time-travel.
  🛠 [AWS Backup](#t-awsbackup), [Azure Backup](#t-azbackup), [GCP Backup](#t-gcpbackup), [Snowflake Time Travel](#t-snowflake), [BigQuery snapshots](#t-bigquery)
- **Enterprise Backup** — multi-platform backup suites.
  🛠 [Veeam](#t-veeam), [Commvault](#t-commvault), [Veritas NetBackup](#t-veritas), [Rubrik](#t-rubrik), [Cohesity](#t-cohesity)

### 12.2 Disaster Recovery

- **DR Tooling** — orchestrated failover.
  🛠 [AWS Elastic DR](#t-edr), [Azure Site Recovery](#t-asr), [Zerto](#t-zerto), [Druva](#t-druva)
- **Patterns** — multi-region replication, active-active, pilot-light, warm standby.

### 12.3 FinOps / Cost Management

- **Cloud Cost Tools** — provider and third-party cost analytics.
  🛠 [AWS Cost Explorer](#t-costexplorer), [Azure Cost Management](#t-azcost), [GCP Billing](#t-gcpbilling), [CloudHealth](#t-cloudhealth), [Cloudability](#t-cloudability), [Vantage](#t-vantage), [Apptio](#t-apptio)
- **Data-Specific FinOps** — warehouse-credit and query-cost tooling.
  🛠 [SELECT](#t-select), [Bluesky](#t-bluesky), [Capital One Slingshot](#t-slingshot), [Snowflake Resource Monitors](#t-snowflake)

### 12.4 SLA / SLO Management

- **SLO Tools** — error-budget and reliability tracking.
  🛠 [Nobl9](#t-nobl9), [Datadog SLOs](#t-datadog), [Grafana SLO](#t-grafana)

### 12.5 Incident Management

- **On-Call / Paging** — alert routing.
  🛠 [PagerDuty](#t-pagerduty), [Opsgenie](#t-opsgenie), [Splunk On-Call](#t-splunkoc), [Grafana OnCall](#t-grafana)
- **Postmortem Tools** — incident review and learning.
  🛠 [FireHydrant](#t-firehydrant), [incident.io](#t-incidentio)

### 12.6 Capacity Planning

- **Monitoring + Forecasting** — APM + capacity dashboards.
  🛠 [Datadog](#t-datadog), [Grafana](#t-grafana), [Prometheus](#t-prometheus), [New Relic](#t-newrelic), [Dynatrace](#t-dynatrace)

### 12.7 Infrastructure Monitoring & Observability

📐 **Concepts:** [Three Pillars (Logs/Metrics/Traces)](#c-three-pillars), [SLI/SLO/SLA](#c-sli-slo-sla), [Error Budget](#c-error-budget), [Distributed Tracing](#c-tracing)
📜 **Standards:** [OpenTelemetry](#s-otel) (the de-facto standard for telemetry collection — instruments libraries, exposes metrics/logs/traces; vendor-neutral), [Prometheus exposition format / OpenMetrics](#s-openmetrics)

- **Commercial APM** — full-stack observability platforms.
  🛠 [Datadog](#t-datadog), [New Relic](#t-newrelic), [Splunk](#t-splunk), [Dynatrace](#t-dynatrace)
- **Open-Source Observability Stack** — DIY observability built from CNCF-graduated components.
  🛠 [OpenTelemetry](#t-otel), [Prometheus](#t-prometheus) (metrics), [Grafana](#t-grafana) (dashboards), [Loki](#t-loki) (logs), [Tempo](#t-tempo) (traces), [Mimir](#t-mimir) (metrics at scale), [Jaeger](#t-jaeger) (tracing), [VictoriaMetrics](#t-victoriametrics) (Prometheus alternative), [Thanos](#t-thanos) (Prometheus long-term storage)

---

## 13. Data Products

Treating datasets as productized, contracted, owned units.

📚 **Primary books:** [Data Mesh](#b-mesh) · [Data Management at Scale](#b-dms) · [Driving Data Quality with Data Contracts](#b-contracts)

### 13.1 Data Contracts

Producer-consumer agreements on schema, semantics, SLAs.

📐 **Concepts:** [Data Contract](#c-data-contract), [Data Product](#c-data-product), [SLA/SLO/SLI for data](#c-data-sla), [Backward/Forward Compatibility](#c-schema-compat)
📜 **Standards:** [Open Data Contract Standard (Bitol)](#t-odcs), [Data Contract Specification](#t-dcs), [AsyncAPI](#s-asyncapi)

- **Tools** — implementation/enforcement of contracts.
  🛠 [Confluent Schema Registry](#t-csr), [DataHub Contracts](#t-datahub), [Gable](#t-gable), [PayPal data-contract-cli](#t-pdcc), [dbt model contracts](#t-dbt)
- **Standards (tools)** — open specifications.
  🛠 [Open Data Contract Standard](#t-odcs), [Data Contract Specification](#t-dcs)

📚 [Driving Data Quality with Data Contracts](#b-contracts)

### 13.2 Data Mesh / Domain Ownership

Decentralized, domain-owned, productized data with federated governance.

- **Enabling Platforms** — federation/virtualization layers.
  🛠 [Starburst](#t-starburst), [Dremio](#t-dremio), [Nextdata OS](#t-nextdata), [Databricks Unity Catalog](#t-databricks)

📚 [Data Mesh](#b-mesh)

### 13.3 Data Marketplace / Sharing

Internal and external dataset distribution.

- **Internal Marketplaces** — discoverability + access workflow.
  🛠 [Atlan](#t-atlan), [DataHub](#t-datahub), [Collibra Marketplace](#t-collibra)
- **Cross-Org Sharing** — secure cross-tenant data exchange.
  🛠 [Snowflake Data Sharing](#t-snowflake), [Databricks Delta Sharing](#t-deltasharing), [BigQuery Analytics Hub](#t-bigquery), [AWS Data Exchange](#t-awsdataexchange)
- **Commercial Data Marketplaces** — third-party data subscription/discovery (relevant for buying market data feeds).
  🛠 [Snowflake Marketplace](#t-snowflake), [Databricks Marketplace](#t-databricks), [Datarade](#t-datarade), [Demyst](#t-demyst), [AWS Data Exchange](#t-awsdataexchange)

### 13.4 Data APIs (Data-as-a-Service)

Productized API access to data.

- **GraphQL** — schema-driven dynamic queries.
  🛠 [Hasura](#t-hasura), [PostGraphile](#t-postgraphile), [StepZen](#t-stepzen)
- **REST** — resource-oriented data services.
  🛠 [Cube REST API](#t-cube), [DreamFactory](#t-dreamfactory), [PostgREST](#t-postgrest)

### 13.5 Customer Data Platforms (CDP)

A distinct category between connectors and reverse ETL: identity resolution, customer-360 modeling, audience building, then activation to ad/marketing/CRM tools. Relevant where data products are customer-centric.

- **Standalone CDPs** — full-stack identity + activation.
  🛠 [Segment (Twilio)](#t-segment), [RudderStack](#t-rudderstack), [mParticle](#t-mparticle), [Tealium](#t-tealium), [Bloomreach](#t-bloomreach)
- **Composable CDPs** — warehouse-native (built on Snowflake/BigQuery/Databricks).
  🛠 [Hightouch](#t-hightouch), [Census](#t-census), [GrowthLoop](#t-growthloop)

---

## 14. Consumption

Where humans and applications actually use the data — BI, viz, embedded analytics, reporting, notebooks, data apps, activation.

📚 **Primary books:** [Storytelling with Data](#b-storytelling) · [The Big Book of Dashboards](#b-bbod)

### 14.1 Business Intelligence

Dashboard, report, ad-hoc analysis platforms.

- **Modern Cloud BI** — SaaS-first BI tools.
  🛠 [Looker](#t-looker), [Power BI](#t-powerbi), [Tableau Cloud](#t-tableau), [Mode](#t-mode), [Sigma](#t-sigma), [ThoughtSpot](#t-thoughtspot), [Lightdash](#t-lightdash), [Omni](#t-omni)
- **On-Prem / Legacy BI** — enterprise installable BI.
  🛠 [Tableau Server](#t-tableau), [MicroStrategy](#t-microstrategy), [SAP BusinessObjects](#t-bo), [IBM Cognos](#t-cognos), [Qlik Sense](#t-qlik), [Pentaho](#t-pentaho), [SAS](#t-sas)
- **Open-Source BI** — self-hosted BI.
  🛠 [Apache Superset](#t-superset), [Metabase](#t-metabase), [Redash](#t-redash), [Lightdash](#t-lightdash), [Evidence](#t-evidence)

📚 [The Big Book of Dashboards](#b-bbod)

### 14.2 Data Visualization

Programmatic charting libraries.

- **Programmatic Libraries** — for building custom visuals.
  🛠 [D3.js](#t-d3), [Plotly](#t-plotly), [ECharts](#t-echarts), [Vega/Vega-Lite](#t-vega), [Observable](#t-observable), [matplotlib](#t-matplotlib), [Seaborn](#t-seaborn)

📚 [Storytelling with Data](#b-storytelling)

### 14.3 Embedded Analytics

BI as a feature of another product.

- **Tools** — embeddable BI engines and components.
  🛠 [Sigma Embed](#t-sigma), [Looker Embed](#t-looker), [Cube](#t-cube), [Explo](#t-explo), [Luzmo](#t-luzmo), [Embeddable](#t-embeddable)

### 14.4 Reporting

- **Operational Reporting** — paginated, fixed-format reports.
  🛠 [Power BI paginated](#t-powerbi), [SAP Crystal Reports](#t-crystal), [JasperReports](#t-jasper), [BIRT](#t-birt)
- **Regulatory Reporting** — submission-grade reporting (highly relevant in fund/securities).
  🛠 [Workiva](#t-workiva), [AxiomSL](#t-axiom), [Vermeg](#t-vermeg), [Wolters Kluwer](#t-wk)

### 14.5 Self-Service Analytics / Notebooks

- **Cloud Notebooks** — collaborative hosted notebooks.
  🛠 [Hex](#t-hex), [Deepnote](#t-deepnote), [Mode](#t-mode), [Databricks](#t-databricks), [Google Colab](#t-colab), [Observable](#t-observable)
- **Self-Hosted** — on-prem notebook servers.
  🛠 [JupyterHub](#t-jupyter), [Zeppelin](#t-zeppelin)

### 14.6 Data Apps

Interactive data-driven applications.

- **Frameworks** — code-first data app frameworks.
  🛠 [Streamlit](#t-streamlit), [Gradio](#t-gradio), [Plotly Dash](#t-plotly), [Shiny](#t-shiny), [Panel](#t-panel), [Solara](#t-solara)
- **Internal Tools** — low-code tool builders.
  🛠 [Retool](#t-retool), [Appsmith](#t-appsmith), [ToolJet](#t-tooljet), [Budibase](#t-budibase)

### 14.7 Alerting & Data Activation

Triggering actions and people from data signals.

- **Anomaly Alerting** — quality/observability triggers.
  🛠 [Monte Carlo](#t-montecarlo), [Bigeye](#t-bigeye), [Anomalo](#t-anomalo)
- **Reverse-ETL Activation** — push data to operational systems (also §2.7).
  🛠 [Hightouch](#t-hightouch), [Census](#t-census)
- **Notification Tools** — paging and chat.
  🛠 [PagerDuty](#t-pagerduty), [Opsgenie](#t-opsgenie)

---

# Concepts, Patterns & Standards — Reference List

Concepts, patterns, and standards referenced throughout the taxonomy. Linked from inline 📐 (concepts/patterns) and 📜 (standards/protocols) annotations.

## Concepts & Patterns

<a id="c-idempotency"></a>
### Idempotency
The property that repeating an operation yields the same result as performing it once. Critical for retry safety in distributed systems and pipelines.

<a id="c-delivery-semantics"></a>
### Delivery Semantics: At-Most-Once / At-Least-Once / Exactly-Once
Three guarantees a messaging system can offer. At-most-once may lose messages; at-least-once may duplicate; exactly-once requires deduplication or idempotency at the consumer. "Exactly-once processing" (Kafka/Flink) is achieved via transactions over offsets and side-effects, not magic.

<a id="c-outbox"></a>
### Outbox Pattern
Producer writes the business event to an *outbox* table in the same DB transaction as the business state change, then a separate process publishes events from the outbox. Ensures atomicity between state and events without distributed transactions.

<a id="c-saga"></a>
### Saga Pattern
A long-running business transaction broken into local transactions, each with a compensating action for rollback. Two flavors: choreography (events) and orchestration (a coordinator like Temporal or Camunda). The bedrock of multi-service trade lifecycles.

<a id="c-event-sourcing"></a>
### Event Sourcing
Persist state as an append-only log of events; current state is a fold over the log. Enables full audit, time travel, replay. Heavy in financial/regulated systems.

<a id="c-cqrs"></a>
### CQRS (Command-Query Responsibility Segregation)
Separate write model (commands) from read model (queries) — often paired with event sourcing. Enables different optimization for writes vs. reads.

<a id="c-dlq"></a>
### Dead-Letter Queue (DLQ)
A side-channel queue for messages that cannot be processed after retries. Lets the main flow proceed while preserving failed messages for inspection.

<a id="c-backpressure"></a>
### Backpressure
A producer is slowed down when a consumer can't keep up — implemented via buffer limits, blocking writes, dropped messages, or reactive streams.

<a id="c-2pc"></a>
### Two-Phase Commit (2PC)
Classical distributed transaction protocol with prepare and commit phases. Brittle under failures; modern systems prefer sagas, outbox, or event sourcing.

<a id="c-cdc-pattern"></a>
### Change Data Capture (CDC)
Pattern of capturing row-level changes from a source database via the transaction log (preferred), triggers, or polling — and propagating them as a stream.

<a id="c-strangler"></a>
### Strangler Fig Pattern
Incremental replacement of a legacy system: route a slice of traffic to the new system, grow the slice over time, retire legacy at the end. Crucial for replacing core banking/post-trade systems.

<a id="c-bulkhead"></a>
### Bulkhead Pattern
Isolate resources (thread pools, connection pools) by client/use-case so that one failing consumer can't exhaust resources for others.

<a id="c-circuit-breaker"></a>
### Circuit Breaker
Wrap a remote call so that repeated failures *open* the circuit (fail fast) and only periodically test the dependency. Prevents cascading failures.

<a id="c-watermarks"></a>
### Watermarks
A heuristic for "we have seen all events with timestamp ≤ T" in a stream. Enables event-time windowing without waiting forever for late data.

<a id="c-windowing"></a>
### Windowing (Tumbling / Sliding / Session / Global)
Strategies for partitioning an unbounded stream into bounded chunks for aggregation. Tumbling = fixed non-overlapping; sliding = overlapping; session = activity-based; global = single window.

<a id="c-late-data"></a>
### Late Data Handling
Strategies for events arriving after their event-time window has closed: drop, side-output, allowed lateness, restate.

<a id="c-event-time"></a>
### Event Time vs Processing Time
Event time = when the event happened in the real world. Processing time = when the system processes it. They differ; reasoning in event time gives correct, deterministic results.

<a id="c-triggers"></a>
### Triggers
When to emit a result for a window: at watermark, periodically, on count, on completion. Decoupled from windowing strategy in the Beam model.

<a id="c-stateful"></a>
### Stateful vs Stateless Processing
Stateless: each event handled independently. Stateful: the operator maintains state (counts, joins, aggregations) — requires state backends, checkpointing, recovery.

<a id="c-schema-compat"></a>
### Schema Evolution Compatibility (Forward / Backward / Full / None)
**Backward**: new schema can read old data. **Forward**: old schema can read new data. **Full**: both. **None**: anything goes (avoid). Enforcement happens in schema registries.

<a id="c-normalization"></a>
### Normalization (1NF–6NF) and Denormalization
Normal forms reduce redundancy and update anomalies (3NF/BCNF for OLTP). Denormalization reintroduces redundancy for read performance (star schemas, wide tables for OLAP).

<a id="c-denormalization"></a>
### Denormalization
Pre-joining/flattening tables for read performance, accepting redundancy. Standard practice in OLAP and analytical models.

<a id="c-scd"></a>
### Slowly Changing Dimensions (SCD)
Strategies for tracking dimension history. Type 1 = overwrite. Type 2 = new row with effective dates (most common). Type 3 = limited history columns. Type 6 = hybrid (1+2+3). Critical for fund/security reference data history.

<a id="c-keys"></a>
### Surrogate vs Natural Keys
Natural keys carry business meaning (ISIN, account number); surrogate keys are arbitrary numeric IDs. Surrogate keys are dimensional-modeling standard for join performance and SCD.

<a id="c-star-snowflake"></a>
### Star vs Snowflake Schema
Star: central fact table joined to denormalized dimensions. Snowflake: dimensions further normalized into sub-dimensions. Star is the default; snowflake when dimension hierarchies are deep and reused.

<a id="c-schema-on-read"></a>
### Schema-on-Read vs Schema-on-Write
Schema-on-write: enforce schema at ingestion (warehouse). Schema-on-read: store as-is, parse at query (lake). Lakehouses blur the line via table formats.

<a id="c-active-metadata"></a>
### Active vs Passive Metadata
Passive: stored, browsed. Active: programmatically pushed back into tools (e.g., to alert on quality, to drive access policy, to surface in BI).

<a id="c-tech-biz-metadata"></a>
### Technical vs Business Metadata
Technical: schemas, types, lineage, freshness. Business: definitions, owners, SLAs, glossary terms. Both belong in the catalog.

<a id="c-dq-dimensions"></a>
### Data Quality Dimensions
Standard set: **Accuracy** (matches reality), **Completeness** (no missing values), **Consistency** (no contradictions across stores), **Timeliness** (fresh enough), **Uniqueness** (no unintended duplicates), **Validity** (conforms to schema/rules).

<a id="c-dq-rules"></a>
### Data Quality Rules
Programmatic assertions encoding the dimensions above — null checks, regex validations, range checks, referential integrity, custom SQL.

<a id="c-data-profiling"></a>
### Data Profiling
The discipline of *discovering* statistical properties of a dataset (distributions, cardinalities, patterns) — usually a *prerequisite* to writing DQ rules. Distinct from quality testing.

<a id="c-synthetic-data"></a>
### Synthetic Data
Statistically representative fake data — generated by GANs, copulas, or rules — used for development, testing, sharing, and ML training without privacy risk.

<a id="c-subsetting"></a>
### Data Subsetting
Extracting a referentially-consistent slice of production data for non-prod environments. Distinct from masking — subsets shrink, masking transforms.

<a id="c-mask-vs-synth"></a>
### Data Masking vs Synthesis
Masking deterministically transforms PII (tokenize, redact, hash). Synthesis generates new data that statistically resembles real data without preserving record-level mapping. Masking preserves relationships; synthesis breaks them by design.

<a id="c-rbac"></a>
### RBAC (Role-Based Access Control)
Permissions assigned to roles, users assigned to roles. Coarse but simple.

<a id="c-abac"></a>
### ABAC (Attribute-Based Access Control)
Decisions based on attributes of subject, resource, action, environment. Far more expressive than RBAC; basis of OPA, Cedar.

<a id="c-rebac"></a>
### ReBAC (Relationship-Based Access Control)
Permissions derived from graph relationships ("user is editor of this document because they're a member of this team"). Google Zanzibar model; SpiceDB and OpenFGA implement it.

<a id="c-zero-trust"></a>
### Zero Trust
"Never trust, always verify" — no implicit trust based on network location. Every request is authenticated and authorized.

<a id="c-least-priv"></a>
### Least Privilege
Each principal has only the minimum access needed. Foundational security principle.

<a id="c-rls"></a>
### Row-Level Security (RLS)
Filter rows visible to a query based on the current user's identity/attributes. Native in Snowflake, BigQuery, Postgres.

<a id="c-cls"></a>
### Column-Level Security (CLS)
Mask or block specific columns based on identity. Often combined with dynamic data masking.

<a id="c-three-pillars"></a>
### Three Pillars of Observability (Logs, Metrics, Traces)
Logs: text events. Metrics: time-series numbers. Traces: causal request paths across services. Modern stacks add Profiles. OpenTelemetry standardizes all of them.

<a id="c-sli-slo-sla"></a>
### SLI / SLO / SLA
**SLI** (Indicator): a measurement (e.g., 99.5% of pipeline runs complete < 10min). **SLO** (Objective): the internal target. **SLA** (Agreement): the contractual external promise, usually with penalties.

<a id="c-error-budget"></a>
### Error Budget
1 − SLO. The amount of allowed unreliability in a period. When the budget is consumed, freeze risky changes.

<a id="c-tracing"></a>
### Distributed Tracing
A trace ID propagates through service calls so the full path of a request is reconstructable. OpenTelemetry, Jaeger, Tempo, Datadog APM.

<a id="c-pubsub"></a>
### Pub/Sub
Publishers don't know subscribers. Decouples producers from consumers via a broker.

<a id="c-data-contract"></a>
### Data Contract
An explicit, versioned, enforceable agreement between data producer and consumer covering schema, semantics, SLAs, ownership, quality. Distinct from API contracts in scope and enforcement.

<a id="c-data-product"></a>
### Data Product
A dataset (or set of datasets) treated as a product: discoverable, addressable, trustworthy, self-describing, secure, interoperable. Dehghani's data mesh definition.

<a id="c-data-sla"></a>
### Data SLAs / SLOs / SLIs
Same construct as service SLAs but for data: freshness, completeness, schema stability, accuracy. Encoded in data contracts.

<a id="c-drift"></a>
### Drift Detection
Detection of unintended divergence between desired and actual state — schema drift, infrastructure drift, model drift. Triggers reconciliation or alerts.

## Standards & Protocols

<a id="s-uml"></a>
### UML (Unified Modeling Language)
ISO/IEC 19501. Visual modeling language with structural diagrams (class, component, deployment) and behavioral diagrams (sequence, state machine, activity, use case). Maintained by OMG.
🔗 https://www.omg.org/spec/UML/

<a id="s-bpmn"></a>
### BPMN 2.0 (Business Process Model and Notation)
ISO/IEC 19510. Standard for executable business process diagrams. Widely supported by Camunda, Flowable, jBPM. Used for trade lifecycle, settlement, KYC processes.
🔗 https://www.omg.org/spec/BPMN/2.0/

<a id="s-dmn"></a>
### DMN (Decision Model and Notation)
OMG standard for modeling decision logic separate from process flow — decision tables, decision requirements diagrams, FEEL expression language. Often paired with BPMN.
🔗 https://www.omg.org/spec/DMN/

<a id="s-cmmn"></a>
### CMMN (Case Management Model and Notation)
OMG standard for modeling unstructured, knowledge-worker-driven cases (vs. predefined BPMN flows). Less widely adopted than BPMN; suited to exception handling and ad-hoc workflows.
🔗 https://www.omg.org/spec/CMMN/

<a id="s-archimate"></a>
### ArchiMate
The Open Group standard for enterprise architecture modeling — distinct from UML/BPMN: spans business, application, technology, motivation, strategy layers. Often used with TOGAF.
🔗 https://www.opengroup.org/archimate-forum/

<a id="s-c4"></a>
### C4 Model
Lightweight architecture-as-code modeling: Context → Containers → Components → Code, four levels of zoom. Authored by Simon Brown.
🔗 https://c4model.com/

<a id="s-erd"></a>
### ERD (Entity-Relationship Diagram)
Foundational data-modeling notation by Peter Chen (1976). Multiple notations: Chen, IE/Crow's Foot, Bachman.

<a id="s-idef1x"></a>
### IDEF1X
US Federal Information Processing Standard 184. Rigorous data-modeling notation, more formal than Crow's Foot. Used in defense, government, regulated industries.
🔗 https://www.idef.com/idefx-data-modeling-method/

<a id="s-crowsfoot"></a>
### Crow's Foot Notation
The most common ERD notation in commercial tools — cardinality shown by "crow's feet" symbols at relationship endpoints.

<a id="s-http"></a>
### HTTP / HTTPS
The web's request/response protocol. RFC 9110+. Foundation of REST APIs.
🔗 https://www.rfc-editor.org/rfc/rfc9110.html

<a id="s-grpc"></a>
### gRPC
Google's HTTP/2-based RPC framework using Protobuf. High-performance binary protocol; widely used inside microservice meshes.
🔗 https://grpc.io/docs/

<a id="s-graphql"></a>
### GraphQL
Query language and server runtime for APIs — clients specify exactly what they want. Spec maintained by GraphQL Foundation.
🔗 https://graphql.org/learn/

<a id="s-websocket"></a>
### WebSocket
RFC 6455. Bi-directional persistent TCP-over-HTTP connection for low-latency real-time apps.
🔗 https://www.rfc-editor.org/rfc/rfc6455.html

<a id="s-mqtt"></a>
### MQTT
Lightweight pub/sub protocol designed for IoT/constrained devices. ISO/IEC 20922.
🔗 https://mqtt.org/

<a id="s-amqp"></a>
### AMQP (Advanced Message Queuing Protocol)
ISO/IEC 19464. Open queueing protocol — RabbitMQ's native protocol, also supported by ActiveMQ.
🔗 https://www.amqp.org/

<a id="s-stomp"></a>
### STOMP
Simple Text-Oriented Messaging Protocol — text-based broker protocol, easy to implement clients in any language.
🔗 https://stomp.github.io/

<a id="s-jdbc"></a>
### JDBC
Java Database Connectivity — Oracle/Java standard for SQL database connections.
🔗 https://docs.oracle.com/javase/tutorial/jdbc/

<a id="s-odbc"></a>
### ODBC
Open Database Connectivity — Microsoft-led, language-agnostic SQL connection API.
🔗 https://learn.microsoft.com/sql/odbc/

<a id="s-arrow-flight"></a>
### Apache Arrow Flight / Flight SQL
High-performance gRPC-based protocol for transferring Arrow data — orders of magnitude faster than JDBC/ODBC for analytical workloads.
🔗 https://arrow.apache.org/docs/format/Flight.html

<a id="s-adbc"></a>
### ADBC (Arrow Database Connectivity)
Successor to JDBC/ODBC for columnar data — native Arrow throughout, no row-by-row marshaling.
🔗 https://arrow.apache.org/adbc/

<a id="s-kafka-wire"></a>
### Kafka Wire Protocol
The TCP binary protocol Kafka clients speak to brokers. Supported by Redpanda, WarpStream, AutoMQ to enable Kafka-API compatibility without Kafka itself.
🔗 https://kafka.apache.org/protocol

<a id="s-pg-wire"></a>
### PostgreSQL Wire Protocol
The TCP protocol Postgres clients speak — increasingly adopted as a *de facto* standard (Materialize, RisingWave, CockroachDB, YugabyteDB all speak it).
🔗 https://www.postgresql.org/docs/current/protocol.html

<a id="s-sparql-protocol"></a>
### SPARQL Protocol
W3C standard HTTP protocol for querying RDF data via SPARQL.
🔗 https://www.w3.org/TR/sparql11-protocol/

<a id="s-odata"></a>
### OData
OASIS standard REST-like protocol for querying and updating data — widely used by Microsoft (Power BI, Dynamics 365, SAP).
🔗 https://www.odata.org/

<a id="s-soap"></a>
### SOAP
Legacy XML-based RPC protocol; still ubiquitous in financial services and SWIFT.
🔗 https://www.w3.org/TR/soap/

<a id="s-rest"></a>
### REST / HATEOAS
Architectural style (Fielding 2000), not a strict spec — resources, representations, stateless calls, hypermedia controls.

<a id="s-jsonapi"></a>
### JSON:API
A specification for building REST APIs in JSON with consistent conventions for relationships, includes, sparse fieldsets, pagination.
🔗 https://jsonapi.org/

<a id="s-json"></a>
### JSON
RFC 8259 / ECMA-404. Ubiquitous text-based data interchange format.
🔗 https://www.json.org/

<a id="s-xml"></a>
### XML
W3C extensible markup language. Still dominant in financial services (ISO 20022, FpML, FIX/FIXML, SWIFT MX).
🔗 https://www.w3.org/XML/

<a id="s-yaml"></a>
### YAML
Human-friendly data serialization standard; ubiquitous for configuration. v1.2 superset of JSON.
🔗 https://yaml.org/

<a id="s-protobuf"></a>
### Protocol Buffers (Protobuf)
Google's compact binary serialization format with code generation. The wire format underneath gRPC.
🔗 https://protobuf.dev/

<a id="s-avro-format"></a>
### Apache Avro
Binary serialization with strong schema evolution support. Dominant on Kafka.
🔗 https://avro.apache.org/docs/

<a id="s-msgpack"></a>
### MessagePack
"Like JSON, but fast and small" — binary, schema-less. Common in Redis, ZeroMQ.
🔗 https://msgpack.org/

<a id="s-thrift"></a>
### Apache Thrift
Cross-language RPC + serialization stack from Facebook. Older alternative to gRPC.
🔗 https://thrift.apache.org/

<a id="s-flatbuffers"></a>
### FlatBuffers
Google zero-copy serialization library; faster reads than Protobuf, no parse step.
🔗 https://flatbuffers.dev/

<a id="s-capnp"></a>
### Cap'n Proto
Sandstorm's zero-copy serialization with built-in RPC. Author overlaps with Protobuf.
🔗 https://capnproto.org/

<a id="s-cbor"></a>
### CBOR (Concise Binary Object Representation)
RFC 8949 — binary equivalent of JSON, used by IoT, COSE, WebAuthn.
🔗 https://cbor.io/

<a id="s-asyncapi"></a>
### AsyncAPI
The OpenAPI counterpart for event-driven APIs — describes channels, messages, bindings (Kafka/AMQP/MQTT/etc).
🔗 https://www.asyncapi.com/

<a id="s-cloudevents"></a>
### CloudEvents
CNCF specification for a common event envelope: id, source, type, subject, data, datacontenttype. Letting brokers, FaaS, and event mesh share a vocabulary.
🔗 https://cloudevents.io/

<a id="s-openapi"></a>
### OpenAPI
The dominant REST API description language (formerly Swagger). Used to generate clients, servers, docs, mocks.
🔗 https://www.openapis.org/

<a id="s-json-schema"></a>
### JSON Schema
Validation/annotation vocabulary for JSON documents.
🔗 https://json-schema.org/

<a id="s-rdf"></a>
### RDF / RDFS / OWL
W3C semantic web stack: RDF (subject-predicate-object triples), RDFS (lightweight vocabulary), OWL (description-logic ontologies). FIBO is OWL.
🔗 https://www.w3.org/RDF/ · https://www.w3.org/OWL/

<a id="s-sparql"></a>
### SPARQL
W3C query language for RDF graphs.
🔗 https://www.w3.org/TR/sparql11-query/

<a id="s-shacl"></a>
### SHACL (Shapes Constraint Language)
W3C standard for validating RDF graphs against constraints — analogous to JSON Schema/XSD for triples.
🔗 https://www.w3.org/TR/shacl/

<a id="s-oauth"></a>
### OAuth 2.0
RFC 6749. Authorization framework — third-party apps get scoped access without seeing user credentials.
🔗 https://oauth.net/2/

<a id="s-oidc"></a>
### OpenID Connect (OIDC)
Identity layer on top of OAuth 2.0 — the modern SSO standard.
🔗 https://openid.net/connect/

<a id="s-saml"></a>
### SAML 2.0
OASIS XML-based SSO/identity federation standard. Predecessor of OIDC; still ubiquitous in enterprise.
🔗 https://www.oasis-open.org/standard/saml/

<a id="s-scim"></a>
### SCIM (System for Cross-domain Identity Management)
Standard REST API for user/group provisioning across IdPs and apps. RFC 7643/7644.
🔗 https://scim.cloud/

<a id="s-otel"></a>
### OpenTelemetry (OTel)
CNCF standard for instrumenting applications to emit traces, metrics, and logs. Vendor-neutral; supported by Datadog, New Relic, Splunk, Grafana, AWS, Azure, GCP. Default observability standard going forward.
🔗 https://opentelemetry.io/docs/

<a id="s-openmetrics"></a>
### OpenMetrics / Prometheus Exposition Format
The text-based exposition format for /metrics endpoints, originating in Prometheus, now an IETF effort.
🔗 https://openmetrics.io/

<a id="s-openlineage"></a>
### OpenLineage Spec
LF AI & Data open standard for metadata + lineage events emitted from data tools.
🔗 https://openlineage.io/docs/

<a id="s-openmetadata-spec"></a>
### OpenMetadata Spec
Open standard for metadata schemas and APIs across catalogs.
🔗 https://docs.open-metadata.org/

<a id="s-iceberg-rest"></a>
### Iceberg REST Catalog Specification
Open spec defining the HTTP API for an Iceberg catalog — decouples table format from compute engine. Implemented by Apache Polaris, Lakekeeper, Unity Catalog (REST mode), Snowflake, AWS Glue.
🔗 https://iceberg.apache.org/spec/

## Financial Services Standards & Protocols

<a id="s-iso20022"></a>
### ISO 20022
The global standard for financial messaging — XML schemas covering payments, securities, FX, trade services, cards. Adopted by SWIFT (MX), SEPA, target2, CBPR+. Replacing legacy MT messages by November 2025.
🔗 https://www.iso20022.org/

<a id="s-lei"></a>
### ISO 17442 (LEI — Legal Entity Identifier)
Global 20-character identifier for legal entities involved in financial transactions. Maintained by GLEIF. Mandatory under MiFID II, EMIR, Dodd-Frank.
🔗 https://www.gleif.org/

<a id="s-isin"></a>
### ISIN (International Securities Identification Number)
ISO 6166 — 12-character globally unique security identifier. Allocated by national NNAs; coordinated by ANNA.
🔗 https://www.isin.org/

<a id="s-cfi"></a>
### CFI (Classification of Financial Instruments)
ISO 10962 — 6-character code classifying instruments by category, group, and attributes (equity, debt, derivative, etc.).
🔗 https://www.iso.org/standard/81179.html

<a id="s-figi"></a>
### FIGI (Financial Instrument Global Identifier)
Open Symbology identifier from Bloomberg, now an OMG standard (ISO 16550 candidate). Free alternative to ISIN at the venue level.
🔗 https://www.openfigi.com/

<a id="s-fibo"></a>
### FIBO (Financial Industry Business Ontology)
Open OWL ontology of financial industry concepts — securities, contracts, agents, processes — by EDM Council. Used for semantic master/reference data.
🔗 https://spec.edmcouncil.org/fibo/

<a id="s-emt-ept"></a>
### EMT / EPT (FinDatEx Templates)
**European MiFID Template** (target market & cost data) and **European PRIIPs Template** (KID data) — XML/CSV templates for fund-data dissemination across European distributors. Core to Kneip's product domain.
🔗 https://findatex.eu/

<a id="s-swift"></a>
### SWIFT MT / MX
SWIFT MT (legacy text messages — MT103 payments, MT540 settlements, etc.) and MX (XML, ISO 20022 over SWIFT) for inter-bank financial messaging.
🔗 https://www.swift.com/standards

<a id="s-fpml"></a>
### FpML (Financial Products Markup Language)
ISDA-led XML standard for OTC derivatives — trades, valuations, lifecycle events.
🔗 https://www.fpml.org/

<a id="s-fix"></a>
### FIX Protocol
Financial Information eXchange — the dominant trading messaging protocol. Versions 4.2/4.4/5.0; FIXML for XML-based variants.
🔗 https://www.fixtrading.org/

<a id="s-iban"></a>
### IBAN (ISO 13616) / SEPA
International Bank Account Number standard underpinning SEPA payments in Europe.
🔗 https://www.iso.org/standard/81090.html

<a id="s-dcam"></a>
### DCAM (Data Capability Assessment Model)
EDM Council's data management framework — financial-services-focused, parallel to and often used alongside DAMA-DMBOK. Defines capabilities across data strategy, governance, architecture, quality, control, analytics.
🔗 https://edmcouncil.org/frameworks/dcam/

---



<a id="b-fode"></a>
### Fundamentals of Data Engineering

Joe Reis & Matt Housley (O'Reilly, 2022). The closest book to a "textbook" for the modern data lifecycle, covering generation, storage, ingestion, transformation, and serving. Strongly aligned with this taxonomy.
🔗 https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/

<a id="b-ddia"></a>
### Designing Data-Intensive Applications

Martin Kleppmann (O'Reilly, 2017; v2 in progress). The canonical deep-dive into the principles behind storage engines, distributed systems, replication, partitioning, transactions, and stream/batch processing. Heavy on "why," light on tools — exactly the foundation Fundamentals lacks.
🔗 https://dataintensive.net/

<a id="b-kimball"></a>
### The Data Warehouse Toolkit (3rd ed.)

Ralph Kimball & Margy Ross (Wiley, 2013). The reference for dimensional modeling — star schemas, slowly changing dimensions, conformed dimensions. Still the dominant analytical modeling approach, especially in regulated/financial reporting marts.
🔗 https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/

<a id="b-dms"></a>
### Data Management at Scale (2nd ed.)

Piethein Strengholt (O'Reilly, 2023). Practical large-organization patterns: domain-oriented architecture, data mesh, data fabric, federated governance. Particularly applicable to large regulated organizations (e.g., Clearstream-scale).
🔗 https://www.oreilly.com/library/view/data-management-at/9781098138851/

<a id="b-mesh"></a>
### Data Mesh

Zhamak Dehghani (O'Reilly, 2022). The original full-length treatment of data mesh: domain ownership, data-as-a-product, self-serve platform, federated computational governance.
🔗 https://www.oreilly.com/library/view/data-mesh/9781492092384/

<a id="b-lakehouse"></a>
### Building the Data Lakehouse

Bill Inmon, Ranjeet Srivastava, Mary Levins (Technics, 2021). Inmon's perspective on the lakehouse architecture and how it relates to traditional warehousing. Pair with Kimball for both modeling traditions.
🔗 https://www.amazon.com/Building-Data-Lakehouse-Bill-Inmon/dp/1634629663

<a id="b-evolutionary"></a>
### Building Evolutionary Architectures (2nd ed.)

Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage (O'Reilly, 2023). Architecture as a living, testable thing — fitness functions, deployment pipelines, evolutionary change. Applies directly to data architecture decisions.
🔗 https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/

<a id="b-vault"></a>
### Building a Scalable Data Warehouse with Data Vault 2.0

Daniel Linstedt & Michael Olschimke (Morgan Kaufmann, 2015). The reference for Data Vault modeling — Hubs, Links, Satellites — heavily used in financial services for auditability and full source-of-truth tracking.
🔗 https://www.elsevier.com/books/building-a-scalable-data-warehouse-with-data-vault-2-0/linstedt/978-0-12-802510-9

<a id="b-corr"></a>
### Agile Data Warehouse Design

Lawrence Corr & Jim Stagnitto (DecisionOne, 2011). Workshop-driven dimensional design with the BEAM (Business Event Analysis & Modeling) approach. Practical complement to Kimball.
🔗 https://www.amazon.com/Agile-Data-Warehouse-Design-Collaborative/dp/0956817203

<a id="b-streaming"></a>
### Streaming Systems

Tyler Akidau, Slava Chernyak, Reuven Lax (O'Reilly, 2018). The canonical text on stream processing — windowing, watermarks, triggers, exactly-once. Authored by the team behind Google Dataflow / Apache Beam.
🔗 https://www.oreilly.com/library/view/streaming-systems/9781491983867/

<a id="b-eds"></a>
### Designing Event-Driven Systems

Ben Stopford (O'Reilly, 2018; free PDF from Confluent). Patterns for building event-driven architectures on Kafka — event sourcing, CQRS, stateful streaming.
🔗 https://www.confluent.io/designing-event-driven-systems/

<a id="b-kafka"></a>
### Kafka: The Definitive Guide (2nd ed.)

Gwen Shapira, Todd Palino, Rajini Sivaram, Krit Petty (O'Reilly, 2021). End-to-end Kafka — design, operations, security, stream processing, deployment patterns.
🔗 https://www.oreilly.com/library/view/kafka-the-definitive/9781492043072/

<a id="b-aedbt"></a>
### Analytics Engineering with SQL and dbt

Cameron Cyr & Dustin Dorsey (O'Reilly, 2024). Practical guide to dbt-style analytics engineering: model layering, testing, documentation, deployment.
🔗 https://www.oreilly.com/library/view/analytics-engineering-with/9781098142377/

<a id="b-informed"></a>
### The Informed Company

Dave Fowler & Matthew C. David (Wiley, 2021). Modern data stack adoption journey — stages of maturity, organizational patterns, tooling choices.
🔗 https://www.wiley.com/en-us/The+Informed+Company%3A+How+to+Build+Modern+Agile+Data+Stacks+that+Drive+Winning+Insights-p-9781119748021

<a id="b-dggtg"></a>
### Data Governance: The Definitive Guide

Evren Eryurek, Uri Gilad, Valliappa Lakshmanan, Anita Kibunguchy-Grant, Jessi Ashdown (O'Reilly, 2021). Cloud-era data governance, written by Google Cloud practitioners.
🔗 https://www.oreilly.com/library/view/data-governance-the/9781492063483/

<a id="b-dqf"></a>
### Data Quality Fundamentals

Barr Moses, Lior Gavish, Molly Vorwerck (O'Reilly, 2022). Concepts and practices for modern data quality and observability. Vendor bias toward Monte Carlo (the authors' company), but solid concepts.
🔗 https://www.oreilly.com/library/view/data-quality-fundamentals/9781098112035/

<a id="b-niv"></a>
### Non-Invasive Data Governance

Robert S. Seiner (Technics, 2014). Pragmatic, low-friction governance program design — particularly applicable in regulated environments where heavy governance gets resisted.
🔗 https://technicspub.com/non-invasive-data-governance/

<a id="b-dama"></a>
### DAMA-DMBOK (2nd ed.)

DAMA International (Technics, 2017). The encyclopedic reference for data management — every governance discipline mapped, defined, and related. Used as the basis for the CDMP certification; widely referenced in financial services.
🔗 https://technicspub.com/dmbok/

<a id="b-privacy"></a>
### Data Privacy: A runbook for engineers

Nishant Bhajaria (Manning, 2022). Implementation-level privacy engineering — PII handling, consent, GDPR/CCPA, privacy-by-design.
🔗 https://www.manning.com/books/data-privacy

<a id="b-pcs"></a>
### Practical Cloud Security (2nd ed.)

Chris Dotson (O'Reilly, 2023). Hands-on cloud security across AWS/Azure/GCP — IAM, network security, encryption, incident response.
🔗 https://www.oreilly.com/library/view/practical-cloud-security/9781098148171/

<a id="b-dmls"></a>
### Designing Machine Learning Systems

Chip Huyen (O'Reilly, 2022). End-to-end ML system design — data pipelines, feature stores, training, deployment, monitoring. Aligned with the AI/ML domain in this taxonomy.
🔗 https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/

<a id="b-mle"></a>
### Machine Learning Engineering

Andriy Burkov (True Positive, 2020). Concise, practical ML engineering practices — data prep, training, evaluation, deployment, monitoring.
🔗 http://www.mlebook.com/

<a id="b-bllm"></a>
### Building LLMs for Production

Louis-François Bouchard & Louie Peters (Towards AI, 2024). Production-grade LLM application design — RAG, fine-tuning, evaluation, deployment.
🔗 https://www.amazon.com/Building-LLMs-Production-Reliability-Fine-Tuning/dp/B0D4FFPFW8

<a id="b-storytelling"></a>
### Storytelling with Data

Cole Nussbaumer Knaflic (Wiley, 2015). Visualization fundamentals — pre-attentive attributes, decluttering, narrative structure, audience design.
🔗 https://www.storytellingwithdata.com/books

<a id="b-bbod"></a>
### The Big Book of Dashboards

Steve Wexler, Jeffrey Shaffer, Andy Cotgreave (Wiley, 2017). Dashboard pattern catalog with annotated real-world examples across industries.
🔗 https://www.bigbookofdashboards.com/

<a id="b-accelerate"></a>
### Accelerate

Nicole Forsgren, Jez Humble, Gene Kim (IT Revolution, 2018). The research basis for the DORA metrics; how delivery practices correlate with organizational performance.
🔗 https://itrevolution.com/product/accelerate/

<a id="b-devops"></a>
### The DevOps Handbook (2nd ed.)

Gene Kim, Jez Humble, Patrick Debois, John Willis (IT Revolution, 2021). Practical DevOps practices — flow, feedback, continual learning. Direct applicability to DataOps.
🔗 https://itrevolution.com/product/the-devops-handbook-second-edition/

<a id="b-contracts"></a>
### Driving Data Quality with Data Contracts

Andrew Jones (Packt, 2023). The first dedicated book on data contracts — schema, semantics, SLAs, enforcement, organizational adoption.
🔗 https://www.packtpub.com/product/driving-data-quality-with-data-contracts/9781837635009

---

## Domain-Specific Books (Financial Services / Fund Data)

Particularly relevant for Clearstream / Kneip context — fund data dissemination, post-trade settlement, regulatory reporting.

### After the Trade Is Made (3rd ed.)

David M. Weiss (Portfolio, 2006). Foundational text on post-trade securities lifecycle — clearance, settlement, custody, asset servicing. Direct relevance to a CSD/post-trade environment.
🔗 https://www.amazon.com/After-Trade-Made-Processing-Securities/dp/1591841275

### Securities Operations: A Guide to Trade and Position Management

Michael Simmons (Wiley, 2002). Trade lifecycle, reconciliation, corporate actions — the operational mechanics of securities processing.
🔗 https://www.wiley.com/en-us/Securities+Operations%3A+A+Guide+to+Trade+and+Position+Management-p-9780471497585

### The Fund Industry: How Your Money is Managed (2nd ed.)

Robert Pozen & Theresa Hamacher (Wiley, 2015). How investment funds work — structure, operations, distribution, regulation. Directly relevant to fund-data businesses.
🔗 https://www.wiley.com/en-us/The+Fund+Industry%3A+How+Your+Money+is+Managed%2C+2nd+Edition-p-9781118929940

### Fund Custody and Administration

David Loader (Academic Press, 2016). NAV calculation, fund administration, transfer agency operations.
🔗 https://www.elsevier.com/books/fund-custody-and-administration/loader/978-0-12-804252-6

### Standards and Specifications (no books — read the specs)

Essential standards for the fund/securities domain — read the specifications directly:

- **ISO 20022** — financial messaging standard. 🔗 https://www.iso20022.org/
- **ISO 17442 (LEI)** — Legal Entity Identifier. 🔗 https://www.gleif.org/
- **ISIN / CFI** — instrument identifiers. 🔗 https://www.anna-dsb.com/ · https://www.iso.org/standard/44799.html
- **FIBO** — Financial Industry Business Ontology. 🔗 https://spec.edmcouncil.org/fibo/
- **EMT / EPT (FinDatEx)** — European MiFID/PRIIPs Templates (Kneip core). 🔗 https://findatex.eu/
- **SWIFT MT/MX** — financial messaging (post-trade legacy). 🔗 https://www.swift.com/standards
- **FpML** — derivatives markup. 🔗 https://www.fpml.org/
- **FIX Protocol** — trading messaging. 🔗 https://www.fixtrading.org/

---

# Tools & Vendors — Reference List

Format: **Name** — *(license/deployment tags)* — short description — link.

Tags: `OS` open-source · `C` cloud-managed (SaaS / fully-managed) · `E` enterprise/proprietary on-prem.

## A

<a id="t-acceldata"></a>
**Acceldata** — *(C)* — multidimensional data observability platform. 🔗 https://www.acceldata.io/

<a id="t-activemq"></a>
**ActiveMQ** — *(OS)* — Apache message broker (JMS). 🔗 https://activemq.apache.org/

<a id="t-activiti"></a>
**Activiti** — *(OS)* — Java BPMN 2.0 process engine; predecessor of Flowable. 🔗 https://www.activiti.org/

<a id="t-acryl"></a>
**Acryl Data** — *(C)* — managed cloud platform built on the OSS DataHub catalog. 🔗 https://www.acryldata.io/

<a id="t-adf"></a>
**Azure Data Factory** — *(C)* — Microsoft cloud ETL/orchestration service. 🔗 https://learn.microsoft.com/azure/data-factory/

<a id="t-adls"></a>
**Azure Data Lake Storage Gen2** — *(C)* — hierarchical-namespace object storage on Azure Blob. 🔗 https://learn.microsoft.com/azure/storage/blobs/data-lake-storage-introduction

<a id="t-aerospike"></a>
**Aerospike** — *(E, C)* — high-performance distributed NoSQL key-value store. 🔗 https://aerospike.com/docs/

<a id="t-aim"></a>
**Aim** — *(OS)* — open-source experiment tracker. 🔗 https://aimstack.io/

<a id="t-allegrograph"></a>
**AllegroGraph** — *(E, C)* — RDF triple store with semantic reasoning (Franz Inc.). 🔗 https://allegrograph.com/

<a id="t-ansible"></a>
**Ansible** — *(OS)* — agentless configuration management (Red Hat). 🔗 https://docs.ansible.com/

<a id="t-archi"></a>
**Archi** — *(OS)* — open-source ArchiMate modeling tool. 🔗 https://www.archimatetool.com/

<a id="t-asa"></a>
**Azure Stream Analytics** — *(C)* — managed real-time event processing on Azure. 🔗 https://learn.microsoft.com/azure/stream-analytics/

<a id="t-asr"></a>
**Azure Site Recovery** — *(C)* — Azure-native disaster recovery orchestration. 🔗 https://learn.microsoft.com/azure/site-recovery/

<a id="t-awscdk"></a>
**AWS CDK** — *(OS)* — AWS Cloud Development Kit; define CloudFormation stacks in TypeScript/Python/Java. 🔗 https://docs.aws.amazon.com/cdk/

<a id="t-airbyte"></a>
**Airbyte** — *(OS, C)* — open-source ELT connector platform. 🔗 https://docs.airbyte.com/

<a id="t-airflow"></a>
**Apache Airflow** — *(OS)* — Python-based workflow orchestrator. 🔗 https://airflow.apache.org/docs/

<a id="t-alation"></a>
**Alation** — *(E, C)* — enterprise data catalog and governance platform. 🔗 https://docs.alation.com/

<a id="t-alembic"></a>
**Alembic** — *(OS)* — SQLAlchemy-based Python schema migration tool. 🔗 https://alembic.sqlalchemy.org/

<a id="t-algolia"></a>
**Algolia** — *(C)* — managed search-as-a-service. 🔗 https://www.algolia.com/doc/

<a id="t-alteryx"></a>
**Alteryx (Trifacta)** — *(E, C)* — visual data preparation and analytics platform. 🔗 https://help.alteryx.com/

<a id="t-amundsen"></a>
**Amundsen** — *(OS)* — Lyft's open-source metadata/discovery platform. 🔗 https://www.amundsen.io/

<a id="t-anomalo"></a>
**Anomalo** — *(C)* — automated data quality monitoring with ML anomaly detection. 🔗 https://www.anomalo.com/

<a id="t-apicurio"></a>
**Apicurio Registry** — *(OS)* — Red Hat schema registry for Avro/Protobuf/JSON. 🔗 https://www.apicur.io/registry/docs/

<a id="t-apigee"></a>
**Apigee** — *(C)* — Google Cloud API management. 🔗 https://cloud.google.com/apigee/docs

<a id="t-apollo"></a>
**Apollo GraphQL** — *(OS, C)* — GraphQL platform and federation gateway. 🔗 https://www.apollographql.com/docs/

<a id="t-appsmith"></a>
**Appsmith** — *(OS, C)* — open-source low-code internal tool builder. 🔗 https://docs.appsmith.com/

<a id="t-apptio"></a>
**Apptio** — *(C)* — IT financial management / FinOps platform. 🔗 https://www.apptio.com/

<a id="t-arango"></a>
**ArangoDB** — *(OS)* — multi-model graph/document database. 🔗 https://docs.arangodb.com/

<a id="t-argo"></a>
**Argo Workflows** — *(OS)* — Kubernetes-native workflow engine. 🔗 https://argo-workflows.readthedocs.io/

<a id="t-argocd"></a>
**Argo CD** — *(OS)* — Kubernetes GitOps continuous delivery. 🔗 https://argo-cd.readthedocs.io/

<a id="t-arrow"></a>
**Apache Arrow** — *(OS)* — language-agnostic in-memory columnar format. 🔗 https://arrow.apache.org/docs/

<a id="t-athena"></a>
**AWS Athena** — *(C)* — serverless Presto/Trino-based SQL on S3. 🔗 https://docs.aws.amazon.com/athena/

<a id="t-atlan"></a>
**Atlan** — *(C)* — modern active-metadata data catalog. 🔗 https://docs.atlan.com/

<a id="t-atlas"></a>
**Atlas (Ariga)** — *(OS)* — declarative schema migration tool. 🔗 https://atlasgo.io/docs

<a id="t-atscale"></a>
**AtScale** — *(E)* — universal semantic layer over warehouses/lakehouses. 🔗 https://documentation.atscale.com/

<a id="t-auth0"></a>
**Auth0** — *(C)* — Okta-owned identity-as-a-service. 🔗 https://auth0.com/docs

<a id="t-avro"></a>
**Apache Avro** — *(OS)* — binary serialization format with schema evolution. 🔗 https://avro.apache.org/docs/

<a id="t-awsapigw"></a>
**AWS API Gateway** — *(C)* — managed REST/HTTP/WebSocket API gateway. 🔗 https://docs.aws.amazon.com/apigateway/

<a id="t-awsbackup"></a>
**AWS Backup** — *(C)* — centralized backup across AWS services. 🔗 https://docs.aws.amazon.com/aws-backup/

<a id="t-awsdataexchange"></a>
**AWS Data Exchange** — *(C)* — third-party data subscription marketplace. 🔗 https://docs.aws.amazon.com/data-exchange/

<a id="t-awsdms"></a>
**AWS DMS** — *(C)* — Database Migration Service with CDC. 🔗 https://docs.aws.amazon.com/dms/

<a id="t-awsiam"></a>
**AWS IAM** — *(C)* — AWS identity and access management. 🔗 https://docs.aws.amazon.com/iam/

<a id="t-awswar"></a>
**AWS Well-Architected Framework** — *(C)* — AWS reference architecture framework. 🔗 https://aws.amazon.com/architecture/well-architected/

<a id="t-axiom"></a>
**AxiomSL (Adenza)** — *(E)* — enterprise regulatory reporting platform. 🔗 https://www.adenza.com/

<a id="t-azbackup"></a>
**Azure Backup** — *(C)* — Azure-native backup service. 🔗 https://learn.microsoft.com/azure/backup/

<a id="t-azcost"></a>
**Azure Cost Management** — *(C)* — Microsoft cloud cost analytics. 🔗 https://learn.microsoft.com/azure/cost-management-billing/

<a id="t-azdevops"></a>
**Azure DevOps** — *(C)* — Microsoft CI/CD and project management. 🔗 https://learn.microsoft.com/azure/devops/

<a id="t-azdurable"></a>
**Azure Durable Functions** — *(C)* — durable workflow extension for Azure Functions; orchestrator/activity functions in C#/Python/JS/Java. 🔗 https://learn.microsoft.com/azure/azure-functions/durable/

<a id="t-azfunc"></a>
**Azure Functions** — *(C)* — Microsoft serverless compute. 🔗 https://learn.microsoft.com/azure/azure-functions/

<a id="t-azmonitor"></a>
**Azure Monitor** — *(C)* — Azure observability and audit logging. 🔗 https://learn.microsoft.com/azure/azure-monitor/

<a id="t-azureaisearch"></a>
**Azure AI Search** — *(C)* — managed vector + keyword search with RAG features. 🔗 https://learn.microsoft.com/azure/search/

<a id="t-azureblob"></a>
**Azure Blob Storage** — *(C)* — Azure object storage with lifecycle policies. 🔗 https://learn.microsoft.com/azure/storage/blobs/

<a id="t-azurecaf"></a>
**Azure Cloud Adoption Framework** — *(C)* — Microsoft cloud adoption guidance. 🔗 https://learn.microsoft.com/azure/cloud-adoption-framework/

<a id="t-azuredisks"></a>
**Azure Managed Disks** — *(C)* — Azure block storage. 🔗 https://learn.microsoft.com/azure/virtual-machines/managed-disks-overview

<a id="t-azurefiles"></a>
**Azure Files** — *(C)* — managed SMB/NFS file shares. 🔗 https://learn.microsoft.com/azure/storage/files/

<a id="t-azureml"></a>
**Azure Machine Learning** — *(C)* — Microsoft managed ML platform. 🔗 https://learn.microsoft.com/azure/machine-learning/

<a id="t-azuresql"></a>
**Azure SQL Database** — *(C)* — managed SQL Server in Azure. 🔗 https://learn.microsoft.com/azure/azure-sql/

## B

<a id="t-b2"></a>
**Backblaze B2** — *(C)* — low-cost S3-compatible cloud object storage. 🔗 https://www.backblaze.com/docs/cloud-storage

<a id="t-backstage"></a>
**Backstage** — *(OS)* — Spotify's open-source developer portal. 🔗 https://backstage.io/docs/

<a id="t-bedrock"></a>
**AWS Bedrock** — *(C)* — managed foundation models with knowledge bases (RAG). 🔗 https://docs.aws.amazon.com/bedrock/

<a id="t-beam"></a>
**Apache Beam** — *(OS)* — unified batch + streaming programming model. 🔗 https://beam.apache.org/documentation/

<a id="t-bento"></a>
**BentoML** — *(OS)* — model packaging and serving framework. 🔗 https://docs.bentoml.com/

<a id="t-bicep"></a>
**Azure Bicep / ARM** — *(OS)* — domain-specific language for declaring Azure resources; transpiles to ARM. 🔗 https://learn.microsoft.com/azure/azure-resource-manager/bicep/

<a id="t-bigeye"></a>
**Bigeye** — *(C)* — data observability and quality monitoring platform. 🔗 https://docs.bigeye.com/

<a id="t-bigid"></a>
**BigID** — *(E, C)* — data discovery, classification, privacy. 🔗 https://bigid.com/

<a id="t-bigquery"></a>
**BigQuery** — *(C)* — Google serverless analytical warehouse. 🔗 https://cloud.google.com/bigquery/docs

<a id="t-bigtable"></a>
**Cloud Bigtable** — *(C)* — Google wide-column NoSQL store. 🔗 https://cloud.google.com/bigtable/docs

<a id="t-birt"></a>
**Eclipse BIRT** — *(OS)* — Business Intelligence and Reporting Tools. 🔗 https://eclipse.github.io/birt-website/

<a id="t-bitbucket"></a>
**Bitbucket** — *(C)* — Atlassian Git hosting. 🔗 https://support.atlassian.com/bitbucket-cloud/

<a id="t-blazegraph"></a>
**Blazegraph** — *(OS, archived)* — RDF triple store; powered Wikidata Query Service for years. Now legacy / unmaintained. 🔗 https://blazegraph.com/

<a id="t-bloomreach"></a>
**Bloomreach** — *(C)* — customer data platform with ecommerce focus. 🔗 https://documentation.bloomreach.com/

<a id="t-bluesky"></a>
**Bluesky (data.bluesky)** — *(C)* — Snowflake/BigQuery FinOps platform. 🔗 https://www.getbluesky.io/

<a id="t-bpmnio"></a>
**bpmn.io** — *(OS)* — open-source web-based BPMN/DMN/CMMN modeling toolkit (Camunda). 🔗 https://bpmn.io/

<a id="t-bo"></a>
**SAP BusinessObjects** — *(E)* — SAP's enterprise BI suite. 🔗 https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM

<a id="t-boomi"></a>
**Boomi** — *(C)* — iPaaS integration platform. 🔗 https://help.boomi.com/

<a id="t-budibase"></a>
**Budibase** — *(OS, C)* — open-source low-code internal tool platform. 🔗 https://docs.budibase.com/

## C

<a id="t-cadence"></a>
**Cadence** — *(OS)* — Uber's durable workflow engine; predecessor of Temporal. 🔗 https://cadenceworkflow.io/docs/

<a id="t-camunda"></a>
**Camunda** — *(OS, C, E)* — leading BPMN/DMN process orchestration platform; Camunda 7 (legacy Java engine, OS) and Camunda 8 (Zeebe-based, source-available core + commercial). Heavily used in financial services. 🔗 https://docs.camunda.io/

<a id="t-cassandra"></a>
**Apache Cassandra** — *(OS)* — distributed wide-column NoSQL database. 🔗 https://cassandra.apache.org/doc/

<a id="t-cedar"></a>
**Cedar** — *(OS)* — AWS-developed authorization policy language and engine. 🔗 https://www.cedarpolicy.com/

<a id="t-ceph"></a>
**Ceph** — *(OS)* — distributed object/block/file storage. 🔗 https://docs.ceph.com/

<a id="t-census"></a>
**Census** — *(C)* — reverse ETL platform. 🔗 https://docs.getcensus.com/

<a id="t-chef"></a>
**Chef** — *(OS, E)* — Ruby-DSL configuration management (Progress Software). 🔗 https://docs.chef.io/

<a id="t-chroma"></a>
**Chroma** — *(OS)* — open-source embeddings/vector database. 🔗 https://docs.trychroma.com/

<a id="t-chronon"></a>
**Chronon** — *(OS)* — Airbnb's open-source feature platform with batch + streaming feature definitions. 🔗 https://chronon.ai/

<a id="t-circleci"></a>
**CircleCI** — *(C)* — cloud CI/CD platform. 🔗 https://circleci.com/docs/

<a id="t-clearml"></a>
**ClearML** — *(OS, C)* — MLOps platform with experiment tracking. 🔗 https://clear.ml/docs/

<a id="t-clickhouse"></a>
**ClickHouse** — *(OS, C)* — high-performance columnar OLAP DBMS. 🔗 https://clickhouse.com/docs

<a id="t-cloudability"></a>
**Cloudability (Apptio)** — *(C)* — cloud cost management. 🔗 https://www.apptio.com/products/cloudability/

<a id="t-cloudhealth"></a>
**CloudHealth (VMware Tanzu)** — *(C)* — cloud cost & governance platform. 🔗 https://cloudhealth.vmware.com/

<a id="t-cloudsql"></a>
**Cloud SQL** — *(C)* — Google managed Postgres/MySQL/SQL Server. 🔗 https://cloud.google.com/sql/docs

<a id="t-cloudtrail"></a>
**AWS CloudTrail** — *(C)* — AWS API audit log. 🔗 https://docs.aws.amazon.com/cloudtrail/

<a id="t-cluedin"></a>
**CluedIn** — *(E, C)* — graph-based MDM and reference data. 🔗 https://documentation.cluedin.net/

<a id="t-cloudformation"></a>
**AWS CloudFormation** — *(C)* — AWS-native declarative template service for provisioning AWS resources. 🔗 https://docs.aws.amazon.com/cloudformation/

<a id="t-coalesce"></a>
**Coalesce** — *(C)* — visual data transformation platform on Snowflake. 🔗 https://docs.coalesce.io/

<a id="t-cockroach"></a>
**CockroachDB** — *(SA, C)* — distributed SQL database with strong consistency. **License note (Nov 2024):** moved to CockroachDB Software License (CSL), source-available, free for orgs under $10M revenue, paid otherwise. Not OSI-approved. 🔗 https://www.cockroachlabs.com/docs/

<a id="t-cognos"></a>
**IBM Cognos Analytics** — *(E)* — IBM's enterprise BI suite. 🔗 https://www.ibm.com/docs/en/cognos-analytics

<a id="t-cohere"></a>
**Cohere** — *(C)* — managed LLM and embedding APIs. 🔗 https://docs.cohere.com/

<a id="t-cohesity"></a>
**Cohesity** — *(E, C)* — enterprise data protection and DR platform. 🔗 https://www.cohesity.com/

<a id="t-colab"></a>
**Google Colab** — *(C)* — hosted Jupyter notebooks with GPU/TPU. 🔗 https://colab.research.google.com/

<a id="t-collibra"></a>
**Collibra** — *(E, C)* — enterprise data governance and catalog platform. 🔗 https://productresources.collibra.com/

<a id="t-comet"></a>
**Comet** — *(C)* — ML experiment tracking and model monitoring. 🔗 https://www.comet.com/docs/

<a id="t-commvault"></a>
**Commvault** — *(E, C)* — enterprise backup and data protection. 🔗 https://documentation.commvault.com/

<a id="t-composer"></a>
**Cloud Composer** — *(C)* — GCP managed Airflow. 🔗 https://cloud.google.com/composer/docs

<a id="t-conductor"></a>
**Netflix Conductor** — *(OS)* — microservices orchestration engine; JSON-defined workflows, multi-language workers. 🔗 https://conductor-oss.github.io/conductor/

<a id="t-confluent"></a>
**Confluent Cloud** — *(C)* — managed Kafka with schema registry, ksqlDB, connectors. **License note:** Confluent Platform components use the Confluent Community License (source-available, not OSI-approved); core Kafka itself remains Apache 2.0. 🔗 https://docs.confluent.io/cloud/

<a id="t-contextmapper"></a>
**Context Mapper** — *(OS)* — DSL/tools for DDD strategic design and bounded contexts. 🔗 https://contextmapper.org/

<a id="t-costexplorer"></a>
**AWS Cost Explorer** — *(C)* — AWS cost and usage analytics. 🔗 https://docs.aws.amazon.com/cost-management/

<a id="t-couchbase"></a>
**Couchbase** — *(OS, E, C)* — NoSQL document database with N1QL. 🔗 https://docs.couchbase.com/

<a id="t-crossplane"></a>
**Crossplane** — *(OS)* — Kubernetes-native control plane for managing cloud infrastructure (CNCF). 🔗 https://docs.crossplane.io/

<a id="t-crystal"></a>
**SAP Crystal Reports** — *(E)* — paginated reporting tool. 🔗 https://help.sap.com/docs/SAP_CRYSTAL_REPORTS

<a id="t-csr"></a>
**Confluent Schema Registry** — *(OS, C)* — schema registry for Kafka. 🔗 https://docs.confluent.io/platform/current/schema-registry/

<a id="t-cube"></a>
**Cube** — *(OS, C)* — semantic/metrics layer with REST/GraphQL/SQL APIs. 🔗 https://cube.dev/docs/

<a id="t-cursor"></a>
**Cursor** — *(C)* — AI-native code editor. 🔗 https://docs.cursor.com/

## D

<a id="t-d3"></a>
**D3.js** — *(OS)* — JavaScript visualization library. 🔗 https://d3js.org/

<a id="t-dagster"></a>
**Dagster** — *(OS, C)* — data-aware (asset-oriented) Python orchestrator with strong typing, software-defined assets, and integrated lineage. 🔗 https://docs.dagster.io/

<a id="t-dama"></a>
**DAMA International / DMBOK** — *(reference)* — data management body of knowledge framework. 🔗 https://www.dama.org/

<a id="t-dask"></a>
**Dask** — *(OS)* — Python parallel computing for analytics. 🔗 https://docs.dask.org/

<a id="t-databand"></a>
**Databand (IBM)** — *(C)* — data pipeline observability. 🔗 https://www.ibm.com/products/databand

<a id="t-databrew"></a>
**AWS Glue DataBrew** — *(C)* — visual data preparation. 🔗 https://docs.aws.amazon.com/databrew/

<a id="t-databricks"></a>
**Databricks** — *(C)* — unified lakehouse platform (Spark, Delta, MLflow, Unity Catalog). 🔗 https://docs.databricks.com/

<a id="t-datadiff"></a>
**data-diff** — *(OS)* — open-source database/dataset diffing tool. 🔗 https://github.com/datafold/data-diff

<a id="t-datadog"></a>
**Datadog** — *(C)* — observability, APM, SIEM, SLOs. 🔗 https://docs.datadoghq.com/

<a id="t-datafold"></a>
**Datafold** — *(C)* — data diff, regression testing, lineage in CI. 🔗 https://docs.datafold.com/

<a id="t-dataform"></a>
**Dataform** — *(C, OS)* — GCP SQL transformation tool (now part of BigQuery). 🔗 https://cloud.google.com/dataform/docs

<a id="t-datagrail"></a>
**DataGrail** — *(C)* — privacy and consent management. 🔗 https://www.datagrail.io/

<a id="t-datagrip"></a>
**DataGrip** — *(E)* — JetBrains database IDE. 🔗 https://www.jetbrains.com/help/datagrip/

<a id="t-datahub"></a>
**DataHub** — *(OS)* — open-source data catalog/lineage/contracts platform (LinkedIn). 🔗 https://datahubproject.io/docs/

<a id="t-datamasker"></a>
**DataMasker / Redgate Data Masker** — *(E)* — enterprise data masking tool for SQL Server / Oracle. 🔗 https://www.red-gate.com/products/data-masker/

<a id="t-dataprep"></a>
**DataPrep** — *(OS)* — Python library for data exploration, profiling, and cleaning. 🔗 https://docs.dataprep.ai/

<a id="t-datarade"></a>
**Datarade** — *(C)* — third-party data marketplace and discovery platform. 🔗 https://datarade.ai/

<a id="t-dataflow"></a>
**Cloud Dataflow** — *(C)* — GCP managed Apache Beam runner. 🔗 https://cloud.google.com/dataflow/docs

<a id="t-dataproc"></a>
**Cloud Dataproc** — *(C)* — GCP managed Spark/Hadoop. 🔗 https://cloud.google.com/dataproc/docs

<a id="t-datastage"></a>
**IBM DataStage** — *(E)* — IBM enterprise ETL. 🔗 https://www.ibm.com/docs/en/iis

<a id="t-dataworld"></a>
**data.world** — *(C)* — knowledge-graph data catalog and collaboration. 🔗 https://docs.data.world/

<a id="t-dbeaver"></a>
**DBeaver** — *(OS)* — universal SQL client / database tool. 🔗 https://dbeaver.io/docs/

<a id="t-dbt"></a>
**dbt Core** — *(OS)* — SQL-based transformation, testing, docs. 🔗 https://docs.getdbt.com/

<a id="t-dbtcloud"></a>
**dbt Cloud** — *(C)* — managed dbt with IDE, scheduler, semantic layer. 🔗 https://docs.getdbt.com/docs/cloud/

<a id="t-demyst"></a>
**Demyst** — *(C)* — external data marketplace for financial services. 🔗 https://demyst.com/

<a id="t-dcs"></a>
**Data Contract Specification** — *(OS spec)* — open spec for data contracts. 🔗 https://datacontract.com/

<a id="t-deepeval"></a>
**DeepEval** — *(OS)* — LLM evaluation framework. 🔗 https://docs.confident-ai.com/

<a id="t-deepnote"></a>
**Deepnote** — *(C)* — collaborative cloud notebook. 🔗 https://deepnote.com/docs

<a id="t-deepspeed"></a>
**DeepSpeed** — *(OS)* — Microsoft distributed training optimization library. 🔗 https://www.deepspeed.ai/

<a id="t-debezium"></a>
**Debezium** — *(OS)* — log-based CDC for many databases. 🔗 https://debezium.io/documentation/

<a id="t-deequ"></a>
**Deequ** — *(OS)* — Spark-based data quality library (AWS Labs). 🔗 https://github.com/awslabs/deequ

<a id="t-delphix"></a>
**Delphix** — *(E)* — data masking and test-data management. 🔗 https://docs.delphix.com/

<a id="t-delta"></a>
**Delta Lake** — *(OS)* — ACID table format originally from Databricks. 🔗 https://docs.delta.io/

<a id="t-deltasharing"></a>
**Delta Sharing** — *(OS)* — open protocol for cross-org data sharing. 🔗 https://delta.io/sharing/

<a id="t-docdb"></a>
**Amazon DocumentDB** — *(C)* — MongoDB-compatible managed document DB. 🔗 https://docs.aws.amazon.com/documentdb/

<a id="t-docusaurus"></a>
**Docusaurus** — *(OS)* — Meta's documentation static site generator. 🔗 https://docusaurus.io/docs

<a id="t-doppler"></a>
**Doppler** — *(C)* — secrets management platform. 🔗 https://docs.doppler.com/

<a id="t-dvbuilder"></a>
**Datavault Builder** — *(E)* — Data Vault automation suite. 🔗 https://www.datavault-builder.com/

<a id="t-drata"></a>
**Drata** — *(C)* — continuous compliance automation (SOC 2, ISO 27001, etc.). 🔗 https://drata.com/

<a id="t-drawio"></a>
**draw.io / diagrams.net** — *(OS, C)* — diagramming tool. 🔗 https://www.drawio.com/

<a id="t-dremio"></a>
**Dremio** — *(C, OS)* — lakehouse query engine and catalog. 🔗 https://docs.dremio.com/

<a id="t-dreamfactory"></a>
**DreamFactory** — *(OS, E)* — auto-generated REST APIs over databases. 🔗 https://wiki.dreamfactory.com/

<a id="t-drill"></a>
**Apache Drill** — *(OS)* — schema-free SQL query engine. 🔗 https://drill.apache.org/docs/

<a id="t-druid"></a>
**Apache Druid** — *(OS)* — real-time OLAP database. 🔗 https://druid.apache.org/docs/

<a id="t-druva"></a>
**Druva** — *(C)* — cloud-native data protection and DR. 🔗 https://docs.druva.com/

<a id="t-duckdb"></a>
**DuckDB** — *(OS)* — embedded analytical database (SQLite for OLAP). 🔗 https://duckdb.org/docs/

<a id="t-dvc"></a>
**DVC** — *(OS)* — Git-based data and model versioning. 🔗 https://dvc.org/doc

<a id="t-dynamodb"></a>
**Amazon DynamoDB** — *(C)* — serverless NoSQL key-value store. 🔗 https://docs.aws.amazon.com/dynamodb/

<a id="t-dynatrace"></a>
**Dynatrace** — *(E, C)* — full-stack observability platform. 🔗 https://docs.dynatrace.com/

## E

<a id="t-ebs"></a>
**AWS EBS** — *(C)* — elastic block storage. 🔗 https://docs.aws.amazon.com/ebs/

<a id="t-echarts"></a>
**Apache ECharts** — *(OS)* — JavaScript charting library. 🔗 https://echarts.apache.org/

<a id="t-edr"></a>
**AWS Elastic Disaster Recovery** — *(C)* — replicated DR for on-prem and cloud. 🔗 https://docs.aws.amazon.com/drs/

<a id="t-efs"></a>
**AWS EFS** — *(C)* — managed NFS file system. 🔗 https://docs.aws.amazon.com/efs/

<a id="t-elastic"></a>
**Elasticsearch / Elastic Stack** — *(OS, C)* — search engine, observability, SIEM. 🔗 https://www.elastic.co/guide/

<a id="t-elasticache"></a>
**AWS ElastiCache** — *(C)* — managed Redis/Memcached. 🔗 https://docs.aws.amazon.com/elasticache/

<a id="t-elementary"></a>
**Elementary** — *(OS)* — dbt-native data observability. 🔗 https://docs.elementary-data.com/

<a id="t-embeddable"></a>
**Embeddable** — *(C)* — embedded analytics platform. 🔗 https://docs.embeddable.com/

<a id="t-emr"></a>
**AWS EMR** — *(C)* — managed Spark/Hadoop/Presto. 🔗 https://docs.aws.amazon.com/emr/

<a id="t-entra"></a>
**Microsoft Entra ID (Azure AD)** — *(C)* — Microsoft cloud identity. 🔗 https://learn.microsoft.com/entra/

<a id="t-erstudio"></a>
**ER/Studio (IDERA)** — *(E)* — enterprise data modeling tool. 🔗 https://www.idera.com/er-studio/

<a id="t-erwin"></a>
**erwin Data Modeler (Quest)** — *(E)* — enterprise data modeling tool. 🔗 https://www.quest.com/products/erwin-data-modeler/

<a id="t-eventbridge"></a>
**AWS EventBridge** — *(C)* — managed event bus / event mesh on AWS; supports CloudEvents. 🔗 https://docs.aws.amazon.com/eventbridge/

<a id="t-evidence"></a>
**Evidence** — *(OS)* — code-first BI in markdown + SQL. 🔗 https://docs.evidence.dev/

<a id="t-exasol"></a>
**Exasol** — *(E, C)* — in-memory MPP analytical database. 🔗 https://docs.exasol.com/

<a id="t-eventhubs"></a>
**Azure Event Hubs** — *(C)* — managed event streaming (Kafka-compatible). 🔗 https://learn.microsoft.com/azure/event-hubs/

<a id="t-explo"></a>
**Explo** — *(C)* — embedded analytics and dashboards. 🔗 https://docs.explo.co/

## F

<a id="t-faker"></a>
**Faker** — *(OS)* — Python library for generating fake names, addresses, etc. (also faker.js for JavaScript). 🔗 https://faker.readthedocs.io/

<a id="t-feast"></a>
**Feast** — *(OS)* — open-source feature store. 🔗 https://docs.feast.dev/

<a id="t-featureform"></a>
**Featureform** — *(OS, C)* — open-source virtual feature store / feature platform. 🔗 https://docs.featureform.com/

<a id="t-filebeat"></a>
**Filebeat** — *(OS)* — Elastic-stack log shipper. 🔗 https://www.elastic.co/guide/en/beats/filebeat/

<a id="t-firebolt"></a>
**Firebolt** — *(C)* — high-performance cloud data warehouse. 🔗 https://docs.firebolt.io/

<a id="t-firehose"></a>
**AWS Kinesis Data Firehose** — *(C)* — managed streaming delivery. 🔗 https://docs.aws.amazon.com/firehose/

<a id="t-firehydrant"></a>
**FireHydrant** — *(C)* — incident management and postmortems. 🔗 https://docs.firehydrant.com/

<a id="t-firestore"></a>
**Firestore** — *(C)* — Google managed document database. 🔗 https://firebase.google.com/docs/firestore

<a id="t-fivetran"></a>
**Fivetran** — *(C)* — managed ELT connector platform. 🔗 https://fivetran.com/docs

<a id="t-flink"></a>
**Apache Flink** — *(OS)* — stateful stream processing engine. 🔗 https://flink.apache.org/

<a id="t-flowable"></a>
**Flowable** — *(OS, E)* — Java-based BPMN/CMMN/DMN process engine; fork of Activiti. 🔗 https://www.flowable.com/open-source/docs/

<a id="t-fluentbit"></a>
**Fluent Bit** — *(OS)* — lightweight log/metric processor. 🔗 https://docs.fluentbit.io/

<a id="t-fluentd"></a>
**Fluentd** — *(OS)* — unified logging layer. 🔗 https://docs.fluentd.org/

<a id="t-flyway"></a>
**Flyway** — *(OS, E)* — database migration tool. 🔗 https://documentation.red-gate.com/fd/

## G

<a id="t-gable"></a>
**Gable** — *(C)* — data contracts platform. 🔗 https://www.gable.ai/

<a id="t-gatling"></a>
**Gatling** — *(OS, E)* — Scala-based load testing tool. 🔗 https://docs.gatling.io/

<a id="t-gcs"></a>
**Google Cloud Storage** — *(C)* — GCP object storage. 🔗 https://cloud.google.com/storage/docs

<a id="t-gcpbackup"></a>
**Google Cloud Backup and DR** — *(C)* — GCP managed backup/DR. 🔗 https://cloud.google.com/backup-disaster-recovery/docs

<a id="t-gcpbilling"></a>
**GCP Billing** — *(C)* — Google cloud cost management. 🔗 https://cloud.google.com/billing/docs

<a id="t-gcpcaf"></a>
**GCP Cloud Adoption Framework** — *(C)* — GCP cloud adoption guidance. 🔗 https://cloud.google.com/adoption-framework

<a id="t-gcpcf"></a>
**GCP Cloud Functions** — *(C)* — Google serverless compute. 🔗 https://cloud.google.com/functions/docs

<a id="t-gcpdlp"></a>
**Google Cloud Sensitive Data Protection (DLP)** — *(C)* — PII discovery/classification. 🔗 https://cloud.google.com/sensitive-data-protection/docs

<a id="t-gcpdts"></a>
**GCP Data Transfer Service** — *(C)* — managed data transfer to BigQuery/GCS. 🔗 https://cloud.google.com/bigquery-transfer/docs

<a id="t-gcpkms"></a>
**Google Cloud KMS** — *(C)* — GCP key management. 🔗 https://cloud.google.com/kms/docs

<a id="t-gcppd"></a>
**GCP Persistent Disk** — *(C)* — GCP block storage. 🔗 https://cloud.google.com/persistent-disk

<a id="t-gcpdm"></a>
**GCP Deployment Manager** — *(C)* — GCP-native declarative infrastructure templates (legacy; Terraform/Config Connector is current direction). 🔗 https://cloud.google.com/deployment-manager/docs

<a id="t-gcpsecrets"></a>
**Google Secret Manager** — *(C)* — GCP secrets store. 🔗 https://cloud.google.com/secret-manager/docs

<a id="t-ge"></a>
**Great Expectations** — *(OS)* — data validation and documentation framework. 🔗 https://docs.greatexpectations.io/

<a id="t-geoparquet"></a>
**GeoParquet** — *(OS spec)* — open standard for storing geospatial vector data in Apache Parquet. 🔗 https://geoparquet.org/

<a id="t-gerrit"></a>
**Gerrit** — *(OS)* — code review for Git. 🔗 https://gerrit-review.googlesource.com/Documentation/

<a id="t-ghactions"></a>
**GitHub Actions** — *(C)* — CI/CD integrated with GitHub. 🔗 https://docs.github.com/actions

<a id="t-gitea"></a>
**Gitea** — *(OS)* — self-hosted Git service. 🔗 https://docs.gitea.com/

<a id="t-github"></a>
**GitHub** — *(C, E)* — Git hosting + CI/CD + collaboration. 🔗 https://docs.github.com/

<a id="t-gitlab"></a>
**GitLab** — *(OS, C, E)* — Git hosting + CI/CD + DevSecOps platform. 🔗 https://docs.gitlab.com/

<a id="t-gitlfs"></a>
**Git LFS** — *(OS)* — Git extension for large file versioning. 🔗 https://git-lfs.com/

<a id="t-gluecatalog"></a>
**AWS Glue Data Catalog** — *(C)* — Hive-compatible AWS catalog. 🔗 https://docs.aws.amazon.com/glue/latest/dg/components-overview.html

<a id="t-glueregistry"></a>
**AWS Glue Schema Registry** — *(C)* — schema registry for Avro/JSON/Protobuf. 🔗 https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html

<a id="t-gluster"></a>
**GlusterFS** — *(OS)* — distributed network file system. 🔗 https://docs.gluster.org/

<a id="t-goldengate"></a>
**Oracle GoldenGate** — *(E)* — enterprise log-based replication and CDC. 🔗 https://docs.oracle.com/en/middleware/goldengate/

<a id="t-gomigrate"></a>
**golang-migrate** — *(OS)* — Go DB schema migration tool. 🔗 https://github.com/golang-migrate/migrate

<a id="t-gradio"></a>
**Gradio** — *(OS)* — Python data app/demo framework (Hugging Face). 🔗 https://www.gradio.app/docs

<a id="t-grafana"></a>
**Grafana / Grafana Cloud** — *(OS, C)* — observability dashboards, SLOs, OnCall. **License note:** Grafana relicensed core to AGPLv3 in 2021. 🔗 https://grafana.com/docs/

<a id="t-graphdb"></a>
**Ontotext GraphDB** — *(E, C)* — enterprise RDF triple store with reasoning. Free tier available. 🔗 https://graphdb.ontotext.com/documentation/

<a id="t-gravitino"></a>
**Apache Gravitino** — *(OS)* — Datastrato-led multi-source metadata catalog (incubating in Apache). 🔗 https://gravitino.apache.org/

<a id="t-greenplum"></a>
**Greenplum** — *(OS, E)* — Postgres-based MPP analytical DB (Broadcom/VMware). 🔗 https://docs.vmware.com/en/VMware-Tanzu-Greenplum/

<a id="t-gretel"></a>
**Gretel.ai** — *(C)* — synthetic data platform with privacy-preserving ML training data. 🔗 https://docs.gretel.ai/

<a id="t-griffin"></a>
**Apache Griffin** — *(OS)* — open-source data quality solution for batch and streaming. 🔗 https://griffin.apache.org/

<a id="t-growthloop"></a>
**GrowthLoop** — *(C)* — composable CDP / audience activation on the data warehouse. 🔗 https://www.growthloop.com/

## H

<a id="t-h3"></a>
**H3** — *(OS)* — Uber's hexagonal hierarchical geospatial indexing system. 🔗 https://h3geo.org/

<a id="t-hackolade"></a>
**Hackolade** — *(E)* — schema design for SQL, NoSQL, JSON Schema, etc. 🔗 https://hackolade.com/help/

<a id="t-hadoop"></a>
**Apache Hadoop** — *(OS)* — distributed storage (HDFS) and MapReduce. 🔗 https://hadoop.apache.org/docs/

<a id="t-haystack"></a>
**Haystack (deepset)** — *(OS)* — RAG/LLM application framework. 🔗 https://docs.haystack.deepset.ai/

<a id="t-hasura"></a>
**Hasura** — *(OS, C)* — instant GraphQL APIs over databases. 🔗 https://hasura.io/docs/

<a id="t-hazelcast"></a>
**Hazelcast** — *(OS, E)* — in-memory data grid and stream processing. 🔗 https://docs.hazelcast.com/

<a id="t-hbase"></a>
**Apache HBase** — *(OS)* — Hadoop-based wide-column NoSQL DB. 🔗 https://hbase.apache.org/book.html

<a id="t-hdfs"></a>
**HDFS** — *(OS)* — Hadoop Distributed File System. 🔗 https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/

<a id="t-hdinsight"></a>
**Azure HDInsight** — *(C)* — Azure managed Hadoop/Spark. 🔗 https://learn.microsoft.com/azure/hdinsight/

<a id="t-helicone"></a>
**Helicone** — *(OS, C)* — LLM observability and prompt management. 🔗 https://docs.helicone.ai/

<a id="t-hex"></a>
**Hex** — *(C)* — collaborative data workspace and notebook. 🔗 https://learn.hex.tech/

<a id="t-hightouch"></a>
**Hightouch** — *(C)* — reverse ETL / data activation platform. 🔗 https://hightouch.com/docs

<a id="t-hopsworks"></a>
**Hopsworks** — *(OS, E, C)* — feature store + ML platform. 🔗 https://docs.hopsworks.ai/

<a id="t-horovod"></a>
**Horovod** — *(OS)* — distributed deep learning training library. 🔗 https://horovod.readthedocs.io/

<a id="t-hudi"></a>
**Apache Hudi** — *(OS)* — table format for incremental processing on lakes. 🔗 https://hudi.apache.org/docs/

<a id="t-hvr"></a>
**Fivetran HVR** — *(E, C)* — log-based replication for enterprise databases. 🔗 https://fivetran.com/docs/hvr6

## I

<a id="t-ibmib"></a>
**IBM Integration Bus / App Connect** — *(E)* — enterprise ESB. 🔗 https://www.ibm.com/docs/en/app-connect

<a id="t-ibmilm"></a>
**IBM Information Lifecycle Management** — *(E)* — enterprise ILM. 🔗 https://www.ibm.com/docs/en/storage-protect

<a id="t-ibmmdm"></a>
**IBM InfoSphere MDM** — *(E)* — enterprise master data management. 🔗 https://www.ibm.com/docs/en/imdm

<a id="t-ibis"></a>
**Ibis** — *(OS)* — Python dataframe API portable across 20+ engines (DuckDB, BigQuery, Snowflake, Polars, Spark, etc.). 🔗 https://ibis-project.org/

<a id="t-iceberg"></a>
**Apache Iceberg** — *(OS)* — open table format with rich metadata, hidden partitioning, snapshots, branching/tagging. 🔗 https://iceberg.apache.org/docs/

<a id="t-ignite"></a>
**Apache Ignite** — *(OS)* — distributed in-memory data grid and SQL. 🔗 https://ignite.apache.org/docs/

<a id="t-immuta"></a>
**Immuta** — *(C)* — fine-grained data access control and policy. 🔗 https://docs.immuta.com/

<a id="t-impala"></a>
**Apache Impala** — *(OS)* — MPP SQL engine on Hadoop/object storage. 🔗 https://impala.apache.org/docs.html

<a id="t-imply"></a>
**Imply** — *(C, E)* — managed Apache Druid platform with Pivot UI. 🔗 https://docs.imply.io/

<a id="t-incidentio"></a>
**incident.io** — *(C)* — incident management and on-call. 🔗 https://incident.io/docs

<a id="t-influx"></a>
**InfluxDB** — *(OS, C)* — time-series database. 🔗 https://docs.influxdata.com/

<a id="t-informatica"></a>
**Informatica PowerCenter** — *(E)* — enterprise ETL platform. 🔗 https://docs.informatica.com/data-integration/powercenter.html

<a id="t-informaticadq"></a>
**Informatica Data Quality** — *(E)* — enterprise DQ platform. 🔗 https://docs.informatica.com/data-quality.html

<a id="t-informaticaedc"></a>
**Informatica EDC / IDMC** — *(E, C)* — enterprise data catalog (now Intelligent Data Management Cloud). 🔗 https://docs.informatica.com/data-catalog.html

<a id="t-informaticamdm"></a>
**Informatica MDM** — *(E, C)* — master data management. 🔗 https://docs.informatica.com/master-data-management.html

## J

<a id="t-jaeger"></a>
**Jaeger** — *(OS)* — CNCF distributed tracing platform; OpenTelemetry-compatible backend. 🔗 https://www.jaegertracing.io/docs/

<a id="t-janusgraph"></a>
**JanusGraph** — *(OS)* — distributed graph database. 🔗 https://docs.janusgraph.org/

<a id="t-jasper"></a>
**JasperReports** — *(OS, E)* — open-source paginated reporting (Jaspersoft, Cloud Software Group). 🔗 https://www.jaspersoft.com/products/jasperreports-library

<a id="t-jax"></a>
**JAX** — *(OS)* — Google's array computing + autograd + XLA. 🔗 https://jax.readthedocs.io/

<a id="t-jbpm"></a>
**jBPM** — *(OS)* — Red Hat / Kogito BPMN process engine for Java. 🔗 https://www.jbpm.org/

<a id="t-jeg"></a>
**Jupyter Enterprise Gateway** — *(OS)* — multi-user, multi-cluster Jupyter kernel gateway for production. 🔗 https://jupyter-enterprise-gateway.readthedocs.io/

<a id="t-jena"></a>
**Apache Jena** — *(OS)* — Java framework for building semantic web/RDF/SPARQL applications. 🔗 https://jena.apache.org/documentation/

<a id="t-jenkins"></a>
**Jenkins** — *(OS)* — extensible CI/CD server. 🔗 https://www.jenkins.io/doc/

<a id="t-jetbrains"></a>
**JetBrains IDEs** — *(E)* — IntelliJ, PyCharm, DataGrip, etc. 🔗 https://www.jetbrains.com/help/

<a id="t-jmeter"></a>
**Apache JMeter** — *(OS)* — load and performance testing tool. 🔗 https://jmeter.apache.org/usermanual/

<a id="t-jupyter"></a>
**Jupyter / JupyterHub** — *(OS)* — interactive notebooks and multi-user server. 🔗 https://docs.jupyter.org/

<a id="t-junit"></a>
**JUnit** — *(OS)* — Java unit testing framework. 🔗 https://junit.org/

## K

<a id="t-k6"></a>
**Grafana k6** — *(OS, C)* — load testing tool with JavaScript scripts. 🔗 https://grafana.com/docs/k6/

<a id="t-kafka"></a>
**Apache Kafka** — *(OS)* — distributed event streaming platform. 🔗 https://kafka.apache.org/documentation/

<a id="t-kafkaconnect"></a>
**Kafka Connect** — *(OS)* — pluggable Kafka↔external systems integration. 🔗 https://kafka.apache.org/documentation/#connect

<a id="t-kda"></a>
**AWS Kinesis Data Analytics / Managed Service for Apache Flink** — *(C)* — managed Flink. 🔗 https://docs.aws.amazon.com/managed-flink/

<a id="t-kdb"></a>
**kdb+ (KX)** — *(E)* — high-performance time-series and tick database. 🔗 https://code.kx.com/q/

<a id="t-keycloak"></a>
**Keycloak** — *(OS)* — open-source identity provider. 🔗 https://www.keycloak.org/documentation

<a id="t-keyvault"></a>
**Azure Key Vault** — *(C)* — Azure secrets and key management. 🔗 https://learn.microsoft.com/azure/key-vault/

<a id="t-kinesis"></a>
**AWS Kinesis Data Streams** — *(C)* — managed event streaming. 🔗 https://docs.aws.amazon.com/streams/

<a id="t-kms"></a>
**AWS KMS** — *(C)* — AWS Key Management Service. 🔗 https://docs.aws.amazon.com/kms/

<a id="t-kong"></a>
**Kong Gateway** — *(OS, C)* — API gateway built on NGINX. 🔗 https://docs.konghq.com/

<a id="t-kserve"></a>
**KServe** — *(OS)* — Kubernetes-native model serving. 🔗 https://kserve.github.io/website/

<a id="t-kstreams"></a>
**Kafka Streams** — *(OS)* — Java stream processing library on Kafka. 🔗 https://kafka.apache.org/documentation/streams/

<a id="t-ksqldb"></a>
**ksqlDB** — *(OS, C)* — SQL stream processing on Kafka (Confluent). 🔗 https://docs.ksqldb.io/

<a id="t-kubeflow"></a>
**Kubeflow** — *(OS)* — Kubernetes-native ML workflows. 🔗 https://www.kubeflow.org/docs/

<a id="t-kyligence"></a>
**Kyligence (Apache Kylin)** — *(OS, E, C)* — OLAP/semantic layer with cube acceleration. 🔗 https://docs.kyligence.io/

## L

<a id="t-lakefs"></a>
**lakeFS** — *(OS, C)* — Git-like data versioning for object storage. 🔗 https://docs.lakefs.io/

<a id="t-lakekeeper"></a>
**Lakekeeper** — *(OS)* — Rust-based open-source Iceberg REST Catalog implementation. 🔗 https://docs.lakekeeper.io/

<a id="t-lakeformation"></a>
**AWS Lake Formation** — *(C)* — fine-grained access control on S3 lakes. 🔗 https://docs.aws.amazon.com/lake-formation/

<a id="t-lambda"></a>
**AWS Lambda** — *(C)* — AWS serverless compute. 🔗 https://docs.aws.amazon.com/lambda/

<a id="t-langchain"></a>
**LangChain** — *(OS)* — LLM application framework. 🔗 https://python.langchain.com/docs/

<a id="t-langfuse"></a>
**Langfuse** — *(OS, C)* — LLM observability and evaluation. 🔗 https://langfuse.com/docs

<a id="t-langsmith"></a>
**LangSmith** — *(C)* — LangChain's hosted LLMOps platform. 🔗 https://docs.smith.langchain.com/

<a id="t-lgbm"></a>
**LightGBM** — *(OS)* — Microsoft's gradient boosting framework. 🔗 https://lightgbm.readthedocs.io/

<a id="t-lightdash"></a>
**Lightdash** — *(OS, C)* — open-source BI on dbt. 🔗 https://docs.lightdash.com/

<a id="t-lightning"></a>
**PyTorch Lightning** — *(OS)* — high-level PyTorch training framework. 🔗 https://lightning.ai/docs/pytorch/stable/

<a id="t-lightup"></a>
**Lightup** — *(C)* — data quality and observability platform. 🔗 https://www.lightup.ai/

<a id="t-liquibase"></a>
**Liquibase** — *(OS, E)* — DB schema change management. 🔗 https://docs.liquibase.com/

<a id="t-llamaindex"></a>
**LlamaIndex** — *(OS)* — RAG/data framework for LLM applications. 🔗 https://docs.llamaindex.ai/

<a id="t-localstack"></a>
**LocalStack** — *(OS, E)* — local AWS cloud emulator for development. 🔗 https://docs.localstack.cloud/

<a id="t-locust"></a>
**Locust** — *(OS)* — Python-based load testing tool. 🔗 https://docs.locust.io/

<a id="t-logstash"></a>
**Logstash** — *(OS)* — Elastic-stack log/event processing. 🔗 https://www.elastic.co/guide/en/logstash/

<a id="t-loki"></a>
**Grafana Loki** — *(OS, C)* — log aggregation system inspired by Prometheus; AGPLv3. 🔗 https://grafana.com/docs/loki/

<a id="t-looker"></a>
**Looker / LookML** — *(C)* — Google's modeled BI platform with embeddable analytics. 🔗 https://cloud.google.com/looker/docs

<a id="t-lucid"></a>
**Lucidchart** — *(C)* — diagramming tool. 🔗 https://help.lucid.co/

<a id="t-luigi"></a>
**Luigi** — *(OS)* — Spotify's Python workflow engine (legacy). 🔗 https://luigi.readthedocs.io/

<a id="t-luzmo"></a>
**Luzmo** — *(C)* — embedded analytics platform (formerly Cumul.io). 🔗 https://docs.luzmo.com/

## M

<a id="t-macie"></a>
**AWS Macie** — *(C)* — sensitive data discovery on S3. 🔗 https://docs.aws.amazon.com/macie/

<a id="t-mage"></a>
**Mage** — *(OS, C)* — modern data orchestrator. 🔗 https://docs.mage.ai/

<a id="t-malloy"></a>
**Malloy** — *(OS)* — semantic data model and query language (Google). 🔗 https://docs.malloydata.dev/

<a id="t-manta"></a>
**Manta** — *(E)* — automated data lineage. 🔗 https://manta.io/

<a id="t-marquez"></a>
**Marquez** — *(OS)* — open-source metadata service (OpenLineage backend). 🔗 https://marquezproject.ai/docs/

<a id="t-matillion"></a>
**Matillion** — *(C)* — cloud-native ELT/orchestration platform. 🔗 https://docs.matillion.com/

<a id="t-matplotlib"></a>
**matplotlib** — *(OS)* — Python plotting library. 🔗 https://matplotlib.org/stable/

<a id="t-materialize"></a>
**Materialize** — *(C)* — streaming database; incremental view maintenance with Postgres wire protocol. **License note:** core was relicensed from BSL to source-available; cloud is the primary product. 🔗 https://materialize.com/docs/

<a id="t-mdclone"></a>
**MDClone** — *(C)* — synthetic data platform with healthcare focus. 🔗 https://www.mdclone.com/

<a id="t-meili"></a>
**Meilisearch** — *(OS, C)* — fast typo-tolerant search engine. 🔗 https://www.meilisearch.com/docs

<a id="t-memcached"></a>
**Memcached** — *(OS)* — in-memory key-value cache. 🔗 https://memcached.org/

<a id="t-memgraph"></a>
**Memgraph** — *(OS, C)* — in-memory graph database; Cypher-compatible. 🔗 https://memgraph.com/docs

<a id="t-metabase"></a>
**Metabase** — *(OS, C)* — open-source BI tool. 🔗 https://www.metabase.com/docs/

<a id="t-metaflow"></a>
**Metaflow** — *(OS)* — Netflix ML workflow framework. 🔗 https://docs.metaflow.org/

<a id="t-metricflow"></a>
**MetricFlow** — *(OS)* — semantic layer engine inside dbt. 🔗 https://docs.getdbt.com/docs/build/about-metricflow

<a id="t-microstrategy"></a>
**MicroStrategy ONE** — *(E, C)* — enterprise BI platform. 🔗 https://www.microstrategy.com/support

<a id="t-milvus"></a>
**Milvus** — *(OS)* — open-source vector database. 🔗 https://milvus.io/docs

<a id="t-mimir"></a>
**Grafana Mimir** — *(OS)* — horizontally scalable Prometheus-compatible metrics backend (AGPLv3). 🔗 https://grafana.com/docs/mimir/

<a id="t-minio"></a>
**MinIO** — *(OS, E)* — S3-compatible object storage. **License note:** core is AGPLv3. 🔗 https://min.io/docs/minio/linux/

<a id="t-mlflow"></a>
**MLflow** — *(OS)* — open-source MLOps platform with tracking, models, registry. 🔗 https://mlflow.org/docs/latest/

<a id="t-mode"></a>
**Mode** — *(C)* — collaborative analytics + BI (now ThoughtSpot). 🔗 https://mode.com/help/

<a id="t-modal"></a>
**Modal** — *(C)* — serverless GPU/CPU for Python (especially ML inference). 🔗 https://modal.com/docs

<a id="t-modin"></a>
**Modin** — *(OS)* — drop-in pandas accelerator. 🔗 https://modin.readthedocs.io/

<a id="t-mongo"></a>
**MongoDB** — *(SA, C)* — document NoSQL database (Atlas managed). **License note:** Community Server is SSPLv1 since 2018 — *not OSI-approved*; Atlas (cloud) is proprietary. 🔗 https://www.mongodb.com/docs/

<a id="t-montecarlo"></a>
**Monte Carlo** — *(C)* — data observability platform. 🔗 https://docs.getmontecarlo.com/

<a id="t-mostlyai"></a>
**Mostly AI** — *(C)* — synthetic data generation platform. 🔗 https://mostly.ai/docs/

<a id="t-mparticle"></a>
**mParticle** — *(C)* — enterprise customer data platform. 🔗 https://docs.mparticle.com/

<a id="t-mkdocs"></a>
**MkDocs** — *(OS)* — Markdown documentation generator. 🔗 https://www.mkdocs.org/

<a id="t-msk"></a>
**AWS MSK** — *(C)* — managed Apache Kafka on AWS. 🔗 https://docs.aws.amazon.com/msk/

<a id="t-mulesoft"></a>
**MuleSoft Anypoint Platform** — *(E, C)* — Salesforce iPaaS. 🔗 https://docs.mulesoft.com/

<a id="t-mwaa"></a>
**AWS MWAA** — *(C)* — Managed Workflows for Apache Airflow. 🔗 https://docs.aws.amazon.com/mwaa/

<a id="t-mysql"></a>
**MySQL** — *(OS)* — popular open-source relational database. 🔗 https://dev.mysql.com/doc/

## N

<a id="t-n8n"></a>
**n8n** — *(SA, C)* — workflow automation tool. **License note:** Sustainable Use License (fair-code, source-available, not OSI-approved); free for self-hosting non-commercial. 🔗 https://docs.n8n.io/

<a id="t-nats"></a>
**NATS** — *(OS)* — lightweight messaging system. 🔗 https://docs.nats.io/

<a id="t-neo4j"></a>
**Neo4j** — *(OS, E, C)* — leading graph database (Cypher). 🔗 https://neo4j.com/docs/

<a id="t-neptune"></a>
**Amazon Neptune** — *(C)* — managed graph database. 🔗 https://docs.aws.amazon.com/neptune/

<a id="t-neptune-ai"></a>
**Neptune.ai** — *(C)* — ML experiment tracking. 🔗 https://docs.neptune.ai/

<a id="t-nessie"></a>
**Project Nessie** — *(OS)* — Git-like versioning for Iceberg tables. 🔗 https://projectnessie.org/docs/

<a id="t-netezza"></a>
**IBM Netezza Performance Server** — *(E, C)* — IBM MPP appliance / cloud DB. 🔗 https://www.ibm.com/docs/en/netezza

<a id="t-newrelic"></a>
**New Relic** — *(C)* — full-stack observability. 🔗 https://docs.newrelic.com/

<a id="t-nextdata"></a>
**Nextdata OS** — *(C)* — data mesh platform from Zhamak Dehghani's company. 🔗 https://www.nextdata.com/

<a id="t-nfs"></a>
**NFS** — *(OS protocol)* — Network File System protocol. 🔗 https://datatracker.ietf.org/doc/html/rfc7530

<a id="t-nifi"></a>
**Apache NiFi** — *(OS)* — visual data flow tool. 🔗 https://nifi.apache.org/documentation/

<a id="t-nobl9"></a>
**Nobl9** — *(C)* — SLO management platform. 🔗 https://docs.nobl9.com/

## O

<a id="t-odcs"></a>
**Open Data Contract Standard (Bitol)** — *(OS spec)* — Linux Foundation data contract spec. 🔗 https://bitol-io.github.io/open-data-contract-standard/

<a id="t-okta"></a>
**Okta** — *(C)* — enterprise identity-as-a-service. 🔗 https://help.okta.com/

<a id="t-omni"></a>
**Omni** — *(C)* — modern BI platform with semantic + ad-hoc layers. 🔗 https://docs.omni.co/

<a id="t-onehouse"></a>
**Onehouse** — *(C)* — managed data lakehouse on Hudi. 🔗 https://docs.onehouse.ai/

<a id="t-onetrust"></a>
**OneTrust** — *(C)* — privacy, consent, and compliance platform. 🔗 https://www.onetrust.com/

<a id="t-opa"></a>
**Open Policy Agent (OPA)** — *(OS)* — CNCF general-purpose policy engine; Rego policy language. The de-facto standard for policy-as-code. 🔗 https://www.openpolicyagent.org/docs/

<a id="t-openai"></a>
**OpenAI API** — *(C)* — managed LLM and embedding APIs. 🔗 https://platform.openai.com/docs

<a id="t-openlineage"></a>
**OpenLineage** — *(OS)* — open standard for metadata and lineage collection. 🔗 https://openlineage.io/docs/

<a id="t-openmetadata"></a>
**OpenMetadata** — *(OS)* — open-source data catalog/metadata platform. 🔗 https://docs.open-metadata.org/

<a id="t-opensearch"></a>
**OpenSearch** — *(OS, C)* — Elasticsearch fork (AWS-led community), Apache 2.0. 🔗 https://opensearch.org/docs/

<a id="t-opentofu"></a>
**OpenTofu** — *(OS)* — community-driven open-source fork of Terraform 1.5.7 under MPL 2.0; Linux Foundation project. Drop-in replacement, native state encryption, broad provider support. 🔗 https://opentofu.org/docs/

<a id="t-opsgenie"></a>
**Opsgenie** — *(C)* — Atlassian on-call/alerting. 🔗 https://support.atlassian.com/opsgenie/

<a id="t-oracle"></a>
**Oracle Database** — *(E, C)* — flagship enterprise RDBMS. 🔗 https://docs.oracle.com/en/database/

<a id="t-orc"></a>
**Apache ORC** — *(OS)* — columnar file format. 🔗 https://orc.apache.org/docs/

<a id="t-oso"></a>
**OSO** — *(OS, C)* — authorization library and cloud service; Polar policy language. 🔗 https://www.osohq.com/docs

<a id="t-otel"></a>
**OpenTelemetry (OTel)** — *(OS)* — CNCF telemetry collection standard (logs/metrics/traces); becoming the universal observability instrumentation layer. 🔗 https://opentelemetry.io/docs/

<a id="t-observable"></a>
**Observable** — *(OS, C)* — JavaScript notebook + Framework + Plot library. 🔗 https://observablehq.com/

## P

<a id="t-1pass"></a>
**1Password Secrets Automation** — *(C)* — programmatic secrets vault. 🔗 https://developer.1password.com/

<a id="t-pachyderm"></a>
**Pachyderm** — *(OS, E)* — data versioning + pipeline platform. 🔗 https://docs.pachyderm.com/

<a id="t-pact"></a>
**Pact** — *(OS)* — consumer-driven contract testing. 🔗 https://docs.pact.io/

<a id="t-pagerduty"></a>
**PagerDuty** — *(C)* — incident response and on-call. 🔗 https://support.pagerduty.com/

<a id="t-pandas"></a>
**pandas** — *(OS)* — Python DataFrame library. 🔗 https://pandas.pydata.org/docs/

<a id="t-panel"></a>
**Panel (HoloViz)** — *(OS)* — Python data app framework. 🔗 https://panel.holoviz.org/

<a id="t-papermill"></a>
**Papermill** — *(OS)* — parameterize and execute Jupyter notebooks programmatically (Netflix). 🔗 https://papermill.readthedocs.io/

<a id="t-parquet"></a>
**Apache Parquet** — *(OS)* — columnar file format. 🔗 https://parquet.apache.org/docs/

<a id="t-pdcc"></a>
**PayPal data-contract-cli** — *(OS)* — open-source CLI for data contracts. 🔗 https://github.com/datacontract/datacontract-cli

<a id="t-pentaho"></a>
**Pentaho** — *(E)* — data integration + BI suite (Hitachi Vantara). 🔗 https://docs.hitachivantara.com/r/en-us/pentaho/

<a id="t-permit"></a>
**Permit.io** — *(C, OS)* — authorization-as-a-service built on OPA/Cedar. 🔗 https://docs.permit.io/

<a id="t-pgvector"></a>
**pgvector** — *(OS)* — vector similarity search extension for Postgres. 🔗 https://github.com/pgvector/pgvector

<a id="t-phoenix"></a>
**Arize Phoenix** — *(OS, C)* — open-source LLM/ML observability. 🔗 https://docs.arize.com/phoenix

<a id="t-pinecone"></a>
**Pinecone** — *(C)* — managed vector database. 🔗 https://docs.pinecone.io/

<a id="t-ping"></a>
**Ping Identity** — *(E, C)* — enterprise identity platform. 🔗 https://docs.pingidentity.com/

<a id="t-pinot"></a>
**Apache Pinot** — *(OS)* — real-time analytical OLAP database. 🔗 https://docs.pinot.apache.org/

<a id="t-ploomber"></a>
**Ploomber** — *(OS, C)* — pipelines from notebooks; promote `.ipynb` to scheduled production. 🔗 https://docs.ploomber.io/

<a id="t-plotly"></a>
**Plotly / Dash** — *(OS, C)* — Python visualization + data app framework. 🔗 https://plotly.com/python/ · https://dash.plotly.com/

<a id="t-polars"></a>
**Polars** — *(OS)* — Rust-based DataFrame library, fast columnar engine. 🔗 https://docs.pola.rs/

<a id="t-polaris"></a>
**Apache Polaris** — *(OS)* — Snowflake-donated open-source Iceberg REST Catalog (incubating in Apache). 🔗 https://polaris.apache.org/

<a id="t-polytomic"></a>
**Polytomic** — *(C)* — reverse ETL platform. 🔗 https://docs.polytomic.com/

<a id="t-postgis"></a>
**PostGIS** — *(OS)* — open-source geospatial extension for PostgreSQL. 🔗 https://postgis.net/documentation/

<a id="t-postgraphile"></a>
**PostGraphile** — *(OS)* — auto-generated GraphQL from Postgres. 🔗 https://www.graphile.org/postgraphile/

<a id="t-postgres"></a>
**PostgreSQL** — *(OS)* — full-featured open-source relational DB. 🔗 https://www.postgresql.org/docs/

<a id="t-postgrest"></a>
**PostgREST** — *(OS)* — auto REST API from PostgreSQL. 🔗 https://docs.postgrest.org/

<a id="t-powerautomate"></a>
**Microsoft Power Automate** — *(C)* — Microsoft workflow automation. 🔗 https://learn.microsoft.com/power-automate/

<a id="t-powerbi"></a>
**Microsoft Power BI** — *(C, E)* — Microsoft BI platform with semantic model and paginated reports. 🔗 https://learn.microsoft.com/power-bi/

<a id="t-presidio"></a>
**Microsoft Presidio** — *(OS)* — PII detection and de-identification framework. 🔗 https://microsoft.github.io/presidio/

<a id="t-presto"></a>
**Presto** — *(OS)* — distributed SQL query engine (the original; see also Trino). 🔗 https://prestodb.io/docs/

<a id="t-prefect"></a>
**Prefect** — *(OS, C)* — Python-based workflow orchestration. 🔗 https://docs.prefect.io/

<a id="t-privacera"></a>
**Privacera** — *(E, C)* — data access governance and security. 🔗 https://docs.privacera.com/

<a id="t-profisee"></a>
**Profisee** — *(E)* — enterprise master data management. 🔗 https://profisee.com/

<a id="t-prometheus"></a>
**Prometheus** — *(OS)* — open-source metrics monitoring and time-series DB. 🔗 https://prometheus.io/docs/

<a id="t-promptlayer"></a>
**PromptLayer** — *(C)* — prompt management and analytics for LLMs. 🔗 https://docs.promptlayer.com/

<a id="t-protegrity"></a>
**Protegrity** — *(E)* — enterprise data tokenization and protection. 🔗 https://www.protegrity.com/

<a id="t-protobuf"></a>
**Protocol Buffers** — *(OS)* — Google's compact binary serialization format. 🔗 https://protobuf.dev/

<a id="t-proton"></a>
**Proton (Timeplus)** — *(OS, C)* — streaming SQL database; ClickHouse-based with native streaming. 🔗 https://docs.timeplus.com/proton

<a id="t-prql"></a>
**PRQL** — *(OS)* — Pipelined Relational Query Language; modern alternative to SQL syntax with stronger composability. 🔗 https://prql-lang.org/

<a id="t-pubsub"></a>
**Google Cloud Pub/Sub** — *(C)* — GCP managed messaging. 🔗 https://cloud.google.com/pubsub/docs

<a id="t-pulsar"></a>
**Apache Pulsar** — *(OS)* — distributed messaging and streaming platform. 🔗 https://pulsar.apache.org/docs/

<a id="t-pulumi"></a>
**Pulumi** — *(OS, C)* — IaC using general-purpose languages (TypeScript/Python/Go/.NET). 🔗 https://www.pulumi.com/docs/

<a id="t-puppet"></a>
**Puppet** — *(OS, E)* — declarative configuration management (Perforce). 🔗 https://www.puppet.com/docs/

<a id="t-purview"></a>
**Microsoft Purview** — *(C)* — data governance, catalog, lineage, classification. 🔗 https://learn.microsoft.com/purview/

<a id="t-pytest"></a>
**pytest** — *(OS)* — Python testing framework. 🔗 https://docs.pytest.org/

<a id="t-pytorch"></a>
**PyTorch** — *(OS)* — deep learning framework (Meta). 🔗 https://pytorch.org/docs/

## Q

<a id="t-qdrant"></a>
**Qdrant** — *(OS, C)* — vector database with filterable payloads. 🔗 https://qdrant.tech/documentation/

<a id="t-qlik"></a>
**Qlik Sense** — *(E, C)* — associative-engine BI platform. 🔗 https://help.qlik.com/

<a id="t-qlikreplicate"></a>
**Qlik Replicate** — *(E)* — log-based CDC and replication. 🔗 https://help.qlik.com/en-US/replicate/

<a id="t-questdb"></a>
**QuestDB** — *(OS, C)* — high-performance time-series database. 🔗 https://questdb.io/docs/

## R

<a id="t-rabbitmq"></a>
**RabbitMQ** — *(OS, C)* — message broker (AMQP, MQTT, STOMP). 🔗 https://www.rabbitmq.com/documentation.html

<a id="t-ragas"></a>
**Ragas** — *(OS)* — RAG/LLM evaluation framework. 🔗 https://docs.ragas.io/

<a id="t-ranger"></a>
**Apache Ranger** — *(OS)* — fine-grained access control for Hadoop ecosystem. 🔗 https://ranger.apache.org/

<a id="t-ray"></a>
**Ray** — *(OS)* — distributed computing framework with Train/Serve/Tune libraries. 🔗 https://docs.ray.io/

<a id="t-rds"></a>
**Amazon RDS / Aurora** — *(C)* — managed relational databases. 🔗 https://docs.aws.amazon.com/rds/

<a id="t-redash"></a>
**Redash** — *(OS)* — open-source BI/query tool. 🔗 https://redash.io/help/

<a id="t-redis"></a>
**Redis / Redis Stack / Redis Cloud** — *(OS, C)* — in-memory data store, caching, pub/sub. **License note:** since Redis 8 (May 2025), tri-licensed under AGPLv3 / RSALv2 / SSPLv1. The community-favored fork is **Valkey** (BSD-3, Linux Foundation), launched after Redis's controversial 2024 SSPL switch. 🔗 https://redis.io/docs/

<a id="t-redpanda"></a>
**Redpanda** — *(OS, C)* — Kafka-API compatible streaming platform in C++. 🔗 https://docs.redpanda.com/

<a id="t-redshift"></a>
**Amazon Redshift / Redshift Spectrum** — *(C)* — AWS data warehouse + query over S3. 🔗 https://docs.aws.amazon.com/redshift/

<a id="t-reltio"></a>
**Reltio** — *(C)* — cloud-native MDM. 🔗 https://docs.reltio.com/

<a id="t-replicate"></a>
**Replicate** — *(C)* — managed model inference (especially open models). 🔗 https://replicate.com/docs

<a id="t-restate"></a>
**Restate** — *(OS, C)* — durable execution runtime for transactional microservices; alternative to Temporal. 🔗 https://docs.restate.dev/

<a id="t-retool"></a>
**Retool** — *(C, E)* — low-code internal tool builder. 🔗 https://docs.retool.com/

<a id="t-reviewable"></a>
**Reviewable** — *(C)* — code review for GitHub. 🔗 https://docs.reviewable.io/

<a id="t-riak"></a>
**Riak KV** — *(OS)* — distributed key-value store. 🔗 https://docs.riak.com/

<a id="t-risingwave"></a>
**RisingWave** — *(OS, C)* — Postgres-compatible streaming database; Apache 2.0. Materialize alternative. 🔗 https://docs.risingwave.com/

<a id="t-rubrik"></a>
**Rubrik** — *(E, C)* — enterprise backup, DR, ransomware protection. 🔗 https://www.rubrik.com/

<a id="t-rudderstack"></a>
**RudderStack** — *(OS, C)* — open-source customer data platform; warehouse-first event collection and reverse ETL. 🔗 https://www.rudderstack.com/docs/

## S

<a id="t-s3"></a>
**Amazon S3** — *(C)* — AWS object storage with lifecycle, versioning, replication. 🔗 https://docs.aws.amazon.com/s3/

<a id="t-sagemaker"></a>
**Amazon SageMaker** — *(C)* — managed ML platform (training, endpoints, feature store). 🔗 https://docs.aws.amazon.com/sagemaker/

<a id="t-salt"></a>
**SaltStack / Salt Project** — *(OS, E)* — event-driven configuration management (VMware/Broadcom). 🔗 https://docs.saltproject.io/

<a id="t-sapmdg"></a>
**SAP Master Data Governance** — *(E)* — SAP MDM solution. 🔗 https://help.sap.com/docs/SAP_MASTER_DATA_GOVERNANCE

<a id="t-sas"></a>
**SAS Viya** — *(E, C)* — SAS analytics and BI platform. 🔗 https://documentation.sas.com/

<a id="t-satori"></a>
**Satori** — *(C)* — data security platform. 🔗 https://satoricyber.com/docs/

<a id="t-scylla"></a>
**ScyllaDB** — *(OS, C)* — Cassandra-compatible high-performance NoSQL DB in C++. 🔗 https://docs.scylladb.com/

<a id="t-sbert"></a>
**sentence-transformers** — *(OS)* — Python library for sentence/paragraph embeddings. 🔗 https://www.sbert.net/

<a id="t-seaborn"></a>
**Seaborn** — *(OS)* — Python statistical visualization library. 🔗 https://seaborn.pydata.org/

<a id="t-secoda"></a>
**Secoda** — *(C)* — modern data catalog with AI-driven search. 🔗 https://docs.secoda.co/

<a id="t-secretsmgr"></a>
**AWS Secrets Manager** — *(C)* — secrets storage with rotation. 🔗 https://docs.aws.amazon.com/secretsmanager/

<a id="t-securiti"></a>
**Securiti.ai** — *(C)* — privacy, governance, and security platform. 🔗 https://securiti.ai/

<a id="t-sdv"></a>
**SDV (Synthetic Data Vault)** — *(OS)* — Python ecosystem for synthesizing tabular, relational, and time-series data. 🔗 https://docs.sdv.dev/

<a id="t-sedona"></a>
**Apache Sedona** — *(OS)* — distributed geospatial computing on Spark/Flink/Snow. 🔗 https://sedona.apache.org/

<a id="t-segment"></a>
**Segment (Twilio)** — *(C)* — leading customer data platform; event collection + identity + activation. 🔗 https://segment.com/docs/

<a id="t-select"></a>
**SELECT** — *(C)* — Snowflake/BigQuery cost optimization. 🔗 https://select.dev/docs

<a id="t-selectstar"></a>
**Select Star** — *(C)* — automated data lineage and discovery platform. 🔗 https://docs.selectstar.com/

<a id="t-semarchy"></a>
**Semarchy xDM** — *(E, C)* — MDM and data hub. 🔗 https://www.semarchy.com/docs/

<a id="t-semantickernel"></a>
**Microsoft Semantic Kernel** — *(OS)* — LLM orchestration SDK. 🔗 https://learn.microsoft.com/semantic-kernel/

<a id="t-shiny"></a>
**Shiny** — *(OS, C)* — R/Python data app framework (Posit). 🔗 https://shiny.posit.co/

<a id="t-sigma"></a>
**Sigma Computing** — *(C)* — cloud spreadsheet-style BI with embedding. 🔗 https://help.sigmacomputing.com/

<a id="t-singlestore"></a>
**SingleStore (MemSQL)** — *(C)* — distributed HTAP database. 🔗 https://docs.singlestore.com/

<a id="t-skyflow"></a>
**Skyflow** — *(C)* — privacy/PII vault as a service. 🔗 https://docs.skyflow.com/

<a id="t-sklearn"></a>
**scikit-learn** — *(OS)* — Python classical ML library. 🔗 https://scikit-learn.org/stable/

<a id="t-slingshot"></a>
**Capital One Slingshot** — *(C)* — Snowflake cost optimization. 🔗 https://www.capitalone.com/software/slingshot/

<a id="t-snowflake"></a>
**Snowflake** — *(C)* — cloud data warehouse + sharing + AI features. 🔗 https://docs.snowflake.com/

<a id="t-soda"></a>
**Soda Cloud** — *(C)* — data quality monitoring platform. 🔗 https://docs.soda.io/

<a id="t-sodacore"></a>
**Soda Core** — *(OS)* — open-source data quality library (SodaCL). 🔗 https://docs.soda.io/soda-core/

<a id="t-solace"></a>
**Solace PubSub+** — *(E, C)* — event mesh / messaging platform spanning cloud and on-prem. 🔗 https://docs.solace.com/

<a id="t-solara"></a>
**Solara** — *(OS)* — Python web framework for data apps. 🔗 https://solara.dev/documentation

<a id="t-solr"></a>
**Apache Solr** — *(OS)* — Lucene-based search platform. 🔗 https://solr.apache.org/guide/

<a id="t-spark"></a>
**Apache Spark** — *(OS)* — distributed batch + streaming processing engine. 🔗 https://spark.apache.org/docs/latest/

<a id="t-sparx"></a>
**Sparx Enterprise Architect** — *(E)* — enterprise modeling tool supporting UML, BPMN, ArchiMate, SysML. 🔗 https://sparxsystems.com/

<a id="t-sphinx"></a>
**Sphinx** — *(OS)* — Python documentation generator. 🔗 https://www.sphinx-doc.org/

<a id="t-spicedb"></a>
**SpiceDB (Authzed)** — *(OS, C)* — Google Zanzibar-inspired authorization database; ReBAC permission system. 🔗 https://authzed.com/docs

<a id="t-spline"></a>
**Spline** — *(OS)* — Spark lineage tracking. 🔗 https://absaoss.github.io/spline/

<a id="t-stardog"></a>
**Stardog** — *(E, C)* — knowledge graph platform combining RDF + virtualization + SPARQL/GraphQL. 🔗 https://docs.stardog.com/

<a id="t-splunk"></a>
**Splunk** — *(E, C)* — log analytics, SIEM, observability. 🔗 https://docs.splunk.com/

<a id="t-splunkoc"></a>
**Splunk On-Call (VictorOps)** — *(C)* — incident management. 🔗 https://docs.splunk.com/Documentation/OnCall

<a id="t-sqlite"></a>
**SQLite** — *(OS)* — embedded SQL database. 🔗 https://www.sqlite.org/docs.html

<a id="t-sqldbm"></a>
**SqlDBM** — *(C)* — cloud-based data modeling tool. 🔗 https://docs.sqldbm.com/

<a id="t-sqlmesh"></a>
**SQLMesh** — *(OS)* — data transformation framework with virtual env, diff, CI built-in. 🔗 https://sqlmesh.com/docs/

<a id="t-sqlserver"></a>
**Microsoft SQL Server** — *(E, C)* — Microsoft enterprise RDBMS. 🔗 https://learn.microsoft.com/sql/

<a id="t-sqoop"></a>
**Apache Sqoop** — *(OS, retired)* — Hadoop ↔ RDBMS bulk transfer (legacy). 🔗 https://sqoop.apache.org/

<a id="t-sqs"></a>
**AWS SQS** — *(C)* — managed message queue. 🔗 https://docs.aws.amazon.com/sqs/

<a id="t-ssis"></a>
**SQL Server Integration Services** — *(E)* — Microsoft ETL platform. 🔗 https://learn.microsoft.com/sql/integration-services/

<a id="t-starburst"></a>
**Starburst** — *(C, E)* — enterprise Trino + data products platform. 🔗 https://docs.starburst.io/

<a id="t-starrocks"></a>
**StarRocks** — *(OS)* — high-performance MPP analytical database. 🔗 https://docs.starrocks.io/

<a id="t-stepfunctions"></a>
**AWS Step Functions** — *(C)* — serverless workflow orchestration. 🔗 https://docs.aws.amazon.com/step-functions/

<a id="t-stepzen"></a>
**StepZen (IBM)** — *(C)* — GraphQL API mesh. 🔗 https://stepzen.com/docs

<a id="t-stibo"></a>
**Stibo Systems STEP** — *(E)* — enterprise MDM platform. 🔗 https://www.stibosystems.com/

<a id="t-stitch"></a>
**Stitch (Talend)** — *(C)* — managed ELT connectors. 🔗 https://www.stitchdata.com/docs/

<a id="t-streamlit"></a>
**Streamlit** — *(OS, C)* — Python data app framework (Snowflake). 🔗 https://docs.streamlit.io/

<a id="t-striim"></a>
**Striim** — *(E, C)* — streaming integration and CDC platform. 🔗 https://www.striim.com/docs/

<a id="t-structurizr"></a>
**Structurizr** — *(OS, C)* — C4 model architecture-as-code tool by Simon Brown. 🔗 https://docs.structurizr.com/

<a id="t-sumo"></a>
**Sumo Logic** — *(C)* — cloud log analytics and SIEM. 🔗 https://help.sumologic.com/

<a id="t-superset"></a>
**Apache Superset** — *(OS)* — open-source BI tool. 🔗 https://superset.apache.org/docs/

<a id="t-sweetviz"></a>
**Sweetviz** — *(OS)* — Python library for high-density EDA visualizations and data profiling. 🔗 https://github.com/fbdesignpro/sweetviz

<a id="t-synapse"></a>
**Azure Synapse Analytics** — *(C)* — Microsoft analytics service (warehouse + Spark + serverless SQL). 🔗 https://learn.microsoft.com/azure/synapse-analytics/

<a id="t-synthesized"></a>
**Synthesized** — *(C)* — synthetic data and test data automation platform. 🔗 https://docs.synthesized.io/

## T

<a id="t-tableau"></a>
**Tableau (Server / Cloud)** — *(E, C)* — Salesforce visual BI platform. 🔗 https://help.tableau.com/

<a id="t-tableauprep"></a>
**Tableau Prep** — *(E)* — visual data preparation for Tableau. 🔗 https://help.tableau.com/current/prep/

<a id="t-talend"></a>
**Talend (Qlik)** — *(E, C)* — data integration and quality platform. 🔗 https://help.qlik.com/talend/

<a id="t-tamr"></a>
**Tamr** — *(C)* — ML-based MDM/data unification. 🔗 https://docs.tamr.com/

<a id="t-tealium"></a>
**Tealium** — *(C)* — enterprise customer data platform. 🔗 https://docs.tealium.com/

<a id="t-tecton"></a>
**Tecton** — *(C)* — managed feature store / real-time ML platform. 🔗 https://docs.tecton.ai/

<a id="t-tempo"></a>
**Grafana Tempo** — *(OS, C)* — high-volume distributed tracing backend; AGPLv3. 🔗 https://grafana.com/docs/tempo/

<a id="t-temporal"></a>
**Temporal** — *(OS, C)* — durable execution platform; workflow-as-code (Go/Java/Python/TS/.NET) with fault-tolerant state, retries, timers, signals. Temporal Cloud is the managed offering. 🔗 https://docs.temporal.io/

<a id="t-tensorboard"></a>
**TensorBoard** — *(OS)* — TF/PyTorch experiment visualizer. 🔗 https://www.tensorflow.org/tensorboard

<a id="t-tensorflow"></a>
**TensorFlow** — *(OS)* — Google's deep learning framework. 🔗 https://www.tensorflow.org/api_docs

<a id="t-teradata"></a>
**Teradata Vantage** — *(E, C)* — enterprise MPP analytical platform. 🔗 https://docs.teradata.com/

<a id="t-terraform"></a>
**HashiCorp Terraform** — *(SA, E, C)* — infrastructure-as-code tool. **License note (Aug 2023):** moved from MPL 2.0 to BSL 1.1, source-available, not OSI-approved. The community fork [OpenTofu](#t-opentofu) (MPL 2.0, Linux Foundation) preserves open-source IaC. Acquired by IBM. 🔗 https://developer.hashicorp.com/terraform/docs

<a id="t-testcontainers"></a>
**Testcontainers** — *(OS)* — programmatic Docker containers for testing. 🔗 https://testcontainers.com/

<a id="t-tfserving"></a>
**TensorFlow Serving** — *(OS)* — high-performance TF model server. 🔗 https://www.tensorflow.org/tfx/guide/serving

<a id="t-thanos"></a>
**Thanos** — *(OS)* — CNCF horizontally scalable Prometheus long-term storage and global query view. 🔗 https://thanos.io/

<a id="t-thoughtspot"></a>
**ThoughtSpot** — *(C)* — search-based + AI-driven BI. 🔗 https://docs.thoughtspot.com/

<a id="t-tibco"></a>
**TIBCO BusinessWorks (Cloud Software Group)** — *(E)* — enterprise integration platform. 🔗 https://docs.tibco.com/

<a id="t-tidb"></a>
**TiDB** — *(OS, C)* — MySQL-compatible distributed HTAP database. 🔗 https://docs.pingcap.com/tidb/

<a id="t-tigergraph"></a>
**TigerGraph** — *(E, C)* — enterprise graph database. 🔗 https://docs.tigergraph.com/

<a id="t-timescale"></a>
**TimescaleDB / Timescale Cloud** — *(OS, C)* — Postgres extension for time-series. **License note:** TimescaleDB community is Apache 2.0; some advanced features are TSL (Timescale License, source-available). 🔗 https://docs.timescale.com/

<a id="t-tinybird"></a>
**Tinybird** — *(C)* — managed real-time analytics on ClickHouse with HTTP APIs. 🔗 https://www.tinybird.co/docs

<a id="t-togaf"></a>
**TOGAF (The Open Group)** — *(framework)* — enterprise architecture framework. 🔗 https://www.opengroup.org/togaf

<a id="t-tonic"></a>
**Tonic.ai** — *(C)* — synthetic data generation and test data management. 🔗 https://docs.tonic.ai/

<a id="t-tooljet"></a>
**ToolJet** — *(OS, C)* — open-source low-code internal tools. 🔗 https://docs.tooljet.com/

<a id="t-topaz"></a>
**Topaz (Aserto)** — *(OS)* — open-source authorization with OPA + ReBAC built on top of Edge directory. 🔗 https://www.topaz.sh/docs

<a id="t-torchserve"></a>
**TorchServe** — *(OS)* — PyTorch model serving. 🔗 https://pytorch.org/serve/

<a id="t-transcend"></a>
**Transcend** — *(C)* — privacy automation, DSAR, consent. 🔗 https://docs.transcend.io/

<a id="t-triton"></a>
**NVIDIA Triton Inference Server** — *(OS)* — multi-framework model server. 🔗 https://docs.nvidia.com/deeplearning/triton-inference-server/

<a id="t-trino"></a>
**Trino** — *(OS)* — distributed SQL query engine (fork of PrestoSQL). 🔗 https://trino.io/docs/

<a id="t-trulens"></a>
**TruLens** — *(OS)* — LLM/RAG evaluation framework. 🔗 https://www.trulens.org/

<a id="t-trustarc"></a>
**TrustArc** — *(C)* — privacy and consent management. 🔗 https://trustarc.com/

<a id="t-tyk"></a>
**Tyk** — *(OS, C)* — open-source API gateway. 🔗 https://tyk.io/docs/

<a id="t-typesense"></a>
**Typesense** — *(OS, C)* — typo-tolerant search engine. 🔗 https://typesense.org/docs/

## U

<a id="t-unitycatalog"></a>
**Unity Catalog** — *(OS, C)* — open-source data and AI catalog donated by Databricks to the LF; supports Iceberg REST and Delta. Both managed (Databricks) and OSS server. 🔗 https://docs.unitycatalog.io/

## V

<a id="t-valkey"></a>
**Valkey** — *(OS)* — Linux Foundation BSD-3 fork of Redis (created in March 2024 after Redis's SSPL switch); backed by AWS, Google Cloud, Oracle, Ericsson. Drop-in Redis replacement. 🔗 https://valkey.io/topics/

<a id="t-vanta"></a>
**Vanta** — *(C)* — continuous compliance automation (SOC 2, ISO 27001, etc.). 🔗 https://www.vanta.com/

<a id="t-vantage"></a>
**Vantage** — *(C)* — multi-cloud cost management. 🔗 https://docs.vantage.sh/

<a id="t-vault"></a>
**HashiCorp Vault** — *(SA, E, C)* — secrets management and encryption-as-a-service. **License note (Aug 2023):** moved from MPL 2.0 to BSL 1.1, source-available, not OSI-approved. **OpenBao** is the LF community fork that preserves MPL 2.0 (https://openbao.org/). 🔗 https://developer.hashicorp.com/vault/docs

<a id="t-vaultspeed"></a>
**VaultSpeed** — *(C)* — Data Vault automation. 🔗 https://docs.vaultspeed.com/

<a id="t-vector"></a>
**Vector (Datadog)** — *(OS)* — high-performance observability data pipeline. 🔗 https://vector.dev/docs/

<a id="t-veeam"></a>
**Veeam** — *(E, C)* — enterprise backup and replication. 🔗 https://www.veeam.com/documentation-guides-datasheets.html

<a id="t-vega"></a>
**Vega / Vega-Lite** — *(OS)* — declarative visualization grammar. 🔗 https://vega.github.io/vega/docs/ · https://vega.github.io/vega-lite/docs/

<a id="t-vermeg"></a>
**Vermeg AGILE / COLLINE** — *(E)* — regulatory reporting platforms (banking/funds). 🔗 https://www.vermeg.com/

<a id="t-veritas"></a>
**Veritas NetBackup / InfoScale** — *(E)* — enterprise backup, DR, ILM. 🔗 https://www.veritas.com/support

<a id="t-vertex"></a>
**Vertex AI** — *(C)* — GCP unified ML platform (training, prediction, feature store, search). 🔗 https://cloud.google.com/vertex-ai/docs

<a id="t-vertica"></a>
**Vertica** — *(E, C)* — columnar MPP analytical database (OpenText). 🔗 https://docs.vertica.com/

<a id="t-vespa"></a>
**Vespa** — *(OS, C)* — large-scale serving engine (search + vector + ranking). 🔗 https://docs.vespa.ai/

<a id="t-victoriametrics"></a>
**VictoriaMetrics** — *(OS, C)* — high-performance Prometheus-compatible time-series DB. 🔗 https://docs.victoriametrics.com/

<a id="t-virtuoso"></a>
**Virtuoso (OpenLink)** — *(OS, E, C)* — multi-model database engine; widely used as a SPARQL endpoint (DBpedia, LOD cloud). 🔗 https://docs.openlinksw.com/virtuoso/

<a id="t-vllm"></a>
**vLLM** — *(OS)* — high-throughput LLM inference engine. 🔗 https://docs.vllm.ai/

<a id="t-voyage"></a>
**Voyage AI (Anthropic)** — *(C)* — high-quality embedding APIs. 🔗 https://docs.voyageai.com/

<a id="t-vp"></a>
**Visual Paradigm** — *(E)* — UML / BPMN / ArchiMate / ERD modeling suite. 🔗 https://www.visual-paradigm.com/support/

<a id="t-vscode"></a>
**Visual Studio Code** — *(OS)* — Microsoft's open-source code editor. 🔗 https://code.visualstudio.com/docs

## W

<a id="t-wandb"></a>
**Weights & Biases** — *(C)* — ML experiment tracking, model registry, evaluation. 🔗 https://docs.wandb.ai/

<a id="t-wasabi"></a>
**Wasabi Hot Cloud Storage** — *(C)* — low-cost S3-compatible cloud storage. 🔗 https://docs.wasabi.com/

<a id="t-weaviate"></a>
**Weaviate** — *(OS, C)* — vector database with built-in modules. 🔗 https://weaviate.io/developers/weaviate

<a id="t-wherescape"></a>
**WhereScape** — *(E)* — data automation (3NF, Kimball, Data Vault). 🔗 https://www.wherescape.com/

<a id="t-whylogs"></a>
**whylogs** — *(OS)* — open-source data and ML logging library for profiling and drift detection (WhyLabs). 🔗 https://docs.whylabs.ai/docs/whylogs/

<a id="t-wk"></a>
**Wolters Kluwer OneSumX** — *(E)* — finance, risk, regulatory reporting. 🔗 https://www.wolterskluwer.com/en/solutions/onesumx-for-finance-risk-and-regulatory-reporting

<a id="t-workato"></a>
**Workato** — *(C)* — iPaaS / workflow automation. 🔗 https://docs.workato.com/

<a id="t-workiva"></a>
**Workiva** — *(C)* — financial, regulatory, and ESG reporting platform. 🔗 https://success.workiva.com/

<a id="t-workstream"></a>
**Workstream.io** — *(C)* — AI-native data discovery and exploration. 🔗 https://www.workstream.io/

## X

<a id="t-xgboost"></a>
**XGBoost** — *(OS)* — scalable gradient boosting library. 🔗 https://xgboost.readthedocs.io/

## Y

<a id="t-ydata"></a>
**ydata-profiling** — *(OS)* — Python library for one-line exploratory data analysis reports (formerly pandas-profiling). 🔗 https://docs.profiling.ydata.ai/

## Z

<a id="t-zapier"></a>
**Zapier** — *(C)* — SaaS workflow automation (light iPaaS). 🔗 https://help.zapier.com/

<a id="t-zeebe"></a>
**Zeebe** — *(SA, OS)* — Camunda's distributed BPMN workflow engine for cloud-native microservice orchestration. **License note:** Camunda License v1.0, source-available; community edition has restrictions. 🔗 https://docs.camunda.io/docs/components/zeebe/zeebe-overview/

<a id="t-zenml"></a>
**ZenML** — *(OS)* — open MLOps framework. 🔗 https://docs.zenml.io/

<a id="t-zeppelin"></a>
**Apache Zeppelin** — *(OS)* — web-based notebook (Spark/JDBC/Python/etc.). 🔗 https://zeppelin.apache.org/docs/

<a id="t-zerto"></a>
**Zerto (HPE)** — *(E, C)* — enterprise disaster recovery. 🔗 https://www.zerto.com/

---

**End of guide.**
