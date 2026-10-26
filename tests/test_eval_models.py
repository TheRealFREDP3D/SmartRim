import unittest

from smartrim import eval_models

VALID_CANDIDATE = {
    "title": "Food processing priority",
    "cause_chain": [
        "Plant-cutting work priority was too low.",
        "Harvested crops were not processed into meals.",
        "Food days decayed from 7.2 to 1.5 despite a harvest.",
    ],
    "trigger": {
        "phases": ["early_survival"],
        "threats": ["low_food"],
        "resources": ["food_under_5_days"],
        "difficulty": "Adventure story",
        "storyteller": "Cassandra Classic",
        "biome": "any",
    },
    "recommendation": "Assign plant cutting priority 1 so harvested crops become meals.",
    "rationale": "Food days fell from 7.2 to 1.5 despite a harvest on Day 10.",
    "source": ["Day 9: Starvation", "Day 10: harvest"],
    "wiki_pages_used": ["Rice"],
    "unverified_claims": [],
    "confidence": 0.6,
}


def _answer(candidates, section_b=True, label_a=False):
    import json

    body = json.dumps(candidates, indent=2)
    out = ""
    if label_a:
        out += "## Section A\n\n"
    out += f"```json\n{body}\n```\n"
    if section_b:
        out += "\n**Section B: Summary**\n\n* Primary cause: food.\n* What worked: survival.\n"
    return out


class TestDetectSections(unittest.TestCase):
    def test_explicit_labels(self):
        a, b = eval_models._detect_sections(_answer([VALID_CANDIDATE], label_a=True))
        self.assertTrue(a)
        self.assertTrue(b)

    def test_implicit_section_a_is_detected(self):
        """Models often emit the bare JSON array with no 'Section A' heading."""
        a, b = eval_models._detect_sections(_answer([VALID_CANDIDATE], label_a=False))
        self.assertTrue(a, "a JSON fence before Section B must count as Section A")
        self.assertTrue(b)

    def test_section_b_without_json_is_not_section_a(self):
        a, b = eval_models._detect_sections("**Section B: Summary**\n\n* something\n")
        self.assertFalse(a)
        self.assertTrue(b)

    def test_json_without_section_b(self):
        a, b = eval_models._detect_sections(_answer([VALID_CANDIDATE], section_b=False))
        self.assertTrue(a)
        self.assertFalse(b)

    def test_empty_answer(self):
        a, b = eval_models._detect_sections("")
        self.assertFalse(a)
        self.assertFalse(b)


class TestCountBullets(unittest.TestCase):
    def test_counts_dash_and_star_markers(self):
        text = "- one\n* two\n   - three\nnot a bullet\n"
        self.assertEqual(eval_models._count_bullets(text), 3)

    def test_ignores_empty_bullets(self):
        self.assertEqual(eval_models._count_bullets("- \n* x\n"), 1)


class TestScoring(unittest.TestCase):
    def test_well_formed_answer_scores_high(self):
        criteria, total = eval_models.score_debrief_answer("", _answer([VALID_CANDIDATE]))
        self.assertEqual(criteria[1], 2, "format")
        self.assertEqual(criteria[2], 2, "grounding")
        self.assertEqual(criteria[6], 2, "scope fields")
        self.assertEqual(criteria[9], 2, "failure analysis")
        self.assertGreaterEqual(total, 14)

    def test_all_criteria_at_least_one(self):
        """A contract-compliant answer must not score 0 on any criterion."""
        criteria, total = eval_models.score_debrief_answer("", _answer([VALID_CANDIDATE]))
        for i in range(1, 11):
            self.assertGreaterEqual(criteria[i], 1, f"criterion {i} scored 0")

    def test_candidate_lessons_dict_shape_is_accepted(self):
        import json

        body = json.dumps({"candidate_lessons": [VALID_CANDIDATE]}, indent=2)
        raw = f"```json\n{body}\n```\n\n**Section B: Summary**\n\n* x\n"
        criteria, total = eval_models.score_debrief_answer("", raw)
        self.assertEqual(criteria[1], 2)
        self.assertGreater(total, 0)

    def test_missing_section_b_scores_zero_on_format(self):
        criteria, _ = eval_models.score_debrief_answer("", _answer([VALID_CANDIDATE], section_b=False))
        self.assertEqual(criteria[1], 0)

    def test_management_actions_count_as_actionable(self):
        """Models recommend things like 'prioritize' and 'monitor', not just 'build'."""
        cand = dict(VALID_CANDIDATE)
        cand["recommendation"] = "Monitor colonist mood and prioritize plant cutting."
        criteria, _ = eval_models.score_debrief_answer("", _answer([cand]))
        self.assertEqual(criteria[7], 2, "actionability")


if __name__ == "__main__":
    unittest.main()
