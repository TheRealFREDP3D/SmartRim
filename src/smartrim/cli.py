"""SmartRim CLI - Command-line interface for game interaction."""

import json
import os
import sys
from datetime import datetime

from smartrim import counselor as c
from smartrim.config import BASE_DIR
from smartrim.reflex_actor import ReflexActor

HUMAN_ACTION_FILE = os.path.join(BASE_DIR, "memory", "last_human_action.json")
HUMAN_ACTIONS = ("order_pawn", "build", "designate")
HUMAN_WINDOW_SECONDS = 60


def run_ping(args=None):
    """Check MCP server status and return a structured dict."""
    ok, err = c.ping(timeout=1.5)
    return {
        "status": "connected" if ok else "offline",
        "url": getattr(c, "MCP_URL", "http://localhost:8787/"),
        "error": err,
    }


def check_connection(timeout=1.5):
    """Quick pre-flight check to verify RimMolt MCP connectivity."""
    ok, err = c.ping(timeout=timeout)
    if not ok:
        print("=" * 64, file=sys.stderr)
        print("[!] ERROR: Cannot connect to RimWorld MCP server at http://localhost:8787/", file=sys.stderr)
        print("=" * 64, file=sys.stderr)
        print("RimWorld / RimMolt does not appear to be running or responding.", file=sys.stderr)
        print("\nPlease ensure:", file=sys.stderr)
        print("  1. RimWorld is running.", file=sys.stderr)
        print("  2. The RimMolt mod is active and listening on port 8787.", file=sys.stderr)
        print("  3. A colony / save game is loaded in-game.", file=sys.stderr)
        if err:
            print(f"\nConnection details: {err}", file=sys.stderr)
        print("=" * 64, file=sys.stderr)
        print("Tip: Use '--force' to bypass this check.", file=sys.stderr)
        return False
    return True


def _record_human_action(action):
    """Record the timestamp of a human-issued order_pawn/build/designate call.

    Written before the MCP call so the 60-second deferral window applies even
    when the game call fails or the command runs outside the monitor process.
    """
    if action not in HUMAN_ACTIONS:
        return
    try:
        os.makedirs(os.path.dirname(HUMAN_ACTION_FILE), exist_ok=True)
        with open(HUMAN_ACTION_FILE, "w", encoding="utf-8") as f:
            json.dump({"action": action, "timestamp": datetime.now().isoformat()}, f)
    except OSError:
        pass


def _build(args):
    _record_human_action("build")
    return c.build(args[0], int(args[1]), int(args[2]), args[3] if len(args) > 3 else None)


def _order(args):
    _record_human_action("order_pawn")
    return c.order(args[0], args[1], args[2] if len(args) > 2 else None)


def _designate(args):
    _record_human_action("designate")
    return c.designate(
        args[0], int(args[1]), int(args[2]),
        int(args[3]) if len(args) > 3 else None,
        int(args[4]) if len(args) > 4 else None,
    )


