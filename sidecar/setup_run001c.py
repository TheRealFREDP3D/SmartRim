import json, sys
sys.path.insert(0, r"C:\Users\fred\Desktop\RimWorld Consellor\RimAutonomous\sidecar")
from counselor import _call

TATEN = "Taten 'Tater' Stamm"
BRAN = "Bran 'Sawyher' Shawb"
BARAN = "Baran Gargatosh"

# Unforbid all
r = _call("list_unmanaged_items", {"limit": 500, "confirm": True})
ids = [t["id"] for t in r.get("items", []) if t.get("forbidden")]
print("forbidden:", len(ids))
for iid in ids:
    _call("do_thing_action", {"id": iid, "label": "Allow"})
print("unforbidden done")

# Equip
print("Taten rifle:", _call("manage_gear", {"name": TATEN, "op": "equip", "item": "Gun_BoltActionRifle15409"}).get("ok"))
print("Bran revolver:", _call("manage_gear", {"name": BRAN, "op": "equip", "item": "Gun_Revolver15410"}).get("ok"))
print("Baran knife:", _call("manage_gear", {"name": BARAN, "op": "equip", "item": "MeleeWeapon_Knife15411"}).get("ok"))
print("Taten vest:", _call("manage_gear", {"name": TATEN, "op": "wear", "item": "Apparel_FlakVest15413"}).get("ok"))
print("Bran helmet:", _call("manage_gear", {"name": BRAN, "op": "wear", "item": "Apparel_AdvancedHelmet15414"}).get("ok"))
print("Baran pants:", _call("manage_gear", {"name": BARAN, "op": "wear", "item": "Apparel_FlakPants15412"}).get("ok"))
print("research:", _call("set_research", {"project": "Smithing"}).get("label"))
