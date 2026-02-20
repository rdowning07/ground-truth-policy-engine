# Reference curriculum: Phase 1 — Verbose code and comments (tutor walkthrough)

This document is a **reference curriculum** for Phase 1 (Python fundamentals + one rule, many records): explicit, step-by-step code with heavy comments, as a tutor would walk through it. Every example is runnable. No shortcuts, no clever one-liners—just one concept at a time.

**How to use:** Read each section; run the code (copy into a file or use the [single runnable file](reference_phase1_examples.py) that contains all examples in order). The comments are there to explain *what this line does* and *why we write it this way*.

**Tied to:** [Python fundamentals](python_fundamentals.md) (Stages 1–11) and [Phase 1 canonical example](canonical_examples/phase_1_canonical_example.md).

---

## 1. Script and print: run a file and see output

A script is a file of instructions. Python runs them from top to bottom. The simplest way to see something happen is `print(...)`.

```python
# We are in a file (e.g. example_1_script.py).
# When we run "python3 example_1_script.py", Python runs every line in order.

# This line sends the text "hello" to the terminal. Nothing else happens.
print("hello")

# This line sends two things: the text "Age check: " and the value of 20.
# The comma means "print these one after the other, with a space between."
print("Age check:", 20)
```

**Run it:** Save as `example_1_script.py`, then in the terminal: `python3 example_1_script.py`. You should see two lines of output.

---

## 2. Values and types: the data we work with

Values are the actual data. Every value has a type. We don’t declare the type—Python knows it from how we write the value.

```python
# --- Numbers (integers and decimals) ---
# An integer: a whole number. No quotes.
age_years = 18

# A decimal (float). Used when we need fractions.
age_with_months = 18.5

# --- Strings (text) ---
# A string: characters in double quotes. Used for ids, regions, messages.
user_region = "US"
error_message = "missing age"

# --- Booleans (yes/no) ---
# Only two values: True and False. Capital T and F.
# We use these for pass/fail, eligible/not eligible.
is_eligible = True
passed_check = False

# We can print any of these to see their value.
print("age_years is", age_years)
print("user_region is", user_region)
print("is_eligible is", is_eligible)
```

**What we just did:** We stored different kinds of data (number, text, yes/no). In policy logic we compare numbers (e.g. age >= 18), store text (e.g. region), and set booleans (passed = True or False).

---

## 3. Variables: giving a value a name

A variable is a name that refers to a value. We create it with `name = value`. After that, using the name is the same as using the value.

```python
# Create a variable by writing: name = value
# The name is on the left, the value on the right of the equals sign.
age = 25

# Now "age" means 25. We can use it in expressions.
# Here we compare: is age greater than or equal to 18?
# The result of that comparison is True or False.
age_meets_minimum = age >= 18

# We can print the variable to see what we stored.
print("age is", age)
print("age_meets_minimum is", age_meets_minimum)

# We can reuse the variable. Later we might assign a different value (e.g. in a loop).
# For now we just show that we can use "age" again.
next_age_to_check = age + 1
print("next_age_to_check would be", next_age_to_check)
```

**What we just did:** We gave the value 25 the name `age`. Then we used `age` in a comparison and stored that result in another variable. Variables let us refer to data by a meaningful name instead of repeating the raw value.

---

## 4. Comparisons: expressions that produce True or False

A comparison is an expression that evaluates to `True` or `False`. We use these inside conditionals and to set variables like `passed`.

```python
# We'll use these variables in the comparisons below.
age = 20
minimum_age = 18

# Equal: == (two equals signs). True only if both sides are the same value.
print("age == 20 is", age == 20)   # True
print("age == 18 is", age == 18)   # False

# Not equal: !=
print("age != 0 is", age != 0)     # True

# Greater than: >
print("age > minimum_age is", age > minimum_age)   # True

# Greater than or equal: >=  (this is the one we use for "at least 18")
print("age >= minimum_age is", age >= minimum_age) # True
print("age >= 21 is", age >= 21)                    # False

# Less than and less than or equal: < and <=
print("age < 21 is", age < 21)     # True
print("age <= 20 is", age <= 20)   # True

# We can store the result of a comparison in a variable.
# That variable will be either True or False.
passed = age >= minimum_age
print("passed is", passed)
```

**What we just did:** We used comparison operators to produce booleans. The one we care most about for the age rule is `age >= 18`. Business rules are conditions; comparisons turn them into True or False.

---

