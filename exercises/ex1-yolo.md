# Exercise 1: Round 1 — Pre-Riccardo ("Solve It Your Way" Baseline)

> **Audience**: AI Coding Agent (`Antigravity CLI (agy)`, `Gemini CLI`, `Claude Code`, `OpenAI Codex`) + Human Cloud Architect.
> **Universal Playbook**: Works identically for **Track 0 (`rag`)**, **Track 1 (`arch`)**, OR **Track 2 (`guggu`)**!
> **Goal**: Establish an honest **Pre-Riccardo baseline** in `20-30 minutes` using your normal prompting habits before applying Harness Engineering & Evals in Exercise 2 (*Post-Riccardo*).

---

## 1. Step 1 — Pick ONE Track (Starter, Medium, or Boss Mode)

Ask the human which difficulty track they want to run today, then read its local stack-agnostic PRD:

- **Track 0 — Starter (`rag`, 45-60 min)**: **Manual RAG Over 10 Bundled Swiss Literature PDFs** (*Heidi, William Tell, Ruetli 1291, Pilatus, Matterhorn...*) -> [`tracks/track0-swiss-rag.md`](../tracks/track0-swiss-rag.md)
- **Track 1 — Medium (`arch`, 1.5-2.5h)**: **Swiss Cloud Arch Diagram Draw** (CLI `.dot` OR Drag-and-Drop Canvas for GCP/AWS/Azure) -> [`tracks/track1-cloud-arch.md`](../tracks/track1-cloud-arch.md)
- **Track 2 — Boss Mode (`guggu`, 3-5h)**: **`Guggu-Gstaeltli` (aka `Gugger-Gschirr`) Swiss-German Cuckoo UI Harness** -> [`tracks/track2-guggu-harness.md`](../tracks/track2-guggu-harness.md)

---

## 2. Step 2 — Local Offline Ground Rules (Pre-Riccardo)

Everything is already bundled in this repository (`corpus/swiss-stories/`, `scenarios/`, `grader.py`, `evals/harbor-task/`):

1. Work strictly inside **`./round1-pre-riccardo/`** (create it if missing).
2. Read your track's local inputs:
   - **Track 0 (`rag`)**: the 10 Swiss PDFs in `./corpus/swiss-stories/` (do NOT peek at `golden_qa.json` trap answers yet!).
   - **Track 1 (`arch`)**: your chosen scenario in `./scenarios/` (recommended default: `./scenarios/02_cantonal_bank_mortgage_rag.md`).
   - **Track 2 (`guggu`)**: the PRD in `./tracks/track2-guggu-harness.md`.
3. **Stay Honest (Blind Exam Rule!)**:
   - Do **NOT** install extra workflow plugins yet (`/grill-me`, Superpowers, Ralph Loop, Conductor, `/swarm`) — save them for **Exercise 2 (Post-Riccardo)**!
   - Do **NOT** read the source code of `grader.py` or peek at `corpus/swiss-stories/golden_qa.json` trap questions while implementing Round 1 — run `grader.py` ONLY at the very end as an honest **blind exam** so the Pre-Riccardo vs. Post-Riccardo delta is scientifically real!
4. Keep **PRD/SPEC separate from Tech Stack**: ask the human which language/framework they prefer from the track's Optional Tech Stack Menu.

---

## 3. Step 3 — Grade Your Pre-Riccardo Baseline & Commit to Git

Run the deterministic grader for your chosen track (`rag`, `arch`, or `guggu`):

```bash
python3 grader.py ./round1-pre-riccardo --track <rag|arch|guggu>
```

1. Save the output into `./round1-pre-riccardo/SCORE_ROUND1.txt` along with wall-clock minutes spent.
2. Commit Round 1 cleanly on a branch or in your own hackathon repo so your **Pre-Riccardo vs. Post-Riccardo** diff is preserved when you publish to GitHub and ping `@palladius` after Exercise 2!

Now close this chat session and start a **brand-new session** (e.g. `agy -i "Start Round 2!"`) for **[Exercise 2: Post-Riccardo (`ex2-harness.md`)](ex2-harness.md)**!
