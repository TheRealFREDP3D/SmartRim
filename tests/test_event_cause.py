"""Auto event_cause tagging from the game's own alerts."""

import json
import os

from smartrim import config, event_cause, monitor


def _alerts(*pairs):
    return [{"type": "urgent", "category": cat, "message": msg} for cat, msg in pairs]


def test_derive_colony_death():
    assert event_cause.derive_event_cause(_alerts(("colony_death", "All colonists dead"))) == "colony_death"


def test_derive_fire_during_raid_vs_alone():
    assert event_cause.derive_event_cause(
        _alerts(("game_alert", "Fire!"), ("game_alert", "Raid incoming"))) == "fire_during_raid"
    assert event_cause.derive_event_cause(_alerts(("game_alert", "Fire!"))) == "fire_unknown"


def test_derive_raid_and_predator():
    assert event_cause.derive_event_cause(_alerts(("game_alert", "Enemies"))) == "hostile_raid"
    assert event_cause.derive_event_cause(_alerts(("game_alert", "Raiders attack"))) == "hostile_raid"
    assert event_cause.derive_event_cause(_alerts(("danger_rating", "Map 0 danger rating: High"))) == "high_danger"


def test_derive_conditions():
    assert event_cause.derive_event_cause(_alerts(("mood_extreme", "Bo mood at 4%"))) == "mood_break_risk"
    assert event_cause.derive_event_cause(_alerts(("downed", "Bo is DOWNED"))) == "colonist_downed"
    assert event_cause.derive_event_cause(_alerts(("food_low", "Food stock low (9 units)"))) == "food_exhaustion"
    assert event_cause.derive_event_cause(_alerts(("medicine_low", "Medicine stock low (1)"))) == "medicine_shortage"
    assert event_cause.derive_event_cause(_alerts(("medical_treatment_needed", "Medical treatment needed"))) == "medical_emergency"
    assert event_cause.derive_event_cause(_alerts(("sleeping_during_threat", "Ana is sleeping during a threat"))) == "threat_response_failure"


def test_derive_unclassified_and_empty():
    assert event_cause.derive_event_cause(_alerts(("game_alert", "Weather changing"))) == "unclassified"
    assert event_cause.derive_event_cause([]) is None


def test_derive_from_text_and_categories():
    assert event_cause.derive_event_cause(None, text="Enemy downed", categories="game_alert") == "hostile_raid"
    assert event_cause.derive_event_cause(None, text="Fire!", categories="game_alert") == "fire_unknown"
    assert event_cause.derive_event_cause(None, text="", categories="") is None


def _seed_advice(run_dir, records):
    path = os.path.join(run_dir, "advice.jsonl")
    with open(path, "w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec) + "\n")
    return path


def _record(rid, **over):
    rec = {"advice_id": f"adv-{rid}", "run_id": rid, "trigger": "reflex",
           "severity": "urgent", "status": "expired", "situation": "Enemy downed",
           "reflex_name": "game_alert", "event_cause": None, "auto_paused": True}
    rec.update(over)
    return rec


def test_backfill_tags_urgent_records(tmp_path):
    run_dir = config.run_dir("run-960-adv")
    os.makedirs(run_dir)
    path = _seed_advice(run_dir, [
        _record("run-960-adv"),
        _record("run-960-adv", advice_id="adv-keep", event_cause="raider arson"),
        _record("run-960-adv", advice_id="adv-sched", trigger="scheduled", severity="info",
                event_cause=None),
    ])
    changed = event_cause.backfill("run-960-adv")
    assert changed == 1
    recs = {r["advice_id"]: r for r in map(json.loads, open(path, encoding="utf-8"))}
    assert recs["adv-run-960-adv"]["event_cause"] == "hostile_raid"
    assert recs["adv-run-960-adv"]["event_cause_source"] == "auto:alerts"
    assert recs["adv-keep"]["event_cause"] == "raider arson"     # human tag preserved
    assert recs["adv-keep"].get("event_cause_source") is None     # not re-labelled
    assert recs["adv-sched"]["event_cause"] is None               # informational, untagged


def test_backfill_all_runs(tmp_path):
    for rid in ("run-961-adv", "run-962-adv"):
        run_dir = config.run_dir(rid)
        os.makedirs(run_dir)
        _seed_advice(run_dir, [_record(rid, trigger="reflex")])
    assert event_cause.backfill(all_runs=True) == 2


def test_backfill_dry_run_writes_nothing(tmp_path):
    run_dir = config.run_dir("run-963-adv")
    os.makedirs(run_dir)
    path = _seed_advice(run_dir, [_record("run-963-adv")])
    before = open(path, encoding="utf-8").read()
    assert event_cause.backfill("run-963-adv", dry_run=True) == 1
    assert open(path, encoding="utf-8").read() == before


def test_monitor_auto_event_cause_smoke():
    cause = monitor._auto_event_cause(_alerts(("game_alert", "Fire!"), ("game_alert", "Enemies")))
    assert cause == "fire_during_raid"
    assert monitor._auto_event_cause([]) is None
