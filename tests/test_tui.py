"""Smoke + pilot tests for the Textual TUI.

Gated behind ``pytest.importorskip('textual')`` so the core suite stays green
when the optional ``tui`` extra is not installed.
"""

import asyncio

import pytest

textual = pytest.importorskip("textual")

from smartrim.tui.app import SmartRimApp


def test_app_instantiates():
    app = SmartRimApp()
    assert app is not None


def test_pilot_runs():
    async def run():
        app = SmartRimApp()
        async with app.run_test() as pilot:
            await pilot.pause(0.2)
            await pilot.press("r")
            await pilot.pause(0.2)

    asyncio.run(run())