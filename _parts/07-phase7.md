<a id="phase-7"></a>
## Phase 7: AI/ML & LLM Platforms for Fund Data (months 40–43, 74 h + 7 h Appendix A)

**Goal:** working-level command of the ML/LLM platform stack from the *data architect's* seat: the lifecycle (MLflow), feature serving, vector storage, RAG over fund documents, and — critically for regulated use — evaluation and tracing. Depth is deliberately T2/T3: you architect the platform ML teams run on; you don't compete with them on modeling.
**Entry prerequisites:** Phases 2–6 (lakehouse, orchestration, governance — ML platforms inherit all of it). No ML-theory prerequisite: this phase targets platform-architecture depth, not modeling depth — the entries stay at the intuition level, and each resource is self-contained.
**Exit criteria:** you can (1) design the MLOps lifecycle on your platform with registry, tracking, and promotion gates; (2) choose vector storage and defend hybrid search for RAG; (3) build and *evaluate* an LLM extraction pipeline over fund documents; (4) tell a CIO what LLMOps controls a regulated deployment needs (traces, evals, human gates) and show them running.
**Appendix A items scheduled here:** A.21 LLM agent patterns & prompt engineering, A.23 Model Context Protocol, A.24 LLM application security (7 h).

### T1/T2 topics

#### 6.4.1 MLOps platforms & the ML lifecycle (MLflow) — T2
- **Why:** the registry/tracking/promotion lifecycle is the governance pattern of ML — and the architect owns how it plugs into the data platform, lineage, and audit.
- **Learn:** ML system anatomy (Huyen's framing): data → features → training → registry → serving → monitoring, and where each touches *your* platform; MLflow: tracking (runs/params/metrics), model registry (stages/aliases, approvals), packaging; experiment tracking as audit trail (6.7.1 lives here); drift concepts (data/concept) and retraining triggers; model risk management vocabulary for finance (SR 11-7/ECB TRIM awareness — models need inventories and owners too).
- **Resource:** Chip Huyen, *Designing Machine Learning Systems* ch. 1–2, 7–9 (skim the deep-modeling middle) + MLflow docs (tracking + registry).
- **Tools:** FOSS: MLflow (↔ Azure ML registry, SageMaker, W&B) · Corp: Azure ML (evaluation level, next entry).
- **Do:** stand up MLflow on the platform; track a small fund-flow forecasting experiment (sklearn, a few runs); register the winner and define a written promotion gate (eval threshold + human approval) from Staging→Production.
- **Done when:** "which model version produced this number, trained on what data, approved by whom?" is answerable from the registry — the model-governance analogue of your lineage drill.
- Est. hours: 10

#### 6.4.2 Managed MLOps (Azure ML) — T2
- **Why:** Azure ML is what your employer likely already licenses; you must map open concepts onto it for build-vs-buy and audit conversations.
- **Learn:** workspaces, compute targets, environments; pipelines vs your Dagster (overlap and friction); model registry + endpoints; responsible-AI dashboard positioning; cost profile; where Azure ML adds value over OSS-on-AKS (managed endpoints, RBAC integration) and where it constrains.
- **Resource:** Azure ML documentation (concepts section).
- **Do:** map every Capstone-7 component to its Azure ML equivalent in a one-page table with a build-vs-buy verdict per row.
- **Done when:** you can brief a platform team on what changes (and what doesn't) if they adopt Azure ML.
- Est. hours: 4

#### 6.1.1 Feature stores (Feast) — T2
- **Why:** the online/offline consistency problem is the architecturally interesting part of ML serving — and feature stores are a frequent (often premature) vendor pitch you must evaluate.
- **Learn:** offline vs online stores; point-in-time-correct joins (the training-serving skew killer — your SCD2 instincts apply directly); feature definitions as code; materialization; when a feature store is overkill (batch-only scoring — most fund use cases!).
- **Resource:** Feast docs (concepts + point-in-time joins).
- **Tools:** FOSS: Feast on Postgres/Redis (↔ Databricks/Tecton/SageMaker feature stores).
- **Do:** define three fund features (30-day flow volatility, investor churn signal, NAV staleness) in Feast over your lakehouse; demonstrate a point-in-time-correct training set vs a naive (leaky) join.
- **Done when:** you can show concretely how the naive join leaks future data, and state when you'd veto a feature-store purchase.
- Est. hours: 5

#### 1.1.4 + 3.2.9 Vector data & vector storage — T2
- **Why:** embeddings are a new first-class data type in your storage portfolio; the "dedicated vector DB vs pgvector vs search-engine hybrid" decision is today's recurring architecture question.
- **Learn:** embeddings as learned features; ANN indexing (HNSW intuition, IVF; recall-latency-memory triangle); pgvector (indexes, filtering) vs dedicated stores (Qdrant/Milvus) vs hybrid engines (the convergence note from the taxonomy: keyword+vector reranked is the RAG default); metadata filtering at scale; vector data lifecycle (re-embedding on model change — a lineage problem!).
- **Resource:** pgvector README + Qdrant docs (concepts: indexing, filtering, hybrid).
- **Tools:** FOSS: pgvector + Qdrant (↔ Azure AI Search vectors, Pinecone) .
- **Do:** embed 1k fund-document chunks; benchmark pgvector vs Qdrant on filtered top-k (latency/recall vs exact); write the 10-line "when does Postgres suffice" verdict.
- **Done when:** you can defend "pgvector until proven otherwise" — or its rejection — with your own numbers.
- Est. hours: 7

#### 6.6.1 Embedding models — T2
- **Why:** embedding choice quietly determines retrieval quality, cost, and re-indexing burden — an architect decision dressed as a detail.
- **Learn:** sentence-transformers locally vs API embeddings (cost/latency/sovereignty — EU data residency applies to embeddings too!); dimensionality tradeoffs; domain fit for financial text; versioning embeddings (model change = full re-index = pipeline design issue); MTEB as a (gameable) benchmark.
- **Resource:** sentence-transformers docs (+ MTEB leaderboard, read skeptically).
- **Tools:** FOSS: sentence-transformers (↔ OpenAI/Cohere/Voyage embedding APIs, Azure OpenAI embeddings).
- **Do:** compare a local multilingual model vs one API model on 20 fund-domain retrieval queries (French/English mix — Luxembourg reality); tabulate quality/cost/residency.
- **Done when:** your pick comes with a stated re-embedding strategy and a data-residency position.
- Est. hours: 4

#### 6.6.2 RAG frameworks & architecture — T2
- **Why:** RAG is the dominant enterprise LLM pattern and a *data architecture* problem at heart: ingestion, chunking, indexing, retrieval, and freshness are your home turf.
- **Learn:** RAG anatomy: load → chunk (strategies and their failure modes on structured PDFs like KIDs) → embed → index → retrieve (hybrid + rerank) → generate with citations; LlamaIndex vs Haystack vs LangChain positioning (and framework-fatigue caution — thin frameworks, strong pipelines); structured extraction with schema-constrained output (the capstone pattern); document parsing reality (tables in PDFs are where RAG dies); freshness pipeline (document updates → re-index, via your orchestrator).
- **Resource:** LlamaIndex docs (RAG concepts + structured extraction). *Alternate:* *Building LLMs for Production* (RAG chapters).
- **Tools:** FOSS: LlamaIndex + Ollama for local models (↔ Azure OpenAI + AI Search, Bedrock KBs).
- **Do:** build retrieval over 30 public fund KIDs/prospectuses (PDF parsing, chunking experiments, hybrid retrieval with citations); measure retrieval hit-rate on 20 hand-written questions before any generation.
- **Done when:** you can show retrieval quality numbers (not vibes) and explain which chunking decision moved them most.
- Est. hours: 10

#### 6.6.3 Managed RAG platforms — T2
- **Why:** "just use Azure AI Search + OpenAI" is the default corp pitch; you need its real capability/cost envelope versus your open pipeline.
- **Learn:** Azure AI Search: hybrid + semantic ranker, integrated vectorization, security trimming (ACL-aware retrieval — the enterprise killer feature); pricing tiers; Bedrock KB / Vertex Search equivalents at a glance; what managed buys (ops, security integration) vs costs (lock-in, chunking opacity).
- **Resource:** Azure AI Search docs (vector + semantic ranking overview).
- **Do:** one-page eval: your open RAG stack vs Azure AI Search for the fund-document corpus, including the ACL-trimming requirement.
- **Done when:** you can name the one requirement (usually security trimming or ops) that flips the decision either way.
- Est. hours: 3

#### 6.8.1 LLM tracing & prompt management (Langfuse) — T2
- **Why:** regulated LLM use without traces is unauditable; prompt/version/trace capture is the LLMOps analogue of your lineage work.
- **Learn:** trace model (traces/spans/generations); prompt versioning & rollout; cost/latency telemetry per call; PII handling in traces (don't log what you masked elsewhere!); user feedback capture as eval input.
- **Resource:** Langfuse docs (tracing + prompt management).
- **Tools:** FOSS: Langfuse self-hosted (↔ LangSmith, Azure AI Foundry tracing).
- **Do:** instrument the RAG pipeline with Langfuse; version one prompt change and compare cost/quality across versions from the traces.
- **Done when:** "what exactly did the model see and answer for document X last Tuesday?" is a lookup, not a mystery.
- Est. hours: 4

#### 6.8.2 LLM evaluation (Ragas, golden sets) — T2
- **Why:** evaluation is the control that makes LLM extraction defensible in a regulated workflow — without it you have a demo, not a system.
- **Learn:** eval layers: retrieval metrics (precision/recall@k), generation metrics (faithfulness, answer relevancy — Ragas), and *task* metrics (field-level extraction accuracy vs golden set — the one that matters here); LLM-as-judge caveats (bias, drift, cost); building golden datasets (your BA skills, weaponized); eval-in-CI: regression gates for prompt/model changes; human-in-the-loop sampling design.
- **Resource:** Ragas docs (metrics + testset) + DeepEval docs (CI integration page).
- **Tools:** FOSS: Ragas/DeepEval + pytest (↔ Azure AI evaluation SDK, LangSmith evals).
- **Do:** hand-build a 50-field golden set from 10 KIDs (SRI, costs, ISIN…); wire field-accuracy + faithfulness evals into CI so a prompt change that drops accuracy below threshold fails the build.
- **Done when:** a deliberately degraded prompt is caught by CI before a human would have noticed — and you can explain each metric's blind spot.
- Est. hours: 6

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 3.2.8 | Search engines | Inverted-index/BM25 stores (Elasticsearch/OpenSearch); the keyword half of hybrid RAG | OpenSearch "intro to search" docs | 30 |
| 6.1.2 | Managed feature stores | Tecton/Databricks/SageMaker FS — buy-side of 6.1.1 | Tecton "what is a feature store" page | 20 |
| 6.2.1 | Training frameworks | PyTorch/sklearn/XGBoost — the ML team's tools; you read, not write | sklearn user-guide landing page | 25 |
| 6.2.2 | Distributed training | Multi-GPU/node training (DeepSpeed/Ray Train); HPC-adjacent, out of role | Ray Train overview | 15 |
| 6.2.3 | Managed training | Azure ML/SageMaker training jobs; covered conceptually in 6.4.2 | Azure ML training docs intro | 15 |
| 6.3.1 | OS model serving | KServe/BentoML/vLLM serving infra; platform-team territory | BentoML "what is model serving" | 20 |
| 6.3.2 | Managed inference endpoints | Pay-per-call hosted inference; procurement awareness | Azure ML endpoints overview | 15 |
| 6.7.1 | OS experiment tracking | MLflow tracking — already hands-on in 6.4.1 | covered there | 5 |
| 6.7.2 | Managed experiment tracking | W&B/Neptune collaboration features | W&B product page | 10 |

*T3 subtotal: 2.5 h*

### Capstone 7 — LLM extraction of fund documents (RAG + eval harness)

- **Goal:** a regulated-grade LLM document pipeline: public fund documents in, schema-valid structured data out, with retrieval metrics, field-accuracy evals, full traces, and human gates — feeding the governed lakehouse like any other source.
- **Stack (100% free):** Ollama with a local open-weights model (↔ Azure OpenAI), LlamaIndex (↔ Azure AI Foundry / Bedrock KBs), pgvector + Qdrant comparison (↔ Azure AI Search), sentence-transformers (↔ Azure OpenAI embeddings), Langfuse (↔ LangSmith), Ragas/DeepEval in CI (↔ Azure AI evals), MLflow registry for prompt+model versions, Dagster orchestrating ingest/re-index, outputs into Iceberg with Soda DQ checks + OpenLineage lineage (the Phase-6 control plane applies unchanged).
- **Build:** (1) corpus: 30+ public KIDs/prospectuses (EN/FR); (2) parsing + chunking tuned on tables; (3) hybrid retrieval with citations; (4) schema-constrained extraction into an EMT/EPT-shaped record (Pydantic-validated); (5) golden-set evals (field accuracy + faithfulness) gating CI; (6) Langfuse traces end-to-end, PII-safe; (7) low-confidence extractions routed to a human-review queue (simple Streamlit screen); (8) results land in silver with DQ checks; lineage shows document → field.
- **Architecture deliverables:** C4 update (AI subsystem); ADR-019 local vs API models (cost/quality/residency), ADR-020 vector-store choice (with your benchmark), ADR-021 human-in-the-loop design (confidence thresholds, sampling, accountability).
- **Acceptance criteria:** field-level accuracy ≥ target on the held-out golden set with the number stated honestly; every extracted value traces to a source span (citation) and a trace ID; a degraded prompt fails CI; sub-threshold extractions reach the review queue with full context; the whole run is reproducible offline (no paid APIs).
- Est. hours: 18

*Phase 7 total: 74 h (T1/T2 entries 53 h + T3 2.5 h + capstone 18 h ≈ 74) + Appendix A items A.21, A.23, A.24 (7 h) scheduled in this phase*
