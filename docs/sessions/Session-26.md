# Session 26 – Frontend Architecture & UI Design

## Duration

30 Minutes

## Objective

Design the **user-facing part** of our AI Enterprise Knowledge Assistant and understand how employees will interact with the product.

The main principle:

> **Frontend = User Experience Layer**

It communicates with the backend through APIs. It should **never directly access the database or LLM**.

---

# Task 1 – Frontend Responsibility

The frontend provides:

* Login
* Dashboard
* AI Chat
* Document access/upload
* Source references
* Conversation history
* Admin dashboard

Basic architecture:

```text
User
 ↓
Frontend
 ↓
Backend API
 ↓
Database / RAG / LLM
```

---

# Task 2 – Employee User Journey

Our main employee journey:

```text
Login
  ↓
Dashboard
  ↓
Open AI Assistant
  ↓
Ask Question
  ↓
RAG Processing
  ↓
Answer
  ↓
View Source
  ↓
Continue Conversation
```

Example:

**Employee:**

> How many casual leaves can I take?

**AI:**

> You can take 12 casual leaves per year.

**Source:**

> Employee Leave Policy.pdf — Page 12

This is the **core product experience**.

---

# Task 3 – Main Screens

## 1. Login

Purpose:

> Authenticate the user.

```text
Enterprise AI Knowledge Assistant

Email
[____________]

Password
[____________]

[ Login ]
```

---

## 2. Dashboard

Provides a quick overview:

```text
Welcome, Employee

[ Ask AI Assistant ]

Recent Conversations
• Leave policy
• Work from home
• Medical reimbursement

Documents Available: 24
```

---

## 3. AI Chat ⭐

Most important screen:

```text
AI Enterprise Knowledge Assistant

User:
How many casual leaves can I take?

AI:
You can take 12 casual leaves per year.

Source:
Employee Leave Policy.pdf
Page 12

[ Ask another question... ]
```

The answer and source should be clearly visible.

---

# Task 4 – Conversation History

Employees should access previous conversations.

```text
Conversation History

Today
• Leave policy
• Work from home policy

Yesterday
• Medical reimbursement
• Working hours
```

Selecting a conversation can call:

```text
GET /api/conversations/{id}
```

---

# Task 5 – Document Management

Authorized users can manage documents.

```text
Documents

[ Upload Document ]

Employee Leave Policy.pdf ✓ Processed
HR Policy.pdf             ✓ Processed
Work From Home Policy.pdf ⏳ Processing
```

Only authorized users should receive upload/delete capabilities.

---

# Task 6 – Admin Dashboard

Administrators may have:

```text
Admin Dashboard

Users
Documents
Roles & Permissions
System Activity
Processing Status
```

Possible functions:

```text
[ Manage Users ]
[ Manage Documents ]
[ View Audit Logs ]
```

### Important Security Principle

> **Hiding a button is not security.**

Even if the frontend hides an admin feature, the **backend must independently check authorization**.

---

# Task 7 – Frontend → Backend Communication

### Login

```text
Login Page
   ↓
POST /api/auth/login
   ↓
FastAPI
   ↓
Authentication
   ↓
Response
   ↓
Dashboard
```

### Chat

```text
Chat UI
   ↓
POST /api/chat
   ↓
FastAPI
   ↓
RAG
   ↓
LLM
   ↓
Answer
   ↓
Chat UI
```

### Document Upload

```text
Upload UI
   ↓
POST /api/documents/upload
   ↓
FastAPI
   ↓
Document Processing
   ↓
Vector Storage
```

---

# Task 8 – Frontend Component Structure

Instead of one large frontend file, we can use reusable components.

```text
frontend/
│
├── components/
│   ├── Navbar
│   ├── ChatWindow
│   ├── MessageBubble
│   ├── SourceReference
│   ├── DocumentCard
│   └── LoadingIndicator
│
├── pages/
│   ├── Login
│   ├── Dashboard
│   ├── Chat
│   ├── Documents
│   └── Admin
│
├── services/
│   └── api
│
└── App
```

The exact structure will be refined during implementation.

---

# Task 9 – Important UX Requirements

Because our client wants **simple answers for employees**, the interface should prioritize:

### Simplicity

Avoid unnecessary technical AI terminology.

### Source Visibility

Clearly display:

```text
Source: LeavePolicy.pdf
Page: 12
```

### Loading State

```text
AI is searching company documents...
```

### Error State

```text
Sorry, we couldn't process your request.
Please try again.
```

### Empty State

```text
Ask a question about company policies.
```

These small details make the application feel like a **real product**, not just an AI demo.

---

# Complete Product Architecture

```text
                    USER
                      ↓
               React Frontend
                      ↓
               FastAPI REST API
                      ↓
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
 Authentication    Database          RAG
                                      ↓
                              Vector Search
                                      ↓
                                     LLM
                                      ↓
                              Answer + Sources
                                      ↓
                              React Frontend
```

---

# Key Learning

> **The frontend is the user experience layer. It communicates with the backend through APIs and presents the AI answer, document sources, conversations, and other functionality to the employee.**

The complete employee flow:

```text
Employee
   ↓
Login
   ↓
Dashboard
   ↓
Ask Question
   ↓
Frontend → API
   ↓
Authentication + Authorization
   ↓
RAG
   ↓
LLM
   ↓
Answer + Source
   ↓
Frontend
```

---

# Documentation

Created:

```text
docs/sessions/Session-26.md
docs/Frontend-Architecture.md
```

`Frontend-Architecture.md` contains the permanent frontend design and user journey.

---

# Session Outcome

✅ Understood frontend responsibility.

✅ Designed employee user journey.

✅ Designed Login.

✅ Designed Dashboard.

✅ Designed AI Chat.

✅ Designed source/reference display.

✅ Designed conversation history.

✅ Designed document management.

✅ Designed admin dashboard.

✅ Understood frontend–backend communication.

✅ Learned important UX and security principles.

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
Implementation          ⏳
Testing                 ⏳
Deployment              ⏳
Production              ⏳
```

## Next — Session 27

**Frontend–Backend Integration & Complete Application Flow**

We will design the exact flow of **login → authentication → dashboard → chat → API → RAG → LLM → answer → source → conversation history**, including loading states, errors, authentication state, and API communication.
