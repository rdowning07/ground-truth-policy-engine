"""
Reference curriculum: Phase 5 — Stateful CLI (tutor walkthrough).

This file contains all the examples from REFERENCE_CURRICULUM_PHASE5.md in order.
Run: python3 reference_phase5_examples.py

Prerequisite: Phases 1–4. See reference_phase1_examples.py through reference_phase4_examples.py.
"""
# pylint: disable=invalid-name,redefined-outer-name

from typing import Any, Callable, Sequence

# =============================================================================
# Phase 4-style pipeline (needed for handle_eval and full example)
# =============================================================================


def _validate(record: dict[str, Any]) -> dict[str, Any]:
    """Return valid or a failure reason."""
    if "age" not in record:
        return {"valid": False, "reason": "missing age"}
    if not isinstance(record["age"], (int, float)):
        return {"valid": False, "reason": "age not a number"}
    if record["age"] < 0 or record["age"] > 120:
        return {"valid": False, "reason": "age out of range"}
    return {"valid": True}


def _rule_age(record: dict[str, Any]) -> dict[str, Any]:
    """Rule: age >= 18."""
    if record.get("age", 0) >= 18:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "age below minimum"}


def _evaluate(
    record: dict[str, Any],
    rule_list: Sequence[Callable[[dict[str, Any]], dict[str, Any]]],
) -> dict[str, Any]:
    """Assume record is valid. Run every rule, return allow/deny."""
    reasons: list[Any] = []
    for rule_fn in rule_list:
        result = rule_fn(record)
        if not result["passed"]:
            reasons.append(result["reason"])
    return {"allowed": len(reasons) == 0, "reasons": reasons}


def _format_result(decision: dict[str, Any]) -> str:
    """Turn validation or evaluation result into a string."""
    if "valid" in decision and not decision["valid"]:
        return "Validation failed: " + str(decision["reason"])
    if decision["allowed"]:
        return "Allowed"
    return "Denied: " + "; ".join(str(r) for r in decision["reasons"])


def _run_policy(
    record: dict[str, Any],
    rule_list: Sequence[Callable[[dict[str, Any]], dict[str, Any]]],
) -> str:
    """Single entry point: validate → evaluate (if valid) → format."""
    validation = _validate(record)
    if not validation["valid"]:
        return _format_result(validation)
    decision = _evaluate(record, rule_list)
    return _format_result(decision)


_rules = [_rule_age]

# =============================================================================
# 1. Reading a line and splitting into command and args
# =============================================================================

print("--- Example 1: Reading a line and splitting ---")

line = "add 1 25 true US"
parts = line.split()
command = parts[0].lower()
args = parts[1:] if len(parts) > 1 else []

print("command:", command)
print("args:", args)

line2 = "list"
parts2 = line2.split()
command2 = parts2[0].lower()
args2 = parts2[1:] if len(parts2) > 1 else []
print("command2:", command2, "args2:", args2)

# =============================================================================
# 2. Command loop: repeat until quit
# =============================================================================

print("\n--- Example 2: Command loop (simulated lines) ---")

simulated_lines = ["list", "add 1 25 true US", "quit"]

for simulated_line in simulated_lines:
    line = simulated_line.strip()
    if not line:
        continue
    parts = line.split()
    cmd = parts[0].lower()
    cmd_args = parts[1:] if len(parts) > 1 else []
    if cmd == "quit":
        print("bye")
        break
    print("Got command:", cmd, "args:", cmd_args)

# =============================================================================
# 3. In-memory store: one list, mutated only by add
# =============================================================================

print("\n--- Example 3: In-memory store ---")

store: list[dict[str, Any]] = []

record = {"id": "1", "age": 25, "verified": True, "region": "US"}
store.append(record)
print("After one add, users:", store)

record2 = {"id": "2", "age": 17, "verified": False, "region": "UK"}
store.append(record2)
print("After two adds, len(users):", len(store))

# =============================================================================
# 4. handle_add: parse args, build record, append to store
# =============================================================================

print("\n--- Example 4: handle_add ---")


