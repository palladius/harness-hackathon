import contextlib
import io
import json
import os
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

import grader

REPO_ROOT = Path(__file__).resolve().parent.parent


def make_valid_dot(cloud: str, region: str) -> str:
    return f"""digraph {cloud}_arch {{
  rankdir=LR;
  subgraph cluster_ch {{
    label="{region} Sovereign Perimeter";
    user [label="Credit Officer"];
    sso [label="SSO OAuth OBO RFC 8693"];
    gw [label="AI Gateway FinOps Kill-Switch"];
    vec [label="Vector Search Pre-Retrieval ACL"];
    mcp [label="Read-Only MCP Core Banking"];
    llm [label="Enterprise LLM ZDR CMEK"];
    user -> sso -> gw -> vec -> llm;
    gw -> mcp -> llm;
  }}
  risk_timeout [label="Bottleneck: sync LLM 504 timeout", color="#dc2626", style="dashed"];
  risk_acl [label="SPOF: Confused Deputy without pre-retrieval ACL", color="red", style="dashed"];
  risk_cap [label="FinOps: missing token kill-switch quota", color="#e11d48", style="dashed"];
  gw -> risk_timeout [color="red", style="dashed"];
  vec -> risk_acl [color="red", style="dashed"];
  llm -> risk_cap [color="red", style="dashed"];
}}
"""


