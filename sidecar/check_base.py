import json, requests

def call(name, args=None):
    payload = {'jsonrpc':'2.0','id':1,'method':'tools/call','params':{'name':name,'arguments':args or {}}}
    resp = requests.post('http://localhost:8787/', json=payload, timeout=5)
    return json.loads(resp.json()['result']['content'][0]['text'])

# Try get_area with summary to see what's in the base area
r = call('get_area', {'minX': 120, 'minZ': 160, 'maxX': 165, 'maxZ': 190, 'summary': True})
print('=== AREA SUMMARY ===')
print(json.dumps(r, indent=2)[:3000])
print()
# Try list_things with no category filter, just limit
r = call('list_things', {'limit': 10})
print('=== THINGS (no filter) ===')
print(json.dumps(r, indent=2)[:1000])
print()
# Try inspecting the area around the growing zone
r = call('list_things', {'x': 130, 'z': 175, 'radius': 20, 'limit': 20})
print('=== THINGS near (130,175) ===')
print(json.dumps(r, indent=2)[:1000])
