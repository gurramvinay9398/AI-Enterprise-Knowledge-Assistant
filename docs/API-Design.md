# API Design

## Purpose

The API layer provides communication between the frontend and backend.

## Base Structure

Frontend
→ REST API
→ FastAPI Backend
→ Database / RAG / LLM

## Authentication

POST /api/auth/register
POST /api/auth/login
POST /api/auth/logout
GET /api/auth/me

## Documents

POST /api/documents/upload
GET /api/documents
GET /api/documents/{id}
DELETE /api/documents/{id}

## Chat

POST /api/chat

## Conversations

GET /api/conversations
POST /api/conversations
GET /api/conversations/{id}
DELETE /api/conversations/{id}

## API Contract

Each API defines:

- HTTP method
- Endpoint
- Authentication requirement
- Request format
- Validation rules
- Response format
- Error responses

## Standard Error Format

{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message"
  }
}

## Main API Contracts

### POST /api/auth/login

Purpose:
Authenticate a user.

### POST /api/documents/upload

Purpose:
Upload an authorized enterprise document.

### POST /api/chat

Purpose:
Ask a question and receive a grounded answer with document references.

### GET /api/documents

Purpose:
Retrieve documents accessible to the authenticated user.

### GET /api/conversations

Purpose:
Retrieve the user's conversation history.