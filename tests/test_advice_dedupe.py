"""Duplicate-urgent guard for the monitor and advice log.

Run 002 wrote 99 identical open urgent records in a startup burst (monitor restarts
before the colony was loaded). These tests pin the fix: an identical, still-open
situation is never written twice for the same run.
"""

import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sidecar"))

import advice_log


@pytest.fixture()
def temp_advice(tmp_path, monkeypatch):
    monkeypatch.setattr(advice_log, "ADVICE_DIR", str(tmp_path))
    monkeypatch.setattr(advice_log, "ADVICE_FILE", str(tmp_path / "advice.jsonl"))
    return tmp_path


def _log(situation, run_id="run-test", status_severity="urgent"):
    return advice_log.log_advice(
        run_id=run_id,
        snapshot_day="1st of Aprimay",
        trigger="reflex",
        severity=status_severity,
        situation=situation,
        actions=[{"rank": 1, "action": "Pause game and assess"}],
    )


def test_find_open_duplicate_matches_same_run_and_situation(temp_advice):
    advice_id = _log("Medicine stock low (0); Food stock low (0 units)")

    assert advice_log.find_open_duplicate("run-test", "Medicine stock low (0); Food stock low (0 units)") == advice_id
    assert advice_log.find_open_duplicate("run-test", "something else") is None
    assert advice_log.find_open_duplicate("other-run", "Medicine stock low (0); Food stock low (0 units)") is None


def test_find_open_duplicate_ignores_closed_records(temp_advice):
    advice_id = _log("Fire!")
    advice_log.update_outcome(advice_id, "helped", "burned out")

    assert advice_log.find_open_duplicate("run-test", "Fire!") is None


def test_duplicate_guard_keeps_one_record_per_situation(temp_advice):
    situation = "Medicine stock low (0); Food stock low (0 units)"
    for _ in range(5):
        if advice_log.find_open_duplicate("run-test", situation) is None:
            _log(situation)

    with open(temp_advice / "advice.jsonl", encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]

    assert len(records) == 1
    assert records[0]["status"] == "open"


def test_different_situations_still_log(temp_advice):
    _log("Medicine stock low (0); Food stock low (0 units)")
    _log("Niklas is DOWNED")

    with open(temp_advice / "advice.jsonl", encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]

    assert len(records) == 2
