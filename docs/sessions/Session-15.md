# Session 15 – Retrieval Strategies

## Duration

30 Minutes

## Objective

Understand how our RAG system decides **which document chunks should be retrieved and provided to the LLM**.

---

# Task 1 – Top-K Retrieval

Our company may have thousands of document chunks.

We don't send everything to the LLM.

Instead, we retrieve the **Top-K most relevant chunks**.

Example:

```text
User Question
      ↓
Similarity Search
      ↓
Top 5 Relevant Chunks
      ↓
LLM
```

If `K = 5`, the system retrieves five results.

Top-K helps:

* Reduce unnecessary context.
* Improve efficiency.
* Keep the prompt focused.

The correct K value should be determined through testing.

---

# Task 2 – Similarity Score

A similarity score indicates how closely a user's question relates to a document chunk.

Example:

```text
Leave Policy      → 0.91
Holiday Policy    → 0.84
Salary Policy     → 0.31
IT Policy         → 0.18
```

Higher similarity generally indicates stronger relevance.

### Similarity Threshold

A threshold can be used to reject results that aren't relevant enough.

```text
Threshold = 0.70

0.91 → Keep
0.84 → Keep
0.31 → Reject
0.18 → Reject
```

**Important:** We shouldn't blindly use `0.70`; the appropriate threshold depends on our embedding model, documents, and testing.

---

# Task 3 – Metadata Filtering

Metadata can contain:

```text
document_id
department
document_type
page_number
access_level
uploaded_by
```

Example:

```text
department = HR
document_type = policy
```

The system can filter documents before performing semantic retrieval.

```text
User
 ↓
Permission Check
 ↓
Metadata Filtering
 ↓
Semantic Search
 ↓
Relevant Chunks
```

Metadata filtering is especially important for **enterprise security**, because users should only retrieve information they are authorized to access.

---

# Task 4 – Hybrid Search

Semantic search understands **meaning**, while keyword search is useful for **exact terms**.

Example:

```text
HR-2026-17
EMP-1024
VPN-003
```

These identifiers may require exact matching.

### Hybrid Search

Combines:

```text
Keyword Search
       +
Semantic Search
       ↓
Combined Results
```

This allows our system to handle both meaning-based questions and exact terms.

---

# Task 5 – Reranking

Initial retrieval may return many potentially relevant chunks.

A **reranker** can examine the question and retrieved chunks more deeply and reorder them according to relevance.

```text
User Question
      ↓
Initial Retrieval
      ↓
Top Candidates
      ↓
Reranker
      ↓
Best Results
      ↓
LLM
```

Reranking can improve the quality of the context given to the LLM.

---

# Complete Retrieval Pipeline

Our retrieval architecture now looks like:

```text
User Question
      ↓
Authentication / Permission Check
      ↓
Metadata Filtering
      ↓
Keyword + Semantic Retrieval
      ↓
Top-K Candidates
      ↓
Reranking
      ↓
Relevance Check
      ↓
Context Construction
      ↓
LLM
      ↓
Answer + Source
```

---

# Key Principle

> **Garbage in → Garbage out.**

If retrieval gives incorrect information:

```text
Bad Retrieval
     ↓
Wrong Context
     ↓
LLM
     ↓
Bad Answer
```

Even a powerful LLM cannot reliably fix incorrect context.

Therefore:

> **Retrieval quality is one of the most important factors in RAG quality.**

---

# Key Learning

We learned:

* **Top-K** → How many candidate results to retrieve.
* **Similarity Score** → How closely content relates to the query.
* **Threshold** → Whether a result is relevant enough.
* **Metadata Filtering** → Restrict retrieval based on attributes and permissions.
* **Hybrid Search** → Keyword + semantic search.
* **Reranking** → Improve the ordering of retrieved results.

---

# Session Outcome

✅ Understood Top-K retrieval.

✅ Learned similarity scores and thresholds.

✅ Learned metadata filtering.

✅ Understood enterprise access control importance.

✅ Learned hybrid search.

✅ Learned reranking.

✅ Updated the conceptual retrieval architecture.

### RAG Progress

```text
LLM                    ✅
Embeddings             ✅
Semantic Search        ✅
Document Chunking      ✅
Vector Database        ✅
Complete RAG           ✅
Prompt Engineering     ✅
Context Construction   ✅
Retrieval Strategies   ✅
RAG Evaluation         ⏳
Security               ⏳
Technology Selection   ⏳
Implementation         ⏳
Production AI          ⏳
```

### Next: Session 16

**RAG Evaluation** — how we test whether our AI assistant is actually producing **accurate, relevant, grounded, and reliable answers** rather than simply appearing to work.
