import json, requests
URL = "http://localhost:8787/"


def call(n, a=None):
    p = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": n, "arguments": a or {}}}
    r = requests.post(URL, json=p, timeout=30)
    d = r.json()
    t = d["result"]["content"][0]["text"]
    try:
        return json.loads(t)
    except Exception:
        return {"text": t}


st = call("game_setup_status")
for p in st["pawns"]:
    inc = p.get("incapableOf") or "None"
    traits = [t["label"] for t in p.get("traits", [])]
    print(f"{p['index']}. {p['name']} ({p['gender']}, {p['age']}) | incapable: {inc}")
    print(f"   skills: {p['skills']}")
    print(f"   traits: {traits}")
    print()
