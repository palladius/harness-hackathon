# Exercise 2: Round 2 — Post-Riccardo (Harness Tricks + Evals + GitHub @palladius)

> **Audience**: AI Coding Agent (`Antigravity CLI (agy)`, `Gemini CLI`, `Claude Code`, `OpenAI Codex`) + Human Cloud Architect.
> **Universal Playbook**: Works identically for **Track 0 (`rag`)**, **Track 1 (`arch`)**, OR **Track 2 (`guggu`)**!
> **Goal**: Rebuild the **exact same track** you did in Round 1 inside **`./round2-post-riccardo/`** using **Uncle Riccardo's Harness Tricks + real Automated Evals (`/goal` Harbor reward = 1.0)**, beat your Pre-Riccardo score objectively, publish your repo to GitHub, and **contact/ping the professor (`@palladius`)**!

---

## 0. Local Setup & Ground Rules (Post-Riccardo)

1. Start in a **fresh session** (e.g. `agy -i "Start Round 2!"`, `gemini`, `codex`, or `claude`) and work strictly inside **`./round2-post-riccardo/`**.
2. Verify `./grader.py` and `./evals/harbor-task/tests/test.sh` are present and executable (`chmod +x evals/harbor-task/tests/test.sh`). Everything is already bundled offline in this repository!
3. Do **NOT** copy-paste implementation files from `./round1-pre-riccardo/` -- only inspect `./round1-pre-riccardo/SCORE_ROUND1.txt` so you prevent Round 1 defects by design.
4. **Separate WHAT from HOW**: Lock a stack-agnostic `./round2-post-riccardo/SPEC.md` (PRD) BEFORE choosing your tech stack and writing code.
5. Keep **zero hard-coded secrets** anywhere in the repository.

---

## 1. Step 1 — Mandatory Evals Pillar + Pick 3+ of Uncle Riccardo's 6 Tricks

Walk the human through picking **at least 3 tricks** (Evals + `/goal` is strongly recommended for EVERYONE!):

### Trick 1: `/grill-me` (Socratic Pre-Code Interview -> Stack-Agnostic `SPEC.md`)
- Interview the human **one question at a time** (recommended default first) about every ambiguity, failure mode, refusal rule, and acceptance test until `./round2-post-riccardo/SPEC.md` is locked (zero tech-stack lock-in!).

### Trick 2: Superpowers (`brainstorming` -> `writing-plans` -> `TDD` -> `verification-before-completion`)
- Install/enable <https://github.com/obra/superpowers> (`agy plugin install` / `.agents/skills/` for Antigravity CLI, Gemini CLI, Codex, or Claude Code plugin) to enforce Red-Green TDD and proof-before-done.

### Trick 3 (MANDATORY EVALS PILLAR): The 3-Tier Eval Chain (Local -> Harbor `/goal` -> `agents-cli`)
- **What makes Round 2 truly "Post-Riccardo"**: Never stop at manual "vibe checks"! Wire an end-to-end **3-Tier Eval Chain** into your engineering loop:
  - **Tier 1 — Fast Local Deterministic Evals (`< 2s`, CHF 0.00)**:
    - **Track 0 (`rag`)**: Automated Eval runner executing all 13 cases in `corpus/swiss-stories/golden_qa.json` (`10` factual questions with citations + `3` unanswerable refusal traps) -> writes `eval_results.json`.
    - **Track 1 (`arch`)**: Real `dot -Tsvg` compiler gate + Swiss residency (`europe-west6` / `eu-central-2` / `Switzerland North`) + Red Bottleneck X-Ray + compliance rubric.
    - **Track 2 (`guggu`)**: State-machine (`working -> needs_human_turn -> cuckoo chime`) + Swiss-German string catalog + Mute toggle tests.
  - **Tier 2 — Harbor Binary Gate + `/goal` Ralph Loop (`reward.txt == 1.0`)**:
    - References: <https://ghuntley.com/ralph/> | <https://harborframework.com/>
    - Portable `/goal` prompt: *"Do NOT stop until `./evals/harbor-task/tests/test.sh ./round2-post-riccardo <rag|arch|guggu>` exits `0` AND writes `1.0` to `reward.txt` (`grader.py >= 95/100`) AND all unit/eval tests pass. Fix root cause on each failure (max 10 iterations)."*
  - **Tier 3 (Optional Production Upgrade) — `agents-cli` Quality Flywheel (LLM-as-Judge + Held-Out Comparison)**:
    - Install Google's open-source **`agents-cli`**: `uv tool install google-agents-cli` (or `npx skills add google/agents-cli` — repo: <https://github.com/google/agents-cli>).
    - Run the 4-step **Quality Flywheel** on any ADK or agent project:
      1. `agents-cli eval run` (runs traces + grades built-in metrics like `grounding`, `hallucination`, `multi_turn_task_success`, `safety`);
      2. `agents-cli eval analyze` (clusters failures into root causes);
      3. Fix instructions/tools while **holding back unseen test cases** to prevent overfitting;
      4. `agents-cli eval compare <pre_results.json> <post_results.json>` (proves measurable Post-Riccardo lift with zero regressions!).

