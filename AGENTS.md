# AGENTS.md — HSLU Harness Hackathon Autopilot

Welcome, AI Coding Agent (`Antigravity CLI (agy)`, `Gemini CLI`, `Claude Code`, or `OpenAI Codex`)!
You are guiding a Cloud Architect / Engineer through the **HSLU Harness Hackathon** (**3 Difficulty Tracks x 2 Rounds: Pre-Riccardo vs. Post-Riccardo**).

---

## Step 0: Ask ONE Single Personalization Question First!

As soon as the human says "start" (or opens a session here), do **NOT** dump a wall of text or start coding blindly.
Ask **ONE concise question** that customizes the entire hackathon to this specific person:

> **Welcome to the HSLU Harness Hackathon! To customize your build, reply in 1 line with:**
> 1. **Track**: `0` (Starter: 10 Swiss PDFs Manual RAG), `1` (Medium: Swiss Cloud Arch Diagram Draw — CLI or Drag & Drop), or `2` (Boss Mode: *Guggu-Gstaeltli* Swiss-German Cuckoo UI Harness)?
> 2. **Your Personal Twist**: your favorite cloud (`GCP` / `AWS` / `Azure`), Swiss canton/dialect (`ZH` / `LU` / `ZG` / `BE` / `TI` / `GR`), company domain, and preferred tech stack (any language/framework!)?
> 3. **Starting Round**: `Round 1 (Pre-Riccardo Blind Exam)` or `Round 2 (Post-Riccardo + Evals)`?

---

## Step 1: Route Cleanly Based on Their Answer

### Track PRDs (Always Separate Stack-Agnostic `SPEC.md` from Tech Stack!)
- **Track 0 (`--track rag`)**: Read `tracks/track0-swiss-rag.md` (corpus in `corpus/swiss-stories/`).
- **Track 1 (`--track arch`)**: Read `tracks/track1-cloud-arch.md` (scenarios in `scenarios/`).
- **Track 2 (`--track guggu`)**: Read `tracks/track2-guggu-harness.md`.

### Round 1 — Pre-Riccardo (`exercises/ex1-yolo.md`)
1. Work strictly inside `./round1-pre-riccardo/`.
2. **BLIND EXAM RULE**: Do **NOT** read the source code of `grader.py` or inspect the trap answers in `corpus/swiss-stories/golden_qa.json` while building Round 1!
3. Do NOT install extra workflow plugins yet (keep Round 1 honest).
4. At the end, run `python3 grader.py ./round1-pre-riccardo --track <rag|arch|guggu>`, save `./round1-pre-riccardo/SCORE_ROUND1.txt`, and offer to commit Round 1 cleanly to Git.

### Round 2 — Post-Riccardo (`exercises/ex2-harness.md`)
1. Work strictly inside `./round2-post-riccardo/` (fresh session, zero copy-paste from Round 1).
2. Lock a stack-agnostic `./round2-post-riccardo/SPEC.md` (incorporating the user's Personal Twist!) BEFORE picking the tech stack and writing code.
3. Help the human enable **at least 3 of Uncle Riccardo's 6 Harness Tricks** (`/grill-me`, `Superpowers`, `Ralph + /goal Harbor Eval`, `Conductor + Worktrees + GitHub Issues + HITL`, `/learn`, `/swarm`).
4. Run the **3-Tier Eval Chain**:
   - **Tier 1 (Local Fast Checks)**: unit tests + `golden_qa.json` / `dot -Tsvg` / state-machine tests + `grader.py`.
   - **Tier 2 (Harbor Binary Gate)**: `./evals/harbor-task/tests/test.sh ./round2-post-riccardo <rag|arch|guggu>` until **`reward.txt == 1.0`** (`score >= 95/100`).
   - **Tier 3 (Optional Production Eval Flywheel)**: `google-agents-cli` (`uv tool install google-agents-cli` -> `agents-cli eval run` -> `eval analyze` -> `eval compare`, docs: `https://github.com/google/agents-cli`).
5. Run `python3 grader.py --compare ./round1-pre-riccardo ./round2-post-riccardo --track <rag|arch|guggu>` and write `./RETRO.md`.

---

## Step 2: Publish & Contact Professor (`@palladius`)

1. Verify `secret_hygiene == 5/5` (ZERO leaked API keys, tokens, or private company data!).
2. Ask permission before creating a public GitHub repo (`gh repo create hslu-harness-hackathon --public --source=. --push`).
3. Draft and open a GitHub Issue tagging **`@palladius`** with the Pre-Riccardo vs. Post-Riccardo scoreboard, Personal Twist, Tech Stack, and `RETRO.md` (or share via LinkedIn `https://www.linkedin.com/in/riccardocarlesso/` if corporate policy blocks public GitHub).
