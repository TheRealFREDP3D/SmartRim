import json, requests

def call(name, args=None):
    payload = {'jsonrpc':'2.0','id':1,'method':'tools/call','params':{'name':name,'arguments':args or {}}}
    resp = requests.post('http://localhost:8787/', json=payload, timeout=5)
    return json.loads(resp.json()['result']['content'][0]['text'])

# Get full area summary of base area
r = call('get_area', {'minX': 120, 'minZ': 160, 'maxX': 165, 'maxZ': 190, 'summary': True})
groups = r.get('thingGroups', [])
# Print all non-plant, non-terrain groups
for g in groups:
    defn = g['def']
    if not defn.startswith('Plant_') and not defn.startswith('RG_') and not defn.startswith('Chunk') and not defn.startswith('Filth') and defn not in ('WoodLog',):
        print(f"  {g['label']} ({defn}): {g['count']}")
print()
# Also check weapon/gear
r = call('list_colonists')
for c in r.get('colonists', []):
    print(f"  {c['name']}: gear={c.get('gear', 'N/A')}")
