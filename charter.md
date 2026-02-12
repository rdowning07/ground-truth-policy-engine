# 30-Hour Policy Engine Dojo Charter

## Mission
Build structural fluency in solving real business-rule problems using Python.

The objective is not to ship a product. The objective is to build reflexes:
- translate business language into code primitives
- place loops correctly over collections
- enforce guard clause discipline
- model state explicitly
- keep function boundaries crisp
- generate explainable decisions

## Scope
We will build a deterministic CLI that:
- stores records (e.g., users)
- evaluates rule functions over records
- combines rule results into allow/deny decisions
- returns multiple failure reasons in priority order
- handles missing/invalid data safely
- can be extended by adding new rules

## Non-negotiables
- No clever one-liners.
- No premature abstraction.
- No classes unless clearly required.
- No frameworks.
- Rules are pure (no mutation, no printing, no I/O).
- The learner writes first; mentor critiques.
- We prefer full evaluation (collect failures) over short-circuiting early.

## Definition of progress
Success means:
- can translate a business paragraph into code primitives without help
- can explain why the loop goes where it goes
- can write guard clauses intentionally
- can rebuild core logic from scratch

Failure mode to avoid:
- drifting into architecture/design discussions instead of practicing primitives

