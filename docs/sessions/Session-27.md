# Session 27 – Frontend–Backend Integration & Complete Application Flow

## Duration

30 Minutes

## Objective

In Session 27, we connected everything designed so far:

```text
Frontend
   ↓
API
   ↓
Backend
   ↓
Database / RAG
   ↓
LLM
   ↓
Response
   ↓
Frontend
```

The goal was to understand **how one employee action travels through the complete system and returns a useful result**.

---

# 1. Full-Stack Integration

Our application consists of multiple layers:

```text
User
 ↓
React Frontend
 ↓
REST API
 ↓
FastAPI Backend
 ↓
Services
 ↓
Database / RAG
 ↓
LLM
 ↓
Backend
 ↓
API Response
 ↓
Frontend
 ↓
User
```

The frontend does not need to know the internal RAG or LLM implementation.

It only needs to:

```text
Send Request
     ↓
Receive Response
     ↓
Display Result
```

This is **abstraction**.

---

# 2. Login Flow

When an employee logs in:

```text
Login Page
    ↓
POST /api/auth/login
    ↓
Backend
    ↓
Validate Credentials
    ↓
Verify Password Hash
    ↓
Authentication
    ↓
Authentication Result
    ↓
Dashboard
```

The frontend maintains authentication state.

If the user is authenticated:

```text
Authenticated
     ↓
Dashboard
Chat
Documents
```

If authentication is missing or expired:

```text
Protected Page
      ↓
Not Authenticated
      ↓
Login Page
```

### Important

Frontend authentication state is for **user experience**.

The **backend must always enforce real security**.

---

# 3. Complete Chat Flow ⭐

Suppose the employee asks:

> **What is the work-from-home policy?**

### Step 1 — User asks question

```text
Chat UI
 ↓
Question
```

### Step 2 — Frontend calls API

```text
POST /api/chat
```

Example:

```json
{
  "conversation_id": 15,
  "question": "What is the work-from-home policy?"
}
```

### Step 3 — Authentication

Backend verifies the user.

### Step 4 — Authorization

Backend checks whether the user can access the relevant enterprise documents.

```text
User
 ↓
Role
 ↓
Document Permissions
```

### Step 5 — RAG Retrieval

```text
Question
   ↓
Query Processing
   ↓
Embedding
   ↓
Vector Search
   ↓
Relevant Chunks
```

### Step 6 — Build Context

```text
Question
+
Relevant Document Chunks
        ↓
     Context
```

### Step 7 — LLM

```text
Context + Question
        ↓
       LLM
        ↓
      Answer
```

### Step 8 — Save Conversation

```text
User Question
+
AI Answer
      ↓
Messages Table
```

### Step 9 — API Response

```json
{
  "answer": "Employees can work from home according to the approved policy.",
  "sources": [
    {
      "document": "Work_From_Home_Policy.pdf",
      "page": 4
    }
  ]
}
```

### Step 10 — Frontend

The UI displays:

```text
AI Answer
────────────
Employees can work from home...

Sources
────────────
Work_From_Home_Policy.pdf
Page 4
```

---

# 4. Loading State

RAG and LLM processing may take some time.

Instead of showing a frozen screen:

```text
⏳ Searching company documents...
```

Possible stages:

```text
Searching documents...
       ↓
Analyzing relevant information...
       ↓
Generating answer...
       ↓
Answer received
```

This provides a better user experience.

---

# 5. Error Flow

If something goes wrong:

```text
Frontend
   ↓
API
   ↓
Backend
   ↓
Error
```

The backend returns a safe response:

```json
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "Something went wrong. Please try again."
  }
}
```

Frontend can display:

> ⚠️ We couldn't process your question. Please try again.

Never expose:

```text
API keys
Passwords
Database errors
Stack traces
Internal system details
```

These should remain in server-side logs.

---

# 6. Document Upload Flow

Authorized user:

```text
Upload Document
       ↓
POST /api/documents/upload
       ↓
Authentication
       ↓
Authorization
       ↓
File Validation
       ↓
Store Document
       ↓
Extract Text
       ↓
Clean Text
       ↓
Chunk
       ↓
Generate Embeddings
       ↓
Vector Storage
       ↓
Update Status
```

Possible statuses:

```text
uploaded
   ↓
processing
   ↓
processed
```

If processing fails:

```text
processing
   ↓
failed
```

---

# 7. Conversation History Flow

To retrieve conversations:

```text
Conversation History
       ↓
GET /api/conversations
       ↓
Backend
       ↓
Database
       ↓
Conversation List
       ↓
Frontend
```

To open one conversation:

```text
GET /api/conversations/{id}
       ↓
Messages
       ↓
Chat UI
```

This gives our assistant **persistent conversation history**.

---

# 8. Complete Application Architecture

```text
                         USER
                           ↓
                    React Frontend
                           ↓
                    Authentication
                           ↓
                      Dashboard
                           ↓
                     Ask Question
                           ↓
                      REST API
                           ↓
                    FastAPI Backend
                           ↓
                  Authentication Check
                           ↓
                  Authorization Check
                           ↓
                     Chat Service
                           ↓
                     RAG Pipeline
                           ↓
                   Vector Retrieval
                           ↓
                   Relevant Chunks
                           ↓
                         LLM
                           ↓
                  Answer + References
                           ↓
                   Save Conversation
                           ↓
                       API Response
                           ↓
                    React Frontend
                           ↓
                  Answer + Sources
                           ↓
                         USER
```

This is our **core end-to-end application flow**.

---

# 9. Important Concepts Learned

### Abstraction

Frontend doesn't need to know how RAG internally works.

### Authentication

Determines **who the user is**.

### Authorization

Determines **what the user is allowed to access**.

### RAG

Retrieves relevant enterprise information before sending context to the LLM.

### LLM

Generates the natural-language answer using the provided context.

### API

Connects frontend and backend.

### Database

Stores users, documents, conversations, messages, permissions, etc.

---

# Key Learning

> **Session 27 connected the entire product into one end-to-end flow: the employee interacts with the frontend, the request travels through APIs and backend services, RAG retrieves relevant enterprise information, the LLM generates an answer, and the response with sources returns to the frontend.**

---

# Documentation

Created:

```text
docs/sessions/Session-27.md
docs/Application-Flow.md
```

`Application-Flow.md` contains the permanent end-to-end application flow.

---

# Session Outcome

✅ Understood full-stack integration.

✅ Designed complete login flow.

✅ Understood authentication state.

✅ Designed complete chat flow.

✅ Connected RAG with backend APIs.

✅ Connected LLM with RAG.

✅ Designed loading states.

✅ Designed error flow.

✅ Designed document processing flow.

✅ Designed conversation history flow.

✅ Connected the complete application architecture.

### Project Progress

```text
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
Frontend Architecture   ✅
Application Flow        ✅
Implementation          ⏳
Testing                 ⏳
Deployment              ⏳
Production              ⏳
```

## Next — Session 28

**Development Environment & Project Initialization**

We will finally move toward implementation: verify the **Windows 8.1-compatible environment**, create the project structure, configure Git and environment variables, and make the first minimal backend/frontend application run successfully.
