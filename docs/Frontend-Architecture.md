# Frontend Architecture

## Purpose

The frontend provides a simple interface for employees to interact with the enterprise knowledge assistant.

## Main Screens

1. Login
2. Dashboard
3. AI Chat
4. Conversation History
5. Documents
6. Admin Dashboard

## Main User Flow

Login
→ Dashboard
→ Ask Question
→ RAG Processing
→ Answer + Source
→ Continue Conversation

## Communication

Frontend
→ REST API
→ FastAPI Backend

The frontend never directly accesses the database or LLM.