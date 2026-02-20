# Phase 3 — Rule composition (Hours 13–18)

## Why this phase matters in industry

Real eligibility or compliance logic is almost never “one rule.” It’s “must be 18+ **and** have a verified account **and** not be in a restricted region.” Each rule is a separate concern; the system must **combine** their results into one allow/deny decision and often return **all** reasons for denial (for appeals, support, and compliance). Doing this with clear, composable rule functions and a single place that aggregates results is standard practice in underwriting, access control, and risk engines.

---

## What you will learn (primitives)

- **Rule functions** — One function per rule: takes a (validated) record, returns a structured result (e.g. passed/failed + reason).
- **Structured returns** — Every rule returns the same shape (e.g. `{"passed": True}` or `{"passed": False, "reason": "..."}`).
- **Failure accumulation** — Run *all* rules (no short-circuit); collect every failure reason.
- **Priority ordering** — Evaluate rules in a defined order so that combined results (e.g. deny + list of reasons) are deterministic and ordered (e.g. by business priority).

By the end of Phase 3 you will implement **multi-rule evaluation** that produces **allow/deny plus reasons**.

---

## Business necessity and best practices

| Practice | Why it matters |
|----------|----------------|
| One function per rule | Easier to test, document, and change one rule without touching others. |
| Same return shape for every rule | Enables a single composition loop; no special cases per rule. |
| Collect all failures (full evaluation) | User and support need “all reasons I was denied”; compliance needs a full picture. |
| Priority ordering of rules/reasons | Ensures consistent messaging (e.g. “age” before “region”) and predictable behavior. |
| Pure rules (no mutation, no I/O) | Rules stay testable and reusable; all side effects live in orchestration. |

---

## Session format (every time)

1. **Primitive lesson** — Rule functions, structured returns, failure accumulation, ordering.
2. **Business paragraph** — Scenario with multiple rules (e.g. age, verification, region).
3. **Implement translation** — You write each rule as a function, then a composer that runs all and aggregates.
4. **Critique + tighten** — Ensure no short-circuit; ensure reasons are collected and ordered.

---

## Hour-by-hour guide

### Hours 13–14: One rule as a function

- Learn: **function** that takes a record and returns `{"passed": True}` or `{"passed": False, "reason": "..."}`.
- **Business scenario:** “Rule: user must be 18+. Implement as a function; same input always gives same output.”
- **Output:** A pure function (no print, no file I/O, no changing the record) that returns the structured result.

### Hours 15–16: Multiple rule functions and a list of rules

- Learn: **list of rule functions** (e.g. `rules = [rule_age, rule_verified, rule_region]`) and a loop that runs each rule.
- **Business scenario:** “We have three rules: age >= 18, account verified, not in restricted region. Implement each as a function; then run all three for a given user.”
- **Output:** Three rule functions plus code that calls each and collects results (e.g. list of `{"passed": ..., "reason": ...}`).

### Hours 17–18: Allow/deny and failure accumulation

- Learn: **allow = all passed**; **deny = any failed**; **reasons = list of failure reasons in rule order**.
- **Business scenario:** “Combine rule results: allow only if every rule passed. If any failed, deny and return all failure reasons in the order the rules were evaluated.”
- **Output:** Multi-rule evaluation producing a single **allow** or **deny** and a list of reasons (e.g. `{"allowed": False, "reasons": ["age below minimum", "account not verified"]}`).

---

## Success criteria for Phase 3

- You can implement each business rule as a separate pure function with a consistent return shape.
- You can run all rules for a record and collect every failure (no short-circuit).
- You can produce one allow/deny decision and an ordered list of reasons.
- You can explain why we collect all failures instead of stopping at the first one.

---

## Canonical example

See **[Phase 3 canonical example](../canonical_examples/phase_3_canonical_example.md)** for multiple rules, structured returns, and full failure accumulation. For a tutor-style walkthrough with verbose, commented code, see **[REFERENCE_CURRICULUM_PHASE3.md](../REFERENCE_CURRICULUM_PHASE3.md)** and **[reference_phase3_examples.py](../reference_phase3_examples.py)**.

---

## Link to overview

Back to [Curriculum overview](../curriculum_overview.md).
