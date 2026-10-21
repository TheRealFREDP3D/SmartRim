import json, sys
sys.path.insert(0, r"C:\Users\fred\Desktop\RimWorld Consellor\RimAutonomous\sidecar")
from counselor import _call

TATEN = "Taten 'Tater' Stamm"
BRAN = "Bran 'Sawyher' Shawb"
BARAN = "Baran Gargatosh"

print("Taten rifle:", _call("manage_gear", {"name": TATEN, "op": "equip", "item": "Gun_BoltActionRifle15409"}).get("ok"))
print("Bran revolver:", _call("manage_gear", {"name": BRAN, "op": "equip", "item": "Gun_Revolver15410"}).get("ok"))
print("Baran knife:", _call("manage_gear", {"name": BARAN, "op": "equip", "item": "MeleeWeapon_Knife15411"}).get("ok"))
print("research:", _call("set_research", {"project": "Smithing"}).get("label"))
st = _call("get_status")
for c in st["bundled"]["list_colonists"]["colonists"]:
    g = _call("get_pawn", {"id": c["id"]})
    print(c["name"], "weapon=", g.get("weapon"))
