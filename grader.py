#!/usr/bin/env python3
"""Deterministic 0..100 grader & Harbor reward verifier for Harness Hackathon (v0.4.1).

Supports 3 orthogonal difficulty tracks -- all graded identically PRE-Riccardo vs POST-Riccardo:
  --track rag    : Track 0 (Starter) Manual RAG over 10 Swiss Literature PDFs + 13-case Golden Eval
  --track arch   : Track 1 (Medium)  Swiss Cloud Arch Diagram Draw (CLI DOT or Drag-and-Drop Canvas)
  --track guggu  : Track 2 (Boss)    Guggu-Gstaeltli Swiss-German UI Harness with Cuckoo Chime

Zero third-party dependencies. Optionally writes a Harbor-compatible reward.txt (1.0 or 0.0).

Usage:
  python3 grader.py ./round1-pre-riccardo --track rag
  python3 grader.py ./round2-post-riccardo --track rag --min-score 95 --harbor-reward ./round2-post-riccardo/reward.txt
  python3 grader.py --compare ./round1-pre-riccardo ./round2-post-riccardo --track rag
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


CLOUD_REGIONS = {
    "gcp": ("europe-west6", re.compile(r"europe-west6|zurich|zuerich", re.I)),
    "aws": ("eu-central-2", re.compile(r"eu-central-2|zurich|zuerich", re.I)),
    "azure": ("Switzerland North", re.compile(r"switzerland[\s_-]*north", re.I)),
}

RED_STYLE_RE = re.compile(
    r'(color\s*=\s*"?(red|crimson|firebrick|#dc2626|#e11d48|#ef4444|#b91c1c|#ff0000)"?|style\s*=\s*"?[^"]*dashed[^"]*"?)',
    re.I,
)

RISK_THEMES = {
    "bottleneck_spof": re.compile(r"\b(bottleneck|spof|single point of failure|contention|hot spot)\b", re.I),
    "latency_async": re.compile(r"\b(timeout|504|starvation|sync|async|queue|backpressure|pub/sub|sqs|service bus)\b", re.I),
    "acl_security": re.compile(r"\b(confused deputy|pre-retrieval|acl|isolation|pii|redaction|prompt.?injection|dlp)\b", re.I),
    "finops_cap": re.compile(r"\b(finops|kill.?switch|budget|quota|token cap|cost|idle gpu)\b", re.I),
    "residency_drift": re.compile(r"\b(sovereign|residency|drift|zdr|zero data retention|cmek|revdsg|finma)\b", re.I),
}

GOVERNANCE_CHECKS = [
    ("Swiss Sovereignty & ZDR (revDSG/FINMA/ZDR/CMEK)", re.compile(r"\b(revdsg|nfadp|finma|zdr|zero data retention|cmek)\b", re.I)),
    ("Identity & Pre-Retrieval ACLs (OBO/RFC 8693/IAM)", re.compile(r"\b(obo|on-behalf-of|rfc\s*8693|pre-retrieval|acl_groups|workload identity|managed identity)\b", re.I)),
    ("Token FinOps & Kill-Switch", re.compile(r"\b(finops|kill.?switch|token cap|budget|quota|tco)\b", re.I)),
    ("Automated Evaluation / CI Gate", re.compile(r"\b(eval|evaluation gate|golden set|scorecard|ci/cd|pytest|unittest)\b", re.I)),
]

SECRET_PATTERNS = [
    ("Google API Key", re.compile(r"(?<![0-9A-Za-z_-])AIzaSy[0-9A-Za-z_-]{30,}")),
    ("OpenAI/Anthropic Key", re.compile(r"(?<![0-9A-Za-z_-])sk-(?:proj-|ant-)?[0-9A-Za-z_-]{20,}")),
    ("GitHub PAT", re.compile(r"(?<![0-9A-Za-z_-])ghp_[0-9A-Za-z]{30,}")),
    ("AWS Access Key", re.compile(r"(?<![0-9A-Za-z_-])AKIA[0-9A-Z]{16}(?![0-9A-Z])")),
]

TEST_FILE_RE = re.compile(r"(^test_.*\.py$|_test\.py$|\.test\.(ts|tsx|js|jsx)$|\.spec\.(ts|tsx|js|jsx)$|_test\.go$|_spec\.rb$|_test\.dart$)", re.I)
ASSERTION_RE = re.compile(r"\b(assert|assertEqual|assertTrue|expect\(|testing\.T|describe\(|it\(|test\()\b")
DND_RE = re.compile(r"(draggable|ondragstart|ondrop|xyflow|reactflow|pointerdown|drag.?and.?drop)", re.I)

# Track 0 (RAG) patterns
PDF_INGEST_RE = re.compile(r"(pypdf|pypdf2|pdfplumber|pymupdf|fitz|pdftotext|pdf-parse|pdfjs|pdfreader|\.pdf)", re.I)
CHUNKING_RETRIEVAL_RE = re.compile(r"(chunk|overlap|cosine|tfidf|tf_idf|bm25|embedding|dot_product|similarity|top_k|topk)", re.I)
CITATION_RE = re.compile(r"(citation|cite|source_doc|0[1-9]_[a-z_]+\.pdf|10_[a-z_]+\.pdf)", re.I)
REFUSAL_RE = re.compile(r"(cannot answer|not found|not in the|insufficient|no information|out of scope|unanswerable|refus|don't know|do not know|does not contain|not mentioned)", re.I)

# Track 2 (Guggu-Gstaeltli) deterministic patterns
SWISS_BRAND_RE = re.compile(r"(#d52b1e|#da291c|swiss.?cross|schweiz|ch-cross|zurich|zuerich|luzern|bern|zug)", re.I)
SWISS_GERMAN_TOKENS = [
    re.compile(r"gr[uü][e]?zi", re.I),
    re.compile(r"(guggu|gugger|kuckuck|cu-?cu)", re.I),
    re.compile(r"(am schaffe|schaffe|f[aä]rtig|du bisch dra|wartet uf dich|huere|gschirr|gst[aä]ltli)", re.I),
]
CUCKOO_AUDIO_RE = re.compile(r"(AudioContext|webkitAudioContext|createOscillator|659|554|playCuckoo|playGuggu|simpleaudio|playsound|audioplayers)", re.I)
MUTE_TEST_RE = re.compile(r"(mute|stumm)", re.I)
MULTI_THREAD_RE = re.compile(r"(needs_human_turn|waiting_for_user|working|threads|conversations|sessions)", re.I)
MOCK_MODE_RE = re.compile(r"(mock|offline|simul)", re.I)


@dataclass
class CheckResult:
    key: str
    label: str
    points: int
    max_points: int
    passed: bool
    detail: str


def find_dot_file(root: Path, cloud: str) -> Optional[Path]:
    preferred = [
        root / "out" / f"{cloud}.dot",
        root / f"{cloud}.dot",
        root / "diagrams" / f"{cloud}.dot",
    ]
    for p in preferred:
        if p.is_file():
            return p
    for p in sorted(root.rglob("*.dot")):
        if ".git" in p.parts:
            continue
        if cloud in p.stem.lower():
            return p
    return None


def validate_dot_syntax(dot_path: Path) -> Tuple[bool, str]:
    text = dot_path.read_text(encoding="utf-8", errors="ignore")
    edges = len(re.findall(r"->|--", text))
    if edges < 5:
        return False, f"too trivial ({edges} edges; need >= 5 to avoid toy 3-box diagram)"

    dot_bin = shutil.which("dot")
    if dot_bin:
        proc = subprocess.run(
            [dot_bin, "-Tsvg", str(dot_path)],
            capture_output=True,
            text=True,
            timeout=15,
        )
        if proc.returncode != 0:
            err = (proc.stderr or proc.stdout).strip().splitlines()[:1]
            return False, f"dot -Tsvg failed: {err[0] if err else 'syntax error'}"
        return True, f"dot -Tsvg PASS ({edges} edges)"

    if not re.search(r"\b(di)?graph\b", text):
        return False, "missing digraph/graph declaration"
    if text.count("{") != text.count("}") or text.count("{") == 0:
        return False, "unbalanced curly braces"
    return True, f"static DOT check PASS ({edges} edges; install graphviz `dot` for full render)"


def read_all_text_files(root: Path) -> List[Tuple[Path, str]]:
    out: List[Tuple[Path, str]] = []
    skip_dirs = {".git", "node_modules", "__pycache__", ".venv", "venv", ".pytest_cache", "dist", "build"}
    text_exts = {
        ".md", ".dot", ".py", ".ts", ".tsx", ".js", ".jsx", ".html", ".css",
        ".svg", ".go", ".rb", ".rs", ".dart", ".yaml", ".yml", ".json", ".txt", ".sh",
    }
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in skip_dirs]
        for f in sorted(fn):
            p = Path(dp) / f
            if p.suffix.lower() in text_exts or f.lower() in {"justfile", "dockerfile"}:
                try:
                    out.append((p, p.read_text(encoding="utf-8", errors="ignore")))
                except OSError:
                    pass
    return out


def detect_process_artifacts(target: Path) -> Dict[str, bool]:
    has_spec = any((target / name).is_file() for name in ("SPEC.md", "PRD.md")) or any(
        p.name in {"SPEC.md", "PRD.md"} for p in target.rglob("*.md") if ".git" not in p.parts
    )
    has_learn = any(
        p.name in {"AGENTS.md", "CLAUDE.md", "GEMINI.md", "SKILL.md"}
        for p in target.rglob("*.md")
        if ".git" not in p.parts
    )
    return {"has_spec": has_spec, "has_learn_memory": has_learn}


def check_tests_and_secrets(target: Path, all_files: List[Tuple[Path, str]]) -> Tuple[CheckResult, CheckResult]:
    test_hits = [
        str(p.relative_to(target))
        for p, content in all_files
        if TEST_FILE_RE.search(p.name) and ASSERTION_RE.search(content)
    ]
    c_tests = CheckResult(
        "automated_tests",
        "Automated Test Suite with Assertions",
        10 if test_hits else 0,
        10,
        bool(test_hits),
        f"Found: {', '.join(test_hits[:3])}" if test_hits else "No test files with assertions found",
    )

    leaks = []
    for p, content in all_files:
        for secret_name, rx in SECRET_PATTERNS:
            if rx.search(content):
                leaks.append(f"{secret_name} in {p.relative_to(target)}")
    c_sec = CheckResult(
        "secret_hygiene",
        "Zero Hard-Coded Secrets",
        0 if leaks else 5,
        5,
        not leaks,
        "Clean" if not leaks else "LEAK: " + "; ".join(leaks[:3]),
    )
    return c_tests, c_sec


def grade_rag(target: Path, scenario: str = "swiss-stories") -> Dict[str, object]:
    checks: List[CheckResult] = []
    all_files = read_all_text_files(target)
    code_corpus = "\n".join(
        content
        for p, content in all_files
        if p.suffix.lower() in {".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".go", ".rb", ".rs", ".java", ".kt", ".cs", ".dart", ".sh"}
    )

    # 1. PDF Ingestion + Transparent Chunking & Retrieval (25 pts)
    has_pdf = bool(PDF_INGEST_RE.search(code_corpus))
    ret_hits = len(set(m.group(1).lower() for m in CHUNKING_RETRIEVAL_RE.finditer(code_corpus)))
    ingest_pts = (10 if has_pdf else 0) + (15 if ret_hits >= 3 else (8 if ret_hits >= 1 else 0))
    checks.append(
        CheckResult(
            "pdf_retrieval",
            "PDF Ingestion + Manual Chunking & Retrieval",
            ingest_pts,
            25,
            ingest_pts == 25,
            f"pdf_parser={has_pdf}, retrieval_signals={ret_hits}",
        )
    )

    # 2. Grounded Citations & Refusal Guardrail in Code (20 pts)
    has_cite = bool(CITATION_RE.search(code_corpus))
    has_refusal = bool(REFUSAL_RE.search(code_corpus))
    guard_pts = (10 if has_cite else 0) + (10 if has_refusal else 0)
    checks.append(
        CheckResult(
            "citations_refusal",
            "Mandatory Source Citations & Refusal Guardrail",
            guard_pts,
            20,
            guard_pts == 20,
            f"citation_logic={has_cite}, refusal_guardrail={has_refusal}",
        )
    )

    # 3. Executable Golden QA Eval Results (40 pts = 20 grounded accuracy + 20 trap refusal)
    eval_file = None
    for cand in [target / "eval_results.json", target / "evals" / "eval_results.json", target / "out" / "eval_results.json"]:
        if cand.is_file():
            eval_file = cand
            break
    if not eval_file:
        for p in sorted(target.rglob("*eval_results*.json")):
            if ".git" not in p.parts:
                eval_file = p
                break

    grounded_pts = 0
    trap_pts = 0
    grounded_detail = "Missing eval_results.json (run your 13-case golden_qa.json eval!)"
    trap_detail = "Missing eval_results.json (no trap refusal proof)"

    if eval_file:
        try:
            data = json.loads(eval_file.read_text(encoding="utf-8"))
            rows = data.get("results", data) if isinstance(data, dict) else data
            if isinstance(rows, list):
                grounded_total = 0
                grounded_ok = 0
                trap_total = 0
                trap_ok = 0
                for row in rows:
                    if not isinstance(row, dict):
                        continue
                    qid = str(row.get("id", ""))
                    ans = str(row.get("answer", ""))
                    cited = str(row.get("cited_doc", row.get("source", ""))) + " " + ans
                    is_trap = "TRAP" in qid.upper() or row.get("answerable") is False
                    if is_trap:
                        trap_total += 1
                        if row.get("refused") is True or REFUSAL_RE.search(ans):
                            trap_ok += 1
                    else:
                        grounded_total += 1
                        has_pdf_cite = bool(re.search(r"0?[1-9]_[a-z_]+\.pdf|10_[a-z_]+\.pdf", cited, re.I))
                        passed_flag = row.get("passed")
                        if passed_flag is True or (passed_flag is None and has_pdf_cite and len(ans.strip()) >= 8):
                            grounded_ok += 1
                if grounded_total >= 8:
                    rate = grounded_ok / grounded_total
                    grounded_pts = 20 if rate >= 0.85 else int(round(20 * rate))
                    grounded_detail = f"{grounded_ok}/{grounded_total} grounded cases passed ({rate*100:.0f}%)"
                else:
                    grounded_detail = f"Only {grounded_total} grounded cases in {eval_file.name} (need >= 8 from golden_qa.json)"
                if trap_total >= 3:
                    trate = trap_ok / trap_total
                    trap_pts = 20 if trap_ok == trap_total else int(round(12 * trate))
                    trap_detail = f"{trap_ok}/{trap_total} unanswerable trap questions cleanly refused"
                else:
                    trap_detail = f"Only {trap_total} trap cases in {eval_file.name} (need all 3 Q11..Q13_TRAP)"
        except Exception as e:
            grounded_detail = f"Invalid JSON in {eval_file.name}: {e}"
            trap_detail = grounded_detail

    checks.append(CheckResult("golden_grounded", "Golden QA Eval: Grounded Recall + Citations (>=85%)", grounded_pts, 20, grounded_pts == 20, grounded_detail))
    checks.append(CheckResult("golden_traps", "Golden QA Eval: 3/3 Anti-Hallucination Trap Refusals", trap_pts, 20, trap_pts == 20, trap_detail))

    c_tests, c_sec = check_tests_and_secrets(target, all_files)
    checks.extend([c_tests, c_sec])

    total = sum(c.points for c in checks)
    return {
        "track": "rag",
        "target": str(target),
        "scenario": scenario,
        "score": total,
        "max_score": 100,
        "process": detect_process_artifacts(target),
        "checks": [asdict(c) for c in checks],
    }


def grade_arch(target: Path, scenario: str = "02") -> Dict[str, object]:
    checks: List[CheckResult] = []
    dot_texts: Dict[str, str] = {}

    for cloud in ("gcp", "aws", "azure"):
        dp = find_dot_file(target, cloud)
        if not dp:
            checks.append(CheckResult(f"{cloud}_dot", f"{cloud.upper()} Graphviz DOT valid", 0, 10, False, f"Missing {cloud}.dot"))
            continue
        dot_texts[cloud] = dp.read_text(encoding="utf-8", errors="ignore")
        ok, msg = validate_dot_syntax(dp)
        checks.append(CheckResult(f"{cloud}_dot", f"{cloud.upper()} Graphviz DOT valid", 10 if ok else 0, 10, ok, f"{dp.relative_to(target)}: {msg}"))

    region_pts = 0
    region_notes = []
    for cloud, (canonical, pat) in CLOUD_REGIONS.items():
        txt = dot_texts.get(cloud, "")
        if txt and pat.search(txt):
            region_pts += 5
            region_notes.append(f"{cloud.upper()}={canonical} OK")
        else:
            region_notes.append(f"{cloud.upper()} missing {canonical}")
    checks.append(
        CheckResult("swiss_regions", "Swiss Data Residency (GCP/AWS/Azure)", region_pts, 15, region_pts == 15, "; ".join(region_notes))
    )

    combined_dots = "\n".join(dot_texts.values())
    has_red_style = bool(RED_STYLE_RE.search(combined_dots))
    matched_themes = [name for name, rx in RISK_THEMES.items() if rx.search(combined_dots)]
    if has_red_style and len(matched_themes) >= 3:
        xray_pts, xray_ok = 20, True
    elif has_red_style and len(matched_themes) >= 1:
        xray_pts, xray_ok = 10, False
    elif len(matched_themes) >= 2:
        xray_pts, xray_ok = 5, False
    else:
        xray_pts, xray_ok = 0, False
    checks.append(
        CheckResult("red_xray", "Red Bottleneck & SPOF X-Ray (>=3 risks)", xray_pts, 20, xray_ok, f"red_styling={has_red_style}, themes={len(matched_themes)} ({', '.join(matched_themes) or 'none'})")
    )

    all_files = read_all_text_files(target)
    doc_corpus = "\n".join(content for p, content in all_files if p.suffix.lower() in {".md", ".dot", ".txt"})
    gov_pts = 0
    gov_missing = []
    for label, rx in GOVERNANCE_CHECKS:
        if rx.search(doc_corpus):
            gov_pts += 5
        else:
            gov_missing.append(label)
    checks.append(
        CheckResult("governance_doc", "Governance, ACLs, FinOps & Eval Gate", gov_pts, 20, gov_pts == 20, "All 4 pillars covered" if not gov_missing else "Missing: " + ", ".join(gov_missing))
    )

    c_tests, c_sec = check_tests_and_secrets(target, all_files)
    checks.extend([c_tests, c_sec])

    ui_corpus = "\n".join(content for p, content in all_files if p.suffix.lower() in {".html", ".tsx", ".jsx", ".ts", ".js", ".svelte", ".vue"})
    has_dnd = bool(DND_RE.search(ui_corpus))

    total = sum(c.points for c in checks)
    return {
        "track": "arch",
        "target": str(target),
        "scenario": scenario,
        "score": total,
        "max_score": 100,
        "drag_and_drop_ui_detected": has_dnd,
        "process": detect_process_artifacts(target),
        "checks": [asdict(c) for c in checks],
    }


def grade_guggu(target: Path, scenario: str = "boss") -> Dict[str, object]:
    checks: List[CheckResult] = []
    all_files = read_all_text_files(target)
    code_corpus = "\n".join(
        content for p, content in all_files if p.suffix.lower() in {".html", ".css", ".js", ".jsx", ".ts", ".tsx", ".py", ".rs", ".dart", ".rb", ".go", ".svg"}
    )
    full_corpus = "\n".join(content for _, content in all_files)

    brand_hits = len(set(m.group(0).lower() for m in SWISS_BRAND_RE.finditer(code_corpus)))
    brand_ok = brand_hits >= 2
    checks.append(CheckResult("swiss_brand", "Swiss Branded UI (#D52B1E + Cross/Canton)", 20 if brand_ok else (10 if brand_hits == 1 else 0), 20, brand_ok, f"matched_signals={brand_hits}"))

    sg_hits = sum(1 for rx in SWISS_GERMAN_TOKENS if rx.search(code_corpus))
    sg_pts = {3: 20, 2: 14, 1: 7, 0: 0}[sg_hits]
    checks.append(CheckResult("swiss_german", "Authentic Schwiizerduetsch UI & Persona", sg_pts, 20, sg_hits == 3, f"{sg_hits}/3 dialect categories found"))

    has_audio = bool(CUCKOO_AUDIO_RE.search(code_corpus))
    has_mute = bool(MUTE_TEST_RE.search(code_corpus))
    audio_pts = (20 if has_audio else 0) + (5 if has_mute else 0)
    checks.append(CheckResult("cuckoo_chime", "Synthesized Guggu/Cuckoo Chime + Mute Toggle", audio_pts, 25, has_audio and has_mute, f"audio_synth={has_audio}, mute_toggle={has_mute}"))

    has_multi = bool(MULTI_THREAD_RE.search(code_corpus))
    has_mock = bool(MOCK_MODE_RE.search(full_corpus))
    multi_pts = (15 if has_multi else 0) + (5 if has_mock else 0)
    checks.append(CheckResult("multi_thread_mock", "Multi-Conversation Turn State + Offline Mock", multi_pts, 20, has_multi and has_mock, f"multi_thread_state={has_multi}, offline_mock={has_mock}"))

    c_tests, c_sec = check_tests_and_secrets(target, all_files)
    checks.extend([c_tests, c_sec])

    total = sum(c.points for c in checks)
    return {
        "track": "guggu",
        "target": str(target),
        "scenario": scenario,
        "score": total,
        "max_score": 100,
        "process": detect_process_artifacts(target),
        "checks": [asdict(c) for c in checks],
    }


def grade_directory(target: Path, scenario: str = "02", track: str = "arch") -> Dict[str, object]:
    if not target.exists() or not target.is_dir():
        return {
            "track": track,
            "target": str(target),
            "scenario": scenario,
            "score": 0,
            "max_score": 100,
            "process": {"has_spec": False, "has_learn_memory": False},
            "checks": [asdict(CheckResult("exists", "Target directory exists", 0, 100, False, f"Missing: {target}"))],
        }
    if track == "rag":
        return grade_rag(target, scenario)
    if track == "guggu":
        return grade_guggu(target, scenario)
    return grade_arch(target, scenario)


def format_single_report(res: Dict[str, object]) -> str:
    proc = res.get("process", {})
    lines = [
        f"=== Harness Hackathon Grader (Track={res['track']}, Scenario={res['scenario']}) ===",
        f"Target  : {res['target']}",
        f"Score   : {res['score']} / {res['max_score']}",
        f"Process : SPEC/PRD={proc.get('has_spec', False)} | /learn Memory={proc.get('has_learn_memory', False)}",
    ]
    if res.get("drag_and_drop_ui_detected"):
        lines.append("Bonus   : Interactive Drag-and-Drop Canvas UI detected!")
    lines.append("")
    for c in res["checks"]:
        badge = "PASS" if c["passed"] else "FAIL"
        lines.append(f"[{badge}] {c['points']:2d}/{c['max_points']:2d} | {c['label']} -- {c['detail']}")
    return "\n".join(lines)


def format_compare_report(r1: Dict[str, object], r2: Dict[str, object], min_score: int = 95) -> str:
    delta = int(r2["score"]) - int(r1["score"])
    sign = "+" if delta >= 0 else ""
    rew1 = "1.0 (PASS)" if int(r1["score"]) >= min_score else "0.0 (FAIL)"
    rew2 = "1.0 (PASS)" if int(r2["score"]) >= min_score else "0.0 (FAIL)"
    p1 = r1.get("process", {})
    p2 = r2.get("process", {})
    lines = [
        f"# Pre-Riccardo vs. Post-Riccardo Scoreboard (Track={r1['track']})",
        "",
        "| Check / Eval Signal | Pre-Riccardo (Round 1) | Post-Riccardo (Round 2) | Delta |",
        "|---|---:|---:|---:|",
    ]
    c2_map = {c["key"]: c for c in r2["checks"]}
    for c1 in r1["checks"]:
        c2 = c2_map.get(c1["key"], {"points": 0, "max_points": c1["max_points"]})
        d = int(c2["points"]) - int(c1["points"])
        ds = f"+{d}" if d > 0 else str(d)
        lines.append(
            f"| {c1['label']} | {c1['points']}/{c1['max_points']} | {c2['points']}/{c2['max_points']} | {ds} |"
        )
    lines.append(f"| **TOTAL SCORE** | **{r1['score']}/100** | **{r2['score']}/100** | **{sign}{delta}** |")
    lines.append(f"| **Harbor Reward (`>={min_score}`)** | `{rew1}` | `{rew2}` | {'PASS!' if int(r2['score']) >= min_score else 'KEEP LOOPING'} |")
    lines.append(f"| Stack-Agnostic `SPEC.md` | {'Yes' if p1.get('has_spec') else 'No'} | {'Yes' if p2.get('has_spec') else 'No'} | - |")
    lines.append(f"| `/learn` Memory (`AGENTS.md`/`SKILL.md`) | {'Yes' if p1.get('has_learn_memory') else 'No'} | {'Yes' if p2.get('has_learn_memory') else 'No'} | - |")
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Deterministic PRE vs POST grader & Harbor verifier for Harness Hackathon.")
    parser.add_argument("target", nargs="?", help="Directory to grade (e.g. ./round1-pre-riccardo)")
    parser.add_argument("--compare", nargs=2, metavar=("PRE_DIR", "POST_DIR"), help="Compare Pre-Riccardo vs Post-Riccardo")
    parser.add_argument("--track", choices=["rag", "arch", "guggu"], default="arch", help="Hackathon track (rag, arch, or guggu)")
    parser.add_argument("--scenario", default="02", help="Scenario ID (swiss-stories, 01..05, or boss)")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--min-score", type=int, default=0, help="Exit non-zero if score is below threshold")
    parser.add_argument("--harbor-reward", metavar="FILE", help="Write Harbor reward (1.0 if >= min-score else 0.0) to FILE")
    args = parser.parse_args(argv)

    effective_min = args.min_score if args.min_score > 0 else (95 if args.harbor_reward else 0)

    if args.compare:
        r1 = grade_directory(Path(args.compare[0]), args.scenario, args.track)
        r2 = grade_directory(Path(args.compare[1]), args.scenario, args.track)
        if args.json:
            print(json.dumps({"pre_riccardo": r1, "post_riccardo": r2}, indent=2))
        else:
            print(format_compare_report(r1, r2, min_score=effective_min or 95))
        passed = int(r2["score"]) >= effective_min
        if args.harbor_reward:
            Path(args.harbor_reward).write_text("1.0\n" if passed else "0.0\n", encoding="utf-8")
        return 0 if passed else 1

    if not args.target:
        parser.error("Provide a target directory or --compare PRE_DIR POST_DIR")

    res = grade_directory(Path(args.target), args.scenario, args.track)
    passed = int(res["score"]) >= effective_min
    if args.harbor_reward:
        Path(args.harbor_reward).write_text("1.0\n" if passed else "0.0\n", encoding="utf-8")
    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_single_report(res))
        if args.harbor_reward:
            print(f"\nHarbor Reward ({args.harbor_reward}): {'1.0' if passed else '0.0'}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
