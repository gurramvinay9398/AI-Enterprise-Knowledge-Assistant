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