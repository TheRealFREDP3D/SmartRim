import os
import unittest
from contextlib import redirect_stdout
from io import StringIO

SIDECAR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sidecar")

from smartrim import situation
from smartrim.situation import (
    build_resources,
    build_situation,
    build_threats,
    classify_phase,
    retrieve,
)


class TestClassifyPhase(unittest.TestCase):
    def test_early_survival_day_1(self):
        self.assertEqual(classify_phase({"day": "1st of Septober, 5500"}, []), "early_survival")

    def test_early_survival_day_7(self):
        self.assertEqual(classify_phase({"day": "7th of Septober, 5500"}, []), "early_survival")

    def test_stabilization_day_10(self):
        self.assertEqual(classify_phase({"day": "10th of Septober, 5500"}, []), "stabilization")

    def test_crisis_overrides_phase(self):
        alerts = [{"category": "downed", "message": "X is DOWNED"}]
        self.assertEqual(classify_phase({"day": "3rd of Septober, 5500"}, alerts), "crisis")

    def test_raid_prep_on_raid_alert(self):
        alerts = [{"category": "game_alert", "label": "Raid: Pollution Unit", "message": "Raid: Pollution Unit"}]
        self.assertEqual(classify_phase({"day": "5th of Septober, 5500"}, alerts), "raid_prep")

    def test_expansion_day_25(self):
        self.assertEqual(classify_phase({"day": "25th of Septober, 5500"}, []), "expansion")

    def test_crisis_from_danger_rating(self):
        alerts = [{"category": "danger_rating", "message": "Map 0 danger rating: High"}]
        self.assertEqual(classify_phase({"day": "5th of Septober, 5500"}, alerts), "crisis")

    def test_day_as_int(self):
        self.assertEqual(classify_phase({"colonist_count": 3, "day": 3}, []), "early_survival")


class TestBuildThreats(unittest.TestCase):
    def test_downed_maps_to_colonist_downed(self):
        threats = build_threats([{"category": "downed", "message": "X is DOWNED"}])
        self.assertIn("colonist_downed", threats)

    def test_food_low_maps(self):
        threats = build_threats([{"category": "food_low", "message": "Food stock low"}])
        self.assertIn("low_food", threats)

    def test_game_alert_keyword_refines(self):
        threats = build_threats([{"category": "game_alert", "message": "Raid: Pollution Unit", "label": "Raid: Pollution Unit"}])
        self.assertIn("raid_incoming", threats)

    def test_empty_alerts(self):
        self.assertEqual(build_threats([]), set())


class TestBuildResources(unittest.TestCase):
    def test_food_under_5_days(self):
        r = build_resources({"food_days": 3, "medicine_count": 10, "resources": {}})
        self.assertIn("food_under_5_days", r)
        self.assertNotIn("food_under_2_days", r)

    def test_food_under_2_days(self):
        r = build_resources({"food_days": 1, "medicine_count": 10, "resources": {}})
        self.assertIn("food_under_2_days", r)

    def test_no_medicine(self):
        r = build_resources({"food_days": 10, "medicine_count": 0, "resources": {}})
        self.assertIn("no_medicine", r)

    def test_medicine_under_5(self):
        r = build_resources({"food_days": 10, "medicine_count": 3, "resources": {}})
        self.assertIn("medicine_under_5", r)

    def test_low_wood(self):
        r = build_resources({"food_days": 10, "medicine_count": 10, "resources": {"WoodLog": 10}})
        self.assertIn("low_wood", r)

    def test_low_steel(self):
        r = build_resources({"food_days": 10, "medicine_count": 10, "resources": {"Steel": 10}})
        self.assertIn("low_steel", r)


class TestBuildSituation(unittest.TestCase):
    def test_returns_all_fields(self):
        sit = build_situation({"day": "5th of Septober, 5500", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "temperate forest", "food_days": 3, "medicine_count": 4, "colonist_count": 3, "resources": {"WoodLog": 200}}, [{"category": "food_low", "message": "Food stock low"}])
        self.assertEqual(sit["phase"], "early_survival")
        self.assertEqual(sit["difficulty"], "Adventure story")
        self.assertIn("low_food", sit["threats"])
        self.assertIn("food_under_5_days", sit["resources"])