def handle_add(args: list[str], users: list[dict[str, Any]]) -> str:
    """Append one record to the store; return message. No print inside."""
    if len(args) < 4:
        return "add requires: id age verified region"
    user_id = args[0]
    try:
        age = int(args[1])
    except ValueError:
        return "age must be a number"
    verified = args[2].lower() in ("true", "1", "yes")
    region = args[3]
    rec = {"id": user_id, "age": age, "verified": verified, "region": region}
    users.append(rec)
    return "added " + str(user_id)


# Use a fresh list for this demo so we can show add and then list/eval
demo_store: list[dict[str, Any]] = []
print(handle_add(["u1", "25", "true", "US"], demo_store))
print(handle_add(["u2", "17", "false", "UK"], demo_store))
print("users now:", demo_store)
print(handle_add(["u3"], demo_store))

# =============================================================================
# 5. handle_list: read the store, format and return
# =============================================================================

print("\n--- Example 5: handle_list ---")


def handle_list(users: list[dict[str, Any]]) -> str:
    """Read-only: format each user; return string. No mutation."""
    if not users:
        return "no users"
    lines = []
    for u in users:
        lines.append(
            f"id={u['id']} age={u['age']} verified={u['verified']} region={u['region']}"
        )
    return "\n".join(lines)


print(handle_list(demo_store))

# =============================================================================
# 6. handle_eval: find user by id, run policy pipeline, return result
# =============================================================================

print("\n--- Example 6: handle_eval ---")


def handle_eval(
    args: list[str],
    users: list[dict[str, Any]],
    run_policy_fn: Callable[
        [dict[str, Any], Sequence[Callable[[dict[str, Any]], dict[str, Any]]]], str
    ],
    rules_list: Sequence[Callable[[dict[str, Any]], dict[str, Any]]],
) -> str:
    """Look up user by id; run full policy pipeline; return formatted string."""
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
    return run_policy_fn(record, rules_list)


print("eval u1:", handle_eval(["u1"], demo_store, _run_policy, _rules))
print("eval u2:", handle_eval(["u2"], demo_store, _run_policy, _rules))
print("eval 99:", handle_eval(["99"], demo_store, _run_policy, _rules))

# =============================================================================
# 7. Dispatch: match command to handler (concept)
# =============================================================================

print("\n--- Example 7: Dispatch (concept) ---")
print("One if/elif per command; each calls a handler and prints the returned string.")

# =============================================================================
# 8. I/O at the edge (concept)
# =============================================================================

print("\n--- Example 8: I/O at the edge (concept) ---")
print("input/print only in the command loop; handlers and run_policy return values.")

# =============================================================================
# 9. Full example: simulated session (command loop + dispatch + store)
# =============================================================================

print("\n--- Example 9: Full Phase 5-style simulated session ---")


def run_simulated_session(
    lines: list[str],
    users: list[dict[str, Any]],
    rules_list: Sequence[Callable[[dict[str, Any]], dict[str, Any]]],
    run_policy_fn: Callable[
        [dict[str, Any], Sequence[Callable[[dict[str, Any]], dict[str, Any]]]], str
    ],
) -> None:
    """
    Run the same logic as main_cli but read commands from a list instead of input().
    So we can run the full example without waiting for user input.
    """
    print("Commands: add <id> <age> <verified> <region> | list | eval <id> | quit")
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        cmd = parts[0].lower()
        cmd_args = parts[1:] if len(parts) > 1 else []

        if cmd == "quit":
            print("bye")
            break
        if cmd == "add":
            print(handle_add(cmd_args, users))
        elif cmd == "list":
            print(handle_list(users))
        elif cmd == "eval":
            print(handle_eval(cmd_args, users, run_policy_fn, rules_list))
        else:
            print("unknown command: " + cmd)


session_store: list[dict[str, Any]] = []
session_lines = [
    "add alice 25 true US",
    "add bob 17 false UK",
    "list",
    "eval alice",
    "eval bob",
    "eval nobody",
    "quit",
]
run_simulated_session(session_lines, session_store, _rules, _run_policy)

print("\n--- Done. See REFERENCE_CURRICULUM_PHASE5.md for the tutor walkthrough. ---")
