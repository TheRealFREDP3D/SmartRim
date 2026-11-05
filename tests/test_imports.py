"""Import smoke test: every module in src/smartrim must import cleanly.

Catches collapsed/corrupted modules (e.g. counselor.main_menu) and missing
dependencies early, without needing RimWorld or the MCP server.
"""

import importlib
import importlib.util
import pkgutil

import smartrim
import smartrim.cli


def _module_names():
    names = sorted(m.name for m in pkgutil.iter_modules(smartrim.__path__))
    # Optional extras: skip when their dependencies are not installed so a
    # clone with only `pip install -e ".[dev]"` still passes the core suite.
    if importlib.util.find_spec("textual") is None:
        names = [n for n in names if n != "tui"]
    dashboard_deps = ("pandas", "plotly", "streamlit")
    if any(importlib.util.find_spec(dep) is None for dep in dashboard_deps):
        names = [n for n in names if n != "dashboard"]
    return names


def test_all_modules_import():
    for name in _module_names():
        mod = importlib.import_module(f"smartrim.{name}")
        assert mod is not None


def test_optional_modules_skipped_when_deps_missing(monkeypatch):
    real = importlib.util.find_spec

    def fake(name, *args, **kwargs):
        if name in ("textual", "pandas", "plotly", "streamlit"):
            return None
        return real(name, *args, **kwargs)

    monkeypatch.setattr(importlib.util, "find_spec", fake)
    names = _module_names()
    assert "tui" not in names
    assert "dashboard" not in names


def test_cli_commands_callable():
    from smartrim import cli

    assert isinstance(cli.COMMANDS, dict)
    assert len(cli.COMMANDS) > 0
    for cmd, fn in cli.COMMANDS.items():
        assert callable(fn), f"command {cmd!r} is not callable"


def test_counselor_pause_exists():
    from smartrim import counselor

    assert hasattr(counselor, "pause")
    assert callable(counselor.pause)
    assert hasattr(counselor, "main_menu")
    assert callable(counselor.main_menu)
