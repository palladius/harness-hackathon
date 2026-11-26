# Harness Hackathon: 3 Difficulty Tracks x 2 Rounds (Pre-Riccardo vs. Post-Riccardo)

> **Same challenge. Same AI coding harness (`Claude Code`, `OpenAI Codex`, `Gemini CLI`, or `Antigravity`). Any difficulty level (Starter, Medium, or Boss Mode). Measurable `Pre-Riccardo` vs. `Post-Riccardo` score jump (`0..100` + Harbor `reward = 1.0`)!**

Built for **HSLU `CAS Cloud Architecture` — Module M3 (*AI/ML Solutions with the Cloud*, 27 Nov 2026)**.

---

## Quick Start: Clone & Say "Start!" (`AGENTS.md` + `CLAUDE.md` Included!)

```bash
git clone https://github.com/palladius/harness-hackathon.git
cd harness-hackathon
claude   # or: codex / gemini / antigravity -> just type "Start the hackathon!"
```

Your harness automatically reads [`AGENTS.md`](AGENTS.md) (and [`CLAUDE.md`](CLAUDE.md) / [`GEMINI.md`](GEMINI.md)), asks **1 single personalization question** (Track + your Personal Twist + Round), and guides you through the full **Pre-Riccardo vs. Post-Riccardo + 3-Tier Eval Chain (`Local -> Harbor -> agents-cli`)**!

---

## Step 1: Pick ONE Track (All 3 Separate Stack-Agnostic `PRD/SPEC` from Tech Stack!)

| Track | Level | Time | Challenge | Grader Flag | Optional Tech Stacks |
|---|---|---|---|---|---|
| **Track 0: Swiss Literature Manual RAG** ([PRD](tracks/track0-swiss-rag.md)) | Starter | 45-60m | Build a transparent manual RAG over **10 Public-Domain Swiss PDFs** (*Heidi, William Tell, Ruetli 1291, Pilatus, Matterhorn...*) with citations + 13-case anti-hallucination eval (`golden_qa.json`) | `--track rag` | Offline Python/TS/Go/Ruby (TF-IDF/BM25) OR live embeddings + Ollama/Gemini/OpenAI |
| **Track 1: Swiss Cloud Arch Diagram Draw** ([PRD](tracks/track1-cloud-arch.md)) | Medium | 1.5-2.5h | **Option 1A (CLI `.dot`)** or **Option 1B (Drag-and-Drop Canvas)** for your favorite cloud (`GCP`, `AWS`, `Azure`) across 5 Swiss scenarios + Red Bottleneck X-Ray | `--track arch` | Python, Go, Rust, Ruby, TS; React (`@xyflow/react`), Vanilla HTML5 SVG, Svelte, Rails |
| **Track 2: `Guggu-Gstaeltli` (aka `Gugger-Gschirr`)** ([PRD](tracks/track2-guggu-harness.md)) | Boss Mode | 3-5h | Build your own Swiss-branded, **Schwiizerduetsch** multi-thread UI Harness that chimes **`"Guggu! Guggu!"`** (`E5 -> C#5` Web Audio) when ANY thread waits for your turn (+ Mute!) | `--track guggu` | Electron, Tauri, Flutter Desktop, PyWebView, or zero-install Localhost Web App |

---

## Step 2: Run Both Rounds (Pre-Riccardo vs. Post-Riccardo)

### Round 1 — Pre-Riccardo ("Your Way / Baseline", 20-30 min)

```text
Read https://storage.googleapis.com/palladius-genai-storagify/hslu/2026-11-27-m3-v1.0.2/hackathon/ex1-yolo.md.
I choose Track <0 (rag) | 1 (arch) | 2 (guggu)>. Complete Round 1 (Pre-Riccardo) inside ./round1-pre-riccardo
using your normal default workflow, then run grader.py --track <rag|arch|guggu> and report my score!
```

### Round 2 — Post-Riccardo ("Harness Tricks + Evals + `/goal` Harbor + Ping `@palladius`", 60-120 min)

```text
Read https://storage.googleapis.com/palladius-genai-storagify/hslu/2026-11-27-m3-v1.0.2/hackathon/ex2-harness.md.
Rebuild my exact same Track <0|1|2> cleanly inside ./round2-post-riccardo keeping SPEC.md separate from Tech Stack,
enable 3+ harness tricks + automated Evals looping until Harbor reward = 1.0, run grader.py --compare, write RETRO.md,
and help me publish to GitHub + ping @palladius on a GitHub Issue!
```

---

## Live Links & Public Resources

- **Live Hackathon Hub**: <https://storage.googleapis.com/palladius-genai-storagify/hslu/2026-11-27-m3-v1.0.2/hackathon.html>
- **Standalone 6-Slide HTML Deck**: <https://storage.googleapis.com/palladius-genai-storagify/hslu/2026-11-27-m3-v1.0.2/hackathon-slides.html>
- **10 Swiss Literature PDFs + `golden_qa.json`**: [`corpus/swiss-stories/`](corpus/swiss-stories/)
- **Harbor Eval Task**: [`evals/harbor-task/`](evals/harbor-task/task.toml) | <https://harborframework.com/>
- **Conductor + Git Worktrees + GitHub Issues + HITL**: [Part 1](https://ricc.rocks/en/posts/technology/2026-06-16-crescendo-of-agents-part-1/) | [Part 2](https://ricc.rocks/en/posts/technology/2026-07-03-crescendo-of-agents-part-2/)
- **Superpowers**: <https://github.com/obra/superpowers> | **Ralph**: <https://ghuntley.com/ralph/> | **Skills**: <https://palladius.github.io/skills/> | **Contact**: `@palladius` on GitHub or [LinkedIn](https://www.linkedin.com/in/riccardocarlesso/)
