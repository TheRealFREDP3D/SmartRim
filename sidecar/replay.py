"""Replay harness for Layer 2 reflex actions.

Usage: python sidecar/replay.py <run_id> [snapshots_root]
"""

import os
import sys

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from smartrim.replay import main

if __name__ == "__main__":
    sys.exit(main())
