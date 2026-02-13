# Phase 4 — Canonical example: Decomposition (validate, evaluate, format)

## Business paragraph (how it shows up in the wild)

> “We need a single entry point that: (1) validates the record, (2) if valid, runs all eligibility rules and gets allow/deny + reasons, and (3) returns a result in a form the caller can use—e.g. a human-readable message for the CLI or a structured payload for an API. Validation, rule logic, and presentation must be separate so we can test and change each without touching the others.”

---

## What we’re training

- **Function boundaries:** validate / evaluate / format—each does one job.
- **Orchestration:** One function that only calls validate → evaluate → format in order and passes data; no business logic in the orchestrator.
- **Separation of concerns:** Validation = “is data usable?”; evaluation = “does it pass rules?”; format = “how do we present the result?”

---

## Industry tie-in

- **Testability:** Validate can be tested with invalid data; evaluate with valid data; format with mock decisions.
- **Reuse:** Same evaluate/format can sit behind CLI, API, or batch; only the “how we get input and send output” changes.
- **Auditability:** Clear steps make it obvious where a failure came from (validation vs rule).

---

## Canonical code (assumes Phases 1–3 done)

**1. Validate** (from Phase 2): returns `{"valid": True}` or `{"valid": False, "reason": "..."}`.

```python
def validate(record):
    if "age" not in record:
        return {"valid": False, "reason": "missing age"}
    if not isinstance(record["age"], (int, float)):
        return {"valid": False, "reason": "age not a number"}
    if record["age"] < 0 or record["age"] > 120:
        return {"valid": False, "reason": "age out of range"}
    return {"valid": True}
```

**2. Evaluate** (from Phase 3): assumes valid record; returns `{"allowed": bool, "reasons": [...]}`.

```python
def evaluate(record, rules):
    reasons = []
    for rule_fn in rules:
        result = rule_fn(record)
        if not result["passed"]:
            reasons.append(result["reason"])
    return {"allowed": len(reasons) == 0, "reasons": reasons}
```

**3. Format:** turns the decision into a string (or structure) for the caller. No validation or rule logic. We use one formatter that accepts either a validation result or an evaluation result so the orchestrator has a single “format this” step.

```python
def format_result(decision):
    """
    decision: either validation result {"valid": False, "reason": str}
    or evaluation result {"allowed": bool, "reasons": list}.
    """
    if "valid" in decision and not decision["valid"]:
        return "Validation failed: " + decision["reason"]
    if decision["allowed"]:
        return "Allowed"
    return "Denied: " + "; ".join(decision["reasons"])
```

**4. Orchestration:** thin glue—only calls the three steps and passes data.

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
```

Note: `format_result` accepts either a validation result (with `"valid"`) or an evaluation result (with `"allowed"`, `"reasons"`). In a fuller design you might use two formatters (one for validation, one for evaluation); the principle is the same: format only formats.

---

## Why this is canonical

| Choice | Reason |
|--------|--------|
| Validate / evaluate / format split | Each can be tested and changed independently; I/O stays at the edges. |
| Orchestrator is thin | `run_policy` only sequences calls; reading it tells you the full flow. |
| No I/O in validate or evaluate | They take data and return data; CLI or API does input/output. |
| Explicit data flow | Each function has clear inputs and outputs; no hidden globals. |

---

## Link to phase

This example implements the learning goals of [Phase 4 — Decomposition](../curriculum/phase_4_decomposition.md).
