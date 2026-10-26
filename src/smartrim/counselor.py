"""SmartRim - Reusable tool library for game interaction via MCP."""

import json

import requests

from smartrim.mcp_client import McpClient, McpError

try:
    from smartrim.config import MCP_DELAY, MCP_URL
except ImportError:
    MCP_URL = "http://localhost:8787/"
    MCP_DELAY = 0.15
_client = McpClient(MCP_URL, delay=MCP_DELAY)


def _call(name, arguments=None):
    """Make an MCP tool call and return parsed result."""
    try:
        return _client.call_tool(name, arguments)
    except McpError as e:
        return {"error": str(e)}


# === Game State ===

def ping(timeout=1.5):
    """Check if the RimMolt MCP server is running and reachable.
    
    Returns (True, None) or (False, error_message).
    """
    return _client.ping(timeout=timeout)


def status():
    """Get full game status including bundled colonists and alerts."""
    return _call("get_status")


def conditions():
    """Get current game conditions (date, weather, temperature)."""
    return _call("get_conditions")


def colonists():
    """List all colonists with health, mood, jobs."""
    return _call("list_colonists")


def alerts():
    """Get active alerts and letters."""
    return _call("get_alerts")


def resources():
    """Get stockpiled resources and wealth."""
    return _call("get_resources")


def research():
    """Get research status."""
    return _call("get_research")


def zones():
    """List all zones."""
    return _call("list_zones")


def wildlife():
    """List wildlife on map."""
    return _call("list_wildlife")


def pawns(include_hostiles=False):
    """List pawns on map."""
    args = {}
    if include_hostiles:
        args["includeHostiles"] = True
    return _call("list_things", {"category": "pawn", **args})


# === Game Control ===

def pause():
    """Pause the game."""
    return _call("set_speed", {"action": "pause"})


def resume():
    """Resume the game (at last selected speed)."""
    return _call("set_speed", {"action": "unpause"})


def wait(hours=1):
    """Safely advance time by N game hours. Auto-pauses after.

    Retries once if a wait is already in progress (server-side stuck wait).
    """
    r = _call("wait_for_event", {"maxGameHours": hours, "pause": "always"})
    if isinstance(r, dict) and "already in progress" in str(r.get("error", "")).lower():
        _call("set_speed", {"action": "pause"})
        import time
        time.sleep(0.5)
        r = _call("wait_for_event", {"maxGameHours": hours, "pause": "always"})
    return r


def save(name=None):
    """Save the game."""
    args = {}
    if name:
        args["name"] = name
    return _call("save_game", args)


# === Building ===

def build(def_name, x, z, stuff=None, rotation=None):
    """Build a thing at coordinates."""
    args = {"def": def_name, "x": x, "z": z}
    if stuff:
        args["stuff"] = stuff
    if rotation is not None:
        args["rot"] = rotation
    return _call("build", args)


def build_wall(x1, z1, x2, z2, stuff="WoodLog"):
    """Build walls in a rectangle."""
    return _call("build", {
        "def": "Wall", "minX": x1, "minZ": z1,
        "maxX": x2, "maxZ": z2, "fill": "outline", "stuff": stuff,
    })


def inspect(x=None, z=None, thing_id=None):
    """Inspect a thing at coordinates or by ID."""
    if thing_id:
        return _call("inspect_thing", {"id": thing_id})
    return _call("inspect_thing", {"x": x, "z": z})


def area(x1, z1, x2, z2, summary=False, render=None):
    """Get area info."""
    args = {"minX": x1, "minZ": z1, "maxX": x2, "maxZ": z2}
    if summary:
        args["summary"] = True
    if render:
        args["render"] = render
    return _call("get_area", args)


# === Colonist Management ===

def set_priority(colonist, work_type, priority):
    """Set work priority for a colonist."""
    return _call("set_work_priority", {
        "name": colonist, "workType": work_type, "priority": priority,
    })


def draft(colonists):
    """Draft colonists (comma-separated names or list)."""
    if isinstance(colonists, list):
        colonists = ",".join(colonists)
    return _call("draft", {"action": "draft", "ids": colonists})


def undraft(colonists):
    """Undraft colonists."""
    if isinstance(colonists, list):
        colonists = ",".join(colonists)
    return _call("draft", {"action": "undraft", "ids": colonists})


def order(colonist, target_id, command=None):
    """Order a pawn. Omit command to list options."""
    args = {"id": colonist, "targetId": target_id}
    if command:
        args["command"] = command
    return _call("order_pawn", args)


def do_action(thing_id, label):
    """Execute a gizmo action on a thing."""
    return _call("do_thing_action", {"id": thing_id, "label": label})


