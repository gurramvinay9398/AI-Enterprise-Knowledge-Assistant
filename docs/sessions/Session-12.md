# Session 12 – Vector Databases & Similarity Search

## Duration

30 Minutes

## Objective

Understand **vector databases, similarity search, metadata**, and how they fit into our RAG architecture.

---

# Task 1 – What is a Vector Database?

A **vector database** is designed to store and efficiently search **vector embeddings**.

We learned earlier:

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

Example:

```text
"Employees receive 12 casual leaves"
              ↓
[0.21, -0.45, 0.73, 0.18, ...]
```

A vector database can store:

```text
Vector
   +
Document Chunk
   +
Metadata
```

Example:

```text
Vector → [0.21, -0.45, ...]
Text → "Employees receive 12 casual leaves..."
Source → LeavePolicy.pdf
Page → 12
```

---

# Task 2 – Why Do We Need a Vector Database?

Our application needs to find information based on **meaning**, not only exact keywords.

User asks:

> "How much annual time off do I get?"

Document says:

> "Employees receive 12 casual leaves per year."

The wording is different, but the meaning is related.

The vector database helps compare the question's embedding with stored document embeddings and retrieve relevant content.

---

# Task 3 – SQL Database vs Vector Database

They have different purposes.

### SQL Database

Used for structured application information:

```text
Users
Documents
Messages
Conversations
Permissions
```

### Vector Database

Used for semantic retrieval:

```text
Document Embeddings
Document Chunks
Vector Metadata
```

**Important:** A vector database does not necessarily replace our SQL database. Our application may use both.

---

# Task 4 – Similarity Search

Similarity search finds vectors that are **closest or most related in meaning** to the user's question.

Example:

```text
Question:
"How many casual leaves can I take?"
          ↓
Question Embedding
          ↓
Similarity Search
          ↓
Leave Policy     → High similarity
Salary Policy    → Low similarity
WFH Policy       → Low similarity
          ↓
Relevant Chunk
```

One common similarity measurement is **Cosine Similarity**.

We don't need to memorize its formula yet.

---

# Task 5 – Metadata

Metadata provides information about where a chunk came from.

Examples:

```text
document_id
file_name
page_number
department
document_type
chunk_id
```

Example:

```text
Chunk:
"Employees receive 12 casual leaves..."

Metadata:
File: LeavePolicy.pdf
Page: 12
Department: HR
```

Metadata will help us provide **document references** and later implement access filtering.

---

# RAG Architecture So Far

### Document Ingestion

```text
Company Document
      ↓
Extract Text
      ↓
Chunking
      ↓
Embedding Model
      ↓
Vector Database
```

### User Query

```text
User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Relevant Chunks
      ↓
LLM
      ↓
Answer + Source
```

---

# Key Learning

The main concept is:

> **A vector database stores embeddings and allows us to efficiently retrieve document chunks that are semantically similar to a user's question.**

It works alongside our normal application database rather than necessarily replacing it.

---

# Session Outcome

✅ Understood vector databases.

✅ Understood similarity search.

✅ Learned about cosine similarity.

✅ Understood metadata.

✅ Compared SQL and vector databases.

✅ Connected vector databases to RAG.

### RAG Progress

```text
LLM                 ✅
Embeddings          ✅
Semantic Search     ✅
Document Chunking   ✅
Vector Database     ✅
RAG Pipeline        ⏳
Prompt Engineering  ⏳
RAG Evaluation      ⏳
Production AI       ⏳
```

**Next:** We will connect everything together and understand the **complete RAG pipeline** from document upload to the final AI answer.
