# Roadmap: Personal Project 1 and the Boot.dev Python → Go path

This repo is **Personal Project 1** (course 12) on the Boot.dev Backend Developer Path (Python & Go). The plan is to complete the agreed curriculum work, submit, then **continue iterating** and **connect extension specs to the Boot.dev path** as you complete later courses. This doc is for the author; the repo is public on GitHub and may be read by trusted coders and reviewers.

**Path:** Python → Go (not TypeScript). **Capstone:** No decision yet; options are listed below.

---

## Agreed work: what the five phases and Phase 6 are supposed to do

The curriculum defines the following. Completing this is “the work as agreed upon” for Personal Project 1.

### Phase 1 — Deterministic evaluation (Hours 1–6)

- **Goal:** Evaluate **one rule** (e.g. age >= 18) across **many records** and produce a **structured result per record** (e.g. id + passed/not passed).
- **Output:** One function that takes a list of records (dicts with id, age) and returns a list of results (dicts with id, passed). Loop over records; for each record, apply the conditional; use an accumulator (`results = []`, `results.append(...)`). No printing inside the rule; return data only. Deterministic: same input list → same output list.

### Phase 2 — Guard clauses + validation (Hours 7–12)

- **Goal:** **Validate before evaluating.** Reject or fail safely when data is missing, wrong type, or out of range; return **structured failures** (e.g. `valid: False`, `reason: "missing age"`) distinct from rule failures (e.g. `reason: "age below minimum"`).
- **Output:** Guard clauses at the start of the flow (early return on invalid data). Validation checks: field present, correct type, in range (e.g. age 0–120). For each record: if validation fails, add a validation result to output; if valid, run the rule and add the rule result. No silent defaults for missing data.

### Phase 3 — Rule composition (Hours 13–18)

- **Goal:** **Multiple rules** (e.g. age, verified, region); **one allow/deny** per record; **all failure reasons** collected (no short-circuit), in a **fixed order**.
- **Output:** One function per rule; each returns the same shape (e.g. `passed` + optional `reason`). A composer runs all rules for a record and aggregates: allow only if every rule passed; deny with a list of all failure reasons in rule order. Pure rules (no I/O, no mutation inside rules).

### Phase 4 — Decomposition (Hours 19–22)

- **Goal:** Separate **validate**, **evaluate**, and **format** into distinct functions; **orchestration** that only calls them in order (no business logic in the orchestrator).
- **Output:** `validate(record)` → valid/invalid + reason. `evaluate_rules(record, rules)` → allowed/denied + reasons (assumes valid record). `format_result(decision)` → string or structure for the caller. One entry point (e.g. `run_policy(record, rules)`) that: validate → if invalid return formatted failure; else evaluate → return formatted result. I/O and formatting only at the edges.

### Phase 5 — Stateful CLI (Hours 23–28)

- **Goal:** A **command-line interface** that maintains an **in-memory store** of users and **dispatches** commands: add, list, eval, quit.
- **Output:** A loop that reads input (e.g. `add <id> <age> <verified>`, `list`, `eval <id>`, `quit`). One store (e.g. list of records) that changes only when `add` is called. `list` prints all users; `eval <id>` finds the user, runs validate → evaluate → format, and prints the result. No `print` or `input` inside validate, evaluate, or rule functions; CLI layer does all I/O.

### Phase 6 — Rebuild (Hours 29–30)

- **Goal:** Reproduce the **core engine structure** (validate → evaluate → format, rules, CLI with add/list/eval) **from scratch** in a new file (e.g. `rebuild/scratch.py`) **without copying** from the main engine. Proves you can rebuild the patterns from memory.

---

## Roadmap: finish → submit → iterate and connect specs to the path

