# Session 23 – API Design

## Duration

30 Minutes

## Objective

Understand how the **frontend communicates with the backend** through APIs and design the initial API structure for our AI Enterprise Knowledge Assistant.

---

# Task 1 – What Is an API?

**API = Application Programming Interface.**

In our project, the API acts as the communication layer between the frontend and backend.

```text id="n8k4ae"
Frontend
   ↓
HTTP Request
   ↓
Backend API
   ↓
Processing
   ↓
HTTP Response
   ↓
Frontend
```

Our architecture:

```text id="x8s6zq"
React Frontend
      ↓
REST API
      ↓
FastAPI Backend
      ↓
Database + RAG + LLM
```

---

# Task 2 – HTTP Methods

| Method | Purpose          | Example                      |
| ------ | ---------------- | ---------------------------- |
| GET    | Retrieve data    | `GET /api/documents`         |
| POST   | Create/submit    | `POST /api/chat`             |
| PUT    | Replace/update   | `PUT /api/users/profile`     |
| PATCH  | Partially update | `PATCH /api/users/profile`   |
| DELETE | Delete           | `DELETE /api/documents/{id}` |

Remember:

```text id="6j8xsp"
GET     → Read
POST    → Create / Submit
PUT     → Replace
PATCH   → Partial Update
DELETE  → Delete
```

---

# Task 3 – Authentication APIs

Initial authentication endpoints:

```text id="e7qj1x"
POST /api/auth/register
POST /api/auth/login
POST /api/auth/logout
GET  /api/auth/me
```

Login concept:

```text id="1s3w9y"
Frontend
   ↓
Email + Password
   ↓
Backend
   ↓
Verify Credentials
   ↓
Authenticated User
```

We will later decide between **JWT, secure sessions, or another suitable approach**.

---

# Task 4 – Document APIs

Initial document endpoints:

```text id="0shxwy"
POST   /api/documents/upload
GET    /api/documents
GET    /api/documents/{id}
DELETE /api/documents/{id}
```

Upload flow:

```text id="l9y9xz"
Upload Document
      ↓
Validate File
      ↓
Store File
      ↓
Extract Text
      ↓
Chunk
      ↓
Create Embeddings
      ↓
Vector Storage
```

Document processing may later be moved to background processing instead of keeping the upload request waiting.

---

# Task 5 – Chat API ⭐

The most important API:

```text id="a9qvxb"
POST /api/chat
```

Example request:

```json id="n3h5gj"
{
  "conversation_id": 15,
  "question": "How many casual leaves can I take?"
}
```

Backend flow:

```text id="2f2g74"
Question
   ↓
Authentication
   ↓
Permission Check
   ↓
Retrieve Relevant Chunks
   ↓
Construct Context
   ↓
LLM
   ↓
Generate Answer
   ↓
Save Message
```

Possible response:

```json id="5f2j0c"
{
  "answer": "Employees receive 12 casual leaves per year.",
  "sources": [
    {
      "document": "Employee_Leave_Policy.pdf",
      "page": 12
    }
  ]
}
```

This directly satisfies our client requirement:

> **Simple answer + document reference.**

---

# Task 6 – Conversation APIs

To support conversation history:

```text id="g7g9q3"
GET    /api/conversations
POST   /api/conversations
GET    /api/conversations/{id}
DELETE /api/conversations/{id}
```

These APIs interact with our:

```text id="u2p8zw"
conversations
messages
```

tables.

---

# Task 7 – HTTP Status Codes

Important status codes:

| Code | Meaning            |
| ---- | ------------------ |
| 200  | Successful request |
| 201  | Resource created   |
| 400  | Bad request        |
| 401  | Not authenticated  |
| 403  | Not authorized     |
| 404  | Resource not found |
| 409  | Conflict           |
| 422  | Validation error   |
| 500  | Server error       |

### Important Difference

**401:**

> Who are you?

Authentication problem.

**403:**

> You are authenticated, but you aren't allowed to perform this action.

Authorization problem.

---

# Initial API Structure

```text id="k3yr6f"
Authentication
----------------
POST /api/auth/register
POST /api/auth/login
POST /api/auth/logout
GET  /api/auth/me

Documents
----------------
POST   /api/documents/upload
GET    /api/documents
GET    /api/documents/{id}
DELETE /api/documents/{id}

Chat
----------------
POST /api/chat

Conversations
----------------
GET    /api/conversations
POST   /api/conversations
GET    /api/conversations/{id}
DELETE /api/conversations/{id}
```

These are **initial endpoints** and can be refined later.

---

# API Design Principles

Our APIs should:

1. Have a clear responsibility.
2. Validate input.
3. Require authentication where necessary.
4. Check authorization.
5. Return consistent responses.
6. Handle errors safely.
7. Never expose passwords, secrets, or internal system details.

---

# Complete API Architecture

```text id="a3u5h1"
                React Frontend
                       ↓
                  REST API
                       ↓
                FastAPI Backend
                       ↓
          ┌────────────┼────────────┐
          ↓            ↓            ↓
      Database        RAG      Authentication
                       ↓
                Vector Search
                       ↓
                      LLM
                       ↓
                  API Response
                       ↓
                React Frontend
```

---

# Key Learning

> **An API is the communication contract between our frontend and backend.**

The frontend sends an HTTP request, the backend validates and processes it, and the backend returns a structured response.

Our major application flow is:

```text id="o6r4h7"
Frontend
   ↓
API
   ↓
FastAPI
   ↓
Authentication
   ↓
Database / RAG
   ↓
LLM
   ↓
API Response
   ↓
Frontend
```

---

# Documentation

We created/updated:

```text id="h4k2r9"
docs/sessions/Session-23.md
docs/API-Design.md
```

`API-Design.md` contains our permanent API blueprint.

---

# Session Outcome

✅ Understood APIs.

✅ Learned HTTP methods.

✅ Designed authentication APIs.

✅ Designed document APIs.

✅ Designed the main chat API.

✅ Designed conversation APIs.

✅ Learned HTTP status codes.

✅ Understood authentication vs authorization in APIs.

✅ Created the initial API architecture.

### Project Progress

```text id="2v6j8k"
Requirements            ✅
SRS                     ✅
Architecture Basics     ✅
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
DB Relationships        ✅
Database Schema         ✅
API Design              ✅
Implementation          ⏳
Testing                 ⏳
Deployment              ⏳
Production              ⏳
```

### Next — Session 24

**API Request/Response Design & Error Handling**

We'll define the actual **request JSON, response JSON, validation rules, authentication requirements, error format, and detailed flow** for each major API before starting FastAPI implementation.
