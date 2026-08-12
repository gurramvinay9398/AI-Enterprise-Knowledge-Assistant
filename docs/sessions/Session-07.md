# Session 07 – Assumptions and Constraints

## Duration

30 Minutes

## Objective

Understand **Assumptions** and **Constraints** in software development and complete the final sections of our initial SRS.

---

## Task 1 – Understanding Assumptions

An **assumption** is something we expect to be true while developing or using the application.

For our AI Enterprise Knowledge Assistant, we identified:

* **A-01:** Users are expected to have internet access.
* **A-02:** Users are expected to have valid credentials and permissions.
* **A-03:** The company will provide legitimate and relevant enterprise documents.
* **A-04:** Uploaded documents will contain readable information.
* **A-05:** Required AI services will be available when needed.
* **A-06:** Users will access only information they are authorized to see.

### Simple Example

> Users have internet access.

We expect this to be true, but it is not something our application controls.

---

## Task 2 – Understanding Constraints

A **constraint** is a limitation or restriction that affects how we build or operate the project.

Important constraints identified:

* **C-01:** Development must work with our Windows 8.1 environment.
* **C-02:** Local hardware resources are limited.
* **C-03:** Large AI models may not be practical to run locally.
* **C-04:** Cloud AI services may therefore be required.
* **C-05:** AI APIs can have usage limits, rate limits, or costs.
* **C-06:** Enterprise data requires strong security and privacy.
* **C-07:** The first release will be an MVP with limited scope.

---

## Task 3 – Important Difference

### Assumption

Something we **expect to be true**.

Example:

> Users have internet access.

### Constraint

Something that **limits our options**.

Example:

> Our laptop has limited resources for running large AI models.

Understanding this difference helps us make realistic technical decisions.

---

## Key Learning

Before development, engineers must understand not only **what the client wants**, but also the conditions and limitations under which the product must be built.

Our constraints will later influence our technology choices, AI architecture, deployment strategy, and overall system design.

---

# Session Outcome

✅ Understood assumptions.

✅ Understood constraints.

✅ Added both sections to `docs/SRS.md`.

✅ Considered our actual development environment.

✅ Completed the initial SRS requirements phase.

### Current SRS Status

**Sections 1–10 → ✅ Completed**

We now have a clear understanding of:

**What we are building → Why we are building it → What it must do → How well it should work → What limitations we have.**

**Next phase: System Design** — we'll start deciding how the frontend, backend, database, LLM, RAG pipeline, vector database, authentication, and deployment will work together.
