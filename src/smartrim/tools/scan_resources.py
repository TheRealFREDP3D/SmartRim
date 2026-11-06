"""Grid-scan a map area for resource concentrations.

Promoted from runtime/scan_trees.py and runtime/scan_trees_near.py.
Generalized: scans for any resource keyword, accepts step/box size,
minimum count threshold, and optional center point with max distance.
Outputs sorted candidates (count, x, z) plus optional distance ordering.
"""

import argparse
import sys

sys.path.insert(0, "src")
from smartrim.config import MCP_URL
from smartrim.mcp_client import McpClient


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Grid-scan for resource concentrations via get_area."
    )
    parser.add_argument("--match", default="tree",
                        help="Substring matched against thing group label (case-insensitive).")
    parser.add_argument("--min-x", type=int, default=6)
    parser.add_argument("--min-z", type=int, default=6)
    parser.add_argument("--max-x", type=int, default=None)
    parser.add_argument("--max-z", type=int, default=None)
    parser.add_argument("--step", type=int, default=12)
    parser.add_argument("--box", type=int, default=20,
                        help="Size of each scanned cell (square).")
    parser.add_argument("--min-count", type=int, default=12,
                        help="Minimum group count to report a cell.")
    parser.add_argument("--center-x", type=int, default=None)
    parser.add_argument("--center-z", type=int, default=None)
    parser.add_argument("--max-dist", type=int, default=None,
                        help="Max Manhattan distance from center; skips cells beyond it.")
    parser.add_argument("--delay", type=float, default=0.05)
    parser.add_argument("--full-map", action="store_true",
                        help="Scan whole map (uses get_map size for bounds).")
    args = parser.parse_args(argv)

    mc = McpClient(MCP_URL, delay=args.delay)

    if args.full_map:
        m = mc.call_tool("get_map")
        max_x = m.get("sizeX", 174)
        max_z = m.get("sizeZ", 174)
        min_x = 0
        min_z = 0
    else:
        max_x = args.max_x if args.max_x is not None else 174
        max_z = args.max_z if args.max_z is not None else 174
        min_x = args.min_x
        min_z = args.min_z

    keyword = args.match.lower()
    cx = args.center_x
    cz = args.center_z
    rows = []

    for x in range(min_x, max_x - args.box, args.step):
        for z in range(min_z, max_z - args.box, args.step):
            if cx is not None and cz is not None:
                dist = abs(x - cx) + abs(z - cz)
                if args.max_dist is not None and dist > args.max_dist:
                    continue
            else:
                dist = 0

            a = mc.call_tool(
                "get_area",
                {
                    "minX": x, "minZ": z,
                    "maxX": x + args.box, "maxZ": z + args.box,
                    "summary": True,
                },
            )
            count = 0
            for g in a.get("thingGroups") or []:
                if keyword in str(g.get("label", "")).lower():
                    count += g.get("count") or 0
            if count >= args.min_count:
                rows.append((count, dist, x, z))

    rows.sort(reverse=True)
    print(f"{args.match}, count, dist, x, z")
    for count, dist, x, z in rows[:20]:
        print(f"  {count}, {dist}, {x}, {z}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
