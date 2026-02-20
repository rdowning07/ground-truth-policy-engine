# Phase 2 — Guard clauses + validation (Hours 7–12)

## Why this phase matters in industry

Production systems receive incomplete or invalid data: missing fields, wrong types, out-of-range values. If you run business rules on bad data, you get wrong decisions and hard-to-debug errors. **Validation first** means: check that the record has everything needed and that values are valid *before* applying any eligibility or business rule. **Guard clauses** are simple checks at the start of a function that exit early with a clear reason when something is wrong. This pattern reduces nested conditionals and makes “why was I denied?” explicit—critical for compliance and support.

---

## What you will learn (primitives)

- **Guard clauses** — “If X is wrong, return failure immediately; otherwise continue.” No deep nesting.
- **Validation** — Checks such as: field present? correct type? in allowed range? Required before any business rule runs.
- **Early exit** — Return (or append a failure and skip the rest) as soon as you detect invalid or missing data.
- **Structured failure** — Return a result that says *what* failed (e.g. `{"valid": False, "reason": "missing age"}`), not just True/False.

By the end of Phase 2 you will **deny safely on missing/invalid data** and **return validation failures distinctly** from rule failures.

---

## Business necessity and best practices

| Practice | Why it matters |
|----------|----------------|
| Validate before evaluating rules | Prevents garbage-in/garbage-out; avoids crashes and wrong approvals/denials. |
| Guard clauses at the top | Makes invalid paths obvious; avoids “arrow code” and nested if/else. |
| Distinct validation vs rule failure | Support and auditing need to know “missing field” vs “failed age rule.” |
| No silent defaults for missing data | Filling in defaults (e.g. age = 0) hides bugs; fail explicitly instead. |

---

## Session format (every time)

1. **Primitive lesson** — Guard clauses, validation, early exit.
2. **Business paragraph** — Scenario with missing or invalid data (e.g. “User may have no age, or age may be negative”).
3. **Implement translation** — You write validation first, then the rule; return structured failures.
4. **Critique + tighten** — Ensure invalid data never reaches the rule; ensure failure reasons are explicit.

---

## Hour-by-hour guide

### Hours 7–8: Guard clause pattern

- Learn: **early return** — at the start of a function, `if not condition: return failure_result`.
- **Business scenario:** “A user record must have an `age` field. If it’s missing, return a validation failure and do not run any rule.”
- **Output:** A function that returns either `{"valid": False, "reason": "missing age"}` or proceeds to the next check. No nested ifs for “if valid then …”.

### Hours 9–10: Multiple guards and types

- Learn: **multiple guard clauses** in sequence (missing field? wrong type? out of range?).
- **Business scenario:** “User must have `age` present, be a number, and be between 0 and 120. Otherwise return a specific validation reason.”
- **Output:** One validation function that returns either `{"valid": True}` or `{"valid": False, "reason": "..."}` with a distinct reason per failure.

### Hours 11–12: Validation + one rule, structured output

- Learn: **orchestration** — first call validation; if invalid, return validation result; if valid, run the rule and return rule result.
- **Business scenario:** “For each user, first validate (age present, number, 0–120). If invalid, add a validation failure to the results. If valid, run the ‘age >= 18’ rule and add that result.”
- **Output:** Deny safely on missing/invalid data; return validation failures distinctly from “failed rule” (e.g. `reason: "missing age"` vs `reason: "age below minimum"`).

---

## Success criteria for Phase 2

- You can write guard clauses that return immediately when data is invalid or incomplete.
- You can validate presence, type, and range before running any business rule.
- You can return structured validation failures (e.g. `valid: False`, `reason: "..."`) distinct from rule failures.
- You can explain why validation runs *before* the rule and why we don’t substitute defaults for missing data.

---

## Canonical example

See **[Phase 2 canonical example](../canonical_examples/phase_2_canonical_example.md)** for a full validation pipeline with guard clauses and distinct failure reasons. For a tutor-style walkthrough with verbose, commented code, see **[REFERENCE_CURRICULUM_PHASE2.md](../REFERENCE_CURRICULUM_PHASE2.md)** and **[reference_phase2_examples.py](../reference_phase2_examples.py)**.

---

## Link to overview

Back to [Curriculum overview](../curriculum_overview.md).
