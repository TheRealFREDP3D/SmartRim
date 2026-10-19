import json, sys
sys.path.insert(0, r"C:\Users\fred\Desktop\RimWorld Consellor\RimAutonomous\sidecar")
from counselor import _call

msg = "ANCIENT DANGER ALERT: As Sawyher draws near the ancient wall, a sense of foreboding. Do NOT break into it. Mark and avoid. Can be useful later (loot, but risky)."
print(_call("say", {"text": msg}).get("shown"))
print("pause:", _call("set_speed", {"action": "pause"}).get("ok"))