## 5. Conditionals: if / else — branching

A conditional runs different code depending on whether a condition is True or False. In Python we use `if condition:` and optionally `else:`. The code that belongs to the if (or else) is **indented**—usually 4 spaces. Indentation is part of the syntax; it defines which lines are “inside” the if or else.

```python
# We have a variable that holds an age. We want to set "passed" to True or False
# depending on whether that age is at least 18.
age = 17

# The condition goes after "if" and before the colon.
# If the condition is True, Python runs the indented block under "if".
# If the condition is False, Python skips that block and runs the block under "else" (if there is one).
if age >= 18:
    # This line runs only when age >= 18 is True.
    # We indent it with 4 spaces so Python knows it belongs to the if.
    passed = True
else:
    # This line runs only when age >= 18 is False (i.e. age is less than 18).
    passed = False

# After the if/else, we continue with no indentation.
print("age", age, "-> passed is", passed)

# Run this again with age = 18 or age = 25 to see passed become True.
```

**What we just did:** We branched: one path when the condition is true (set passed = True), another when it’s false (set passed = False). This is how we implement “the rule” in code.

---

## 6. Lists: ordered collections

A list is an ordered collection of values. We write it with square brackets. We use lists to hold “many records” (e.g. many users). We can append to a list and get its length.

```python
# An empty list: no elements yet.
results = []

# A list with values. The order is kept: first 1, then 2, then 3.
numbers = [1, 2, 3]

# A list of strings.
regions = ["US", "UK", "CA"]

# We can get the number of elements with len(...).
print("len(numbers) is", len(numbers))

# We can append one value to the end of a list.
# The list changes; we don't assign to a new variable—we modify the same list.
results.append("first result")
results.append("second result")
print("results is now", results)
print("len(results) is", len(results))

# We can get one element by its position (index). The first element is index 0.
first_number = numbers[0]
print("first element of numbers is", first_number)
```

**What we just did:** We created lists, appended to one, and read an element by index. In Phase 1 we’ll have a list of records and we’ll build a list of results by appending one result per record.

---

## 7. Dicts: key–value records

A dict maps keys to values. We use it for one “record” with named fields (e.g. id, age). We write a dict with curly braces and key: value pairs. We read a value with `record["key"]`.

```python
# One record: a dict with keys "id" and "age".
# Keys are usually strings; values can be numbers, strings, booleans, etc.
record = {"id": 1, "age": 25}

# To get the value for a key, we use square brackets and the key name.
user_id = record["id"]
age = record["age"]
print("user_id is", user_id)
print("age is", age)

# We can build a new dict from variables. This is how we form one "result" per record.
passed = True
one_result = {"id": user_id, "passed": passed}
print("one_result is", one_result)

# A list of records: this is our "many records" that we'll loop over.
records = [
    {"id": 1, "age": 25},
    {"id": 2, "age": 17},
]
print("we have", len(records), "records")
```

**What we just did:** We represented one record as a dict, read its fields by key, and built another dict for one result. We also made a list of two records. In the full example we’ll loop over that list and produce one result dict per record.

---

## 8. Loop: for each item in a list

A for-loop runs once for each item in a list. We write `for item in my_list:` and then indent the block that should run for each item. Inside the block, `item` is the current element.

```python
# Our list of records (same shape as in the Phase 1 example).
records = [
    {"id": 1, "age": 25},
    {"id": 2, "age": 17},
]

# The loop: "for each record in the list records, do the following."
# The variable "record" will be the first dict, then the second, then the next, etc.
for record in records:
    # Everything indented here runs once per record.
    # First time: record is {"id": 1, "age": 25}
    # Second time: record is {"id": 2, "age": 17}
    user_id = record["id"]
    age = record["age"]
    # We're not applying the rule yet—just showing we can pull out the fields.
    print("Record id", user_id, "has age", age)
# When the loop finishes, we continue here (no indentation).
print("Loop finished.")
```

**What we just did:** We visited each record in the list, one at a time, and did the same steps (get id and age, print them). In the full example we’ll add the conditional (age >= 18) and the accumulator inside this loop.

---

## 9. Accumulator: build a list inside the loop

An accumulator is a variable we create *before* the loop and *update inside* the loop. For a list of results, we start with an empty list and append one result each time through the loop.

