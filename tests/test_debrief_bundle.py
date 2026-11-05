import json
import os
import shutil
import tempfile
import unittest
from unittest import mock

import smartrim.debrief_bundle as db
from smartrim.debrief_bundle import UNVERIFIED, WIKI_FACTS, _load_wiki_facts, build_bundle


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
                        "## 6. Notable changes", "## 7. Advice log", "## 8. Task"]:
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

    def test_timeline_is_chronological_across_quadrums(self):
        """Aprimay comes before Jugust; file names sort the other way round."""
        snaps = os.path.join(self.tmp, "order")
        os.makedirs(snaps)
        json.dump(valid_snapshot("1st of Jugust, 5500"), open(os.path.join(snaps, "day-a.json"), "w"))
        json.dump(valid_snapshot("15th of Aprimay, 5500"), open(os.path.join(snaps, "day-b.json"), "w"))
        json.dump(valid_snapshot("9th of Aprimay, 5500"), open(os.path.join(snaps, "day-c.json"), "w"))

        bundle, _ = build_bundle(snaps, self.debs, "t-order", advice_records=[])
        text = open(bundle, encoding="utf-8").read()

        apr9 = text.index("### 9th of Aprimay")
        apr15 = text.index("### 15th of Aprimay")
        jug1 = text.index("### 1st of Jugust")
        self.assertLess(apr9, apr15)
        self.assertLess(apr15, jug1)

    def test_outcome_and_biome_come_from_run_meta(self):
        from smartrim import config

        run_dir = config.run_dir("t-meta")
        os.makedirs(run_dir, exist_ok=True)
        with open(os.path.join(run_dir, "meta.json"), "w") as f:
            json.dump({"biome": "temperate forest (flat)"}, f)
        bundle, _ = build_bundle(self.snaps, self.debs, "t-meta", advice_records=[])
        text = open(bundle, encoding="utf-8").read()
        self.assertIn("temperate forest (flat)", text)
        self.assertNotIn("outcome: not stated by the user", text)

    def test_event_digest_reports_transitions_and_urgent_advice(self):
        snaps = os.path.join(self.tmp, "events")
        os.makedirs(snaps)
        first = valid_snapshot("1st of Aprimay, 5500")
        first["alerts"] = {"activeAlerts": []}
        second = valid_snapshot("2nd of Aprimay, 5500")
        second["alerts"] = {"activeAlerts": [{"label": "Low food"}]}
        second["colonists"]["colonists"][0]["health"] = 70
        json.dump(first, open(os.path.join(snaps, "day-1.json"), "w"))
        json.dump(second, open(os.path.join(snaps, "day-2.json"), "w"))

        rec = {"advice_id": "adv-9", "snapshot_day": "2nd of Aprimay, 5500", "timestamp": "t",
               "trigger": "reflex", "severity": "urgent", "status": "helped", "auto_paused": True,
               "situation": "Fire!"}
        bundle, _ = build_bundle(snaps, self.debs, "t-events", advice_records=[rec])
        text = open(bundle, encoding="utf-8").read()

        self.assertIn("new alerts: Low food", text)
        self.assertIn("health 100% -> 70%", text)
        self.assertIn("2nd of Aprimay, 5500: Fire!", text)


class TestWikiFactsLoading(unittest.TestCase):
    def test_load_wiki_facts_returns_lists(self):
        """Test that _load_wiki_facts returns two lists."""
        verified, unverified = _load_wiki_facts()
        self.assertIsInstance(verified, list)
        self.assertIsInstance(unverified, list)

    def test_wiki_facts_are_populated(self):
        """Test that WIKI_FACTS and UNVERIFIED are populated from YAML."""
        # If wiki_facts.yaml exists, should have entries
        import smartrim.debrief_bundle as db
        if os.path.exists(db.WIKI_FACTS_PATH):
            self.assertGreater(len(WIKI_FACTS), 0)
            self.assertGreater(len(UNVERIFIED), 0)

    def test_wiki_facts_format_with_citations(self):
        """Test that verified facts include wiki:citation format."""
        verified, _ = _load_wiki_facts()
        if verified:
            # At least one fact should have a wiki: citation
            has_citation = any("(wiki:" in fact for fact in verified)
            self.assertTrue(has_citation, "Verified facts should include wiki citations")

    def test_wiki_facts_missing_file_returns_empty(self):
        """Test that missing YAML file returns empty lists (graceful degradation)."""
        import smartrim.debrief_bundle as db
        old_path = db.WIKI_FACTS_PATH
        try:
            db.WIKI_FACTS_PATH = "/nonexistent/path/wiki_facts.yaml"
            verified, unverified = db._load_wiki_facts()
            self.assertEqual(verified, [])
            self.assertEqual(unverified, [])
        finally:
            db.WIKI_FACTS_PATH = old_path


class TestWikiExcerpts(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.snaps = os.path.join(self.tmp, "snapshots")
        self.debs = os.path.join(self.tmp, "debriefs")
        self.wiki = os.path.join(self.tmp, "wiki")
        os.makedirs(self.snaps)
        os.makedirs(self.wiki)
        snap = valid_snapshot("3rd of Aprimay, 5500")
        snap["alerts"] = {"activeAlerts": [{"label": "Low food"}, {"label": "Minor break risk"}]}
        json.dump(snap, open(os.path.join(self.snaps, "day-1.json"), "w"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _page(self, name, body):
        with open(os.path.join(self.wiki, f"{name}.md"), "w", encoding="utf-8") as f:
            f.write(body)

    def test_excerpts_are_selected_and_boilerplate_removed(self):
        self._page("Food", (
            "Food - RimWorld Wiki\n\nJump to navigation\n\n"
            "Food is the basic source of nutrition to both humans and animals. "
            "Deprivation of food leads to malnutrition and death.\n\n"
            "This article is suggested to be rewritten. You can help the RimWorld Wiki."
        ))
        self._page("Mood", (
            "Mood - RimWorld Wiki\n\nContents\n\n"
            "Mood is a game mechanic describing a colonist's feelings. "
            "Low moods cause mental breaks, while high moods may trigger inspirations."
        ))
        with mock.patch.object(db, "WIKI_DIR", self.wiki), \
             mock.patch.object(db, "WIKI_FACTS", []), \
             mock.patch.object(db, "UNVERIFIED", []):
            bundle, _ = build_bundle(self.snaps, self.debs, "t-wiki", advice_records=[])
        text = open(bundle, encoding="utf-8").read()
        self.assertIn("wiki:Food", text)
        self.assertIn("wiki:Mood", text)
        self.assertIn("basic source of nutrition", text)
        self.assertNotIn("suggested to be rewritten", text)
        self.assertIn("(none recorded for this run)", text)

    def test_no_pages_states_it_explicitly(self):
        with mock.patch.object(db, "WIKI_DIR", os.path.join(self.tmp, "missing")), \
             mock.patch.object(db, "WIKI_FACTS", []):
            bundle, _ = build_bundle(self.snaps, self.debs, "t-empty", advice_records=[])
        text = open(bundle, encoding="utf-8").read()
        self.assertIn("(no wiki pages matched this run", text)

    def test_curated_facts_take_precedence(self):
        with mock.patch.object(db, "WIKI_DIR", self.wiki), \
             mock.patch.object(db, "WIKI_FACTS", ["Curated fact (wiki:Food)"]):
            bundle, _ = build_bundle(self.snaps, self.debs, "t-curated", advice_records=[])
        text = open(bundle, encoding="utf-8").read()
        self.assertIn("- Curated fact (wiki:Food)", text)


if __name__ == "__main__":
    unittest.main()
