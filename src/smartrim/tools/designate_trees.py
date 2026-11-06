"""Designate trees (or any matching things) within an area.

Promoted from runtime/designate_trees.py. Generalized: accepts area bounds,
designator type, match keyword, and optional cancel boxes to correct
over-broad designations (e.g. blanket plant-cut orders that also flag grass).
"""

import argparse
import sys

sys.path.insert(0, "src")
from smartrim.config import MCP_URL
from smartrim.mcp_client import McpClient


def parse_box(s):
    parts = [int(p) for p in s.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be minX,minZ,maxX,maxZ")
    return tuple(parts)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Designate matching things (default: trees) in an area."
    )
    parser.add_argument("--min-x", type=int, default=32)
    parser.add_argument("--min-z", type=int, default=76)
    parser.add_argument("--max-x", type=int, default=56)
    parser.add_argument("--max-z", type=int, default=116)
    parser.add_argument("--designator", default="Designator_PlantsCut")
    parser.add_argument(
        "--match", default="tree",
        help="Substring matched against thing label (case-insensitive).",
    )
    parser.add_argument(
        "--cancel", type=parse_box, action="append", default=None,
        help="Box to cancel first (minX,minZ,maxX,maxZ). Repeatable.",
    )
    parser.add_argument("--delay", type=float, default=0.12)
    args = parser.parse_args(argv)

    mc = McpClient(MCP_URL, delay=args.delay)

    if args.cancel:
        for box in args.cancel:
            r = mc.call_tool(
                "designate",
                {
                    "designator": "Designator_Cancel",
                    "minX": box[0], "minZ": box[1],
                    "maxX": box[2], "maxZ": box[3],
                },
            )
            print(
                f"cancel {box}: applied={r.get('applied')} rejected={r.get('rejected')}"
            )

    area = mc.call_tool(
        "get_area",
        {
            "minX": args.min_x, "minZ": args.min_z,
            "maxX": args.max_x, "maxZ": args.max_z, "confirm": True,
        },
    )
    things = area.get("things") or []
    keyword = args.match.lower()
    targets = [t for t in things if keyword in str(t.get("label", "")).lower()]
    print(f"{args.match} found: {len(targets)}")

    applied = 0
    rejected = 0
    for t in targets:
        r = mc.call_tool(
            "designate",
            {
                "designator": args.designator,
                "x": t["x"], "z": t["z"],
            },
        )
        if r.get("ok"):
            applied += 1
        else:
            rejected += 1
    print(f"designated: applied={applied} rejected={rejected}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
