# Python fundamentals — What you need before the curriculum

This document is for **zero prior Python**. It defines every concept you will need to read and write the Phase 1 example: what each thing is, why we use it, how we use it, and where it appears in the curriculum. Work through the stages in order; by the end you will have the fluency to start [Phase 1 — Deterministic evaluation](curriculum/phase_1_deterministic_evaluation.md).

---

## How to use this doc

- **Stage 0** gets your environment ready (no code yet). **Stages 1–11** build in order. Each stage adds one idea and ties it to “why we need it for policy/eligibility logic.”
- **“Where you’ll see it”** in each stage points to the curriculum phase and the canonical example so you can cross-check.
- After Stage 11, use **“Mapping the Phase 1 example”** to read the canonical code line by line with the concept that explains it.
- For a compact lookup of “concept → Python syntax,” see **Quick reference** and the [Glossary](GLOSSARY.md).
- For a **reference curriculum** with explicit, verbose code and tutor-style comments for each concept, see [REFERENCE_CURRICULUM_PHASE1.md](REFERENCE_CURRICULUM_PHASE1.md) and the runnable [reference_phase1_examples.py](reference_phase1_examples.py).

---

## Stage 0: Get ready to run Python (environment)

### What it is

Before you run any code, you need **Python installed** and a way to run commands (a **terminal**). The project may also provide a **virtual environment** (e.g. `.venv`)—an isolated copy of Python and packages for this project.

### Why it matters

If Python isn’t installed or you’re in the wrong folder, “run the script” fails and you can’t practice. Doing this once unblocks everything else.

### What to do

1. **Check Python:** Open a terminal and run `python3 --version`. You should see something like `Python 3.11.x`. If you get “command not found,” install Python from [python.org](https://www.python.org/downloads/) or your system package manager.
2. **Find the project folder:** Use `cd` to go to the folder that contains `src` and `curriculum` (e.g. `cd ~/Dev/ground-truth-policy-engine`).
3. **Optional but recommended:** If the project has a `.venv` folder, activate it so you use this project’s Python:
   - On macOS/Linux: `source .venv/bin/activate`
   - On Windows (Command Prompt): `.venv\Scripts\activate.bat`
   - Your prompt may show `(.venv)` when it’s active.
4. **Run the scaffold:** From the project root, run `python3 src/engine.py`. You should see two lines of output. If you do, you’re ready for Stage 1.

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md) Hours 1–2: “Install Python and run a single script.”

---

## Stage 1: Running Python and “a script”

### What it is

A **script** is a text file containing instructions Python can run. You run it from a terminal (e.g. `python3 src/engine.py`). Python executes the instructions from top to bottom and can produce **output** (e.g. text printed to the screen).

### Why you use it

Backend logic lives in scripts (or modules). You need to be able to run your code and see that it does something. No need to understand the inside yet—just: “this file runs, and running it produces a result.”

### How you use it

1. Create a file with a `.py` extension (e.g. `engine.py`).
2. Put one or more lines of Python in it.
3. In a terminal, from the folder that contains the file (or with the path to the file), run: `python3 engine.py` (or `python3 src/engine.py` if the file is in `src/`).

Example: a file containing only `print("hello")` will, when run, output `hello`.

### The entry point: `if __name__ == "__main__":`

In `src/engine.py` you will see:

```python
if __name__ == "__main__":
    main()
```

When you run `python3 src/engine.py`, Python runs the file. The line `if __name__ == "__main__":` means: “run the block below **only when this file is executed**, not when it’s imported by another file.” For this overview, treat it as “this is where execution starts when I run the script.”

### Your first script (do this now)

Create a new file (e.g. `first_script.py` in the project root) with exactly:

```python
age = 20
print("Age is", age)
print("Passes age check?", age >= 18)
```

Run it: `python3 first_script.py`. You should see two lines. Change `20` to `17` and run again; the second line should change. You’ve used a variable, `print`, and a comparison—enough to confirm the environment works.

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md) Hours 1–2: “Install Python and run a single script.”
- You run `python3 src/engine.py` to execute the policy engine.

---

## Stage 2: Values and types (the data we work with)

### What it is

A **value** is a single piece of data Python can work with. Every value has a **type**:

