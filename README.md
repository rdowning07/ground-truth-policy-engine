# Ground Truth Policy Engine
A 30-hour backend fluency dojo: translate business rules into deterministic Python control flow.

## What this is
This repo is a learning scaffold, not a production policy engine.

The goal is to build "blank-page fluency" for real-world backend work:
- read a business paragraph
- identify the primitive being tested (loops, guards, composition, decomposition, state)
- translate into clear Python
- produce deterministic, explainable decisions

The working artifact is a simple CLI that evaluates eligibility for a digital marketplace feature.

## What this is not
- A DSL or JSON-driven rules platform (not yet)
- A framework project
- A resume-polish exercise
- An architecture playground

## How to run
This project is intentionally lightweight.

### Option A: Run directly
```bash
python3 src/engine.py

