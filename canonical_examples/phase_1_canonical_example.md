# Phase 1 — Canonical example: One rule, many records

## Business paragraph (how it shows up in the wild)

> “Our digital marketplace allows sellers to list items only if they are at least 18 years old. We have a batch of seller records (id and age). For each seller, we need to know whether they meet the age requirement. The result must list every seller and a clear pass/fail so that we can report eligibility and follow up on failures.”

---

## What we’re training

- **One rule:** “age >= 18.”
- **Many records:** a list of sellers.
- **Structured result per record:** for each seller, output something like “id, passed yes/no” so we can report and audit.

We use: a **loop** over the list, a **conditional** for the rule, and an **accumulator** (a list we build) to collect one result per record.

---

## Industry tie-in

- **Compliance:** Auditors need to see “who was evaluated and what was the outcome” for every record.
- **Determinism:** Same input list must always produce the same output list.
- **Explicit loop:** The code makes it obvious that we evaluate the rule once per record—no hidden iteration.

---

## Canonical code (assumes no prior Python)

Below is a single function that takes a list of records and returns a list of results. Each record is a dict with `id` and `age`; each result is a dict with `id` and `passed`.

```python
def evaluate_age_rule(records):
    """
    One rule: age must be >= 18.
    Many records: we loop over each record.
    Structured result: we return a list of {id, passed} for each record.
    """

    # Accumulator: we will build a list of results, one per record.
    results = []

    # Loop: do the same steps for each record in the list.
    for record in records:
        # Get the fields we need. (Assume record has "id" and "age".)
        user_id = record["id"]
        age = record["age"]

        # Conditional: the rule is "age >= 18".
        if age >= 18:
            passed = True
        else:
            passed = False

        # Append one structured result for this record.
        results.append({"id": user_id, "passed": passed})

    # Return the full list of results. Same length as input.
    return results
```

**Example use:**

- Input: `[{"id": 1, "age": 25}, {"id": 2, "age": 17}]`
- Output: `[{"id": 1, "passed": True}, {"id": 2, "passed": False}]`

---

## Why this is canonical

| Choice | Reason |
|--------|--------|
| One function, one job | The function only “evaluate this one rule over many records.” Easy to test and reuse. |
| Accumulator pattern | `results = []` then `results.append(...)` in the loop is the standard way to build a list from a loop. |
| Loop over records, rule inside | The loop is “for each record”; the if/else is “does this record pass the rule?” Clear and auditable. |
| Return data, no printing | Caller can print, log, or send to an API. The rule stays pure and deterministic. |
| Same structure per result | Every result has `id` and `passed`. Consistent shape makes reporting and debugging simple. |

---

## Link to phase

This example implements the learning goals of [Phase 1 — Deterministic evaluation](../curriculum/phase_1_deterministic_evaluation.md).
