import json, requests

def call(name, args=None):
    payload = {'jsonrpc':'2.0','id':1,'method':'tools/call','params':{'name':name,'arguments':args or {}}}
    resp = requests.post('http://localhost:8787/', json=payload, timeout=5)
    return json.loads(resp.json()['result']['content'][0]['text'])

cond = call('get_conditions')
status = call('get_status')
alerts = call('get_alerts')

day = cond.get('dayOfSeason', '?')
hour = cond.get('hour', '?')
temp = cond.get('temperature', {}).get('outdoorC', '?')
weather = cond.get('weather', {}).get('current', '?')

colonists = status['bundled']['list_colonists']['colonists']
names = ', '.join(f"{c['name']} (HP:{c['health']}% Mood:{c['mood']}%)" for c in colonists)

alert_list = [a['label'] for a in alerts.get('activeAlerts', [])]
alerts_str = ', '.join(alert_list) if alert_list else 'None'

message = f"""=== DAY {day} SUMMARY ===
Weather: {weather} | Temp: {temp}C | Hour: {hour}
Colonists: {names}
Alerts: {alerts_str}

ADVICE:
- Finish wall expansion (53 blueprints remaining)
- Build fueled stove + stonecutter table (blueprints ready)
- Plant cotton for sandbags (cloth needed for defense)
- Harvest wild healroot for medicine (tropical disease risk)
- Set work priorities: Creed=Construction/Plants/Research, Zack=Cooking/Research, Freya=Shooting/Crafting
- First raid window: Days 8-15. Build sandbags before Day 8.
- Rice growing zone: sow when ready (127 cells, rich soil)
"""

result = call('say', {'text': message})
print(f"Message displayed: {result.get('shown', False)} ({result.get('chars', 0)} chars)")
print(message)