class TestRetrieve(unittest.TestCase):
    def setUp(self):
        # Load real lessons
        self.lessons = situation.load_lessons()

    def test_returns_list(self):
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["low_food"], "resources": ["food_under_5_days"]}
        result = retrieve(sit, self.lessons, limit=5)
        self.assertIsInstance(result, list)
        self.assertLessEqual(len(result), 5)

    def test_deterministic(self):
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["low_food"], "resources": ["food_under_5_days"]}
        r1 = retrieve(sit, self.lessons, limit=5)
        r2 = retrieve(sit, self.lessons, limit=5)
        self.assertEqual([lesson["id"] for lesson in r1], [lesson["id"] for lesson in r2])

    def test_scope_strict(self):
        # A lesson scoped to Community builder should not appear for Adventure story
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["raid_incoming"], "resources": []}
        result = retrieve(sit, self.lessons, limit=10)
        for lesson in result:
            diff = lesson.get("trigger", {}).get("difficulty", [])
            if diff:
                self.assertIn("Adventure story", diff)

    def test_no_match_returns_empty(self):
        # A lesson with no scoping criteria at all is too broad to ever retrieve.
        unscoped = [{"id": "L-9999", "title": "t", "status": "active", "confidence": 0.5,
                     "trigger": {"phases": [], "threats": [], "resources": [],
                                 "difficulty": [], "storyteller": [], "biome": []},
                     "times_helped": 0, "times_failed": 0, "times_applied": 0}]
        sit = {"phase": "expansion", "difficulty": "Adventure story", "storyteller": "Cassandra Classic",
               "biome": "any", "threats": [], "resources": []}
        result = retrieve(sit, unscoped, limit=5)
        self.assertEqual(result, [])

    def test_limit_respected(self):
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["low_food", "mood_break_risk"], "resources": ["food_under_5_days"]}
        result = retrieve(sit, self.lessons, limit=3)
        self.assertLessEqual(len(result), 3)

    def test_difficulty_match_is_case_insensitive(self):
        """The situation carries the game's own casing; lessons store canonical labels.

        An exact comparison silently rejected every difficulty-scoped lesson, so the
        food/raid lessons never surfaced (run-007 starved with L-0052 active).
        """
        scoped = [{"id": "L-9998", "title": "scoped", "status": "active", "confidence": 0.5,
                   "trigger": {"phases": ["early_survival"], "threats": ["low_food"],
                               "resources": [], "difficulty": ["Adventure story"],
                               "storyteller": [], "biome": []},
                   "times_helped": 0, "times_failed": 0, "times_applied": 0}]
        sit = {"phase": "early_survival", "difficulty": "adventure story",
               "storyteller": "Cassandra Classic", "biome": "any",
               "threats": ["low_food"], "resources": []}
        result = retrieve(sit, scoped, limit=5)
        self.assertEqual([x["id"] for x in result], ["L-9998"])

    def test_storyteller_match_is_case_insensitive(self):
        scoped = [{"id": "L-9997", "title": "scoped", "status": "active", "confidence": 0.5,
                   "trigger": {"phases": ["early_survival"], "threats": ["low_food"],
                               "resources": [], "difficulty": [],
                               "storyteller": ["Cassandra Classic"], "biome": []},
                   "times_helped": 0, "times_failed": 0, "times_applied": 0}]
        sit = {"phase": "early_survival", "difficulty": "any",
               "storyteller": "cassandra classic", "biome": "any",
               "threats": ["low_food"], "resources": []}
        result = retrieve(sit, scoped, limit=5)
        self.assertEqual([x["id"] for x in result], ["L-9997"])

    def test_status_filter(self):
        # needs_review lessons should not be retrieved
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["raid_incoming"], "resources": []}
        result = retrieve(sit, self.lessons, limit=10)
        for lesson in result:
            self.assertEqual(lesson.get("status"), "active")


class TestGameAlertKeywords(unittest.TestCase):
    """Food/medicine/mood alerts arrive as generic game alerts and must still map
    to a threat tag, otherwise the matching lessons never fire.

    run-007 starved while L-0016 was active because 'Starvation' fell through to
    other_game_alert.
    """

    def _threats(self, label):
        return situation.build_threats([{"category": "game_alert", "label": label}])

    def test_starvation_maps_to_low_food(self):
        self.assertIn("low_food", self._threats("Starvation"))

    def test_food_stock_low_maps_to_low_food(self):
        self.assertIn("low_food", self._threats("Food stock low (0 units)"))

    def test_low_food_maps_to_low_food(self):
        self.assertIn("low_food", self._threats("Low food"))

    def test_medicine_stock_maps_to_medical_untreated(self):
        self.assertIn("medical_untreated", self._threats("Medicine stock low (0)"))

    def test_break_risk_maps_to_mood_break_risk(self):
        self.assertIn("mood_break_risk", self._threats("Minor break risk"))
        self.assertIn("mood_break_risk", self._threats("Major break risk"))

    def test_recreation_maps_to_mood_break_risk(self):
        self.assertIn("mood_break_risk", self._threats("Need recreation variety"))

    def test_enemy_downed_maps_to_raid(self):
        self.assertIn("raid_incoming", self._threats("Enemy downed"))

    def test_unrelated_alert_stays_generic(self):
        self.assertEqual(self._threats("Need batteries"), {"other_game_alert"})


