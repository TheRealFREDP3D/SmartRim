"""Tests for the Layer 2 replay harness (sidecar/replay.py)."""

import json
import os
import shutil
import sys
import tempfile
import unittest

from smartrim.replay import run_replay


def _snap(day, days_passed, colonists, alerts):
    return {
        "day": day,
        "status": {"daysPassed": days_passed, "colonistCount": len(colonists)},
        "summary": {
            "day": day,
            "colonist_count": len(colonists),
            "downed": [],
            "alerts": [a.get("label") for a in alerts],
        },
        "conditions": {"date": day, "hour": 10, "seasonLabel": "Summer"},
        "colonists": {"colonists": colonists},
        "alerts": {"activeAlerts": alerts},
        "resources": {"resources": []},
    }


class _Env:
    def __init__(self):
        self.saved = {k: os.environ.get(k) for k in
                      ("REFLEX_KILL", "REFLEX_DRY_RUN", "REFLEX_PAUSE",
                       "REFLEX_ACTIONS_FILE", "REFLEX_HUMAN_ACTION_FILE",
                       "REFLEX_LOCK_FILE", "REFLEX_PAUSE_FILE", "RUN_ID")}

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


class TestReplay(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = os.path.join(self.tmp, "snapshots")
        self.actions_file = os.path.join(self.tmp, "actions.jsonl")
        self.human_file = os.path.join(self.tmp, "last_human_action.json")
        self.lock_file = os.path.join(self.tmp, "reflex.lock")
        self.pause_file = os.path.join(self.tmp, "reflex_pause.json")
        self.env = _Env()
        self.env.set(RUN_ID="replay-run", REFLEX_KILL="0", REFLEX_DRY_RUN="0", REFLEX_PAUSE="0",
                     REFLEX_ACTIONS_FILE=self.actions_file,
                     REFLEX_HUMAN_ACTION_FILE=self.human_file,
                     REFLEX_LOCK_FILE=self.lock_file,
                     REFLEX_PAUSE_FILE=self.pause_file)

    def tearDown(self):
        self.env.restore()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _write_run(self, run_id, snaps):
        dest = os.path.join(self.root, run_id)
        os.makedirs(dest, exist_ok=True)
        for snap in snaps:
            label = str(snap["day"]).replace("/", "-")
            with open(os.path.join(dest, f"day-{label}.json"), "w", encoding="utf-8") as f:
                json.dump(snap, f)

    def test_replay_detects_draft_delta(self):
        colonists = [
            {"name": f"C{i}", "health": 100, "drafted": False} for i in range(6)
        ]
        s1 = _snap("10th of Septober, 5500", 9, colonists,
                   [{"label": "Raid incoming!", "category": "game_alert"}])
        drafted = [dict(c) for c in colonists]
        for c in drafted:
            c["drafted"] = True
        s2 = _snap("11th of Septober, 5500", 10, drafted, [])
        self._write_run("run-ok", [s1, s2])
        rc = run_replay("run-ok", self.root)
        self.assertEqual(rc, 0)

    def test_replay_flags_missing_delta(self):
        colonists = [
            {"name": f"C{i}", "health": 100, "drafted": False} for i in range(6)
        ]
        s1 = _snap("10th of Septober, 5500", 9, colonists,
                   [{"label": "Raid incoming!", "category": "game_alert"}])
        s2 = _snap("11th of Septober, 5500", 10, colonists, [])
        self._write_run("run-bad", [s1, s2])
        rc = run_replay("run-bad", self.root)
        self.assertNotEqual(rc, 0)

    def test_replay_needs_two_snapshots(self):
        colonists = [{"name": "A", "health": 100, "drafted": False}]
        s1 = _snap("10th of Septober, 5500", 9, colonists, [])
        self._write_run("run-single", [s1])
        rc = run_replay("run-single", self.root)
        self.assertEqual(rc, 1)

    def test_replay_handles_reflex_incident_snapshots(self):
        colonists = [
            {"name": f"C{i}", "health": 100, "drafted": False} for i in range(6)
        ]
        s1 = _snap("10th of Septober, 5500", 9, colonists,
                   [{"label": "Raid incoming!", "category": "game_alert"}])
        sreflex = _snap("reflex-20261025-190000", 9,
                        [dict(c, drafted=True) for c in colonists],
                        [{"label": "Raid incoming!", "category": "game_alert"}])
        drafted = [dict(c) for c in colonists]
        for c in drafted:
            c["drafted"] = True
        s2 = _snap("11th of Septober, 5500", 10, drafted, [])
        self._write_run("run-inc", [s1, sreflex, s2])
        rc = run_replay("run-inc", self.root)
        self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
