# Supplemental learning (optional, in phase order)

This document lists **optional** external resources in the **same order as the curriculum**. Use them only if you want more practice or broader Python exposure. They are **not required** and must not replace the main path: [Python overview: Day 1](python_overview_day1.md) → [Phase 1](curriculum/phase_1_deterministic_evaluation.md) → … → Phase 6.

**Rule:** Complete each curriculum step in order. Use a supplemental resource only when it’s listed for your current (or completed) phase, and only in the order given below.

---

## Phase order summary

| Curriculum position | Supplemental recommendations (do in this order if you use them) |
|---------------------|------------------------------------------------------------------|
| **Before Phase 1** (Day 1) | 1) 30 Days of Python Days 1–4 (syntax, types, operators, strings). 2) 30 Days Day 5 (lists) and Day 8 (dictionaries). |
| **After Phase 1** | 1) CodingBat Python Warmup-1, List-1. 2) Practice Python exercises 1–15. 3) Optional: 30 Days Days 9–11 (conditionals, loops, functions). |
| **After Phase 2** | 1) 30 Days Day 17 (exception handling) — reference only; we use explicit returns, not exceptions, in rules. |
| **After Phase 3** | (Optional) More “multiple conditions” practice: CodingBat Logic-1, or Practice Python exercises 16–25. |
| **After Phase 4** | No specific supplement; optional re-read of 30 Days Day 11 (functions) for boundaries. |
| **After Phase 5** | No specific supplement. |
| **Phase 6** | No supplement; rebuild from scratch only. |

---

## Before Phase 1: Python overview (Day 1)

You are here when: you are working through [Python overview: Day 1](python_overview_day1.md) (Stages 0–11 and the Phase 1 mapping table).

**Supplemental order (optional):**

1. **30 Days of Python — Days 1–4**  
   [GitHub: Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python)  
   - **Day 1:** Introduction, environment, syntax, indentation, comments, data types. Use only as extra exposure; our Day 1 is tailored to Phase 1.  
   - **Day 2:** Variables, built-in functions.  
   - **Day 3:** Operators (arithmetic, comparison, logical).  
   - **Day 4:** Strings (we use strings for keys and messages; deep dive only if you need it).  

2. **30 Days of Python — Days 5 and 8**  
   - **Day 5:** Lists (more exercises on lists; aligns with our lists + loop).  
   - **Day 8:** Dictionaries (more exercises on dicts; aligns with our records).  

**Do not use yet:** 30 Days Days 6–7 (tuples, sets), 12–14 (modules, list comprehensions, higher-order functions), or 21+ (classes, web, APIs). We don’t use those in this course; they can distract from the phase order.

---

## Phase 1 — Deterministic evaluation

You are here when: you are in or have completed [Phase 1](curriculum/phase_1_deterministic_evaluation.md) (one rule, many records, loop, conditional, accumulator, structured result).

**Supplemental order (optional):**

1. **CodingBat — Python**  
   [codingbat.com/python](https://codingbat.com/python)  
   - Do **Warmup-1** (simple conditionals and returns).  
   - Then **List-1** (lists, loops, no dicts).  
   Use these for same primitives (conditionals, loops) in a different context.  

2. **Practice Python**  
   [practicepython.org](https://www.practicepython.org/)  
   - Do exercises **1–15** in order (variables, conditionals, loops, lists, functions).  
   Stop if you feel confident; no need to finish all before Phase 2.  

3. **30 Days of Python — Days 9–11 (optional)**  
   - **Day 9:** Conditionals.  
   - **Day 10:** Loops.  
   - **Day 11:** Functions.  
   Only if you want more syntax and exercises on these; our Phase 1 already covers what you need.  

**If stuck on one concept:** Do that topic in CodingBat or Practice Python (e.g. “loops” or “lists”), then return to the next hour or phase.

---

## Phase 2 — Guard clauses + validation

You are here when: you are in or have completed [Phase 2](curriculum/phase_2_guard_clauses_validation.md) (validation first, guard clauses, structured failure).

**Supplemental order (optional):**

1. **30 Days of Python — Day 17 (exception handling)**  
   Use as **reference only**. In this course we use explicit validation and return failure structures, not `try/except` inside rule logic. Reading Day 17 helps if you see exceptions elsewhere; do not switch to exceptions inside your policy rules.

**No other supplemental** for Phase 2; focus on guard clauses and distinct validation vs rule failure.

---

## Phase 3 — Rule composition

You are here when: you are in or have completed [Phase 3](curriculum/phase_3_rule_composition.md) (multi-rule, allow/deny, ordered reasons).

**Supplemental order (optional):**

1. **CodingBat — Logic-1**  
   More “multiple conditions” style problems in a different context.  

2. **Practice Python — exercises 16–25**  
   Slightly harder problems that still use conditionals, loops, and functions.  

Use only if you want extra practice combining conditions; not required.

---

## Phase 4 — Decomposition

You are here when: you are in or have completed [Phase 4](curriculum/phase_4_decomposition.md) (validate → evaluate → format, orchestration).

**Supplemental:** None required. Optionally re-read **30 Days of Python Day 11 (functions)** if you want to reinforce function boundaries and parameters; our phase doc and canonical example are the main source.

---

## Phase 5 — Stateful CLI

You are here when: you are in or have completed [Phase 5](curriculum/phase_5_stateful_cli.md) (command loop, dispatch, I/O at the edge).

**Supplemental:** None. The phase and canonical example are sufficient.

---

## Phase 6 — Rebuild

You are here when: you are doing [Phase 6](curriculum_overview.md#phase-6--rebuild-hours-2930) (rebuild from scratch).

**Supplemental:** None. Do not use external exercises or code during rebuild; the goal is to reproduce the core engine from memory.

---

## Out of scope for this course (do not mix in)

To keep the curriculum in spec and avoid overwhelm, **do not** treat the following as part of this course’s path, even if you find them in 30 Days of Python or elsewhere:

- **List comprehensions, higher-order functions** — Charter: no clever one-liners, no premature abstraction.  
- **Classes and OOP** — Charter: no classes unless clearly required.  
- **Web, APIs, pandas, MongoDB** — Out of scope; different learning goals.  
- **Replacing our Day 1 with 30 Days Day 1** — Our Day 1 is tailored to Phase 1; follow it first.

If you want to explore those later, do so **after** you finish Phase 6 and the rebuild.

---

## Quick reference: links

| Resource | URL | Use for |
|----------|-----|--------|
| 30 Days of Python | https://github.com/Asabeneh/30-Days-Of-Python | Optional syntax & exercises; follow phase order above. |
| CodingBat Python | https://codingbat.com/python | Same primitives, different problems (Warmup-1, List-1, Logic-1). |
| Practice Python | https://www.practicepython.org/ | Beginner exercises 1–25 in order. |

---

Back to [Curriculum overview](curriculum_overview.md).
