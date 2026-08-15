# Database Design

## Purpose

The relational database stores structured application information such as users, roles, documents, permissions, conversations, messages, and audit activities.

## Initial Tables

- users
- roles
- documents
- document_permissions
- conversations
- messages
- audit_logs

## Design Principle

The relational database manages application and transactional data, while vector storage/search manages embeddings and semantic document retrieval.

## Primary Keys

Each main table will have a unique primary key.

## Foreign Keys

Foreign keys will maintain relationships between related tables.

## Main Relationships

- Role → Users = One-to-Many
- User → Conversations = One-to-Many
- Conversation → Messages = One-to-Many
- Role → Document Permissions = One-to-Many
- Document → Document Permissions = One-to-Many

## Normalization

The database will avoid unnecessary duplication by separating entities such as users, roles, documents, conversations, and messages into dedicated tables.

## Constraints

The database will use appropriate PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, and CHECK constraints to maintain data integrity.

## Indexing

Indexes will be added to frequently queried columns based on actual application access patterns.

## Detailed Schema

### roles

- id
- name
- description
- created_at

### users

- id
- name
- email
- password_hash
- role_id
- is_active
- created_at
- updated_at

### documents

- id
- file_name
- file_path
- document_type
- department
- uploaded_by
- status
- created_at
- updated_at

### document_permissions

- id
- document_id
- role_id
- access_type
- created_at

### conversations

- id
- user_id
- title
- created_at
- updated_at

### messages

- id
- conversation_id
- role
- content
- created_at

### audit_logs

- id
- user_id
- action
- resource_type
- resource_id
- created_at
