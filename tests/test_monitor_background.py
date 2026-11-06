"""The poll loop must not block on slow, LLM-backed advice work."""

import time

from smartrim import monitor
from tests.test_phase1 import FakeClient


def _snapshot(hour=6):
    return {
        "status": {"colonistCount": 2, "daysPassed": 2, "loaded": True, "programState": "Playing"},
        "conditions": {"date": "3rd of Aprimay, 5500", "hour": hour},
        "colonists": {"colonists": [{"name": "A", "mood": 80, "health": 100}]},
        "resources": {"resources": []},
        "alerts": {"activeAlerts": []},
        "research": {},
    }


def test_slow_daily_say_does_not_block_poll(monkeypatch):
    """A four-minute model call used to stall the loop and delay the reflex."""
    calls = []

    def slow_say(client, conditions, slot=None):
        calls.append(slot)
        time.sleep(0.6)
        return True

    monkeypatch.setattr(monitor, "_say_daily_message", slow_say)
    monkeypatch.setattr(monitor, "SAY_DAILY_HOURS", (6, 18))
    monkeypatch.setattr(monitor, "OBSERVE_ONLY", True)

    started = time.monotonic()
    monitor.poll_once(FakeClient(_snapshot()), monitor.PollResult())
    elapsed = time.monotonic() - started

    assert elapsed < 0.5, f"poll_once waited on the daily say ({elapsed:.2f}s)"
    monitor.drain_background(timeout=5)
    assert calls == ["morning"]


def test_submit_background_survives_failing_task():
    seen = []

    def boom():
        seen.append("ran")
        raise RuntimeError("provider down")

    monitor.submit_background(boom)
    monitor.drain_background(timeout=5)
    assert seen == ["ran"]


def test_drain_background_is_idempotent():
    monitor.drain_background(timeout=1)
    monitor.drain_background(timeout=1)
