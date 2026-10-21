import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

MCP_URL = os.getenv("MCP_URL", "http://localhost:8787/")
POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", "30"))
MCP_DELAY = float(os.getenv("MCP_DELAY", "0.15"))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALERTS_DIR = os.path.join(BASE_DIR, "memory", "alerts")
SNAPSHOTS_DIR = os.path.join(BASE_DIR, "memory", "snapshots")
DEBRIEFS_DIR = os.path.join(BASE_DIR, "memory", "debriefs")
CANDIDATES_DIR = os.path.join(BASE_DIR, "memory", "candidates")

HEALTH_THRESHOLD = int(os.getenv("HEALTH_THRESHOLD", "50"))
# Wiki base values for a normal colonist: minor break 35%, major 20%, extreme 5% (Mental_break page).
# Traits shift these; this is an approximation.
MOOD_MINOR_THRESHOLD = int(os.getenv("MOOD_MINOR_THRESHOLD", "35"))
MOOD_MAJOR_THRESHOLD = int(os.getenv("MOOD_MAJOR_THRESHOLD", "20"))
MOOD_EXTREME_THRESHOLD = int(os.getenv("MOOD_EXTREME_THRESHOLD", "5"))
MOOD_THRESHOLD = MOOD_MINOR_THRESHOLD

# (Threshold names standardized: MOOD_*_THRESHOLD / HEALTH_THRESHOLD)

URGENT_KEYWORDS = ["fire", "predator", "raid", "attack", "downed", "berserk", "pyromaniac"]

# Optional LLM provider for debrief generation (Phase 1 optional)
# Providers: openai | anthropic | ollama
LLM_API_KEY = os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")  # openai | anthropic | ollama
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Run identity for advice logging
RUN_ID = os.getenv("RUN_ID", "current-run")

# Fixed run length for comparable runs (see RUN-PROTOCOL.md).
# Definition: the 1st day is Day 1, then 10 full days must complete after it.
# get_status.daysPassed counts elapsed days from 0 on the 1st day, so the run ends
# when daysPassed reaches 11 (1 + 10).
RUN_DAYS = int(os.getenv("RUN_DAYS", "11"))
