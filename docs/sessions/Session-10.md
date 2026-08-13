# Session 10 – Embeddings and Semantic Search

## Duration

30 Minutes

## Objective

Understand **embeddings, vectors, semantic search**, and how they help our RAG system find relevant information from enterprise documents.

---

# Task 1 – Understanding Embeddings

An **embedding** converts text into a numerical representation called a **vector**.

Example:

```text
"How many casual leaves can I take?"
              ↓
       Embedding Model
              ↓
[0.21, -0.45, 0.73, 0.18, ...]
```

The actual numbers are not important to us. The important idea is:

**Text → Embedding Model → Vector**

Text with similar meanings generally produces vectors that are closer together in the embedding space.

---

# Task 2 – Why Embeddings Are Needed

Suppose a company document says:

> Employees are entitled to 12 casual leaves every year.

A user asks:

> How much annual time off am I allowed?

The exact words are different, but the **meaning is similar**.

Keyword search may struggle because it mainly looks for matching words.

Embeddings allow **semantic search**, which focuses more on the meaning of the text.

---

# Task 3 – Keyword Search vs Semantic Search

### Keyword Search

Searches primarily for matching words.

```text
"annual time off"
        ↓
Exact keyword matching
```

### Semantic Search

Searches based on meaning.

```text
"annual time off"
        ↓
Embedding
        ↓
Compare with document embeddings
        ↓
"12 casual leaves"
        ↓
Relevant result
```

Semantic search is therefore extremely useful for our RAG application.

---

# How Embeddings Fit into RAG

Our future document-processing pipeline will be:

```text
Company Document
      ↓
Extract Text
      ↓
Split into Chunks
      ↓
Create Embeddings
      ↓
Store Vectors
      ↓
Vector Database
```

When a user asks a question:

```text
User Question
      ↓
Question Embedding
      ↓
Search Similar Vectors
      ↓
Relevant Document Chunks
      ↓
LLM
      ↓
Answer + Reference
```

---

# Key Concepts

### Vector

An ordered collection of numbers.

Example:

```text
[0.12, -0.35, 0.78, 0.42]
```

### Embedding

A vector representation of text created by an embedding model.

### Semantic Search

Finding information based on **meaning and similarity**, rather than only exact keywords.

### Cosine Similarity

A mathematical method that can be used to measure the similarity between vectors. We will study its mathematics when we implement semantic search.

---

# Key Learning

The important idea from this session is:

> **Embeddings allow computers to represent and compare the meaning of text mathematically.**

This enables our RAG system to find relevant information even when the user's exact words don't appear in the source document.

---

# Session Outcome

✅ Understood embeddings.

✅ Understood vectors.

✅ Learned semantic search.

✅ Compared keyword and semantic search.

✅ Understood how embeddings fit into RAG.

✅ Understood the basic document-to-vector pipeline.

### RAG Learning Progress

```text
LLM                 ✅
Embeddings          ✅
Semantic Search     ✅
Document Chunking   ⏳
Vector Database     ⏳
RAG Pipeline        ⏳
Prompt Engineering  ⏳
RAG Evaluation      ⏳
Production AI       ⏳
```

**Next:** Learn **Document Chunking**—how large enterprise documents are divided into smaller meaningful pieces before creating embeddings and performing retrieval.
