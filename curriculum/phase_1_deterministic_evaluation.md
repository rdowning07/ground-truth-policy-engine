# Phase 1 — Deterministic evaluation (Hours 1–6)

**Rough time:** Hours 1–2 ≈ 1–2 hours; Hours 3–4 ≈ 1–2 hours; Hours 5–6 ≈ 1–2 hours. **Recommended:** Use three sessions (see [curriculum overview](../curriculum_overview.md#recommended-pacing-and-session-boundaries)). Stop after Hours 2 and after Hours 4; don’t do all 6 hours in one go unless you already have the primitives.

## Why this phase matters in industry

Backend systems constantly answer: *“Does this record satisfy this rule?”* for many records. Billing systems check subscriptions; marketplaces check seller eligibility; fraud systems score transactions. The pattern is always: **one rule, many records, structured yes/no per record**. Doing this in a repeatable, auditable way is a core skill. “Deterministic” means: same inputs always produce the same outputs—no hidden state or randomness. That is required for compliance, debugging, and trust.

---

## What you will learn (primitives)

We assume you have **no prior Python**. Before this phase, complete **[Python overview: Day 1](../python_overview_day1.md)** so you have clear definitions and fluency for: values and types, variables, **deterministic** (what it is, why we require it), comparisons, conditionals, lists, dicts, **loops** (what they are, why we use them, how we use them), **accumulators**, and functions. You will then use only:

- **Values and variables** — storing a single piece of data (e.g. a number, text, or yes/no).
- **Lists** — ordered collections of values (e.g. a list of user records).
- **Loops** — doing the same steps for each item in a list (e.g. “for each user, check one rule”).
- **Conditionals** — branching (if this, do that; else do something else).
- **Accumulators** — a variable you update inside a loop to collect results (e.g. a list of pass/fail outcomes).

By the end of Phase 1 you will **evaluate one rule across many records** and produce a **structured result per record** (e.g. record id + passed/not passed).

---

## Business necessity and best practices

| Practice | Why it matters |
|----------|----------------|
| One rule, many records | Matches how businesses define rules (“all orders over $X”) and how data is stored (rows in a table). |
| Structured results per record | Enables reporting, auditing, and “why was this user denied?” without re-running logic. |
| Deterministic evaluation | Required for regulatory and operational consistency; no “it worked yesterday” surprises. |
| Explicit loop over records | Makes it obvious *where* the rule runs; avoids hidden magic and makes debugging straightforward. |

---

## Session format (every time)

1. **Primitive lesson** — What we’re training (e.g. loops, conditionals, accumulators).
2. **Business paragraph** — How it shows up in the wild (real-world scenario).
3. **Implement translation** — You write the code that turns the paragraph into the primitive.
4. **Critique + tighten** — Review for clarity, correctness, and consistency with the charter.

---

## Hour-by-hour guide

### Hours 1–2: Environment and one record

- Install Python and run a single script (e.g. `python3 src/engine.py`).
- Learn: **variables** (e.g. `age = 25`), **comparisons** (e.g. `age >= 18`), **conditionals** (`if age >= 18: ... else: ...`).
- **Business scenario:** “A user must be at least 18 to access the feature.” Translate to: one variable (age), one check, one outcome (eligible / not eligible).
- **Output:** A single result for a single “record” (e.g. `{"eligible": True}` or `{"eligible": False}`).

**Before you continue:** Can you explain what `age >= 18` evaluates to when `age` is 17? When `age` is 20? If unsure, try it in a tiny script with `print(17 >= 18)` and `print(20 >= 18)`.

### Hours 3–4: Many records and a loop

- Learn: **lists** (e.g. `users = [{"id": 1, "age": 20}, {"id": 2, "age": 17}]`), **for-loops** (`for user in users: ...`).
- **Business scenario:** “For each user in our list, determine if they are at least 18.”
- **Output:** A list of results, one per user (e.g. `[{"id": 1, "eligible": True}, {"id": 2, "eligible": False}]`).

**Before you continue:** Can you write a for-loop that prints each record’s `"id"` from a list `records`? (No rule or accumulator yet.) If you can, you’re ready for Hours 5–6.

### Hours 5–6: Accumulator and structured results

- Learn: **accumulator** — start with an empty list `results = []`, and inside the loop **append** each result: `results.append(...)`.
- **Business scenario:** “Evaluate the same age rule for every user; produce a list of outcomes with user id and pass/fail.”
- **Output:** One function that takes a list of records and returns a list of structured results (e.g. `{"id": 1, "passed": True}`, `{"id": 2, "passed": False}`). No printing inside the rule; return data only.

**If this feels dense:** Hours 5–6 tie together loop, conditional, accumulator, and return. If you’re overloaded: (1) Re-read the [Phase 1 canonical example](../canonical_examples/phase_1_canonical_example.md). (2) Trace one record through the code by hand (e.g. `{"id": 1, "age": 25}`). (3) Implement only the loop and `results.append({"id": record["id"], "passed": True})` for every record; then add the if/else for the real rule.

---

## Success criteria for Phase 1

- You can write a loop that visits every record in a list.
- You can use an **if/else** (or conditional) to decide “passed” vs “not passed” for one rule.
- You can use an **accumulator** (a list you build in the loop) to collect one result per record.
- You can explain *why* the loop is around “evaluate this one rule for this record,” and why the accumulator is outside the loop.

---

## Canonical example

See **[Phase 1 canonical example](../canonical_examples/phase_1_canonical_example.md)** for a full business paragraph, line-by-line translation, and a single-rule, multi-record implementation with zero prior Python assumed.

---

## What you built (recap)

- A **function** that takes a list of records and returns a list of results.
- A **loop** over each record.
- A **conditional** for one rule (e.g. age >= 18) that sets passed True/False.
- An **accumulator** (`results = []` and `results.append(...)`) that collects one result per record and returns the full list.

Before starting Phase 2, take a short break. Next phase adds validation and guard clauses for missing or invalid data.

---

## Link to overview

Back to [Curriculum overview](../curriculum_overview.md).
