import json
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime

SIDECAR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sidecar")
sys.path.insert(0, SIDECAR)

import advice_log
import monitor
import quests
from debrief_bundle import build_bundle
from mcp_client import McpError


class FakeClient:
    """Minimal MCP stand-in. Records calls so tests can assert on request counts."""

    def __init__(self, quests_list=None, detail=None):
        self.calls = []
        self.quests_list = quests_list if quests_list is not None else [
            {"id": 1, "name": "The Hunted Knight", "state": "Ongoing"},
        ]
        self.detail = detail or {}

    def call_tool(self, name, arguments=None):
        self.calls.append((name, arguments or {}))
        if name == "get_quest":
            if arguments and arguments.get("id") is not None:
                base = {"id": arguments["id"], "ok": True, "name": "The Hunted Knight",
                        "description": "<color=#D09B61FF>Antigonos</color> wants you to keep him safe "
                                       "at Tesnus until his shuttle can come pick him up.",
                        "accepter": "Matthew"}
                base.update(self.detail.get(arguments["id"], {}))
                return base
            return {"ok": True, "quests": self.quests_list}
        if name == "get_status":
            return {"colonistCount": 1, "daysPassed": 3, "loaded": True,
                    "difficulty": "Adventure story", "storyteller": "Cassandra Classic"}
        if name == "get_conditions":
            return {"date": "1st of Aprimay, 5500", "hour": 6}
        if name == "list_colonists":
            return {"colonists": [{"name": "A", "health": 90, "mood": 40, "job": "firefighting"}]}
        if name == "get_resources":
            return {"resources": [{"label": "meal", "count": 5}]}
        if name == "get_research":
            return {"projects": []}
        if name == "get_alerts":
            return {"activeAlerts": [{"label": "Fire!"}]}
        return {}

    def names(self):
        return [c[0] for c in self.calls]


