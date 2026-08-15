# Technology Stack

## Selection Principles

Technology decisions are based on:

- Project requirements
- Windows 8.1 compatibility
- Hardware limitations
- AI/RAG ecosystem
- Production suitability
- Cost
- Maintainability
- Learning value

## Initial Decisions

| Component | Candidate | Status | Reason |
|---|---|---|---|
| Frontend | React | Candidate | Interactive production-style UI |
| Backend | Python + FastAPI | Candidate | Strong AI/RAG ecosystem |
| Database | SQLite | Initial | Lightweight local development |
| Production DB | PostgreSQL | Candidate | Production scalability |
| Vector Search | To evaluate | Open | RAG retrieval requirement |
| LLM | Cloud API | Direction | Local hardware limitation |
| Embeddings | To evaluate | Open | Depends on compatibility/cost |
| Authentication | JWT/secure sessions | To evaluate | Enterprise access control |
| Deployment | Cloud platform | To evaluate | Production requirement |