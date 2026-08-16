## RAG Architecture

### Document Ingestion

Document
→ Text Extraction
→ Cleaning
→ Chunking
→ Embeddings
→ Vector Database

### Query Processing

User Question
→ Question Embedding
→ Similarity Search
→ Relevant Chunks
→ Context
→ LLM
→ Answer + Source

## Prompt and Context Construction

The system retrieves relevant document chunks and constructs context before sending the request to the LLM.

Flow:

User Question
→ Retrieve Relevant Chunks
→ Construct Context
→ Apply System Instructions
→ Send Context + Question to LLM
→ Generate Grounded Answer

## Retrieval Strategy

The system will use a retrieval pipeline designed to improve relevance and protect enterprise information.

Conceptual flow:

User Question
→ Authentication / Permission Check
→ Metadata Filtering
→ Semantic and/or Keyword Retrieval
→ Top-K Candidates
→ Reranking
→ Relevance Check
→ Context Construction
→ LLM
→ Answer + Source Reference

## RAG Evaluation

The system will be evaluated at multiple stages:

1. Retrieval Quality
2. Context Relevance
3. Answer Relevance
4. Faithfulness / Groundedness
5. Source Accuracy

Evaluation will use a test dataset containing realistic employee questions, expected information, and document references.

The evaluation process will be iterative:

Test → Measure → Identify Failure → Improve → Test Again

## Security Architecture

The system will implement authentication and authorization before document retrieval.

Conceptual flow:

User
→ Authentication
→ Authorization / RBAC
→ Permission Validation
→ Metadata Filtering
→ Semantic Retrieval
→ Allowed Document Chunks
→ Context Construction
→ LLM
→ Grounded Answer
→ Source Reference

### Security Principles

- Users can only access authorized documents.
- Authorization should occur before retrieval.
- Sensitive information should not be unnecessarily exposed.
- Retrieved documents should be treated as data, not trusted instructions.
- Important system actions should be logged securely.

Technology Decision Matrix:

| Component      | Options                          | Decision    |
| -------------- | -------------------------------- | ----------- |
| Frontend       | HTML/CSS/JS, React               | To evaluate |
| Backend        | Python/FastAPI, Java/Spring Boot | To evaluate |
| Database       | SQLite, PostgreSQL               | To evaluate |
| Vector Search  | Local/Dedicated/PostgreSQL       | To evaluate |
| LLM            | Cloud/API                        | To evaluate |
| Embeddings     | Local/API                        | To evaluate |
| Authentication | JWT/session-based                | To evaluate |
| Deployment     | Cloud platform                   | To evaluate |

## Technology Selection

Technology decisions will be based on:

- Project requirements
- Windows 8.1 compatibility
- Hardware limitations
- AI/RAG ecosystem
- Production suitability
- Cost
- Maintainability
- Learning value

No technology will be selected solely because it is currently popular.

Initial API List

Authentication
-------------
POST /api/auth/register
POST /api/auth/login
POST /api/auth/logout
GET  /api/auth/me

Documents
---------
POST   /api/documents/upload
GET    /api/documents
GET    /api/documents/{id}
DELETE /api/documents/{id}

Chat
----
POST /api/chat

Conversations
-------------
GET    /api/conversations
POST   /api/conversations
GET    /api/conversations/{id}
DELETE /api/conversations/{id}
