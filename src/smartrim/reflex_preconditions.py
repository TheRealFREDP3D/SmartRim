"""Precondition predicates for reflex actions.

Each predicate is a pure function ``(game_state) -> bool``. game_state is the
dict returned by ``counselor.game_state()`` (or a snapshot-derived equivalent),
so predicates are testable without the MCP server. All lookups are tolerant of
missing keys.
"""

__all__ = [
    "PRECONDITIONS",
    "has_fire_alert",
    "has_raid_alert",
    "has_shooter_above_5",
    "has_unassigned_colonist",
    "none_drafted",
]

_ALERT_KEYS = ("label", "message")


def _alerts(game_state):
    return game_state.get("alerts") or [] if isinstance(game_state, dict) else []


def _colonists(game_state):
    return game_state.get("colonists") or [] if isinstance(game_state, dict) else []


def _alert_text(alert):
    if not isinstance(alert, dict):
        return ""
    return " ".join(str(alert.get(k) or "") for k in _ALERT_KEYS).lower()


def has_raid_alert(game_state) -> bool:
    """Raid/enemy/attack keyword in any alert label or message."""
    text = " ".join(_alert_text(a) for a in _alerts(game_state))
    return any(kw in text for kw in ("raid", "enemy", "attack"))


def has_fire_alert(game_state) -> bool:
    """Fire keyword in any alert label or message."""
    text = " ".join(_alert_text(a) for a in _alerts(game_state))
    return "fire" in text


def has_unassigned_colonist(game_state) -> bool:
    """Idle colonist alert, or a colonist with no assigned bed."""
    for a in _alerts(game_state):
        if a.get("category") == "idle_colonist" or "idle" in _alert_text(a):
            return True
    for c in _colonists(game_state):
        if isinstance(c, dict) and not c.get("bed_id") and not c.get("bed"):
            return True
    return False


def has_shooter_above_5(game_state) -> bool:
    """At least 5 combat-ready colonists (not downed, not sleeping, healthy)."""
    count = 0
    for c in _colonists(game_state):
        if not isinstance(c, dict):
            continue
        if c.get("downed"):
            continue
        job = str(c.get("job", "")).lower()
        if "sleep" in job or "rest" in job:
            continue
        health = c.get("health")
        if health is not None and health <= 0:
            continue
        count += 1
    return count >= 5


def none_drafted(game_state) -> bool:
    """No colonist is currently drafted."""
    for c in _colonists(game_state):
        if isinstance(c, dict) and c.get("drafted") is True:
            return False
    return True


PRECONDITIONS = {
    "has_raid_alert": has_raid_alert,
    "has_fire_alert": has_fire_alert,
    "has_unassigned_colonist": has_unassigned_colonist,
    "has_shooter_above_5": has_shooter_above_5,
    "none_drafted": none_drafted,
}
