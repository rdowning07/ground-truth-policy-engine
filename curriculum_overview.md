# Curriculum overview: 30-Hour Backend Fluency CLI

This document is the map. Each phase has its own detailed curriculum and a canonical example. **Assume no prior Python;** concepts are introduced in context.

**Before Phase 1:** If you have zero Python experience, work through **[Python overview: Day 1](python_overview_day1.md)**. It defines every concept you need (values, variables, deterministic, conditionals, lists, loops, accumulators, functions) in clear stages—what each is, why we use it, how we use it—and maps them to the Phase 1 example. Then start Phase 1.

---

## Session format (every time)

1. **Primitive lesson** — What we’re training (e.g. loops, guards, composition).
2. **Business paragraph** — How it shows up in the wild (real-world scenario).
3. **Implement translation** — Learner writes the code that turns the paragraph into the primitive.
4. **Critique + tighten** — Review for clarity, correctness, and charter alignment.

---

## Phases 1–5 (detailed curricula + canonical examples)

| Phase | Focus | Output | Curriculum | Canonical example |
|-------|--------|--------|------------|-------------------|
| **1** | Deterministic evaluation | One rule across many records; structured result per record | [Phase 1 — Deterministic evaluation](curriculum/phase_1_deterministic_evaluation.md) | [Phase 1 example](canonical_examples/phase_1_canonical_example.md) |
| **2** | Guard clauses + validation | Deny safely on bad data; distinct validation vs rule failures | [Phase 2 — Guard clauses + validation](curriculum/phase_2_guard_clauses_validation.md) | [Phase 2 example](canonical_examples/phase_2_canonical_example.md) |
| **3** | Rule composition | Multi-rule allow/deny + ordered list of reasons | [Phase 3 — Rule composition](curriculum/phase_3_rule_composition.md) | [Phase 3 example](canonical_examples/phase_3_canonical_example.md) |
| **4** | Decomposition | Validate → evaluate → format; thin orchestration | [Phase 4 — Decomposition](curriculum/phase_4_decomposition.md) | [Phase 4 example](canonical_examples/phase_4_canonical_example.md) |
| **5** | Stateful CLI | Add / list / evaluate users; command loop; I/O at the edge | [Phase 5 — Stateful CLI](curriculum/phase_5_stateful_cli.md) | [Phase 5 example](canonical_examples/phase_5_canonical_example.md) |

---

## Phase 6 — Rebuild (Hours 29–30)

- **Primitive:** Rebuild from a blank file without reference.
- **Output:** Reproduce the core engine structure from memory.
- No separate curriculum doc; the exercise is to re-implement the patterns from Phases 1–5 in a fresh file (e.g. `rebuild/scratch.py`).

---

## How to use this curriculum

1. **(Zero Python?)** Do [Python overview: Day 1](python_overview_day1.md) first—stages 1–11 and the Phase 1 mapping table.
2. Start with [Phase 1](curriculum/phase_1_deterministic_evaluation.md); read the phase doc and the [Phase 1 canonical example](canonical_examples/phase_1_canonical_example.md).
3. Implement the phase in `src/engine.py` (or as directed); get critique.
4. Proceed through phases 2–5 in order; each builds on the previous.
5. For Phase 6, put the code in `rebuild/scratch.py` and do not copy from the main engine.

See the [charter](charter.md) for non-negotiables and definition of progress.
