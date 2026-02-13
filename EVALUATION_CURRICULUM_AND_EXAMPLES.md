# Evaluation: Curriculum phases 1–5 and canonical examples

This document evaluates the work done against the request: build out phases 1–5 in separate markdowns per phase, canonical examples in separate markdown files, clear ties to business/industry necessity and best practices, assume the learner knows nothing about Python, rename curriculum to curriculum_overview, and evaluate the work.

---

## 1. Deliverables completed

| Requested | Delivered |
|-----------|-----------|
| Phases 1–5 in separate markdowns per phase | Yes. `curriculum/phase_1_deterministic_evaluation.md` through `curriculum/phase_5_stateful_cli.md`. |
| Canonical examples in separate markdown files | Yes. `canonical_examples/phase_1_canonical_example.md` through `canonical_examples/phase_5_canonical_example.md`. |
| Clear ties to business and industry necessity | Yes. Each phase doc has a “Why this phase matters in industry” and a “Business necessity and best practices” table; each example has “Industry tie-in” and “Why this is canonical.” |
| Best practices | Yes. Tables in each phase and “Why this is canonical” in each example; charter non-negotiables (pure rules, full evaluation, no silent defaults) reflected throughout. |
| Assume learner knows nothing about Python | Yes. Phase 1 introduces variables, lists, loops, conditionals, accumulators in order; later phases assume only what was built in prior phases. Code in examples is commented and avoids jargon. |
| Rename curriculum.md to curriculum_overview.md | Yes. `curriculum.md` removed; `curriculum_overview.md` created with a table linking to each phase and canonical example, plus Phase 6 rebuild note. |

---

## 2. Strengths of the design

- **Progressive disclosure:** Phase 1 starts from “no Python”; each phase adds one layer (validation, composition, decomposition, stateful CLI) without re-teaching basics.
- **Consistent structure:** Every phase has: industry why, primitives, session format, hour-by-hour guide, success criteria, link to canonical example, link back to overview. Every example has: business paragraph, what we’re training, industry tie-in, canonical code, “why this is canonical” table.
- **Explicit business linkage:** Real-world phrasing (marketplace eligibility, compliance, support, auditing) appears in both curriculum and examples so the learner sees why each primitive matters.
- **Charter alignment:** Pure rules, full evaluation, guard clauses, validate-then-evaluate, I/O at the edge are all reinforced in phase docs and examples.
- **Navigation:** Overview table links to both curriculum and example per phase; each phase and example links back to the overview (and Phase 6 is clearly “rebuild only”).

---

## 3. Gaps and limitations

- **Phase 6:** Not expanded into a full curriculum doc; the overview only states “rebuild from blank file.” Acceptable given the request was phases 1–5, but a future “phase_6_rebuild.md” could add a short checklist (e.g. “re-implement validate, evaluate, format, one rule, then CLI loop”).
- **No runnable code in repo:** Canonical examples are in markdown only; `src/engine.py` remains a stub. Learners must type or paste code. Adding a single “reference” script per phase (or one `examples/` script) would be optional follow-up.
- **Phase 1 Python setup:** “Install Python and run a single script” is one bullet; a true zero-Python learner might need a one-page “Environment setup” (e.g. install Python 3, run from terminal, what `python3 src/engine.py` does). Could live in README or a separate `setup.md`.
- **Diversity of business scenarios:** Examples use a single domain (marketplace/seller eligibility). Broader industry examples (e.g. billing, fraud, access control) could be added as optional “variant paragraphs” in phase docs or examples.

---

## 4. Consistency check

- **Naming:** Phase filenames and titles match; example filenames match phase numbers; overview links use relative paths from repo root (`curriculum/...`, `canonical_examples/...`). Links from inside `curriculum/` to `canonical_examples/` and `../curriculum_overview.md` are correct.
- **Cross-references:** Phase 2 references Phase 1 (validation before rules); Phase 3 builds on Phase 2 (valid record); Phase 4 references “Phases 1–3 done”; Phase 5 references “Phase 4: validate, evaluate, format, run_policy.” Dependency chain is consistent.
- **Code consistency:** Example return shapes align across phases (e.g. `{"passed": True/False, "reason": ...}` in rules; `{"allowed": ..., "reasons": [...]}` in composition; `{"valid": True/False, "reason": ...}` in validation). Phase 5’s `handle_eval` calls `run_policy_fn(record, rules)`, matching Phase 4’s `run_policy(record, rules)`.

---

## 5. Verdict

The work **meets the request**: phases 1–5 are in separate curriculum markdowns, canonical examples are in separate markdown files, business/industry necessity and best practices are explicit, the material assumes no prior Python (with Phase 1 as the foundation), and `curriculum.md` has been renamed to `curriculum_overview.md` with clear links to all phases and examples. The evaluation above documents strengths, minor gaps, and consistency; the curriculum is ready for a learner to use in order, with optional follow-up (Phase 6 doc, setup note, or runnable example scripts) as needed.
