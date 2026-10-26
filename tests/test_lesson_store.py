"""Tests for lesson_store module (SQLite + FTS5 and JSONL stores)."""

import os
import tempfile
import unittest

from smartrim.lesson_store import (
    JsonlLessonStore,
    Lesson,
    SqliteLessonStore,
    get_store,
)


class TestLesson(unittest.TestCase):
    def test_to_dict(self):
        lesson = Lesson(
            id="L-0001",
            title="Test lesson",
            trigger={"phases": ["early_survival"], "threats": ["low_food"], "resources": []},
            recommendation="Do X",
            rationale="Because Y",
            source=["test"],
            confidence=0.8,
            status="active",
            tags=["food"],
        )
        d = lesson.to_dict()
        self.assertEqual(d["id"], "L-0001")
        self.assertEqual(d["title"], "Test lesson")
        self.assertEqual(d["confidence"], 0.8)

    def test_from_dict(self):
        d = {
            "id": "L-0001",
            "title": "Test lesson",
            "trigger": {"phases": ["early_survival"], "threats": ["low_food"], "resources": []},
            "recommendation": "Do X",
            "rationale": "Because Y",
            "source": ["test"],
            "confidence": 0.8,
            "status": "active",
            "tags": ["food"],
            "times_applied": 5,
            "times_helped": 3,
            "times_failed": 1,
        }
        lesson = Lesson.from_dict(d)
        self.assertEqual(lesson.id, "L-0001")
        self.assertEqual(lesson.title, "Test lesson")
        self.assertEqual(lesson.confidence, 0.8)
        self.assertEqual(lesson.times_applied, 5)


class TestJsonlLessonStore(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".jsonl")
        self.temp_path = self.temp_file.name
        self.temp_file.close()

        # Write test lessons
        lessons = [
            {
                "id": "L-0001",
                "title": "Early food shortage",
                "trigger": {"phases": ["early_survival"], "threats": ["low_food"], "resources": ["food_under_5_days"]},
                "recommendation": "Hunt animals",
                "rationale": "Need food",
                "source": ["test"],
                "confidence": 0.9,
                "status": "active",
                "tags": ["food", "early"],
                "times_applied": 10,
                "times_helped": 8,
                "times_failed": 1,
            },
            {
                "id": "L-0002",
                "title": "Raid defense",
                "trigger": {"phases": ["raid_prep"], "threats": ["raid_incoming"], "resources": []},
                "recommendation": "Build sandbags",
                "rationale": "Need defense",
                "source": ["test"],
                "confidence": 0.8,
                "status": "active",
                "tags": ["defense"],
                "times_applied": 5,
                "times_helped": 4,
                "times_failed": 0,
            },
            {
                "id": "L-0003",
                "title": "Retired lesson",
                "trigger": {"phases": ["early_survival"], "threats": ["low_food"], "resources": []},
                "recommendation": "Should not appear",
                "rationale": "Retired",
                "source": ["test"],
                "confidence": 0.5,
                "status": "retired",
                "tags": [],
                "times_applied": 0,
                "times_helped": 0,
                "times_failed": 0,
            },
        ]
        with open(self.temp_path, "w", encoding="utf-8") as f:
            for lesson in lessons:
                f.write(__import__("json").dumps(lesson) + "\n")

        self.store = JsonlLessonStore(self.temp_path)

    def tearDown(self):
        os.unlink(self.temp_path)

    def test_load_all(self):
        lessons = self.store.load_all()
        self.assertEqual(len(lessons), 3)
        self.assertEqual(lessons[0].id, "L-0001")

    def test_retrieve_exact_match(self):
        situation = {
            "phase": "early_survival",
            "threats": ["low_food"],
            "resources": ["food_under_5_days"],
            "difficulty": "any",
            "storyteller": "any",
            "biome": "any",
        }
        results = self.store.retrieve(situation, limit=5)
        self.assertGreater(len(results), 0)
        # Should not include retired lesson
        for r in results:
            self.assertEqual(r.status, "active")

    def test_retrieve_no_match(self):
        situation = {
            "phase": "expansion",
            "threats": [],
            "resources": [],
            "difficulty": "any",
            "storyteller": "any",
            "biome": "any",
        }
        results = self.store.retrieve(situation, limit=5)
        self.assertEqual(len(results), 0)

    def test_retrieve_ignores_query_text(self):
        # JSONL store should ignore query_text parameter
        situation = {
            "phase": "early_survival",
            "threats": ["low_food"],
            "resources": ["food_under_5_days"],
            "difficulty": "any",
            "storyteller": "any",
            "biome": "any",
        }
        results1 = self.store.retrieve(situation, limit=5, query_text=None)
        results2 = self.store.retrieve(situation, limit=5, query_text="food shortage")
        self.assertEqual(len(results1), len(results2))

    def test_reindex_noop(self):
        # JSONL store reindex should be a no-op
        self.store.reindex()  # Should not raise


