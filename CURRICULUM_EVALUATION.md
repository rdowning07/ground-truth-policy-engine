# Curriculum evaluation: Comparison to 30 Days of Java and 0-to-fluency courses

This document compares the 30-Hour Policy Engine curriculum to established “0 to fluency” courses (e.g. 30 Days of Java on GitHub, Codecademy, BiteSize Python, Microsoft Web Dev for Beginners) and recommends additions so **learners avoid being overwhelmed**.

---

## How respected courses are structured

### 30 Days of Java (BlondieBytes / GitHub variants)

- **One day = one topic (or small cluster).** Variables, if statements, loops, arrays, dictionaries, recursion, inheritance, linked lists, exceptions, queues, interfaces, generics, BST, games, unit testing, databases. Each day has a natural stop point.
- **Many small, varied deliverables.** MadLibs, GuessTheNumber, CoinToss, Library Catalogue, TicTacToe, Hangman, Calendar, ArrayPractice, LoopPractice. Learners get frequent “I built something” wins.
- **Mix of practice files and mini-apps.** Reinforces the same primitives in different contexts (games, tools, data structures) so concepts stick without feeling repetitive.
- **Explicit “day” boundaries.** “Day 5: Loops” means “do this today and stop.” No pressure to do 6 hours in one sitting.

### Other 0-to-fluency patterns (Codecademy, BiteSize Python, Microsoft curriculum, ExplorePython)

- **Bite-sized lessons** — Often 5–15 minutes per lesson; clear “one idea per step.”
- **Quizzes and checkpoints** — Comprehension checks or small coding tasks between lessons; instant feedback before moving on.
- **Hands-on throughout** — Not just “read then build at the end”; code early and often.
- **Gradual complexity** — Print → variables → conditionals → loops → collections → functions; each step builds on the previous with minimal new load.
- **Time estimates** — “This lesson ~10 min,” “This phase ~2 hours,” so learners can plan and not overcommit.
- **Self-paced with explicit break points** — “Complete this unit then take a break”; “Week 2: Lessons 5–8.”

---

## What this curriculum does well

- **Single domain (policy/eligibility)** — Clear “why”; no context-switching.
- **Business paragraph → code** — Translation is the skill; matches real work.
- **Canonical examples + mapping** — Learners can read code and tie it to concepts.
- **Charter and success criteria** — Clear definition of “done” per phase.
- **Python Day 1 + Glossary** — Good for zero-Python learners; concept → syntax available.

---

## Gaps that can overwhelm learners

| Gap | Why it matters |
|-----|----------------|
| **No explicit session boundaries** | “Phase 1: Hours 1–6” can be read as “do 6 hours in one go.” Learners may push through and burn out or skip breaks and retain less. |
| **No “day” or “session” pacing** | 30 Days of Java has “Day 1, Day 2, …”; this has “Phase 1, Phase 2” and hour ranges. Missing clear “stop here, resume here” points. |
| **One big deliverable per phase** | Phase 1 has one outcome (full `evaluate_age_rule`). No smaller wins (e.g. “just the conditional,” “just the loop”) before the full integration. |
| **No self-check or quiz** | No “can you explain X?” or “write a one-line comparison” before moving on. Mentors provide critique; solo learners have no checkpoint. |
| **No time estimates per chunk** | Day 1 has 11 stages + mapping; Phase 1 has 3 two-hour blocks. Learners don’t know “Stage 0 is ~15 min” vs “Hours 5–6 are the densest.” |
| **Single artifact (engine.py)** | Everything goes into one file. No variety (e.g. a tiny script for “only conditionals”) to reinforce one concept in isolation. |
| **No “if stuck” or “dense section” callouts** | Phases don’t say “Hours 5–6 tie everything together; if overwhelmed, re-read the canonical example and do one record by hand.” |
| **No optional stretch** | Everyone gets the same path. No “if you finish early, try…” so faster learners have a next step and others don’t feel behind. |
| **No phase recap** | Missing “What you built in Phase 1 (3 bullets).” Closure helps retention and reduces “what did I just do?” anxiety. |

---

## Recommendations: What to add so learners aren’t overwhelmed

### 1. Recommended pacing (session boundaries)

- **Publish a “recommended schedule”** (e.g. in the curriculum overview or a separate PACING.md):
  - **Session 1:** Stage 0 + Day 1 Stages 1–4 (~1 hour). Stop. “Next time: Stages 5–11 and mapping.”
  - **Session 2:** Day 1 Stages 5–11 + Phase 1 mapping (~1 hour). Stop. “Next time: Phase 1 Hours 1–2.”
  - **Session 3:** Phase 1 Hours 1–2 (one record, variable, conditional). Stop.
  - **Session 4:** Phase 1 Hours 3–4 (list, loop). Stop.
  - **Session 5:** Phase 1 Hours 5–6 (accumulator, full function). Phase 1 done.
  - Then 2–3 sessions per phase for Phases 2–5, with explicit “Phase complete? Take a break before Phase N.”
- **Label natural break points** in each phase doc: “Recommended stop after Hour 2,” “Checkpoint: you have a working loop before adding the accumulator.”

