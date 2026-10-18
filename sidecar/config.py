import os

MCP_URL = "http://localhost:8787/"
POLL_INTERVAL = 10  # seconds, real-time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALERTS_DIR = os.path.join(BASE_DIR, "memory", "alerts")
SNAPSHOTS_DIR = os.path.join(BASE_DIR, "memory", "snapshots")
DEBRIEFS_DIR = os.path.join(BASE_DIR, "memory", "debriefs")

HEALTH_THRESHOLD = 50
MOOD_THRESHOLD = 25

URGENT_KEYWORDS = ["fire", "predator", "raid", "attack", "downed", "berserk", "pyromaniac"]