- **Numbers:** integers (e.g. `18`, `25`) and decimals (e.g. `18.5`).
- **Strings:** text in quotes (e.g. `"hello"`, `"US"`).
- **Booleans:** exactly two values, `True` and `False`, used for yes/no, pass/fail, eligible/not eligible.

We use these types because business rules and records are made of numbers (age, amount), text (region, id), and yes/no outcomes (passed, allowed).

### Why you use it

Policy logic compares numbers (e.g. age >= 18), stores text (e.g. region code), and produces clear yes/no results (passed / not passed). Without a clear idea of “value” and “type,” you can’t read expressions like `age >= 18` or `passed = True`.

### How you use it

You don’t “declare” types in Python; you just write values. Python infers the type.

- Number: `18`, `0`, `120`
- String: `"missing age"`, `"US"`
- Boolean: `True`, `False`

**One more value: `None`.** Python has a special value `None` meaning “no value” or “not set.” We use it when a field is optional (e.g. “no failure reason yet”). You’ll see it in Phase 2 and later; for Phase 1 you only need to know it exists.

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md): “values and variables,” “conditionals” (True/False).
- [Phase 1 example](canonical_examples/phase_1_canonical_example.md): `passed = True` and `passed = False`; numbers in `age >= 18`.

---

## Stage 3: Variables (giving a value a name)

### What it is

A **variable** is a name that refers to a value. You create it by writing `name = value`. After that, using `name` in an expression uses that value. You use variables to store inputs, intermediate results, and outputs so you can refer to them and reuse them.

### Why you use it

We need to name the “current record,” “current age,” “current result,” etc. Variables make the code readable and let us pass data from one step to the next (e.g. “get age from the record, then check age >= 18”).

### How you use it

- Assign: `age = 25`, `user_id = record["id"]`, `passed = True`.
- Use: `age >= 18`, `results.append({"id": user_id, "passed": passed})`.

The same variable name can be reassigned later (e.g. in a loop, `passed` might be True for one record and False for the next).

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md): “variables,” “accumulator.”
- [Phase 1 example](canonical_examples/phase_1_canonical_example.md): `user_id`, `age`, `passed`, `results`.

---

## Stage 4: Deterministic (same in → same out)

### What it is

**Deterministic** means: for the same inputs, the program always produces the same outputs. There is no randomness and no hidden state that changes the result. If you run the same rule on the same record again, you get the same answer.

### Why you use it

Compliance, auditing, and debugging require repeatability. “It worked yesterday” and “we can’t reproduce the denial” are unacceptable. Determinism is a requirement for policy and eligibility systems.

### How you use it

- Don’t use random number generators or “current time” inside rule logic.
- Don’t rely on global state that changes between runs in a way that affects the result.
- Keep rules **pure**: same record in → same result out. Reading data from the record and returning a result is deterministic; printing or reading from the keyboard inside the rule is not (and we avoid that).

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md): “Deterministic evaluation” in the industry section and the best-practices table.
- [Phase 1 example](canonical_examples/phase_1_canonical_example.md): “Determinism: same input list must always produce the same output list”; the function only reads the record and returns a result—no print, no I/O.

---

## Stage 5: Comparisons (expressions that produce True or False)

### What it is

A **comparison** is an expression that evaluates to `True` or `False`. You use operators like `==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=`. They are the building blocks of rules: “is age at least 18?” → `age >= 18`.

### Why you use it

Business rules are conditions: “age >= 18,” “verified is True,” “region not in restricted list.” Comparisons turn those conditions into a boolean so we can branch (if/else) or store the outcome (passed = True/False).

### How you use it

- `age >= 18`   → True if age is 18 or more, else False  
- `age == 18`   → True only if age is exactly 18  
- `age != 0`    → True if age is not 0  
- `value in some_list` → True if value is in the list  

Comparisons are used inside conditionals and in assignments (e.g. `passed = age >= 18`).

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md): “comparisons (e.g. age >= 18),” “conditionals.”
- [Phase 1 example](canonical_examples/phase_1_canonical_example.md): `if age >= 18:`.

---

## Stage 6: Conditionals (if / else — branching)

### What it is

