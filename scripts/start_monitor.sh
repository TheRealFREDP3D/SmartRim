#!/usr/bin/env bash
# Start the SmartRim reflex monitor.
#
# Usage:
#   ./scripts/start_monitor.sh              # adviser on (pauses + logs advice)
#   ./scripts/start_monitor.sh --observe-only  # adviser off (snapshots only)
#   ./scripts/start_monitor.sh --advise       # adviser on (explicit)
#
# Environment:
#   RUN_ID          run identifier (default: current-run)
#   OBSERVE_ONLY    1 = observe-only, 0 = adviser on (default: 0)
#   POLL_INTERVAL   seconds between polls (default: 30)
set -euo pipefail

cd "$(dirname "$0")/.."

export PYTHONPATH="src${PYTHONPATH:+:$PYTHONPATH}"

exec python -m smartrim.monitor "$@"