class TestGrader(unittest.TestCase):
    def test_swiss_corpus_10_pdfs_and_golden_qa_exist(self) -> None:
        corpus = REPO_ROOT / "corpus" / "swiss-stories"
        pdfs = sorted(corpus.glob("*.pdf"))
        self.assertEqual(len(pdfs), 10)
        for pdf in pdfs:
            self.assertGreater(pdf.stat().st_size, 10_000, f"{pdf.name} should be a substantial multi-page PDF")
        golden = json.loads((corpus / "golden_qa.json").read_text(encoding="utf-8"))
        qs = golden["questions"]
        self.assertEqual(len(qs), 13)
        self.assertEqual(sum(1 for q in qs if not q["answerable"]), 3)

    def test_compliant_rag_scores_100_and_harbor_reward_1(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "tests").mkdir()
            (root / "SPEC.md").write_text("# Stack-agnostic RAG SPEC\n", encoding="utf-8")
            (root / "AGENTS.md").write_text("# Learned rules\n", encoding="utf-8")
            (root / "rag.py").write_text(
                "import pypdf\n# chunk with overlap, tfidf cosine similarity top_k\n# cite 01_heidi_alps_mayenfeld.pdf or refuse: I cannot answer\n",
                encoding="utf-8",
            )
            results = [
                {"id": f"Q{i:02d}", "answerable": True, "cited_doc": f"0{i}_doc.pdf" if i < 10 else "10_doc.pdf", "answer": "Grounded answer with citation", "passed": True}
                for i in range(1, 11)
            ] + [
                {"id": f"Q{i}_TRAP", "answerable": False, "answer": "I cannot answer this from the provided Swiss corpus.", "refused": True}
                for i in (11, 12, 13)
            ]
            (root / "eval_results.json").write_text(json.dumps({"results": results}), encoding="utf-8")
            (root / "tests" / "test_rag.py").write_text("def test_ok():\n    assert True\n", encoding="utf-8")

            res = grader.grade_directory(root, "swiss-stories", "rag")
            self.assertEqual(res["score"], 100, grader.format_single_report(res))
            self.assertTrue(res["process"]["has_spec"])
            self.assertTrue(res["process"]["has_learn_memory"])

            test_sh = REPO_ROOT / "evals" / "harbor-task" / "tests" / "test.sh"
            proc = subprocess.run(["bash", str(test_sh), str(root), "rag", "swiss-stories"], capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            self.assertEqual((root / "reward.txt").read_text().strip(), "1.0")

    def test_toy_yolo_scores_low(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "gcp.dot").write_text("digraph G { User -> App -> AI; }", encoding="utf-8")
            res = grader.grade_directory(root, "02", "arch")
            self.assertLess(res["score"], 25)

    def test_broken_dot_syntax_fails(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "gcp.dot").write_text("digraph G { a -> b -> c -> d -> e -> f; BROKEN {{{", encoding="utf-8")
            res = grader.grade_directory(root, "02", "arch")
            gcp_check = next(c for c in res["checks"] if c["key"] == "gcp_dot")
            self.assertFalse(gcp_check["passed"])

    def test_compliant_arch_scores_100_and_harbor_reward_1(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "out").mkdir()
            (root / "tests").mkdir()
            (root / "out" / "gcp.dot").write_text(make_valid_dot("gcp", "europe-west6"), encoding="utf-8")
            (root / "out" / "aws.dot").write_text(make_valid_dot("aws", "eu-central-2"), encoding="utf-8")
            (root / "out" / "azure.dot").write_text(make_valid_dot("azure", "Switzerland North"), encoding="utf-8")
            (root / "ARCHITECTURE.md").write_text(
                "# Architecture\nSwiss revDSG + ZDR + CMEK.\nOAuth 2.0 On-Behalf-Of (RFC 8693) pre-retrieval ACL.\nToken FinOps kill-switch budget.\nCI/CD evaluation gate with pytest.\n",
                encoding="utf-8",
            )
            (root / "canvas.html").write_text("<div draggable='true' ondragstart='x()'>GCP</div>", encoding="utf-8")
            (root / "tests" / "test_arch.py").write_text("def test_ok():\n    assert True\n", encoding="utf-8")
            res = grader.grade_directory(root, "02", "arch")
            self.assertEqual(res["score"], 100, grader.format_single_report(res))
            self.assertTrue(res["drag_and_drop_ui_detected"])

            test_sh = REPO_ROOT / "evals" / "harbor-task" / "tests" / "test.sh"
            proc = subprocess.run(["bash", str(test_sh), str(root), "arch", "02"], capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            self.assertEqual((root / "reward.txt").read_text().strip(), "1.0")

    def test_compliant_guggu_scores_100(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "tests").mkdir()
            (root / "app.html").write_text(
                """<style>header { background: #D52B1E; }</style>
                <div class="swiss-cross">Luzern</div>
                <p>Gruezi! Am schaffe... Faertig! Guggu, du bisch dra!</p>
                <button id="mute">Stumm</button>
                <script>
                  const threads = [{status: 'working'}, {status: 'needs_human_turn'}];
                  const mockOffline = true;
                  function playGuggu() { const ctx = new AudioContext(); const o = ctx.createOscillator(); o.frequency.value = 659; }
                </script>""",
                encoding="utf-8",
            )
            (root / "tests" / "guggu.test.js").write_text("it('chimes', () => { expect(true).toBe(true); });\n", encoding="utf-8")
            res = grader.grade_directory(root, "boss", "guggu")
            self.assertEqual(res["score"], 100, grader.format_single_report(res))

    def test_secret_leak_penalized(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fake_key = "AIza" + "Sy" + ("A1b2C3d4E5" * 4)
            (root / "config.txt").write_text(f"KEY={fake_key}\n", encoding="utf-8")
            res = grader.grade_directory(root, "02", "arch")
            sec = next(c for c in res["checks"] if c["key"] == "secret_hygiene")
            self.assertFalse(sec["passed"])
            self.assertEqual(sec["points"], 0)

    def test_compare_report_format(self) -> None:
        with tempfile.TemporaryDirectory() as td1, tempfile.TemporaryDirectory() as td2:
            r1 = grader.grade_directory(Path(td1), "02", "arch")
            r2 = grader.grade_directory(Path(td2), "02", "arch")
            md = grader.format_compare_report(r1, r2)
            self.assertIn("Pre-Riccardo (Round 1)", md)
            self.assertIn("Harbor Reward", md)

    def test_compare_harbor_reward_defaults_to_95_threshold(self) -> None:
        with tempfile.TemporaryDirectory() as td1, tempfile.TemporaryDirectory() as td2:
            reward_file = Path(td2) / "reward.txt"
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = grader.main(["--compare", td1, td2, "--track", "arch", "--harbor-reward", str(reward_file)])
            self.assertEqual(rc, 1)
            self.assertEqual(reward_file.read_text(encoding="utf-8").strip(), "0.0")

    def test_css_class_not_flagged_as_openai_secret(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "styles.css").write_text(".task-list-item-convert-container { display: block; }\n", encoding="utf-8")
            res = grader.grade_directory(root, "02", "arch")
            sec = next(c for c in res["checks"] if c["key"] == "secret_hygiene")
            self.assertTrue(sec["passed"])
            self.assertEqual(sec["points"], 5)

    def test_public_repo_hygiene(self) -> None:
        forbidden = [
            re.compile(r"/Users/[A-Za-z0-9._-]+/"),
            re.compile(r"/home/[A-Za-z0-9._-]+/"),
            re.compile(r"[\u2018\u2019\u201c\u201d]"),
        ]
        for dp, dn, fn in os.walk(REPO_ROOT):
            dn[:] = [d for d in dn if d not in {".git", "__pycache__", "previews"}]
            for f in fn:
                p = Path(dp) / f
                if p.resolve() == Path(__file__).resolve():
                    continue
                if p.suffix.lower() in {".md", ".py", ".txt", ".yaml", ".yml", ".toml", ".sh", ".json"} or f == "justfile":
                    txt = p.read_text(encoding="utf-8", errors="ignore")
                    for rx in forbidden:
                        self.assertIsNone(
                            rx.search(txt),
                            f"Hygiene violation ({rx.pattern}) in {p.relative_to(REPO_ROOT)}",
                        )
                    for secret_name, rx in grader.SECRET_PATTERNS:
                        self.assertIsNone(
                            rx.search(txt),
                            f"Secret leak ({secret_name}) in {p.relative_to(REPO_ROOT)}",
                        )


if __name__ == "__main__":
    unittest.main()
