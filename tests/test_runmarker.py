"""Run-end markers: creation, validation, inconclusive quarantine, sweep."""

import json
import os

import pytest

from smartrim import config, evaluate, protocol, runmarker


def _stamp_protocol(marker):
    return protocol.stamp(marker, storyteller="Cassandra Classic",
                          difficulty="Adventure story", run_days=11)


def _make_run(name, *, days_passed=5, with_snapshot=True, with_advice=True, finished=False):
    run_dir = config.run_dir(name)
    os.makedirs(os.path.join(run_dir, "snapshots"), exist_ok=True)
    if with_snapshot:
        snap = {
            "run_id": name,
            "day": f"{days_passed + 1}th",
            "timestamp": "2026-11-05T12:00:00",
            "status": {
                "daysPassed": days_passed,
                "difficulty": "adventure story",
                "storyteller": "Cassandra Classic",
                "colonistCount": 3,
            },
            "summary": {"days_passed": days_passed, "colonist_count": 3},
        }
        with open(os.path.join(run_dir, "snapshots", f"day-{days_passed}.json"), "w") as f:
            json.dump(snap, f)
    if with_advice:
        with open(os.path.join(run_dir, "advice.jsonl"), "w") as f:
            f.write(json.dumps({"advice_id": f"adv-{name}", "run_id": name,
                                "severity": "urgent", "auto_paused": True,
                                "status": "expired"}) + "\n")
    if finished:
        with open(os.path.join(run_dir, "end.json"), "w") as f:
            json.dump(_stamp_protocol({"run_id": name, "stop_reason": "run_length",
                                       "days_passed": days_passed, "arm": "on",
                                       "created_by": "smartrim.monitor"}), f)
    return run_dir


def test_is_inconclusive_definitive_and_not():
    assert runmarker.is_inconclusive({"stop_reason": "run_length"}) is False
    assert runmarker.is_inconclusive({"stop_reason": "colony_death"}) is False


def test_is_inconclusive_manual_monitor_and_garbage():
    for reason in ("manual_close", "monitor_abort"):
        assert runmarker.is_inconclusive({"stop_reason": reason}) is True
    assert runmarker.is_inconclusive({"stop_reason": "bogus"}) is True
    assert runmarker.is_inconclusive({}) is True
    assert runmarker.is_inconclusive(None) is True
    assert runmarker.is_inconclusive({"stop_reason": "run_length", "inconclusive": True}) is True


def test_validate_marker():
    assert runmarker.validate_marker({"run_id": "run-001-adv", "stop_reason": "run_length",
                                      "days_passed": 11}) == []
    errors = runmarker.validate_marker({"run_id": "run-001-adv", "stop_reason": "nope"})
    assert any("stop_reason" in e for e in errors)
    errors = runmarker.validate_marker({"stop_reason": "run_length"})
    assert any("run_id" in e for e in errors)
    errors = runmarker.validate_marker({"run_id": "run-001-adv",
                                        "stop_reason": "run_length",
                                        "days_passed": -1})
    assert any("days_passed" in e for e in errors)


def test_has_run_data(tmp_path):
    empty = str(tmp_path / "empty")
    os.makedirs(empty)
    assert runmarker.has_run_data(empty) is False
    run_dir = _make_run("run-900-adv")
    assert runmarker.has_run_data(run_dir) is True


def test_close_run_writes_inconclusive_marker():
    _make_run("run-901-adv", days_passed=7)
    path = runmarker.close_run("run-901-adv", stop_reason="manual_close", note="game closed")
    with open(path, encoding="utf-8") as fh:
        marker = json.load(fh)
    assert marker["stop_reason"] == "manual_close"
    assert marker["inconclusive"] is True
    assert marker["created_by"] == "smartrim.runmarker"
    assert marker["days_passed"] == 7
    assert marker["difficulty"] == "adventure story"
    assert marker["urgent_alerts"] == 1
    assert marker["auto_pauses"] == 1
    assert marker["final_snapshot"] and os.path.isfile(marker["final_snapshot"])
    assert runmarker.is_inconclusive(marker) is True
    assert runmarker.validate_marker(marker) == []


def test_close_run_refuses_without_data():
    os.makedirs(config.run_dir("run-902-adv"))
    with pytest.raises(FileNotFoundError):
        runmarker.close_run("run-902-adv", stop_reason="manual_close")


