"""Tests for the Layer 2 reflex actor (smartrim/reflex_actor.py)."""

import json
import os
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta
from typing import ClassVar

from smartrim.reflex_actor import (
    ReflexActor,
    close_action_outcomes,
    load_reflex_actions,
)
from smartrim.reflex_preconditions import (
    PRECONDITIONS,
    has_fire_alert,
    has_raid_alert,
    has_shooter_above_5,
    has_unassigned_colonist,
    none_drafted,
)


def _write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        if isinstance(data, str):
            f.write(data)
        else:
            json.dump(data, f)


class _FakeCounselor:
    """Records calls instead of hitting the MCP."""

    def __init__(self):
        self.calls = []

    def say(self, message):
        self.calls.append(("say", message))
        return {"shown": True}

    def draft(self, colonists):
        self.calls.append(("draft", colonists if isinstance(colonists, list) else [colonists]))
        return {"drafted": True}

    def designate(self, *a, **kw):
        self.calls.append(("designate", a, kw))
        return {"designated": True}

    def assign(self, *a, **kw):
        self.calls.append(("assign", a, kw))
        return {"assigned": True}


class _Env:
    def __init__(self):
        self.saved = {k: os.environ.get(k) for k in
                      ("REFLEX_KILL", "REFLEX_DRY_RUN", "REFLEX_PAUSE", "RUN_ID")}

    def set(self, **kw):
        for k, v in kw.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

    def restore(self):
        for k, v in self.saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


class TestReflexWhitelist(unittest.TestCase):
    def test_loads_five_dry_run_actions(self):
        actions = {a.id: a for a in load_reflex_actions()}
        self.assertEqual(len(actions), 5)
        ids = set(actions)
        self.assertEqual(ids, {"draft-and-focus-fire", "designate-firefighting", "assign-beds-to-unassigned", "rescue-downed", "prioritize-treatment"})
        for a in actions.values():
            if a.id == "draft-and-focus-fire":
                self.assertFalse(a.dry_run)
            else:
                self.assertTrue(a.dry_run)
        raid = {"label": "Raid incoming!", "category": "game_alert", "message": "Raid incoming!"}
        fire = {"label": "Fire!", "category": "game_alert", "message": "A fire has broken out"}
        idle = {"label": "1 colonist idle", "category": "idle_colonist", "message": "1 colonist idle"}
        sys_alert = {"label": "Low food", "category": "food_low", "message": "Low food"}
        self.assertTrue(actions["draft-and-focus-fire"].matches(raid))
        self.assertFalse(actions["draft-and-focus-fire"].matches(fire))
        self.assertTrue(actions["designate-firefighting"].matches(fire))
        self.assertTrue(actions["assign-beds-to-unassigned"].matches(idle))
        self.assertFalse(actions["assign-beds-to-unassigned"].matches(sys_alert))
        self.assertFalse(actions["draft-and-focus-fire"].matches(sys_alert))


class TestPreconditions(unittest.TestCase):
    COLONISTS: ClassVar[list[dict]] = [
        {"name": "A", "health": 100, "job": "Constructor", "downed": False},
        {"name": "B", "health": 100, "job": "Constructor", "downed": False},
        {"name": "C", "health": 100, "job": "Constructor", "downed": False},
        {"name": "D", "health": 100, "job": "Constructor", "downed": False},
        {"name": "E", "health": 100, "job": "Constructor", "downed": False},
    ]

    def test_has_raid_alert(self):
        self.assertTrue(has_raid_alert({"alerts": [{"label": "Raid incoming", "category": "game_alert"}]}))
        self.assertTrue(has_raid_alert({"alerts": [{"message": "Enemy detected"}]}))
        self.assertFalse(has_raid_alert({"alerts": [{"label": "Fire!", "category": "game_alert"}]}))
        self.assertFalse(has_raid_alert({"alerts": []}))

    def test_has_fire_alert(self):
        self.assertTrue(has_fire_alert({"alerts": [{"label": "Fire!"}]}))
        self.assertFalse(has_fire_alert({"alerts": [{"label": "Raid"}]}))
        self.assertFalse(has_fire_alert({"alerts": []}))

    def test_has_shooter_above_5(self):
        gs = {"colonists": list(self.COLONISTS)}
        self.assertTrue(has_shooter_above_5(gs))
        gs["colonists"] = gs["colonists"][:4]
        self.assertFalse(has_shooter_above_5(gs))
        gs["colonists"] = list(self.COLONISTS)
        gs["colonists"][0]["downed"] = True
        self.assertFalse(has_shooter_above_5(gs))
        gs["colonists"][0]["downed"] = False
        gs["colonists"][0]["job"] = "Sleeping"
        self.assertFalse(has_shooter_above_5(gs))

    def test_none_drafted(self):
        self.assertTrue(none_drafted({"colonists": self.COLONISTS}))
        drafted = [dict(c) for c in self.COLONISTS]
        drafted[0]["drafted"] = True
        self.assertFalse(none_drafted({"colonists": drafted}))

    def test_has_unassigned_colonist(self):
        self.assertTrue(has_unassigned_colonist({"alerts": [{"category": "idle_colonist"}]}))
        self.assertTrue(has_unassigned_colonist({"colonists": [{"name": "A"}]}))
        self.assertFalse(has_unassigned_colonist({"colonists": [{"name": "A", "bed_id": "bed-1"}]}))
        self.assertFalse(has_unassigned_colonist({"colonists": [], "alerts": []}))

    def test_precondition_registry(self):
        self.assertEqual(set(PRECONDITIONS), {"has_raid_alert", "has_fire_alert",
                                              "has_unassigned_colonist", "has_shooter_above_5", "none_drafted"})


