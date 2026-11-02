"""Sweeper + single-owner tests for the advice log.

- advice_log is the single owner of memory/advice/advice.jsonl (outcomes delegates to it).
- expire_stale ages out old `open` records so stale advice stops polluting debrief bundles.
"""

import json
from datetime import datetime, timedelta

import pytest

from smartrim import advice_log, outcomes


@pytest.fixture()
def temp_advice(tmp_path, monkeypatch):
    monkeypatch.setattr(advice_log, "ADVICE_DIR", str(tmp_path))
    monkeypatch.setattr(advice_log, "ADVICE_FILE", str(tmp_path / "advice.jsonl"))
    monkeypatch.setattr(outcomes, "LESSONS_FILE", str(tmp_path / "lessons.jsonl"))
    return tmp_path


def _seed(path, **overrides):
    rec = {
        "advice_id": "adv-x",
        "run_id": "run-test",
        "timestamp": datetime.now().isoformat(),
        "trigger": "reflex",
        "severity": "urgent",
        "status": "open",
        "outcome_note": None,
        "situation": "Food stock low",
        "linked_lessons": [],
    }
    rec.update(overrides)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    rec["path_hint"] = path
    return rec


class TestExpireStale:
    def test_expires_old_open_records(self, temp_advice):
        path = str(temp_advice / "advice.jsonl")
        old_ts = (datetime.now() - timedelta(days=5)).isoformat()
        _seed(path, advice_id="adv-old", timestamp=old_ts)
        _seed(path, advice_id="adv-fresh")
        _seed(path, advice_id="adv-helped", timestamp=old_ts, status="helped")

        n = advice_log.expire_stale(max_age_days=3)

        statuses = {r["advice_id"]: r["status"] for r in advice_log.read_advice()}
        assert n == 1
        assert statuses["adv-old"] == "expired"
        assert "auto-expired" in next(
            r["outcome_note"] for r in advice_log.read_advice() if r["advice_id"] == "adv-old"
        )
        assert statuses["adv-fresh"] == "open"
        assert statuses["adv-helped"] == "helped"

    def test_idempotent(self, temp_advice):
        path = str(temp_advice / "advice.jsonl")
        old_ts = (datetime.now() - timedelta(days=30)).isoformat()
        _seed(path, advice_id="adv-old", timestamp=old_ts)
        assert advice_log.expire_stale() == 1
        assert advice_log.expire_stale() == 0

    def test_unparseable_timestamp_left_alone(self, temp_advice):
        path = str(temp_advice / "advice.jsonl")
        _seed(path, advice_id="adv-bad", timestamp="t")

        assert advice_log.expire_stale() == 0
        statuses = {r["advice_id"]: r["status"] for r in advice_log.read_advice()}
        assert statuses["adv-bad"] == "open"

    def test_boundary_age_respects_max_age_days(self, temp_advice):
        path = str(temp_advice / "advice.jsonl")
        at_two_days = (datetime.now() - timedelta(days=2)).isoformat()
        _seed(path, advice_id="adv-2d", timestamp=at_two_days)

        assert advice_log.expire_stale(max_age_days=3) == 0
        assert advice_log.expire_stale(max_age_days=1) == 1


class TestCloseOutcomesExpiresStale:
    def test_close_outcomes_ages_out_stale_open_records(self, temp_advice):
        path = temp_advice / "advice.jsonl"
        old_ts = (datetime.now() - timedelta(days=10)).isoformat()
        _seed(str(path), advice_id="adv-ancient", timestamp=old_ts, situation="Fungal infection risk")
        _seed(str(path), advice_id="adv-living", situation="Mood major break risk")

        # min_mood in (20..35) keeps the fresh mood advice open in _close_advice.
        summary = {"min_mood": 30, "alerts": []}
        outcomes.close_outcomes(summary, run_id="run-test")

        statuses = {r["advice_id"]: r["status"] for r in advice_log.read_advice()}
        assert statuses["adv-ancient"] == "expired"
        assert statuses["adv-living"] == "open"

    def test_expired_records_no_longer_reopen_after_debrief(self, temp_advice):
        path = temp_advice / "advice.jsonl"
        old_ts = (datetime.now() - timedelta(days=10)).isoformat()
        _seed(str(path), advice_id="adv-ancient", timestamp=old_ts, situation="Rice stock low")

        summary = {"food_days": 7, "medicine_count": 10, "min_mood": 50, "alerts": []}
        outcomes.close_outcomes(summary, run_id="run-test")
        n = advice_log.expire_stale(max_age_days=3)

        statuses = {r["advice_id"]: r["status"] for r in advice_log.read_advice()}
        assert statuses["adv-ancient"] == "expired"
        assert n == 0


class TestOutcomesDelegatesToAdviceLog:
    def test_close_outcomes_writes_through_advice_log(self, temp_advice, monkeypatch):
        path = temp_advice / "advice.jsonl"
        _seed(str(path), advice_id="adv-1", situation="Food stock low")

        summary = {"food_days": 7, "medicine_count": 10, "min_mood": 50, "alerts": []}
        outcomes.close_outcomes(summary, run_id="run-test")

        statuses = {r["advice_id"]: r["status"] for r in advice_log.read_advice()}
        assert statuses["adv-1"] == "helped"

    def test_outcomes_write_is_atomic(self, temp_advice, monkeypatch):
        from smartrim.advice_log import save_atomic

        path = temp_advice / "advice.jsonl"
        _seed(str(path))
        records = advice_log.read_advice()
        records[0]["status"] = "failed"

        calls = []
        monkeypatch.setattr("smartrim.advice_log.os.replace", lambda a, b: calls.append((a, b)))
        save_atomic(records)

        assert calls, "save_atomic must end with os.replace, not an in-place rewrite"
        assert str(path) == calls[0][1]
