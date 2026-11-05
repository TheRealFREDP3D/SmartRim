"""Desktop notifier for SmartRim urgent alerts.

Polls the active run's alerts/current.json and pops a small always-on-top window
(plus a beep) whenever a *new* urgent signature appears, so the player is alerted
even when not looking at the second screen.

Usage:
    python -m smartrim.notify            # loop (default 5s)
    python -m smartrim.notify --once     # single check, then exit
    python -m smartrim.notify --interval 10
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime

from smartrim import config

# Optional override for tests/tooling; None means the active run's alerts dir.
ALERTS_DIR: str | None = None


def _alerts_dir() -> str | None:
    return ALERTS_DIR or config.alerts_dir()


def _notified_file() -> str | None:
    d = _alerts_dir()
    return os.path.join(d, "last_notified.json") if d else None


def _load_alerts():
    d = _alerts_dir()
    if not d:
        return []
    path = os.path.join(d, "current.json")
    if not os.path.exists(path):
        return []
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        return []


def _signature(alerts):
    urgents = sorted(a.get("message", "") for a in alerts if a.get("type") == "urgent")
    return urgents


def _load_last_notified():
    path = _notified_file()
    if not path or not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f).get("signature")
    except (OSError, json.JSONDecodeError, AttributeError):
        return None


def _save_last_notified(sig):
    path = _notified_file()
    if not path:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"signature": sig, "timestamp": datetime.now().isoformat()}, f)


def _beep():
    try:
        if sys.platform == "win32":
            import winsound
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        else:
            print("\a", end="", flush=True)
    except Exception:
        pass


def _popup(title, message):
    """Show a small always-on-top window. Falls back to console if no GUI."""
    try:
        import tkinter as tk
        from tkinter import ttk
    except ImportError:
        print(f"[SmartRim] {title}: {message}")
        return
    try:
        root = tk.Tk()
        root.title(title)
        root.attributes("-topmost", True)
        root.resizable(False, False)
        frm = ttk.Frame(root, padding=16)
        frm.grid()
        ttk.Label(frm, text=title, font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="w")
        ttk.Label(frm, text=message, wraplength=360, justify="left").grid(row=1, column=0, sticky="w", pady=(8, 12))
        ttk.Button(frm, text="OK", command=root.destroy).grid(row=2, column=0, sticky="e")

        # Auto-close after 12s
        root.after(12000, root.destroy)
        root.mainloop()
    except Exception as e:
        print(f"[SmartRim] popup failed: {e}")
        print(f"{title}: {message}")


def check_once():
    alerts = _load_alerts()
    sig = _signature(alerts)
    if not sig:
        return False
    if sig == _load_last_notified():
        return False
    _beep()
    _popup("SmartRim — Urgent Alert", "\n".join(sig))
    _save_last_notified(sig)
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description="SmartRim desktop notifier")
    parser.add_argument("--once", action="store_true", help="Check once and exit")
    parser.add_argument("--interval", type=int, default=5, help="Poll interval in seconds")
    args = parser.parse_args(argv)

    if args.once:
        fired = check_once()
        print("notified" if fired else "no new urgent alerts")
        return 0

    print(f"SmartRim notifier running (interval={args.interval}s). Ctrl+C to stop.")
    try:
        while True:
            try:
                check_once()
            except Exception as e:
                print(f"notify error: {e}", file=sys.stderr)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("stopped")
        return 0


if __name__ == "__main__":
    sys.exit(main())