class TestReflexActor(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.actions_file = os.path.join(self.tmp, "actions.jsonl")
        self.human_file = os.path.join(self.tmp, "last_human_action.json")
        self.lock_file = os.path.join(self.tmp, "reflex.lock")
        self.pause_file = os.path.join(self.tmp, "reflex_pause.json")
        self.env = _Env()
        self.env.set(RUN_ID="test-run", REFLEX_KILL="1", REFLEX_DRY_RUN="1", REFLEX_PAUSE="0")
        self.actor = ReflexActor(run_id="test-run", actions_file=self.actions_file,
                                 human_action_file=self.human_file, lock_file=self.lock_file,
                                 pause_file=self.pause_file)

    def tearDown(self):
        self.env.restore()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _read_actions(self):
        if not os.path.exists(self.actions_file):
            return []
        return [json.loads(line) for line in open(self.actions_file, encoding="utf-8") if line.strip()]

    def test_dry_run_writes_audit_and_no_mcp_calls(self):
        self.env.set(REFLEX_KILL="0", REFLEX_DRY_RUN="1", REFLEX_PAUSE="0")
        counselor = _FakeCounselor()
        actor = ReflexActor(run_id="test-run", actions_file=self.actions_file,
                            human_action_file=self.human_file, lock_file=self.lock_file,
                            pause_file=self.pause_file, counselor_mod=counselor)
        gs = {
            "colonists": [{"name": f"C{i}", "health": 100, "job": "Hunter", "downed": False} for i in range(6)],
            "alerts": [{"label": "Raid incoming!", "category": "game_alert", "message": "Raid incoming!"}],
        }
        results = actor.evaluate(gs["alerts"], {}, gs, current_day="10th of Septober, 5500")
        self.assertEqual(len(results), 1)
        r = results[0]
        self.assertIsNone(r["skipped_reason"])
        self.assertTrue(r["precondition_result"])
        self.assertTrue(r["dry_run"])
        self.assertFalse(r["executed"])
        self.assertEqual(counselor.calls, [])  # no MCP write in dry-run
        recs = self._read_actions()
        self.assertEqual(len(recs), 1)
        self.assertEqual(recs[0]["action"], "draft_and_focus_fire")
        self.assertEqual(recs[0]["executed"], False)
        self.assertEqual(recs[0]["dry_run"], True)
        self.assertIsNone(recs[0]["outcome_status"])
        self.assertEqual(recs[0]["run_id"], "test-run")
        self.assertEqual(recs[0]["alert_id"], "game_alert|Raid incoming!")

    def test_kill_switch_disables_all(self):
        self.env.set(REFLEX_KILL="1")
        counselor = _FakeCounselor()
        actor = ReflexActor(run_id="test-run", actions_file=self.actions_file,
                            human_action_file=self.human_file, lock_file=self.lock_file,
                            pause_file=self.pause_file, counselor_mod=counselor)
        gs = {
            "colonists": [{"name": f"C{i}", "health": 100, "job": "Hunter", "downed": False} for i in range(6)],
            "alerts": [{"label": "Raid incoming!", "category": "game_alert"}],
        }
        results = actor.evaluate(gs["alerts"], {}, gs)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["skipped_reason"], "kill_switch")
        self.assertEqual(counselor.calls, [])
        self.assertEqual(self._read_actions(), [])

    def test_live_mode_executes_draft(self):
        self.env.set(REFLEX_KILL="0", REFLEX_DRY_RUN="0", REFLEX_PAUSE="0")
        counselor = _FakeCounselor()
        actor = ReflexActor(run_id="test-run", actions_file=self.actions_file,
                            human_action_file=self.human_file, lock_file=self.lock_file,
                            pause_file=self.pause_file, counselor_mod=counselor)
        gs = {
            "colonists": [{"name": f"C{i}", "health": 100, "job": "Hunter", "downed": False} for i in range(6)],
            "alerts": [{"label": "Raid incoming!", "category": "game_alert"}],
        }
        results = actor.evaluate(gs["alerts"], {}, gs)
        self.assertEqual(len(results), 1)
        r = results[0]
        self.assertFalse(r["dry_run"])
        self.assertTrue(r["executed"])
        self.assertEqual(counselor.calls[0][0], "say")
        self.assertEqual(counselor.calls[1][0], "draft")
        recs = self._read_actions()
        self.assertEqual(len(recs), 1)
        self.assertEqual(recs[0]["executed"], True)
        self.assertEqual(recs[0]["dry_run"], False)

    def test_human_action_window_defers(self):
        self.env.set(REFLEX_KILL="0", REFLEX_DRY_RUN="0", REFLEX_PAUSE="0")
        _write(self.human_file, {"action": "build", "timestamp": datetime.now().isoformat()})
        counselor = _FakeCounselor()
        actor = ReflexActor(run_id="test-run", actions_file=self.actions_file,
                            human_action_file=self.human_file, lock_file=self.lock_file,
                            pause_file=self.pause_file, counselor_mod=counselor)
        gs = {
            "colonists": [{"name": f"C{i}", "health": 100, "job": "Hunter", "downed": False} for i in range(6)],
            "alerts": [{"label": "Raid incoming!", "category": "game_alert"}],
        }
        results = actor.evaluate(gs["alerts"], {}, gs)
        self.assertEqual(results[0]["skipped_reason"], "human_window")
        self.assertEqual(counselor.calls, [])
        self.assertEqual(self._read_actions(), [])

    def test_human_action_window_expired_after_60s(self):
        self.env.set(REFLEX_KILL="0", REFLEX_DRY_RUN="0", REFLEX_PAUSE="0")
        old = (datetime.now() - timedelta(seconds=120)).isoformat()
        _write(self.human_file, {"action": "build", "timestamp": old})
        counselor = _FakeCounselor()
        actor = ReflexActor(run_id="test-run", actions_file=self.actions_file,
                            human_action_file=self.human_file, lock_file=self.lock_file,
                            pause_file=self.pause_file, counselor_mod=counselor)
        gs = {
            "colonists": [{"name": f"C{i}", "health": 100, "job": "Hunter", "downed": False} for i in range(6)],
            "alerts": [{"label": "Raid incoming!", "category": "game_alert"}],
        }
        results = actor.evaluate(gs["alerts"], {}, gs)
        self.assertIsNone(results[0]["skipped_reason"])
        self.assertTrue(results[0]["precondition_result"])
        self.assertEqual(counselor.calls[0][0], "say")

    def test_pause_active_for_one_day(self):
        self.env.set(REFLEX_KILL="0", REFLEX_DRY_RUN="0", REFLEX_PAUSE="1")
        day = "10th of Septober, 5500"
        _write(self.pause_file, {"day": day, "set_at": "2026-01-01T00:00:00"})
        counselor = _FakeCounselor()
        actor = ReflexActor(run_id="test-run", actions_file=self.actions_file,
                            human_action_file=self.human_file, lock_file=self.lock_file,
                            pause_file=self.pause_file, counselor_mod=counselor)
        gs = {
            "colonists": [{"name": f"C{i}", "health": 100, "job": "Hunter", "downed": False} for i in range(6)],
            "alerts": [{"label": "Raid incoming!", "category": "game_alert"}],
        }
        results = actor.evaluate(gs["alerts"], {}, gs, current_day=day)
        self.assertEqual(results[0]["skipped_reason"], "paused")

    def test_pause_cleared_on_day_roll(self):
        self.env.set(REFLEX_KILL="0", REFLEX_DRY_RUN="0", REFLEX_PAUSE="1")
        _write(self.pause_file, {"day": "9th of Septober, 5500", "set_at": "2026-01-01T00:00:00"})
        counselor = _FakeCounselor()
        actor = ReflexActor(run_id="test-run", actions_file=self.actions_file,
                            human_action_file=self.human_file, lock_file=self.lock_file,
                            pause_file=self.pause_file, counselor_mod=counselor)
        gs = {
            "colonists": [{"name": f"C{i}", "health": 100, "job": "Hunter", "downed": False} for i in range(6)],
            "alerts": [{"label": "Raid incoming!", "category": "game_alert"}],
        }
        results = actor.evaluate(gs["alerts"], {}, gs, current_day="10th of Septober, 5500")
        self.assertFalse(os.path.exists(self.pause_file))  # cleared by day roll
        self.assertIsNone(results[0]["skipped_reason"])
        self.assertTrue(results[0]["precondition_result"])

    def test_lock_held_by_other_pid_defers(self):
        self.env.set(REFLEX_KILL="0", REFLEX_DRY_RUN="0", REFLEX_PAUSE="0")
        _write(self.lock_file, "99999")
        import smartrim.reflex_actor as ra
        orig = ra._pid_alive
        ra._pid_alive = lambda pid: True
        try:
            counselor = _FakeCounselor()
            actor = ReflexActor(run_id="test-run", actions_file=self.actions_file,
                                human_action_file=self.human_file, lock_file=self.lock_file,
                                pause_file=self.pause_file, counselor_mod=counselor)
            gs = {
                "colonists": [{"name": f"C{i}", "health": 100, "job": "Hunter", "downed": False} for i in range(6)],
                "alerts": [{"label": "Raid incoming!", "category": "game_alert"}],
            }
            results = actor.evaluate(gs["alerts"], {}, gs)
            self.assertEqual(results[0]["skipped_reason"], "lock_held")
            self.assertEqual(counselor.calls, [])
        finally:
            ra._pid_alive = orig

    def test_dedup_skips_repeat_alert(self):
        self.env.set(REFLEX_KILL="0", REFLEX_DRY_RUN="0", REFLEX_PAUSE="0")
        counselor = _FakeCounselor()
        actor = ReflexActor(run_id="test-run", actions_file=self.actions_file,
                            human_action_file=self.human_file, lock_file=self.lock_file,
                            pause_file=self.pause_file, counselor_mod=counselor)
        gs = {
            "colonists": [{"name": f"C{i}", "health": 100, "job": "Hunter", "downed": False} for i in range(6)],
            "alerts": [{"label": "Raid incoming!", "category": "game_alert"}],
        }
        actor.evaluate(gs["alerts"], {}, gs)
        actor.evaluate(gs["alerts"], {}, gs)  # same poll situation again
        recs = self._read_actions()
        self.assertEqual(len(recs), 1)  # no duplicate action record
        self.assertEqual(counselor.calls[0][0], "say")  # say only once

    def test_precondition_failure_audited_no_call(self):
        self.env.set(REFLEX_KILL="0", REFLEX_DRY_RUN="0", REFLEX_PAUSE="0")
        counselor = _FakeCounselor()
        actor = ReflexActor(run_id="test-run", actions_file=self.actions_file,
                            human_action_file=self.human_file, lock_file=self.lock_file,
                            pause_file=self.pause_file, counselor_mod=counselor)
        gs = {
            "colonists": [{"name": "A", "health": 100, "job": "Hunter", "downed": False}],  # < 5 shooters
            "alerts": [{"label": "Raid incoming!", "category": "game_alert"}],
        }
        results = actor.evaluate(gs["alerts"], {}, gs)
        self.assertEqual(results[0]["skipped_reason"], "preconditions")
        self.assertFalse(results[0]["precondition_result"])
        self.assertEqual(counselor.calls, [])
        recs = self._read_actions()
        self.assertEqual(len(recs), 1)
        self.assertEqual(recs[0]["precondition_result"], False)
        self.assertEqual(recs[0]["executed"], False)

    def test_close_action_outcomes_reuses_close_advice(self):
        _write(self.actions_file,
               json.dumps({"run_id": "test-run", "executed": True, "alert_id": "game_alert|Low food alert",
                           "action": "draft_and_focus_fire", "outcome_status": None}) + "\n" +
               json.dumps({"run_id": "test-run", "executed": True, "alert_id": "game_alert|Raid incoming",
                           "action": "draft_and_focus_fire", "outcome_status": None}) + "\n")
        summary = {"food_days": 6.0, "medicine_count": 10, "min_mood": 50, "alerts": []}
        changed = close_action_outcomes(summary, run_id="test-run", actions_file=self.actions_file)
        self.assertTrue(changed)
        recs = self._read_actions()
        food_rec = next(r for r in recs if "food" in r.get("alert_id", ""))
        raid_rec = next(r for r in recs if "Raid" in r.get("alert_id", ""))
        self.assertEqual(food_rec["outcome_status"], "helped")  # food days >= 5 via _close_advice
        self.assertEqual(raid_rec["outcome_status"], "expired")  # no active threat -> expired
        self.assertIsNotNone(food_rec["outcome_check_at"])


if __name__ == "__main__":
    unittest.main()
