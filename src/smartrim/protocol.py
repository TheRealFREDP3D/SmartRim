"""Run protocol: what a comparable run is, and how to enforce it.

The evaluation protocol (docs/RUN-PROTOCOL.md) fixes scenario, storyteller,
difficulty, run length and the no-reload rule so runs are comparable. The
sidecar cannot see scenario or the tile from MCP, but it CAN see what the
game reports: storyteller, difficulty and daysPassed. Those are stamped on
every end.json as a fingerprint, and the evaluator refuses mismatched
protocols by default.

Definitive endings (monitor-written) are the only valid comparison set;
inconclusive markers are already quarantined separately.
"""

from __future__ import annotations

PROTOCOL = {
    "scenario": "Crashlanded",
    "storyteller": "Cassandra Classic",
    "difficulty": "Adventure story",
    "run_days": 11,
    "biome": "temperate forest (flat)",  # human-checked at colony creation; recorded, not enforced
}

# Only what the game itself reports is fingerprint-checked. Scenario/tile are
# human responsibilities (they are why the protocol forbids reload/scumming).
ENFORCED_KEYS = ("storyteller", "difficulty", "run_days")


def normalize(value):
    return str(value or "").strip().lower()


def protocol_fingerprint(*, storyteller=None, difficulty=None, run_days=None) -> dict:
    return {
        "storyteller": storyteller,
        "difficulty": difficulty,
        "run_days": int(run_days) if run_days is not None else None,
    }


def stamp(marker: dict, *, storyteller=None, difficulty=None, run_days=None) -> dict:
    """Attach the protocol block to an end.json marker dict (in place)."""
    marker = dict(marker)
    marker["protocol"] = protocol_fingerprint(
        storyteller=storyteller, difficulty=difficulty, run_days=run_days)
    return marker


def protocol_matches(marker) -> bool:
    """True when a definitive marker conforms to the evaluation protocol."""
    if not isinstance(marker, dict):
        return False
    fp = marker.get("protocol")
    if not isinstance(fp, dict):
        return False
    if normalize(fp.get("storyteller")) != normalize(PROTOCOL["storyteller"]):
        return False
    if normalize(fp.get("difficulty")) != normalize(PROTOCOL["difficulty"]):
        return False
    try:
        if int(fp.get("run_days")) != int(PROTOCOL["run_days"]):
            return False
    except (TypeError, ValueError):
        return False
    return True
