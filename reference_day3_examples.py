"""
Reference curriculum: Day 3 — Rule composition (tutor walkthrough).

This file contains all the examples from REFERENCE_CURRICULUM_DAY3.md in order.
Run: python3 reference_day3_examples.py

Prerequisite: Phase 1 and Phase 2. See reference_day1_examples.py and reference_day2_examples.py.
"""
# Pylint: pedagogical names and reuse of names across examples.
# pylint: disable=invalid-name,redefined-outer-name

from typing import Any, Callable

# =============================================================================
# 1. One rule as a function: same shape every time
# =============================================================================
# A rule function takes a record and returns {"passed": ..., "reason": ...}.

print("--- Example 1: One rule as a function ---")


def rule_age(record: dict[str, Any]) -> dict[str, Any]:
    """Rule: age >= 18."""
    if record.get("age", 0) >= 18:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "age below minimum"}


print(rule_age({"age": 25}))
print(rule_age({"age": 17}))

# =============================================================================
# 2. Same return shape: why it matters
# =============================================================================
# (Concept only; no code to run.)

print("\n--- Example 2: Same return shape (concept) ---")
print("Every rule returns {\"passed\": bool, \"reason\": None or str}.")

# =============================================================================
# 3. A second and third rule function
# =============================================================================

print("\n--- Example 3: Three rule functions ---")


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


print(rule_verified({"verified": True}))
print(rule_verified({"verified": False}))
print(rule_region({"region": "US"}))
print(rule_region({"region": "XX"}))

# =============================================================================
# 4. List of rule functions: pass rules in
# =============================================================================

print("\n--- Example 4: List of rule functions ---")
rules: list[Callable[[dict[str, Any]], dict[str, Any]]] = [
    rule_age,
    rule_verified,
    rule_region,
]
record = {"age": 25, "verified": True, "region": "US"}
result_age = rules[0](record)
result_verified = rules[1](record)
result_region = rules[2](record)
print("Age:", result_age)
print("Verified:", result_verified)
print("Region:", result_region)

# =============================================================================
# 5. Run all rules and collect results
# =============================================================================

print("\n--- Example 5: Run all rules, collect results ---")


def run_all_rules(
    rec: dict[str, Any],
    rule_list: list[Callable[[dict[str, Any]], dict[str, Any]]],
) -> list[dict[str, Any]]:
    """Run each rule and collect every result. No short-circuit."""
    results: list[dict[str, Any]] = []
    for rule_fn in rule_list:
        result = rule_fn(rec)
        results.append(result)
    return results


record = {"age": 17, "verified": False, "region": "US"}
out = run_all_rules(record, rules)
print("All results:", out)

# =============================================================================
# 6. Collect only failure reasons (in order)
# =============================================================================

print("\n--- Example 6: Collect failure reasons ---")


def collect_failure_reasons(results: list[dict[str, Any]]) -> list[Any]:
    """Build a list of reasons for every result that did not pass."""
    reasons: list[Any] = []
    for result in results:
        if not result["passed"]:
            reasons.append(result["reason"])
    return reasons


results = run_all_rules(record, rules)
reasons = collect_failure_reasons(results)
print("Failure reasons (in rule order):", reasons)

# =============================================================================
# 7. Allow only if all passed
# =============================================================================

print("\n--- Example 7: Allow or deny ---")


def allow_or_deny(reason_list: list[Any]) -> dict[str, Any]:
    """Allowed if no failures; otherwise denied with the list of reasons."""
    allowed = len(reason_list) == 0
    return {"allowed": allowed, "reasons": reason_list}


decision = allow_or_deny(reasons)
print("Decision:", decision)

# =============================================================================
# 8. Full composer: evaluate_all_rules (Phase 3 style)
# =============================================================================

print("\n--- Example 8: Full composer (evaluate_all_rules) ---")


def evaluate_all_rules(
    rec: dict[str, Any],
    rule_list: list[Callable[[dict[str, Any]], dict[str, Any]]],
) -> dict[str, Any]:
    """
    Full evaluation: run every rule, collect every failure.
    Return: allowed (bool), reasons (list of strings, in rule order).
    """
    reason_list: list[Any] = []

    for rule_fn in rule_list:
        result = rule_fn(rec)
        if not result["passed"]:
            reason_list.append(result["reason"])

    allowed = len(reason_list) == 0
    return {"allowed": allowed, "reasons": reason_list}


record = {"age": 17, "verified": False, "region": "US"}
decision = evaluate_all_rules(record, rules)
print("Record:", record)
print("Decision:", decision)

# =============================================================================
# 9. Full example: three rules, one allow/deny
# =============================================================================

print("\n--- Example 9: Full Phase 3-style (pass vs fail record) ---")
record_pass = {"age": 25, "verified": True, "region": "US"}
record_fail = {"age": 17, "verified": False, "region": "US"}
print("Pass record:", evaluate_all_rules(record_pass, rules))
print("Fail record:", evaluate_all_rules(record_fail, rules))

print("\n--- Done. See REFERENCE_CURRICULUM_DAY3.md for the tutor walkthrough. ---")
