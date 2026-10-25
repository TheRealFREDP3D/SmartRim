"""Quest context for snapshots and the debrief bundle (bundle v3).

The debrief bundle used to see only colonists and resources, so a protection quest looked
like a random joiner and a raider-lit fire looked like a construction accident. This module
records what the game says about quests: name, state, accepter, and the description text
(cleaned of colour tags), which is where the actual objective lives ("keep him safe ...
until his shuttle can come pick him up").

A small registry keeps a description even after the quest is over, so a quest that starts
and ends between two daily snapshots is still explicable.
"""

import json
import os
import re
from datetime import datetime

try:
    from smartrim.config import BASE_DIR
except ImportError:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    from smartrim.mcp_client import McpError
except ImportError:
    McpError = Exception
DEFAULT_REGISTRY = os.path.join(BASE_DIR, "memory", "quests", "registry.json")

TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")

# States worth fetching a description for. Ended quests keep the description they had.
SKIP_DETAIL_STATES = ("Dismissed",)
MAX_DETAIL_FETCHES = 6


def clean_text(value):
    """Strip RimWorld colour tags and collapse whitespace."""
    text = TAG_RE.sub("", str(value or ""))
    return SPACE_RE.sub(" ", text).strip()


def load_registry(path=None):
    path = path or DEFAULT_REGISTRY
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        quests = data.get("quests")
        return quests if isinstance(quests, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_registry(registry, path=None):
    path = path or DEFAULT_REGISTRY
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"quests": registry}, f, indent=2, sort_keys=True)


def list_quests(client):
    """Ask the game for its quest list. Returns [] on any problem; never raises."""
    try:
        resp = client.call_tool("get_quest")
    except McpError:
        return []
    if not isinstance(resp, dict):
        return []
    quests = resp.get("quests")
    if quests is None:
        quests = [resp] if resp.get("name") else []
    out = []
    for q in quests:
        if isinstance(q, dict) and q.get("id") is not None:
            out.append({"id": q.get("id"), "name": clean_text(q.get("name")), "state": q.get("state")})
    return out


def _detail(client, quest_id):
    try:
        resp = client.call_tool("get_quest", {"id": quest_id})
    except McpError:
        return None
    if not isinstance(resp, dict) or resp.get("error"):
        return None
    return resp


def update(client, day_label=None, path=None):
    """Refresh the registry from the game. Returns the registry records seen in this pass."""
    registry = load_registry(path)
    seen = list_quests(client)
    day_label = day_label or "unknown day"
    fetched = 0

    for quest in seen:
        key = str(quest["id"])
        rec = registry.get(key) or {
            "id": quest["id"],
            "name": quest.get("name"),
            "description": None,
            "accepter": None,
            "states": [],
            "first_day": day_label,
            "last_day": day_label,
            "first_seen": datetime.now().isoformat(timespec="seconds"),
        }
        rec["name"] = quest.get("name") or rec.get("name")
        state = quest.get("state")
        if state and (not rec["states"] or rec["states"][-1] != state):
            rec["states"].append(state)
        rec["last_day"] = day_label
        rec["last_state"] = state

        needs_detail = rec.get("description") is None and state not in SKIP_DETAIL_STATES
        if needs_detail and fetched < MAX_DETAIL_FETCHES:
            detail = _detail(client, quest["id"])
            fetched += 1
            if detail:
                rec["description"] = clean_text(detail.get("description"))
                rec["accepter"] = detail.get("accepter") or rec.get("accepter")
        registry[key] = rec

    save_registry(registry, path)
    return [registry[str(q["id"])] for q in seen if str(q["id"]) in registry]


def summary_lines(records, max_chars=320):
    """Bullet lines for the bundle's metadata section."""
    if not records:
        return ["- quests: none reported by the game"]
    out = ["- quests seen this run:"]
    for rec in sorted(records, key=lambda r: r.get("id", 0)):
        states = " -> ".join(rec.get("states") or [rec.get("last_state") or "unknown"])
        head = f"  - [{rec.get('id')}] {rec.get('name')} - {states}"
        if rec.get("accepter"):
            head += f" - accepted by {rec['accepter']}"
        out.append(head)
        desc = rec.get("description")
        if desc:
            if len(desc) > max_chars:
                desc = desc[: max_chars - 1].rstrip() + "…"
            out.append(f"    {desc}")
    return out


def quests_from_snapshots(snapshots):
    """Union of quest records embedded in snapshots, keyed by id (last state wins)."""
    merged = {}
    for snap in snapshots or []:
        for rec in snap.get("quests") or []:
            if not isinstance(rec, dict) or rec.get("id") is None:
                continue
            key = str(rec["id"])
            prev = merged.get(key) or {}
            states = list(prev.get("states") or [])
            for state in rec.get("states") or ([rec.get("state")] if rec.get("state") else []):
                if state and (not states or states[-1] != state):
                    states.append(state)
            merged[key] = {
                "id": rec.get("id"),
                "name": rec.get("name") or prev.get("name"),
                "description": rec.get("description") or prev.get("description"),
                "accepter": rec.get("accepter") or prev.get("accepter"),
                "states": states,
            }
    return [merged[k] for k in sorted(merged, key=lambda x: int(x) if str(x).isdigit() else 0)]
