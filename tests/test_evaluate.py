import json
import os
import shutil
import sys
import tempfile
import unittest

SIDECAR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sidecar")
sys.path.insert(0, SIDECAR)

import evaluate
import monitor


def _snap(day, days_passed, colonists, mood, alerts, downed=None):
    return {
        "day": day,
        "status": {"daysPassed": days_passed, "colonistCount": colonists, "difficulty": "Adventure story",
                   "storyteller": "Cassandra Classic"},
        "summary": {
            "day": day,
            "colonist_count": colonists,
            "min_mood": mood,
            "downed": downed or [],
            "alerts": alerts,
        },
        "alerts": {"activeAlerts": [{"label": label} for label in alerts]},
    }


class TestEvaluate(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.runs = os.path.join(self.tmp, "runs")
        self.snaps = os.path.join(self.tmp, "snapshots")
        self.advice = os.path.join(self.tmp, "advice.jsonl")
        os.makedirs(self.runs)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _write_run(self, run_id, arm, days, snaps, advice_rows, urgent=1, pauses=1):
        dest = os.path.join(self.snaps, run_id)
        os.makedirs(dest, exist_ok=True)
        for snap in snaps:
            label = str(snap["day"]).replace("/", "-")
            path = os.path.join(dest, f"day-{label}.json")
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(snap, fh)
        final = os.path.join(dest, f"day-end-day-{days}.json")
        with open(final, "w", encoding="utf-8") as fh:
            json.dump(snaps[-1], fh)
        marker = {
            "run_id": run_id,
            "arm": arm,
            "observe_only": arm == "off",
            "days_passed": days,
            "urgent_alerts": urgent,
            "auto_pauses": pauses,
            "stop_reason": "run_length",
            "snapshots_dir": dest,
            "final_snapshot": final,
        }
        with open(os.path.join(self.runs, f"{run_id}.end.json"), "w", encoding="utf-8") as fh:
            json.dump(marker, fh)
        with open(self.advice, "a", encoding="utf-8") as fh:
            for row in advice_rows:
                row = dict(row)
                row["run_id"] = run_id
                fh.write(json.dumps(row) + "\n")

    def test_summarize_separates_runs_and_arms(self):
        on_snaps = [
            _snap("2nd of Aprimay, 5500", 1, 3, 60, ["Low food"]),
            _snap("10th of Aprimay, 5500", 10, 2, 40, ["Medicine stock low"]),
        ]
        off_snaps = [
            _snap("4th of Aprimay, 5500", 3, 3, 55, []),
            _snap("10th of Aprimay, 5500", 10, 3, 70, []),
        ]
        self._write_run("run-on", "on", 11, on_snaps, [
            {"status": "helped", "severity": "warning", "auto_paused": False},
            {"status": "failed", "severity": "urgent", "auto_paused": True},
            {"status": "open", "severity": "info", "auto_paused": False},
        ], urgent=2, pauses=1)
        self._write_run("run-off", "off", 11, off_snaps, [], urgent=0, pauses=0)

        on = evaluate.summarize_run("run-on", self.runs, self.advice, self.snaps)
        off = evaluate.summarize_run("run-off", self.runs, self.advice, self.snaps)

        self.assertEqual(on["arm"], "on")
        self.assertEqual(off["arm"], "off")
        self.assertEqual(on["colonists_alive_day10"], 2)
        self.assertEqual(off["colonists_alive_day10"], 3)
        self.assertEqual(on["first_low_food_day"], "2nd of Aprimay, 5500")
        self.assertEqual(on["first_medicine_day"], "10th of Aprimay, 5500")
        self.assertIsNone(off["first_low_food_day"])
        self.assertEqual(on["advice_helped"], 1)
        self.assertEqual(on["advice_failed"], 1)
        self.assertEqual(on["advice_ignored"], 1)
        self.assertEqual(off["advice_helped"], 0)
        self.assertEqual(on["auto_pauses"], 1)
        self.assertEqual(off["auto_pauses"], 0)
        self.assertEqual(on["lowest_mood"], 40)

    def test_medical_treatment_is_not_a_medicine_shortage(self):
        snaps = [_snap("3rd of Aprimay, 5500", 2, 3, 50, ["Medical treatment needed"])]
        self._write_run("run-med", "on", 11, snaps, [], urgent=0, pauses=0)
        row = evaluate.summarize_run("run-med", self.runs, self.advice, self.snaps)
        self.assertIsNone(row["first_medicine_day"])

    def test_compare_is_descriptive_and_flags_small_n(self):
        for i, arm in enumerate(("on", "off", "on")):
            snaps = [_snap("10th of Aprimay, 5500", 10, 3 - i, 50 + i, [])]
            self._write_run(f"r{i}", arm, 11, snaps, [], urgent=i, pauses=1 if arm == "on" else 0)
        rows = [evaluate.summarize_run(f"r{i}", self.runs, self.advice, self.snaps) for i in range(3)]
        summary = evaluate.arm_summary(rows)
        self.assertEqual(summary["on"]["n"], 2)
        self.assertEqual(summary["off"]["n"], 1)
        self.assertNotIn("p_value", summary["on"])
        text = evaluate.format_arm_summary(summary)
        self.assertIn("no significance test", text.lower())
        self.assertIn("fewer than 3 runs", text)
        report = evaluate.render_report(rows)
        self.assertIn("Exit not met", report)

    def test_missing_marker_does_not_crash(self):
        row = evaluate.summarize_run("missing", self.runs, self.advice, self.snaps)
        self.assertEqual(row["arm"], "unknown")
        self.assertIsNone(row["days_survived"])
        self.assertFalse(row["has_end_marker"])


class TestObserveOnly(unittest.TestCase):
    def test_flag_parsing(self):
        self.assertTrue(monitor.configure_observe_only(["--observe-only"]))
        self.assertFalse(monitor.configure_observe_only(["--advise"]))
        self.assertFalse(monitor.adviser_acts(True))
        self.assertTrue(monitor.adviser_acts(False))

    def test_end_marker_records_arm(self):
        tmp = tempfile.mkdtemp()
        orig_alerts = monitor.ALERTS_DIR
        orig_snaps = monitor.SNAPSHOTS_DIR
        monitor.ALERTS_DIR = os.path.join(tmp, "alerts")
        monitor.SNAPSHOTS_DIR = os.path.join(tmp, "snapshots")
        os.makedirs(monitor.ALERTS_DIR)
        try:
            client = _Client()
            marker = monitor.write_run_end(client, "off-run", 11, observe_only=True, urgent_alerts=2, auto_pauses=0)
            data = json.load(open(marker, encoding="utf-8"))
            self.assertEqual(data["arm"], "off")
            self.assertEqual(data["auto_pauses"], 0)
            self.assertEqual(data["urgent_alerts"], 2)
            self.assertTrue(os.path.exists(data["final_snapshot"]))
            self.assertIn("off-run", data["snapshots_dir"])
            # observe-only runs never pause, even at run end
            self.assertFalse(any(c[0] == "set_speed" for c in client.calls))
        finally:
            monitor.ALERTS_DIR = orig_alerts
            monitor.SNAPSHOTS_DIR = orig_snaps
            shutil.rmtree(tmp, ignore_errors=True)


class _Client:
    def __init__(self):
        self.calls = []

    def call_tool(self, name, arguments=None):
        self.calls.append((name, arguments))
        if name == "get_status":
            return {"colonistCount": 3, "daysPassed": 11, "difficulty": "Adventure story",
                    "storyteller": "Cassandra Classic"}
        if name == "get_conditions":
            return {"date": "11th of Aprimay, 5500", "hour": 0}
        if name == "list_colonists":
            return {"colonists": []}
        if name == "get_alerts":
            return {"activeAlerts": []}
        return {}


if __name__ == "__main__":
    unittest.main()
