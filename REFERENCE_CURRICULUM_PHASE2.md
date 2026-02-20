# Reference curriculum: Phase 2 — Guard clauses and validation (tutor walkthrough)

This document is a **reference curriculum** for Phase 2: explicit, step-by-step code with heavy comments for **guard clauses**, **validation**, and **orchestration** (validate first, then run the rule). Every example is runnable. No shortcuts—one concept at a time.

**Prerequisite:** You have completed [Phase 1](curriculum/phase_1_deterministic_evaluation.md) (one rule, many records, loop, conditional, accumulator) and the [Phase 1 reference](REFERENCE_CURRICULUM_PHASE1.md).

**How to use:** Read each section; run the code (copy into a file or use the [single runnable file](reference_phase2_examples.py)). The comments explain *what this line does* and *why we write it this way*.

**Tied to:** [Phase 2 — Guard clauses + validation](curriculum/phase_2_guard_clauses_validation.md) and [Phase 2 canonical example](canonical_examples/phase_2_canonical_example.md).

---

## 1. Early return: if something is wrong, return immediately

A **guard clause** is a check at the start of a function. If the condition is not met, we **return immediately** with a failure result. We do not nest “if valid then do the rest”—we exit early so invalid paths are obvious.

```python
# We're writing a function that requires an age to be present.
# If age is missing, we return a structured failure and stop. No rule runs.
def check_has_age(record):
    # Guard: if "age" is not a key in the dict, we return right away.
    # The string "age" not in record is True when the key is missing.
    if "age" not in record:
        # We return a small dict that says what went wrong.
        # The caller gets this and can show "missing age" to the user or logs.
        return {"valid": False, "reason": "missing age"}

    # If we get here, the guard did not fire. So "age" is in the record.
    # We could run more checks or a rule next. For this example we just say valid.
    return {"valid": True}


# Try it with a record that has no age.
result_missing = check_has_age({"id": 1})
print("Record without age:", result_missing)

# Try it with a record that has age.
result_ok = check_has_age({"id": 1, "age": 25})
print("Record with age:", result_ok)
```

**What we just did:** We used one guard. If the record was invalid (missing key), we returned immediately. No nested if/else—just “if bad, return; otherwise continue.”

---

## 2. Checking for a key: "key" not in record

In Phase 1 we used `record["age"]`. If the key is missing, that raises `KeyError`. To avoid that, we **check first** with `"age" not in record`. That expression is `True` when the key is missing.

```python
# Two ways to think about it:
# - "age" not in record  →  True when the key "age" is missing
# - "age" in record      →  True when the key "age" is present

record_with_age = {"id": 1, "age": 25}
record_without_age = {"id": 2}

# Check before we try to read the key.
print("'age' in record_with_age?", "age" in record_with_age)
print("'age' not in record_without_age?", "age" not in record_without_age)

# So our guard is: if "age" not in record, return failure.
# We never call record["age"] when the key might be missing.
```

**What we just did:** We used `in` and `not in` to test for a key before reading it. That’s how we avoid `KeyError` and return a clear “missing age” instead.

---

## 3. Multiple guards: missing, type, range

We run several guard clauses **in order**. First we check the key is present. Then we get the value and check it’s a number. Then we check it’s in the allowed range. The **first** failure wins—we return that reason and stop.

```python
def validate_age_field(record):
    """
    Guard 1: age must be present.
    Guard 2: age must be a number (int or float).
    Guard 3: age must be between 0 and 120 (inclusive).
    """

    # Guard 1: the key "age" must exist.
    if "age" not in record:
        return {"valid": False, "reason": "missing age"}

    # We only get here if "age" is in the record. Now we can safely read it.
    age = record["age"]

    # Guard 2: age must be a number. isinstance(x, (int, float)) is True when x is an int or a float.
    # We do not allow a string like "25" or something else.
    if not isinstance(age, (int, float)):
        return {"valid": False, "reason": "age not a number"}

    # Guard 3: age must be in a sensible range. Outside 0–120 we return a clear reason.
    if age < 0 or age > 120:
        return {"valid": False, "reason": "age out of range"}

    # All guards passed. The record is valid for the age field.
    return {"valid": True}


# Try different invalid inputs.
print(validate_age_field({}))                    # missing age
print(validate_age_field({"age": "twenty"}))    # age not a number
print(validate_age_field({"age": -1}))           # age out of range
print(validate_age_field({"age": 25}))           # valid
```

**What we just did:** We ran three guards in sequence. Each guard returns a structured failure with a specific reason. Only if all pass do we return `{"valid": True}`.

---

## 4. Validation function: one function that only validates

We put all the guard clauses into a single function whose **only job** is validation. It returns either `{"valid": True}` or `{"valid": False, "reason": "..."}`. It does **not** run any business rule—that happens later.

```python
def validate_user_record(record):
    """
    Guard clauses: if anything is wrong, return immediately with a reason.
    No business rules run until the record passes validation.
    """

    if "age" not in record:
        return {"valid": False, "reason": "missing age"}

    age = record["age"]

    if not isinstance(age, (int, float)):
        return {"valid": False, "reason": "age not a number"}

    if age < 0 or age > 120:
        return {"valid": False, "reason": "age out of range"}

    return {"valid": True}


# The caller will check validation["valid"]. If True, they run the rule.
# If False, they use validation["reason"] and never run the rule.
v1 = validate_user_record({"id": 1, "age": 25})
v2 = validate_user_record({"id": 2})
print("Valid record:", v1)
print("Missing age:", v2)
```

