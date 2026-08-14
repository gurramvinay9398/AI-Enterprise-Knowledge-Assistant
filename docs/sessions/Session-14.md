# Session 14 – Prompt Engineering & Context Construction

## Duration

30 Minutes

## Objective

Understand how to design prompts for our RAG system so the LLM generates **simple, relevant, grounded, and reliable answers** using enterprise documents.

---

# Task 1 – What is Prompt Engineering?

A **prompt** is the instruction and information provided to an LLM.

**Prompt engineering** means designing these instructions carefully so the LLM behaves as required.

For our project, the prompt should tell the AI:

* What role it has.
* How it should answer.
* What information it should use.
* What it should avoid.
* What to do when information is unavailable.

---

# Task 2 – RAG Prompt Structure

Our future prompt will conceptually contain:

```text id="7f3a2p"
SYSTEM INSTRUCTIONS

You are an enterprise knowledge assistant.

Rules:
- Answer using the provided context.
- Use simple English.
- Don't invent company policies.
- If information is unavailable, say so.
- Mention sources when available.

CONTEXT

[Relevant document chunk 1]
[Relevant document chunk 2]

USER QUESTION

How many casual leaves can I take?
```

The LLM uses the retrieved context to generate the answer.

---

# Task 3 – Grounded Answers

**Grounding** means generating an answer based on the information supplied by the retrieval system rather than unsupported assumptions.

Suppose the document says:

> Employees receive 12 casual leaves per year.

### Good answer:

> According to the employee leave policy, employees receive 12 casual leaves per year.

### Bad answer:

> Employees receive 15 casual leaves per year.

The second answer is unsupported because **15 wasn't present in the retrieved information**.

---

# Task 4 – Missing Information

If the user asks something that isn't available in the documents, the system shouldn't force an answer.

Example:

> "I couldn't find sufficient information about international relocation in the available company documents."

This helps reduce unsupported AI responses.

---

# Task 5 – Context Construction

Context construction means preparing the relevant retrieved information before sending it to the LLM.

```text id="7v6w1b"
User Question
      ↓
Retrieve Relevant Chunks
      ↓
Combine Relevant Context
      ↓
Build Prompt
      ↓
Send Context + Question to LLM
      ↓
Generate Answer
```

---

# Task 6 – Conversation Context

Our assistant should also handle follow-up questions.

Example:

**User:** How many casual leaves can I take?

**AI:** You can take 12 casual leaves per year.

**User:** Can I carry them to next year?

The system needs conversation context to understand that **"them" refers to casual leaves**.

---

# Key Learning

The important concept is:

> **RAG isn't just retrieving information. We must construct useful context and provide clear instructions to the LLM so it generates a grounded answer based on enterprise information.**

---

# Session Outcome

✅ Learned prompt engineering.

✅ Understood RAG prompt structure.

✅ Learned grounding.

✅ Learned how to handle missing information.

✅ Understood context construction.

✅ Understood the importance of conversation history.

✅ Added prompt/context flow to `Architecture.md`.

### Current Progress

```text id="9b1m2c"
LLM                    ✅
Embeddings             ✅
Semantic Search        ✅
Document Chunking      ✅
Vector Database        ✅
Complete RAG           ✅
Prompt Engineering     ✅
Context Construction   ✅
Retrieval Strategies   ⏳
RAG Evaluation         ⏳
Security               ⏳
Implementation         ⏳
Production AI          ⏳
```

**Next:** Learn **Retrieval Strategies — Top-K retrieval, similarity thresholds, metadata filtering, hybrid search, and reranking.**
