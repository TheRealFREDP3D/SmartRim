import json
import os
import sys
import unittest

SIDEcar = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sidecar")
sys.path.insert(0, SIDEcar)

from monitor import run_reflex_checks, normalize_snapshot, write_snapshot
from debrief import generate_debrief
from config import SNAPSHOTS_DIR, DEBRIEFS_DIR, CANDIDATES_DIR


class FakeClient:
    """Replays a recorded snapshot for every tool call."""

    def __init__(self, snapshot):
        self.snapshot = snapshot
        self.calls = []

    def call_tool(self, name, arguments=None):
        self.calls.append(name)
        if name == "get_status":
            return self.snapshot.get("status", {})
        if name == "get_conditions":
            return self.snapshot.get("conditions", {})
        if name == "list_colonists":
            return self.snapshot.get("colonists", {})
        if name == "get_resources":
            return self.snapshot.get("resources", {})
        if name == "get_research":
            return self.snapshot.get("research", {})
        if name == "get_alerts":
            return self.snapshot.get("alerts", {})
        if name == "list_things":
            return {"things": []}
        if name == "list_wildlife":
            return {"animals": []}
        if name == "set_speed":
            return {"ok": True}
        return {}


class TestReflexChecks(unittest.TestCase):
    def setUp(self):
        path = os.path.join(os.path.dirname(__file__), "fixtures", "snapshot_day13.json")
        self.snapshot = json.load(open(path))
        self.client = FakeClient(self.snapshot)

    def test_run_reflex_checks_returns_list(self):
        alerts = run_reflex_checks(self.client)
        self.assertIsInstance(alerts, list)

    def test_low_food_alert_present(self):
        # The Session 5 final state had "Low food" alert
        alerts = run_reflex_checks(self.client)
        cats = [a.get("category") for a in alerts]
        # Either game_alert or food_low should fire
        self.assertTrue(
            "low_food" in cats or "game_alert" in cats or "food_low" in cats,
            f"Expected a food-related alert, got {cats}",
        )

    def test_no_crash_on_empty_snapshot(self):
        empty = {"status": {}, "conditions": {}, "colonists": {}, "resources": {}, "alerts": {}}
        client = FakeClient(empty)
        alerts = run_reflex_checks(client)
        self.assertIsInstance(alerts, list)


class TestNormalizeSnapshot(unittest.TestCase):
    def test_normalize_adds_summary(self):
        path = os.path.join(os.path.dirname(__file__), "fixtures", "snapshot_day13.json")
        snapshot = json.load(open(path))
        out = normalize_snapshot(snapshot)
        self.assertIn("summary", out)
        self.assertIsInstance(out["summary"], dict)

    def test_food_days_counts_meals_not_raw_units(self):
        snapshot = {
            "status": {"colonistCount": 2, "daysPassed": 1},
            "conditions": {},
            "colonists": {"colonists": []},
            "resources": {"resources": [
                {"defName": "RawRice", "label": "rice", "count": 100},
                {"defName": "MealSimple", "label": "simple meal", "count": 4},
            ]},
            "alerts": {},
        }
        out = normalize_snapshot(snapshot)
        # 4 meals / (2 colonists * 2 meals per day) = 1.0 day
        self.assertEqual(out["summary"]["food_days"], 1.0)


class TestDebrief(unittest.TestCase):
    def test_generate_debrief_with_fixture(self):
        import tempfile, shutil
        d = tempfile.mkdtemp()
        sdir = os.path.join(d, "snapshots")
        ddir = os.path.join(d, "debriefs")
        os.makedirs(sdir)
        os.makedirs(ddir)
        # copy fixture as a snapshot
        import shutil
        shutil.copy(
            os.path.join(os.path.dirname(__file__), "fixtures", "snapshot_day13.json"),
            os.path.join(sdir, "day-13th of Septober, 5500.json"),
        )
        path = generate_debrief(sdir, ddir, "test-run")
        self.assertTrue(os.path.exists(path))
        content = open(path).read()
        self.assertIn("Debrief: test-run", content)
        self.assertIn("Colony Timeline", content)


if __name__ == "__main__":
    unittest.main()
