"""Shared pytest setup.

The suite must never write into the repository's ``memory/`` or ``runtime/``
trees. Every test gets a private runtime root (control/ + one run dir) and the
modules that cache path constants are pointed at it.

Tests may still override individual paths; this is only the default.
"""

import pytest

from smartrim import advice_log, config, debrief_llm, monitor, outcomes, quests, timelapse


@pytest.fixture(autouse=True)
def isolate_runtime(tmp_path, monkeypatch):
    runtime = tmp_path / "runtime"
    control = runtime / "control"
    control.mkdir(parents=True)

    paths = {
        "RUNTIME_DIR": runtime,
        "CONTROL_DIR": control,
        "ACTIVE_RUN_FILE": control / "active.json",
        "MONITOR_PID_FILE": control / "monitor.pid",
        "MONITOR_LOG_FILE": control / "monitor.log",
        "MONITOR_ERR_LOG_FILE": control / "monitor.err.log",
        "MONITOR_STARTUP_LOCK": control / "monitor.startup.lock",
        "REFLEX_LOCK_FILE": control / "reflex.lock",
        "REFLEX_PAUSE_FILE": control / "reflex_pause.json",
        "HUMAN_ACTION_FILE": control / "last_human_action.json",
        "WATCHDOG_STOP_FILE": control / "monitor.watchdog.stop",
        "WATCHDOG_LOG_FILE": control / "monitor.watchdog.log",
    }
    for name, value in paths.items():
        monkeypatch.setattr(config, name, str(value))

    # Modules that captured a path constant at import time.
    monkeypatch.setattr(monitor, "PID_FILE", str(control / "monitor.pid"))
    # outcomes writes the lesson store; never point it at the tracked file.
    monkeypatch.setattr(outcomes, "LESSONS_FILE", str(runtime / "lessons.jsonl"))

    # Per-module overrides default to "resolve from config".
    for module, attr in (
        (advice_log, "ADVICE_DIR"),
        (advice_log, "ADVICE_FILE"),
        (quests, "DEFAULT_REGISTRY"),
        (timelapse, "TIMELAPSE_DIR"),
        (debrief_llm, "DEBRIEFS_DIR"),
    ):
        monkeypatch.setattr(module, attr, None)

    # Force run resolution to use the isolated runtime root.
    monkeypatch.delenv("RUN_ID", raising=False)
    monkeypatch.setattr(config, "RUN_ID", config.UNSET_RUN_ID)

    yield tmp_path
