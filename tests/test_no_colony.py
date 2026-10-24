import os
import sys
import unittest

SIDECAR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sidecar")
sys.path.insert(0, SIDECAR)

from monitor import run_reflex_checks


class NoColonyClient:
    """Replays the main-menu response."""

    def __init__(self):
        self.calls = []

    def call_tool(self, name, arguments=None):
        self.calls.append(name)
        if name == "get_status":
            return {"loaded": False, "programState": "Entry"}
        return {}


class TestNoColony(unittest.TestCase):
    def test_main_menu_produces_no_alerts(self):
        client = NoColonyClient()
        alerts = run_reflex_checks(client)
        self.assertEqual(alerts, [])

    def test_main_menu_makes_no_extra_tool_calls(self):
        client = NoColonyClient()
        run_reflex_checks(client)
        self.assertEqual(client.calls, ["get_status"])


if __name__ == "__main__":
    unittest.main()