A **conditional** is a branch in the program: “if this condition is true, do this; otherwise do that.” In Python you write `if condition:` and optionally `else:`. The code under `if` runs only when the condition is True; the code under `else` runs when it’s False. **Indentation (usually 4 spaces) defines which lines belong to the if or else block.**

**Indentation is part of the syntax.** In Python, indentation isn’t just style—it defines blocks of code. Wrong indentation causes an `IndentationError` or changes what runs. Use **spaces** (typically 4 per level), not tabs, and keep them consistent. The body of an `if`, `else`, or `for` must be indented one level more than the line that starts the block.

### Why you use it

Rules are decisions: “does this record pass or not?” We need to run different code for pass vs fail (e.g. set `passed = True` vs `passed = False`, or append different results). Conditionals are how we express that.

### How you use it

```python
if age >= 18:
    passed = True
else:
    passed = False
```

Or with a single expression: `passed = True if age >= 18 else False`. For clarity we often use the if/else block so the “rule” is obvious.

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md): “conditionals,” “if/else.”
- [Phase 1 example](canonical_examples/phase_1_canonical_example.md): the `if age >= 18: ... else: ...` block that sets `passed`.

---

## Stage 7: Lists (ordered collections)

### What it is

A **list** is an ordered collection of values. It can hold numbers, strings, booleans, or other structures (e.g. dicts). You write a list with square brackets: `[a, b, c]`. You can get the length with `len(my_list)` and get an element by position (index) with `my_list[0]` (first item), `my_list[1]` (second), etc. We use lists to represent “many records” (e.g. many users).

### Why you use it

Business logic often applies the same rule to many records. Those records are stored in an ordered collection; in our curriculum we use a list of records. The loop (Stage 9) will “visit” each element of that list.

### How you use it

- Literal: `[1, 2, 3]`, `[]` (empty list).
- Append: `results.append(value)` adds one value to the end of the list.
- Loop (see Stage 9): `for record in records:` gives you each element as `record`.

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md): “lists,” “accumulator” (a list we build with append).
- [Phase 1 example](canonical_examples/phase_1_canonical_example.md): `results = []`, `results.append(...)`, `for record in records:`.

---

## Stage 8: Dicts (key–value records)

### What it is

A **dict** (dictionary) is a mapping from **keys** to **values**. We use it to represent one **record** (e.g. one user) with named fields: `{"id": 1, "age": 25}`. You read a value by key with square brackets: `record["id"]`, `record["age"]`. You can write a literal dict with curly braces: `{"id": user_id, "passed": passed}`.

### Why you use it

Records in the real world have named fields (id, age, region, verified). A dict is the natural way to represent “one record with named fields” and to pass it into a rule function. Each result we build is also a small record (e.g. id + passed), so we use a dict for that too.

### How you use it

- Literal: `{"id": 1, "age": 25}`, `{"id": user_id, "passed": passed}`.
- Read: `record["id"]`, `record["age"]`. **If the key doesn’t exist,** `record["age"]` causes a `KeyError`. In Phase 2 we handle missing data with guard clauses and patterns like `record.get("age", default)` to avoid that.
- Keys are usually strings; values can be any type (number, string, boolean, list, another dict).

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md): “lists” of “user records” (list of dicts).
- [Phase 1 example](canonical_examples/phase_1_canonical_example.md): `record["id"]`, `record["age"]`, `{"id": user_id, "passed": passed}`; input/output are lists of dicts.

---

## Stage 9: Loops — for (do something for each item)

### What it is

A **loop** is code that runs repeatedly. A **for-loop** runs once **for each item** in a collection (e.g. a list). You write `for item in my_list:` and then indent the block that should run for each item. Inside the block, `item` is the current element (first time through, then second, then third, etc.).

### Why you use it

We have “one rule” and “many records.” We must run the same steps for every record. The loop is the place where we say “for each record, do this.” Without a loop we’d have to copy-paste the same code for every record; with a loop we write it once and Python repeats it for each element. That’s why the curriculum says “explicit loop over records”—so it’s obvious where the rule is applied to each record.

### How you use it

```python
for record in records:
    user_id = record["id"]
    age = record["age"]
    # ... do something with user_id and age
```

The indented block is the “body” of the loop. Everything that must run per record goes inside that block.

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md): “loops,” “for each user, check one rule,” “loop over records.”
- [Phase 1 example](canonical_examples/phase_1_canonical_example.md): `for record in records:` and the indented block that evaluates the rule and appends a result.

