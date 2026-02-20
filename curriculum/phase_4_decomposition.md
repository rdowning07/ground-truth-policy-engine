# Phase 4 — Decomposition (Hours 19–22)

## Why this phase matters in industry

Real systems separate **what** they do from **how** they do it: validate, then evaluate, then format for the caller. That separation makes it possible to test validation without evaluation, change output format without touching rules, and reuse the same logic in CLI, API, or batch jobs. Clear **function boundaries** and **orchestration vs evaluation** are how teams keep backend code maintainable and auditable.

---

## What you will learn (primitives)

- **Function boundaries** — One responsibility per function: e.g. `validate(record)`, `evaluate_rules(record, rules)`, `format_result(decision, reasons)`.
- **Orchestration** — A top-level flow that calls validate → evaluate → format in order and passes data between them (no business logic inside the orchestrator; it only wires steps).
- **Evaluation** — The “run all rules and combine results” logic only; no I/O, no validation, no formatting.
- **Separation of concerns** — Validation deals with “is the data usable?”; evaluation with “does it pass the rules?”; formatting with “how do we return it to the caller?”

By the end of Phase 4 you will have **clean separations**: validate, evaluate, format.

---

## Business necessity and best practices

| Practice | Why it matters |
|----------|----------------|
| Validate / evaluate / format split | Enables testing each part alone; allows different outputs (CLI, API, CSV) from same logic. |
| Orchestration as thin glue | One place to read the flow; changes to order or steps don’t scatter across the codebase. |
| No I/O inside rules or validation | Pure functions are testable without mocks; I/O belongs at the edges (CLI, API). |
| Explicit data flow | Each function takes inputs and returns outputs; no hidden globals—easier to reason about and audit. |

---

## Session format (every time)

1. **Primitive lesson** — Function boundaries, orchestration vs evaluation, separation of concerns.
2. **Business paragraph** — Scenario that implies “validate, then evaluate, then present results.”
3. **Implement translation** — You write distinct validate, evaluate, and format steps; orchestrator calls them in order.
4. **Critique + tighten** — Ensure no mixing of validation, rule logic, and formatting in one function.

---

## Hour-by-hour guide

### Hours 19–20: Extract validate and evaluate

- Learn: **separate functions** — `validate(record)` returns valid/invalid + reason; `evaluate_rules(record, rules)` assumes valid record and returns allow/deny + reasons.
- **Business scenario:** “We already have validation and multi-rule evaluation. Split them so that one function only validates, and another only runs rules. The caller will call validate first; if valid, call evaluate.”
- **Output:** Two clear functions; no validation logic inside the evaluator; no rule logic inside the validator.

### Hours 21: Add format

- Learn: **format function** — Takes the result of evaluation (e.g. allowed, reasons) and returns a string or structure suitable for the caller (e.g. for CLI: “Allowed” or “Denied: reason1; reason2”).
- **Business scenario:** “Our evaluator returns `{"allowed": True}` or `{"allowed": False, "reasons": [...]}`. Add a function that turns that into a human-readable message (or a fixed structure for an API).”
- **Output:** `format_result(decision)` that only does formatting; no evaluation or validation.

### Hour 22: Orchestration

- Learn: **single entry point** — e.g. `run_policy(record, rules)` that: (1) validates; if invalid, returns formatted validation failure; (2) else evaluates; (3) returns formatted evaluation result.
- **Business scenario:** “One function that runs the full pipeline: validate → evaluate (if valid) → format. No business logic in this function—only calling the three steps in order.”
- **Output:** Clean separations: validate, evaluate, format, and a thin orchestrator that ties them together.

---

## Success criteria for Phase 4

- You can name and implement separate validate, evaluate, and format functions.
- You can describe “orchestration” as “calling the right functions in order” with no business logic in the orchestrator.
- You can test (or trace) validate, evaluate, and format independently.
- You can explain why I/O and formatting belong at the edges, not inside rules or validation.

---

## Canonical example

See **[Phase 4 canonical example](../canonical_examples/phase_4_canonical_example.md)** for a decomposed pipeline with validate, evaluate, format, and orchestration. For a tutor-style walkthrough, see **[REFERENCE_CURRICULUM_PHASE4.md](../REFERENCE_CURRICULUM_PHASE4.md)** and **[reference_phase4_examples.py](../reference_phase4_examples.py)**.

---

## Link to overview

Back to [Curriculum overview](../curriculum_overview.md).