def assign(colonist, building_id):
    """Assign a pawn to a building (bed, etc)."""
    return _call("assign_building", {"pawn": colonist, "building": building_id})


# === Research ===

def set_research(project):
    """Set research project."""
    return _call("set_research", {"project": project})


# === Zones ===

def designate(designator, x1, z1, x2=None, z2=None, x=None, z=None):
    """Apply a designator to an area or cell."""
    args = {"designator": designator}
    if x is not None and z is not None:
        args["x"] = x
        args["z"] = z
    else:
        args["minX"] = x1
        args["minZ"] = z1
        args["maxX"] = x2 if x2 else x1
        args["maxZ"] = z2 if z2 else z1
    return _call("designate", args)


def growing_zone(x1, z1, x2, z2, plant="Plant_Rice"):
    """Create a growing zone."""
    before = zones()
    before_ids = {z.get("id") for z in (before.get("zones", []) if isinstance(before, dict) else []) if z.get("kind") == "growing"}
    r = designate("Designator_ZoneAdd_Growing", x1, z1, x2, z2)
    zones_list = zones()
    growing = [z for z in (zones_list.get("zones", []) if isinstance(zones_list, dict) else []) if z.get("kind") == "growing" and z.get("id") not in before_ids]
    if not growing:
        growing = [z for z in (zones_list.get("zones", []) if isinstance(zones_list, dict) else []) if z.get("kind") == "growing"]
    if growing:
        _call("set_growing_zone", {"id": growing[0]["id"], "plant": plant})
    return r


def stockpile(x1, z1, x2, z2):
    """Create a stockpile zone."""
    return designate("Designator_ZoneAddStockpile_Resources", x1, z1, x2, z2)


# === Communication ===

def say(message):
    """Display a message in-game."""
    return _call("say", {"text": message})


def read_letter(letter_id):
    """Read a letter."""
    return _call("read_letter", {"id": letter_id})


# === Utility ===

def screenshot():
    """Take a screenshot."""
    return _call("screenshot", {})


def things(def_name=None, category=None, label=None, limit=20):
    """List things on map."""
    args = {"limit": limit}
    if def_name:
        args["def"] = def_name
    if category:
        args["category"] = category
    if label:
        args["label"] = label
    return _call("list_things", args)


def get_map():
    """Get map overview."""
    return _call("get_map", {})


def power():
    """Get power grid status."""
    return _call("list_power_grids", {})


def world():
    """Get world info."""
    return _call("get_world", {})


# === Consolidated tools (from scratchpad scripts) ===

def unforbid_all():
    """Unforbid every forbidden item on the map. Returns count."""
    r = _call("list_unmanaged_items", {"limit": 500, "confirm": True})
    ids = [t["id"] for t in (r.get("items", []) if isinstance(r, dict) else []) if t.get("forbidden")]
    done = 0
    for iid in ids:
        _call("do_thing_action", {"id": iid, "label": "Allow"})
        done += 1
    return {"unforbidden": done, "total_found": len(ids)}


def survey(x1, z1, x2, z2):
    """Survey an area: terrain, tree count, razor wire count."""
    a = _call("get_area", {"minX": x1, "minZ": z1, "maxX": x2, "maxZ": z2, "summary": True})
    tg = a.get("thingGroups", []) if isinstance(a, dict) else []
    trees = sum(g.get("count", 0) for g in tg if "Tree" in g.get("def", ""))
    razor = sum(g.get("count", 0) for g in tg if "Razor" in g.get("def", ""))
    return {
        "terrain": a.get("terrainSummary", {}),
        "trees": trees,
        "razor_wire": razor,
        "thing_groups": tg,
    }


def find_rich_soil():
    """Find 10x10 areas containing rich soil. Returns list of (x,z,cells)."""
    results = []
    for x in range(0, 250, 10):
        for z in range(0, 250, 10):
            a = _call("get_area", {"minX": x, "minZ": z, "maxX": x + 9, "maxZ": z + 9, "summary": True})
            ts = a.get("terrainSummary", {}) if isinstance(a, dict) else {}
            if ts.get("SoilRich", 0) > 0:
                results.append({"x": x, "z": z, "rich_cells": ts.get("SoilRich", 0)})
    return results


def chop_trees(x1, z1, x2, z2):
    """Designate trees in an area for harvesting."""
    return _call("designate", {"designator": "Designator_PlantsHarvestWood", "minX": x1, "minZ": z1, "maxX": x2, "maxZ": z2})