---

## Stage 10: Accumulators (building a list inside a loop)

### What it is

An **accumulator** is a variable you use **outside** the loop and **update inside** the loop to collect results. For a list of results, you start with an empty list (`results = []`) and each time through the loop you **append** one new result (`results.append(...)`). When the loop finishes, the accumulator holds “all results we collected.”

### Why you use it

We need to produce “one result per record” in a single list. The loop gives us one record at a time; we compute one result for that record and must add it to a growing list. The accumulator is that growing list. It lives outside the loop so it persists across iterations; we only append inside the loop.

### How you use it

```python
results = []                    # accumulator: start empty
for record in records:
    # ... compute something for this record ...
    results.append(one_result)  # add one result each time
return results                  # full list when loop is done
```

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md): “accumulator,” “results = []”, “results.append(...).”
- [Phase 1 example](canonical_examples/phase_1_canonical_example.md): `results = []` before the loop, `results.append({"id": user_id, "passed": passed})` inside the loop, `return results` after.

---

## Stage 11: Functions (named block: inputs and return)

### What it is

A **function** is a named block of code that takes **inputs** (parameters) and can **return** a value. You define it with `def name(parameter1, parameter2):` and indent the body. You **return** a value with `return something`. Callers use the function by name and pass arguments: `evaluate_age_rule(my_records)`.

**Docstrings and comments.** The triple-quoted string immediately under `def ...` is a **docstring**—it describes what the function does (e.g. `"""One rule: age must be >= 18. ..."""`). Lines starting with `#` are **comments**; Python ignores them. Both help humans (and you) understand the code.

### Why you use it

We want “one job” per function (e.g. “evaluate this one rule over many records”). Functions let us name that job, pass in data (the list of records), and get back a result (the list of outcomes) without duplicating code. Rules and validation will also be functions so we can test and reuse them.

### How you use it

- Define: `def evaluate_age_rule(records):` then indented body ending with `return results`.
- Call: `evaluate_age_rule([{"id": 1, "age": 25}])` → returns the list of results.
- Parameters: `records` is the name used inside the function for whatever list was passed in.

### Where you’ll see it

- [Phase 1](curriculum/phase_1_deterministic_evaluation.md): “One function that takes a list of records and returns a list of structured results.”
- [Phase 1 example](canonical_examples/phase_1_canonical_example.md): the whole of `evaluate_age_rule(records)` and the final `return results`.

---

## Mapping the Phase 1 example (line by line)

After the stages above, open [Phase 1 canonical example](canonical_examples/phase_1_canonical_example.md) and use this map to tie each part of the code to the concept.

| Line(s) / idea | Concept (stage) |
|----------------|------------------|
| `def evaluate_age_rule(records):` | Function (Stage 11): name and parameter. |
| `results = []` | Accumulator (Stage 10): start with empty list. |
| `for record in records:` | Loop (Stage 9): for each record in the list. |
| `user_id = record["id"]`, `age = record["age"]` | Variables (Stage 3) and dict access (Stage 8). |
| `if age >= 18:` | Comparison (Stage 5) and conditional (Stage 6). |
| `passed = True` / `passed = False` | Variables and booleans (Stages 2–3). |
| `results.append({"id": user_id, "passed": passed})` | Accumulator (Stage 10), dict literal (Stage 8). |
| `return results` | Function return (Stage 11). |
| No `print`, no input inside the function | Deterministic, pure rule (Stage 4). |

---

## When something goes wrong (reading errors)

When Python can’t run your code, it prints a **traceback** (a stack of lines) and an **error message**. You don’t have to understand every line; focus on the **last two lines**:

1. **Error type and message** (e.g. `NameError: name 'age' is not defined`, `KeyError: 'age'`).
2. **File and line number** (e.g. `File "src/engine.py", line 12`).

**Common errors and what they usually mean:**

