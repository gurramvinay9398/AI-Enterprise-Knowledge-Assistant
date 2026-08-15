# Session 21 – Database Relationships, Keys, Normalization & Indexes

## Duration

30 Minutes

## Objective

Learn how to convert our basic database design into a **proper, maintainable relational database structure** using primary keys, foreign keys, relationships, normalization, constraints, and indexes.

---

# Task 1 – Primary Key

A **Primary Key (PK)** uniquely identifies every row in a table.

Example:

```text
users
----------------
id ← Primary Key
name
email
role_id
```

Every user should have a unique `id`.

---

# Task 2 – Foreign Key

A **Foreign Key (FK)** connects one table to another.

Example:

```text
roles
---------
id
name

users
---------
id
name
role_id ← Foreign Key
```

`users.role_id` refers to `roles.id`.

This creates:

```text
Role
 ↓
Users
```

---

# Task 3 – Database Relationships

### One-to-One

One record connects to one record.

```text
User → Profile
```

### One-to-Many ⭐

One record connects to many records.

Our project examples:

```text
Role → Users
User → Conversations
Conversation → Messages
```

### Many-to-Many

Many records connect to many records.

Example:

```text
Users ←→ Documents
```

We use an **association/junction table**:

```text
Users
  ↓
Document_Permissions
  ↑
Documents
```

This is important for enterprise document access control.

---

# Task 4 – Normalization

**Normalization** means organizing data to reduce unnecessary duplication and maintain consistency.

### Poor Design

```text
id | name  | role
1  | Vinay | Employee
2  | Rahul | Employee
3  | Ravi  | Employee
```

The role is repeated.

### Better Design

```text
roles

id | name
1  | Employee
2  | HR
3  | Admin
```

Then:

```text
users

id | name  | role_id
1  | Vinay | 1
2  | Rahul | 1
3  | Ravi  | 1
```

### Benefits

* Less duplication.
* Better consistency.
* Easier updates.
* Better data integrity.

---

# Task 5 – Database Constraints

Constraints prevent invalid data.

Important constraints:

### PRIMARY KEY

Uniquely identifies a row.

### FOREIGN KEY

Maintains relationships.

### NOT NULL

Requires a value.

### UNIQUE

Prevents duplicate values.

Example:

```text
email UNIQUE
```

### CHECK

Ensures a value follows a rule.

These constraints help keep our database reliable.

---

# Task 6 – Indexes

An **index** helps the database find frequently searched data more efficiently.

For example:

```text
users.email
```

If the application frequently searches users by email, an index can make that query faster.

Potential indexes:

```text
users.email
users.role_id
documents.department
documents.document_type
conversations.user_id
messages.conversation_id
document_permissions.document_id
document_permissions.role_id
```

### Important

We should **not index every column**.

Indexes:

* Improve certain read operations.
* Consume storage.
* Can make inserts/updates more expensive.

Therefore, indexes should be based on actual query patterns.

---

# Updated Database Relationship

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
                │ 1:M         │
                ▼             ▼
             MESSAGES   DOCUMENT_PERMISSIONS
                              │
                              │ M:1
                              ▼
                             ROLES
```

This is our improved conceptual relational design.

---

# Key Learning

A professional database is not simply a collection of tables.

It uses:

```text
Primary Keys
     +
Foreign Keys
     +
Relationships
     +
Normalization
     +
Constraints
     +
Indexes
```

to maintain **data integrity, consistency, security, and efficient access**.

---

# Session Outcome

✅ Learned primary keys.

✅ Learned foreign keys.

✅ Learned one-to-one, one-to-many, and many-to-many relationships.

✅ Understood association tables.

✅ Learned normalization.

✅ Learned database constraints.

✅ Learned indexes.

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
API Design              ⏳
Detailed Architecture   ⏳
Implementation          ⏳
Testing                 ⏳
Deployment              ⏳
Production              ⏳
```

### Next — Session 22

**Actual Database Schema Design**

We will convert our conceptual design into a detailed schema containing **tables, columns, data types, primary keys, foreign keys, constraints, and indexes** before we write the actual SQL/database code.
