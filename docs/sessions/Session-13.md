# Session 13 – Complete RAG Pipeline

## Duration

30 Minutes

## Objective

Connect everything learned so far and understand the **complete RAG pipeline** from document upload to the final AI answer with a document reference.

---

# Task 1 – Document Ingestion Pipeline

When a company document is uploaded, it goes through:

```text
Company Document
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Chunking
      ↓
Embedding Model
      ↓
Vector Embeddings
      ↓
Vector Database
```

### Example

An administrator uploads:

`Employee_Leave_Policy.pdf`

The system:

1. Extracts text.
2. Cleans unnecessary content.
3. Divides the text into meaningful chunks.
4. Converts each chunk into an embedding.
5. Stores embeddings in the vector database.
6. Stores metadata such as document name and page number.

The document is now ready for retrieval.

---

# Task 2 – Query Processing Pipeline

Employee asks:

> **"How many casual leaves can I take?"**

The system performs:

```text
User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Vector Database
      ↓
Relevant Chunks
      ↓
Context
      ↓
LLM
      ↓
Generated Answer
      ↓
Source Reference
```

Suppose the retrieved chunk says:

> Employees are entitled to 12 casual leaves per year.

The LLM can generate:

> **According to the employee leave policy, you are entitled to 12 casual leaves per year.**

The application can show:

**Source:** `Employee_Leave_Policy.pdf — Page 12`

---

# Task 3 – Complete RAG Architecture

```text
             DOCUMENT INGESTION
                    ↓
             Company Documents
                    ↓
              Text Extraction
                    ↓
                 Chunking
                    ↓
                Embeddings
                    ↓
             Vector Database
                    ↑
                    │
                    │
              User Question
                    ↓
           Question Embedding
                    ↓
             Similarity Search
                    ↓
            Relevant Chunks
                    ↓
                 Context
                    ↓
                   LLM
                    ↓
            Generated Answer
                    ↓
           Document Reference
```

This is the **core RAG architecture** of our project.

---

# Important Concept – RAG Does Not Train the LLM

When a company uploads a new document, we **do not retrain the LLM**.

Instead:

```text
Company Document
      ↓
Embeddings
      ↓
Vector Database
      ↓
Retrieve Relevant Information
      ↓
Give Information to LLM
      ↓
Generate Answer
```

The retrieved information becomes **context** for the LLM.

Therefore:

> **RAG provides external knowledge to an LLM without retraining the LLM for every new document.**

---

# Role of Each Component

| Component       | Purpose                     |
| --------------- | --------------------------- |
| Document        | Contains company knowledge  |
| Text Extraction | Extracts usable text        |
| Chunking        | Divides large content       |
| Embedding Model | Converts text into vectors  |
| Vector Database | Stores and searches vectors |
| Retrieval       | Finds relevant information  |
| LLM             | Generates the answer        |
| Metadata        | Provides source information |
| Backend         | Connects system components  |
| Frontend        | Displays answers to users   |

---

# Key Learning

The most important concept from this session:

> **RAG combines retrieval with generation. It retrieves relevant enterprise information and provides it to the LLM so the LLM can generate a grounded answer.**

We also learned that **document ingestion** and **query processing** are two different pipelines.

---

# Session Outcome

✅ Connected LLM, embeddings, chunking, and vector databases.

✅ Understood document ingestion.

✅ Understood query processing.

✅ Understood the complete RAG pipeline.

✅ Learned why RAG doesn't require LLM retraining for every document.

✅ Added the initial RAG architecture to `docs/Architecture.md`.

### RAG Progress

```text
LLM                  ✅
Embeddings           ✅
Semantic Search      ✅
Document Chunking    ✅
Vector Database      ✅
Complete RAG         ✅
Prompt Engineering   ⏳
Retrieval Strategies ⏳
RAG Evaluation       ⏳
Security             ⏳
Implementation       ⏳
Production AI        ⏳
```

### One-Minute Project Explanation

> **Our application takes enterprise documents, extracts and chunks their content, converts the chunks into embeddings, and stores them in a vector database. When an employee asks a question, the system retrieves relevant document chunks and provides them as context to an LLM. The LLM generates a simple answer based on that context, while the application displays the source document reference.**

This explanation represents the **core AI architecture** of our project.
