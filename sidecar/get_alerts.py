import json, requests

def call(name, args=None):
    payload = {'jsonrpc':'2.0','id':1,'method':'tools/call','params':{'name':name,'arguments':args or {}}}
    resp = requests.post('http://localhost:8787/', json=payload, timeout=5)
    return json.loads(resp.json()['result']['content'][0]['text'])

alerts = call('get_alerts')
print('=== ACTIVE ALERTS ===')
for a in alerts.get('activeAlerts', []):
    print(f"  ! {a['label']} ({a.get('priority', '?')})")
    print(f"    {a.get('explanation', '')[:200]}")
print()
print('=== ACTIVE LETTERS ===')
for l in alerts.get('activeLetters', []):
    print(f"  * {l['label']} (id={l['id']}, type={l['type']})")
print()
# Get research status
r = call('get_research')
print('=== RESEARCH ===')
current = r.get('current')
print(f"  Current: {current.get('label', 'NONE') if current else 'NONE'}")
print(f"  Completed: {r.get('completedCount', 0)} / {r.get('totalCount', 0)}")
print(f"  Available: {r.get('availableCount', 0)}")
print()
# Get wildlife
w = call('list_wildlife')
print('=== WILDLIFE (first 10) ===')
for a in w.get('animals', [])[:10]:
    print(f"  {a.get('kind')} at ({a.get('x')},{a.get('z')})")
