# Harbor Task Instruction: Swiss Cloud Arch Diagram Draw

Build a verified Swiss Multi-Cloud Architecture submission for Scenario 02 (Cantonal Bank Mortgage RAG) inside the target workspace directory.

## Required Deliverables

1. Valid Graphviz DOT files (`out/gcp.dot`, `out/aws.dot`, `out/azure.dot`) with at least 5 directed edges each that compile cleanly with `dot -Tsvg` (exit code `0`).
2. Strict Swiss data residency regions across all three clouds:
   - GCP: `europe-west6`
   - AWS: `eu-central-2`
   - Azure: `Switzerland North`
3. Red Bottleneck & SPOF X-Ray annotations (`color="red"` / `#dc2626` / `style="dashed"`) highlighting at least 3 distinct failure vectors (sync LLM timeout, Confused Deputy ACL leak, missing FinOps kill-switch, residency drift).
4. `ARCHITECTURE.md` documenting Swiss `revDSG`/`ZDR`/`CMEK`, `OAuth 2.0 On-Behalf-Of (RFC 8693)` pre-retrieval ACLs, Token FinOps kill-switch, and an automated CI/CD evaluation gate.
5. Runnable automated tests with real assertions and zero hard-coded secrets.

## Verification Contract

The verifier runs `tests/test.sh`, executes `grader.py --min-score 95 --harbor-reward`, and writes `1.0` (PASS) or `0.0` (FAIL) to `/logs/verifier/reward.txt` (or `./reward.txt` when run locally).
