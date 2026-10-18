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

message = f"""=== DAY {day} SUMMARY (Hour {hour}) ===
Weather: {weather} | Temp: {temp}C
Colonists: {names}
Alerts: {alerts_str}

CRITICAL ACTIONS NEEDED:
1. MAD PEAHEN hostile (44 cells from Freya) - Draft and hunt it
2. LOW MEDICINE - Harvest wild healroot NOW. Tropical disease risk.
3. NO RESEARCH - Set project: Smithing (weapons) or Medicine (disease)
4. DEFENSES - First raid Days 8-15. Build sandbags before Day 8.
5. FREYA PREGNANT - Prepare medical bed. She'll need care later.
6. Visitor on map - Check who it is, trade or recruit.
7. Gift received from Kinship of Zone - Goodwill boost.

TROPICAL NOTES:
- Heat: 30.7C. Watch for heat stroke. Passive cooler active.
- Fog reduces visibility - good for hiding, bad for spotting predators.
- Mad animals common in tropical. Draft colonists near base.
"""

result = call('say', {'text': message})
print(f"Displayed: {result.get('shown', False)} ({result.get('chars', 0)} chars)")
print(message)