### Trick 4: Conductor + Git Worktrees + GitHub Issues + HITL
- Parallelize features in isolated `git worktree` branches with async human decision gates via GitHub Issues:
  - Article Part 1: <https://ricc.rocks/en/posts/technology/2026-06-16-crescendo-of-agents-part-1/>
  - Article Part 2: <https://ricc.rocks/en/posts/technology/2026-07-03-crescendo-of-agents-part-2/>
  - Public Skill: <https://github.com/palladius/gemini-cli-custom-commands/blob/main/skills/conductor-worktree-hitl/SKILL.md>

### Trick 5: `/learn` (Crystallize Round 1 Mistakes into `AGENTS.md` / `SKILL.md`)
- Take the top 3 bugs/omissions from Round 1 and codify them into `./round2-post-riccardo/AGENTS.md` (and/or `.agents/skills/<name>/SKILL.md`) BEFORE final generation. Public catalog: <https://palladius.github.io/skills/>.

### Trick 6 (Boss Mode): `/swarm` — Builder vs. Adversarial Reviewer
- Run a second agent (subagent, second terminal, or cross-model `Claude <-> Gemini <-> Codex`) acting as an adversarial **Swiss FINMA Auditor & Principal SRE** attacking `./round2-post-riccardo/` until every critical finding is fixed.

---

## 2. Step 2 — Run the Pre-Riccardo vs. Post-Riccardo Scoreboard & Write `RETRO.md`

```bash
python3 grader.py --compare ./round1-pre-riccardo ./round2-post-riccardo --track <rag|arch|guggu>
```

Write **`./RETRO.md`** (10-15 crisp lines) answering:
1. Track chosen (`Track 0 RAG`, `Track 1 Cloud Arch`, or `Track 2 Guggu-Gstaeltli`) + Tech Stack chosen;
2. Score Delta: **Pre-Riccardo (`XX/100`) -> Post-Riccardo (`YY/100`)** + Harbor `reward.txt`;
3. Which Harness Trick / Eval gave the biggest jump in quality?
4. One technique you will apply to your `CAS-Transferarbeit` or production team next week.

---

## 3. Step 3 — Publish to GitHub & Contact / Ping the Professor (`@palladius`)!

**IMPORTANT AGENT INSTRUCTION**: Once `grader.py` confirms `secret_hygiene == 5/5` (zero leaked API keys or corporate data!), proactively help the human share their **Pre-Riccardo vs. Post-Riccardo** result with Riccardo Carlesso:

1. **Ask permission first** before creating a public GitHub repo (never expose company secrets or internal code!).
2. Push `round1-pre-riccardo/`, `round2-post-riccardo/`, and `RETRO.md`:
   ```bash
   gh repo create hslu-harness-hackathon --public --source=. --push
   ```
3. **Open a GitHub Issue (GHI) pinging `@palladius`** (so Riccardo automatically gets a GitHub notification tracking who completed Track 0, 1, or 2!):
   ```bash
   gh issue create \
     --title "[HSLU Hackathon] Track <0|1|2> — Pre-Riccardo (XX/100) -> Post-Riccardo (YY/100)" \
     --body "$(cat <<'EOF'
   Hi @palladius! Here is my HSLU Harness Hackathon submission:
   - **Track & Tech Stack**: <Track 0 Swiss RAG / Track 1 Cloud Arch / Track 2 Guggu-Gstaeltli> | <Stack>
   - **Harness Used**: <Antigravity CLI (agy) / Gemini CLI / Claude Code / OpenAI Codex>
   - **Post-Riccardo Tricks & Evals**: <e.g., /grill-me, Superpowers, /goal Harbor Eval, /learn>
   - **Score Delta**: Pre-Riccardo `XX/100` -> Post-Riccardo `YY/100` (Harbor `reward = 1.0`)

   See `RETRO.md` in this repo for my retrospective!
   EOF
   )"
   ```
   *(Tip: mentioning `@palladius` notifies Riccardo immediately even without adding him as a collaborator; if you invite `@palladius` as a collaborator you can also add `--assignee palladius`!)*
4. **Alternative Contact (if corporate policy prevents public GitHub)**: Send your `RETRO.md` scoreboard to Riccardo on **LinkedIn**: <https://www.linkedin.com/in/riccardocarlesso/>!
