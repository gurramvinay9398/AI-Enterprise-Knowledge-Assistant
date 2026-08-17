# Backend Architecture

## Principle

The backend follows separation of concerns so that HTTP handling, validation, business logic, database access, AI/RAG processing, and infrastructure are maintained separately.

## Layers

API
→ HTTP endpoints

Schemas
→ Request/response validation

Services
→ Business logic

Repositories
→ Database operations

Models
→ Database entities

RAG
→ Document processing, retrieval, prompting and AI pipeline

Core
→ Configuration, security and database infrastructure

Our initial backend structure:

backend/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── api/
│   │   ├── auth.py
│   │   ├── documents.py
│   │   ├── chat.py
│   │   └── conversations.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── document.py
│   │   ├── chat.py
│   │   └── conversation.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── document.py
│   │   ├── conversation.py
│   │   └── message.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── document_service.py
│   │   ├── chat_service.py
│   │   └── conversation_service.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   ├── document_repository.py
│   │   └── conversation_repository.py
│   │
│   ├── rag/
│   │   ├── ingestion.py
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── retrieval.py
│   │   ├── prompts.py
│   │   └── pipeline.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   │
│   └── utils/
│       └── helpers.py
│
├── tests/
│
├── requirements.txt
├── .env
└── README.md