# Curriculum overview: 30-Hour Backend Fluency CLI

This document is the map. Each phase has its own detailed curriculum and a canonical example. **Assume no prior Python;** concepts are introduced in context.

**Before Phase 1:** If you have zero Python experience, work through **[Python overview: Day 1](python_overview_day1.md)**. It defines every concept you need (values, variables, deterministic, conditionals, lists, loops, accumulators, functions) in clear stages—what each is, why we use it, how we use it—and maps them to the Phase 1 example. For a one-place lookup of terms, see the **[Glossary](GLOSSARY.md)**. Then start Phase 1.

**Avoiding overwhelm:** This course is 30 hours of content with no required prior Python. To avoid burnout, use **session boundaries** instead of doing whole phases in one sitting. See **[Recommended pacing](#recommended-pacing-and-session-boundaries)** below and the full comparison to other 0-to-fluency courses in **[CURRICULUM_EVALUATION.md](CURRICULUM_EVALUATION.md)**.

---

## Recommended pacing and session boundaries

Use these as default stop/resume points. Each session is roughly 1–2 hours.

| Session | Content | Stop after |
|---------|---------|------------|
| 1 | Day 1: Stage 0 + Stages 1–4 | Environment, script, values, variables, deterministic. |
| 2 | Day 1: Stages 5–11 + Phase 1 mapping | Comparisons through functions; map canonical example. |
| 3 | Phase 1 Hours 1–2 | One record, variable, conditional, single outcome. |
| 4 | Phase 1 Hours 3–4 | List of records, for-loop, list of outcomes. |
| 5 | Phase 1 Hours 5–6 | Accumulator, full function, return list. **Phase 1 complete.** |
| 6–7 | Phase 2 (Hours 7–12) | Guard clauses, validation, structured failure. |
| 8–9 | Phase 3 (Hours 13–18) | Rule composition, multi-rule, reasons. |
| 10 | Phase 4 (Hours 19–22) | Decomposition, validate → evaluate → format. |
| 11–12 | Phase 5 (Hours 23–28) | Stateful CLI, command loop, I/O at edge. |
| 13 | Phase 6 (Hours 29–30) | Rebuild from scratch. |

**Rule of thumb:** If you have less than ~1.5 hours, do only the next sub-chunk (e.g. Phase 1 Hours 1–2, or Phase 2 Hours 7–8) and stop. After each phase, take a short break before starting the next.

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
2. Use **[Recommended pacing](#recommended-pacing-and-session-boundaries)** so you don’t do whole phases in one sitting.
3. Start with [Phase 1](curriculum/phase_1_deterministic_evaluation.md); read the phase doc and the [Phase 1 canonical example](canonical_examples/phase_1_canonical_example.md).
4. Implement the phase in `src/engine.py` (or as directed); get critique.
5. Proceed through phases 2–5 in order; each builds on the previous.
6. For Phase 6, put the code in `rebuild/scratch.py` and do not copy from the main engine.

See the [charter](charter.md) for non-negotiables and definition of progress. For a comparison to courses like 30 Days of Java and what was added to reduce overwhelm, see [CURRICULUM_EVALUATION.md](CURRICULUM_EVALUATION.md).
