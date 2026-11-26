# Track 1 (Medium -- Cloud Architect): Swiss Cloud Arch Diagram Draw

> **Difficulty**: Medium (`1.5-2.5h`, ideal for Cloud Architects & Solution Engineers).
> **Structure**: Pure **Product Specification (`PRD / SPEC`)** decoupled from the **Optional Tech Stack Menu** below.
> **Works identically in**: **Round 1 (Pre-Riccardo)** inside `./round1-pre-riccardo/` AND **Round 2 (Post-Riccardo + Evals)** inside `./round2-post-riccardo/`!

---

## 1. Pick 1 of 5 Regulated Swiss Scenarios (`scenarios/`)

- `01_insurance_claims_disparity.md`: Multimodal hail photo Vision vs. PDF garage invoice OCR + HITL adjuster queue.
- `02_cantonal_bank_mortgage_rag.md` (**Recommended default**): Pre-retrieval OAuth 2.0 OBO ACL Vector Search + read-only MCP Core Banking.
- `03_canton_public_admin_citizen_portal.md`: DE/FR/IT/EN civic portal + pre-prompt AHV/PII redaction shield.
- `04_rag_on_vms_vs_serverless_managed.md`: Self-hosted sovereign `Apertus` / `Gemma 4` GPU K8s vs. Serverless Managed RAG.
- `05_redundant_lamp_to_cloud_native.md`: Modernizing 2 sticky VMs into Multi-AZ stateless containers + HA DB + zero secrets.

---

## 2. Product Specification (PRD / SPEC -- Tech-Stack Agnostic)

Choose **Option 1A (Headless CLI Compiler)** OR **Option 1B (Interactive Drag-and-Drop Canvas for your favorite cloud: GCP, AWS, or Azure)**:
- **Option 1A (CLI)**: Reads the scenario `.md` and compiles the multi-cloud diagrams, bottleneck X-ray, and architecture specification.
- **Option 1B (Drag-and-Drop Web Studio)**: Interactive canvas where you drag cloud services and Swiss-region perimeters onto a board, wire edges, toggle a **Red Bottleneck X-Ray**, and export the `.dot` files and `ARCHITECTURE.md`.

Both options MUST emit these verifiable artifacts:
1. **Multi-Cloud Graphviz Diagrams**: `out/gcp.dot` (`europe-west6`), `out/aws.dot` (`eu-central-2`), `out/azure.dot` (`Switzerland North`), each with `>= 5` directed edges passing `dot -Tsvg` with exit code `0`.
2. **Red Bottleneck & SPOF X-Ray**: Highlight at least **3 failure vectors in red** (`color="red"` / `#dc2626` / `style="dashed"`) on the graph (e.g., synchronous LLM timeout, Confused Deputy missing pre-retrieval ACL, missing Token FinOps kill-switch, cross-region drift).
3. **Architecture & Compliance Spec (`ARCHITECTURE.md`)**: Multi-cloud Rosetta table + Swiss `revDSG`/`ZDR`/`CMEK` + `OAuth 2.0 On-Behalf-Of (RFC 8693)` ACLs + Token FinOps caps + CI/CD Evaluation Gate.
4. **Automated Tests & Zero Secrets**: Runnable test suite verifying Graphviz compilation + compliance invariants, with zero hard-coded API keys.

---

## 3. Optional Tech Stack Menu (Pick Whatever You Like!)

- **Option 1A (CLI)**: Python (`uv` / stdlib), Go, Rust, Ruby, or Node/TypeScript.
- **Option 1B (Drag-and-Drop Canvas)**: React + `@xyflow/react`, Vanilla HTML5 SVG/Canvas (zero npm build step!), Svelte, Vue, or Rails + Hotwire.

---

## 4. Grade & Compare Pre-Riccardo vs. Post-Riccardo

```bash
python3 grader.py ./round1-pre-riccardo --track arch --scenario 02
python3 grader.py ./round2-post-riccardo --track arch --scenario 02 --min-score 95 --harbor-reward ./round2-post-riccardo/reward.txt
python3 grader.py --compare ./round1-pre-riccardo ./round2-post-riccardo --track arch --scenario 02
```
