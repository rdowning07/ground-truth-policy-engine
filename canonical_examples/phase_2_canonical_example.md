# Phase 2 — Canonical example: Guard clauses and validation

## Business paragraph (how it shows up in the wild)

> “Before we run any eligibility rule, we must ensure the user record is valid: it must have an `age` field, that value must be a number, and it must be between 0 and 120. If any of these fail, we return a validation failure with a specific reason (e.g. ‘missing age’, ‘age not a number’, ‘age out of range’) and we do not run the business rule. Only valid records get evaluated.”

---

## What we’re training

- **Validation first:** Check data before running rules.
- **Guard clauses:** At the start of the function, if something is wrong, return immediately with a structured failure.
- **Distinct reasons:** So support and auditing can tell “missing field” from “wrong type” from “failed rule.”

---

## Industry tie-in

- **Compliance:** “We did not approve invalid data” is explicit; we never run rules on bad input.
- **Support:** “Missing age” vs “age below minimum” tells the user exactly what to fix.
- **No silent defaults:** We do not guess (e.g. age = 0); we fail explicitly so bugs don’t hide.

---

## Canonical code (assumes no prior Python)

Validation function: returns either `{"valid": True}` or `{"valid": False, "reason": "..."}`. Guard clauses run in order; first failure wins.

```python
def validate_user_record(record):
    """
    Guard clauses: if anything is wrong, return immediately with a reason.
    No business rules run until the record passes validation.
    """

    # Guard 1: record must have "age" key.
    if "age" not in record:
        return {"valid": False, "reason": "missing age"}

    age = record["age"]

    # Guard 2: age must be a number (int or float).
    if not isinstance(age, (int, float)):
        return {"valid": False, "reason": "age not a number"}

    # Guard 3: age must be in allowed range.
    if age < 0 or age > 120:
        return {"valid": False, "reason": "age out of range"}

    # All guards passed.
    return {"valid": True}
```

Using validation before one rule (age >= 18):

```python
def validate_then_evaluate_age(record):
    """
    Orchestration: validate first. If invalid, return validation result.
    If valid, run the rule and return rule result (with a distinct reason).
    """

    validation = validate_user_record(record)
    if not validation["valid"]:
        # Return validation failure distinctly (e.g. "missing age").
        return {"passed": False, "reason": validation["reason"], "kind": "validation"}

    # Record is valid; run the business rule.
    if record["age"] >= 18:
        return {"passed": True, "reason": None, "kind": "rule"}
    else:
        return {"passed": False, "reason": "age below minimum", "kind": "rule"}
```

---

## Why this is canonical

| Choice | Reason |
|--------|--------|
| Guards at the top | Invalid paths exit early; no deep nesting. |
| One reason per failure | `reason` is a single string; `kind` separates "validation" vs "rule" for reporting. |
| No defaults for missing data | We never set age = 0 or skip the check; we return "missing age." |
| Same return shape | Both validation and rule return a structure with at least passed/reason (and optionally kind). |

---

## Link to phase

This example implements the learning goals of [Phase 2 — Guard clauses + validation](../curriculum/phase_2_guard_clauses_validation.md).
