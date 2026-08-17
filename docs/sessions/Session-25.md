# Session 25 – Backend Architecture & Project Structure

## Duration

30 Minutes

## Objective

Design a **professional backend structure** for our AI Enterprise Knowledge Assistant instead of putting all functionality into one `app.py`.

The main principle is:

> **Separate different responsibilities so the project is easier to understand, test, maintain, and scale.**

---

# Task 1 – Why Not One `app.py`?

A small application can put everything inside:

```text id="m3p9kx"
app.py
 ├── Login
 ├── Database
 ├── File Upload
 ├── RAG
 ├── LLM
 └── Chat
```

But as the project grows, this becomes:

* Difficult to understand.
* Difficult to test.
* Difficult to maintain.
* Difficult for multiple developers to work on.

Therefore, we use **Separation of Concerns**.

---

# Task 2 – Backend Structure

Our planned structure:

```text id="x9h3vd"
backend/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   ├── auth.py
│   │   ├── documents.py
│   │   ├── chat.py
│   │   └── conversations.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── document.py
│   │   ├── chat.py
│   │   └── conversation.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── document.py
│   │   ├── conversation.py
│   │   └── message.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── document_service.py
│   │   ├── chat_service.py
│   │   └── conversation_service.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   ├── document_repository.py
│   │   └── conversation_repository.py
│   │
│   ├── rag/
│   │   ├── ingestion.py
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── retrieval.py
│   │   ├── prompts.py
│   │   └── pipeline.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   │
│   └── utils/
│       └── helpers.py
│
├── tests/
├── requirements.txt
├── .env
└── README.md
```

This is our **planned architecture**, not yet the implementation.

---

# Task 3 – API Layer

The `api/` layer contains HTTP endpoints.

Example:

```text id="d7v2ca"
api/chat.py
      ↓
POST /api/chat
```

Its responsibility is mainly:

```text id="h4c6xn"
Request
 ↓
Validation
 ↓
Authentication
 ↓
Call Service
 ↓
Response
```

It shouldn't contain the entire RAG algorithm.

---

# Task 4 – Schema Layer

The `schemas/` layer defines the structure of incoming and outgoing data.

Examples:

```text id="8t1f4r"
LoginRequest
LoginResponse
ChatRequest
ChatResponse
DocumentRequest
```

It provides:

* Input validation.
* Output structure.
* Clear API contracts.

---

# Task 5 – Model Layer

The `models/` layer represents database entities.

Examples:

```text id="w5q3vn"
User
Role
Document
Conversation
Message
```

Conceptually:

```text id="j0x6kd"
Database Table
      ↕
Database Model
```

Example:

```text id="q1k4mw"
users table
     ↕
User model
```

---

# Task 6 – Service Layer

The `services/` layer contains **business logic**.

For example, `chat_service.py` may coordinate:

```text id="8g6h2s"
User Question
 ↓
Permission Check
 ↓
RAG Retrieval
 ↓
Prompt Construction
 ↓
LLM
 ↓
Save Response
```

Therefore:

```text id="x7v5zq"
API
 ↓
Chat Service
 ↓
RAG + Database + LLM
```

This keeps the API layer clean.

---

# Task 7 – Repository Layer

The `repositories/` layer handles database operations.

Examples:

```text id="9d8f2a"
find_user_by_email()
get_user_by_id()
create_user()
```

Architecture:

```text id="p4x8r6"
Service
   ↓
Repository
   ↓
Database
```

This separates business logic from database access.

---

# Task 8 – RAG Layer ⭐

The `rag/` layer contains our AI-specific logic:

```text id="0m7c4x"
rag/
├── ingestion.py
├── chunking.py
├── embeddings.py
├── retrieval.py
├── prompts.py
└── pipeline.py
```

Responsibilities:

| File            | Purpose                  |
| --------------- | ------------------------ |
| `ingestion.py`  | Process documents        |
| `chunking.py`   | Split documents          |
| `embeddings.py` | Generate vectors         |
| `retrieval.py`  | Retrieve relevant chunks |
| `prompts.py`    | Build LLM prompts        |
| `pipeline.py`   | Coordinate RAG           |

Complete flow:

```text id="n6j2p4"
Document
 ↓
Ingestion
 ↓
Chunking
 ↓
Embedding
 ↓
Vector Storage
 ↓
Retrieval
 ↓
Context
 ↓
Prompt
 ↓
LLM
```

---

# Task 9 – Core Layer

The `core/` layer contains important infrastructure:

```text id="w4r7k2"
core/
├── config.py
├── security.py
└── database.py
```

### `config.py`

Application configuration.

### `security.py`

Authentication and security utilities.

### `database.py`

Database connection/session management.

---

# Complete Backend Flow

When an employee asks:

> **"How many casual leaves can I take?"**

The system conceptually works like:

```text id="q5m8y2"
React
  ↓
POST /api/chat
  ↓
API Layer
  ↓
Schema Validation
  ↓
Authentication
  ↓
Chat Service
  ↓
Permission Check
  ↓
RAG Pipeline
  ↓
Retrieval
  ↓
Prompt Construction
  ↓
LLM
  ↓
Repository
  ↓
Database
  ↓
Response
  ↓
React
```

---

# Separation of Responsibilities

| Layer        | Responsibility                  |
| ------------ | ------------------------------- |
| API          | HTTP communication              |
| Schemas      | Data validation                 |
| Services     | Business logic                  |
| Repositories | Database operations             |
| Models       | Database entities               |
| RAG          | AI/retrieval logic              |
| Core         | Configuration/security/database |

This separation is one of the most important software engineering concepts we've learned.

---

# Key Learning

> **A professional backend should separate HTTP handling, validation, business logic, database access, and AI processing instead of putting everything into one file.**

Our core architecture is:

```text id="b2c5z8"
Frontend
   ↓
API
   ↓
Schema
   ↓
Service
   ↓
Repository / RAG
   ↓
Database / Vector Search / LLM
```

---

# Documentation

Created:

```text id="c7v4n1"
docs/sessions/Session-25.md
docs/Backend-Architecture.md
```

`Backend-Architecture.md` contains the permanent backend architecture and folder structure.

---

# Session Outcome

✅ Understood separation of concerns.

✅ Designed the backend folder structure.

✅ Understood API layer.

✅ Understood schema layer.

✅ Understood model layer.

✅ Understood service layer.

✅ Understood repository layer.

✅ Designed the RAG layer.

✅ Understood the core infrastructure layer.

✅ Connected all backend layers into one request flow.

### Project Progress

```text id="k6m1p9"
Requirements            ✅
SRS                     ✅
Architecture            ✅
LLM                     ✅
Embeddings              ✅
Chunking                ✅
Vector Database         ✅
RAG                     ✅
Prompt Engineering      ✅
Retrieval               ✅
Evaluation              ✅
Security                ✅
Technology Selection    ✅
Database Design         ✅
Database Schema         ✅
API Design              ✅
API Contracts           ✅
Backend Architecture    ✅
Implementation          ⏳
Testing                 ⏳
Deployment              ⏳
Production              ⏳
```

### Next — Session 26

**Frontend Architecture & UI Design**

We will design the complete employee journey:

```text
Login
 ↓
Dashboard
 ↓
Document Access/Upload
 ↓
Chat
 ↓
AI Answer + Sources
 ↓
Conversation History
 ↓
Admin Dashboard
```

and understand how the frontend communicates with our backend APIs.
