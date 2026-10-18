import json, requests

def call(name, args=None):
    payload = {'jsonrpc':'2.0','id':1,'method':'tools/call','params':{'name':name,'arguments':args or {}}}
    resp = requests.post('http://localhost:8787/', json=payload, timeout=5)
    return json.loads(resp.json()['result']['content'][0]['text'])

# Check for blueprints/frames
for cat in ['building', 'blueprint', 'frame', 'furniture', 'structure']:
    r = call('list_things', {'category': cat, 'limit': 5})
    print(f"  category={cat}: matched={r.get('matched', 0)}")
    for t in r.get('things', [])[:3]:
        print(f"    {t.get('label')} ({t.get('def')}) at ({t.get('x')},{t.get('z')})")

# Try inspecting a specific area
print()
r = call('get_area', {'minX': 100, 'minZ': 100, 'maxX': 140, 'maxZ': 140})
print('Area info:', json.dumps(r, indent=2)[:1000])
