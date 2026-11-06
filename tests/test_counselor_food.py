"""Counselor food-supply helpers: shape tolerance and honest (ok, reason)."""

from smartrim import counselor


def _patch_call(monkeypatch, handler):
    monkeypatch.setattr(counselor, "_call", handler)


def _colonists(_name, _args=None):
    return {"colonists": [{"name": "Ana", "x": 10, "z": 10}]}


class TestZoneListShapes:
    def test_bare_list(self):
        assert counselor._zone_list([{"id": 1}]) == [{"id": 1}]

    def test_wrapped(self):
        assert counselor._zone_list({"zones": [{"id": 1}]}) == [{"id": 1}]

    def test_error_or_garbage(self):
        assert counselor._zone_list({"error": "boom"}) == []
        assert counselor._zone_list("nonsense") == []
        assert counselor._zone_list(None) == []


class TestEnsureCookingBill:
    def _handler(self, buildings, bills_by_id, add_result=None):
        def handler(name, args=None):
            if name == "list_things":
                return {"things": buildings}
            if name == "list_bills":
                return {"bills": bills_by_id.get(args["id"], [])}
            if name == "add_bill":
                return add_result or {"added": True}
            raise AssertionError(name)
        return handler

    def test_no_stoves_or_campfires(self, monkeypatch):
        _patch_call(monkeypatch, self._handler([{"def": "Table", "id": "t1"}], {}))
        ok, detail = counselor.ensure_cooking_bill()
        assert ok is False
        assert "no campfire or stove" in detail

    def test_lists_things_error(self, monkeypatch):
        _patch_call(monkeypatch, lambda name, args=None: {"error": "mcp down"})
        ok, detail = counselor.ensure_cooking_bill()
        assert ok is False
        assert "list_things failed" in detail

    def test_adds_bill_to_stove_missing_one(self, monkeypatch):
        _patch_call(monkeypatch, self._handler(
            [{"def": "Stove_Fueled", "id": "s1"}], {}, add_result={"added": True}))
        ok, detail = counselor.ensure_cooking_bill()
        assert ok is True
        assert "s1" in detail

    def test_campfire_counts_as_stove(self, monkeypatch):
        _patch_call(monkeypatch, self._handler(
            [{"def": "Campfire", "id": "c1"}], {}, add_result={"added": True}))
        ok, _ = counselor.ensure_cooking_bill()
        assert ok is True

    def test_existing_meal_bill_not_duplicated(self, monkeypatch):
        _patch_call(monkeypatch, self._handler(
            [{"def": "Stove_Fueled", "id": "s1"}], {"s1": [{"label": "Cook simple meal"}]}))
        ok, detail = counselor.ensure_cooking_bill()
        assert ok is False
        assert "already present" in detail

    def test_add_bill_error_is_reported(self, monkeypatch):
        _patch_call(monkeypatch, self._handler(
            [{"def": "Stove_Fueled", "id": "s1"}], {}, add_result={"error": "no recipe"}))
        ok, detail = counselor.ensure_cooking_bill()
        assert ok is False
        assert "add_bill failed: no recipe" in detail


class TestStartFoodZone:
    def _patch_arable(self, monkeypatch, terrain=None):
        """All candidates return the given terrain (or a healthy soil default)."""
        terrain = terrain if terrain is not None else {"Soil": 96, "Rock": 16}

        def handler(name, args=None):
            if name == "list_colonists":
                return _colonists(name, args)
            if name == "get_area":
                return {"summary": True, "terrainSummary": terrain}
            if name == "designate":
                return {"designated": 48}
            if name == "list_zones":
                handler.zones_calls += 1
                if handler.zones_calls == 1:
                    return {"zones": []}                      # before
                return {"zones": [{"id": 42, "kind": "growing", "plant": "Plant_Rice"}]}  # after
            if name == "set_growing_zone":
                return {"id": 42}
            raise AssertionError(name)
        handler.zones_calls = 0
        return handler

    def test_creates_zone_and_sets_plant(self, monkeypatch):
        handler = self._patch_arable(monkeypatch)
        _patch_call(monkeypatch, handler)
        ok, detail = counselor.start_food_zone()
        assert ok is True
        assert "growing zone" in detail

    def test_terrain_key_variants_are_tolerated(self, monkeypatch):
        terrain = {"Soil": 96, "Rock": 16}
        for key in ("terrainSummary", "terrain", "terrainCounts"):
            terrain_key = key
            calls = []

            def handler(name, args=None, _key=terrain_key, _calls=calls):
                if name == "list_colonists":
                    return _colonists(name, args)
                if name == "get_area":
                    return {"summary": True, _key: terrain}
                if name == "designate":
                    return {"designated": 48}
                if name == "list_zones":
                    _calls.append(name)
                    if len(_calls) == 1:
                        return {"zones": []}
                    return {"zones": [{"id": 42, "kind": "growing", "plant": "Plant_Rice"}]}
                if name == "set_growing_zone":
                    return {"id": 42}
                raise AssertionError(name)

            _patch_call(monkeypatch, handler)
            ok, _ = counselor.start_food_zone()
            assert ok is True, key

    def test_missing_terrain_info_proceeds_optimistically(self, monkeypatch):
        calls = []

        def handler(name, args=None):
            if name == "list_colonists":
                return _colonists(name, args)
            if name == "get_area":
                return {"summary": True}          # no terrain keys at all
            if name == "designate":
                return {"designated": 48}
            if name == "list_zones":
                calls.append(name)
                if len(calls) == 1:
                    return {"zones": []}
                return {"zones": [{"id": 42, "kind": "growing", "plant": "Plant_Rice"}]}
            if name == "set_growing_zone":
                return {"id": 42}
            raise AssertionError(name)

        _patch_call(monkeypatch, handler)
        ok, _ = counselor.start_food_zone()
        assert ok is True

    def test_no_arable_ground(self, monkeypatch):
        _patch_call(monkeypatch, self._patch_arable(monkeypatch, terrain={"Rock": 112}))
        ok, detail = counselor.start_food_zone()
        assert ok is False
        assert "arable" in detail

    def test_no_colonists_on_map(self, monkeypatch):
        _patch_call(monkeypatch, lambda name, args=None: {"colonists": []})
        ok, detail = counselor.start_food_zone()
        assert ok is False
        assert "no colonists" in detail

    def test_get_area_error_aborts(self, monkeypatch):
        def handler(name, args=None):
            if name == "list_colonists":
                return _colonists(name, args)
            if name == "get_area":
                return {"error": "area too big"}
            raise AssertionError(name)
        _patch_call(monkeypatch, handler)
        ok, detail = counselor.start_food_zone()
        assert ok is False
        assert "get_area failed" in detail
