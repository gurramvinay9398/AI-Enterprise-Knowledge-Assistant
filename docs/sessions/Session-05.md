# Session 05 – Functional Requirements

## Duration

30 Minutes

## Objective

Understand **Functional Requirements** and define what the AI Enterprise Knowledge Assistant must do from the user's and business perspective.

---

# Task 1 – Understanding Functional Requirements

A functional requirement describes a **specific action or capability that the system must provide**.

Example:

> The system shall allow authorized users to upload enterprise documents.

It describes **what the system should do**, not how we will technically implement it.

For example:

* Requirement: Retrieve relevant information from documents.
* Implementation: Use embeddings, vector search, and RAG.

Implementation decisions will be made later during System Design.

---

# Task 2 – Functional Requirements Defined

We created 12 functional requirements:

### FR-01 – User Registration and Login

Allow authorized users to securely access the system.

### FR-02 – Document Upload

Allow authorized users to upload supported enterprise documents.

### FR-03 – Document Processing

Process uploaded documents and prepare their content for retrieval.

### FR-04 – Question Submission

Allow users to ask questions using natural language.

### FR-05 – Relevant Information Retrieval

Search enterprise knowledge and retrieve information relevant to the question.

### FR-06 – AI Answer Generation

Generate simple, clear, and relevant answers using retrieved information.

### FR-07 – Document References

Show the source documents used to generate the answer.

### FR-08 – Chat Interface

Provide an interactive interface for communicating with the AI assistant.

### FR-09 – Conversation History

Store and display previous conversations.

### FR-10 – Admin Dashboard

Allow administrators to manage users, documents, and system activity.

### FR-11 – Access Control

Provide appropriate permissions for employees and administrators.

### FR-12 – Error Handling and Notifications

Provide meaningful messages when operations succeed or fail.

---

# Task 3 – Complete User Flow

The main workflow is:

User Login → Documents → Processing → Question → Information Retrieval → AI Answer → Document Reference → Conversation History

---

# Key Learning

Functional requirements define **what the application must do**. They act as a bridge between business requirements and technical system design.

---

# Session Outcome

✅ Understood functional requirements.

✅ Defined 12 functional requirements.

✅ Created the complete user flow.

✅ Distinguished requirements from implementation.

The next step is defining **Non-Functional Requirements**, including security, performance, scalability, reliability, and usability.
