import contextlib
import os
import re


def allocate_run_id(arm="adv"):
    """Next run id, based on run directories already present."""
    nums = []
    roots = (RUNTIME_DIR, os.path.join(BASE_DIR, "memory", "runs"))
    for root in roots:
        try:
            names = os.listdir(root)
        except OSError:
            continue
        for name in names:
            m = re.search(r"run-(\d+)", name)
            if m:
                nums.append(int(m.group(1)))
    n = (max(nums) + 1) if nums else 1
    return f"run-{n:03d}-{arm}"

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

MCP_URL: str = os.getenv("MCP_URL", "http://localhost:8787/")
POLL_INTERVAL: int = int(os.getenv("POLL_INTERVAL", "30"))
MCP_DELAY: float = float(os.getenv("MCP_DELAY", "0.15"))

BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- Storage layout ----------
# memory/  = durable knowledge (committed): lessons, wiki cache, docs, rubrics.
# runtime/ = disposable state, safe to delete: control/ plus one dir per run.
RUNTIME_DIR: str = os.path.join(BASE_DIR, "runtime")
CONTROL_DIR: str = os.path.join(RUNTIME_DIR, "control")

ACTIVE_RUN_FILE: str = os.path.join(CONTROL_DIR, "active.json")
MONITOR_PID_FILE: str = os.path.join(CONTROL_DIR, "monitor.pid")
MONITOR_LOG_FILE: str = os.path.join(CONTROL_DIR, "monitor.log")
MONITOR_ERR_LOG_FILE: str = os.path.join(CONTROL_DIR, "monitor.err.log")
MONITOR_STARTUP_LOCK: str = os.path.join(CONTROL_DIR, "monitor.startup.lock")
REFLEX_LOCK_FILE: str = os.path.join(CONTROL_DIR, "reflex.lock")
REFLEX_PAUSE_FILE: str = os.path.join(CONTROL_DIR, "reflex_pause.json")
HUMAN_ACTION_FILE: str = os.path.join(CONTROL_DIR, "last_human_action.json")
WATCHDOG_STOP_FILE: str = os.path.join(CONTROL_DIR, "monitor.watchdog.stop")
WATCHDOG_LOG_FILE: str = os.path.join(CONTROL_DIR, "monitor.watchdog.log")

LESSONS_FILE: str = os.path.join(BASE_DIR, "memory", "lessons.jsonl")
LESSONS_DB: str = os.path.join(BASE_DIR, "memory", "lessons.sqlite")
WIKI_DIR: str = os.path.join(BASE_DIR, "memory", "wiki")
WIKI_FACTS_FILE: str = os.path.join(BASE_DIR, "memory", "wiki_facts.yaml")
REFLEX_ACTIONS_FILE: str = os.path.join(BASE_DIR, "memory", "reflex_actions.yaml")

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
# Providers: openai | anthropic | ollama | nvidia
LLM_API_KEY: str | None = os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "ollama")  # openai | anthropic | ollama | nvidia
LLM_MODEL: str | None = os.getenv("LLM_MODEL")
OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# NVIDIA NIM (OpenAI-compatible API). Free tier; no local GPU needed.
NVIDIA_BASE_URL: str = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
NVIDIA_API_KEY: str | None = os.getenv("NVIDIA_API_KEY")
NVIDIA_MODEL: str = os.getenv("NVIDIA_MODEL", "nvidia/nemotron-3.5-super-vl-120b-a12b")

# Per-task model selection (ModelRegistry). Override via env vars.
LLM_MODEL_DAILY: str = os.getenv("LLM_MODEL_DAILY", "llama3.2:1b-instruct-q4_K_M")
LLM_MODEL_DEBRIEF: str = os.getenv("LLM_MODEL_DEBRIEF", "gemma4-e2b-rimworld")
LLM_MODEL_CHAT: str = os.getenv("LLM_MODEL_CHAT", "qwen3-rimworld")

# Run identity for advice logging.
# UNSET_RUN_ID is a sentinel meaning "the monitor has not allocated a run yet".
# It must never be used to name a snapshot/timelapse directory.
UNSET_RUN_ID: str = "current-run"
RUN_ID: str = os.getenv("RUN_ID", UNSET_RUN_ID)

# Daily in-game status message (say command) — comma-separated hours (0-23)
SAY_DAILY_HOURS: list[int] = [int(h.strip()) for h in os.getenv("SAY_DAILY_HOURS", "6,18").split(",") if h.strip().isdigit()]
# Use local LLM (Ollama) for daily advice instead of rule-based heuristics
SAY_DAILY_USE_LLM: bool = os.getenv("SAY_DAILY_USE_LLM", "0") == "1"

# Fixed run length for comparable runs (see RUN-PROTOCOL.md).
# Definition: the 1st day is Day 1, then 10 full days must complete after it.
# get_status.daysPassed counts elapsed days from 0 on the 1st day, so the run ends
# when daysPassed reaches 11 (1 + 10).
RUN_DAYS: int = int(os.getenv("RUN_DAYS", "11"))


# ---------- Run directories and id resolution ----------
#
# The monitor allocates a real id ("run-010-adv") at startup, writes it to
# runtime/control/active.json and patches ``smartrim.config.RUN_ID`` in its own
# process. Other processes (TUI, dashboard, CLI) resolve the active run from
# active.json instead of guessing. The UNSET_RUN_ID sentinel never names a dir.


def run_dir(run_id) -> str:
    """Absolute path of a run's directory: runtime/<run_id>."""
    return os.path.join(RUNTIME_DIR, str(run_id))


