# Session 22 – Actual Database Schema Design

## Duration

30 Minutes

## Objective

Convert our conceptual database design into a **detailed technical blueprint** containing tables, columns, relationships, primary keys, foreign keys, constraints, and indexes.

---

# Task 1 – Roles Table

Stores the roles available in our application.

```text
roles
-------------------------
id
name
description
created_at
```

Possible roles:

```text
Employee
HR
Manager
Admin
```

Important constraints:

```text
id   → PRIMARY KEY
name → UNIQUE + NOT NULL
```

---

# Task 2 – Users Table

Stores registered users.

```text
users
-------------------------
id
name
email
password_hash
role_id
is_active
created_at
updated_at
```

Relationship:

```text
users.role_id
      ↓
roles.id
```

Important:

> We store a **password hash**, never a plain-text password.

Constraints:

```text
id            → PRIMARY KEY
email         → UNIQUE + NOT NULL
password_hash → NOT NULL
role_id       → FOREIGN KEY
```

---

# Task 3 – Documents Table

Stores information about uploaded enterprise documents.

```text
documents
-------------------------
id
file_name
file_path
document_type
department
uploaded_by
status
created_at
updated_at
```

Relationship:

```text
uploaded_by
     ↓
users.id
```

Possible statuses:

```text
uploaded
processing
processed
failed
```

---

# Task 4 – Document Permissions

Controls which roles can access documents.

```text
document_permissions
-------------------------
id
document_id
role_id
access_type
created_at
```

Relationships:

```text
document_id → documents.id
role_id     → roles.id
```

Example:

```text
LeavePolicy.pdf
   ↓
Employee → Read
HR       → Read
Admin    → Read
```

We should prevent duplicate permissions using a constraint such as:

```text
UNIQUE(document_id, role_id)
```

---

# Task 5 – Conversations

Stores employee chat sessions.

```text
conversations
-------------------------
id
user_id
title
created_at
updated_at
```

Relationship:

```text
user_id → users.id
```

One user can have many conversations:

```text
User
 ↓
Conversation 1
Conversation 2
Conversation 3
```

---

# Task 6 – Messages

Stores individual conversation messages.

```text
messages
-------------------------
id
conversation_id
role
content
created_at
```

Relationship:

```text
conversation_id
       ↓
conversations.id
```

Possible roles:

```text
user
assistant
system
```

Example:

```text
Conversation
     ↓
User:      How many casual leaves?
Assistant: You receive 12 casual leaves.
```

---

# Task 7 – Audit Logs

Stores important system activities.

```text
audit_logs
-------------------------
id
user_id
action
resource_type
resource_id
created_at
```

Relationship:

```text
user_id → users.id
```

Possible actions:

```text
LOGIN
LOGOUT
DOCUMENT_UPLOAD
DOCUMENT_ACCESS
DOCUMENT_DELETE
```

Sensitive document content should not unnecessarily be stored in audit logs.

---

# Complete Database Structure

```text
                         ROLES
                           │
                           │ 1:M
                           ▼
                         USERS
                      /     │      \
                     /      │       \
                   1:M     1:M       1:M
                   ▼        ▼         ▼
          CONVERSATIONS  DOCUMENTS  AUDIT_LOGS
                │             │
                │ 1:M         │ 1:M
                ▼             ▼
             MESSAGES   DOCUMENT_PERMISSIONS
                              │
                              │ M:1
                              ▼
                             ROLES
```

---

# How It Supports RAG

When an employee asks:

> **"How many casual leaves can I take?"**

The application can conceptually perform:

```text
Find User
   ↓
Find Role
   ↓
Check Document Permissions
   ↓
Retrieve Allowed Document Chunks
   ↓
Send Context to LLM
   ↓
Generate Answer
   ↓
Save Conversation
   ↓
Record Important Activity
```

This shows how the **database, security, chat system, and RAG system work together**.

---

# Key Learning

A database schema is the technical blueprint of our database.

Our relational database manages:

```text
Users
Roles
Documents
Permissions
Conversations
Messages
Audit Logs
```

while the vector system manages:

```text
Document Chunks
Embeddings
Metadata
```

They have different responsibilities but work together in our application.

---

# Session Outcome

✅ Designed the `roles` table.

✅ Designed the `users` table.

✅ Designed the `documents` table.

✅ Designed document permissions.

✅ Designed conversations and messages.

✅ Designed audit logs.

✅ Defined major relationships.

✅ Defined important constraints.

✅ Updated `Database-Design.md`.

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
Database Design         ✅
DB Relationships        ✅
Database Schema         ✅
API Design              ⏳
Implementation          ⏳
Testing                 ⏳
Deployment              ⏳
Production              ⏳
```

### Next — Session 23

**API Design**

We'll design how the frontend communicates with the backend using APIs, including **HTTP methods, endpoints, request/response formats, authentication, status codes, and error handling**.
