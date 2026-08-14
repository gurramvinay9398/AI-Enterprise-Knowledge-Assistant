# Session 16 – RAG Evaluation & Testing

## Duration

30 Minutes

## Objective

Understand how to **test, measure, and improve** our RAG system so that it produces accurate, relevant, grounded, and reliable answers.

---

# Task 1 – Why RAG Evaluation Is Needed

A RAG pipeline can technically work but still produce incorrect answers.

Example:

**Document:**

> Employees can take 12 casual leaves per year.

**User:**

> How many casual leaves can I take?

**AI:**

> You can take 20 casual leaves.

The pipeline worked:

```text
Question → Retrieval → LLM → Answer
```

But the answer is incorrect.

Therefore:

> **A working RAG pipeline does not automatically mean a reliable RAG system.**

---

# Task 2 – Retrieval Quality

We need to check whether the system retrieves the **correct document chunks**.

Example:

```text
Question:
How many casual leaves can I take?

Expected:
LeavePolicy.pdf → Page 12

Retrieved:
SalaryPolicy.pdf → Page 8
```

The retrieval system failed.

The main question is:

> **Did we retrieve the information required to answer the question?**

---

# Task 3 – Answer Quality

Even when retrieval is correct, the LLM can generate a bad answer.

### Context:

> Employees receive 12 casual leaves per year.

### Good:

> Employees receive 12 casual leaves per year.

### Bad:

> Employees receive 20 casual leaves per year.

Therefore, we must evaluate the final answer separately.

---

# Important Evaluation Dimensions

## 1. Faithfulness / Groundedness

Does the answer remain supported by the retrieved context?

```text
Context:
12 casual leaves

Answer:
Employees receive 12 casual leaves.

→ Grounded ✅
```

If the answer says 20:

```text
→ Not grounded ❌
```

---

## 2. Answer Relevance

Does the answer actually address the user's question?

**Question:**

> How many casual leaves can I take?

**Relevant:**

> You can take 12 casual leaves per year.

**Not relevant:**

> The company provides medical insurance.

---

## 3. Context Relevance

Did the system retrieve information useful for the question?

```text
Question:
How many casual leaves?

Leave Policy → Relevant ✅
Salary Policy → Not relevant ❌
```

---

# Task 4 – Test Dataset

We need a collection of realistic employee questions and expected information.

Example:

| Question                               | Expected Information  | Source          |
| -------------------------------------- | --------------------- | --------------- |
| How many casual leaves are available?  | 12 leaves             | LeavePolicy.pdf |
| What is the WFH policy?                | WFH rules             | WFHPolicy.pdf   |
| How can I claim medical reimbursement? | Reimbursement process | Benefits.pdf    |
| What are office working hours?         | Working hours         | HRPolicy.pdf    |

This dataset will later be used to test our RAG system.

---

# Task 5 – Evaluation Process

```text
Company Documents
      ↓
Create Test Questions
      ↓
Expected Answers / Sources
      ↓
Run RAG System
      ↓
Collect Generated Answers
      ↓
Compare Results
      ↓
Measure Quality
      ↓
Identify Problems
      ↓
Improve System
      ↓
Test Again
```

This is an **iterative process**.

---

# Important Engineering Concept

If an answer is wrong, don't immediately blame the LLM.

The problem could be:

```text
Bad Chunking
     ↓
Bad Embedding
     ↓
Bad Retrieval
     ↓
Wrong Context
     ↓
Wrong Answer
```

Or:

```text
Correct Retrieval
     ↓
Correct Context
     ↓
Bad Prompt
     ↓
Wrong Answer
```

We need to identify **where the failure happened** before fixing it.

---

# Key Learning

> **RAG evaluation checks whether the system retrieves the right information and generates answers that are relevant, accurate, and grounded in enterprise documents.**

The basic engineering cycle is:

```text
Build
 ↓
Test
 ↓
Measure
 ↓
Find Failure
 ↓
Improve
 ↓
Test Again
```

---

# Session Outcome

✅ Understood why RAG evaluation is necessary.

✅ Learned retrieval quality.

✅ Learned answer relevance.

✅ Learned context relevance.

✅ Learned faithfulness/groundedness.

✅ Understood test datasets.

✅ Learned the RAG evaluation process.

### RAG Progress

```text
LLM                    ✅
Embeddings             ✅
Semantic Search        ✅
Document Chunking      ✅
Vector Database        ✅
Complete RAG           ✅
Prompt Engineering     ✅
Context Construction   ✅
Retrieval Strategies   ✅
RAG Evaluation         ✅
Security               ⏳
Technology Selection   ⏳
Implementation         ⏳
Testing                ⏳
Deployment             ⏳
Production AI          ⏳
```

### Next: Session 17

**Enterprise AI Security & Access Control**

We'll learn **authentication, authorization, RBAC, document-level permissions, data privacy, prompt injection, and basic security practices for a client-facing RAG application.**
