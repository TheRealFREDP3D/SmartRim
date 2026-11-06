"""Precondition predicates for reflex actions.

Each predicate is a pure function ``(game_state) -> bool``. game_state is the
dict returned by ``counselor.game_state()`` (or a snapshot-derived equivalent),
so predicates are testable without the MCP server. All lookups are tolerant of
missing keys.
"""

__all__ = [
    "PRECONDITIONS",
    "has_downed_colonist",
    "has_fire_alert",
    "has_food_alert",
    "has_raid_alert",
    "has_research_idle_alert",
    "has_shooter_above_5",
    "has_unassigned_colonist",
    "has_wounded_colonist",
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
    return any(kw in text for kw in ("raid", "enem", "attack", "hostile"))


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
    """At least one combat-ready colonist with Shooting skill above 5.

    The previous version required five combat-ready colonists, which made the
    raid reflex impossible for a normal early colony. The name and the intent
    are about a competent shooter, not a headcount.
    """
    import re

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
        for skill in c.get("topSkills") or []:
            match = re.search(r"Shooting\s+(\d+)", str(skill))
            if match and int(match.group(1)) > 5:
                return True
    return False


def none_drafted(game_state) -> bool:
    """No colonist is currently drafted."""
    for c in _colonists(game_state):
        if isinstance(c, dict) and c.get("drafted") is True:
            return False
    return True


def has_wounded_colonist(game_state) -> bool:
    """Any colonist injured (health below 100) and not already downed."""
    for c in _colonists(game_state):
        if not isinstance(c, dict):
            continue
        if c.get("downed"):
            continue
        health = c.get("health")
        if health is not None and health < 100:
            return True
    return False


def has_downed_colonist(game_state) -> bool:
    """Any colonist currently downed."""
    return any(
        isinstance(c, dict) and c.get("downed")
        for c in _colonists(game_state)
    )


def has_food_alert(game_state) -> bool:
    """Food shortage mentioned in any alert label or message."""
    text = " ".join(_alert_text(a) for a in _alerts(game_state))
    return any(kw in text for kw in (
        "food stock low", "starving", "starvation", "malnutrition",
        "no food", "food shortage",
    ))


def has_research_idle_alert(game_state) -> bool:
    """The game reports that no research project is selected."""
    text = " ".join(_alert_text(a) for a in _alerts(game_state))
    return "research project" in text or "no research" in text


PRECONDITIONS = {
    "has_raid_alert": has_raid_alert,
    "has_fire_alert": has_fire_alert,
    "has_unassigned_colonist": has_unassigned_colonist,
    "has_shooter_above_5": has_shooter_above_5,
    "none_drafted": none_drafted,
    "has_wounded_colonist": has_wounded_colonist,
    "has_downed_colonist": has_downed_colonist,
    "has_food_alert": has_food_alert,
    "has_research_idle_alert": has_research_idle_alert,
}
