"""RimWorld Counselor CLI - Command-line interface for game interaction."""

import sys
import json
import counselor as c

COMMANDS = {
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
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <command> [args...]")
        print(f"Commands: {', '.join(sorted(COMMANDS.keys()))}")
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd}")
        print(f"Available: {', '.join(sorted(COMMANDS.keys()))}")
        return

    try:
        result = COMMANDS[cmd](args)
        print(json.dumps(result, indent=2, default=str)[:3000])
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
