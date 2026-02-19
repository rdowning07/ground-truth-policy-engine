# Reference curriculum: Day 3 — Rule composition (tutor walkthrough)

This document is a **reference curriculum** for Phase 3: explicit, step-by-step code with heavy comments for **rule functions**, **same return shape**, **failure accumulation**, and **allow/deny with reasons**. Every example is runnable. No shortcuts—one concept at a time.

**Prerequisite:** You have completed [Phase 1](curriculum/phase_1_deterministic_evaluation.md) (one rule, many records) and [Phase 2](curriculum/phase_2_guard_clauses_validation.md) (validation, guard clauses). See [Day 1](REFERENCE_CURRICULUM_DAY1.md) and [Day 2](REFERENCE_CURRICULUM_DAY2.md) references.

**How to use:** Read each section; run the code (copy into a file or use the [single runnable file](reference_day3_examples.py)). The comments explain *what this line does* and *why we write it this way*.

**Tied to:** [Phase 3 — Rule composition](curriculum/phase_3_rule_composition.md) and [Phase 3 canonical example](canonical_examples/phase_3_canonical_example.md).

---

## 1. One rule as a function: same shape every time

A **rule function** takes a (validated) record and returns one result: either passed or failed, and if failed, a reason. Every rule returns the **same shape** so we can loop over rules and handle results uniformly.

```python
# This rule: age must be at least 18.
# We return a dict with "passed" (True or False) and "reason" (None if passed, else a string).
def rule_age(record):
    """Rule: age >= 18."""
    # Use .get so we don't crash if "age" is missing; 0 means "missing" fails the rule.
    if record.get("age", 0) >= 18:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "age below minimum"}


# Try it. Same input always gives same output (deterministic).
print(rule_age({"age": 25}))
print(rule_age({"age": 17}))
```

**What we just did:** We turned one business rule into a pure function. It doesn't print or change the record; it only reads and returns. The return shape is always `{"passed": ..., "reason": ...}`.

---

## 2. Same return shape: why it matters

Every rule must return the same structure. Then the code that **calls** the rules doesn't need to know which rule ran—it just checks `result["passed"]` and `result["reason"]`. That lets us add or remove rules without changing the composer.

```python
# Rule 1 returns this shape when it passes:
# {"passed": True, "reason": None}

# Rule 2 returns this shape when it fails:
# {"passed": False, "reason": "account not verified"}

# So we can write one loop: for each rule, get result; if not result["passed"], collect result["reason"].
# We never have to say "if rule is age then do X, else if rule is verified then do Y."
```

**What we just did:** We didn't write new code—we stated the convention. Every rule returns `{"passed": bool, "reason": None or str}`. The composer only needs that.

---

## 3. A second and third rule function

We add more rules as separate functions. Each one takes the record and returns the same shape. We use `.get(key, default)` so missing keys don't raise errors (validation may have run first, or we're being defensive).

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
    restricted = ["XX", "YY"]
    if record.get("region", "") not in restricted:
        return {"passed": True, "reason": None}
    return {"passed": False, "reason": "region restricted"}


# Each rule is independent. We can test them one at a time.
print(rule_verified({"verified": True}))
print(rule_verified({"verified": False}))
print(rule_region({"region": "US"}))
print(rule_region({"region": "XX"}))
```

**What we just did:** We have three rule functions. Each is pure and returns the same shape. The order we define them is the order we'll use for "reasons" (age first, then verification, then region).

---

## 4. List of rule functions: pass rules in

We put the rule functions in a **list**. Then we can loop over that list and call each function with the same record. The list defines the **order** of evaluation—and the order of reasons when we deny.

```python
# The list holds functions. We don't call them yet—we pass the list to the composer.
rules = [rule_age, rule_verified, rule_region]

# To call one rule: rules[0](record) is the same as rule_age(record).
record = {"age": 25, "verified": True, "region": "US"}
result_age = rules[0](record)
result_verified = rules[1](record)
result_region = rules[2](record)
print("Age:", result_age)
print("Verified:", result_verified)
print("Region:", result_region)
```

**What we just did:** We stored the three rule functions in a list. Calling `rules[i](record)` runs the i-th rule. The composer will do this in a loop so we don't have to write three separate lines.

---

## 5. Run all rules and collect results

We loop over the list of rule functions. For each rule we call it with the record and get back a result. We don't stop at the first failure—we run **every** rule every time. That way we can collect **all** failure reasons.

```python
def run_all_rules(record, rules):
    """Run each rule and collect every result. No short-circuit."""
    results = []
    for rule_fn in rules:
        result = rule_fn(record)
        results.append(result)
    return results


