"""Tests for counselor.ensure_research_project."""

import pytest

from smartrim import counselor


def _patch(monkeypatch, responder):
    calls = []

    def fake_call(name, arguments=None):
        calls.append((name, dict(arguments or {})))
        return responder(name, arguments or {})

    monkeypatch.setattr(counselor, "_call", fake_call)
    return calls


def test_leaves_an_active_project_alone(monkeypatch):
    calls = _patch(monkeypatch, lambda name, args: {"current": {"defName": "Machining"}})

    assert counselor.ensure_research_project() is False
    assert [c[0] for c in calls] == ["get_research"]


def test_prefers_machining_over_cheaper_projects(monkeypatch):
    def responder(name, args):
        if name == "get_research" and args.get("list") == "unfinished":
            return {"projects": [
                {"defName": "Brewing", "cost": 400, "canStartNow": True},
                {"defName": "Machining", "cost": 1000, "canStartNow": True},
                {"defName": "GunTurrets", "cost": 500, "canStartNow": False},
            ]}
        if name == "get_research":
            return {"current": None}
        if name == "set_research":
            return {"ok": True}
        return {}

    calls = _patch(monkeypatch, responder)

    assert counselor.ensure_research_project() is True
    assert calls[-1] == ("set_research", {"project": "Machining"})


def test_falls_back_to_cheapest_startable(monkeypatch):
    def responder(name, args):
        if name == "get_research" and args.get("list") == "unfinished":
            return {"projects": [
                {"defName": "Harp", "cost": 900, "canStartNow": True},
                {"defName": "WoodFloor", "cost": 300, "canStartNow": True},
                {"defName": "GunTurrets", "cost": 100, "canStartNow": False},
            ]}
        if name == "get_research":
            return {"current": None}
        return {"ok": True}

    calls = _patch(monkeypatch, responder)

    assert counselor.ensure_research_project() is True
    assert calls[-1] == ("set_research", {"project": "WoodFloor"})


def test_does_nothing_when_no_project_can_start(monkeypatch):
    def responder(name, args):
        if name == "get_research" and args.get("list") == "unfinished":
            return {"projects": [{"defName": "GunTurrets", "cost": 500, "canStartNow": False}]}
        return {"current": None}

    calls = _patch(monkeypatch, responder)

    assert counselor.ensure_research_project() is False
    assert not [c for c in calls if c[0] == "set_research"]


if __name__ == "__main__":  # pragma: no cover
    pytest.main([__file__, "-v"])
