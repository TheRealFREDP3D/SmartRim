# Plan: Address Review.md Recommendations

## Implemented (code/docs)

1. Consolidated `lessons.py` and `situation.py`: `situation.py` is now the single
   source of truth; `lessons.py` is a backward-compatible shim. CLI extracted
   into `main()`.
2. Moved legacy one-off scripts from `sidecar/` to `scratchpad/`.
3. Removed duplicate `HEALTH_THRESHOLD` line in `config.py` (config drift).
4. Added log rotation to `start-monitor.ps1` (archives `monitor.log` > 5MB).
5. Added `pytest.ini` (testpaths/pythonpath) for a standard test runner.
6. Added `README.md` documenting repo boundary, getting started, layout.
7. Added `.pre-commit-config.yaml` for lesson validation + tests on commit.

## Requires user input / environment

8. Git remote: needs a remote URL (`git remote add origin <url>`).
9. Evaluation runs (5 more: 3 adviser-off, 2 adviser-on) require RimWorld sessions.
10. Near-miss live test (Step 7) requires a running game session.

## Deferred (low priority / out of scope)

11. Session log naming standardization.
12. Wiki cache invalidation strategy.
13. Snapshot schema drift resolution (monitor output vs. schema) - needs decision.
14. Pre-commit hook installation (config added; `pre-commit` package not installed).
