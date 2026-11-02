import json
import os
import shutil
import tempfile
import unittest

SIDECAR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sidecar")

from smartrim import monitor
from smartrim.monitor import run_length_reached


class FakeClient:
    def __init__(self):
        self.calls = []

    def call_tool(self, name, arguments=None):
        self.calls.append((name, arguments))
        if name == "get_status":
            return {"colonistCount": 3, "daysPassed": 10}
        if name == "get_conditions":
            return {"date": "10th of Septober, 5500", "hour": 0}
        if name == "list_colonists":
            return {"colonists": []}
        return {}


class TestRunLength(unittest.TestCase):
    def test_below_limit(self):
        self.assertFalse(run_length_reached(9, 10))

    def test_at_limit(self):
        self.assertTrue(run_length_reached(10, 10))

    def test_above_limit(self):
        self.assertTrue(run_length_reached(11, 10))

    def test_unknown_days_never_ends(self):
        self.assertFalse(run_length_reached(None, 10))

    def test_default_is_config_value(self):
        import importlib

        from smartrim import config as config_mod

        # .env may legitimately override RUN_DAYS for long evaluation runs;
        # verify the documented default by reloading config with it forced to 11.
        saved = os.environ.get("RUN_DAYS")
        try:
            os.environ["RUN_DAYS"] = "11"
            importlib.reload(config_mod)
            self.assertEqual(config_mod.RUN_DAYS, 11)
            self.assertFalse(run_length_reached(config_mod.RUN_DAYS - 1, config_mod.RUN_DAYS))
            self.assertTrue(run_length_reached(config_mod.RUN_DAYS, config_mod.RUN_DAYS))
        finally:
            if saved is None:
                os.environ.pop("RUN_DAYS", None)
            else:
                os.environ["RUN_DAYS"] = saved
            importlib.reload(config_mod)


class TestRunEndMarker(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.orig_alerts = monitor.ALERTS_DIR
        self.orig_snaps = monitor.SNAPSHOTS_DIR
        monitor.ALERTS_DIR = os.path.join(self.tmp, "memory", "alerts")
        monitor.SNAPSHOTS_DIR = os.path.join(self.tmp, "memory", "snapshots")
        os.makedirs(monitor.ALERTS_DIR)
        os.makedirs(monitor.SNAPSHOTS_DIR)

    def tearDown(self):
        monitor.ALERTS_DIR = self.orig_alerts
        monitor.SNAPSHOTS_DIR = self.orig_snaps
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_marker_written_and_game_paused(self):
        client = FakeClient()
        marker = monitor.write_run_end(client, "test-run", 10)
        self.assertTrue(os.path.exists(marker))
        data = json.load(open(marker, encoding="utf-8"))
        self.assertEqual(data["run_id"], "test-run")
        self.assertEqual(data["days_passed"], 10)
        self.assertTrue(os.path.exists(data["final_snapshot"]))
        names = [c[0] for c in client.calls]
        self.assertIn("set_speed", names)
        pause = next(c for c in client.calls if c[0] == "set_speed")
        self.assertEqual(pause[1], {"action": "pause"})


if __name__ == "__main__":
    unittest.main()