def test_close_run_refuses_overwrite_and_force():
    _make_run("run-903-adv", finished=True)
    with pytest.raises(FileExistsError):
        runmarker.close_run("run-903-adv", stop_reason="manual_close")
    path = runmarker.close_run("run-903-adv", stop_reason="manual_close",
                               note="redone", overwrite=True)
    with open(path, encoding="utf-8") as fh:
        assert json.load(fh)["stop_reason"] == "manual_close"


def test_close_run_rejects_definitive_reasons():
    _make_run("run-904-adv")
    with pytest.raises(ValueError):
        runmarker.close_run("run-904-adv", stop_reason="run_length")


def test_find_unfinished_and_sweep():
    _make_run("run-910-adv", days_passed=3)
    _make_run("run-911-adv", days_passed=4, finished=True)
    _make_run("run-912-adv", days_passed=6)
    unfinished = runmarker.find_unfinished_runs()
    assert "run-910-adv" in unfinished
    assert "run-912-adv" in unfinished
    assert "run-911-adv" not in unfinished

    closed = runmarker.close_abandoned_runs(stop_reason="monitor_abort")
    assert sorted(closed) == ["run-910-adv", "run-912-adv"]
    for name in closed:
        marker = json.load(open(os.path.join(config.run_dir(name), "end.json"),
                                encoding="utf-8"))
        assert marker["stop_reason"] == "monitor_abort"
        assert marker["created_by"] == "smartrim.runmarker"
    # Sweep again: nothing left to close.
    assert runmarker.close_abandoned_runs() == []


def test_sweep_excludes_current_run():
    _make_run("run-913-adv")
    closed = runmarker.close_abandoned_runs(exclude="run-913-adv")
    assert closed == []
    assert not os.path.isfile(os.path.join(config.run_dir("run-913-adv"), "end.json"))


def test_evaluate_quarantines_inconclusive_runs():
    _make_run("run-920-adv", days_passed=11, finished=True)
    _make_run("run-921-adv", days_passed=5)
    runmarker.close_run("run-921-adv", stop_reason="manual_close")

    rows, excluded = evaluate._rows_from_dir(config.RUNTIME_DIR, None, None)
    assert [run_id for run_id, _ in excluded] == ["run-921-adv"]
    assert [reason for _, reason in excluded] == ["inconclusive"]
    assert [r["run_id"] for r in rows] == ["run-920-adv"]
    assert rows[0]["inconclusive"] is False
    assert rows[0]["protocol_ok"] is True

    rows, excluded = evaluate._rows_from_dir(config.RUNTIME_DIR, None, None,
                                             include_inconclusive=True)
    assert excluded == []
    assert {r["run_id"] for r in rows} == {"run-920-adv", "run-921-adv"}
    assert next(r for r in rows if r["run_id"] == "run-921-adv")["inconclusive"] is True


def test_evaluate_quarantines_protocol_mismatch():
    _make_run("run-940-adv", days_passed=11, finished=True)
    # Rewrite the definitive marker with the wrong storyteller.
    path = os.path.join(config.run_dir("run-940-adv"), "end.json")
    with open(path, encoding="utf-8") as fh:
        marker = json.load(fh)
    marker["protocol"] = {"storyteller": "Phoebe Chillax",
                          "difficulty": "Adventure story", "run_days": 11}
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(marker, fh)

    rows, excluded = evaluate._rows_from_dir(config.RUNTIME_DIR, None, None)
    assert ("run-940-adv", "protocol mismatch") in excluded
    assert [r["run_id"] for r in rows] == []

    rows, excluded = evaluate._rows_from_dir(config.RUNTIME_DIR, None, None,
                                             include_any_protocol=True)
    assert [r["run_id"] for r in rows] == ["run-940-adv"]
    assert rows[0]["protocol_ok"] is False


def test_evaluate_quarantines_missing_protocol_fingerprint():
    _make_run("run-941-adv", days_passed=11, finished=True)
    path = os.path.join(config.run_dir("run-941-adv"), "end.json")
    with open(path, encoding="utf-8") as fh:
        marker = json.load(fh)
    marker.pop("protocol", None)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(marker, fh)

    rows, excluded = evaluate._rows_from_dir(config.RUNTIME_DIR, None, None)
    assert ("run-941-adv", "protocol mismatch") in excluded


def test_cli_list_close_status(capsys):
    _make_run("run-930-adv")
    assert runmarker.main(["list"]) == 0
    assert "run-930-adv" in capsys.readouterr().out
    assert runmarker.main(["close", "run-930-adv", "--reason", "manual_close",
                           "--note", "test close"]) == 0
    assert runmarker.main(["status", "run-930-adv"]) == 0
    out = capsys.readouterr().out
    assert "manual_close" in out
    assert "inconclusive" in out
