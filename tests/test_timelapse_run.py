"""Tests for run-id resolution and the timelapse read path.

Regression cover for the ``current-run`` phantom directory: reading timelapse
state used to call ``os.makedirs`` and left an empty
``runtime/current-run/timelapse`` folder behind just by opening the TUI tab.
"""

import json
import os
import unittest
from unittest import mock

from smartrim import config, timelapse


class TestLatestRunId(unittest.TestCase):
    def _snapshot_run(self, run_id, mtime=None):
        d = config.snapshots_dir(run_id, create=True)
        with open(os.path.join(d, "day-1.json"), "w", encoding="utf-8") as f:
            json.dump({"day": "1st of Aprimay, 5500"}, f)
        if mtime is not None:
            os.utime(d, (mtime, mtime))

    def test_no_runs_returns_none(self):
        self.assertIsNone(config.latest_run_id())

    def test_ignores_empty_and_placeholder_dirs(self):
        os.makedirs(os.path.join(config.RUNTIME_DIR, config.UNSET_RUN_ID), exist_ok=True)
        os.makedirs(os.path.join(config.RUNTIME_DIR, "run-001-adv"), exist_ok=True)
        self.assertIsNone(config.latest_run_id())

    def test_picks_newest_run_with_data(self):
        import time

        now = time.time()
        self._snapshot_run("run-001-adv", mtime=now - 3600)
        self._snapshot_run("run-002-adv", mtime=now - 60)
        self.assertEqual(config.latest_run_id(), "run-002-adv")

    def test_env_run_id_wins(self):
        self._snapshot_run("run-001-adv")
        with mock.patch.dict(os.environ, {"RUN_ID": "run-009-adv"}):
            self.assertEqual(config.resolve_run_id(), "run-009-adv")

    def test_placeholder_env_falls_back_to_latest(self):
        self._snapshot_run("run-003-adv")
        with mock.patch.dict(os.environ, {"RUN_ID": config.UNSET_RUN_ID}):
            self.assertEqual(config.resolve_run_id(), "run-003-adv")

    def test_active_run_file_is_used(self):
        self._snapshot_run("run-004-adv")
        config.write_active_run("run-004-adv", pid=os.getpid())
        self.assertEqual(config.resolve_run_id(), "run-004-adv")
        self.assertEqual(config.read_active_run()["run_id"], "run-004-adv")
        config.clear_active_run(pid=os.getpid())
        self.assertIsNone(config.read_active_run())

    def test_resolve_returns_none_on_fresh_checkout(self):
        self.assertIsNone(config.resolve_run_id())


class TestTimelapseNoSideEffects(unittest.TestCase):
    def setUp(self):
        self.patch_env = mock.patch.object(timelapse, "resolve_run_id", lambda: None)
        self.patch_env.start()

    def tearDown(self):
        self.patch_env.stop()

    def test_list_captures_does_not_create_dir(self):
        data = timelapse.list_captures()
        self.assertIsNone(data["run_id"])
        self.assertIsNone(data["dir"])
        self.assertEqual(data["files"], [])
        self.assertFalse(os.path.exists(os.path.join(config.RUNTIME_DIR, "timelapse")))

    def test_run_dir_read_does_not_create(self):
        d, rid = timelapse._run_dir("run-001-adv", create=False)
        self.assertEqual(rid, "run-001-adv")
        self.assertFalse(os.path.exists(d))

    def test_capture_without_run_returns_error_before_mcp(self):
        with mock.patch("smartrim.mcp_client.McpClient") as client:
            result = timelapse.capture()
        self.assertIn("error", result)
        client.assert_not_called()

    def test_list_captures_reports_existing_run(self):
        run_dir = config.timelapse_dir("run-002-adv", create=True)
        with open(os.path.join(run_dir, "capture-1.png"), "wb") as f:
            f.write(b"not-a-real-png")
        with mock.patch.object(timelapse, "resolve_run_id", lambda: "run-002-adv"):
            data = timelapse.list_captures()
        self.assertEqual(data["run_id"], "run-002-adv")
        self.assertEqual(data["files"], ["capture-1.png"])


if __name__ == "__main__":
    unittest.main()
