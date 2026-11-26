#!/usr/bin/env bash
# Harbor-compatible verifier script (works both inside Harbor sandboxes AND locally!)
# Usage locally: ./evals/harbor-task/tests/test.sh ./round2-post-riccardo [rag|arch|guggu] [scenario]
set -euo pipefail

TARGET_DIR="${1:-./round2-post-riccardo}"
TRACK="${2:-arch}"
SCENARIO="${3:-02}"
MIN_SCORE="${MIN_SCORE:-95}"

if [[ -d "/logs/verifier" ]]; then
  REWARD_FILE="/logs/verifier/reward.txt"
else
  REWARD_FILE="${TARGET_DIR}/reward.txt"
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GRADER_PATH="${GRADER_PATH:-}"
if [[ -z "${GRADER_PATH}" ]]; then
  if [[ -f "./grader.py" ]]; then
    GRADER_PATH="./grader.py"
  elif [[ -f "${SCRIPT_DIR}/../../../grader.py" ]]; then
    GRADER_PATH="${SCRIPT_DIR}/../../../grader.py"
  else
    echo "ERROR: grader.py not found. Download it from the Hackathon Hub first." >&2
    echo "0.0" > "${REWARD_FILE}"
    exit 1
  fi
fi

mkdir -p "$(dirname "${REWARD_FILE}")"
python3 "${GRADER_PATH}" "${TARGET_DIR}" \
  --track "${TRACK}" \
  --scenario "${SCENARIO}" \
  --min-score "${MIN_SCORE}" \
  --harbor-reward "${REWARD_FILE}"
