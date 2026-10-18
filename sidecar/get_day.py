import json, requests

def call(name, args=None):
    payload = {'jsonrpc':'2.0','id':1,'method':'tools/call','params':{'name':name,'arguments':args or {}}}
    resp = requests.post('http://localhost:8787/', json=payload, timeout=5)
    return json.loads(resp.json()['result']['content'][0]['text'])

cond = call('get_conditions')
print(f"Day {cond.get('dayOfSeason', '?')} of {cond.get('seasonLabel', '?')}, Hour {cond.get('hour', '?')}")
print(f"Date: {cond.get('date', '?')}")
print(f"Temp: {cond.get('temperature', {}).get('outdoorC', '?')}C")
print(f"Weather: {cond.get('weather', {}).get('current', '?')}")
status = call('get_status')
print(f"Colonists: {status.get('colonistCount', '?')}")
for c in status['bundled']['list_colonists']['colonists']:
    print(f"  {c['name']}: HP {c['health']}% Mood {c['mood']}%")
alerts = call('get_alerts')
for a in alerts.get('activeAlerts', []):
    print(f"  ALERT: {a['label']}")
