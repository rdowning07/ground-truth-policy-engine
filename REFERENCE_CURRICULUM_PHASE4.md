# Reference curriculum: Phase 4 — Decomposition (tutor walkthrough)

This document is a **reference curriculum** for Phase 4: explicit, step-by-step code with heavy comments for **function boundaries** (validate / evaluate / format) and **orchestration** (one entry point that only calls them in order). Every example is runnable.

**Prerequisite:** You have completed Phases 1–3 and the [Phase 1](REFERENCE_CURRICULUM_PHASE1.md), [Phase 2](REFERENCE_CURRICULUM_PHASE2.md), and [Phase 3](REFERENCE_CURRICULUM_PHASE3.md) references.

**How to use:** Read each section; run the code (copy into a file or use the [single runnable file](reference_phase4_examples.py)).

**Tied to:** [Phase 4 — Decomposition](curriculum/phase_4_decomposition.md) and [Phase 4 canonical example](canonical_examples/phase_4_canonical_example.md).

---

## 1. Function boundaries: one job per function

We split the pipeline into three kinds of work: **validate** (is the data usable?), **evaluate** (does it pass the rules?), **format** (how do we present the result?). Each is a separate function. No function does two of these jobs. That way we can test and change each part without touching the others.

```python
# We will have:
# - validate(record)       → {"valid": True} or {"valid": False, "reason": "..."}
# - evaluate(record, rules) → {"allowed": bool, "reasons": [...]}  (assumes valid record)
# - format_result(decision) → string (or structure) for the caller
# - run_policy(record, rules) → calls validate, then evaluate (if valid), then format; returns formatted result
```

**What we just did:** We stated the four pieces. The orchestrator (`run_policy`) only calls the other three in order; it contains no validation logic, no rule logic, and no formatting logic.

---

## 2. Validate: one function that only validates

Validation is the same idea as Phase 2: guard clauses, return valid or a structured failure. We keep it in its own function so the orchestrator can call it first and decide whether to run evaluation.

```python
def validate(record):
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
```

**What we just did:** One function whose only job is validation. It returns a dict the orchestrator can check: `if not validation["valid"]` then we don't call evaluate.

---

## 3. Evaluate: one function that only runs rules

Evaluation assumes the record is already valid. It runs all rules and returns allow/deny plus reasons—same as Phase 3. No validation checks here, no formatting. Just rules in, decision out.

```python
def evaluate(record, rules):
    """
    Assume record is valid. Run every rule, collect failure reasons, return allow/deny.
    """
    reasons = []
    for rule_fn in rules:
        result = rule_fn(record)
        if not result["passed"]:
            reasons.append(result["reason"])
    return {"allowed": len(reasons) == 0, "reasons": reasons}


# We need at least one rule to call evaluate. Use a simple age rule.
def rule_age(record):
    if record.get("age", 0) >= 18:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "age below minimum"}

rules = [rule_age]
print(evaluate({"age": 25}, rules))
print(evaluate({"age": 17}, rules))
```

**What we just did:** Evaluate only runs rules and returns a decision. It does not validate or format. The caller is responsible for calling validate first.

---

## 4. Format: one function that only formats

Format takes a **decision** (either a validation result or an evaluation result) and turns it into something the caller can use—e.g. a string for the CLI. It does not validate or run rules. It only shapes output.

```python
def format_result(decision):
    """
    decision: either {"valid": False, "reason": str} or {"allowed": bool, "reasons": list}.
    Return a string suitable for the caller (e.g. CLI).
    """
    if "valid" in decision and not decision["valid"]:
        return "Validation failed: " + decision["reason"]
    if decision["allowed"]:
        return "Allowed"
    return "Denied: " + "; ".join(decision["reasons"])


print(format_result({"valid": False, "reason": "missing age"}))
print(format_result({"allowed": True, "reasons": []}))
print(format_result({"allowed": False, "reasons": ["age below minimum"]}))
```

**What we just did:** One function that only formats. It branches on the shape of the decision (validation failure vs evaluation result) and returns a string. No I/O inside validate or evaluate—format is where “presentation” lives.

---

## 5. Orchestration: one entry point that only wires steps

The **orchestrator** calls validate, then (if valid) evaluate, then format. It does not contain validation logic, rule logic, or formatting logic—only the order of calls and passing data.

```python
def run_policy(record, rules):
    """
    Single entry point: validate → evaluate (if valid) → format.
    No business logic here—only ordering and data passing.
    """
    validation = validate(record)
    if not validation["valid"]:
        return format_result(validation)

    decision = evaluate(record, rules)
    return format_result(decision)


# Try invalid record: we never call evaluate.
print(run_policy({}, rules))
# Try valid record that fails the rule.
print(run_policy({"age": 17}, rules))
# Try valid record that passes.
print(run_policy({"age": 25}, rules))
```

**What we just did:** One function that ties the pipeline together. Reading it tells you the full flow: validate first; if invalid, format that and return; otherwise evaluate, then format the decision and return.

---

## 6. Full example: validate, evaluate, format, run_policy (Phase 4 style)

This matches the [Phase 4 canonical example](canonical_examples/phase_4_canonical_example.md): all four functions in one place, with the same rules as Phase 3 (age, verified, region). The orchestrator is the only place that decides “validate then evaluate then format.”

```python
# Define validate, rule_age, rule_verified, rule_region, evaluate, format_result, run_policy.
# rules = [rule_age, rule_verified, rule_region]
# Then:
# print(run_policy({"age": 25, "verified": True, "region": "US"}, rules))
# print(run_policy({"age": 17}, rules))
# print(run_policy({}, rules))
```

**What we just did:** We described the full pipeline. The runnable file implements it so you can run and see "Allowed", "Denied: age below minimum; account not verified", and "Validation failed: missing age".

---

## All examples in one runnable file

The file [reference_phase4_examples.py](reference_phase4_examples.py) contains all of the above in order. Run:

```bash
python3 reference_phase4_examples.py
```

**Previous:** [REFERENCE_CURRICULUM_PHASE3.md](REFERENCE_CURRICULUM_PHASE3.md) (Phase 3: rule composition). **Next:** [REFERENCE_CURRICULUM_PHASE5.md](REFERENCE_CURRICULUM_PHASE5.md) (Phase 5: stateful CLI).

---

Back to [Phase 4 curriculum](curriculum/phase_4_decomposition.md) · [Curriculum overview](curriculum_overview.md).
