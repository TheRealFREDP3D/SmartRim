"""Tests for counselor.build blueprint feasibility probing."""

import pytest

from smartrim import counselor


class FakeCall:
    """Record calls and answer them from a canned table."""

    def __init__(self, responses):
        self.responses = responses
        self.calls = []

    def __call__(self, name, arguments=None):
        self.calls.append((name, arguments or {}))
        return self.responses.get(name, {})


def _colonists(*ids):
    return {"colonists": [{"id": pid} for pid in ids]}


def test_build_returns_ok_when_a_colonist_can_construct(monkeypatch):
    fake = FakeCall(
        {
            "build": {"ok": True, "footprint": {"minX": 34, "minZ": 98, "maxX": 37, "maxZ": 101}},
            "list_colonists": _colonists("Human1"),
            "order_pawn": {"options": [{"label": "Prioritize constructing solar generator"}]},
        }
    )
    monkeypatch.setattr(counselor, "_call", fake)

    result = counselor.build("SolarGenerator", 35, 99)

    assert result["ok"] is True
    assert "cancelled" not in result
    assert [name for name, _ in fake.calls] == ["build", "list_colonists", "order_pawn"]
    # probes the center of the 4x4 footprint, not the anchor cell
    assert fake.calls[2][1]["x"] == 35
    assert fake.calls[2][1]["z"] == 99


def test_build_cancels_blueprint_when_skill_is_too_low(monkeypatch):
    fake = FakeCall(
        {
            "build": {"ok": True, "footprint": {"minX": 34, "minZ": 98, "maxX": 37, "maxZ": 101}},
            "list_colonists": _colonists("Human1", "Human2"),
            "order_pawn": {
                "options": [
                    {"label": "Cannot construct solar generator (building): Construction skill too low",
                     "disabled": True}
                ]
            },
            "inspect_thing": {"id": "Frame_SolarGenerator1"},
        }
    )
    monkeypatch.setattr(counselor, "_call", fake)

    result = counselor.build("SolarGenerator", 35, 99)

    assert result["ok"] is False
    assert result["cancelled"] is True
    assert "Construction skill too low" in result["reason"]
    assert ("do_thing_action", {"id": "Frame_SolarGenerator1", "label": "Cancel"}) in fake.calls


def test_build_keeps_blueprint_when_only_pathing_is_blocked(monkeypatch):
    fake = FakeCall(
        {
            "build": {"ok": True, "footprint": {"minX": 29, "minZ": 102, "maxX": 29, "maxZ": 102}},
            "list_colonists": _colonists("Human1"),
            "order_pawn": {"options": [{"label": "Cannot construct door: No path", "disabled": True}]},
            "inspect_thing": {"id": "Blueprint_Door1"},
        }
    )
    monkeypatch.setattr(counselor, "_call", fake)

    result = counselor.build("Door", 29, 102)

    assert result["ok"] is True
    assert "warning" in result
    assert "No path" in result["warning"]
    assert not [call for call in fake.calls if call[0] == "do_thing_action"]


def test_build_skips_probe_when_placement_failed(monkeypatch):
    fake = FakeCall({"build": {"ok": False, "reason": "Space already occupied."}})
    monkeypatch.setattr(counselor, "_call", fake)

    result = counselor.build("Wall", 20, 20)

    assert result["ok"] is False
    assert result["reason"] == "Space already occupied."
    assert [name for name, _ in fake.calls] == ["build"]


def test_build_verify_false_does_not_probe(monkeypatch):
    fake = FakeCall({"build": {"ok": True, "footprint": {"minX": 1, "minZ": 1, "maxX": 1, "maxZ": 1}}})
    monkeypatch.setattr(counselor, "_call", fake)

    result = counselor.build("Wall", 1, 1, verify=False)

    assert result["ok"] is True
    assert [name for name, _ in fake.calls] == ["build"]


if __name__ == "__main__":  # pragma: no cover
    pytest.main([__file__, "-v"])
