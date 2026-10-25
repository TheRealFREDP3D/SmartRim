import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

MCP_URL: str = os.getenv("MCP_URL", "http://localhost:8787/")
POLL_INTERVAL: int = int(os.getenv("POLL_INTERVAL", "30"))
MCP_DELAY: float = float(os.getenv("MCP_DELAY", "0.15"))

BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ALERTS_DIR: str = os.path.join(BASE_DIR, "memory", "alerts")
SNAPSHOTS_DIR: str = os.path.join(BASE_DIR, "memory", "snapshots")
DEBRIEFS_DIR: str = os.path.join(BASE_DIR, "memory", "debriefs")
CANDIDATES_DIR: str = os.path.join(BASE_DIR, "memory", "candidates")

HEALTH_THRESHOLD: int = int(os.getenv("HEALTH_THRESHOLD", "50"))
# Wiki base values for a normal colonist: minor break 35%, major 20%, extreme 5% (Mental_break page).
# Traits shift these; this is an approximation.
MOOD_MINOR_THRESHOLD: int = int(os.getenv("MOOD_MINOR_THRESHOLD", "35"))
MOOD_MAJOR_THRESHOLD: int = int(os.getenv("MOOD_MAJOR_THRESHOLD", "20"))
MOOD_EXTREME_THRESHOLD: int = int(os.getenv("MOOD_EXTREME_THRESHOLD", "5"))
MOOD_THRESHOLD: int = MOOD_MINOR_THRESHOLD

# (Threshold names standardized: MOOD_*_THRESHOLD / HEALTH_THRESHOLD)

URGENT_KEYWORDS: list[str] = ["fire", "predator", "raid", "attack", "downed", "berserk", "pyromaniac"]

# Optional LLM provider for debrief generation (Phase 1 optional)
# Providers: openai | anthropic | ollama
LLM_API_KEY: str | None = os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "ollama")  # openai | anthropic | ollama
LLM_MODEL: str | None = os.getenv("LLM_MODEL")
OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Per-task model selection (ModelRegistry). Override via env vars.
LLM_MODEL_DAILY: str = os.getenv("LLM_MODEL_DAILY", "llama3.2:1b-instruct-q4_K_M")
LLM_MODEL_DEBRIEF: str = os.getenv("LLM_MODEL_DEBRIEF", "gemma4-e2b-rimworld")
LLM_MODEL_CHAT: str = os.getenv("LLM_MODEL_CHAT", "qwen3-rimworld")

# Run identity for advice logging
RUN_ID: str = os.getenv("RUN_ID", "current-run")

# Daily in-game status message (say command) — comma-separated hours (0-23)
SAY_DAILY_HOURS: list[int] = [int(h.strip()) for h in os.getenv("SAY_DAILY_HOURS", "6,18").split(",") if h.strip().isdigit()]
# Use local LLM (Ollama) for daily advice instead of rule-based heuristics
SAY_DAILY_USE_LLM: bool = os.getenv("SAY_DAILY_USE_LLM", "0") == "1"

# Fixed run length for comparable runs (see RUN-PROTOCOL.md).
# Definition: the 1st day is Day 1, then 10 full days must complete after it.
# get_status.daysPassed counts elapsed days from 0 on the 1st day, so the run ends
# when daysPassed reaches 11 (1 + 10).
RUN_DAYS: int = int(os.getenv("RUN_DAYS", "11"))
