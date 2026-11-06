"""Win-rate retrieval ranking and protocol fingerprints."""

import json

from smartrim import protocol, situation
from smartrim.lesson_store import (
    MIN_EFFECTIVE_VERDICTS,
    SqliteLessonStore,
    effectiveness,
    is_clear_loser,
)


def _lesson(lid, *, helped=0, failed=0, confidence=0.5):
    return {
        "id": lid, "title": f"lesson {lid}",
        "trigger": {"phases": ["early_survival"], "threats": [], "resources": []},
        "recommendation": f"do the thing for {lid}", "rationale": "r",
        "source": ["x"], "confidence": confidence,
        "times_applied": helped + failed,
        "times_helped": helped, "times_failed": failed,
        "status": "active", "tags": [], "source_runs": [],
        "last_updated": "2026-11-01",
    }


SIT = {"phase": "early_survival", "threats": [], "resources": [],
       "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any"}


def test_effectiveness_requires_min_evidence():
    assert effectiveness(100, 0) == 1.0
    assert effectiveness(0, MIN_EFFECTIVE_VERDICTS - 1) == 0.0  # not enough evidence
    assert effectiveness(0, MIN_EFFECTIVE_VERDICTS) == -1.0


def test_is_clear_loser():
    assert is_clear_loser(0, 4) is True
    assert is_clear_loser(1, 3) is True   # -0.5
    assert is_clear_loser(2, 2) is False  # 0.0
    assert is_clear_loser(0, 3) is False  # below min evidence


def test_legacy_retrieval_winner_unjudged_loser():
    winner = _lesson("L-0001", helped=4, failed=0, confidence=0.1)
    unjudged = _lesson("L-0002", confidence=0.9)
    loser = _lesson("L-0003", helped=0, failed=6, confidence=0.95)
    out = situation.retrieve(SIT, [loser, unjudged, winner], limit=5)
    assert [item["id"] for item in out] == ["L-0001", "L-0002", "L-0003"]


def test_sqlite_retrieval_demotes_clear_losers(tmp_path):
    jsonl = tmp_path / "lessons.jsonl"
    db = tmp_path / "lessons.sqlite"
    lessons = [
        _lesson("L-0001", helped=4, failed=0, confidence=0.3),   # clear winner
        _lesson("L-0002", helped=0, failed=6, confidence=0.9),   # clear loser, strong FTS match
        _lesson("L-0003", confidence=0.5),                        # unjudged
    ]
    with open(jsonl, "w", encoding="utf-8") as fh:
        for lesson in lessons:
            fh.write(json.dumps(lesson) + "\n")
    store = SqliteLessonStore(db_path=str(db), jsonl_path=str(jsonl))
    try:
        out = store.retrieve(SIT, limit=5, query_text="lesson")
    finally:
        store.close()
    ids = [lesson.id for lesson in out]
    assert ids[-1] == "L-0002"          # loser sinks despite confidence and FTS match
    assert set(ids[:2]) == {"L-0001", "L-0003"}


def test_protocol_fingerprint_matches():
    marker = protocol.stamp({"run_id": "run-1", "stop_reason": "run_length"},
                            storyteller="Cassandra Classic",
                            difficulty="Adventure story",
                            run_days=11)
    assert protocol.protocol_matches(marker) is True
    assert protocol.protocol_matches({**marker, "protocol": {**marker["protocol"], "storyteller": "Phoebe Chillax"}}) is False
    assert protocol.protocol_matches({**marker, "protocol": {**marker["protocol"], "run_days": 10}}) is False
    assert protocol.protocol_matches({"run_id": "run-1"}) is False
    # game reports difficulty in lowercase; matching is case-insensitive
    assert protocol.protocol_matches(protocol.stamp({"run_id": "run-1"},
                                                    storyteller="Cassandra Classic",
                                                    difficulty="adventure story",
                                                    run_days=11)) is True


def test_protocol_stamp_preserves_marker_fields():
    marker = protocol.stamp({"run_id": "run-1", "custom": "kept"},
                            storyteller="Cassandra Classic",
                            difficulty="Adventure story",
                            run_days=11)
    assert marker["custom"] == "kept"
    assert marker["run_id"] == "run-1"