def run_subdir(name: str, run_id=None, create: bool = False) -> str | None:
    """A subdirectory inside a run. Returns None when no run id is known.

    Only creates the directory when ``create`` is True; reads must not have
    side effects.
    """
    rid = run_id or resolve_run_id()
    if not rid:
        return None
    path = os.path.join(run_dir(rid), name)
    if create:
        os.makedirs(path, exist_ok=True)
    return path


def run_file(name: str, run_id=None, create: bool = False) -> str | None:
    """A file at the root of a run directory. Returns None when no run is known."""
    rid = run_id or resolve_run_id()
    if not rid:
        return None
    path = os.path.join(run_dir(rid), name)
    if create:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def alerts_dir(run_id=None, create: bool = False):
    return run_subdir("alerts", run_id, create)


def snapshots_dir(run_id=None, create: bool = False):
    return run_subdir("snapshots", run_id, create)


def debriefs_dir(run_id=None, create: bool = False):
    return run_subdir("debriefs", run_id, create)


def candidates_dir(run_id=None, create: bool = False):
    return run_subdir("candidates", run_id, create)


def timelapse_dir(run_id=None, create: bool = False):
    return run_subdir("timelapse", run_id, create)


def advice_file(run_id=None, create: bool = False):
    return run_file("advice.jsonl", run_id, create)


def actions_file(run_id=None, create: bool = False):
    return run_file("actions.jsonl", run_id, create)


def quests_file(run_id=None, create: bool = False):
    return run_file("quests.json", run_id, create)


def _pid_alive(pid) -> bool:
    try:
        pid = int(pid)
    except (TypeError, ValueError):
        return False
    if pid <= 0:
        return False
    if os.name == "nt":  # os.kill(pid, 0) would terminate the process on Windows
        import ctypes

        handle = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)
        if not handle:
            return False
        try:
            code = ctypes.c_ulong()
            if not ctypes.windll.kernel32.GetExitCodeProcess(handle, ctypes.byref(code)):
                return False
            return code.value == 259  # STILL_ACTIVE
        finally:
            ctypes.windll.kernel32.CloseHandle(handle)
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def write_active_run(run_id, pid=None, arm=None, observe_only: bool = False) -> None:
    """Record the run the monitor is writing. Read by every other process."""
    if not run_id or run_id == UNSET_RUN_ID:
        return
    import json
    from datetime import datetime

    os.makedirs(CONTROL_DIR, exist_ok=True)
    payload = {
        "run_id": str(run_id),
        "pid": int(pid) if pid is not None else os.getpid(),
        "arm": arm,
        "observe_only": bool(observe_only),
        "started_at": datetime.now().isoformat(),
    }
    with open(ACTIVE_RUN_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def read_active_run() -> dict | None:
    """Active-run record, or None when absent/unreadable."""
    import json

    try:
        with open(ACTIVE_RUN_FILE, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) and data.get("run_id") else None
    except (OSError, json.JSONDecodeError):
        return None


def clear_active_run(pid=None) -> None:
    """Remove active.json, but only if it still describes ``pid`` (when given)."""
    data = read_active_run()
    if data is None:
        return
    if pid is not None and data.get("pid") not in (None, pid):
        return
    with contextlib.suppress(OSError):
        os.remove(ACTIVE_RUN_FILE)


def _dir_has_run_data(path: str) -> bool:
    for name, marker in (("snapshots", "day-"), ("timelapse", None)):
        sub = os.path.join(path, name)
        try:
            entries = os.listdir(sub)
        except OSError:
            continue
        if marker:
            if any(n.startswith(marker) and n.endswith(".json") for n in entries):
                return True
        elif any(n.lower().endswith(".png") for n in entries):
            return True
    return os.path.exists(os.path.join(path, "end.json"))


def latest_run_id() -> str | None:
    """Newest run with real data on disk; None on a fresh checkout.

    Run ids are allocated monotonically (run-NNN), so the highest number wins.
    Directory mtime is only a tie-breaker: Windows directory timestamps are not
    reliable enough to order runs on their own.
    """
    try:
        names = os.listdir(RUNTIME_DIR)
    except OSError:
        return None
    candidates: list[tuple[int, float, str]] = []
    for name in names:
        if name in ("control", "archive") or name == UNSET_RUN_ID:
            continue
        path = os.path.join(RUNTIME_DIR, name)
        if not os.path.isdir(path) or not _dir_has_run_data(path):
            continue
        try:
            mtime = os.path.getmtime(path)
        except OSError:
            continue
        match = re.match(r"run-(\d+)", name)
        candidates.append((int(match.group(1)) if match else -1, mtime, name))
    if not candidates:
        return None
    highest = max(c[0] for c in candidates)
    if highest >= 0:
        return max((c for c in candidates if c[0] == highest), key=lambda c: c[1])[2]
    return max(candidates, key=lambda c: c[1])[2]


def _live_run_from_active() -> str | None:
    data = read_active_run()
    if not data:
        return None
    pid = data.get("pid")
    if pid is not None and not _pid_alive(pid):
        return None
    rid = str(data.get("run_id") or "").strip()
    return rid if rid and rid != UNSET_RUN_ID else None


def resolve_run_id() -> str | None:
    """Concrete run id for this process, or None when no run is known.

    Order: explicit RUN_ID env var, an id the monitor patched into this module
    (same process), runtime/control/active.json (live monitor), then the newest
    run with data on disk.
    """
    env_id = os.getenv("RUN_ID", "").strip()
    if env_id and env_id != UNSET_RUN_ID:
        return env_id
    cfg_id = str(globals().get("RUN_ID") or "").strip()
    if cfg_id and cfg_id != UNSET_RUN_ID:
        return cfg_id
    active = _live_run_from_active()
    if active:
        return active
    return latest_run_id()
