# Session 19 – Technology Stack Selection & Decision

## Duration

30 Minutes

## Objective

The purpose of Session 19 was to move from **technology options** toward a practical technology stack for our AI Enterprise Knowledge Assistant.

We learned that technology should be selected based on **requirements, constraints, compatibility, cost, production suitability, and maintainability**.

---

# Task 1 – Technology Selection Criteria

We will evaluate technologies based on:

* Windows 8.1 compatibility
* AI/RAG ecosystem
* Production suitability
* Learning value
* Ease of development
* Performance
* Cost
* Maintainability
* Deployment options

### Decision Process

```text
Requirements
      ↓
Constraints
      ↓
Available Options
      ↓
Comparison
      ↓
Decision
      ↓
Reason
```

---

# Task 2 – Backend Decision

### Java + Spring Boot

```text
Java
 ↓
Spring Boot
 ↓
REST API
```

Advantages:

* Strong enterprise usage.
* Excellent for backend development.
* Good OOP and software engineering practice.

### Python + FastAPI

```text
Python
 ↓
FastAPI
 ↓
AI/RAG Ecosystem
```

Advantages:

* Strong AI/ML ecosystem.
* Convenient for RAG development.
* Large AI/ML library ecosystem.

### Current Decision

**Python + FastAPI is our current backend candidate** because this particular project is heavily focused on AI/RAG.

We will verify exact versions and dependencies before implementation because of the Windows 8.1 constraint.

---

# Task 3 – Frontend Decision

We considered:

### HTML/CSS/JavaScript

* Lightweight
* Simple
* Easy to develop

### React

* Component-based
* Good for interactive applications
* Strong industry relevance

### Current Direction

**React is our current frontend candidate**, provided the selected development tooling works correctly on Windows 8.1.

If compatibility becomes a serious problem, we can use a simpler frontend without changing the core RAG architecture.

---

# Task 4 – Database Decision

### SQLite

Useful for:

* Local development
* MVP
* Lightweight setup

### PostgreSQL

Useful for:

* Production
* Multiple users
* Scalability
* Strong relational capabilities

### Current Direction

```text
Development → SQLite
Production   → PostgreSQL
```

We will design the application so that moving from SQLite to PostgreSQL is manageable.

---

# Task 5 – Vector Search

We considered:

* Local vector store
* Dedicated vector database
* PostgreSQL with vector capabilities

### Decision

**Not finalized yet.**

We will compare these options based on:

* Windows 8.1 compatibility
* Cost
* Performance
* Simplicity
* Production capability
* RAG requirements

---

# Task 6 – LLM and Embeddings

Because our laptop has limited hardware:

```text
Laptop
   ↓
Backend
   ↓
Cloud LLM API
   ↓
Answer
```

We do **not** plan to depend on running a large LLM locally.

For embeddings, we will evaluate:

* Lightweight local models
* Hosted embedding APIs

The final choice will depend on compatibility, cost, privacy, and quality.

---

# Initial Technology Architecture

Our current candidate architecture:

```text
                 User
                   ↓
             React Frontend
                   ↓
             FastAPI Backend
                   ↓
       ┌───────────┼───────────┐
       ↓           ↓           ↓
   Database       RAG      Authentication
                   ↓
             Vector Search
                   ↓
               Embeddings
                   ↓
              Cloud LLM
```

This is a **candidate architecture**, not yet the final production architecture.

---

# Technology Decision Table

| Component      | Current Choice/Direction | Status      |
| -------------- | ------------------------ | ----------- |
| Frontend       | React                    | Candidate   |
| Backend        | Python + FastAPI         | Candidate   |
| Development DB | SQLite                   | Initial     |
| Production DB  | PostgreSQL               | Candidate   |
| Vector Search  | To evaluate              | Open        |
| LLM            | Cloud API                | Direction   |
| Embeddings     | To evaluate              | Open        |
| Authentication | JWT/Secure Sessions      | To evaluate |
| Deployment     | Cloud platform           | To evaluate |

---

# Important Engineering Lesson

We should not select technologies simply because:

> **"Everyone is using it."**

Instead:

> **Requirements + Constraints → Compare → Decide → Justify**

Also, the **initial development stack and final production stack can differ** when the architecture is designed properly.

---

# Session Outcome

✅ Learned professional technology selection.

✅ Compared Java and Python for our project.

✅ Selected Python + FastAPI as the current backend candidate.

✅ Selected React as the current frontend candidate.

✅ Planned SQLite for initial development.

✅ Identified PostgreSQL as a production candidate.

✅ Decided to use a cloud LLM rather than depending on a large local model.

✅ Kept vector search and embeddings open for further evaluation.

✅ Created the initial technology decision matrix.

### Project Progress

```text
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
Initial Stack           ✅
Database Design         ⏳
API Design              ⏳
Implementation          ⏳
Testing                 ⏳
Deployment              ⏳
Production              ⏳
```

**Next: Session 20 — Database Design**

We will design the actual database structure for **users, roles, documents, permissions, conversations, messages, and audit records**, and understand how the relational database connects with our RAG system.
