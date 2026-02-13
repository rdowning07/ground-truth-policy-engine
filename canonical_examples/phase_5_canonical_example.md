# Phase 5 — Canonical example: Stateful CLI

## Business paragraph (how it shows up in the wild)

> “Support needs a small tool: add a user (id, age, verified, region), list all users, and run the full eligibility pipeline for a user by id. The tool should run in a loop: read a command, do the action, repeat until the user types quit. All state is in memory (no database). The same validate, evaluate, and format logic we already have must be used—no duplicating rule logic in the CLI.”

---

## What we’re training

- **Command loop:** Read input → parse command → dispatch → repeat until `quit`.
- **Dispatch:** Map command name to the right handler (add, list, eval).
- **Controlled mutation:** One store (e.g. list of users) that only changes when `add` runs.
- **I/O at the edge:** input/print only in the CLI; validate, evaluate, format receive and return data only.

---

## Industry tie-in

- **Same logic everywhere:** CLI, API, and batch can share validate/evaluate/format; only the way we read input and write output changes.
- **Explicit state:** One list, updated only in one place—easy to reason about and test.
- **Scriptable:** Commands can be driven by scripts (e.g. `echo "list" | python engine.py`).

---

## Canonical code (assumes Phase 4: validate, evaluate, format, run_policy)

Store lives at module or main scope; only the add-handler mutates it.

```python
# In-memory store. Only the "add" command should modify this list.
users = []


def handle_add(args):
    """args: [id, age, verified, region]. Append a record to the store."""
    if len(args) < 4:
        return "add requires: id age verified region"
    user_id = args[0]
    try:
        age = int(args[1])
    except ValueError:
        return "age must be a number"
    verified = args[2].lower() in ("true", "1", "yes")
    region = args[3]
    record = {"id": user_id, "age": age, "verified": verified, "region": region}
    users.append(record)
    return "added " + str(user_id)


def handle_list(args):
    """Read-only: iterate the store and format each user."""
    if not users:
        return "no users"
    lines = []
    for u in users:
        lines.append(f"id={u['id']} age={u['age']} verified={u['verified']} region={u['region']}")
    return "\n".join(lines)


def handle_eval(args, rules, run_policy_fn):
    """Look up user by id; run full policy pipeline; return formatted result."""
    if not args:
        return "eval requires: user_id"
    user_id = args[0]
    record = None
    for u in users:
        if str(u["id"]) == str(user_id):
            record = u
            break
    if record is None:
        return "user not found: " + user_id
    return run_policy_fn(record, rules)


def main_cli(rules, run_policy_fn):
    """
    Command loop: read line, split into command + args, dispatch, print result.
    I/O only here; validate/evaluate/format are used via run_policy_fn.
    """
    print("Commands: add <id> <age> <verified> <region> | list | eval <id> | quit")
    while True:
        line = input("> ").strip()
        if not line:
            continue
        parts = line.split()
        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        if command == "quit":
            print("bye")
            break
        elif command == "add":
            print(handle_add(args))
        elif command == "list":
            print(handle_list(args))
        elif command == "eval":
            print(handle_eval(args, rules, run_policy_fn))
        else:
            print("unknown command: " + command)
```

Usage: define `rules` (list of rule functions) and pass `run_policy` from Phase 4; call `main_cli(rules, run_policy)` so that `eval` uses the same pipeline as everywhere else.

---

## Why this is canonical

| Choice | Reason |
|--------|--------|
| Single store, mutated only in add | Controlled mutation; no hidden updates. |
| Dispatch by command name | Easy to add new commands; one place to see all actions. |
| run_policy_fn(record, rules) for eval | Reuses validate → evaluate → format; no duplicate rule logic. |
| I/O only in main_cli and handlers | input/print at the edge; core logic stays pure and testable. |

---

## Link to phase

This example implements the learning goals of [Phase 5 — Stateful CLI](../curriculum/phase_5_stateful_cli.md).