class TestQuestRegistry(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.reg = os.path.join(self.tmp, "registry.json")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_description_is_cleaned_and_stored(self):
        client = FakeClient()
        records = quests.update(client, day_label="1st of Aprimay, 5500", path=self.reg)

        self.assertEqual(len(records), 1)
        desc = records[0]["description"]
        self.assertNotIn("<color", desc)
        self.assertIn("keep him safe at Tesnus", desc)
        self.assertEqual(records[0]["accepter"], "Matthew")
        self.assertEqual(records[0]["states"], ["Ongoing"])

    def test_description_is_not_refetched_on_the_next_snapshot(self):
        first = FakeClient()
        quests.update(first, day_label="1st of Aprimay, 5500", path=self.reg)
        detail_calls = [c for c in first.calls if c[0] == "get_quest" and c[1].get("id")]
        self.assertEqual(len(detail_calls), 1)

        second = FakeClient()
        quests.update(second, day_label="2nd of Aprimay, 5500", path=self.reg)
        detail_calls = [c for c in second.calls if c[0] == "get_quest" and c[1].get("id")]
        self.assertEqual(len(detail_calls), 0, "cached description should not be refetched")

    def test_state_history_records_transitions(self):
        quests.update(FakeClient(), day_label="1st of Aprimay, 5500", path=self.reg)
        ended = FakeClient(quests_list=[{"id": 1, "name": "The Hunted Knight", "state": "EndedSuccess"}])
        records = quests.update(ended, day_label="3rd of Jugust, 5500", path=self.reg)

        self.assertEqual(records[0]["states"], ["Ongoing", "EndedSuccess"])
        self.assertEqual(records[0]["last_day"], "3rd of Jugust, 5500")

    def test_a_broken_game_call_does_not_raise(self):
        class Broken:
            def call_tool(self, name, arguments=None):
                raise McpError("mcp down")

        self.assertEqual(quests.list_quests(Broken()), [])
        self.assertEqual(quests.update(Broken(), path=self.reg), [])

    def test_snapshots_merge_quests_by_id(self):
        snaps = [
            {"quests": [{"id": 1, "name": "The Hunted Knight", "states": ["Ongoing"], "description": "d1"}]},
            {"quests": [{"id": 1, "name": "The Hunted Knight", "states": ["EndedSuccess"]},
                        {"id": 2, "name": "Novice Ceremony", "states": ["NotYetAccepted"]}]},
        ]
        merged = quests.quests_from_snapshots(snaps)

        self.assertEqual(len(merged), 2)
        self.assertEqual(merged[0]["states"], ["Ongoing", "EndedSuccess"])
        self.assertEqual(merged[0]["description"], "d1")


class TestAdviceCause(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self._old_dir, self._old_file = advice_log.ADVICE_DIR, advice_log.ADVICE_FILE
        advice_log.ADVICE_DIR = self.tmp
        advice_log.ADVICE_FILE = os.path.join(self.tmp, "advice.jsonl")

    def tearDown(self):
        advice_log.ADVICE_DIR, advice_log.ADVICE_FILE = self._old_dir, self._old_file
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _log(self, situation, run_id="run-x"):
        return advice_log.log_advice(
            run_id=run_id, snapshot_day="1st of Aprimay, 5500", trigger="reflex",
            severity="urgent", situation=situation, actions=[], auto_paused=True,
        )

    def test_cause_is_null_by_default_and_set_by_id(self):
        aid = self._log("Fire!")
        self.assertIsNone(advice_log.read_advice()[0]["event_cause"])
        self.assertTrue(advice_log.set_event_cause(aid, "raider arson"))
        self.assertEqual(advice_log.read_advice()[0]["event_cause"], "raider arson")

    def test_cause_matching_tags_every_record_in_the_burst(self):
        for _ in range(3):
            self._log("Fire!")
        self._log("Antigonos Baspho is DOWNED")

        changed = advice_log.set_cause_matching("run-x", "fire", "raider arson")
        self.assertEqual(changed, 3)

        causes = [r.get("event_cause") for r in advice_log.read_advice()]
        self.assertEqual(causes.count("raider arson"), 3)
        self.assertEqual(causes.count(None), 1, "the downing record must be untouched")

    def test_matching_is_scoped_to_the_run(self):
        self._log("Fire!", run_id="run-a")
        changed = advice_log.set_cause_matching("run-b", "fire", "raider arson")
        self.assertEqual(changed, 0)

    def test_unknown_id_returns_false(self):
        self.assertFalse(advice_log.set_event_cause("adv-nope", "x"))


class TestBundleV3(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.snaps = os.path.join(self.tmp, "snapshots")
        self.debs = os.path.join(self.tmp, "debriefs")
        os.makedirs(self.snaps)
        self._old_base = None

        day = {
            "day": "1st of Aprimay, 5500",
            "timestamp": "2026-10-19T06:00:00",
            "conditions": {"date": "1st of Aprimay, 5500", "hour": 6},
            "status": {"colonistCount": 2},
            "colonists": {"colonists": [
                {"name": "A", "health": 100, "mood": 60, "job": "sleeping"},
                {"name": "B", "health": 100, "mood": 55, "job": "sleeping"},
            ]},
            "resources": {"resources": [{"label": "meal", "count": 30}]},
            "alerts": {"activeAlerts": []},
            "quests": [{"id": 1, "name": "The Hunted Knight", "states": ["Ongoing"],
                        "description": "keep him safe at Tesnus until his shuttle comes",
                        "last_state": "Ongoing"}],
        }
        json.dump(day, open(os.path.join(self.snaps, "day-1.json"), "w"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_timeline_stays_daily_and_incidents_go_to_the_digest(self):
        incident = {
            "day": "reflex-20261019-204826",
            "timestamp": "2026-10-19T20:48:26",
            "conditions": {"date": "1st of Aprimay, 5500", "hour": 20},
            "status": {"colonistCount": 2},
            "colonists": {"colonists": [
                {"name": "A", "health": 83, "mood": 60, "job": "firefighting"},
                {"name": "B", "health": 100, "mood": 55, "job": "drafted"},
            ]},
            "resources": {"resources": [{"label": "meal", "count": 30}]},
            "alerts": {"activeAlerts": [{"label": "Fire!"}, {"label": "Hostile pawn nearby"}]},
            "quests": [{"id": 1, "name": "The Hunted Knight", "states": ["Ongoing"], "last_state": "Ongoing"}],
        }
        json.dump(incident, open(os.path.join(self.snaps, "reflex-20261019-204826.json"), "w"))

        bundle, _ = build_bundle(self.snaps, self.debs, "t-v3", advice_records=[])
        text = open(bundle, encoding="utf-8").read()

        timeline = text.split("## 5. Colony timeline")[1].split("## 6.")[0]
        digest = text.split("## 6. Notable changes")[1].split("## 7.")[0]
        self.assertEqual(timeline.count("### "), 1, "incident snapshot must not become a timeline still")
        self.assertIn("incident snapshots", digest.lower())
        self.assertIn("alerts: Fire!; Hostile pawn nearby", digest)
        self.assertIn("A: HP 83%", digest)
        self.assertIn("hour 20 (20:48)", digest)

    def test_quest_context_appears_in_the_metadata(self):
        bundle, _ = build_bundle(self.snaps, self.debs, "t-v3", advice_records=[])
        text = open(bundle, encoding="utf-8").read()

        self.assertIn("Quest context from the game", text)
        self.assertIn("[1] The Hunted Knight - Ongoing", text)
        self.assertIn("keep him safe at Tesnus", text)

    def test_cause_is_rendered_in_both_advice_places(self):
        rec = {
            "advice_id": "adv-1", "run_id": "t-v3", "snapshot_day": "1st of Aprimay, 5500",
            "timestamp": "2026-10-19T20:48:26", "trigger": "reflex", "severity": "urgent",
            "status": "expired", "auto_paused": True, "situation": "Fire!",
            "event_cause": "raider arson",
        }
        bundle, _ = build_bundle(self.snaps, self.debs, "t-v3", advice_records=[rec])
        text = open(bundle, encoding="utf-8").read()

        digest = text.split("## 6. Notable changes")[1].split("## 7.")[0]
        advice = text.split("## 7. Advice log")[1].split("## 8.")[0]
        self.assertIn("cause: raider arson", digest)
        self.assertIn("cause (recorded after the run): raider arson", advice)

    def test_missing_quest_data_is_not_an_error(self):
        bundle, _ = build_bundle(self.snaps, self.debs, "t-v3", advice_records=[])
        text = open(bundle, encoding="utf-8").read()
        self.assertIn("## 8. Task", text)


class TestReflexSnapshots(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self._old = monitor.SNAPSHOTS_DIR
        monitor.SNAPSHOTS_DIR = self.tmp
        self.reg = os.path.join(self.tmp, "registry.json")

    def tearDown(self):
        monitor.SNAPSHOTS_DIR = self._old
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_name_is_sortable_and_filesystem_safe(self):
        name = monitor.reflex_snapshot_name(datetime(2026, 10, 19, 20, 48, 26))
        self.assertEqual(name, "reflex-20261019-204826")
        self.assertNotIn(" ", name)

    def test_snapshot_writes_quests_and_reflex_prefix(self):
        path = monitor.write_reflex_snapshot(FakeClient(), run_id="t-reflex", quest_registry_path=self.reg)
        data = json.load(open(path, encoding="utf-8"))

        self.assertTrue(os.path.basename(path).startswith("reflex-"))
        self.assertEqual(data["quests"][0]["name"], "The Hunted Knight")
        self.assertIn("keep him safe", data["quests"][0]["description"])
        self.assertEqual(data["summary"]["day"], "1st of Aprimay, 5500")

    def test_snapshots_are_capped(self):
        client = FakeClient()
        for _ in range(3):
            monitor.write_reflex_snapshot(client, run_id="t-cap", limit=2, quest_registry_path=self.reg)
        self.assertIsNone(monitor.write_reflex_snapshot(client, run_id="t-cap", limit=2,
                                                       quest_registry_path=self.reg))
        files = [f for f in os.listdir(os.path.join(self.tmp, "t-cap")) if f.startswith("reflex-")]
        self.assertEqual(len(files), 2)


if __name__ == "__main__":
    unittest.main()
