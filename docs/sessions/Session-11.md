# Session 11 – Document Chunking

## Duration

30 Minutes

## Objective

Understand **document chunking**, why large enterprise documents need to be divided into smaller pieces, and how chunking fits into our RAG pipeline.

---

## Task 1 – What is Document Chunking?

Document chunking means **dividing a large document into smaller meaningful pieces called chunks**.

Example:

```text
Company Employee Handbook.pdf
          ↓
     Extract Text
          ↓
      Split Text
          ↓
 ┌────────┬────────┬────────┐
 Chunk 1  Chunk 2  Chunk 3  ...
```

A chunk can contain a few sentences, paragraphs, or a meaningful section.

---

# Task 2 – Why Do We Need Chunking?

Imagine a company has a **200-page employee handbook** containing:

* Leave policies
* Salary policies
* Attendance rules
* Work-from-home policies
* Benefits
* Code of conduct

If an employee asks:

> "How many casual leaves can I take?"

We don't want to send all 200 pages to the LLM.

Instead:

```text
Question
   ↓
Semantic Search
   ↓
Relevant Chunk
   ↓
Leave Policy Information
   ↓
LLM
   ↓
Answer
```

Chunking helps provide **focused and relevant information** to the LLM.

### Benefits

* Better retrieval
* More relevant context
* Lower processing requirements
* Faster responses
* Better use of LLM context
* Potentially better answer quality

---

# Task 3 – Chunk Size

**Chunk size** means how much content is placed into one chunk.

### Too Large

```text
Large Chunk
↓
Too much unnecessary information
↓
Less focused retrieval
```

### Too Small

```text
Small Chunk
↓
Important context may be separated
↓
Potentially weaker answers
```

Therefore, chunk size needs to be selected and tested based on the documents and retrieval quality.

---

# Task 4 – Chunk Overlap

**Chunk overlap** means repeating a small amount of content between neighboring chunks.

Example:

```text
Chunk 1:
Employees can take up to 12 casual leaves...

       ↓ overlapping content ↓

Chunk 2:
...12 casual leaves per year according to company policy.
```

Overlap helps preserve context when important information crosses a chunk boundary.

---

# RAG Document Pipeline

We now understand this part of the RAG system:

```text
Company Document
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Database
```

When a user asks a question:

```text
User Question
      ↓
Question Embedding
      ↓
Semantic Search
      ↓
Relevant Chunks
      ↓
LLM
      ↓
Answer + Reference
```

---

# Key Learning

The most important concept is:

> **Chunking divides large documents into smaller meaningful pieces so that the RAG system can efficiently retrieve relevant information.**

Good chunking should preserve enough context while avoiding unnecessary information.

---

# Session Outcome

✅ Understood document chunking.

✅ Learned why chunking is necessary.

✅ Learned chunk size.

✅ Learned chunk overlap.

✅ Understood the document-processing pipeline.

✅ Connected chunking with embeddings and RAG.

### RAG Learning Progress

```text
LLM                 ✅
Embeddings          ✅
Semantic Search     ✅
Document Chunking   ✅
Vector Database     ⏳
RAG Pipeline        ⏳
Prompt Engineering  ⏳
RAG Evaluation      ⏳
Production AI       ⏳
```

**Next:** Learn **Vector Databases**—how our document chunks and their embeddings are stored and efficiently searched for relevant information.
