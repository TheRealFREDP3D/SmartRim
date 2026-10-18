import json, requests

def call(name, args=None):
    payload = {'jsonrpc':'2.0','id':1,'method':'tools/call','params':{'name':name,'arguments':args or {}}}
    resp = requests.post('http://localhost:8787/', json=payload, timeout=5)
    return json.loads(resp.json()['result']['content'][0]['text'])

status = call('get_status')
print('=== COLONISTS ===')
for c in status['bundled']['list_colonists']['colonists']:
    print(f"  {c['name']} (ID:{c['id']}) HP:{c['health']}% Mood:{c['mood']}% Skills:{c.get('topSkills',[])}")
print()
print('=== CONDITIONS ===')
cond = call('get_conditions')
print(json.dumps(cond, indent=2)[:800])
print()
print('=== ALERTS ===')
alerts = call('get_alerts')
print(json.dumps(alerts, indent=2)[:800])
print()
print('=== RESOURCES ===')
res = call('get_resources')
print(json.dumps(res, indent=2)[:800])
