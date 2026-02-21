# Reference curriculum: Phase 5 — Stateful CLI (tutor walkthrough)

This document is a **reference curriculum** for Phase 5: explicit, step-by-step code with heavy comments for the **command loop**, **dispatch**, **in-memory store**, and **I/O at the edge**. Every example is runnable. No shortcuts—one concept at a time.

**Prerequisite:** You have completed Phases 1–4 and the [Phase 1](REFERENCE_CURRICULUM_PHASE1.md) through [Phase 4](REFERENCE_CURRICULUM_PHASE4.md) references. You have `validate`, `evaluate`, `format_result`, and `run_policy(record, rules)` from Phase 4.

**How to use:** Read each section; run the code (copy into a file or use the [single runnable file](reference_phase5_examples.py)). The comments explain *what this line does* and *why we write it this way*.

**Tied to:** [Phase 5 — Stateful CLI](curriculum/phase_5_stateful_cli.md) and [Phase 5 canonical example](canonical_examples/phase_5_canonical_example.md).

---

## 1. Reading a line and splitting into command and args

The user types a line like `add 1 25 true US` or `list` or `eval 1`. We need the **command** (first word) and the **arguments** (rest of the words). We use `line.split()` to get a list of words; the first is the command, the rest are args.

```python
# In a real CLI we'd get the line from input(). For this example we use a string
# so you can run it without typing. Same idea: one line of text from the user.
line = "add 1 25 true US"

# split() breaks the line on whitespace. We get a list of strings.
parts = line.split()
# parts is ["add", "1", "25", "true", "US"]

# The first element is the command name. We use .lower() so "ADD" and "add" are the same.
command = parts[0].lower()
# command is "add"

# Everything after the first element is the arguments for that command.
args = parts[1:] if len(parts) > 1 else []
# args is ["1", "25", "true", "US"]

print("command:", command)
print("args:", args)

# Another example: "list" has no arguments.
line2 = "list"
parts2 = line2.split()
command2 = parts2[0].lower()
args2 = parts2[1:] if len(parts2) > 1 else []
print("command2:", command2, "args2:", args2)
```

**What we just did:** We took one line of text and turned it into a command and a list of arguments. The CLI will do this for every line the user types.

---

## 2. Command loop: repeat until quit

