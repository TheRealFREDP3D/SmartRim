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


TATEN = "Taten 'Tater' Stamm"
BRAN = "Bran 'Sawyher' Shawb"
BARAN = "Baran Gargatosh"

r = call("list_unmanaged_items", {"limit": 500, "confirm": True})
gear = {}
for t in r.get("items", []):
    if t["def"] in ("Gun_BoltActionRifle", "Gun_Revolver", "MeleeWeapon_Knife", "Apparel_FlakVest",
                    "Apparel_FlakPants", "Apparel_AdvancedHelmet", "Apparel_Duster",
                    "MedicineIndustrial", "ComponentIndustrial", "Silver", "Steel", "WoodLog",
                    "MealSurvivalPack"):
        gear[t["def"]] = t["id"]
        print(t["id"], t["def"], "at", t["x"], t["z"])

print()
print("Taten rifle:", call("manage_gear", {"name": TATEN, "op": "equip", "item": gear.get("Gun_BoltActionRifle", "")}).get("ok"))
print("Bran revolver:", call("manage_gear", {"name": BRAN, "op": "equip", "item": gear.get("Gun_Revolver", "")}).get("ok"))
print("Baran knife:", call("manage_gear", {"name": BARAN, "op": "equip", "item": gear.get("MeleeWeapon_Knife", "")}).get("ok"))
print("Taten vest:", call("manage_gear", {"name": TATEN, "op": "wear", "item": gear.get("Apparel_FlakVest", "")}).get("ok"))
print("Bran helmet:", call("manage_gear", {"name": BRAN, "op": "wear", "item": gear.get("Apparel_AdvancedHelmet", "")}).get("ok"))
print("Baran pants:", call("manage_gear", {"name": BARAN, "op": "wear", "item": gear.get("Apparel_FlakPants", "")}).get("ok"))
print("research:", call("set_research", {"project": "Smithing"}).get("label"))
