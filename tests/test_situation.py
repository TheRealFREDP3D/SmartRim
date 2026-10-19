import json
import os
import sys
import unittest

SIDECAR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sidecar")
sys.path.insert(0, SIDECAR)

import lessons
import situation
from situation import classify_phase, build_situation, build_threats, build_resources, retrieve


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
        self.lessons = lessons.load_lessons()

    def test_returns_list(self):
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["low_food"], "resources": ["food_under_5_days"]}
        result = retrieve(sit, self.lessons, limit=5)
        self.assertIsInstance(result, list)
        self.assertLessEqual(len(result), 5)

    def test_deterministic(self):
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["low_food"], "resources": ["food_under_5_days"]}
        r1 = retrieve(sit, self.lessons, limit=5)
        r2 = retrieve(sit, self.lessons, limit=5)
        self.assertEqual([l["id"] for l in r1], [l["id"] for l in r2])

    def test_scope_strict(self):
        # A lesson scoped to Community builder should not appear for Adventure story
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["raid_incoming"], "resources": []}
        result = retrieve(sit, self.lessons, limit=10)
        for l in result:
            diff = l.get("trigger", {}).get("difficulty", [])
            if diff:
                self.assertIn("Adventure story", diff)

    def test_no_match_returns_empty(self):
        sit = {"phase": "expansion", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": [], "resources": []}
        result = retrieve(sit, self.lessons, limit=5)
        self.assertEqual(result, [])

    def test_limit_respected(self):
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["low_food", "mood_break_risk"], "resources": ["food_under_5_days"]}
        result = retrieve(sit, self.lessons, limit=3)
        self.assertLessEqual(len(result), 3)

    def test_status_filter(self):
        # needs_review lessons should not be retrieved
        sit = {"phase": "early_survival", "difficulty": "Adventure story", "storyteller": "Cassandra Classic", "biome": "any", "threats": ["raid_incoming"], "resources": []}
        result = retrieve(sit, self.lessons, limit=10)
        for l in result:
            self.assertEqual(l.get("status"), "active")


if __name__ == "__main__":
    unittest.main()
