# Changelog

All notable changes to `harness-hackathon` are documented here.

## [0.6.1] - 2026-11-27

- Added an above-the-fold 3-column clickable NanoBanana Pro target preview gallery right at the top of `README.md` linking directly to Track 0 (`Prompts 0.1/0.2`), Track 1 (`Prompts 1.1/1.2`), and Track 2 (`Prompts 2.1/2.2`).

## [0.6.0] - 2026-11-27

- Reorganized `README.md` into an unmistakable **`3 Tracks x 2 Rounds = 6 Ready-to-Copy Prompts`** layout (`Prompts 0.1/0.2`, `1.1/1.2`, `2.1/2.2`) with zero placeholders to edit, plus 1-line `agy -i` launch commands.
- Added 3 NanoBanana Pro motivational target-preview mockups in `assets/` (`preview-track0-swiss-rag.jpg`, `preview-track1-cloud-arch.jpg`, `preview-track2-guggu-harness.jpg`), embedded across `README.md`, `tracks/track0..2`, and a new **Target Previews Gallery** slide in the standalone HTML deck (`slides/index.html`, now 7 slides).

## [0.5.0] - 2026-11-27

- Upgraded `corpus/swiss-stories/` from 1-page summaries to **10 authentic, multi-page Swiss literature & historical chronicle PDFs (82 pages total, ~331,000 chars, ~287 KB)** compiled from Public Domain Wikisource classics (*Heidi* 1922 Ch. I-II & XII-XIII, Mark Twain *A Tramp Abroad* Ch. XXVI-XXVII, Edward Whymper *Scrambles Amongst the Alps* Ch. XXI-XXII, 1911 *Encyclopaedia Britannica*, W. D. McCrackan) and CC BY-SA 4.0 Wikipedia chronicles.
- Updated `corpus/swiss-stories/golden_qa.json` (`v2`) so all 10 needle-in-a-haystack factual questions and 3 anti-hallucination traps match verbatim multi-page facts across pages 1..12 (with real near-miss Gotthard Base Tunnel trap!).
- Added multi-page PDF size guard in `tests/test_grader.py` and rebuilt the 6-slide HTML deck (`slides/index.html`).

## [0.4.2] - 2026-11-26

- Made `AGENTS.md` the single canonical harness instruction file; replaced standalone `CLAUDE.md` and `GEMINI.md` files with thin relative symlinks (`CLAUDE.md -> AGENTS.md`, `GEMINI.md -> AGENTS.md`).
- Promoted **Antigravity CLI (`agy`)** first-class quick-start & session tips alongside `gemini`, `codex`, and `claude` across `README.md`, `AGENTS.md`, exercises, Track 2, and the 6-slide HTML deck.
- Made all exercises and Track 0 docs 100% self-contained & offline-first (referencing the 10 bundled Swiss PDFs in `corpus/swiss-stories/` directly rather than asking cloned users to `curl` from external storage).

## [0.4.1] - 2026-11-26

- Pre-publish OSS code review & security hardening:
  - Added hackathon secret hygiene starter kit (`.env.example`, `.gitleaks.toml`, `.pre-commit-config.yaml`, `.github/workflows/security-scan.yml`, hardened `.gitignore`).
  - Fixed `grader.py --harbor-reward` to default its pass threshold to `95` when `--min-score` is omitted, and expanded Track 0 (`rag`) language detection (`.tsx`, `.jsx`, `.mjs`, `.sh`, `.java`, `.kt`, `.cs`, `.dart`).
  - Updated `justfile` and `evals/harbor-task/tests/test.sh` defaults to `round1-pre-riccardo` / `round2-post-riccardo` and `--track <rag|arch|guggu>`.
  - Hardened `tests/test_grader.py` (`11/11` unit tests passing, zero secrets, pure OSS hygiene) and added word-boundary guards to `grader.py` `SECRET_PATTERNS` so CSS classes like `.task-list-item-...` never trigger false positives.

## [0.4.0] - 2026-11-26

- Added auto-bootstrapping `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` at repo root so students can `git clone`, type `"Start!"`, answer **1 personalization question** (Track + Personal Twist + Round), and let their harness drive the entire hackathon.
- Upgraded Exercise 2 to a **3-Tier Eval Chain**: Tier 1 Local Deterministic Evals -> Tier 2 `/goal` Harbor Binary Gate (`reward.txt = 1.0`) -> Tier 3 optional **`google-agents-cli`** Quality Flywheel (`agents-cli eval run` -> `eval analyze` -> `eval compare`, `github.com/google/agents-cli`).
- Updated 6-slide standalone HTML deck (`slides/index.html`) and Storagify `hackathon.html`.

## [0.3.0] - 2026-11-26

- Refactored into a clean **3 Difficulty Tracks x 2 Rounds (Pre-Riccardo Blind Exam vs. Post-Riccardo + Evals)** orthogonal matrix (`tracks/track0-swiss-rag.md`, `tracks/track1-cloud-arch.md`, `tracks/track2-guggu-harness.md`).
- Added **Track 0 (Starter)**: 10 Public-Domain Swiss Literature & Lore PDFs (`corpus/swiss-stories/01..10_*.pdf`) + 13-case `golden_qa.json` (10 factual + 3 anti-hallucination refusal traps) + `--track rag` grading in `grader.py`.
- Added Blind Exam Pre-Riccardo vs. Post-Riccardo `--compare` scoreboard (Score 0..100, Harbor `reward.txt`, `SPEC.md`, `/learn` memory) and GitHub `@palladius` Issue / LinkedIn contact instructions.
- Updated standalone 6-slide HTML deck (`slides/index.html`) and tests (`9/9` passing).

## [0.2.0] - 2026-11-26

- Added **Track 1B (Drag-and-Drop Canvas)** option inside Track 1 (Easy: Swiss Cloud Arch Diagram Draw for your favorite cloud).
- Added **Track 2 (Boss Mode / Hard)**: `exercises/ex-boss-guggu.md` -- build your own Swiss-German UI Harness (**Guggu-Gstaeltli**, aka **Gugger-Gschirr**) in Electron (or local Web fallback) with synthesized Web Audio `"Guggu!"` turn chime.
- Added **Harbor-compatible Eval Task** (`evals/harbor-task/{task.toml,instruction.md,tests/test.sh}`) and portable `/goal` autonomous loop prompt writing `reward.txt` (`0.0..1.0`).
- Extended `grader.py` with `--track arch|guggu` and `--harbor-reward <path>` plus unit tests (`tests/test_grader.py`).
- Upgraded standalone Marp HTML deck to **6 slides** (Easy vs. Boss Mode track picker + `/goal` Harbor Evals slide).

## [0.1.0] - 2026-11-26

- Initial release of the **Swiss Cloud Arch Diagram Draw** Harness Engineering Hackathon.
- Added 5 multi-cloud Swiss enterprise architecture scenarios (`scenarios/01..05_*.md`).
- Added agent-readable `exercises/ex1-yolo.md` (Round 1 baseline) and `exercises/ex2-harness.md` (Round 2 with 6 composable Harness Engineering tricks).
- Added zero-dependency deterministic `grader.py` (`0..100` score + `--compare` Round 1 vs Round 2 scoreboard) and unit tests (`tests/test_grader.py`).
- Added 5-slide standalone HTML Marp deck (`slides/slides.md` -> `slides/index.html`).
