"""
Reference curriculum: Day 1 — Verbose code and comments (tutor walkthrough).

This file contains all the examples from REFERENCE_CURRICULUM_PHASE1.md in order.
Run: python3 reference_phase1_examples.py

Each section is commented as a tutor would explain it. No clever code—explicit and boring.
"""
# Pylint: pedagogical names (age, passed, user_id) and deliberate if/else for teaching.
# pylint: disable=invalid-name,simplifiable-if-statement,redefined-outer-name

from typing import Any

# =============================================================================
# 1. Script and print: run a file and see output
# =============================================================================
# When we run this file, Python runs every line in order.
# print(...) sends text (and values) to the terminal.

print("--- Example 1: Script and print ---")
print("hello")
print("Age check:", 20)

# =============================================================================
# 2. Values and types: the data we work with
# =============================================================================
# Values are the actual data. Every value has a type. We don't declare the type.

print("\n--- Example 2: Values and types ---")
age_years = 18
age_with_months = 18.5
user_region = "US"
error_message = "missing age"
is_eligible = True
passed_check = False
print("age_years is", age_years)
print("user_region is", user_region)
print("is_eligible is", is_eligible)

# =============================================================================
# 3. Variables: giving a value a name
# =============================================================================
# We create a variable with name = value. Then we use the name instead of the value.

print("\n--- Example 3: Variables ---")
age = 25
age_meets_minimum = age >= 18
print("age is", age)
print("age_meets_minimum is", age_meets_minimum)
next_age_to_check = age + 1
print("next_age_to_check would be", next_age_to_check)

# =============================================================================
# 4. Comparisons: expressions that produce True or False
# =============================================================================
# A comparison evaluates to True or False. We use these in conditionals.

print("\n--- Example 4: Comparisons ---")
age = 20
minimum_age = 18
print("age == 20 is", age == 20)
print("age == 18 is", age == 18)
print("age != 0 is", age != 0)
print("age > minimum_age is", age > minimum_age)
print("age >= minimum_age is", age >= minimum_age)
print("age >= 21 is", age >= 21)
print("age < 21 is", age < 21)
print("age <= 20 is", age <= 20)
passed = age >= minimum_age
print("passed is", passed)

# =============================================================================
# 5. Conditionals: if / else — branching
# =============================================================================
# We run different code depending on whether a condition is True or False.
# Indentation (4 spaces) defines which lines belong to the if or else.

print("\n--- Example 5: Conditionals ---")
age = 17
if age >= 18:
    passed = True
else:
    passed = False
print("age", age, "-> passed is", passed)

# =============================================================================
# 6. Lists: ordered collections
# =============================================================================
# A list is [a, b, c]. We append to it and get length with len(...).
# We use a different variable name here so "results" is not typed as list[str]
# for mypy when we later use "results" for list of dicts in examples 9 and 11.

print("\n--- Example 6: Lists ---")
collected: list[str] = []
numbers = [1, 2, 3]
regions = ["US", "UK", "CA"]
print("len(numbers) is", len(numbers))
collected.append("first result")
collected.append("second result")
print("results is now", collected)
print("len(results) is", len(collected))
first_number = numbers[0]
print("first element of numbers is", first_number)

# =============================================================================
# 7. Dicts: key–value records
# =============================================================================
# A dict maps keys to values. We use it for one record with named fields.

print("\n--- Example 7: Dicts ---")
record = {"id": 1, "age": 25}
user_id = record["id"]
age = record["age"]
print("user_id is", user_id)
print("age is", age)
passed = True
one_result = {"id": user_id, "passed": passed}
print("one_result is", one_result)
records = [
    {"id": 1, "age": 25},
    {"id": 2, "age": 17},
]
print("we have", len(records), "records")

# =============================================================================
# 8. Loop: for each item in a list
# =============================================================================
# for record in records: ... runs the indented block once per record.

print("\n--- Example 8: Loop ---")
records = [
    {"id": 1, "age": 25},
    {"id": 2, "age": 17},
]
for record in records:
    user_id = record["id"]
    age = record["age"]
    print("Record id", user_id, "has age", age)
print("Loop finished.")

# =============================================================================
# 9. Accumulator: build a list inside the loop
# =============================================================================
# We create results = [] before the loop and results.append(...) inside the loop.

print("\n--- Example 9: Accumulator ---")
records = [
    {"id": 1, "age": 25},
    {"id": 2, "age": 17},
]
results = []
for record in records:
    user_id = record["id"]
    age = record["age"]
    if age >= 18:
        passed = True
    else:
        passed = False
    one_result = {"id": user_id, "passed": passed}
    results.append(one_result)
print("results is", results)

# =============================================================================
# 10. Function: name the block and return a value
# =============================================================================
# def name(parameters): ... return value

print("\n--- Example 10: Function ---")


def add_one(x: int) -> int:
    """Return x + 1. Used to show function definition and return."""
    result = x + 1
    return result


answer = add_one(10)
print("add_one(10) is", answer)

# =============================================================================
# 11. Full example: one rule, many records (Phase 1 style)
# =============================================================================
# Same logic as the Phase 1 canonical example, with step-by-step comments.


def evaluate_age_rule(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    One rule: age must be >= 18.
    We take a list of records (each has "id" and "age") and return a list of
    results (each has "id" and "passed"). Same number of results as records.
    """
    # Step 1: Create the accumulator. It must exist before the loop.
    results: list[dict[str, Any]] = []

    # Step 2: Loop over every record in the list.
    for record in records:
        # Step 3: Get the fields we need from this record.
        user_id = record["id"]
        age = record["age"]

        # Step 4: Apply the rule. The rule is "age must be at least 18."
        if age >= 18:
            passed = True
        else:
            passed = False

        # Step 5: Build one result for this record.
        one_result = {"id": user_id, "passed": passed}

        # Step 6: Append this result to the accumulator.
        results.append(one_result)

    # Step 7: Return the full list of results. No printing—just return.
    return results


print("\n--- Example 11: Full Phase 1-style function ---")
sample_records = [
    {"id": 1, "age": 25},
    {"id": 2, "age": 17},
]
output = evaluate_age_rule(sample_records)
print("Input records:", sample_records)
print("Output results:", output)

print("\n--- Done. See REFERENCE_CURRICULUM_PHASE1.md for the tutor walkthrough. ---")
