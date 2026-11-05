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
    # tui is an optional extra (textual); skip when not installed so clones
    # without `pip install -e ".[tui]"` still pass the core suite.
    if importlib.util.find_spec("textual") is None:
        names = [n for n in names if n != "tui"]
    return names


def test_all_modules_import():
    for name in _module_names():
        mod = importlib.import_module(f"smartrim.{name}")
        assert mod is not None


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
