# Glossary: Policy Engine Curriculum

One-sentence definitions and where each concept is introduced. Use this when you forget a term or need to point someone to the right stage or phase.

**See also:** [Python fundamentals](python_fundamentals.md) for full “what / why / how” and the **Quick reference** table for concept → Python syntax.

---

## Python fundamentals

| Term | Definition | See |
|------|------------|-----|
| **accumulator** | A variable (often a list) you keep outside a loop and update inside it to collect results (e.g. `results = []` then `results.append(...)`). | Fundamentals Stage 10; Phase 1 |
| **block** | A group of statements that belong together, marked by indentation (e.g. the body of an `if` or `for`). | Fundamentals Stages 6, 9 |
| **boolean** | A value that is either `True` or `False`; used for yes/no, pass/fail. | Fundamentals Stage 2 |
| **comment** | A line (or part of a line) starting with `#`; Python ignores it. Used to explain code to humans. | Fundamentals Stage 11 |
| **comparison** | An expression that evaluates to `True` or `False` (e.g. `age >= 18`, `x == y`). | Fundamentals Stage 5 |
| **conditional** | A branch in the program: “if this condition is true, do this; else do that” (`if` / `else`). | Fundamentals Stage 6 |
| **dict** | A mapping from keys to values; used for one record with named fields (e.g. `{"id": 1, "age": 25}`). | Fundamentals Stage 8 |
| **deterministic** | Same inputs always produce the same outputs; no randomness or hidden state that changes the result. | Fundamentals Stage 4; Phase 1 |
| **docstring** | A triple-quoted string right under `def ...` that describes what the function does. | Fundamentals Stage 11 |
| **function** | A named block of code that takes parameters and can return a value; defined with `def name(...):`. | Fundamentals Stage 11 |
| **indentation** | In Python, the spaces at the start of a line define which block the line belongs to; wrong indentation causes errors or wrong behavior. | Fundamentals Stage 6 |
| **list** | An ordered collection of values, written with `[...]`; we use it for “many records.” | Fundamentals Stage 7 |
| **loop (for)** | Code that runs once for each item in a collection (`for item in my_list:`). | Fundamentals Stage 9 |
| **None** | Python’s value meaning “no value” or “not set”; used for optional fields (e.g. no failure reason). | Fundamentals Stage 2; Phase 2+ |
| **parameter** | A name in the function definition that receives an argument when the function is called (e.g. `records` in `def evaluate_age_rule(records):`). | Fundamentals Stage 11 |
| **record** | In this curriculum, one item (e.g. one user) represented as a dict with named fields (id, age, etc.). | Fundamentals Stage 8; Phase 1 |
| **script** | A text file with a `.py` extension that Python can run from top to bottom (e.g. `python3 src/engine.py`). | Fundamentals Stage 1 |
| **type** | The kind of a value: number (int/float), string, boolean, list, dict, etc. Python infers types; you don’t declare them. | Fundamentals Stage 2 |
| **value** | A single piece of data Python can work with (e.g. `18`, `"US"`, `True`). | Fundamentals Stage 2 |
| **variable** | A name that refers to a value; created by `name = value`. | Fundamentals Stage 3 |

---

## Phase 2 — Guard clauses + validation

| Term | Definition | See |
|------|------------|-----|
| **early exit** | Returning (or appending a failure and skipping the rest) as soon as invalid or missing data is detected. | Phase 2 |
| **guard clause** | A check at the start of a function that returns immediately with a clear result when something is wrong (e.g. missing field). | Phase 2 |
| **KeyError** | The error Python raises when you use `record["key"]` and that key is not in the dict. | Fundamentals Stage 8; Phase 2 |
| **validation** | Checks that data is present, has the right type, and is in an allowed range *before* running any business rule. | Phase 2 |
| **structured failure** | A result that says *what* failed (e.g. `{"valid": False, "reason": "missing age"}`), not just True/False. | Phase 2 |

---

## Phase 3 — Rule composition

| Term | Definition | See |
|------|------------|-----|
| **failure accumulation** | Running all rules and collecting every failure reason (no short-circuit) so the caller gets a full list. | Phase 3 |
| **priority ordering** | Evaluating rules in a defined order so combined results and reasons are deterministic and ordered (e.g. by business priority). | Phase 3 |
| **rule function** | A function that takes a (validated) record and returns a structured result (e.g. passed/failed + reason); one function per rule. | Phase 3 |
| **structured return** | Every rule returns the same shape (e.g. `{"passed": True}` or `{"passed": False, "reason": "..."}`) so composition is uniform. | Phase 3 |

---

## Phase 4 — Decomposition

| Term | Definition | See |
|------|------------|-----|
| **evaluation** | The “run all rules and combine results” logic only; no I/O, no validation, no formatting. | Phase 4 |
| **function boundaries** | Giving each function one responsibility (e.g. validate, evaluate, format) so logic is testable and reusable. | Phase 4 |
| **orchestration** | Top-level flow that calls validate → evaluate → format in order and passes data between them; no business logic inside. | Phase 4 |
| **separation of concerns** | Validation = “is the data usable?”; evaluation = “does it pass the rules?”; formatting = “how do we return it?” | Phase 4 |

---

## Phase 5 — Stateful CLI

| Term | Definition | See |
|------|------------|-----|
| **command loop** | Read a command from the user (e.g. add, list, eval, quit); repeat until quit. | Phase 5 |
| **controlled mutation** | One in-memory store (e.g. list of users) that only changes in response to explicit commands; no hidden updates. | Phase 5 |
| **dispatch** | Matching the user’s command to the right handler (e.g. if `add` then call add logic). | Phase 5 |
| **I/O at the edge** | Reading and printing happen only in the CLI (or API) layer; rules and validation take data and return data—no `print` inside them. | Phase 4–5; Charter |

---

## Charter and cross-cutting

| Term | Definition | See |
|------|------------|-----|
| **pure (rule/function)** | No side effects: no mutation of shared state, no printing, no I/O inside the rule; same inputs → same return value. | Fundamentals Stage 4; Charter |
| **explainable decision** | The system can return not just allow/deny but reasons (e.g. list of failure reasons) for auditing and support. | Charter; Phases 2–3 |

---

## Common errors (reading tracebacks)

| Term | Meaning |
|------|--------|
| **NameError** | A variable was used before it was assigned or the name is misspelled. |
| **KeyError** | A dict was accessed with a key that doesn’t exist (e.g. `record["age"]` when `"age"` is missing). |
| **IndentationError** | Spaces/tabs are wrong or mixed; Python uses indentation to define blocks. |
| **SyntaxError** | Invalid Python (e.g. missing `:` after `if`/`for`/`def`, or mismatched brackets). |
| **traceback** | The stack of lines Python prints when an error occurs; the last lines show the error type, message, file, and line number. |

---

Back to [Curriculum overview](curriculum_overview.md) · [Python fundamentals](python_fundamentals.md)
