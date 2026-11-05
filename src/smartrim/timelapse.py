"""Timelapse capture for SmartRim.

Takes in-game screenshots at configured hours (default 6am and 6pm) and compiles
them into an animated GIF so the colony's growth can be reviewed as a timelapse.

Usage:
    python -m smartrim.timelapse capture [--run-id ID]   # take one screenshot now
    python -m smartrim.timelapse build [--run-id ID]     # compile GIF
    python -m smartrim.timelapse list [--run-id ID]      # list captures
    python -m smartrim.timelapse status                  # show config
"""

import argparse
import contextlib
import json
import os
import shutil
import time
from datetime import datetime

try:
    from smartrim import config
    from smartrim.config import UNSET_RUN_ID, resolve_run_id
except ImportError:  # pragma: no cover - direct execution fallback
    config = None
    UNSET_RUN_ID = "current-run"

    def resolve_run_id():
        env_id = os.getenv("RUN_ID", "").strip()
        return env_id if env_id and env_id != UNSET_RUN_ID else None


# Optional override for tests/tooling; None means runtime/<run_id>/timelapse.
TIMELAPSE_DIR: str | None = None
TIMELAPSE_HOURS = [int(h.strip()) for h in os.getenv("TIMELAPSE_HOURS", "6,18").split(",") if h.strip().isdigit()]
TIMELAPSE_ENABLED = os.getenv("TIMELAPSE_ENABLED", "1") == "1"


def _resolve_run(run_id=None):
    """Concrete run id for an operation, or None when no run is known.

    The ``current-run`` sentinel is never used as a directory name.
    """
    rid = str(run_id or resolve_run_id() or "").strip()
    return None if not rid or rid == UNSET_RUN_ID else rid


def _run_dir(run_id=None, create=True):
    """Return (dir, run_id). Only creates the directory when ``create`` is True.

    Reading timelapse state must never create ``runtime/<run>/timelapse`` — that
    used to leave an empty ``current-run`` folder just by opening the TUI tab.
    """
    rid = _resolve_run(run_id)
    if rid is None:
        return None, None
    if TIMELAPSE_DIR:
        d = os.path.join(TIMELAPSE_DIR, rid)
        if create:
            os.makedirs(d, exist_ok=True)
    elif config is not None:
        d = config.timelapse_dir(rid, create=create)
    else:  # pragma: no cover
        return None, None
    return d, rid


def _index_path(run_id=None, create=False):
    d, _ = _run_dir(run_id, create=create)
    return os.path.join(d, "index.json") if d else None


def _load_index(run_id=None):
    p = _index_path(run_id)
    if p and os.path.exists(p):
        try:
            with open(p, encoding="utf-8") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError):
            return []
    return []


def _save_index(entries, run_id=None):
    p = _index_path(run_id, create=True)
    if p is None:
        raise ValueError("no active run to save captures for")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)


def _close_screenshot_dialogs(client):
    """Close any pausing dialogs the screenshot tool leaves behind and unpause."""
    for _ in range(10):
        try:
            w = client.call_tool("list_windows")
        except Exception:
            break
        wins = w.get("windows", []) if isinstance(w, dict) else []
        target = None
        for win in wins:
            if win.get("forcePause") or win.get("type") in ("Dialog_SaveFileList_Save", "MainTabWindow_Menu", "ImmediateWindow"):
                target = win
                break
        if target is None:
            break
        try:
            client.call_tool("window_action", {"index": target["index"], "close": True})
        except Exception:
            break
        time.sleep(0.5)
    with contextlib.suppress(Exception):
        client.call_tool("set_speed", {"action": "unpause"})


