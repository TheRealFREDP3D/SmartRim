"""SmartRim CLI - Command-line interface for game interaction."""

import sys
import json
import counselor as c


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
    "build": lambda args: c.build(args[0], int(args[1]), int(args[2]), args[3] if len(args) > 3 else None),
    "research_set": lambda args: c.set_research(args[0]),
    "priority": lambda args: c.set_priority(args[0], args[1], int(args[2])),
    "area": lambda args: c.area(int(args[0]), int(args[1]), int(args[2]), int(args[3]), summary=True),
    "inspect": lambda args: c.inspect(int(args[0]), int(args[1])),
    "draft": lambda args: c.draft(args),
    "undraft": lambda args: c.undraft(args),
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


def main():
    raw_args = sys.argv[1:]
    force = False
    if "--force" in raw_args:
        force = True
        raw_args.remove("--force")

    if not raw_args:
        print("Usage: python cli.py [--force] <command> [args...]")
        print(f"Commands: {', '.join(sorted(COMMANDS.keys()))}")
        return

    cmd = raw_args[0]
    args = raw_args[1:]

    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd}")
        print(f"Available: {', '.join(sorted(COMMANDS.keys()))}")
        sys.exit(1)

    # Pre-flight check for all commands except 'ping' (unless --force is passed)
    if cmd == "ping":
        result = COMMANDS["ping"](args)
        print(json.dumps(result, indent=2))
        if result.get("status") != "connected":
            sys.exit(1)
        return

    if not force and not check_connection():
        sys.exit(1)

    try:
        result = COMMANDS[cmd](args)
        print(json.dumps(result, indent=2, default=str)[:3000])
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
