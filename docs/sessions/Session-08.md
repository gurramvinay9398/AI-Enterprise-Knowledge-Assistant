# Session 08 – Introduction to System Architecture

## Duration

30 Minutes

## Objective

After completing the SRS, we started the **System Design phase**. The purpose of this session was to understand how different parts of our AI Enterprise Knowledge Assistant will communicate before selecting technologies or writing code.

---

## Task 1 – Understanding System Architecture

**System architecture** describes the major components of an application and how they communicate with each other.

We identified five major components:

### 1. Frontend

The interface used by employees.

Examples:

* Login
* Chat interface
* Document upload
* Conversation history
* Admin dashboard

### 2. Backend

Handles the main application logic.

Responsibilities include:

* Authentication
* User requests
* Document processing
* AI requests
* Database operations
* Access control

### 3. Database

Stores structured application information such as:

* Users
* Documents
* Conversations
* Messages
* Permissions

### 4. AI Layer

Handles understanding questions and generating answers.

Basic flow:

```text
User Question
     ↓
Retrieval
     ↓
Relevant Document Content
     ↓
LLM
     ↓
Answer
```

### 5. External Services

External APIs or cloud services may provide AI capabilities that are difficult to run locally because of our limited hardware and Windows 8.1 environment.

---

# Task 2 – Initial Architecture

Our first conceptual architecture is:

```text
Employee
    ↓
Frontend
    ↓
Backend
    ↓
 ┌──────────┬──────────┬──────────┐
 ↓          ↓          ↓
Database   AI Layer   Documents
              ↓
             LLM
```

This is only a **high-level initial design** and will change as we learn more.

---

# Task 3 – Question Flow

For a question such as:

> “What is the company's leave policy?”

The basic flow is:

```text
Employee asks question
        ↓
Frontend
        ↓
Backend
        ↓
Find relevant information
        ↓
AI generates answer
        ↓
Backend
        ↓
Frontend
        ↓
Answer + Source Reference
```

An important realization was that the **LLM should not be expected to know private company policies by itself**. The company's documents contain the required knowledge.

This leads to our next major concept:

**RAG – Retrieval-Augmented Generation.**

---

# Key Learning

We learned the difference between **what the system does** and **how its components work together**.

We also learned that architecture should be designed before implementation.

---

# Session Outcome

✅ Started the System Design phase.

✅ Identified frontend, backend, database, AI layer, and external services.

✅ Created the initial architecture.

✅ Understood the basic question-answer flow.

✅ Identified why RAG will be important.

**Next:** Learn **LLMs → Embeddings → Semantic Search → Vector Databases → RAG**, and then update `docs/Architecture.md` with our refined architecture.
