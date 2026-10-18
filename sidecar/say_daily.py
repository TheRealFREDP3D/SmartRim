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
season = cond.get('seasonLabel', '?')

colonists = status['bundled']['list_colonists']['colonists']
names = ', '.join(f"{c['name']} (HP:{c['health']}% Mood:{c['mood']}%)" for c in colonists)

alert_list = [a['label'] for a in alerts.get('activeAlerts', [])]
alerts_str = ', '.join(alert_list) if alert_list else 'None'

r = call('get_research')
cur = r.get('current')

r2 = call('get_resources')
res_str = ', '.join(f"{res['label']}:{res['count']}" for res in r2.get('resources', []))

# Check cotton maturity
cotton_growth = 'N/A'
for x in range(140, 165, 5):
    for z in range(96, 120, 5):
        r3 = call('inspect_thing', {'x': x, 'z': z})
        if 'cotton' in r3.get('label', '').lower():
            cotton_growth = r3.get('growth', 'N/A')
            break
    if cotton_growth != 'N/A':
        break

# Check for raid threats
threat = status.get('_threatWarning', {})
threat_str = f"Hostiles: {threat.get('count', 0)}" if threat else "No hostiles nearby"

message = f"""=== DAY {day} OVERVIEW (Hour {hour}) ===
Weather: {weather} | Temp: {temp}C | Season: {season}
Colonists: {names}
Alerts: {alerts_str}
Threat: {threat_str}
Research: {cur.get('label', 'NONE') if cur else 'NONE'} ({cur.get('progressPercent', 0) if cur else 0}%)
Resources: {res_str}
Cotton growth: {cotton_growth}%

STATUS:
- Day 9 = Raid window Day 2 (Days 8-15)
- No sandbags yet (cotton at {cotton_growth}% - need 100%)
- Smithing at 25% (Freya 5x buff active)
- 13 packaged meals (emergency food)
- 0 simple meals (need cooking)
- Freya pregnant - HP 100%, resting

PRIORITY ACTIONS:
1. Wait for cotton to mature -> harvest -> cloth -> sandbags
2. Continue Smithing research (Freya's buff)
3. Get Zack to cook simple meals from rice
4. Monitor for raid (could come any day 8-15)
5. Ambrosia sprout - sell to traders
6. Mechanoid Signal quest - evaluate
"""

result = call('say', {'text': message})
print(f"Displayed: {result.get('shown', False)} ({result.get('chars', 0)} chars)")
print(message)
