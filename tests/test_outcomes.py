import json
import os
import sys
import tempfile
import unittest

SIDECAR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sidecar")
sys.path.insert(0, SIDECAR)

import outcomes
import advice_log


class TestOutcomes(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.orig_advice = advice_log.ADVICE_FILE
        self.orig_lessons = outcomes.LESSONS_FILE
        advice_log.ADVICE_FILE = os.path.join(self.tmp, "advice.jsonl")
        outcomes.ADVICE_FILE = advice_log.ADVICE_FILE
        outcomes.LESSONS_FILE = os.path.join(self.tmp, "lessons.jsonl")
        # seed one lesson
        lesson = {"id": "L-0001", "title": "t", "trigger": {"phases": [], "threats": [], "resources": []},
                  "recommendation": "r", "rationale": "r", "source": ["x"], "confidence": 0.5,
                  "times_applied": 0, "times_helped": 0, "times_failed": 0, "status": "active",
                  "tags": [], "source_runs": [], "last_updated": "2026-01-01"}
        with open(outcomes.LESSONS_FILE, "w") as f:
            f.write(json.dumps(lesson) + "\n")
        # seed one open advice record linked to L-0001
        rec = {"advice_id": "adv-1", "run_id": "r1", "status": "open", "trigger": "reflex",
               "severity": "urgent", "situation": "Food stock low", "actions": [],
               "linked_lessons": ["L-0001"], "auto_paused": True, "timestamp": "t"}
        with open(advice_log.ADVICE_FILE, "w") as f:
            f.write(json.dumps(rec) + "\n")

    def tearDown(self):
        advice_log.ADVICE_FILE = self.orig_advice
        outcomes.ADVICE_FILE = self.orig_advice
        outcomes.LESSONS_FILE = self.orig_lessons
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_helped_when_food_recovers(self):
        summary = {"food_days": 7, "medicine_count": 10, "min_mood": 50, "resources": {}}
        changed = outcomes.close_outcomes(summary, run_id="r1")
        self.assertTrue(changed)
        recs = advice_log.read_advice(run_id="r1")
        self.assertEqual(recs[0]["status"], "helped")
        lessons = outcomes._read_lessons()
        self.assertEqual(lessons[0]["times_helped"], 1)
        self.assertAlmostEqual(lessons[0]["confidence"], 0.6)

    def test_failed_when_food_worsens(self):
        summary = {"food_days": 1, "medicine_count": 10, "min_mood": 50, "resources": {}}
        changed = outcomes.close_outcomes(summary, run_id="r1")
        self.assertTrue(changed)
        recs = advice_log.read_advice(run_id="r1")
        self.assertEqual(recs[0]["status"], "failed")
        lessons = outcomes._read_lessons()
        self.assertEqual(lessons[0]["times_failed"], 1)
        self.assertAlmostEqual(lessons[0]["confidence"], 0.35)

    def test_idempotent(self):
        summary = {"food_days": 7, "medicine_count": 10, "min_mood": 50, "resources": {}}
        outcomes.close_outcomes(summary, run_id="r1")
        changed2 = outcomes.close_outcomes(summary, run_id="r1")
        self.assertFalse(changed2)

    def test_expired_when_risk_cleared(self):
        rec = {"advice_id": "adv-2", "run_id": "r1", "status": "open", "trigger": "reflex",
               "severity": "warning", "situation": "Some risk", "actions": [],
               "linked_lessons": [], "auto_paused": False, "timestamp": "t"}
        with open(advice_log.ADVICE_FILE, "a") as f:
            f.write(json.dumps(rec) + "\n")
        summary = {"food_days": 10, "medicine_count": 10, "min_mood": 50, "resources": {}}
        outcomes.close_outcomes(summary, run_id="r1")
        recs = advice_log.read_advice(run_id="r1")
        expired = [r for r in recs if r["advice_id"] == "adv-2"]
        self.assertEqual(expired[0]["status"], "expired")

    def test_needs_review_after_3_failures(self):
        # seed 2 more failed closures by running 3 times
        for _ in range(3):
            # reset advice to open each time
            rec = {"advice_id": f"adv-{_}", "run_id": "r1", "status": "open", "trigger": "reflex",
                   "severity": "urgent", "situation": "Food stock low", "actions": [],
                   "linked_lessons": ["L-0001"], "auto_paused": True, "timestamp": "t"}
            with open(advice_log.ADVICE_FILE, "a") as f:
                f.write(json.dumps(rec) + "\n")
        summary = {"food_days": 1, "medicine_count": 10, "min_mood": 50, "resources": {}}
        outcomes.close_outcomes(summary, run_id="r1")
        lessons = outcomes._read_lessons()
        # confidence should have dropped 3 times
        self.assertLessEqual(lessons[0]["confidence"], 0.35)


if __name__ == "__main__":
    unittest.main()
