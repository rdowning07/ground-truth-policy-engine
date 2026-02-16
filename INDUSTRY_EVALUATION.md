# Industry evaluation: This curriculum’s place and what else jr devs need

This document evaluates where the 30-Hour Policy Engine curriculum sits in the industry and what additional learning is typically needed for other common junior developer positions.

---

## This curriculum’s place in industry

### What it is

A **narrow, deep foundation** in turning business rules into deterministic Python: one rule over many records, validation before evaluation, guard clauses, rule composition, decomposition (validate → evaluate → format), and a small stateful CLI. The goal is **structural fluency**—translate a business paragraph into the right primitives, place loops and conditionals correctly, and produce explainable, auditable decisions—not to ship a product or use frameworks.

### Where it fits

| Dimension | This curriculum |
|-----------|------------------|
| **Domain** | Backend logic for **eligibility, policy, compliance, risk, underwriting**. |
| **Pattern** | “One rule (or many rules), many records, structured yes/no and reasons per record.” |
| **Industries** | Marketplaces (seller/listing eligibility), fintech (underwriting, fraud scoring), billing (subscription checks), access control, internal tools (support CLIs, backoffice). |
| **Level** | **Pre-junior to early junior.** After this, a learner can read a spec (“users must be 18+, verified, and not in a restricted region”), implement it in Python with validation and clear failure reasons, and explain their code. That is exactly what many teams need from a new hire on a rules or eligibility squad. |
| **Artifact** | In-memory CLI: add/list/evaluate. No database, no HTTP, no APIs, no frontend. |

### What it prepares you for (directly)

- **Interviews** that ask you to “implement this rule over a list of records” or “evaluate eligibility and return reasons.”
- **Onboarding** to a team that owns policy, eligibility, underwriting, or rule engines: you already know the “validate first, then evaluate, return structured results” pattern.
- **Contributing** to a rules engine, internal tool, or batch job that applies business logic to records—once someone shows you where the data comes from (DB, API) and where it goes (API, file, UI).
- **Reading and extending** existing rule code: guard clauses, composition, and decomposition will look familiar.

### What it does not cover (by design)

- **HTTP, REST, web APIs** — No servers, no request/response.
- **Databases** — No SQL, no ORM, no persistence; data is in-memory (list of dicts).
- **Testing** — No pytest or test-driven workflow; critique is human.
- **Deployment, infra, CI/CD** — None.
- **Frontend** — None.
- **Frameworks** — Charter: no frameworks; primitives only.
- **Classes/OOP** — Only if clearly required; the course stays procedural/functional.

So: this curriculum is **one slice of backend work**—the “business rule → deterministic code” slice. It is intentionally not a full “backend developer” or “full-stack” course.

---

## How it compares to typical jr dev job descriptions

Many “Junior Backend Developer” or “Junior Software Engineer” roles list:

- Programming in Python (or similar) ✓ — This course builds Python fluency for rule logic.
- APIs, REST, databases — ✗ Not in this course.
- Testing (unit, integration) — ✗ Not in this course.
- Git, collaboration — ✗ Not in this course (assumed elsewhere or on the job).
- “Business logic,” “eligibility,” “rules” — ✓ This course is aimed here.

So: **for a generic “jr backend” role**, this course gives you the “logic” part and a clear mental model (validate → evaluate → format, guard clauses, explainable decisions). It does **not** by itself make you “job ready” for roles that expect HTTP + DB + tests from day one. It **does** make you a strong fit for roles that are **rule-heavy** (eligibility, policy, underwriting, compliance) where the rest (APIs, DB, tests) can be taught on the job or in a follow-on track.

---

## What else is needed for other junior positions

Below: common jr dev positions, what **this curriculum gives** toward that role, and what **you still need** to add (in a typical hiring bar).