1. **Finish the agreed work.** Complete Phases 1–6 as above. Use the [curriculum](curriculum_overview.md), [canonical examples](canonical_examples/), and [recommended pacing](curriculum_overview.md#recommended-pacing-and-session-boundaries).
2. **Submit Personal Project 1.** README with what the project does, how to clone and run, and that it’s Boot.dev Backend path, Personal Project 1 (~30 hours). Code on GitHub.
3. **Continue the Boot.dev path.** Courses 13 → 14 → … → 21 (Learn Go, HTTP Clients, Pokedex, SQL, Blog Aggregator, HTTP Servers, File Servers, Docker, Pub/Sub).
4. **Iterate on this repo by connecting specs to the path.** As you complete each relevant course, you can add an **optional extension spec** to this project (or a sibling repo) that ties that course to the policy engine. The table below maps **Boot.dev course → optional spec idea** so you can choose what to implement and in what order.

---

## Specs connected to the Boot.dev path (Python → Go)

Use this to decide what to build *after* the agreed work, in line with the path. Each row is an optional spec you could add once you’ve done the corresponding course. No obligation to do all (or any); this is for continued iteration.

| After course | Optional spec idea (connect course to this project) |
|--------------|-----------------------------------------------------|
| **12 done** (this project submitted) | **Polish:** README (what it is, how to run, Boot.dev Personal Project 1). Optional: one pytest or script that runs the engine on a fixed input and asserts the output. |
| **13. Learn Go** | **Port the core:** Implement the same pipeline (validate → evaluate → format, one or two rules) in Go in a `go/` directory or a separate repo. Same behavior, same “contract” (input/output shapes); proves you can translate the logic. |
| **14–15. HTTP Clients, Pokedex** | **Call from Go (optional):** A small Go program that calls an HTTP endpoint (if you add one later) or shells out to `python3 src/engine.py` with JSON input; parse result. Lightweight way to “wire” Go to this repo. Or skip and keep engine as standalone. |
| **16. Learn SQL** | **Persistence around the engine:** A spec to load records from a SQLite (or other) table, run the existing validate/evaluate/format pipeline, and write results to a table or file. Engine stays pure; a new script or module does “load → run engine → store.” |
| **18. Learn HTTP Servers** | **Thin API:** A minimal HTTP server (e.g. Go or Python/Flask/FastAPI) that exposes one or two endpoints: e.g. POST a list of records → return evaluation results. The policy engine is the core; the server is a thin wrapper. Could live in this repo (e.g. `api/`) or a sibling. |
| **20. Learn Docker** | **Containerize:** Dockerfile (and optional compose) to run the CLI or the API (if added). Document how to build and run. |
| **21. Learn Pub/Sub** | **Optional:** A spec to consume “evaluate this user” messages from a queue, run the engine, and publish results. Keeps engine unchanged; adapter layer does I/O. |

You can turn any of these into a short spec (acceptance criteria, file/place in repo) when you’re ready; this doc only proposes the link between course and idea.

---

## Capstone options (no commitment yet)

When you reach course 22 (Capstone), you can choose among these or something else. No need to decide now.

- **Option A — Reuse this project’s semantics in Go:** Build a Go service that implements the same policy (validate → evaluate → return reasons), with HTTP API and SQL storage. This repo is the “reference implementation”; the Capstone is “that logic in a deployable backend.” Good if you want one narrative across Personal Project 1 and Capstone.
- **Option B — New Capstone, this repo standalone:** Do a different Capstone (e.g. Blog Aggregator–style or another idea). Keep this repo as your first portfolio piece; link to it from your portfolio or resume as “Personal Project 1: policy/eligibility CLI in Python.”
- **Option C — Extend this repo into a “mini backend”:** Add to this repo (or a sibling): HTTP API (after 18), SQL (after 16), Docker (after 20). The Capstone could be “this project, plus API + DB + containerized.” Less “new project” than “this project grown.”
- **Option D — Hybrid:** Capstone is a new Go service that *calls* or *reimplements* this engine’s contract (e.g. same request/response shape). Lets you show both “Python rule engine” and “Go service that uses it or mirrors it.”

---

## Audience and visibility

- **Primary:** The author (you), for planning and iteration.
- **Also:** Trusted coders and anyone viewing the repo on GitHub. The doc is written so that reviewers can see what “agreed work” means, how the project fits the Boot.dev path, and what optional specs are about.
- **README:** Consider adding a line such as: “How this fits the Boot.dev path and what’s next: see [BOOTDEV_ROADMAP.md](BOOTDEV_ROADMAP.md).”

---

## Summary

- **This project is Personal Project 1** on the Boot.dev Backend path (Python → Go).
- **Agreed work** = Phases 1–6 as summarized above (one rule → validation/guards → multi-rule composition → decompose validate/evaluate/format → stateful CLI add/list/eval → rebuild from scratch).
- **After submit:** Continue the path (Learn Go, then HTTP, SQL, Docker, etc.) and optionally **iterate** by adding specs tied to each course (port to Go, SQL load/store, thin API, Docker, etc.).
- **Capstone:** Options A–D above when you get there; no commitment yet.
- **Public repo:** This roadmap is part of the repo so others can see how the project fits the path and what “done” and “next” mean.

Back to [Curriculum overview](curriculum_overview.md).
