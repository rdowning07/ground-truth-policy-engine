# Phase 5 — Stateful CLI (Hours 23–28)

## Why this phase matters in industry

Many backoffice and internal tools are **command-line interfaces** that maintain state (e.g. in-memory store of users or records) and dispatch commands (add, list, evaluate). Keeping **I/O and user interaction** in one place and **business logic** in another ensures the same rules and validation can be reused in APIs or batch jobs. Controlled mutation (e.g. “add user” appends to a list) in a single, explicit place avoids bugs and makes behavior predictable—a standard pattern for admin tools, migration scripts, and support CLIs.

---

## What you will learn (primitives)

- **Command loop** — Read a command from the user (e.g. `add`, `list`, `eval`, `quit`); repeat until quit.
- **Dispatch** — Match the command to the right handler (e.g. if `add` then call add logic; if `list` then call list logic).
- **Controlled mutation** — One in-memory store (e.g. a list of users) that only changes in response to explicit commands (e.g. add); no hidden updates.
- **Separation of I/O and logic** — Reading/printing happens in the CLI layer; validate, evaluate, and format are called with data and return data—no `print` inside rules or validation.

By the end of Phase 5 you will have a **stateful CLI** that can **add** users, **list** users, and **evaluate** policy for a user, with a clear boundary between I/O and core logic.

---

## Business necessity and best practices

| Practice | Why it matters |
|----------|----------------|
| Command loop + dispatch | Standard pattern for CLIs; easy to add new commands without tangling logic. |
| Single source of truth for state | One store (e.g. list) updated only in one place; avoids inconsistent state. |
| I/O at the edge | Same validate/evaluate/format can be reused from API or tests; CLI only does input/output. |
| Explicit commands | User (or script) sees exactly what actions exist (add, list, eval, quit); no hidden behavior. |

---

## Session format (every time)

1. **Primitive lesson** — Command loop, dispatch, in-memory store, I/O vs logic.
2. **Business paragraph** — Scenario: “Support tool: add a user, list users, run eligibility for a user by id.”
3. **Implement translation** — You write the loop, dispatch, and store; call existing validate/evaluate/format.
4. **Critique + tighten** — Ensure no print/input inside rules or validation; ensure state changes only in add-handler.

---

## Hour-by-hour guide

### Hours 23–24: Command loop and input

- Learn: **infinite loop** that breaks on `quit`; **input()** to read a line; **split()** to get command and arguments (e.g. `add 1 25 verified`).
- **Business scenario:** “CLI that accepts commands: `add <id> <age> <verified>`, `list`, `eval <id>`, `quit`. Loop until user types `quit`.”
- **Output:** A loop that reads a line, splits it, and (for now) prints “Unknown command” or echoes the command—no real logic yet.

### Hours 25–26: In-memory store and add/list

- Learn: **store** — a list (e.g. `users = []`) at module or main scope; **add** command parses args, builds a record, appends to the list; **list** command iterates and prints (or formats) each record.
- **Business scenario:** “Implement `add`: append a user record to the store. Implement `list`: show every user (id, age, verified).”
- **Output:** Controlled mutation: the store changes only when `add` is called; `list` only reads.

### Hours 27–28: Dispatch and eval

- Learn: **dispatch** — `if command == "add": ... elif command == "list": ... elif command == "eval": ...`. **eval** command: find user by id in store; call validate then evaluate then format; print the result.
- **Business scenario:** “Implement `eval <id>`: look up user by id; run the full policy pipeline (validate → evaluate → format); print the formatted result. Use the validate, evaluate, and format functions you already have—no duplicate logic.”
- **Output:** Add / list / evaluate users from an in-memory store; separation of I/O (input/print in CLI) and logic (validate, evaluate, format as pure or data-in/data-out functions).

---

## Success criteria for Phase 5

- You can implement a command loop that reads commands and quits on `quit`.
- You can dispatch to add, list, and eval handlers.
- You can maintain one in-memory store that only changes on `add`.
- You can run the full policy pipeline (validate → evaluate → format) for `eval <id>` without putting print/input inside validate, evaluate, or rules.

---

## Canonical example

See **[Phase 5 canonical example](../canonical_examples/phase_5_canonical_example.md)** for a minimal stateful CLI with add, list, eval, and quit.

---

## Link to overview

Back to [Curriculum overview](../curriculum_overview.md).
