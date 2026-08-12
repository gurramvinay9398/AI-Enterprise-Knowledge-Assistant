# Session 06 – Non-Functional Requirements

## Duration

30 Minutes

## Objective

Understand **Non-Functional Requirements (NFRs)** and define how well the AI Enterprise Knowledge Assistant should operate.

---

# Task 1 – Understanding NFRs

Functional requirements describe **what the system does**, while non-functional requirements describe **how well the system should work**.

Example:

**Functional:**
The system should answer employee questions.

**Non-Functional:**
The system should answer efficiently, securely, reliably, and in a user-friendly manner.

NFRs are important because a system can have all the required features but still be unsuitable for real-world production if it is slow, insecure, unreliable, or difficult to use.

---

# Task 2 – NFR Categories

We defined the following requirements:

### NFR-01: Performance

The system should process queries efficiently and provide responses within a reasonable time.

### NFR-02: Security

User accounts, APIs, documents, and application data should be protected from unauthorized access.

### NFR-03: Scalability

The system should support increasing users, documents, and queries as the company grows.

### NFR-04: Reliability

The system should work consistently and handle errors gracefully.

### NFR-05: Usability

Employees without technical knowledge should easily understand and use the application.

### NFR-06: Maintainability

The code should be modular, organized, documented, and easy to modify.

### NFR-07: Availability

The deployed application should remain accessible to authorized users with minimum downtime.

### NFR-08: Data Privacy

Enterprise documents and user information must remain private and accessible only to authorized users.

### NFR-09: AI Response Quality

Answers should be relevant and grounded in enterprise documents. The system should clearly indicate when sufficient information is unavailable.

### NFR-10: Compatibility

The application should work with the selected development environment and commonly used modern browsers.

---

# Task 3 – Important Difference

**Functional Requirements → What the system does**

**Non-Functional Requirements → How well the system does it**

This distinction is important when designing and testing production applications.

---

# Key Learning

A professional application needs more than features. It must also be secure, reliable, scalable, fast, maintainable, usable, and privacy-focused.

These requirements will later influence our architecture, technology selection, coding practices, testing strategy, and deployment.

---

# Session Outcome

✅ Understood NFRs.

✅ Defined 10 non-functional requirements.

✅ Learned Functional vs Non-Functional Requirements.

✅ Added security, scalability, reliability, privacy, and AI quality considerations.

The SRS now defines both **what our system must do and the quality standards it must meet**.
