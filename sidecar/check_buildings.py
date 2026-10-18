import json, requests

def call(name, args=None):
    payload = {'jsonrpc':'2.0','id':1,'method':'tools/call','params':{'name':name,'arguments':args or {}}}
    resp = requests.post('http://localhost:8787/', json=payload, timeout=5)
    return json.loads(resp.json()['result']['content'][0]['text'])

# Try listing things with specific labels
for label in ['Wall', 'Bed', 'Door', 'Table', 'Stove', 'Bench', 'Lamp', 'Cooler']:
    r = call('list_things', {'label': f'*{label}*', 'limit': 5})
    matched = r.get('matched', 0)
    if matched > 0:
        print(f'  {label}: {matched} found')
        for t in r.get('things', [])[:3]:
            print(f"    {t.get('label')} at ({t.get('x')},{t.get('z')})")
    else:
        print(f'  {label}: 0')
print()
# Check if any buildings exist
r = call('list_things', {'category': 'building', 'limit': 5})
print(f"Total buildings: {r.get('matched', 0)}")
for t in r.get('things', [])[:10]:
    print(f"  {t.get('label')} ({t.get('def')}) at ({t.get('x')},{t.get('z')})")
