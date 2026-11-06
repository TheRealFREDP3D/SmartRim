"""Tests for the food-security helpers in counselor."""

import pytest

from smartrim import counselor


def _patch(monkeypatch, responder):
    calls = []

    def fake_call(name, arguments=None):
        calls.append((name, arguments or {}))
        return responder(name, arguments or {})

    monkeypatch.setattr(counselor, "_call", fake_call)
    return calls


def test_ensure_cooking_bill_adds_meal_bill_to_campfire(monkeypatch):
    def responder(name, args):
        if name == "list_things":
            return {"things": [{"id": "Campfire1", "def": "Campfire"}]}
        if name == "list_bills":
            return {"bills": []}
        if name == "add_bill":
            return {"ok": True}
        return {}

    calls = _patch(monkeypatch, responder)

    assert counselor.ensure_cooking_bill() is True
    added = [c for c in calls if c[0] == "add_bill"]
    assert added == [("add_bill", {"id": "Campfire1", "recipe": "CookMealSimple", "repeatMode": "forever"})]


def test_ensure_cooking_bill_is_idempotent(monkeypatch):
    def responder(name, args):
        if name == "list_things":
            return {"things": [{"id": "Campfire1", "def": "Campfire"}]}
        if name == "list_bills":
            return {"bills": [{"label": "Cook simple meal"}]}
        return {}

    calls = _patch(monkeypatch, responder)

    assert counselor.ensure_cooking_bill() is False
    assert not [c for c in calls if c[0] == "add_bill"]


def test_start_food_zone_skips_unfarmable_ground(monkeypatch):
    summary_calls = {"n": 0}

    def responder(name, args):
        if name == "get_area":
            summary_calls["n"] += 1
            if summary_calls["n"] == 1:
                return {"terrainSummary": {"WaterShallow": 48}}
            return {"terrainSummary": {"Soil": 48}}
        if name == "list_zones":
            return {"zones": [{"id": 0, "kind": "growing", "plant": "Plant_Rice"}]}
        if name == "designate":
            return {"ok": True}
        return {}

    calls = _patch(monkeypatch, responder)

    assert counselor.start_food_zone(center=(30, 100)) is True
    assert summary_calls["n"] == 2
    designated = [c for c in calls if c[0] == "designate"]
    assert designated and designated[0][1]["designator"] == "Designator_ZoneAdd_Growing"


def test_start_food_zone_gives_up_without_arable_ground(monkeypatch):
    def responder(name, args):
        if name == "get_area":
            return {"terrainSummary": {"WaterDeep": 48}}
        return {}

    calls = _patch(monkeypatch, responder)

    assert counselor.start_food_zone(center=(30, 100)) is False
    assert not [c for c in calls if c[0] == "designate"]


def test_start_food_zone_needs_a_colony_center(monkeypatch):
    def responder(name, args):
        if name == "list_colonists":
            return {"colonists": []}
        raise AssertionError(f"unexpected call {name}")

    _patch(monkeypatch, responder)

    assert counselor.start_food_zone() is False


if __name__ == "__main__":  # pragma: no cover
    pytest.main([__file__, "-v"])
