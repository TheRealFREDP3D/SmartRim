import json, requests, time
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


for i in range(20):
    r = call("edit_starting_pawn", {"action": "reroll", "index": 1})
    st = call("game_setup_status")
    pawns = st.get("pawns", [])
    edward = [p for p in pawns if p["index"] == 1][0]
    inc = edward.get("incapableOf") or "None"
    skills = {}
    for s in edward["skills"]:
        parts = s.split()
        if len(parts) > 1 and parts[1].isdigit():
            skills[parts[0]] = int(parts[1])
    med = skills.get("medical", 0)
    con = skills.get("construction", 0)
    pla = skills.get("plants", 0)
    intel = skills.get("intellectual", 0)
    traits = [t["label"] for t in edward.get("traits", [])]
    print(f"{i+1}. {edward['name']} | inc: {inc} | med:{med} con:{con} pla:{pla} intel:{intel} | traits: {traits}")
    if inc in (None, "None") and med >= 4 and con >= 3 and pla >= 3 and intel >= 4:
        print("   >>> ACCEPTABLE")
        break
