path = r"C:\Users\fred\Desktop\SmartRim\sidecar\situation.py"
s = open(path, encoding="utf-8").read()

old = '''        if cat == "game_alert":
            label = a.get("label", "").lower() if "label" in a else a.get("message", "").lower()
            if any(k in label for k in ("raid", "attack", "enemy", "predator", "fire")):
                is_crisis = True
    if is_crisis:
        return "crisis"

    for a in alerts:
        cat = a.get("category", "")
        label = (a.get("label", "") or a.get("message", "")).lower()
        if cat in ("hostile", "predator_near"):
            return "raid_prep"
        if cat == "game_alert" and any(k in label for k in ("raid", "enemy", "attack")):
            return "raid_prep"
'''

new = '''        if cat == "game_alert":
            label = a.get("label", "").lower() if "label" in a else a.get("message", "").lower()
            if any(k in label for k in ("attack", "enemy", "predator", "fire")):
                is_crisis = True
    if is_crisis:
        return "crisis"

    for a in alerts:
        cat = a.get("category", "")
        label = (a.get("label", "") or a.get("message", "")).lower()
        if cat in ("hostile", "predator_near"):
            return "raid_prep"
        if cat == "game_alert" and "raid" in label:
            return "raid_prep"
        if cat == "game_alert" and "defenses" in label:
            return "raid_prep"
'''

assert old in s, "old block not found"
s = s.replace(old, new)
open(path, "w", encoding="utf-8").write(s)
print("patched")
