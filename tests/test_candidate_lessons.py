"""Tests for candidate lesson writing and promotion."""

import json
import os
import shutil
import tempfile
import unittest

from smartrim.debrief_llm import _normalize_trigger, _write_candidate_lessons


class TestNormalizeTrigger(unittest.TestCase):
    def test_normalize_trigger_with_all_fields(self):
        trigger = {
            "phases": ["early_survival"],
            "threats": ["low_food"],
            "resources": ["food_under_5_days"],
            "difficulty": "Adventure story",
            "storyteller": "Cassandra Classic",
            "biome": "temperate forest",
        }
        normalized = _normalize_trigger(trigger)
        self.assertEqual(normalized["phases"], ["early_survival"])
        self.assertEqual(normalized["threats"], ["low_food"])
        self.assertEqual(normalized["resources"], ["food_under_5_days"])
        self.assertEqual(normalized["difficulty"], "Adventure story")
        self.assertEqual(normalized["storyteller"], "Cassandra Classic")
        self.assertEqual(normalized["biome"], "temperate forest")

    def test_normalize_trigger_with_missing_fields(self):
        trigger = {"phases": ["early_survival"]}
        normalized = _normalize_trigger(trigger)
        self.assertEqual(normalized["phases"], ["early_survival"])
        self.assertEqual(normalized["threats"], [])
        self.assertEqual(normalized["resources"], [])
        self.assertEqual(normalized["difficulty"], "any")
        self.assertEqual(normalized["storyteller"], "any")
        self.assertEqual(normalized["biome"], "any")

    def test_normalize_trigger_empty(self):
        normalized = _normalize_trigger({})
        self.assertEqual(normalized["phases"], [])
        self.assertEqual(normalized["threats"], [])
        self.assertEqual(normalized["resources"], [])
        self.assertEqual(normalized["difficulty"], "any")
        self.assertEqual(normalized["storyteller"], "any")
        self.assertEqual(normalized["biome"], "any")


class TestWriteCandidateLessons(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_write_candidate_lessons_creates_file(self):
        candidates = [
            {
                "title": "Test lesson",
                "cause_chain": ["A", "B"],
                "trigger": {
                    "phases": ["early_survival"],
                    "threats": ["low_food"],
                    "resources": [],
                },
                "recommendation": "Do X",
                "rationale": "Because Y",
                "source": ["test-run"],
                "wiki_pages_used": [],
                "unverified_claims": [],
                "confidence": 0.5,
            }
        ]

        path = _write_candidate_lessons("test-run", candidates, candidates_dir=self.tmp)
        self.assertIsNotNone(path)
        self.assertTrue(os.path.exists(path))
        self.assertTrue(path.endswith(".jsonl"))

    def test_write_candidate_lessons_lesson_schema(self):
        candidates = [
            {
                "title": "Test lesson",
                "cause_chain": ["A"],
                "trigger": {"phases": ["early_survival"], "threats": [], "resources": []},
                "recommendation": "Do X",
                "rationale": "Because Y",
                "source": ["test"],
                "wiki_pages_used": [],
                "unverified_claims": [],
                "confidence": 0.5,
            }
        ]

        path = _write_candidate_lessons("test-run", candidates, candidates_dir=self.tmp)

        # Read back and verify schema (skip comment lines)
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    lesson = json.loads(line)
                    break

        self.assertEqual(lesson["status"], "needs_review")
        self.assertEqual(lesson["confidence"], 0.3)  # Floor for single observations
        self.assertEqual(lesson["times_applied"], 0)
        self.assertEqual(lesson["times_helped"], 0)
        self.assertEqual(lesson["times_failed"], 0)
        self.assertTrue(lesson["id"].startswith("C-test-run-"))
        self.assertIn("test-run", lesson["source_runs"])

    def test_write_candidate_lessons_multiple_lessons(self):
        candidates = [
            {
                "title": f"Lesson {i}",
                "cause_chain": [],
                "trigger": {"phases": ["early_survival"], "threats": [], "resources": []},
                "recommendation": f"Do {i}",
                "rationale": f"Because {i}",
                "source": ["test"],
                "wiki_pages_used": [],
                "unverified_claims": [],
                "confidence": 0.5,
            }
            for i in range(3)
        ]

        path = _write_candidate_lessons("test-run", candidates, candidates_dir=self.tmp)

        # Read back and count
        with open(path, encoding="utf-8") as f:
            lessons = [json.loads(line) for line in f if line.strip() and not line.startswith("#")]

        self.assertEqual(len(lessons), 3)
        self.assertEqual(lessons[0]["id"], "C-test-run-0")
        self.assertEqual(lessons[1]["id"], "C-test-run-1")
        self.assertEqual(lessons[2]["id"], "C-test-run-2")

    def test_write_candidate_lessons_without_candidates_dir(self):
        candidates = [{"title": "Test", "cause_chain": [], "trigger": {}, "recommendation": "X", "rationale": "Y", "source": [], "wiki_pages_used": [], "unverified_claims": [], "confidence": 0.5}]

        path = _write_candidate_lessons("test-run", candidates, candidates_dir=None)
        self.assertIsNone(path)


if __name__ == "__main__":
    unittest.main()
