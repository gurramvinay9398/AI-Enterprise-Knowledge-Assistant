# Session 24 – API Request/Response Design & Error Handling

## Duration

30 Minutes

## Objective

Session 23 defined **which APIs our application needs**. Session 24 defined **exactly how those APIs communicate** through requests, responses, validation, authentication, authorization, and error handling.

---

# Task 1 – API Contract

An **API contract** defines:

* HTTP method
* Endpoint
* Authentication requirement
* Request format
* Validation rules
* Response format
* Possible errors

Conceptually:

```text id="g9j4tq"
Frontend
   ↓
Request
   ↓
API
   ↓
Validation
   ↓
Processing
   ↓
Response
   ↓
Frontend
```

The contract acts as an agreement between frontend and backend.

---

# Task 2 – Login API

### Endpoint

```text id="7y2h8r"
POST /api/auth/login
```

### Request

```json id="5u7x0c"
{
  "email": "employee@company.com",
  "password": "********"
}
```

### Validation

* Email is required.
* Password is required.
* Email format should be valid.
* Credentials must be securely verified.

### Success Response

```json id="8d5r2x"
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "name": "Employee",
    "role": "employee"
  }
}
```

The exact authentication mechanism will be finalized during implementation.

---

# Task 3 – Document Upload API

### Endpoint

```text id="l8v0k2"
POST /api/documents/upload
```

File uploads use **multipart/form-data**.

Conceptually:

```text id="p3w7k4"
Upload File
    ↓
Validate File
    ↓
Check User Permission
    ↓
Store File
    ↓
Process Document
```

Validation includes:

* File exists.
* Supported file type.
* Acceptable file size.
* User has permission.
* Safe filename/path.

### Example Response

```json id="f4n6q8"
{
  "message": "Document uploaded successfully",
  "document": {
    "id": 15,
    "file_name": "Employee_Leave_Policy.pdf",
    "status": "processing"
  }
}
```

`processing` allows us to later support background document processing.

---

# Task 4 – Chat API ⭐

This is the most important API.

### Endpoint

```text id="s3j7w1"
POST /api/chat
```

### Request

```json id="k2m8v5"
{
  "conversation_id": 15,
  "question": "How many casual leaves can I take?"
}
```

### Backend Flow

```text id="r4n6x8"
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
Save Messages
```

### Response

```json id="u7p2c9"
{
  "answer": "Employees receive 12 casual leaves per year.",
  "sources": [
    {
      "document": "Employee_Leave_Policy.pdf",
      "page": 12
    }
  ],
  "conversation_id": 15
}
```

This directly supports our client's requirement:

> **Simple answer + document reference.**

---

# Task 5 – Standard Error Format

Our APIs should return errors consistently.

Example:

```json id="h5k9q2"
{
  "error": {
    "code": "ACCESS_DENIED",
    "message": "You do not have permission to access this resource."
  }
}
```

Another example:

```json id="n3v7x1"
{
  "error": {
    "code": "DOCUMENT_NOT_FOUND",
    "message": "The requested document was not found."
  }
}
```

### Never expose internal errors

Bad:

```text id="b2w8j4"
SQLite error: table users...
```

Good:

```json id="z6p1r8"
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "Something went wrong. Please try again."
  }
}
```

Technical details should remain in **server-side logs**.

---

# Task 6 – Important HTTP Errors

| Status | Meaning               |
| ------ | --------------------- |
| 400    | Bad request           |
| 401    | Not authenticated     |
| 403    | Not authorized        |
| 404    | Resource not found    |
| 409    | Conflict              |
| 422    | Validation error      |
| 500    | Internal server error |

### Remember

**401:**

> Who are you?

Authentication problem.

**403:**

> You are authenticated, but you aren't allowed to do this.

Authorization problem.

---

# Task 7 – Secure API Flow

Every protected API should conceptually follow:

```text id="q7t3m5"
Request
  ↓
Authentication
  ↓
Authorization
  ↓
Validation
  ↓
Business Logic
  ↓
Response
```

We should **not** access protected resources first and check permissions afterward.

This connects directly with our Session 17 enterprise security design.

---

# Key Learning

> **An API contract defines exactly how the frontend and backend communicate, including requests, responses, validation, authentication, authorization, and errors.**

Our overall flow is:

```text id="v8x2m6"
Frontend
   ↓
Request
   ↓
API
   ↓
Validation
   ↓
Authentication
   ↓
Authorization
   ↓
Database / RAG / LLM
   ↓
Response
   ↓
Frontend
```

---

# Documentation

We created/updated:

```text id="c5k8n2"
docs/sessions/Session-24.md
docs/API-Design.md
```

`API-Design.md` now contains our API contracts and standard error structure.

---

# Session Outcome

✅ Understood API contracts.

✅ Designed login request/response.

✅ Designed document-upload request/response.

✅ Designed chat request/response.

✅ Learned validation.

✅ Designed a standard error format.

✅ Learned important HTTP status codes.

✅ Connected API security with authentication and authorization.

### Project Progress

```text id="w4q8m1"
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
Implementation          ⏳
Testing                 ⏳
Deployment              ⏳
Production              ⏳
```

## Next — Session 25

**Backend Architecture & Project Structure**

We'll design our FastAPI backend structure and understand how to separate:

**API routes → schemas → services → database/repositories → RAG → LLM**

instead of putting the entire application inside one `app.py` file.
