# Phase 3 — Canonical example: Rule composition

## Business paragraph (how it shows up in the wild)

> “A seller is allowed to list items only if: (1) they are at least 18, (2) their account is verified, and (3) they are not in a restricted region. We need one allow/deny decision per seller. If we deny, we must return all reasons that failed (in order: age, then verification, then region) so that support and the user know exactly what to fix.”

---

## What we’re training

- **Rule functions:** One function per rule; each returns the same shape: passed + optional reason.
- **Full evaluation:** Run all rules; collect every failure (no short-circuit).
- **Composition:** Combine results into one allow/deny and an ordered list of reasons.

---

## Industry tie-in

- **Transparency:** Returning all reasons supports appeals and self-service (“fix these three things”).
- **Consistency:** Same order of rules and reasons every time—deterministic and auditable.
- **Maintainability:** Adding a new rule = add one function and append it to the list; no branching spaghetti.

---

## Canonical code (assumes no prior Python)

Each rule is a **pure function**: same inputs → same outputs; no printing, no I/O, no mutating the record.

```python
def rule_age(record):
    """Rule: age >= 18."""
    if record.get("age", 0) >= 18:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "age below minimum"}


def rule_verified(record):
    """Rule: account must be verified."""
    if record.get("verified", False) is True:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "account not verified"}


def rule_region(record):
    """Rule: not in restricted region."""
    restricted = ["XX", "YY"]  # example codes
    if record.get("region", "") not in restricted:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "region restricted"}
```

Composer: run all rules, collect failures in order, then allow only if all passed.

```python
def evaluate_all_rules(record, rules):
    """
    rules: list of rule functions (e.g. [rule_age, rule_verified, rule_region]).
    Full evaluation: run every rule, collect every failure.
    Return: allowed (bool), reasons (list of strings, in rule order).
    """
    reasons = []

    for rule_fn in rules:
        result = rule_fn(record)
        if not result["passed"]:
            reasons.append(result["reason"])

    allowed = len(reasons) == 0
    return {"allowed": allowed, "reasons": reasons}
```

**Example:**

- Record: `{"age": 17, "verified": False, "region": "US"}`
- Rules: `[rule_age, rule_verified, rule_region]`
- Result: `{"allowed": False, "reasons": ["age below minimum", "account not verified"]}`  
  (region passed, so not in reasons; order matches rule order.)

---

## Why this is canonical

| Choice | Reason |
|--------|--------|
| One function per rule | Easy to test and document; add/remove rules without touching others. |
| Same return shape | Every rule returns `{"passed": ..., "reason": ...}` so the composer loop is simple. |
| Full evaluation | We never stop at the first failure; we collect all reasons (charter non-negotiable). |
| Ordered reasons | The order of `reasons` matches the order of rules—predictable and business-friendly. |
| Pure rules | No side effects; rules can be reused in CLI, API, or batch. |

---

## Link to phase

This example implements the learning goals of [Phase 3 — Rule composition](../curriculum/phase_3_rule_composition.md).