| Error | Likely cause | What to check |
|-------|----------------|----------------|
| `NameError: name 'x' is not defined` | You used a variable before assigning it or you misspelled it. | Assign the variable first (e.g. `age = record["age"]`) or fix the spelling. |
| `KeyError: 'age'` | You used `record["age"]` but that key isn’t in the dict. | Ensure the record has an `"age"` key, or use validation/guard clauses (Phase 2). |
| `IndentationError` | Spaces/tabs are wrong or mixed. | Use 4 spaces per level; no tabs. Make sure the body of `if`/`for`/`def` is indented. |
| `SyntaxError` | Invalid Python (e.g. missing `:`, wrong brackets). | Check the line pointed to; often a missing colon after `if`/`else`/`for`/`def`. |

The traceback lists calls from top (where you ran) to bottom (where the error happened). Use the file and line to find the spot, then the message to decide the fix.

---

## Quick reference: concept → Python (zero coding assumed)

Use this when you know the idea but forget the exact syntax. See the stages above for “why” and “how.”

| Concept | Python form |
|---------|-------------|
| Run a script | `python3 path/to/file.py` |
| Print output | `print("text")` or `print("Age", age)` |
| Integer / number | `18`, `0` |
| Text / string | `"hello"`, `'also a string'` |
| Yes/no value | `True`, `False` |
| No value / not set | `None` |
| Variable (assign) | `name = value` |
| Equal (comparison) | `a == b` |
| Not equal | `a != b` |
| Less than / greater than | `a < b`, `a > b`, `a <= b`, `a >= b` |
| Value in list | `x in my_list` |
| If / else block | `if condition:` then indented block; optional `else:` and indented block |
| Empty list | `[]` |
| List literal | `[a, b, c]` |
| Add to end of list | `my_list.append(value)` |
| Number of items | `len(my_list)` |
| Dict literal | `{"key": value, "key2": value2}` |
| Read from dict | `record["key"]` (key must exist or you get KeyError) |
| Loop over list | `for item in my_list:` then indented block |
| Define function | `def name(param1, param2):` then indented body |
| Return value | `return value` |
| Call function | `name(arg1, arg2)` |
| Comment | `# rest of line ignored` |
| Docstring (under def) | `"""Description of function."""` |

---

## What to do next

1. **Run something.** If you haven’t yet, do **Your first script** under Stage 1; then run `python3 src/engine.py` and confirm you see output.
2. **Re-read Stages 4 (deterministic), 9 (loops), and 10 (accumulators)** so “why we use them” and “how we use them” are clear.
3. **Open the [Phase 1 curriculum](curriculum/phase_1_deterministic_evaluation.md)** and the [Phase 1 canonical example](canonical_examples/phase_1_canonical_example.md); use the mapping table above to label each part of the code with its concept.
4. **Start Phase 1** (Hours 1–6): implement the same pattern yourself in `src/engine.py` for one rule and many records.
5. When you forget a term, use the [Glossary](GLOSSARY.md) or the **Quick reference** table above.

---

## For mentors: Is more “definition → Python” useful for zero experience?

For someone with **zero Python or coding knowledge**, this doc now includes:

- **Stage 0** — Environment and “see it run” before any concepts.
- **First script** — A single copy-paste exercise (variable, `print`, comparison) for an immediate win.
- **Indentation** — Explicit callout that it’s syntax, not style, with a concrete warning (spaces, no tabs).
- **Errors** — “When something goes wrong” with a small table of common errors and what to check.
- **None** — Introduced early so it’s not a surprise in Phase 2+.
- **`if __name__ == "__main__"`** — One sentence so the scaffold file isn’t mysterious.
- **Docstrings and comments** — So triple-quotes and `#` are named when they appear in the canonical example.
- **KeyError / .get()** — Foreshadowed in Stage 8 so missing keys aren’t a blind surprise.
- **Quick reference** — Concept → Python form in one table for “I know the idea but forget the syntax.”
- **Glossary** — One place to re-find terms and see which stage/phase they come from.

**When to add more:** If the intern repeatedly asks “what’s the exact syntax for X?” or gets stuck on the same kind of error, add one row to the Quick reference or one entry to the Glossary and point them there. Avoid expanding the staged narrative with more primitives before Phase 1; the goal is “just enough” to read and write the Phase 1 example. Extra definition/spec (e.g. “what is a type hint?” or “what is a module?”) can be added on demand when a later phase or the codebase introduces it.

Back to [Curriculum overview](curriculum_overview.md).
