# Session 20 – Database Design

## Duration

30 Minutes

## Objective

Understand how to design the **structured data layer** of our AI Enterprise Knowledge Assistant and how it connects with authentication, security, conversations, and RAG.

---

# Task 1 – What Does Our Database Store?

Our application needs to store structured information such as:

```text id="t2hj8n"
Users
Roles
Documents
Permissions
Conversations
Messages
Audit Logs
```

Instead of storing everything in one table, we separate the information into related tables.

---

# Task 2 – Users and Roles

### Users

Initial `users` table:

```text id="qk5t6p"
id
name
email
password_hash
role_id
created_at
updated_at
```

**Important:** Passwords must never be stored as plain text. We store secure password hashes.

### Roles

```text id="y5avk1"
id
name
description
```

Possible roles:

```text id="z7bx9c"
Employee
HR
Manager
Admin
```

Relationship:

```text id="9d5n7c"
Role
 ↓
Users
```

One role can be assigned to multiple users.

---

# Task 3 – Documents and Permissions

### Documents

Stores information about uploaded enterprise documents:

```text id="6w9c1y"
id
file_name
file_path
document_type
department
uploaded_by
created_at
updated_at
status
```

### Document Permissions

Controls who can access each document:

```text id="x3c8mh"
id
document_id
role_id
access_type
```

Example:

```text id="5b9x2a"
LeavePolicy.pdf
   ↓
Employee → Read
HR       → Read
Admin    → Read
```

This connects our **database design with our security architecture**.

---

# Task 4 – Conversations and Messages

### Conversations

Stores employee chat sessions:

```text id="t1k8hy"
id
user_id
title
created_at
updated_at
```

### Messages

Stores individual messages:

```text id="z8f4yk"
id
conversation_id
role
content
created_at
```

Relationship:

```text id="w0f1pj"
Conversation
     ↓
Message 1 → User
Message 2 → AI
Message 3 → User
Message 4 → AI
```

This allows the application to maintain conversation history.

---

# Task 5 – Audit Logs

Audit logs record important system activities.

Example:

```text id="4h7jlp"
audit_logs
-------------------------
id
user_id
action
resource_type
resource_id
timestamp
```

Example activity:

```text id="h7x5tq"
User: 25
Action: DOCUMENT_UPLOAD
Resource: LeavePolicy.pdf
Time: 10:30 AM
```

Audit logs can help with:

* Security investigations
* Troubleshooting
* Monitoring
* Compliance

Sensitive document content should not unnecessarily be placed inside logs.

---

# Task 6 – SQL Database vs Vector Storage

This is one of the most important concepts.

### SQL Database

Stores application/transactional data:

```text id="f8v5js"
Users
Roles
Documents
Permissions
Conversations
Messages
Audit Logs
```

### Vector Storage

Stores information needed for semantic retrieval:

```text id="b5m8qs"
Document Chunks
Embeddings
Metadata
```

They have different responsibilities.

```text id="s7r9mk"
                Application
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
    SQL Database        Vector Storage
          ↓                   ↓
 Users/Roles/etc.     Embeddings/Chunks
```

---

# Task 7 – Connection With RAG

When an employee asks:

> **"How many casual leaves can I take?"**

The application conceptually performs:

```text id="3p8n2v"
Identify User
      ↓
Check Permissions
      ↓
Search Allowed Documents
      ↓
Retrieve Relevant Chunks
      ↓
Send Context to LLM
      ↓
Generate Answer
      ↓
Save Conversation
      ↓
Display Answer + Source
```

This shows how our **database + security + RAG + chat system** work together.

---

# Initial Database Relationship

```text id="1r7n9v"
                     Roles
                       │
                       ▼
                     Users
                    /     \
                   /       \
                  ▼         ▼
          Conversations   Documents
                │             │
                ▼             ▼
             Messages   Document Permissions
                              │
                              ▼
                             Roles

Users ───────────────→ Audit Logs
```

This is our **initial conceptual relational design**.

---

# Key Learning

The main lesson:

> **The relational database manages structured application data, while vector storage manages semantic document retrieval.**

They work together rather than necessarily replacing each other.

---

# Session Outcome

✅ Understood database design.

✅ Identified the main database tables.

✅ Learned users and roles.

✅ Learned document permissions.

✅ Learned conversations and messages.

✅ Learned audit logs.

✅ Understood SQL database vs vector storage.

✅ Connected database design with security and RAG.

✅ Created `docs/Database-Design.md`.

### Project Progress

```text id="8q4p1v"
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
Database Design         ✅
API Design              ⏳
Detailed Architecture   ⏳
Implementation          ⏳
Testing                 ⏳
Deployment              ⏳
Production              ⏳
```

**Next: Session 21 – Database Relationships, Keys, Normalization & Indexes**

We will take our conceptual tables and learn how to design them properly using **primary keys, foreign keys, one-to-many relationships, normalization, constraints, and indexes** before creating the actual database.