A **command loop** runs forever until the user says to stop. We use `while True:` and `break` when the command is `quit`. Each time through the loop we read a line (or get the next line from a list when we're simulating), parse it, and will later dispatch to the right handler.

```python
# We'll simulate three "lines" from the user so the loop runs a few times then quits.
# In the real CLI you'd use: line = input("> ").strip()
simulated_lines = ["list", "add 1 25 true US", "quit"]

for line in simulated_lines:
    line = line.strip()
    if not line:
        continue

    parts = line.split()
    command = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []

    # If the user said quit, we exit the loop. break stops the loop immediately.
    if command == "quit":
        print("bye")
        break

    # For now we just echo what we got. Next we'll dispatch to add/list/eval.
    print("Got command:", command, "args:", args)
```

**What we just did:** We had a loop that parses each line and stops on `quit`. The structure is: get line → parse → if quit then break → else handle command. In the full CLI we'll replace "handle command" with dispatch.

---

## 3. In-memory store: one list, mutated only by add

**Controlled mutation** means we have one place that holds our data (e.g. a list of users) and it **only changes** when we run a specific command (add). The list command only **reads** the store; it never appends or removes. That way we always know what changes state and what doesn't.

```python
# The store lives at module or main scope. It's a list of records (dicts).
# Only the "add" handler will append to this list. "list" and "eval" only read.
users = []

# Simulate adding one user: build the record and append. This is the ONLY place we mutate users.
record = {"id": "1", "age": 25, "verified": True, "region": "US"}
users.append(record)
print("After one add, users:", users)

# Simulate adding another. Again we only append—no other code touches users.
record2 = {"id": "2", "age": 17, "verified": False, "region": "UK"}
users.append(record2)
print("After two adds, len(users):", len(users))

# "list" would only iterate and read. We never do users.append(...) in list logic.
```

**What we just did:** We have one list that holds all users. We only add to it in one place (the add handler). That's controlled mutation—easy to reason about and test.

---

## 4. handle_add: parse args, build record, append to store

The **add** command takes arguments: id, age, verified, region. We parse the args (and handle errors like missing args or non-numeric age), build one record dict, append it to the store, and return a message. The CLI will print that message. No printing inside handle_add—we return a string.

```python
# The store. In the full CLI this is shared; here we use a list we can pass or use at module level.
users = []


def handle_add(args):
    """
    args: list of strings, e.g. ["1", "25", "true", "US"].
    We append one record to the store and return a message. No print here—return only.
    """
    if len(args) < 4:
        return "add requires: id age verified region"

    user_id = args[0]

    # Age must be a number. If the user types "twenty", int() raises ValueError.
    try:
        age = int(args[1])
    except ValueError:
        return "age must be a number"

    # Convert "true"/"1"/"yes" to True, anything else to False.
    verified = args[2].lower() in ("true", "1", "yes")
    region = args[3]

    record = {"id": user_id, "age": age, "verified": verified, "region": region}
    users.append(record)  # Only place we mutate the store.
    return "added " + str(user_id)


# Try it. We pass args as a list of strings, same as we get from line.split()[1:].
print(handle_add(["u1", "25", "true", "US"]))
print(handle_add(["u2", "17", "false", "UK"]))
print("users now:", users)
print(handle_add(["u3"]))  # Too few args → error message
```

**What we just did:** One function that handles the add command: validate args, build record, append to store, return a string. The CLI layer will print that string. I/O stays at the edge.

---

## 5. handle_list: read the store, format and return

The **list** command doesn't change the store. It iterates over the list of users and builds a string (one line per user) to return. The CLI will print that string. Again, no print inside the handler—we return data so the same logic could be used by an API that returns JSON.

```python
# Assume users already has some records (from previous example or from handle_add).


def handle_list(store):
    """
    Read-only: iterate the store and format each user into a string.
    store is the list of user records. We don't modify it.
    """
    if not store:
        return "no users"

    lines = []
    for u in store:
        # One line per user: id, age, verified, region.
        line = f"id={u['id']} age={u['age']} verified={u['verified']} region={u['region']}"
        lines.append(line)
    return "\n".join(lines)


print("--- handle_list ---")
print(handle_list(users))
```

**What we just did:** handle_list only reads the store and returns a formatted string. No mutation. The caller (the command loop) prints the result.

---

## 6. handle_eval: find user by id, run policy pipeline, return result

The **eval** command takes a user id. We look up that user in the store. If not found, we return an error message. If found, we run the **full policy pipeline** (validate → evaluate → format) using the same `run_policy(record, rules)` from Phase 4. We return the formatted string. We do **not** put print or input inside validate, evaluate, or rules—they only get data and return data.

```python
# We need run_policy and rules from Phase 4. For this example we define a minimal
# validate, evaluate, format_result, run_policy and one rule so the file runs standalone.
def validate(record):
    if "age" not in record:
        return {"valid": False, "reason": "missing age"}
    if not isinstance(record["age"], (int, float)):
        return {"valid": False, "reason": "age not a number"}
    if record["age"] < 0 or record["age"] > 120:
        return {"valid": False, "reason": "age out of range"}
    return {"valid": True}


def rule_age(record):
    if record.get("age", 0) >= 18:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "age below minimum"}


def evaluate(record, rules):
    reasons = []
    for rule_fn in rules:
        result = rule_fn(record)
        if not result["passed"]:
            reasons.append(result["reason"])
    return {"allowed": len(reasons) == 0, "reasons": reasons}


def format_result(decision):
    if "valid" in decision and not decision["valid"]:
        return "Validation failed: " + decision["reason"]
    if decision["allowed"]:
        return "Allowed"
    return "Denied: " + "; ".join(decision["reasons"])


def run_policy(record, rules):
    validation = validate(record)
    if not validation["valid"]:
        return format_result(validation)
    decision = evaluate(record, rules)
    return format_result(decision)


rules = [rule_age]


def handle_eval(args, store, run_policy_fn, rules_list):
    """
    args: e.g. ["1"]. Look up user by id in store; run full policy pipeline; return string.
    run_policy_fn(record, rules) is from Phase 4—validate, evaluate, format. No I/O inside it.
    """
    if not args:
        return "eval requires: user_id"

    user_id = args[0]
    record = None
    for u in store:
        if str(u["id"]) == str(user_id):
            record = u
            break

    if record is None:
        return "user not found: " + user_id

    # Same pipeline as everywhere else: validate → evaluate → format. No print here.
    return run_policy_fn(record, rules_list)


# Try it. users has u1 (age 25) and u2 (age 17) from earlier.
print("--- handle_eval ---")
print("eval u1:", handle_eval(["u1"], users, run_policy, rules))
print("eval u2:", handle_eval(["u2"], users, run_policy, rules))
print("eval 99:", handle_eval(["99"], users, run_policy, rules))
```

**What we just did:** handle_eval finds the user, then calls the same run_policy we use everywhere. No duplicate rule logic—I/O at the edge, logic in one place.

---

## 7. Dispatch: match command to handler

**Dispatch** means: look at the command name and call the right function. We use a chain of `if command == "quit": ... elif command == "add": ... elif command == "list": ... elif command == "eval": ... else: unknown`. Each branch does one thing and returns or breaks. The command loop only does: parse line → dispatch → print result (or break).

```python
# Dispatch is just a series of checks. We've already built handle_add, handle_list, handle_eval.
# The loop does:
#   if command == "quit": break
#   elif command == "add": print(handle_add(args))
#   elif command == "list": print(handle_list(users))
#   elif command == "eval": print(handle_eval(args, users, run_policy, rules))
#   else: print("unknown command: " + command)
#
# So adding a new command (e.g. "delete") means one new elif and one new handler. Clear and predictable.
print("--- Dispatch (concept) ---")
print("One if/elif per command; each calls a handler and prints the returned string.")
```

**What we just did:** We stated the dispatch pattern. One place lists all commands; each command has one handler. The loop stays short and readable.

---

## 8. I/O at the edge: input and print only in the loop

**I/O at the edge** means: reading from the user (`input`) and writing to the user (`print`) happen only in the CLI layer—the command loop and the code that calls it. The handlers (handle_add, handle_list, handle_eval) **return** strings; they don't print. Validate, evaluate, format, and rules don't print or read input; they take data and return data. So we can reuse the same validate/evaluate/format from an API or a test; only the way we get the next line and show the result changes.

```python
# Good:
#   main_cli: line = input("> "); ... print(handle_add(args))
#   handle_add: return "added " + str(user_id)
#   run_policy: return format_result(...)  (returns string)
#
# Bad:
#   handle_add: print("added")  ← I/O inside handler; can't reuse in API
#   validate: print("invalid")   ← I/O inside core logic; can't test without capturing stdout
print("--- I/O at the edge (concept) ---")
print("input/print only in the command loop; handlers and run_policy return values.")
```

**What we just did:** We reinforced the boundary: CLI does I/O; everything else returns data. That's the Phase 5 pattern.

---

## 9. Full example: command loop + dispatch + store (Phase 5 style)

This matches the [Phase 5 canonical example](canonical_examples/phase_5_canonical_example.md). We have one store; handle_add mutates it; handle_list and handle_eval only read. The loop parses each line, dispatches, and prints the handler's return value. We use a **simulated** list of lines so you can run the script and see all output without typing—in a real CLI you'd use `line = input("> ").strip()` instead of iterating over simulated_lines.

```python
# See reference_phase5_examples.py for the full runnable version: main_cli that either
# runs interactively (input) or runs a simulated session (list of lines). Same handlers,
# same store, same run_policy. I/O at the edge; controlled mutation in one place.
```

**What we just did:** We described the full Phase 5 CLI. The runnable file implements it and runs a simulated session so every example runs to completion and you see add, list, eval, and quit in order.

---

## All examples in one runnable file

The file [reference_phase5_examples.py](reference_phase5_examples.py) contains all of the above in order. It ends with a **simulated session**: a list of command lines is fed into the loop so you see the same behavior as typing add/list/eval/quit without waiting for input. Run:

```bash
python3 reference_phase5_examples.py
```

Use it as a reference when implementing Phase 5 in `src/engine.py`.

**Previous:** [REFERENCE_CURRICULUM_PHASE4.md](REFERENCE_CURRICULUM_PHASE4.md) (Phase 4: decomposition). **Next:** Phase 6 is rebuild from scratch; no reference curriculum (you rebuild without the reference).

---

Back to [Phase 5 curriculum](curriculum/phase_5_stateful_cli.md) · [Curriculum overview](curriculum_overview.md).
