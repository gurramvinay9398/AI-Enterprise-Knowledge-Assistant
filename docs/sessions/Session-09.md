# Session 09 – Understanding LLMs and Introduction to RAG

## Duration

30 Minutes

## Objective

Understand **Large Language Models (LLMs)**, their capabilities and limitations, and why our AI Enterprise Knowledge Assistant needs **RAG (Retrieval-Augmented Generation)**.

---

# Task 1 – What is an LLM?

An **LLM (Large Language Model)** is an AI model trained on a large amount of text that can understand and generate human-like language.

An LLM can:

* Understand natural-language questions.
* Generate human-readable answers.
* Summarize information.
* Explain concepts.
* Follow instructions.
* Maintain conversational context.

Basic flow:

```text
User Question
      ↓
LLM Understands Language
      ↓
Processes Available Context
      ↓
Generates Answer
```

---

# Task 2 – Limitation of an LLM

An LLM does **not automatically know our company's private documents**.

For example, suppose our company document says:

> Employees receive 12 casual leaves per year.

If we ask a general LLM:

> "How many casual leaves does our company provide?"

It may not know the company's actual policy and could provide an incorrect or generic answer.

This can lead to **AI hallucination**, where the model produces information that is unsupported or incorrect.

Therefore:

**LLM alone ≠ Enterprise Knowledge Assistant**

---

# Task 3 – Understanding RAG

**RAG = Retrieval-Augmented Generation**

It combines information retrieval with an LLM.

### Retrieval

Find relevant information from company documents.

### Augmentation

Provide that retrieved information to the LLM as context.

### Generation

The LLM uses that context to generate the final answer.

Example:

```text
Employee Question
       ↓
Retrieve Relevant Document
       ↓
Company Leave Policy
       ↓
Give Relevant Content to LLM
       ↓
Generate Answer
       ↓
Answer + Source Reference
```

Example answer:

> According to the company leave policy, employees receive 12 casual leaves per year.

**Source:** Employee Leave Policy.pdf

---

# Key Learning

The most important concept learned today is:

> **The LLM provides language intelligence, while RAG provides access to the company's knowledge.**

RAG helps make answers more **relevant, grounded, and traceable** to enterprise documents.

---

# Session Outcome

✅ Understood LLMs.

✅ Understood LLM capabilities.

✅ Learned about hallucinations.

✅ Understood why an LLM alone is insufficient.

✅ Learned Retrieval-Augmented Generation.

✅ Understood Retrieval → Augmentation → Generation.

### Next Learning Path

```text
LLM
 ↓
Embeddings
 ↓
Semantic Search
 ↓
Vector Database
 ↓
RAG Pipeline
 ↓
Prompt Engineering
 ↓
RAG Evaluation
 ↓
Production AI System
```

**Next Session:** We will learn **Embeddings**—how text is converted into numerical representations so that computers can understand semantic meaning and find relevant information.
