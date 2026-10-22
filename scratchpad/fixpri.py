import json, sys
sys.path.insert(0, r"C:\Users\fred\Desktop\SmartRim\sidecar")
from counselor import _call

names = ["Taten 'Tater' Stamm", "Baran Gargatosh", "Bran 'Sawyher' Shawb"]

# Enable manual priorities and set basic work for everyone
for name in names:
    for wt in ["Hauling", "Construction", "Cleaning", "Firefighter", "Patient"]:
        r = _call("set_work_priority", {"name": name, "workType": wt, "priority": 1})
        print(f"{name} {wt} 1: {r.get('ok') if isinstance(r, dict) else r}")

# Role-specific
_call("set_work_priority", {"name": "Taten 'Tater' Stamm", "workType": "Hunting", "priority": 1})
_call("set_work_priority", {"name": "Taten 'Tater' Stamm", "workType": "Shooting", "priority": 2})
_call("set_work_priority", {"name": "Baran Gargatosh", "workType": "Doctor", "priority": 1})
_call("set_work_priority", {"name": "Baran Gargatosh", "workType": "Growing", "priority": 2})
_call("set_work_priority", {"name": "Baran Gargatosh", "workType": "Research", "priority": 3})
_call("set_work_priority", {"name": "Bran 'Sawyher' Shawb", "workType": "Construction", "priority": 1})
_call("set_work_priority", {"name": "Bran 'Sawyher' Shawb", "workType": "Mining", "priority": 2})
_call("set_work_priority", {"name": "Bran 'Sawyher' Shawb", "workType": "Growing", "priority": 3})
print("priorities set")