| Position | What this curriculum gives | What else is typically needed |
|----------|----------------------------|--------------------------------|
| **Jr backend (rules / eligibility / policy)** | Core competency: translate rules to code, validation, guard clauses, composition, decomposition. Fits underwriting, marketplaces, fintech policy teams. | Persistence (DB or service call), how rules are invoked (API, job, event). Often taught on the job. Testing (pytest) recommended as next step. |
| **Jr backend (web / API)** | Clean functions, structured data, validate-before-use mindset. Good foundation for “service layer” logic. | **HTTP/REST** (Flask, FastAPI, or similar). **Database** (SQL + ORM or client). **Auth** (tokens, sessions). **Testing** (pytest, maybe integration tests). **Env/config** (e.g. 12-factor). |
| **Jr full-stack** | Same as jr backend (web); plus discipline about “logic in one place, I/O at the edge.” | Everything for jr backend (web) **plus** frontend: HTML/CSS/JS, and often a framework (React, Vue, etc.). |
| **Jr data / analytics engineer** | Structured thinking, “one result per record,” handling bad data (validation), deterministic behavior. | **SQL** (queries, schema). **Pipelines** (batch/stream). **Tooling** (dbt, Spark, pandas, or similar). Idempotency, backfills. |
| **Jr platform / DevOps** | None directly; course is app logic, not infra. | **Containers** (Docker). **CI/CD** (GitHub Actions, etc.). **Observability** (logs, metrics). **Scripting** (the Python from this course can help here). |
| **Jr QA / SDET** | Understanding of “one rule, many records” and failure reasons helps design test cases. | **Test automation** (pytest, Playwright/Selenium, etc.). **Coverage**, test design. This course has no testing curriculum. |
| **Jr mobile** | Not applicable; different stack. | Mobile framework (e.g. React Native, Swift, Kotlin), platform APIs, app lifecycle. |

---

## Recommended “next steps” by target role

If the learner has a target role in mind, this course can be followed by a **focused next step** so they don’t wander.

- **Staying in rules/eligibility/policy:**  
  Add: **pytest** for the engine (e.g. “given this list of records, assert this output”). Then: how your company loads records (DB, API) and where results go (API response, event, file). Optional: a minimal HTTP API (e.g. FastAPI) that calls the same functions.

- **Moving toward jr backend (web):**  
  Add: **HTTP and one framework** (e.g. FastAPI or Flask), **database** (SQL + SQLAlchemy or similar), **testing** (pytest). Build one small “API that uses your rule logic” so the engine is the core and the API is the edge.

- **Moving toward jr full-stack:**  
  Same as jr backend (web), then **frontend** (HTML/CSS/JS + one framework). Keep the habit: business logic in Python (or shared layer); UI only displays and sends data.

- **Moving toward jr data/analytics eng:**  
  Add: **SQL** (SELECT, JOINs, filters), then **pandas** or **dbt** for transformations. The “validate → transform → output” and “one result per record” mindset from this course transfers; add data tooling and idempotency.

---

## Summary

| Question | Answer |
|----------|--------|
| **Where does this curriculum sit in industry?** | Foundation for **backend rule logic** in eligibility, policy, compliance, underwriting, and internal tools. Pre-junior to early junior; strong fit for rule-heavy teams. |
| **Is it “enough” for a jr dev job?** | For a **rules/eligibility/policy** jr role: it’s a strong core; add tests and how data gets in/out. For **generic jr backend (web)** or **full-stack**: no—add HTTP, DB, testing, and (for full-stack) frontend. |
| **What’s the main gap for other jr positions?** | **Web/API backend:** HTTP, DB, auth, pytest. **Full-stack:** plus frontend. **Data eng:** SQL, pipelines, tooling. **Platform/DevOps:** infra, CI/CD, containers. **QA/SDET:** test automation and design. |
| **Best use of this course** | First backend course for someone aiming at **rules/eligibility** or as the **“logic slice”** of a broader jr backend path, with a clear next step (tests, API, or DB) chosen by target role. |

---

Back to [Curriculum overview](curriculum_overview.md).