class TestLineage(unittest.TestCase):
    def setUp(self):
        self.lessons = [
            {"id": "L-0001", "title": "Helped", "status": "active", "confidence": 0.6,
             "source_runs": ["r1"], "times_applied": 1, "times_helped": 1, "times_failed": 0},
            {"id": "L-0002", "title": "Contradicted", "status": "active", "confidence": 0.35,
             "source_runs": ["r1"], "times_applied": 1, "times_helped": 0, "times_failed": 1},
            {"id": "L-0003", "title": "Applied", "status": "active", "confidence": 0.5,
             "source_runs": ["r1"], "times_applied": 1, "times_helped": 0, "times_failed": 0},
            {"id": "L-0004", "title": "Other run", "status": "active", "confidence": 0.5,
             "source_runs": ["r2"], "times_applied": 1, "times_helped": 0, "times_failed": 0},
        ]
        self.advice = [
            {"advice_id": "adv-1", "run_id": "r1", "status": "helped",
             "outcome_note": "food recovered", "linked_lessons": ["L-0001"]},
            {"advice_id": "adv-2", "run_id": "r1", "status": "failed",
             "outcome_note": "food fell", "linked_lessons": ["L-0002"]},
            {"advice_id": "adv-3", "run_id": "r1", "status": "open",
             "linked_lessons": ["L-0003"]},
        ]

    def test_load_run_lineage_uses_run_specific_outcomes(self):
        lineage = situation.load_run_lineage("r1", self.lessons, self.advice)
        self.assertEqual([item["lesson"]["id"] for item in lineage], ["L-0001", "L-0002", "L-0003"])
        self.assertEqual([item["relationship"] for item in lineage], ["HELPED", "CONTRADICTED", "APPLIED"])
        self.assertEqual(lineage[1]["outcomes"][0]["note"], "food fell")

    def test_lineage_cli_prints_touched_lessons(self):
        orig_lessons = situation.LESSONS_FILE
        import tempfile
        tmp = tempfile.mkdtemp()
        try:
            path = os.path.join(tmp, "lessons.jsonl")
            import json
            with open(path, "w", encoding="utf-8") as fh:
                for lesson in self.lessons:
                    fh.write(json.dumps(lesson) + "\n")
            situation.LESSONS_FILE = path
            out = StringIO()
            with redirect_stdout(out):
                lineage = situation.load_run_lineage("r1", self.lessons, self.advice)
                for item in lineage:
                    lesson = item["lesson"]
                    print(f"{lesson.get('id')}: {lesson.get('title')}")
                    print(f"  Relationship: {item['relationship']}")
            output = out.getvalue()
            self.assertIn("L-0001: Helped", output)
            self.assertIn("Relationship: CONTRADICTED", output)
            self.assertNotIn("L-0004", output)
        finally:
            situation.LESSONS_FILE = orig_lessons
            import shutil
            shutil.rmtree(tmp, ignore_errors=True)


class TestRankActions(unittest.TestCase):
    def setUp(self):
        self.lessons = situation.load_lessons()

    def test_rank_actions_returns_tuple(self):
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["low_food"], "resources": ["food_under_5_days"]}
        alerts = [{"type": "warning", "category": "food_low", "message": "Food stock low (5 units)"}]
        actions, linked = situation.rank_actions(alerts, sit, self.lessons, limit=5)
        self.assertIsInstance(actions, list)
        self.assertIsInstance(linked, list)

    def test_rank_actions_capped_at_limit(self):
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["low_food", "mood_break_risk"], "resources": ["food_under_5_days"]}
        alerts = [{"type": "warning", "category": "food_low", "message": "Food stock low"}]
        actions, _linked = situation.rank_actions(alerts, sit, self.lessons, limit=2)
        self.assertLessEqual(len(actions), 2)

    def test_rank_actions_deterministic(self):
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["low_food"], "resources": ["food_under_5_days"]}
        alerts = [{"type": "warning", "category": "food_low", "message": "Food stock low"}]
        a1, l1 = situation.rank_actions(alerts, sit, self.lessons, limit=5)
        a2, l2 = situation.rank_actions(alerts, sit, self.lessons, limit=5)
        self.assertEqual(a1, a2)
        self.assertEqual(l1, l2)

    def test_rank_actions_empty_alerts(self):
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": [], "resources": []}
        actions, _ = situation.rank_actions([], sit, self.lessons, limit=5)
        self.assertIsInstance(actions, list)


if __name__ == "__main__":
    unittest.main()
