<a id="phase-7"></a>
## Phase 7: AI/ML & LLM Platforms for Fund Data (months 40–43, 74 h + 7 h Appendix A)

*Phase 7 of 8 · months 40–43 · 81 h (74 h + 7 h Appendix A) · capstone: LLM extraction of fund documents.*  ← [Phase 6](#phase-6) · [Phase 8](#phase-8) →

**Goal:** working-level command of the ML/LLM platform stack from the *data architect's* seat: the lifecycle (MLflow), feature serving, vector storage, RAG over fund documents, and — critically for regulated use — evaluation and tracing. Depth is deliberately T2/T3: you architect the platform ML teams run on; you don't compete with them on modeling.
**Entry prerequisites:** Phases 2–6 (lakehouse, orchestration, governance — ML platforms inherit all of it). No ML-theory prerequisite: this phase targets platform-architecture depth, not modeling depth — the entries stay at the intuition level, and each resource is self-contained.
**Exit criteria:** you can (1) design the MLOps lifecycle on your platform with registry, tracking, and promotion gates; (2) choose vector storage and defend hybrid search for RAG; (3) build and *evaluate* an LLM extraction pipeline over fund documents; (4) tell a CIO what LLMOps controls a regulated deployment needs (traces, evals, human gates) and show them running.
**Appendix A items scheduled here:** A.21 LLM agent patterns & prompt engineering, A.23 Model Context Protocol, A.24 LLM application security (7 h).

### T1/T2 topics

#### 6.4.1 MLOps platforms & the ML lifecycle (MLflow) — T2
- **Why:** the registry/tracking/promotion lifecycle is the governance pattern of ML — and the architect owns how it plugs into the data platform, lineage, and audit. Without it, a fund platform ships model changes with no approval trail, and "which model version produced this NAV-impacting forecast?" becomes unanswerable — exactly the question a model-risk validator or CSSF inspector will ask first.
- **Learn:**
  - ML system anatomy — data → features → training → registry → serving → monitoring, and where each stage touches *your* lakehouse, orchestrator, and lineage graph *(DMLS ch. 1–2)*
  - experiment tracking — runs, params, metrics, and artifacts as the audit trail of model development (6.7.1 lives here) *(MLflow docs: Tracking)*
  - model registry & packaging — versions, stages/aliases, pyfunc flavors, and the approval workflow that makes promotion a governed event *(MLflow docs: Model Registry)*
  - drift — data drift vs concept drift, the monitoring signals that detect each, and what triggers retraining *(DMLS ch. 8)*
  - model risk management vocabulary for finance — SR 11-7 / ECB TRIM awareness: model inventory, owners, independent validation; ML models join the same inventory as pricing models *(SR 11-7 letter)*
- **Resources:**
  - **[Designing Machine Learning Systems (Chip Huyen)](https://huyenchip.com/books/) ch. 1–2, 7–9** — system anatomy, deployment, monitoring and drift; skim the deep-modeling middle (primary)
  - [MLflow docs: Tracking](https://mlflow.org/docs/latest/ml/tracking/) — runs, experiments, logging APIs; the hands-on half (reference)
  - [MLflow docs: Model Registry](https://mlflow.org/docs/latest/ml/model-registry/) — versions, aliases/stages, lineage and promotion workflow (reference)
  - [SR 11-7: Guidance on Model Risk Management](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107.htm) — the canonical model-risk vocabulary regulators borrow from (deepening)
- **Tools:**
  - FOSS (hands-on): [MLflow](https://mlflow.org/docs/latest/) — tracking server + registry self-hosted on your platform (↔ Azure ML registry, SageMaker, W&B)
  - Corp (evaluate): [Azure ML](https://learn.microsoft.com/en-us/azure/machine-learning/) — evaluated properly in the next entry (6.4.2)
- **Do:**
  1. Stand up MLflow on the platform (`uv run mlflow server` with a Postgres backend store and a local artifact root) and confirm the UI is reachable.
  2. Build a small fund-flow forecasting experiment — an sklearn regressor over monthly subscription/redemption flows — and track 4–6 runs with different params, logging metrics and the model artifact each time.
  3. Compare runs in the UI; register the winning model in the registry with a version and description of its training data window.
  4. Define a written promotion gate from Staging→Production: a metric threshold plus a named human approver; record the approval as registry tags/aliases so it is queryable.
  5. Drill: starting from the Production alias alone, walk back to the exact run, params, data window, and approver — time yourself.
- **Done when:**
  - [ ] Answer "which model version produced this number, trained on what data, approved by whom?" from the registry alone — the model-governance analogue of your lineage drill.
  - [ ] Sketch the six lifecycle stages from memory and name where each touches your lakehouse and orchestrator.
  - [ ] Explain to a risk officer how the MLflow registry maps onto an SR 11-7-style model inventory (model, owner, validation evidence).
- Est. hours: 10

#### 6.4.2 Managed MLOps (Azure ML) — T2
- **Why:** Azure ML is what your employer likely already licenses; you must map open concepts onto it for build-vs-buy and audit conversations. An architect who can't say where Azure ML overlaps with the Dagster+MLflow stack ends up running two orchestrators and two registries — double cost, split audit trail.
- **Learn:**
  - workspaces, compute targets, environments — the resource model, and how Entra RBAC and networking attach to each *(Azure ML docs: concepts)*
  - Azure ML pipelines vs your Dagster — where they overlap, where they fight, and who should orchestrate whom *(Azure ML docs: Build & train models)*
  - model registry + endpoints — online vs batch endpoints, deployments under an endpoint, safe rollout via traffic split *(Azure ML docs: Endpoints)*
  - responsible-AI dashboard positioning — what it offers a regulated buyer and what it doesn't prove *(Azure ML docs: concepts)*
  - cost profile — compute, managed endpoints, and what idles expensively when the team goes home *(Azure ML pricing)*
  - where managed adds value vs constrains — managed endpoints and RBAC integration vs OSS-on-AKS flexibility and portability *(Azure ML docs: Endpoints)*
- **Resources:**
  - **[Azure Machine Learning documentation](https://learn.microsoft.com/en-us/azure/machine-learning/)** — concepts section: workspaces, compute, pipelines, responsible AI (primary)
  - [Azure ML: Endpoints for inference](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints) — online/batch endpoints and deployment model (reference)
  - [Azure ML: Build & train models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-train-machine-learning-model) — training methods and pipelines, for the Dagster-overlap question (reference)
  - [Azure ML pricing](https://azure.microsoft.com/en-us/pricing/details/machine-learning/) — the cost rows of your build-vs-buy table (reference)
- **Do:**
  1. List every Capstone-7 component (tracking, registry, serving, orchestration, vector store, evals, tracing) down the left of a one-page table.
  2. Map each to its Azure ML (or adjacent Azure service) equivalent, reading the concepts and endpoints docs as you go.
  3. Add a build-vs-buy verdict per row with a one-line justification — cost, RBAC integration, lock-in, or ops burden.
  4. Note the two places Azure ML pipelines and Dagster would fight over orchestration, and state your boundary rule (e.g. Dagster owns data, Azure ML owns training jobs).
- **Done when:**
  - [ ] Brief a platform team on what changes (and what doesn't) if they adopt Azure ML.
  - [ ] Name where Azure ML adds value over OSS-on-AKS (managed endpoints, RBAC) and where it constrains.
  - [ ] State which components you would keep open-source even with an Azure ML licence, and defend each in one sentence.
- Est. hours: 4

#### 6.1.1 Feature stores (Feast) — T2
- **Why:** the online/offline consistency problem is the architecturally interesting part of ML serving — and feature stores are a frequent (often premature) vendor pitch you must evaluate. Get point-in-time correctness wrong and the churn model trains on data it could never have seen at scoring time; buy a feature store for a batch-only fund workload and you've added an online database nobody queries.
- **Learn:**
  - offline vs online stores — training reads months of history from the lakehouse, serving needs millisecond lookups by entity key *(Feast docs: concepts)*
  - point-in-time-correct joins — the training-serving skew killer; your SCD2 instincts apply directly *(Feast docs: Point-in-time joins)*
  - feature definitions as code — entities, feature views, TTLs in versioned Python, reviewable like dbt models *(Feast docs: concepts)*
  - materialization — pushing offline values into the online store on a schedule, and the freshness window that implies *(Feast docs: concepts)*
  - when a feature store is overkill — batch-only scoring (most fund use cases!) needs none of the online machinery *(Tecton/Databricks: What is a feature store)*
- **Resources:**
  - **[Feast documentation](https://docs.feast.dev/)** — concepts: entities, feature views, offline/online stores, materialization (primary)
  - [Feast docs: Point-in-time joins](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) — the exact mechanism you will demonstrate hands-on (reference)
  - [What is a feature store? (Tecton, now Databricks)](https://www.databricks.com/glossary/what-is-a-feature-store) — the vendor framing and components; useful for spotting the buy-side pitch (deepening)
- **Tools:**
  - FOSS (hands-on): [Feast](https://docs.feast.dev/) on [PostgreSQL](https://www.postgresql.org/docs/)/[Redis](https://redis.io/docs/) (↔ Databricks/Tecton/SageMaker feature stores)
  - Corp (evaluate): [Databricks Feature Store](https://docs.databricks.com/) / [SageMaker Feature Store](https://docs.aws.amazon.com/sagemaker/) — what the managed pitch adds: serving SLAs, lineage UI, monitoring
- **Do:**
  1. Define three fund features in Feast over your lakehouse — 30-day flow volatility, investor churn signal, NAV staleness — as entities + feature views with explicit TTLs, committed as code.
  2. Build a training set with `get_historical_features` for a list of (investor, event_timestamp) rows — the point-in-time-correct path.
  3. Build the same training set with a naive latest-value SQL join; diff the two outputs and isolate the rows where the naive join pulled future data past the event timestamp.
  4. Materialize to the online store and fetch the three features for one investor at serving time, noting the freshness lag.
  5. Write a short verdict note: which fund use cases justify an online store, and the conditions under which you'd veto a feature-store purchase.
- **Done when:**
  - [ ] Show concretely how the naive join leaks future data, and state when you'd veto a feature-store purchase.
  - [ ] Explain point-in-time correctness to a data engineer in SCD2 terms (effective-dated lookups, not latest-value).
  - [ ] Name the fund workloads where batch scoring makes the online store unnecessary, and the one that wouldn't.
- Est. hours: 5

#### 1.1.4 + 3.2.9 Vector data & vector storage — T2
- **Why:** embeddings are a new first-class data type in your storage portfolio; the "dedicated vector DB vs pgvector vs search-engine hybrid" decision is today's recurring architecture question. Decide it on vendor slides instead of your own recall/latency numbers and you either buy a cluster Postgres could have replaced, or strand the RAG workload on an index that can't filter by fund family at scale.
- **Learn:**
  - embeddings as learned features — a first-class data type with its own storage, indexing, and lifecycle demands *(Qdrant docs)*
  - ANN indexing — HNSW graph intuition vs IVF lists, and the recall–latency–memory triangle every index trades within *(Qdrant docs: Indexing)*
  - pgvector — HNSW/IVFFlat index types, distance operators, and combining vector search with ordinary WHERE filters *(pgvector README)*
  - dedicated stores vs Postgres vs hybrid engines — the convergence note from the taxonomy: keyword+vector reranked is the RAG default *(Qdrant docs)*
  - metadata filtering at scale — pre- vs post-filtering, and why filterable HNSW is the hard part vendors compete on *(Qdrant docs: Indexing)*
  - vector data lifecycle — re-embedding on model change is a lineage and pipeline problem, not a one-off script *(Qdrant docs)*
- **Resources:**
  - **[pgvector README](https://github.com/pgvector/pgvector)** — index types, distance ops, filtering, tuning; everything for the Postgres half (primary)
  - [Qdrant documentation](https://qdrant.tech/documentation/) — collections, payload filtering, hybrid queries; the dedicated-store half (reference)
  - [Qdrant docs: Indexing](https://qdrant.tech/documentation/concepts/indexing/) — HNSW parameters and filterable-index internals behind your benchmark (deepening)
- **Tools:**
  - FOSS (hands-on): [pgvector](https://github.com/pgvector/pgvector) + [Qdrant](https://qdrant.tech/documentation/) (↔ [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/) vectors, Pinecone)
  - Corp (evaluate): [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/vector-search-overview) — the managed convergence play, evaluated in 6.6.3
- **Do:**
  1. Embed 1k fund-document chunks with a sentence-transformers model (the 6.6.1/6.6.2 corpus or any public KIDs).
  2. Load the same vectors + metadata (fund family, language, doc type) into Postgres+pgvector and into Qdrant; build an HNSW index in each.
  3. Benchmark filtered top-k ("top-10 within fund family X"): measure latency and recall against an exact-scan baseline; vary one HNSW parameter (`ef_search` or `m`) and record how the recall–latency point moves.
  4. Write the 10-line "when does Postgres suffice" verdict, citing your own numbers and the filtering behaviour you observed.
- **Done when:**
  - [ ] Defend "pgvector until proven otherwise" — or its rejection — with your own numbers.
  - [ ] Explain the recall–latency–memory triangle and what HNSW's parameters trade against each other.
  - [ ] State why an embedding-model change forces a full re-embed and how your pipeline (and lineage) would handle it.
- Est. hours: 7

#### 6.6.1 Embedding models — T2
- **Why:** embedding choice quietly determines retrieval quality, cost, and re-indexing burden — an architect decision dressed as a detail. Pick an English-only API model for a Luxembourg corpus and the French KIDs silently retrieve garbage, while every model upgrade triggers an unbudgeted full re-index through a third-country API.
- **Learn:**
  - local sentence-transformers vs API embeddings — the cost/latency/sovereignty triangle; EU data residency applies to embeddings too! *(Azure OpenAI data privacy)*
  - dimensionality tradeoffs — vector width drives storage and ANN latency; bigger is not reliably better *(sentence-transformers docs)*
  - domain fit for financial text — multilingual reality (French/English) and finance vocabulary beat leaderboard rank *(sentence-transformers docs)*
  - versioning embeddings — model change = full re-index = a pipeline design issue; pin model name+version next to the vectors *(sentence-transformers docs)*
  - MTEB as a (gameable) benchmark — shortlist with it, decide with your own retrieval set *(MTEB leaderboard)*
- **Resources:**
  - **[Sentence-Transformers documentation](https://www.sbert.net/)** — usage, pretrained multilingual models, semantic-search examples (primary)
  - [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — model shortlisting; read skeptically (reference)
  - [Azure OpenAI: data, privacy, and security](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy) — what API embeddings mean for EU residency and data processing (deepening)
- **Tools:**
  - FOSS (hands-on): [sentence-transformers](https://www.sbert.net/) (↔ OpenAI/Cohere/Voyage embedding APIs, [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/) embeddings)
- **Do:**
  1. Shortlist one local multilingual model (from the sbert pretrained list, MTEB-informed) and one API embedding model; record dimensions, licence, and published price.
  2. Write 20 fund-domain retrieval queries in a French/English mix — Luxembourg reality (NAV, SRI, frais courants, ISIN lookups).
  3. Embed corpus and queries with the local model and measure hit-rate@k; for the API model, tabulate cost-per-million-tokens and residency/processing terms from its documentation.
  4. Tabulate quality/cost/residency side by side; pick a model and write the re-embedding strategy: trigger, batch re-index job, dual-write or cutover window.
- **Done when:**
  - [ ] Your pick comes with a stated re-embedding strategy and a data-residency position.
  - [ ] Explain why MTEB rank alone would have been a bad selection method for this corpus.
  - [ ] Show how the French queries changed (or would change) the model choice versus English-only evaluation.
- Est. hours: 4

#### 6.6.2 RAG frameworks & architecture — T2
- **Why:** RAG is the dominant enterprise LLM pattern and a *data architecture* problem at heart: ingestion, chunking, indexing, retrieval, and freshness are your home turf. Skip the retrieval-quality discipline and the system confidently cites the wrong fund's fee table — in a KID-extraction workflow that's a mis-sold product, not a typo.
- **Learn:**
  - RAG anatomy — load → chunk → embed → index → retrieve (hybrid + rerank) → generate with citations; each stage is a pipeline stage you already know how to govern *(LlamaIndex docs)*
  - chunking strategies and their failure modes — fixed-size vs structure-aware on structured PDFs like KIDs; tables are where naive chunking dies *(LlamaIndex docs)*
  - hybrid retrieval + reranking — BM25 and vectors fused, then reranked; the enterprise default, not an optimization *(Building AI for Production: RAG chapters)*
  - framework positioning — LlamaIndex vs Haystack vs LangChain, and the framework-fatigue caution: thin frameworks, strong pipelines *(Haystack docs)*
  - structured extraction — schema-constrained output (Pydantic-validated) as the capstone pattern *(LlamaIndex docs)*
  - document parsing reality — PDF tables and multi-column layouts; parser choice moves quality more than the LLM does *(Building AI for Production: RAG chapters)*
  - freshness pipeline — document updates → re-chunk → re-index, owned by your orchestrator like any other source *(LlamaIndex docs)*
- **Resources:**
  - **[LlamaIndex documentation](https://docs.llamaindex.ai/)** — RAG concepts, loading/chunking, retrievers, structured extraction (primary)
  - [Building AI for Production (*Building LLMs for Production*, 2nd ed.)](https://towardsai.net/book) — RAG chapters: chunking, hybrid retrieval, production hardening (alternate)
  - [Haystack documentation](https://docs.haystack.deepset.ai/) — a second, pipeline-first framework for the positioning comparison (reference)
- **Tools:**
  - FOSS (hands-on): [LlamaIndex](https://docs.llamaindex.ai/) + [Ollama](https://ollama.com/) for local models (↔ [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/) + [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/), Bedrock KBs)
- **Do:**
  1. Collect 30 public fund KIDs/prospectuses (EN/FR mix); parse with two different PDF parsers and compare how each handles the fee/SRI tables.
  2. Implement two chunking strategies — fixed-size with overlap vs structure-aware sections — and index both variants into your 1.1.4 vector store.
  3. Hand-write 20 questions with known answers (the seed of the 6.8.2 golden set); measure retrieval hit-rate@k per chunking strategy, before any generation.
  4. Add hybrid retrieval (BM25 + vector, fused) with source-span citations; remeasure hit-rate and record the delta.
  5. Write down which single decision (parser, chunking, hybrid) moved retrieval quality most, with numbers.
- **Done when:**
  - [ ] Show retrieval quality numbers (not vibes) and explain which chunking decision moved them most.
  - [ ] Defend why retrieval is measured before generation, to a colleague who wants to "just eval the answers".
  - [ ] Sketch the freshness pipeline (document update → re-chunk → re-index) as a Dagster job over your existing assets.
- Est. hours: 10

#### 6.6.3 Managed RAG platforms — T2
- **Why:** "just use Azure AI Search + OpenAI" is the default corp pitch; you need its real capability/cost envelope versus your open pipeline. Without that envelope you either pay the semantic-ranker meter for a corpus pgvector served fine, or reject the one managed feature (security trimming) your compliance team actually needed.
- **Learn:**
  - the Azure AI Search hybrid stack — vector + keyword in one query, RRF fusion, semantic ranker on top *(Azure AI Search docs: vector search)*
  - integrated vectorization — chunking and embedding inside the indexer pipeline: convenience bought with opacity *(Azure AI Search docs: vector search)*
  - security trimming — ACL-aware retrieval via identity filters; the enterprise killer feature for investor-restricted documents *(Azure AI Search docs: security trimming)*
  - semantic ranker mechanics and pricing — reranking the top-50 with Microsoft's models, billed by usage *(Azure AI Search docs: semantic ranking)*
  - Bedrock KBs / Vertex Search equivalents at a glance — the same managed trade on other clouds *(Amazon Bedrock docs)*
  - what managed buys vs costs — ops and security integration vs lock-in and chunking opacity *(Azure AI Search docs: vector search)*
- **Resources:**
  - **[Azure AI Search: vector search overview](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)** — hybrid scenarios, integrated vectorization, pricing notes (primary)
  - [Azure AI Search: semantic ranking overview](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview) — how the reranker works and what it's billed on (reference)
  - [Azure AI Search: security filter pattern](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search) — the ACL-trimming mechanism your eval must address (reference)
  - [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/) — Knowledge Bases as the AWS counterpart, glance level (deepening)
- **Do:**
  1. Read the three Azure AI Search pages and sketch the managed pipeline (indexer → skillset → index → semantic ranker) side by side with your open 6.6.2 pipeline.
  2. Write the one-page eval: open RAG stack vs Azure AI Search for the fund-document corpus — rows for capability, cost, ops burden, chunking control, lock-in.
  3. Treat the ACL-trimming requirement explicitly: how each side enforces "investor-restricted documents are never retrieved for the wrong user", and what your open stack would have to build.
  4. Conclude with the single requirement that flips the decision either way, stated in one sentence.
- **Done when:**
  - [ ] Name the one requirement (usually security trimming or ops) that flips the decision either way.
  - [ ] Explain what integrated vectorization hides and why that matters when retrieval quality degrades.
  - [ ] State the semantic ranker's pricing model and when it's worth turning on for this corpus.
- Est. hours: 3

#### 6.8.1 LLM tracing & prompt management (Langfuse) — T2
- **Why:** regulated LLM use without traces is unauditable; prompt/version/trace capture is the LLMOps analogue of your lineage work. Without it, "what exactly did the model see when it extracted this SRI value?" has no answer, and an untracked prompt edit can silently change extraction behaviour across the whole corpus.
- **Learn:**
  - the trace model — traces, spans, generations: every LLM call tied to its inputs, outputs, and pipeline context *(Langfuse docs: Tracing)*
  - prompt versioning & rollout — prompts as managed, versioned artifacts fetched at runtime, with labels for staged rollout and rollback *(Langfuse docs: Prompt Management)*
  - cost/latency telemetry — per-call token and cost capture, aggregated for chargeback and SLOs *(Langfuse docs: Tracing)*
  - PII handling in traces — don't log what you masked elsewhere!; masking hooks before persistence *(Langfuse docs: Tracing)*
  - user feedback capture — reviewer scores attached to traces become tomorrow's eval data for 6.8.2 *(Langfuse docs: Tracing)*
- **Resources:**
  - **[Langfuse documentation](https://langfuse.com/docs)** — tracing model, SDK instrumentation, scores/feedback, self-hosting (primary)
  - [Langfuse docs: Prompt Management](https://langfuse.com/docs/prompts) — versioning, labels, runtime fetching (reference)
- **Tools:**
  - FOSS (hands-on): [Langfuse](https://langfuse.com/docs) self-hosted (↔ [LangSmith](https://docs.smith.langchain.com/), [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/) tracing)
- **Do:**
  1. Self-host Langfuse (docker compose) next to the RAG pipeline and create a project + API keys.
  2. Instrument the 6.6.2 pipeline: one trace per question, spans for retrieval and generation, with model name, token counts, and cost metadata on each generation.
  3. Move the extraction prompt into Langfuse prompt management; create a v2 with a deliberate wording change and fetch it by label at runtime.
  4. Run the 20-question set under both prompt versions; compare cost and answer quality per version straight from the traces.
  5. Configure masking so investor names and other PII never reach the stored traces; verify by inspecting raw traces in the UI.
- **Done when:**
  - [ ] "What exactly did the model see and answer for document X last Tuesday?" is a lookup, not a mystery.
  - [ ] Show two prompt versions with a cost/quality comparison derived from traces, not from memory.
  - [ ] Demonstrate that masked fields appear nowhere in the trace store.
- Est. hours: 4

#### 6.8.2 LLM evaluation (Ragas, golden sets) — T2
- **Why:** evaluation is the control that makes LLM extraction defensible in a regulated workflow — without it you have a demo, not a system. No golden set and no CI gate means a prompt tweak can drop ISIN extraction accuracy for weeks before anyone notices, and the discovery will be made by a transfer agent, not by you.
- **Learn:**
  - eval layers — retrieval metrics (precision/recall@k), generation metrics (faithfulness, answer relevancy), and *task* metrics (field-level extraction accuracy vs golden set — the one that matters here) *(Ragas docs: metrics)*
  - LLM-as-judge caveats — bias, drift, cost; align the judge against human labels before trusting it *(Hamel Husain: evals)*
  - building golden datasets — your BA skills, weaponized: sampling, labeling discipline, synthetic testset generation as a bootstrap *(Ragas docs: testset generation)*
  - eval-in-CI — regression gates so a prompt or model change that degrades quality fails the build, like any other test *(DeepEval docs)*
  - human-in-the-loop sampling design — what humans review, at what rate, where the outcome is recorded *(Hamel Husain: evals)*
- **Resources:**
  - **[Ragas documentation](https://docs.ragas.io/en/stable/)** — metrics (faithfulness, relevancy, precision/recall) + testset generation (primary)
  - [DeepEval documentation](https://deepeval.com/docs/getting-started) — pytest-style LLM assertions and CI integration (reference)
  - [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) — the three-level eval system, LLM-as-judge discipline, human review loops (deepening)
- **Tools:**
  - FOSS (hands-on): [Ragas](https://docs.ragas.io/en/stable/)/[DeepEval](https://deepeval.com/docs/getting-started) + [pytest](https://docs.pytest.org/) (↔ [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/) evaluation SDK, [LangSmith](https://docs.smith.langchain.com/) evals)
- **Do:**
  1. Hand-build a 50-field golden set from 10 KIDs — SRI, ongoing costs, ISIN, currency, recommended holding period — stored as versioned YAML/CSV beside the code.
  2. Write a field-accuracy eval (exact or normalized match per field) over the extraction pipeline, plus a Ragas faithfulness eval over the generated answers.
  3. Wire both into CI with pytest/DeepEval and an explicit threshold, so a run below threshold fails the build.
  4. Deliberately degrade the prompt (drop one extraction instruction); confirm CI catches the regression and the failing fields are identifiable.
  5. Write one paragraph per metric on its blind spot — e.g. faithfulness can score high while the extracted field is still wrong.
- **Done when:**
  - [ ] A deliberately degraded prompt is caught by CI before a human would have noticed — and you can explain each metric's blind spot.
  - [ ] Defend field-level accuracy as the primary metric for this workload, over generic generation scores.
  - [ ] State your human-review sampling rate and what triggers escalation to full review.
- Est. hours: 6

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 3.2.8 | Search engines | Inverted-index/BM25 stores (Elasticsearch/OpenSearch); the keyword half of hybrid RAG and of log search | [OpenSearch docs: Intro to OpenSearch](https://docs.opensearch.org/latest/getting-started/intro/) | 30 |
| 6.1.2 | Managed feature stores | Tecton/Databricks/SageMaker FS — buy-side of 6.1.1 (Tecton now part of Databricks) | [Tecton: what is a feature store (now Databricks)](https://www.databricks.com/glossary/what-is-a-feature-store) | 20 |
| 6.2.1 | Training frameworks | PyTorch/sklearn/XGBoost — the ML team's tools; you read, not write | [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) | 25 |
| 6.2.2 | Distributed training | Multi-GPU/node training (DeepSpeed/Ray Train); HPC-adjacent, out of role | [Ray Train overview](https://docs.ray.io/en/latest/train/train.html) | 15 |
| 6.2.3 | Managed training | Azure ML/SageMaker training jobs; covered conceptually in 6.4.2 | [Azure ML: build & train models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-train-machine-learning-model) | 15 |
| 6.3.1 | OS model serving | KServe/BentoML/vLLM serving infra; platform-team territory | [BentoML docs (model serving)](https://docs.bentoml.com/) | 20 |
| 6.3.2 | Managed inference endpoints | Pay-per-call hosted inference; procurement awareness | [Azure ML: endpoints overview](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints) | 15 |
| 6.7.1 | OS experiment tracking | MLflow tracking — already hands-on in 6.4.1 | [MLflow Tracking (covered in 6.4.1)](https://mlflow.org/docs/latest/ml/tracking/) | 5 |
| 6.7.2 | Managed experiment tracking | W&B/Neptune collaboration features on top of tracking | [W&B product page](https://wandb.ai/site) | 10 |

*T3 subtotal: 2.5 h*

### Capstone 7 — LLM extraction of fund documents (RAG + eval harness)

- **Goal:** a regulated-grade LLM document pipeline: public fund documents in, schema-valid structured data out, with retrieval metrics, field-accuracy evals, full traces, and human gates — feeding the governed lakehouse like any other source.
- **Stack (100% free):** [Ollama](https://ollama.com/) with a local open-weights model (↔ [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)), [LlamaIndex](https://docs.llamaindex.ai/) (↔ [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/) / [Bedrock KBs](https://docs.aws.amazon.com/bedrock/)), [pgvector](https://github.com/pgvector/pgvector) + [Qdrant](https://qdrant.tech/documentation/) comparison (↔ [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/)), [sentence-transformers](https://www.sbert.net/) (↔ Azure OpenAI embeddings), [Langfuse](https://langfuse.com/docs) (↔ [LangSmith](https://docs.smith.langchain.com/)), [Ragas](https://docs.ragas.io/en/stable/)/[DeepEval](https://deepeval.com/docs/getting-started) in CI (↔ Azure AI evals), [MLflow](https://mlflow.org/docs/latest/) registry for prompt+model versions, [Dagster](https://docs.dagster.io/) orchestrating ingest/re-index, outputs into [Iceberg](https://iceberg.apache.org/) with [Soda](https://docs.soda.io/) DQ checks + [OpenLineage](https://openlineage.io/docs/) lineage (the Phase-6 control plane applies unchanged).
- **Build:** (1) corpus: 30+ public KIDs/prospectuses (EN/FR), versioned in object storage; (2) parsing + chunking tuned on tables, with the 6.6.2 parser comparison applied; (3) hybrid retrieval (BM25 + vector) with source-span citations; (4) schema-constrained extraction into an EMT/EPT-shaped record (Pydantic-validated, invalid records rejected not patched); (5) golden-set evals (field accuracy + faithfulness) gating CI per 6.8.2; (6) Langfuse traces end-to-end, PII-safe per 6.8.1; (7) low-confidence extractions routed to a human-review queue (simple [Streamlit](https://docs.streamlit.io/) screen showing field, source span, and confidence); (8) results land in silver with DQ checks; lineage shows document → field.
- **Architecture deliverables:** C4 update (AI subsystem); ADR-019 local vs API models (cost/quality/residency), ADR-020 vector-store choice (with your benchmark), ADR-021 human-in-the-loop design (confidence thresholds, sampling, accountability).
- **Acceptance criteria:** field-level accuracy ≥ target on the held-out golden set with the number stated honestly (no cherry-picked subset); every extracted value traces to a source span (citation) and a trace ID; a degraded prompt fails CI; sub-threshold extractions reach the review queue with full context (field, span, confidence, trace link); reviewer decisions are recorded and queryable; the whole run is reproducible offline (no paid APIs).
- Est. hours: 18

*Phase 7 total: 74 h (T1/T2 entries 53 h + T3 2.5 h + capstone 18 h ≈ 74) + Appendix A items A.21, A.23, A.24 (7 h) scheduled in this phase*
