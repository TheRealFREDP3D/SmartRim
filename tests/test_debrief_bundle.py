import json
import os
import shutil
import sys
import tempfile
import unittest

SIDECAR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sidecar")
sys.path.insert(0, SIDECAR)

from debrief_bundle import build_bundle


def valid_snapshot(day, mood=30):
    return {
        "day": day,
        "conditions": {"date": day, "hour": 6},
        "status": {"colonistCount": 2},
        "colonists": {"colonists": [
            {"name": "A", "health": 100, "mood": mood, "downed": False, "job": "researching"},
            {"name": "B", "health": 60, "mood": 50, "downed": True, "job": "resting"},
        ]},
        "resources": {"resources": [{"label": "meal", "count": 5}]},
        "alerts": {"activeAlerts": [{"label": "Low food"}]},
    }


class TestDebriefBundle(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.snaps = os.path.join(self.tmp, "snapshots")
        self.debs = os.path.join(self.tmp, "debriefs")
        os.makedirs(self.snaps)
        json.dump(valid_snapshot("1st of Septober, 5500"), open(os.path.join(self.snaps, "day-1.json"), "w"))
        json.dump(valid_snapshot("2nd of Septober, 5500", mood=18), open(os.path.join(self.snaps, "day-2.json"), "w"))
        # invalid: game was at the main menu, no colony data
        json.dump({"day": "x", "status": {"loaded": False}, "colonists": {"loaded": False, "message": "No colony"}},
                  open(os.path.join(self.snaps, "day-x.json"), "w"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_bundle_has_all_sections(self):
        bundle, _ = build_bundle(self.snaps, self.debs, "t-run", advice_records=[])
        text = open(bundle, encoding="utf-8").read()
        for section in ["## 1. Instructions", "## 2. Run metadata", "## 3. Wiki facts",
                        "## 4. Claims that are NOT verified", "## 5. Colony timeline",
                        "## 6. Advice log", "## 7. Task"]:
            self.assertIn(section, text)

    def test_invalid_snapshot_is_skipped_and_reported(self):
        bundle, _ = build_bundle(self.snaps, self.debs, "t-run", advice_records=[])
        text = open(bundle, encoding="utf-8").read()
        self.assertIn("snapshots skipped (no colony data)", text)
        self.assertIn("day-x", text)

    def test_timeline_contains_downed_and_mood(self):
        bundle, _ = build_bundle(self.snaps, self.debs, "t-run", advice_records=[])
        text = open(bundle, encoding="utf-8").read()
        self.assertIn("[DOWNED]", text)
        self.assertIn("mood 18%", text)
        self.assertIn("Low food", text)

    def test_response_template_created_once(self):
        _, resp = build_bundle(self.snaps, self.debs, "t-run", advice_records=[])
        self.assertTrue(os.path.exists(resp))
        open(resp, "w", encoding="utf-8").write("edited by user")
        build_bundle(self.snaps, self.debs, "t-run", advice_records=[])
        self.assertEqual(open(resp, encoding="utf-8").read(), "edited by user")

    def test_advice_records_listed(self):
        rec = {"advice_id": "adv-1", "timestamp": "t", "trigger": "reflex", "severity": "urgent",
               "status": "open", "auto_paused": True, "situation": "A is DOWNED"}
        bundle, _ = build_bundle(self.snaps, self.debs, "t-run", advice_records=[rec])
        text = open(bundle, encoding="utf-8").read()
        self.assertIn("adv-1", text)
        self.assertIn("A is DOWNED", text)


if __name__ == "__main__":
    unittest.main()
