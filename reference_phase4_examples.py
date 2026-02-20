"""
Reference curriculum: Day 4 — Decomposition (tutor walkthrough).

This file contains all the examples from REFERENCE_CURRICULUM_PHASE4.md in order.
Run: python3 reference_phase4_examples.py

Prerequisite: Phases 1–3. See reference_phase1_examples.py through reference_phase3_examples.py.
"""
# pylint: disable=invalid-name,redefined-outer-name

from typing import Any, Callable, Sequence

# =============================================================================
# 1. Function boundaries: one job per function (concept)
# =============================================================================

print("--- Example 1: Function boundaries (concept) ---")
print("validate / evaluate / format / run_policy (orchestrator)")

# =============================================================================
# 2. Validate: one function that only validates
# =============================================================================

print("\n--- Example 2: Validate ---")


def validate(record: dict[str, Any]) -> dict[str, Any]:
    """Return valid or a failure reason. No rule logic, no formatting."""
    if "age" not in record:
        return {"valid": False, "reason": "missing age"}
    if not isinstance(record["age"], (int, float)):
        return {"valid": False, "reason": "age not a number"}
    if record["age"] < 0 or record["age"] > 120:
        return {"valid": False, "reason": "age out of range"}
    return {"valid": True}


print(validate({"age": 25}))
print(validate({}))
print(validate({"age": -1}))

# =============================================================================
# 3. Evaluate: one function that only runs rules
# =============================================================================

print("\n--- Example 3: Evaluate ---")


def rule_age(record: dict[str, Any]) -> dict[str, Any]:
    """Rule: age >= 18."""
    if record.get("age", 0) >= 18:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "age below minimum"}


def evaluate(
    record: dict[str, Any],
    rule_list: Sequence[Callable[[dict[str, Any]], dict[str, Any]]],
) -> dict[str, Any]:
    """Assume record is valid. Run every rule, collect failure reasons, return allow/deny."""
    reasons: list[Any] = []
    for rule_fn in rule_list:
        result = rule_fn(record)
        if not result["passed"]:
            reasons.append(result["reason"])
    return {"allowed": len(reasons) == 0, "reasons": reasons}


rules = [rule_age]
print(evaluate({"age": 25}, rules))
print(evaluate({"age": 17}, rules))

# =============================================================================
# 4. Format: one function that only formats
# =============================================================================

print("\n--- Example 4: Format ---")


def format_result(decision: dict[str, Any]) -> str:
    """Turn validation or evaluation result into a string for the caller."""
    if "valid" in decision and not decision["valid"]:
        return "Validation failed: " + str(decision["reason"])
    if decision["allowed"]:
        return "Allowed"
    return "Denied: " + "; ".join(str(r) for r in decision["reasons"])


print(format_result({"valid": False, "reason": "missing age"}))
print(format_result({"allowed": True, "reasons": []}))
print(format_result({"allowed": False, "reasons": ["age below minimum"]}))

# =============================================================================
# 5. Orchestration: one entry point that only wires steps
# =============================================================================

print("\n--- Example 5: Orchestration (run_policy) ---")


def run_policy(
    record: dict[str, Any],
    rule_list: Sequence[Callable[[dict[str, Any]], dict[str, Any]]],
) -> str:
    """Single entry point: validate → evaluate (if valid) → format."""
    validation = validate(record)
    if not validation["valid"]:
        return format_result(validation)

    decision = evaluate(record, rule_list)
    return format_result(decision)


print(run_policy({}, rules))
print(run_policy({"age": 17}, rules))
print(run_policy({"age": 25}, rules))

# =============================================================================
# 6. Full example: validate, evaluate, format, run_policy (Phase 4 style)
# =============================================================================

print("\n--- Example 6: Full Phase 4-style (three rules + pipeline) ---")


def rule_verified(record: dict[str, Any]) -> dict[str, Any]:
    """Rule: account must be verified."""
    if record.get("verified", False) is True:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "account not verified"}


def rule_region(record: dict[str, Any]) -> dict[str, Any]:
    """Rule: not in restricted region."""
    restricted = ["XX", "YY"]
    if record.get("region", "") not in restricted:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "region restricted"}


all_rules: list[Callable[[dict[str, Any]], dict[str, Any]]] = [
    rule_age,
    rule_verified,
    rule_region,
]

record_pass = {"age": 25, "verified": True, "region": "US"}
record_fail = {"age": 17, "verified": False, "region": "US"}
record_invalid: dict[str, Any] = {}

print("Valid pass:", run_policy(record_pass, all_rules))
print("Valid fail:", run_policy(record_fail, all_rules))
print("Invalid:", run_policy(record_invalid, all_rules))

print("\n--- Done. See REFERENCE_CURRICULUM_PHASE4.md for the tutor walkthrough. ---")
