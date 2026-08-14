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