# Harness Hackathon: 3 Difficulty Tracks x 2 Rounds (Pre-Riccardo vs. Post-Riccardo)

> **Same challenge. Same AI coding harness (`Antigravity CLI (agy)`, `Gemini CLI`, `Claude Code`, or `OpenAI Codex`). Any difficulty level (Starter, Medium, or Boss Mode). Measurable `Pre-Riccardo` vs. `Post-Riccardo` score jump (`0..100` + Harbor `reward = 1.0`)!**

Built for **HSLU `CAS Cloud Architecture` — Module M3 (*AI/ML Solutions with the Cloud*, 27 Nov 2026)**.
Everything — all 3 track specs, **10 offline Swiss literature PDFs** (`corpus/swiss-stories/`), 5 enterprise cloud scenarios (`scenarios/`), `grader.py`, and the Harbor eval task (`evals/harbor-task/`) — is **bundled right inside this repo** (zero external downloads needed after `git clone`!).

---

## Quick Start: Clone & Launch Your Harness (`AGENTS.md` Auto-Bootstraps!)

```bash
git clone https://github.com/palladius/harness-hackathon.git
cd harness-hackathon

# Launch your favorite AI coding harness (all auto-read AGENTS.md!):
agy -i "Start the hackathon!"    # Antigravity CLI (https://antigravity.google/download)
# or:
gemini                           # Gemini CLI  -> type "Start the hackathon!"
codex                            # OpenAI Codex -> type "Start the hackathon!"
claude                           # Claude Code  -> type "Start the hackathon!"
```

- **Single Source of Truth**: [`AGENTS.md`](AGENTS.md) drives every harness (`GEMINI.md` and `CLAUDE.md` are thin symlinks pointing to `AGENTS.md`).
- **1-Question Onboarding**: Your harness asks **1 single personalization question** (Track + your Personal Twist + Round), then guides you through **Pre-Riccardo vs. Post-Riccardo + the 3-Tier Eval Chain (`Local -> Harbor -> agents-cli`)**.
- **Antigravity CLI (`agy`) Quick Tips**:
  - Start interactively: `agy` (or `agy -i "Start the hackathon!"`)
  - Resume your session later: `agy --continue` (`agy -c`)
  - Inspect models & plugins/skills: `agy models` | `agy plugin list`
  - Autonomous eval loop: use `/goal` (or the portable prompt in [`exercises/ex2-harness.md`](exercises/ex2-harness.md))

---

## Step 1: Pick ONE Track (All 3 Separate Stack-Agnostic `PRD/SPEC` from Tech Stack!)

| Track | Level | Time | Challenge | Grader Flag | Optional Tech Stacks |
|---|---|---|---|---|---|
| **Track 0: Swiss Literature Manual RAG** ([PRD](tracks/track0-swiss-rag.md)) | Starter | 45-60m | Build a transparent manual RAG over **10 bundled Swiss PDFs** ([`corpus/swiss-stories/`](corpus/swiss-stories/): *Heidi, William Tell, Ruetli 1291, Pilatus, Matterhorn...*) with citations + 13-case anti-hallucination eval (`golden_qa.json`) | `--track rag` | Offline Python/TS/Go/Ruby (TF-IDF/BM25) OR live embeddings + Ollama/Gemini/OpenAI |
| **Track 1: Swiss Cloud Arch Diagram Draw** ([PRD](tracks/track1-cloud-arch.md)) | Medium | 1.5-2.5h | **Option 1A (CLI `.dot`)** or **Option 1B (Drag-and-Drop Canvas)** for your favorite cloud (`GCP`, `AWS`, `Azure`) across 5 Swiss scenarios ([`scenarios/`](scenarios/)) + Red Bottleneck X-Ray | `--track arch` | Python, Go, Rust, Ruby, TS; React (`@xyflow/react`), Vanilla HTML5 SVG, Svelte, Rails |
| **Track 2: `Guggu-Gstaeltli` (aka `Gugger-Gschirr`)** ([PRD](tracks/track2-guggu-harness.md)) | Boss Mode | 3-5h | Build your own Swiss-branded, **Schwiizerduetsch** multi-thread UI Harness that chimes **`"Guggu! Guggu!"`** (`E5 -> C#5` Web Audio) when ANY thread waits for your turn (+ Mute!) | `--track guggu` | Electron, Tauri, Flutter Desktop, PyWebView, or zero-install Localhost Web App |

---

## Step 2: Run Both Rounds (Pre-Riccardo vs. Post-Riccardo)

### Round 1 — Pre-Riccardo ("Your Way / Blind Exam Baseline", 20-30 min)

```text
Read exercises/ex1-yolo.md.
I choose Track <0 (rag) | 1 (arch) | 2 (guggu)>. Complete Round 1 (Pre-Riccardo) inside ./round1-pre-riccardo
using your normal default workflow (do NOT peek at grader.py first!), then run grader.py --track <rag|arch|guggu> and report my score!
```

### Round 2 — Post-Riccardo ("Harness Tricks + Evals + `/goal` Harbor + Ping `@palladius`", 60-120 min)

```text
Read exercises/ex2-harness.md.
Rebuild my exact same Track <0|1|2> cleanly inside ./round2-post-riccardo keeping SPEC.md separate from Tech Stack,
enable 3+ harness tricks + automated Evals looping until Harbor reward = 1.0, run grader.py --compare, write RETRO.md,
and help me publish to GitHub + ping @palladius on a GitHub Issue!
```

---

## Local Commands (`justfile`) & Public Resources

- **Run grader & unit tests locally**: `just test` | `just grade round1-pre-riccardo rag` | `just compare round1-pre-riccardo round2-post-riccardo rag`
- **Bundled 10 Multi-Page Swiss PDFs + `golden_qa.json`**: [`corpus/swiss-stories/`](corpus/swiss-stories/) *(82 real pages, ~331k chars, ~287 KB total — authentic Wikisource Public Domain classics & Wikipedia CC BY-SA 4.0 chronicles: Heidi, William Tell, Mark Twain in Lucerne, Edward Whymper on the Matterhorn 1865, Ruetli 1291, Pilatusbahn, Swiss Constitution!)*
- **Harbor Eval Task**: [`evals/harbor-task/`](evals/harbor-task/task.toml) | <https://harborframework.com/>
- **Live Web Hub & 6-Slide Deck (Browser Preview)**: [Hackathon Hub](https://storage.googleapis.com/palladius-genai-storagify/hslu/2026-11-27-m3-v1.0.2/hackathon.html) | [6-Slide Deck](https://storage.googleapis.com/palladius-genai-storagify/hslu/2026-11-27-m3-v1.0.2/hackathon-slides.html) *(also bundled locally in [`slides/index.html`](slides/index.html))*
- **Antigravity CLI (`agy`)**: <https://antigravity.google/download> | **Google Agents CLI (`agents-cli`)**: <https://github.com/google/agents-cli>
- **Conductor + Git Worktrees + GitHub Issues + HITL**: [Part 1](https://ricc.rocks/en/posts/technology/2026-06-16-crescendo-of-agents-part-1/) | [Part 2](https://ricc.rocks/en/posts/technology/2026-07-03-crescendo-of-agents-part-2/)
- **Superpowers**: <https://github.com/obra/superpowers> | **Ralph**: <https://ghuntley.com/ralph/> | **Skills**: <https://palladius.github.io/skills/> | **Contact**: `@palladius` on GitHub or [LinkedIn](https://www.linkedin.com/in/riccardocarlesso/)