def run_reflex(args):
    """reflex pause | resume | status"""
    if not args:
        print("Usage: smartrim reflex <pause|resume|status>")
        return
    sub = args[0].lower()
    actor = ReflexActor()
    if sub == "pause":
        conditions = c.conditions() or {}
        day = conditions.get("date") if isinstance(conditions, dict) else None
        try:
            os.makedirs(os.path.dirname(actor.pause_file), exist_ok=True)
            # Write to temp file first, then atomic replace
            temp_path = actor.pause_file + ".tmp"
            with open(temp_path, "w", encoding="utf-8") as f:
                json.dump({"day": day, "set_at": datetime.now().isoformat()}, f)
            os.replace(temp_path, actor.pause_file)
        except OSError as e:
            print(f"Error: {e}", file=sys.stderr)
            return
        print(f"Reflex pause set (day={day}). Cleared on day roll; use 'reflex resume' to clear early.")
    elif sub == "resume":
        removed = False
        try:
            if os.path.exists(actor.pause_file):
                os.remove(actor.pause_file)
                removed = True
        except OSError:
            pass
        print("Reflex pause cleared." if removed else "Reflex pause was not set.")
    elif sub == "status":
        conditions = c.conditions() or {}
        day = conditions.get("date") if isinstance(conditions, dict) else None
        paused = actor._paused(day)
        lock_pid = None
        try:
            if os.path.exists(actor.lock_file):
                lock_pid = int(open(actor.lock_file).read().strip())
        except (OSError, ValueError):
            lock_pid = None
        human = None
        try:
            human = json.load(open(actor.human_action_file, encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            human = None
        human_age = None
        if human and human.get("timestamp"):
            try:
                human_age = (datetime.now() - datetime.fromisoformat(human["timestamp"])).total_seconds()
            except ValueError:
                human_age = None
        print(f"REFLEX_KILL={os.getenv('REFLEX_KILL', '1')} "
              f"REFLEX_DRY_RUN={os.getenv('REFLEX_DRY_RUN', '1')} "
              f"REFLEX_PAUSE={os.getenv('REFLEX_PAUSE', '1')}")
        print(f"pause: {'active' if paused else 'inactive'} (day={day})")
        print(f"lock: held by PID {lock_pid}" if lock_pid else "lock: free")
        if human:
            age = f"{human_age:.0f}s ago" if human_age is not None else "unknown age"
            print(f"last human action: {human.get('action')} ({human.get('timestamp')}, {age})")
        else:
            print("last human action: none recorded")
    else:
        print(f"Unknown reflex subcommand: {sub}")
        print("Usage: smartrim reflex <pause|resume|status>")


COMMANDS = {
    "ping": run_ping,
    "status": lambda args: c.game_state(),
    "colonists": lambda args: c.colonists(),
    "alerts": lambda args: c.alerts(),
    "resources": lambda args: c.resources(),
    "research": lambda args: c.research(),
    "zones": lambda args: c.zones(),
    "pause": lambda args: c.pause(),
    "resume": lambda args: c.resume(),
    "wait": lambda args: c.wait(int(args[0]) if args else 1),
    "say": lambda args: c.say(" ".join(args)),
    "daily": lambda args: c.daily_summary(),
    "build": _build,
    "research_set": lambda args: c.set_research(args[0]),
    "priority": lambda args: c.set_priority(args[0], args[1], int(args[2])),
    "area": lambda args: c.area(int(args[0]), int(args[1]), int(args[2]), int(args[3]), summary=True),
    "inspect": lambda args: c.inspect(int(args[0]), int(args[1])),
    "draft": lambda args: c.draft(args),
    "undraft": lambda args: c.undraft(args),
    "order": _order,
    "designate": _designate,
    "reflex": run_reflex,
    "save": lambda args: c.save(args[0] if args else None),
    "screenshot": lambda args: c.screenshot(),
    "map": lambda args: c.get_map(),
    "power": lambda args: c.power(),
    "world": lambda args: c.world(),
    "wildlife": lambda args: c.wildlife(),
    "unforbid_all": lambda args: c.unforbid_all(),
    "survey": lambda args: c.survey(int(args[0]), int(args[1]), int(args[2]), int(args[3])),
    "raid_status": lambda args: c.raid_status(),
    "equip": lambda args: c.equip(args[0], args[1] if len(args) > 1 else None, args[2] if len(args) > 2 else None),
}


def main(argv=None):
    """CLI entry point for `python -m smartrim.cli`."""
    import sys
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print("Usage: python -m smartrim.cli <command> [args...]")
        print(f"Available commands: {', '.join(COMMANDS.keys())}")
        sys.exit(1)
    cmd = argv[0]
    args = argv[1:]
    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd}")
        print(f"Available commands: {', '.join(COMMANDS.keys())}")
        sys.exit(1)
    try:
        result = COMMANDS[cmd](args)
        if result is not None:
            # Detect error dictionaries returned by MCP calls
            if isinstance(result, dict) and result.get("error"):
                print(f"Error: {result}", file=sys.stderr)
                sys.exit(1)
            print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