**What we just did:** We have one function that only validates. Callers call it first; if it returns valid, they then run the rule. Validation and rule are separate.

---

## 5. Orchestration: validate first, then run the rule

**Orchestration** means “call the right functions in order.” We call validation first. If the result is not valid, we return the validation failure and **do not** run the rule. If valid, we run the rule and return the rule result.

```python
# We assume validate_user_record is defined (as in section 4).

def validate_then_evaluate_age(record):
    """
    Step 1: Validate the record.
    Step 2: If invalid, return the validation result (with reason).
    Step 3: If valid, run the age rule and return that result.
    """

    # Step 1: Call the validation function. It returns {"valid": True} or {"valid": False, "reason": "..."}.
    validation = validate_user_record(record)

    # Step 2: If validation failed, we return immediately. We do not run the rule.
    # We turn the validation result into the shape the caller expects: passed False, reason from validation.
    if not validation["valid"]:
        return {"passed": False, "reason": validation["reason"]}

    # Step 3: We only get here when the record is valid. So we can safely use record["age"].
    # Now we run the business rule: age must be >= 18.
    if record["age"] >= 18:
        return {"passed": True, "reason": None}
    else:
        return {"passed": False, "reason": "age below minimum"}
```

**What we just did:** We orchestrated two steps: validate, then (if valid) evaluate. Invalid data never reaches the rule. The caller always gets a result with `passed` and `reason`.

---

## 6. Distinct kind: validation vs rule failure

For support and auditing we need to tell **why** someone was denied: was it a **validation** problem (missing age, bad type, out of range) or a **rule** problem (age below minimum)? We add a `kind` field so the caller can tell them apart.

```python
def validate_then_evaluate_age_with_kind(record):
    """
    Same as before, but we add "kind": "validation" or "kind": "rule" so the caller
    can report "missing age" (validation) vs "age below minimum" (rule).
    """

    validation = validate_user_record(record)
    if not validation["valid"]:
        # This failure came from validation, not from the rule.
        return {"passed": False, "reason": validation["reason"], "kind": "validation"}

    # Record is valid; run the business rule.
    if record["age"] >= 18:
        return {"passed": True, "reason": None, "kind": "rule"}
    else:
        return {"passed": False, "reason": "age below minimum", "kind": "rule"}


# Now the caller can say: "You were denied because of validation: missing age"
# or "You were denied because of the rule: age below minimum."
r1 = validate_then_evaluate_age_with_kind({"id": 1})
r2 = validate_then_evaluate_age_with_kind({"id": 2, "age": 17})
print("Missing age (validation):", r1)
print("Age 17 (rule):", r2)
```

**What we just did:** We kept the same flow (validate then rule) but added `kind` so validation failures and rule failures are distinct. No silent defaults—we fail explicitly with a reason and a kind.

---

## 7. Full example: validate then evaluate (Phase 2 style)

This matches the [Phase 2 canonical example](canonical_examples/phase_2_canonical_example.md), with every step commented.

```python
def validate_user_record(record):
    if "age" not in record:
        return {"valid": False, "reason": "missing age"}
    age = record["age"]
    if not isinstance(age, (int, float)):
        return {"valid": False, "reason": "age not a number"}
    if age < 0 or age > 120:
        return {"valid": False, "reason": "age out of range"}
    return {"valid": True}


def validate_then_evaluate_age(record):
    validation = validate_user_record(record)
    if not validation["valid"]:
        return {"passed": False, "reason": validation["reason"], "kind": "validation"}
    if record["age"] >= 18:
        return {"passed": True, "reason": None, "kind": "rule"}
    else:
        return {"passed": False, "reason": "age below minimum", "kind": "rule"}
```

**What we just did:** Two functions: one only validates, one orchestrates (validate then rule) and returns a result with `passed`, `reason`, and `kind`. This is the Phase 2 pattern.

---

## 8. Loop over records: validate each, then rule or validation result

For **many records**, we loop and for each record: validate; if invalid, append a validation failure to the results; if valid, run the rule and append the rule result. So we get one result per record, and each result says whether it was a validation or rule outcome.

```python
def validate_then_evaluate_all(records):
    results = []
    for record in records:
        validation = validate_user_record(record)
        if not validation["valid"]:
            results.append({"id": record.get("id"), "passed": False, "reason": validation["reason"], "kind": "validation"})
        else:
            if record["age"] >= 18:
                results.append({"id": record["id"], "passed": True, "reason": None, "kind": "rule"})
            else:
                results.append({"id": record["id"], "passed": False, "reason": "age below minimum", "kind": "rule"})
    return results
```

**What we just did:** We combined the Phase 1 pattern (loop, accumulator) with the Phase 2 pattern (validate first, distinct validation vs rule). One result per record; each result has a reason and a kind.

---

## All examples in one runnable file

The file [reference_phase2_examples.py](reference_phase2_examples.py) contains all of the above examples in order. Run:

```bash
python3 reference_phase2_examples.py
```

Use it as a reference when implementing Phase 2 in `src/engine.py`.

**Previous:** [REFERENCE_CURRICULUM_PHASE1.md](REFERENCE_CURRICULUM_PHASE1.md) (Phase 1). **Next:** [REFERENCE_CURRICULUM_PHASE3.md](REFERENCE_CURRICULUM_PHASE3.md) (Phase 3: rule composition).

---

Back to [Phase 2 curriculum](curriculum/phase_2_guard_clauses_validation.md) · [Curriculum overview](curriculum_overview.md).
