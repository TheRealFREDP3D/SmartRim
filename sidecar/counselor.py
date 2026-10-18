"""RimWorld Counselor - Reusable tool library for game interaction via MCP."""

import json
import requests
import os
import sys

MCP_URL = "http://localhost:8787/"
_id_counter = 0


def _call(name, arguments=None):
    """Make an MCP tool call and return parsed result."""
    global _id_counter
    _id_counter += 1
    payload = {
        "jsonrpc": "2.0",
        "id": _id_counter,
        "method": "tools/call",
        "params": {"name": name, "arguments": arguments or {}},
    }
    try:
        resp = requests.post(MCP_URL, json=payload, timeout=10)
        result = resp.json()
        if "result" in result and "content" in result["result"]:
            text = result["result"]["content"][0]["text"]
            try:
                return json.loads(text)
            except (json.JSONDecodeError, TypeError):
                return {"text": text}
        return result
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# === Game State ===

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
    """Safely advance time by N game hours. Auto-pauses after."""
    return _call("wait_for_event", {"maxGameHours": hours, "pause": "always"})


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
    r = designate("Designator_ZoneAdd_Growing", x1, z1, x2, z2)
    # Set plant type
    zones_list = zones()
    growing = [z for z in zones_list.get("zones", []) if z.get("kind") == "growing"]
    if growing:
        last = growing[-1]
        _call("set_growing_zone", {"id": last["id"], "plant": plant})
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


# === Compound Operations ===

def game_state():
    """Get a comprehensive game state summary."""
    s = status()
    c = conditions()
    a = alerts()
    r = resources()
    res = research()
    col = colonists()

    return {
        "colony": s.get("colonyName"),
        "day": c.get("date"),
        "hour": c.get("hour"),
        "season": c.get("seasonLabel"),
        "temp": c.get("temperature", {}).get("outdoorC"),
        "weather": c.get("weather", {}).get("current"),
        "colonists": col.get("colonists", []),
        "alerts": a.get("activeAlerts", []),
        "letters": a.get("activeLetters", []),
        "resources": r.get("resources", []),
        "wealth": r.get("wealthTotal"),
        "research": res.get("current", {}).get("label") if res.get("current") else None,
        "research_progress": res.get("current", {}).get("progressPercent", 0) if res.get("current") else 0,
    }


def daily_summary():
    """Generate and display a daily summary in-game."""
    gs = game_state()
    colonists_str = ", ".join(
        f"{c['name']} (HP:{c['health']}% Mood:{c['mood']}%)" for c in gs["colonists"]
    )
    alerts_str = ", ".join(a["label"] for a in gs["alerts"]) or "None"
    res_str = ", ".join(f"{r['label']}:{r['count']}" for r in gs["resources"])

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
