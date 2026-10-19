import json, requests, time, os
URL="http://localhost:8787/"
def call(n,a=None):
    p={'jsonrpc':'2.0','id':1,'method':'tools/call','params':{'name':n,'arguments':a or {}}}
    r=requests.post(URL,json=p,timeout=30)
    d=r.json(); t=d['result']['content'][0]['text']
    try: return json.loads(t)
    except: return {'text':t}

# Unforbid all forbidden items
r=call('list_unmanaged_items',{'limit':500,'confirm':True})
ids=[t['id'] for t in r['items'] if t.get('forbidden')]
print('forbidden:', len(ids))
for iid in ids:
    call('do_thing_action',{'id':iid,'label':'Allow'})
print('unforbidden:', len(ids))
# Survey area
a=call('get_area',{'minX':130,'minZ':110,'maxX':145,'maxZ':125,'summary':True})
print('terrain:', a.get('terrainSummary'))
tg=a.get('thingGroups',[])
print('trees:', sum(g['count'] for g in tg if 'Tree' in g['def']))
print('razor:', sum(g['count'] for g in tg if 'Razor' in g['def']))
# Rich soil
for x in range(120,160,10):
    for z in range(100,130,10):
        a=call('get_area',{'minX':x,'minZ':z,'maxX':x+9,'maxZ':z+9,'summary':True})
        ts=a.get('terrainSummary',{})
        if ts.get('SoilRich',0)>0:
            print('rich soil at x=%d-%d z=%d-%d: %d cells' % (x,x+9,z,z+9,ts.get('SoilRich')))
# Raid status
pawns=call('list_things',{'category':'pawn','limit':100})
hostiles=[t for t in pawns.get('things',[]) if t.get('hostile')]
print('hostiles:', len(hostiles))
for h in hostiles:
    print('  ', h.get('label'), h.get('x'), h.get('z'))
st=call('get_status')
print('alerts:', [a['label'] for a in st['bundled']['get_alerts'].get('activeAlerts',[])])