class TestSqliteLessonStore(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(delete=False, suffix=".sqlite")
        self.db_path = self.temp_db.name
        self.temp_db.close()

        self.temp_jsonl = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".jsonl")
        self.jsonl_path = self.temp_jsonl.name
        self.temp_jsonl.close()

        # Write test lessons to JSONL
        lessons = [
            {
                "id": "L-0001",
                "title": "Early food shortage",
                "trigger": {"phases": ["early_survival"], "threats": ["low_food"], "resources": ["food_under_5_days"]},
                "recommendation": "Hunt animals for food",
                "rationale": "Colony needs food immediately",
                "source": ["test"],
                "confidence": 0.9,
                "status": "active",
                "tags": ["food", "early", "survival"],
                "times_applied": 10,
                "times_helped": 8,
                "times_failed": 1,
            },
            {
                "id": "L-0002",
                "title": "Raid defense preparation",
                "trigger": {"phases": ["raid_prep"], "threats": ["raid_incoming"], "resources": []},
                "recommendation": "Build sandbag defenses",
                "rationale": "Prepare for incoming raid",
                "source": ["test"],
                "confidence": 0.8,
                "status": "active",
                "tags": ["defense", "combat"],
                "times_applied": 5,
                "times_helped": 4,
                "times_failed": 0,
            },
            {
                "id": "L-0003",
                "title": "Retired lesson",
                "trigger": {"phases": ["early_survival"], "threats": ["low_food"], "resources": []},
                "recommendation": "Should not appear",
                "rationale": "Retired",
                "source": ["test"],
                "confidence": 0.5,
                "status": "retired",
                "tags": [],
                "times_applied": 0,
                "times_helped": 0,
                "times_failed": 0,
            },
        ]
        with open(self.jsonl_path, "w", encoding="utf-8") as f:
            for lesson in lessons:
                f.write(__import__("json").dumps(lesson) + "\n")

        self.store = SqliteLessonStore(db_path=self.db_path, jsonl_path=self.jsonl_path)
        self.store.reindex()

    def tearDown(self):
        self.store.close()
        os.unlink(self.db_path)
        os.unlink(self.jsonl_path)

    def test_load_all(self):
        lessons = self.store.load_all()
        self.assertEqual(len(lessons), 3)
        self.assertEqual(lessons[0].id, "L-0001")

    def test_retrieve_exact_match(self):
        situation = {
            "phase": "early_survival",
            "threats": ["low_food"],
            "resources": ["food_under_5_days"],
            "difficulty": "any",
            "storyteller": "any",
            "biome": "any",
        }
        results = self.store.retrieve(situation, limit=5)
        self.assertGreater(len(results), 0)
        # Should not include retired lesson
        for r in results:
            self.assertEqual(r.status, "active")

    def test_retrieve_no_match(self):
        situation = {
            "phase": "expansion",
            "threats": [],
            "resources": [],
            "difficulty": "any",
            "storyteller": "any",
            "biome": "any",
        }
        results = self.store.retrieve(situation, limit=5)
        self.assertEqual(len(results), 0)

    def test_retrieve_with_query_text(self):
        situation = {
            "phase": "early_survival",
            "threats": ["low_food"],
            "resources": ["food_under_5_days"],
            "difficulty": "any",
            "storyteller": "any",
            "biome": "any",
        }
        # With semantic query text
        results = self.store.retrieve(situation, limit=5, query_text="food shortage hunt animals")
        self.assertGreater(len(results), 0)

    def test_reindex(self):
        # Add a new lesson to JSONL
        new_lesson = {
            "id": "L-0004",
            "title": "New lesson",
            "trigger": {"phases": ["stabilization"], "threats": [], "resources": []},
            "recommendation": "New recommendation",
            "rationale": "New rationale",
            "source": ["test"],
            "confidence": 0.7,
            "status": "active",
            "tags": ["new"],
            "times_applied": 0,
            "times_helped": 0,
            "times_failed": 0,
        }
        with open(self.jsonl_path, "a", encoding="utf-8") as f:
            f.write(__import__("json").dumps(new_lesson) + "\n")

        # Reindex
        self.store.reindex()

        # Verify new lesson is loaded
        lessons = self.store.load_all()
        self.assertEqual(len(lessons), 4)
        lesson_ids = [lesson.id for lesson in lessons]
        self.assertIn("L-0004", lesson_ids)


class TestGetStore(unittest.TestCase):
    def test_get_sqlite_store(self):
        store = get_store(use_sqlite=True)
        self.assertIsInstance(store, SqliteLessonStore)
        store.close()

    def test_get_jsonl_store(self):
        store = get_store(use_sqlite=False)
        self.assertIsInstance(store, JsonlLessonStore)


if __name__ == "__main__":
    unittest.main()
