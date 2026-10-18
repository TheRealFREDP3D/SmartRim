import json, requests

URL = "http://localhost:8787/"


def call(name, args=None):
    payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": name, "arguments": args or {}}}
    resp = requests.post(URL, json=payload, timeout=5)
    data = resp.json()
    text = data["result"]["content"][0]["text"]
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return {"text": text}


def main():
    cond = call("get_conditions")
    status = call("get_status")
    alerts = call("get_alerts")
    research = call("get_research")
    res = call("get_resources")

    day = cond.get("dayOfSeason", "?")
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

    message = (
        f"=== DAY {day} OVERVIEW (Hour {hour}) ===\n"
        f"Weather: {weather} | Temp: {temp}C | Season: {season}\n"
        f"Colonists: {names}\n"
        f"Alerts: {alerts_str}\n"
        f"Research: {research_str}\n"
        f"Resources: {res_str}\n"
    )

    result = call("say", {"text": message})
    print(f"Displayed: {result.get('shown', False)} ({result.get('chars', 0)} chars)")
    print(message)


if __name__ == "__main__":
    main()
