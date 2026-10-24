import os
import sys
import tempfile
import unittest

SIDECAR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sidecar")
sys.path.insert(0, SIDECAR)

import debrief_llm


class TestFindBundle(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.orig = debrief_llm.DEBRIEFS_DIR
        debrief_llm.DEBRIEFS_DIR = self.tmp

    def tearDown(self):
        debrief_llm.DEBRIEFS_DIR = self.orig

    def test_finds_bundle_md(self):
        path = os.path.join(self.tmp, "my-run.bundle.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write("bundle")
        self.assertEqual(debrief_llm.find_bundle("my-run"), path)

    def test_returns_none_when_missing(self):
        self.assertIsNone(debrief_llm.find_bundle("nope"))


if __name__ == "__main__":
    unittest.main()