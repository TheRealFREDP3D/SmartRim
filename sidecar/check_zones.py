import json, requests

def call(name, args=None):
    payload = {'jsonrpc':'2.0','id':1,'method':'tools/call','params':{'name':name,'arguments':args or {}}}
    resp = requests.post('http://localhost:8787/', json=payload, timeout=5)
    return json.loads(resp.json()['result']['content'][0]['text'])

z = call('list_zones')
print('=== ZONES ===')
for zone in z.get('zones', []):
    print(f"  {zone['label']} ({zone['kind']}): {zone['cells']} cells, plant={zone.get('plant','N/A')}")
print()
print('=== BUILDINGS ===')
b = call('list_things', {'category':'building','limit':40})
for t in b.get('things', []):
    print(f"  {t['label']} at ({t['x']},{t['z']})")
print()
print('=== POWER ===')
p = call('list_power_grids')
print(json.dumps(p, indent=2)[:500])