### 2. Time estimates

- Add **approximate time** to Day 1 stages and Phase hour blocks:
  - “Stage 0: ~15 min.” “Stages 1–3: ~30 min.” “Stages 4–7: ~45 min.” “Phase 1 Hours 1–2: ~1–2 hours.”
- Helps learners plan (“I have 45 minutes today → do Stages 4–7”) and avoid “I’ll do all of Phase 1” in one sitting.

### 3. Smaller wins before the big deliverable

- **Phase 1:** Add optional micro-exercises (can live in the phase doc or a separate EXERCISES.md):
  - After Hour 2: “Write a 3-line script: one variable `age`, an if/else that sets `passed`, and a print of `passed`. Run it for age 17 and 20.”
  - After Hour 4: “Write a loop that only prints each record’s `id`. No rule yet.” Then add the conditional and accumulator.
- Gives “I did something” checkpoints before the full “one function, list in, list out.”

### 4. Checkpoints and self-check

- **“Before you continue”** at the end of each Phase 1 hour block (and optionally other phases):
  - Hours 1–2: “Can you explain what `age >= 18` evaluates to for age 17? For 20?”
  - Hours 3–4: “Can you write a for-loop that prints each record’s `id`?”
  - Hours 5–6: “Can you explain why `results` is defined outside the loop?”
- **Success criteria** are already there; add one “Try this without looking” tiny task (e.g. “Write one comparison that uses `in` for a list”) so learners can self-test.

### 5. “If stuck” and “dense section” callouts

- In Phase 1: “**Hours 5–6** tie together loop, conditional, accumulator, and return. If you feel overloaded: (1) Re-read the [Phase 1 canonical example](canonical_examples/phase_1_canonical_example.md). (2) Trace one record through the code by hand. (3) Implement only the loop and append a dummy result; add the if/else next.”
- In Phase 2: “**Hour 11–12** is orchestration (validation then rule). If unclear, implement validation and rule in two separate functions first, then call both from a third.”

### 6. Optional stretch

- At the end of each phase: “**If you have time:** …” One line each, e.g.:
  - Phase 1: “Add a second rule (e.g. `region == "US"`) and a second result field; keep one function per rule for now.”
  - Phase 2: “Return a list of validation reasons instead of the first one only.”
- Gives fast learners a next step; others can ignore without feeling behind.

### 7. Phase recap

- At the end of each phase doc, add **“What you built (recap)”** in 3–4 bullets:
  - Phase 1: “(1) A function that takes a list of records. (2) A loop over each record. (3) A conditional for one rule (age >= 18). (4) An accumulator that collects one result per record and returns a list.”
- Provides closure and a quick “did I get it?” review.

### 8. Variety (optional, larger change)

- Consider one or two **standalone micro-scripts** (e.g. in `exercises/` or the docs) that use the same primitives in a different context:
  - “Given a list of amounts, print which are over 100” (loop + conditional, no dicts).
  - “Given a list of regions, count how many are `"US"`” (loop + accumulator, no rule yet).
- Not required for the main path but supports learners who need to see the same idea in a second context (as in 30 Days of Java’s mix of games and practice files).

---

## Summary table: This course vs 30 Days of Java–style courses

| Dimension | 30 Days Java / similar | This curriculum (before changes) | After recommendations |
|-----------|------------------------|----------------------------------|------------------------|
| Pacing | One day = one topic; natural stops | Phases with hour ranges; no session boundaries | Recommended sessions + “stop here” in phase docs |
| Time visibility | Often “Day N” or “~30 min” | No per-chunk estimates | Time estimates for stages and hour blocks |
| Small wins | Many small projects (MadLibs, GuessTheNumber, etc.) | One deliverable per phase | Micro-exercises + optional stretch tasks |
| Self-check | Quizzes / challenges between lessons | Critique by mentor; no built-in check | “Before you continue” + one “try without looking” per phase |
| If stuck | Video / community; some courses have hints | No “if stuck” guidance in docs | “If stuck” and “dense section” callouts in phase docs |
| Recap | Implicit (new project next day) | None | “What you built (recap)” at end of each phase |
| Variety | Games, tools, data structures | Single domain, single artifact | Optional second-context exercises (optional) |

---

## What to implement first

**High impact, low effort:**

1. Add **Recommended pacing** (session boundaries and “stop here”) to the curriculum overview or a short PACING.md.
2. Add **time estimates** to Day 1 stages and Phase 1 (and optionally other phases).
3. Add **“What you built (recap)”** at the end of each phase doc.
4. Add **“If stuck” / “dense section”** for Phase 1 Hours 5–6 (and Phase 2 orchestration).

**Next:**

5. **“Before you continue”** self-check questions for Phase 1 (and optionally Phase 2).
6. **Optional stretch** one-liners at the end of each phase.
7. **Micro-exercises** for Phase 1 (one script for conditional only; one for loop-only) in the phase doc or EXERCISES.md.

**Optional (more work):**

8. Standalone micro-scripts in a second context (e.g. “amounts over 100,” “count US”) for learners who need variety.

---

Back to [Curriculum overview](curriculum_overview.md).