rules = [rule_age, rule_verified, rule_region]
record = {"age": 17, "verified": False, "region": "US"}
out = run_all_rules(record, rules)
print("All results:", out)
```

**What we just did:** We ran every rule and stored each result in a list. So we get three dicts (one per rule). Next we'll pull out just the failure reasons and decide allow/deny.

---

## 6. Collect only failure reasons (in order)

We don't need the full result for every rule—we need the **reasons** for the ones that failed. We loop over the results and whenever `result["passed"]` is False, we append `result["reason"]` to a list. The order of that list matches the order of the rules.

```python
def collect_failure_reasons(results):
    """Build a list of reasons for every result that did not pass."""
    reasons = []
    for result in results:
        if not result["passed"]:
            reasons.append(result["reason"])
    return reasons


# From the previous example: record had age 17 and verified False, region US.
# So we expect two reasons: age below minimum, account not verified.
results = run_all_rules(record, rules)
reasons = collect_failure_reasons(results)
print("Failure reasons (in rule order):", reasons)
```

**What we just did:** We turned the list of results into a list of failure reasons only. Order is preserved. If all rules passed, reasons is empty.

---

## 7. Allow only if all passed

**Allow** means every rule passed—so the list of reasons is empty. **Deny** means at least one rule failed—so the list of reasons has one or more items. We combine that into one decision and return it with the reasons.

```python
def allow_or_deny(reasons):
    """Allowed if no failures; otherwise denied with the list of reasons."""
    allowed = len(reasons) == 0
    return {"allowed": allowed, "reasons": reasons}


# Same record as before: two failures.
decision = allow_or_deny(reasons)
print("Decision:", decision)
```

**What we just did:** We computed one boolean (allowed) and returned it with the reasons. The caller gets a single allow/deny and a list they can show to the user or logs.

---

## 8. Full composer: evaluate_all_rules (Phase 3 style)

We put the pieces together: run all rules, collect failure reasons in order, then allow only if there are no reasons. This matches the [Phase 3 canonical example](canonical_examples/phase_3_canonical_example.md).

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


# Example: record fails age and verified, passes region.
record = {"age": 17, "verified": False, "region": "US"}
rules = [rule_age, rule_verified, rule_region]
decision = evaluate_all_rules(record, rules)
print("Record:", record)
print("Decision:", decision)
```

**What we just did:** One function does it all: loop over rules, collect reasons for failures, then set allowed = (no reasons). No short-circuit—we always run every rule. The result is one allow/deny and an ordered list of reasons.

---

## 9. Full example: three rules, one allow/deny (Phase 3 style)

This is the same logic as the canonical example, with the three rules and the composer in one place. Run it to see allowed vs denied and the list of reasons.

```python
# Define the three rules (same as in section 3).
# Define evaluate_all_rules (same as in section 8).
# Then:
record_pass = {"age": 25, "verified": True, "region": "US"}
record_fail = {"age": 17, "verified": False, "region": "US"}
print(evaluate_all_rules(record_pass, rules))
print(evaluate_all_rules(record_fail, rules))
```

**What we just did:** We showed that the same composer works for any record. Pass record gets allowed with no reasons; fail record gets denied with two reasons (age, account not verified). Region passed so it's not in the list.

---

## All examples in one runnable file

The file [reference_day3_examples.py](reference_day3_examples.py) contains all of the above examples in order. Run:

```bash
python3 reference_day3_examples.py
```

Use it as a reference when implementing Phase 3 in `src/engine.py`.

**Previous:** [REFERENCE_CURRICULUM_DAY2.md](REFERENCE_CURRICULUM_DAY2.md) (Phase 2: guard clauses, validation).

---

Back to [Phase 3 curriculum](curriculum/phase_3_rule_composition.md) · [Curriculum overview](curriculum_overview.md).