def capture(run_id=None, label=None):
    """Take one screenshot now. Returns dict with path or error.

    Captures the region covering all colonists (the base area) with a margin,
    zoomed out enough to see the whole base, without disturbing the player camera.
    """
    dest_dir, rid = _run_dir(run_id, create=True)
    if dest_dir is None:
        return {"error": "no active run: start the monitor or pass --run-id"}

    from smartrim.mcp_client import McpClient
    client = McpClient(os.getenv("MCP_URL", "http://localhost:8787/"), delay=0.15)

    # Determine region covering all colonists (base area) with margin
    try:
        lc = client.call_tool("list_colonists")
        xs, zs = [], []
        for col in (lc.get("colonists") if isinstance(lc, dict) else []) or []:
            try:
                p = client.call_tool("get_pawn", {"id": col["id"]})
                if isinstance(p, dict) and "x" in p and "z" in p:
                    xs.append(p["x"])
                    zs.append(p["z"])
            except Exception:
                pass
        gm = client.call_tool("get_map")
        size_x = gm.get("sizeX", 250) if isinstance(gm, dict) else 250
        size_z = gm.get("sizeZ", 250) if isinstance(gm, dict) else 250
        if xs:
            margin = 35
            x0 = max(0, min(xs) - margin)
            z0 = max(0, min(zs) - margin)
            x1 = min(size_x - 1, max(xs) + margin)
            z1 = min(size_z - 1, max(zs) + margin)
            w = x1 - x0 + 1
            h = z1 - z0 + 1
        else:
            x0 = max(0, size_x // 2 - 60)
            z0 = max(0, size_z // 2 - 60)
            w, h = 120, 120
        res = client.call_tool("screenshot", {"x": x0, "z": z0, "w": w, "h": h, "include_ui": False})
    except Exception as e:
        return {"error": str(e)}
    if isinstance(res, dict) and res.get("error"):
        return res
    src_path = res.get("path")
    if not src_path or not os.path.exists(src_path):
        return {"error": f"screenshot file not found: {src_path}"}
    _close_screenshot_dialogs(client)

    d = dest_dir
    ts = datetime.now()
    fname = (label or ts.strftime("capture-%Y%m%d-%H%M%S")) + ".png"
    dest = os.path.join(d, fname)
    # Resize to a manageable size for timelapse (max 1024px) if Pillow available
    try:
        from PIL import Image
        with Image.open(src_path) as im:
            im.thumbnail((1024, 1024))
            im.save(dest)
    except Exception:
        shutil.copy2(src_path, dest)

    # game day/hour if available
    day = None
    hour = None
    try:
        st = client.call_tool("get_status")
        if isinstance(st, dict):
            day = st.get("daysPassed")
    except Exception:
        pass
    try:
        cond = client.call_tool("get_conditions")
        if isinstance(cond, dict):
            hour = cond.get("hour")
    except Exception:
        pass

    entries = _load_index(rid)
    entries.append({
        "file": fname,
        "timestamp": ts.isoformat(),
        "day": day,
        "hour": hour,
    })
    _save_index(entries, rid)
    return {"ok": True, "path": dest, "run_id": rid, "day": day, "hour": hour}


def list_captures(run_id=None):
    """List captures for a run without creating any directory."""
    d, rid = _run_dir(run_id, create=False)
    if d is None:
        return {"run_id": None, "dir": None, "index": [], "files": []}
    entries = _load_index(rid)
    # also include any png not in index
    files = sorted(f for f in os.listdir(d) if f.lower().endswith(".png")) if os.path.isdir(d) else []
    return {"run_id": rid, "dir": d, "index": entries, "files": files}


def build_gif(run_id=None, output=None, duration=800):
    """Compile captures into an animated GIF. Requires Pillow."""
    try:
        from PIL import Image
    except ImportError:
        return {"error": "Pillow not installed. pip install Pillow"}
    d, _rid = _run_dir(run_id, create=False)
    if d is None:
        return {"error": "no active run: start the monitor or pass --run-id"}
    files = sorted(f for f in os.listdir(d) if f.lower().endswith(".png")) if os.path.isdir(d) else []
    if not files:
        return {"error": "no captures found"}
    images = []
    for f in files:
        try:
            images.append(Image.open(os.path.join(d, f)).convert("RGBA"))
        except Exception:
            continue
    if not images:
        return {"error": "no readable images"}
    out = output or os.path.join(d, "timelapse.gif")
    images[0].save(out, save_all=True, append_images=images[1:], duration=duration, loop=0)
    return {"ok": True, "output": out, "frames": len(images)}


def should_capture_now():
    """Return True if current hour is a configured timelapse hour and not already captured this hour."""
    if not TIMELAPSE_ENABLED:
        return False
    if _resolve_run() is None:
        return False
    now = datetime.now()
    if now.hour not in TIMELAPSE_HOURS:
        return False
    entries = _load_index()
    # check if any capture in same hour today
    for e in entries:
        try:
            ts = datetime.fromisoformat(e.get("timestamp", ""))
            if ts.date() == now.date() and ts.hour == now.hour:
                return False
        except ValueError:
            continue
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description="SmartRim timelapse")
    sub = parser.add_subparsers(dest="cmd")
    c = sub.add_parser("capture")
    c.add_argument("--run-id", default=None)
    c.add_argument("--label", default=None)
    b = sub.add_parser("build")
    b.add_argument("--run-id", default=None)
    b.add_argument("--output", default=None)
    b.add_argument("--duration", type=int, default=800)
    listp = sub.add_parser("list")
    listp.add_argument("--run-id", default=None)
    sub.add_parser("status")
    args = parser.parse_args(argv)

    if args.cmd == "capture":
        print(json.dumps(capture(args.run_id, args.label), indent=2))
        return 0
    if args.cmd == "build":
        print(json.dumps(build_gif(args.run_id, args.output, args.duration), indent=2))
        return 0
    if args.cmd == "list":
        print(json.dumps(list_captures(args.run_id), indent=2))
        return 0
    if args.cmd == "status":
        print(f"TIMELAPSE_ENABLED={TIMELAPSE_ENABLED}")
        print(f"TIMELAPSE_HOURS={TIMELAPSE_HOURS}")
        print(f"TIMELAPSE_DIR={TIMELAPSE_DIR}")
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