def raid_status():
    """Check for hostiles and raid alerts."""
    pawns = _call("list_things", {"category": "pawn", "limit": 200})
    hostiles = [t for t in (pawns.get("things", []) if isinstance(pawns, dict) else []) if t.get("hostile")]
    alerts = _call("get_alerts")
    active = alerts.get("activeAlerts", []) if isinstance(alerts, dict) else []
    raid_alerts = [a for a in active if any(k in a.get("label", "").lower() for k in ("raid", "enemy", "attack"))]
    return {
        "hostile_count": len(hostiles),
        "hostiles": [{"label": h.get("label"), "x": h.get("x"), "z": h.get("z"), "downed": h.get("downed")} for h in hostiles],
        "raid_alerts": raid_alerts,
    }


def equip(colonist, weapon=None, apparel=None):
    """Equip a weapon and/or apparel on a colonist."""
    results = {}
    if weapon:
        results["weapon"] = _call("manage_gear", {"name": colonist, "op": "equip", "item": weapon})
    if apparel:
        for item in (apparel if isinstance(apparel, list) else [apparel]):
            results[f"wear_{item}"] = _call("manage_gear", {"name": colonist, "op": "wear", "item": item})
    return results


def find_corpses():
    """Find unburied human corpses on the map."""
    # Use inspect on a grid is too slow; rely on list_things with category
    r = _call("list_things", {"category": "item", "limit": 200})
    things = r.get("things", []) if isinstance(r, dict) else []
    return [t for t in things if "corpse" in str(t.get("label", "")).lower() or "corpse" in str(t.get("def", "")).lower()]


def scan_area(x1, z1, x2, z2):
    """Scan a grid of cells, returning non-terrain items (weapons, gear, etc.)."""
    results = []
    for z in range(z1, z2 + 1):
        for x in range(x1, x2 + 1):
            r = _call("inspect_thing", {"x": x, "z": z})
            lab = r.get("label") or ""
            if lab and "Plant" not in lab and "Chunk" not in lab and "Grass" not in lab and "Rubble" not in lab:
                results.append({"x": x, "z": z, "label": lab, "id": r.get("id")})
    return results


# === Compound Operations ===

def _safe(fn, *a, **kw):
    try:
        return fn(*a, **kw)
    except (McpError, requests.RequestException, ValueError, KeyError, TypeError, OSError, AttributeError) as e:
        return {"error": str(e)}


def game_state():
    """Get a comprehensive game state summary."""
    s = _safe(status)
    c = _safe(conditions)
    a = _safe(alerts)
    r = _safe(resources)
    res = _safe(research)
    col = _safe(colonists)

    def g(d, *keys, default=None):
        cur = d
        for k in keys:
            if not isinstance(cur, dict):
                return default
            cur = cur.get(k, default)
            if cur is None:
                return default
        return cur

    return {
        "colony": g(s, "colonyName"),
        "day": g(c, "date"),
        "hour": g(c, "hour"),
        "season": g(c, "seasonLabel"),
        "temp": g(c, "temperature", "outdoorC"),
        "weather": g(c, "weather", "current"),
        "colonists": (col.get("colonists", []) if isinstance(col, dict) else []),
        "alerts": (a.get("activeAlerts", []) if isinstance(a, dict) else []),
        "letters": (a.get("activeLetters", []) if isinstance(a, dict) else []),
        "resources": (r.get("resources", []) if isinstance(r, dict) else []),
        "wealth": g(r, "wealthTotal"),
        "research": (res.get("current", {}).get("label") if isinstance(res, dict) and res.get("current") else None),
        "research_progress": (res.get("current", {}).get("progressPercent", 0) if isinstance(res, dict) and res.get("current") else 0),
    }


def daily_summary():
    """Generate and display a daily summary in-game."""
    gs = game_state()
    colonists_str = ", ".join(
        f"{c.get('name', '?')} (HP:{c.get('health', '?')}% Mood:{c.get('mood', '?')}%)" for c in gs["colonists"]
    )
    alerts_str = ", ".join(a.get("label", str(a)) for a in gs["alerts"]) or "None"
    res_str = ", ".join(f"{r.get('label', '?')}:{r.get('count', '?')}" for r in gs["resources"])

    message = (
        f"=== DAY {gs['day']} (Hour {gs['hour']}) ===\n"
        f"Weather: {gs['weather']} | Temp: {gs['temp']}C\n"
        f"Colonists: {colonists_str}\n"
        f"Alerts: {alerts_str}\n"
        f"Research: {gs['research']} ({gs['research_progress']}%)\n"
        f"Resources: {res_str}\n"
    )
    say(message)
    return gs


if __name__ == "__main__":
    # Quick test
    gs = game_state()
    print(json.dumps(gs, indent=2, default=str)[:2000])
