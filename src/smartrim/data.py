"""Shared data loaders and helpers for SmartRim frontends (dashboard, TUI).

This module is intentionally free of any UI framework (no Streamlit, no Textual).
Both frontends import from here and apply their own caching/refresh strategy.
"""

from __future__ import annotations

import glob
import json
import os
from datetime import datetime
from typing import Any

from smartrim import config
from smartrim.config import (
    BASE_DIR,
    MCP_DELAY,
    MCP_URL,
    resolve_run_id,
)

try:
    from smartrim.mcp_client import McpClient, McpError
except ImportError:  # pragma: no cover - optional dependency
    McpClient = None  # type: ignore[assignment]
    McpError = Exception  # type: ignore[assignment]


# ---------- Pure helpers ----------


def mood_color(mood: Any) -> str:
    try:
        m = float(mood)
    except (TypeError, ValueError):
        return "#6b7280"
    if m < 5:
        return "#dc2626"
    if m < 20:
        return "#f59e0b"
    if m < 35:
        return "#eab308"
    return "#16a34a"


def reflex_enabled() -> bool:
    return os.getenv("REFLEX_KILL", "1") != "1"


def reflex_dry_run() -> bool:
    return os.getenv("REFLEX_DRY_RUN", "1") != "0"


def game_colonists(game_state: Any) -> list[dict[str, Any]]:
    if not game_state:
        return []
    bundled = (game_state.get("bundled") or {}).get("list_colonists") or {}
    return bundled.get("colonists", []) or []


def game_alerts(game_state: Any) -> tuple[list[Any], list[Any]]:
    if not game_state:
        return [], []
    bundled = (game_state.get("bundled") or {}).get("get_alerts") or {}
    active = bundled.get("activeAlerts", []) or []
    recent_msgs = bundled.get("recentMessages", []) or []
    return active, recent_msgs


# ---------- File loaders (uncached) ----------


def load_current_alerts() -> list[Any]:
    alert_dir = config.alerts_dir()
    if not alert_dir:
        return []
    alert_path = os.path.join(alert_dir, "current.json")
    if os.path.exists(alert_path):
        with open(alert_path, encoding="utf-8") as f:
            return json.load(f)
    return []


def load_dismissed_alerts() -> list[dict[str, Any]]:
    alert_dir = config.alerts_dir()
    if not alert_dir:
        return []
    dismissed_path = os.path.join(alert_dir, "dismissed.jsonl")
    dismissed: list[dict[str, Any]] = []
    if os.path.exists(dismissed_path):
        with open(dismissed_path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    dismissed.append(json.loads(line))
    return dismissed


def dismiss_alert(alert_message: str, alert_type: str) -> None:
    alert_dir = config.alerts_dir(create=True)
    if not alert_dir:
        return
    dismissed_path = os.path.join(alert_dir, "dismissed.jsonl")
    dismissed_entry = {
        "message": alert_message,
        "type": alert_type,
        "dismissed_at": datetime.now().isoformat(),
    }
    os.makedirs(os.path.dirname(dismissed_path), exist_ok=True)
    with open(dismissed_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(dismissed_entry) + "\n")


def _run_dirs() -> list[str]:
    """Every runtime run directory (control/ and archive/ excluded)."""
    try:
        names = os.listdir(config.RUNTIME_DIR)
    except OSError:
        return []
    return [
        os.path.join(config.RUNTIME_DIR, n)
        for n in sorted(names)
        if n not in ("control", "archive") and os.path.isdir(os.path.join(config.RUNTIME_DIR, n))
    ]


def load_all_advice() -> list[dict[str, Any]]:
    """Advice records from every run, newest run last."""
    advice_list: list[dict[str, Any]] = []
    for run_path in _run_dirs():
        advice_path = os.path.join(run_path, "advice.jsonl")
        if not os.path.exists(advice_path):
            continue
        with open(advice_path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    advice_list.append(json.loads(line))
    return advice_list


def load_lessons() -> list[dict[str, Any]]:
    lessons_path = config.LESSONS_FILE
    lessons_list: list[dict[str, Any]] = []
    if os.path.exists(lessons_path):
        with open(lessons_path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    lessons_list.append(json.loads(line))
    return lessons_list


def load_runs_metadata() -> list[dict[str, Any]]:
    """Run-end markers: runtime/<run_id>/end.json for every run."""
    runs: list[dict[str, Any]] = []
    for run_path in _run_dirs():
        marker = os.path.join(run_path, "end.json")
        if os.path.exists(marker):
            with open(marker, encoding="utf-8") as f:
                runs.append(json.load(f))
    return runs


def load_run_snapshots(run_id: str) -> list[dict[str, Any]]:
    snapshot_dir = config.snapshots_dir(run_id)
    snapshots: list[dict[str, Any]] = []
    if snapshot_dir and os.path.exists(snapshot_dir):
        for file in glob.glob(os.path.join(snapshot_dir, "day-*.json")):
            with open(file, encoding="utf-8") as f:
                snapshots.append(json.load(f))
        snapshots.sort(key=lambda x: str(x.get("day", "")))
    return snapshots


def load_debriefs() -> list[dict[str, Any]]:
    """Debrief markdown files from every run."""
    debriefs: list[dict[str, Any]] = []
    for run_path in _run_dirs():
        run_debriefs = os.path.join(run_path, "debriefs")
        if not os.path.exists(run_debriefs):
            continue
        for file in glob.glob(os.path.join(run_debriefs, "*.md")):
            with open(file, encoding="utf-8") as f:
                debriefs.append({"filename": os.path.basename(file), "content": f.read()})
    return debriefs


def load_reflex_actions(limit: int = 8) -> list[dict[str, Any]]:
    path = config.actions_file()
    out: list[dict[str, Any]] = []
    if path and os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    out.append(json.loads(line))
    out.reverse()
    return out[:limit]


# ---------- Live MCP ----------


def get_live_game_state() -> dict[str, Any] | None:
    if McpClient is None:
        return None
    try:
        client = McpClient(MCP_URL, delay=MCP_DELAY)
        status = client.call_tool("get_status")
        if status and not (isinstance(status, dict) and status.get("error")):
            return status
    except (McpError, ValueError, KeyError, TypeError, OSError, AttributeError):
        return None
    return None


def fetch_colonists() -> Any:
    if McpClient is None:
        return None
    try:
        client = McpClient(MCP_URL, delay=MCP_DELAY)
        return client.call_tool("list_colonists")
    except (McpError, ValueError, KeyError, TypeError, OSError, AttributeError):
        return None


def fetch_resources() -> Any:
    if McpClient is None:
        return None
    try:
        client = McpClient(MCP_URL, delay=MCP_DELAY)
        return client.call_tool("get_resources")
    except (McpError, ValueError, KeyError, TypeError, OSError, AttributeError):
        return None


__all__ = [
    "BASE_DIR",
    "MCP_DELAY",
    "MCP_URL",
    "dismiss_alert",
    "fetch_colonists",
    "fetch_resources",
    "game_alerts",
    "game_colonists",
    "get_live_game_state",
    "load_all_advice",
    "load_current_alerts",
    "load_debriefs",
    "load_dismissed_alerts",
    "load_lessons",
    "load_reflex_actions",
    "load_run_snapshots",
    "load_runs_metadata",
    "mood_color",
    "reflex_dry_run",
    "reflex_enabled",
    "resolve_run_id",
]
