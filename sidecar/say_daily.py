"""Daily in-game status message via the say command.

Can be run standalone:
    python sidecar/say_daily.py            # auto-detect slot from current hour
    python sidecar/say_daily.py --slot morning
    python sidecar/say_daily.py --slot evening
    python sidecar/say_daily.py --hour 6

Or imported by the monitor for automatic twice-daily display.
"""
import argparse
import json
import os
import sys

# Allow running from repo root or sidecar dir
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from config import MCP_DELAY, MCP_URL
except ImportError:
    MCP_URL = os.getenv("MCP_URL", "http://localhost:8787/")
    MCP_DELAY = 0.15

URL = os.getenv("MCP_URL", MCP_URL)

# Reuse the shared MCP client (requests is a hard dependency).
from mcp_client import McpClient

_client = McpClient(URL, delay=MCP_DELAY)


def call(name, args=None):
    return _client.call_tool(name, args)


def build_llm_advice(status, alerts, research, resources, conditions):
    """Generate advice via local LLM instead of rule-based heuristics.

    Returns a string of advice, or None if LLM is unavailable.
    """
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from llm import generate
        ctx = {
            "colonists": [{"name": c.get("name"), "hp": c.get("health"), "mood": c.get("mood"), "job": c.get("job")} for c in status.get("bundled", {}).get("list_colonists", {}).get("colonists", [])],
            "alerts": [a.get("label") for a in (alerts.get("activeAlerts", []) if isinstance(alerts, dict) else [])],
            "research": research.get("current", {}).get("label") if isinstance(research, dict) and research.get("current") else None,
            "resources": {r.get("label"): r.get("count") for r in (resources.get("resources", []) if isinstance(resources, dict) else [])},
            "weather": conditions.get("weather", {}).get("current") if isinstance(conditions.get("weather"), dict) else None,
            "temp": conditions.get("temperature", {}).get("outdoorC") if isinstance(conditions.get("temperature"), dict) else None,
            "day": conditions.get("date"),
        }
        prompt = f"Colony state: {json.dumps(ctx)}\nGive 2-3 specific actionable advice items for this colony right now."
        system = "You are a RimWorld colony advisor. Be concise (max 3 sentences). Focus on immediate threats and opportunities."
        return generate(prompt, provider="ollama", model="gemma4-e2b-rimworld", system=system, temperature=0.4, num_ctx=4096)
    except Exception:
        return None


def build_message(slot="auto", use_llm=False):
    cond = call("get_conditions")
    status = call("get_status")
    alerts = call("get_alerts")
    research = call("get_research")
    res = call("get_resources")

    day = cond.get("date", f"Day {cond.get('dayOfSeason', '?')}")
    hour = cond.get("hour", "?")
    temp = cond.get("temperature", {}).get("outdoorC", "?") if isinstance(cond.get("temperature"), dict) else "?"
    weather = cond.get("weather", {}).get("current", "?") if isinstance(cond.get("weather"), dict) else "?"
    season = cond.get("seasonLabel", "?")

    colonists = []
    if isinstance(status, dict):
        colonists = status.get("bundled", {}).get("list_colonists", {}).get("colonists", [])
    if not colonists:
        cr = call("list_colonists")
        if isinstance(cr, dict):
            colonists = cr.get("colonists", [])
    names = ", ".join(f"{c.get('name')} (HP:{c.get('health')}% Mood:{c.get('mood')}%)" for c in colonists)

    alert_list = [a.get("label") for a in (alerts.get("activeAlerts", []) if isinstance(alerts, dict) else [])]
    alerts_str = ", ".join(alert_list) if alert_list else "None"

    cur = research.get("current") if isinstance(research, dict) else None
    research_str = f"{cur.get('label', 'NONE')} ({cur.get('progressPercent', 0)}%)" if cur else "NONE"

    res_str = ", ".join(f"{r.get('label')}:{r.get('count')}" for r in (res.get("resources", []) if isinstance(res, dict) else []))

    # Determine slot label
    if slot == "auto":
        h = hour if isinstance(hour, int) else 0
        slot = "morning" if h < 12 else "evening"

    # Advice: LLM or rule-based
    if use_llm:
        llm_advice = build_llm_advice(status, alerts, research, res, cond)
        if llm_advice:
            advice_str = llm_advice
        else:
            use_llm = False  # fall back to rules

    if not use_llm:
        advice_lines = []
        if slot == "morning":
            advice_lines.append("Morning priorities: check mood/health, assign work, harvest/grow food, build/repair.")
        else:
            advice_lines.append("Evening priorities: check defenses, ensure beds assigned, review alerts, plan tomorrow.")

        low_labels = [a.lower() for a in alert_list]
        if any("food" in a or "low food" in a for a in low_labels):
            advice_lines.append("FOOD: Check ground items — resource readout misses unstockpiled food.")
        if any("defens" in a or "raid" in a for a in low_labels):
            advice_lines.append("DEFENSE: Build sandbags, draft fighters, focus-fire raiders.")
        if any("bed" in a for a in low_labels):
            advice_lines.append("BEDS: Assign colonists to beds; sleeping on ground = mood penalty.")
        if any("batter" in a for a in low_labels):
            advice_lines.append("POWER: Build batteries to store solar/wind energy.")
        if any("pen" in a for a in low_labels):
            advice_lines.append("PEN: Enclose animal pen with fence/wall to stop roamers.")
        if any("medical" in a for a in low_labels):
            advice_lines.append("MEDICAL: Tend wounded, check medicine stock.")

        low_mood = [c for c in colonists if (c.get("mood") or 100) < 35]
        if low_mood:
            advice_lines.append(f"MOOD: {', '.join(c.get('name') for c in low_mood)} below 35% — check needs, food, rest, recreation.")

        hurt = [c for c in colonists if (c.get("health") or 100) < 100]
        if hurt:
            advice_lines.append(f"HEALTH: {', '.join(c.get('name') for c in hurt)} injured — tend wounds.")

        advice_str = " | ".join(advice_lines)

    message = (
        f"=== {slot.upper()} STATUS (Day {day}, Hour {hour}) ===\n"
        f"Weather: {weather} | Temp: {temp}C | Season: {season}\n"
        f"Colonists: {names}\n"
        f"Alerts: {alerts_str}\n"
        f"Research: {research_str}\n"
        f"Resources: {res_str}\n"
        f"Advice: {advice_str}\n"
    )
    return message, slot


def say_message(text):
    result = call("say", {"text": text})
    return result


def main():
    parser = argparse.ArgumentParser(description="Daily in-game status + advice via say command")
    parser.add_argument("--slot", choices=["morning", "evening", "auto"], default="auto", help="Time slot")
    parser.add_argument("--hour", type=int, default=None, help="Override hour for slot detection")
    parser.add_argument("--llm", action="store_true", help="Use LLM for advice (slower, richer)")
    args = parser.parse_args()

    slot = args.slot
    if args.hour is not None:
        slot = "morning" if args.hour < 12 else "evening"

    message, slot = build_message(slot, use_llm=args.llm)
    result = say_message(message)
    print(f"Slot: {slot}")
    print(f"Displayed: {result.get('shown', False)} ({result.get('chars', 0)} chars)")
    print(message)


if __name__ == "__main__":
    main()
