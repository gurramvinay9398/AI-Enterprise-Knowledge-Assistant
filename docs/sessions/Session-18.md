# Session 18 – Technology Selection & Architecture Decisions

## Duration

30 Minutes

## Objective

Understand how professional engineers select technologies based on **requirements, constraints, compatibility, cost, maintainability, and production needs**, instead of simply choosing popular technologies.

---

# Task 1 – Technology Selection

Technology selection means choosing tools and frameworks that best satisfy our project's requirements and limitations.

We should consider:

* Does it solve our problem?
* Is it compatible with our development environment?
* Is it suitable for production?
* Is it maintainable?
* Does it have a strong ecosystem?
* Can we deploy it?
* Does it provide useful industry knowledge?

### Important Principle

> **Don't choose technology because it is trending. Choose it because it fits the problem.**

---

# Task 2 – Backend Options

We compared two major options.

### Java + Spring Boot

```text
Java
 ↓
Spring Boot
 ↓
REST APIs
```

Advantages:

* Strong enterprise adoption.
* Excellent for backend development.
* Encourages OOP and structured architecture.
* Valuable for software engineering jobs.

### Python + FastAPI

```text
Python
 ↓
FastAPI
 ↓
REST APIs
 ↓
AI/RAG Ecosystem
```

Advantages:

* Strong AI/ML ecosystem.
* Convenient for RAG development.
* Large number of AI libraries are Python-based.
* Good fit for our AI-heavy project.

### Current Understanding

We **did not permanently choose the backend yet**.

Python is currently a strong candidate for this AI/RAG project, while Java remains highly valuable for enterprise/backend learning and job preparation.

We will verify exact versions and dependencies before implementation because of the Windows 8.1 constraint.

---

# Task 3 – Other Technology Categories

### Frontend

Possible options:

* HTML/CSS/JavaScript
* React

Used for:

```text
Login
Chat
Document Upload
Dashboard
Conversation History
```

### Database

Possible options:

* SQLite → simple development/MVP
* PostgreSQL → production-oriented relational database

Used for:

```text
Users
Roles
Documents
Messages
Conversations
Permissions
```

### Vector Search

Possible approaches:

* Local vector store/library
* Dedicated vector database
* PostgreSQL with vector capabilities

Used for:

```text
Document Chunks
Embeddings
Metadata
```

### LLM

Because our laptop has limited resources:

```text
Laptop
  ↓
Backend
  ↓
Cloud LLM/API
  ↓
Answer
```

We don't plan to run a large LLM locally.

### Embeddings

Used to convert:

```text
Document Chunk
      ↓
Embedding Model
      ↓
Vector
```

The exact embedding approach will be selected later.

---

# Task 4 – Technology Decision Process

We learned that professional technology selection follows:

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
Justification
```

Instead of:

```text
Popular Technology
      ↓
Use It
```

---

# Technology Decision Matrix

Our initial matrix:

| Component      | Options                          | Decision    |
| -------------- | -------------------------------- | ----------- |
| Frontend       | HTML/CSS/JS, React               | To evaluate |
| Backend        | Python/FastAPI, Java/Spring Boot | To evaluate |
| Database       | SQLite, PostgreSQL               | To evaluate |
| Vector Search  | Local/Dedicated/PostgreSQL       | To evaluate |
| LLM            | Cloud/API                        | To evaluate |
| Embeddings     | Local/API                        | To evaluate |
| Authentication | JWT/Session-based                | To evaluate |
| Deployment     | Cloud platform                   | To evaluate |

We intentionally **didn't lock the stack yet**.

---

# Key Learning

The most important lesson:

> **Start with requirements and constraints, compare technologies, make a decision, and document why that decision was made.**

Our Windows 8.1 and hardware limitations are real engineering constraints and must influence our technology choices.

---

# Session Outcome

✅ Learned technology selection.

✅ Compared Java/Spring Boot and Python/FastAPI.

✅ Identified frontend options.

✅ Identified database options.

✅ Identified vector-search approaches.

✅ Understood cloud LLM usage.

✅ Created the initial technology decision matrix.

✅ Added technology-selection principles to `Architecture.md`.

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
Final Stack             ⏳
Database Design         ⏳
API Design              ⏳
Implementation          ⏳
Testing                 ⏳
Deployment              ⏳
Production              ⏳
```

### Next: Session 19

**Final Technology Stack Selection**

We'll compare the candidates more deeply and **lock the actual technology stack** for our project, including frontend, backend, database, vector search, LLM, embeddings, authentication, and deployment.
