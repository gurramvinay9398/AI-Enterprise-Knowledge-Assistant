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