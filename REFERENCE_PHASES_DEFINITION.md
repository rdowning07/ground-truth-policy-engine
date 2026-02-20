# Reference curriculum: what the reference units are and how they map to phases

This document defines the **reference curriculum** units in this repo and how they align with the **phases** of the main curriculum. No new materials are created here—only definitions.

---

## What a reference curriculum unit is

A **reference curriculum** unit is one markdown doc (e.g. `REFERENCE_CURRICULUM_PHASE2.md`) plus a single runnable Python file (e.g. `reference_phase2_examples.py`) that walk through the same concepts with explicit, verbose code and tutor-style comments. Each unit is optional support for learners working through the main curriculum.

---

## Do reference units match phases?

**Yes, with one twist.**

| Reference | Phase(s) | What the reference covers |
|-----------|----------|----------------------------|
| **Phase 1** | **Python fundamentals (pre–Phase 1)** + **Phase 1** | Python fundamentals (script, values, variables, comparisons, conditionals, lists, dicts, loops, accumulators, functions) and the full Phase 1 pattern (one rule, many records). So the Phase 1 reference spans “what you need before Phase 1” and “the Phase 1 canonical example.” |
| **Phase 2** | **Phase 2** | Guard clauses, validation, orchestration (validate then rule), structured failure, distinct kind (validation vs rule). |
| **Phase 3** | **Phase 3** | Rule functions, same return shape, list of rules, failure accumulation, allow/deny with reasons, full composer. |
| **Phase 4** | **Phase 4** | Function boundaries (validate / evaluate / format), orchestration (run_policy), separation of concerns. |
| **Phase 5** | **Phase 5** | Stateful CLI (command loop, dispatch, in-memory store, add/list/eval). *No reference curriculum or examples created yet.* |
| **Phase 6** | **Phase 6** | Rebuild from scratch. *No reference curriculum or examples created yet; the exercise is to rebuild without reference.* |

So:

- **Phase 1 reference** = Python fundamentals + Phase 1 (one unit covers both “prerequisite” and first phase).
- **Phase 2–4 references** = Phases 2–4 one-to-one.
- **Phase 5 reference** = Phase 5 (mapping defined; materials not created).
- **Phase 6 reference** = Phase 6 (mapping defined; materials not created; Phase 6 is “rebuild” so a reference would only state the goal, not step-by-step code).

---

## Summary

- **Reference curriculum** = tutor walkthrough (markdown) + runnable examples (one `.py` file per phase).
- **Phases** are the main curriculum units (curriculum doc + canonical example + implementation in `src/engine.py`).
- **Mapping:** Phase 1 reference ≈ Python fundamentals + Phase 1; Phase 2 reference = Phase 2; Phase 3 = Phase 3; Phase 4 = Phase 4; Phase 5 = Phase 5; Phase 6 = Phase 6.
- **Gap:** Phase 5 and Phase 6 references are defined but have no reference curriculum or example files yet.

---

Back to [Curriculum overview](curriculum_overview.md).