```python
records = [
    {"id": 1, "age": 25},
    {"id": 2, "age": 17},
]

# The accumulator: we create it before the loop so it exists for the whole loop.
# We start with an empty list. We will append one result per record.
results = []

for record in records:
    user_id = record["id"]
    age = record["age"]
    # For this example we'll use a simple rule: passed if age >= 18.
    if age >= 18:
        passed = True
    else:
        passed = False
    # Build one result for this record (a small dict with id and passed).
    one_result = {"id": user_id, "passed": passed}
    # Add it to the accumulator. The list grows by one element each time.
    results.append(one_result)

# After the loop, results has one element per record, in the same order.
print("results is", results)
```

**What we just did:** We combined the loop, the conditional, and the accumulator. We built the full list of results by appending one result per record. The only thing missing is wrapping this in a function and returning `results` instead of printing.

---

## 10. Function: name the block and return a value

A function is a named block of code that takes inputs (parameters) and can return a value. We define it with `def name(parameters):` and indent the body. We return a value with `return something`.

```python
# We define a function with "def", the name, parentheses with parameter names, and a colon.
# The body is indented. We can return a value with "return".
def add_one(x):
    # x is whatever value the caller passed in. We add 1 to it.
    result = x + 1
    # Return sends that value back to the caller. No further code in this function runs after return.
    return result

# To use the function we "call" it: function_name(argument).
# The argument (e.g. 10) becomes the value of x inside the function.
answer = add_one(10)
print("add_one(10) is", answer)
```

**What we just did:** We defined a function with one parameter and a return value. The same pattern applies to our evaluation function: we’ll have a parameter `records` and we’ll `return results` at the end.

---

## 11. Full example: one rule, many records (Phase 1 style)

This is the same logic as the [Phase 1 canonical example](canonical_examples/phase_1_canonical_example.md), with every step commented as a tutor would explain it.

```python
def evaluate_age_rule(records):
    """
    One rule: age must be >= 18.
    We take a list of records (each has "id" and "age") and return a list of
    results (each has "id" and "passed"). Same number of results as records.
    """

    # Step 1: Create the accumulator. It must exist before the loop so we can
    # append to it every time through the loop. It starts empty.
    results = []

    # Step 2: Loop over every record in the list. The variable "record" holds
    # one record at a time: first the first dict, then the second, and so on.
    for record in records:

        # Step 3: Get the fields we need from this record. We assume each
        # record has the keys "id" and "age". (Phase 2 will handle missing keys.)
        user_id = record["id"]
        age = record["age"]

        # Step 4: Apply the rule. The rule is "age must be at least 18."
        # We use a conditional: if the condition is True, set passed to True;
        # otherwise set it to False.
        if age >= 18:
            passed = True
        else:
            passed = False

        # Step 5: Build one result for this record. It's a small dict with
        # the same id and the pass/fail outcome. We'll add it to the accumulator.
        one_result = {"id": user_id, "passed": passed}

        # Step 6: Append this result to the accumulator. The list "results"
        # grows by one element each time we go through the loop.
        results.append(one_result)

    # Step 7: We've processed every record. Return the full list of results.
    # The caller gets one result per record, in the same order. We don't print
    # here—we just return. That keeps the function pure and deterministic.
    return results


# --- Example use (so you can run this and see output) ---
if __name__ == "__main__":
    # Two sample records: one passes the age rule, one fails.
    sample_records = [
        {"id": 1, "age": 25},
        {"id": 2, "age": 17},
    ]
    # Call the function. It returns a list of results.
    output = evaluate_age_rule(sample_records)
    # Print so we can see the result.
    print("Input records:", sample_records)
    print("Output results:", output)
```

**What we just did:** We put the accumulator, loop, conditional, and return inside one function. The function takes a list of records and returns a list of results. No printing inside the function—only reading the record and returning data. That’s the Phase 1 pattern.

**Run it:** Save as a `.py` file and run with `python3`. You should see the input list and the output list (id 1 passed, id 2 failed).

---

## All examples in one runnable file

The file [reference_phase1_examples.py](reference_phase1_examples.py) contains all of the above examples in order. Run:

```bash
python3 reference_phase1_examples.py
```

to execute each section and see the output. Use it as a reference when you’re implementing Phase 1 in `src/engine.py`.

**Next:** After Phase 1, see [REFERENCE_CURRICULUM_PHASE2.md](REFERENCE_CURRICULUM_PHASE2.md) for guard clauses and validation (Phase 2).

---

Back to [Python fundamentals](python_fundamentals.md) · [Curriculum overview](curriculum_overview.md).
