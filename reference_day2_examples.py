"""
Reference curriculum: Day 2 — Guard clauses and validation (tutor walkthrough).

This file contains all the examples from REFERENCE_CURRICULUM_DAY2.md in order.
Run: python3 reference_day2_examples.py

Prerequisite: Phase 1 (one rule, many records). See reference_day1_examples.py.
"""

# =============================================================================
# 1. Early return: if something is wrong, return immediately
# =============================================================================
# A guard clause returns immediately with a failure when the condition is not met.

print("--- Example 1: Early return (guard clause) ---")


def check_has_age(record):
    if "age" not in record:
        return {"valid": False, "reason": "missing age"}
    return {"valid": True}


result_missing = check_has_age({"id": 1})
result_ok = check_has_age({"id": 1, "age": 25})
print("Record without age:", result_missing)
print("Record with age:", result_ok)

# =============================================================================
# 2. Checking for a key: "key" not in record
# =============================================================================
# We check "age" not in record before using record["age"] to avoid KeyError.

print("\n--- Example 2: Checking for a key ---")
record_with_age = {"id": 1, "age": 25}
record_without_age = {"id": 2}
print("'age' in record_with_age?", "age" in record_with_age)
print("'age' not in record_without_age?", "age" not in record_without_age)

# =============================================================================
# 3. Multiple guards: missing, type, range
# =============================================================================
# Run several guards in order; first failure wins.

print("\n--- Example 3: Multiple guards ---")


def validate_age_field(record):
    if "age" not in record:
        return {"valid": False, "reason": "missing age"}
    age = record["age"]
    if not isinstance(age, (int, float)):
        return {"valid": False, "reason": "age not a number"}
    if age < 0 or age > 120:
        return {"valid": False, "reason": "age out of range"}
    return {"valid": True}


print(validate_age_field({}))
print(validate_age_field({"age": "twenty"}))
print(validate_age_field({"age": -1}))
print(validate_age_field({"age": 25}))

# =============================================================================
# 4. Validation function: one function that only validates
# =============================================================================
# validate_user_record is used in examples 5, 6, 7, 8.

print("\n--- Example 4: Validation function ---")


def validate_user_record(record):
    if "age" not in record:
        return {"valid": False, "reason": "missing age"}
    age = record["age"]
    if not isinstance(age, (int, float)):
        return {"valid": False, "reason": "age not a number"}
    if age < 0 or age > 120:
        return {"valid": False, "reason": "age out of range"}
    return {"valid": True}


v1 = validate_user_record({"id": 1, "age": 25})
v2 = validate_user_record({"id": 2})
print("Valid record:", v1)
print("Missing age:", v2)

# =============================================================================
# 5. Orchestration: validate first, then run the rule
# =============================================================================
# Call validation; if invalid return validation result; if valid run the rule.

print("\n--- Example 5: Orchestration (validate then rule) ---")


def validate_then_evaluate_age(record):
    validation = validate_user_record(record)
    if not validation["valid"]:
        return {"passed": False, "reason": validation["reason"]}
    if record["age"] >= 18:
        return {"passed": True, "reason": None}
    else:
        return {"passed": False, "reason": "age below minimum"}


print(validate_then_evaluate_age({"id": 1}))
print(validate_then_evaluate_age({"id": 2, "age": 25}))
print(validate_then_evaluate_age({"id": 3, "age": 17}))

# =============================================================================
# 6. Distinct kind: validation vs rule failure
# =============================================================================
# Add "kind": "validation" or "kind": "rule" so the caller can tell them apart.

print("\n--- Example 6: Distinct kind (validation vs rule) ---")


def validate_then_evaluate_age_with_kind(record):
    validation = validate_user_record(record)
    if not validation["valid"]:
        return {"passed": False, "reason": validation["reason"], "kind": "validation"}
    if record["age"] >= 18:
        return {"passed": True, "reason": None, "kind": "rule"}
    else:
        return {"passed": False, "reason": "age below minimum", "kind": "rule"}


r1 = validate_then_evaluate_age_with_kind({"id": 1})
r2 = validate_then_evaluate_age_with_kind({"id": 2, "age": 17})
print("Missing age (validation):", r1)
print("Age 17 (rule):", r2)

# =============================================================================
# 7. Full example: validate then evaluate (Phase 2 style)
# =============================================================================
# validate_user_record and validate_then_evaluate_age_with_kind already defined above.
# This section just runs them again to show the full Phase 2 pattern.

print("\n--- Example 7: Full Phase 2-style (validate then evaluate) ---")
print(validate_then_evaluate_age_with_kind({"id": 1, "age": 25}))
print(validate_then_evaluate_age_with_kind({"id": 2, "age": 17}))
print(validate_then_evaluate_age_with_kind({"id": 3}))

# =============================================================================
# 8. Loop over records: validate each, then rule or validation result
# =============================================================================
# One result per record; each result has passed, reason, and kind.

print("\n--- Example 8: Loop over records (validate then rule per record) ---")


def validate_then_evaluate_all(records):
    results = []
    for record in records:
        validation = validate_user_record(record)
        if not validation["valid"]:
            # Use .get("id") in case id is also missing.
            results.append({
                "id": record.get("id"),
                "passed": False,
                "reason": validation["reason"],
                "kind": "validation",
            })
        else:
            if record["age"] >= 18:
                results.append({"id": record["id"], "passed": True, "reason": None, "kind": "rule"})
            else:
                results.append({
                    "id": record["id"],
                    "passed": False,
                    "reason": "age below minimum",
                    "kind": "rule",
                })
    return results


all_records = [
    {"id": 1, "age": 25},
    {"id": 2, "age": 17},
    {"id": 3},
    {"id": 4, "age": -5},
]
output = validate_then_evaluate_all(all_records)
print("Input:", all_records)
print("Output:", output)

print("\n--- Done. See REFERENCE_CURRICULUM_DAY2.md for the tutor walkthrough. ---")
