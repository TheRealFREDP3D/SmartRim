"""Run History screen for the SmartRim TUI."""

from __future__ import annotations

import contextlib

from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, ScrollableContainer
from textual.widgets import Button, Input, Static

from smartrim import data as D


def _sparkline(values: list[float]) -> str:
    if not values:
        return ""
    bars = "▁▂▃▄▅▆▇█"
    lo = min(values)
    hi = max(values)
    span = (hi - lo) or 1
    out = []
    for v in values:
        idx = int((v - lo) / span * (len(bars) - 1))
        idx = max(0, min(len(bars) - 1, idx))
        out.append(bars[idx])
    return "".join(out)


class RunsScreen(ScrollableContainer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._filter_timer = None

    def compose(self) -> ComposeResult:
        yield Static("Run History", classes="title")
        with Horizontal():
            yield Input(placeholder="Filter run_id...", id="run-filter")
            yield Button("Refresh", id="run-refresh", variant="primary")
        yield Static("", id="run-list")
        yield Static("", id="run-detail")

    def on_mount(self) -> None:
        self.refresh_data()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "run-refresh":
            self.refresh_data()

    def on_input_changed(self, event: Input.Changed) -> None:
        if self._filter_timer is not None:
            with contextlib.suppress(Exception):
                self._filter_timer.stop()
        self._filter_timer = self.set_timer(0.3, self._trigger_refresh)

    def _trigger_refresh(self) -> None:
        self._filter_timer = None
        self.refresh_data()

    def refresh_data(self) -> None:
        try:
            filt = self.query_one("#run-filter", Input).value.strip().lower()
        except Exception:
            filt = ""
        self._load_runs(filt)

    @work(thread=True, exclusive=True)
    def _load_runs(self, filt: str) -> None:
        try:
            runs = D.load_runs_metadata()
        except Exception as e:
            self.app.call_from_thread(self._apply_error, f"Error loading runs: {e}")
            return
        if filt:
            runs = [r for r in runs if filt in str(r.get("run_id", "")).lower()]

        lines = []
        for r in runs[:20]:
            lines.append(
                f"{r.get('run_id','?')}  arm={r.get('arm','?')}  days={r.get('days_passed','?')}  "
                f"alerts={r.get('urgent_alerts','?')}  pauses={r.get('auto_pauses','?')}"
            )

        detail = ""
        if runs:
            r = runs[0]
            rid = r.get("run_id")
            try:
                snaps = D.load_run_snapshots(rid)
            except Exception:
                snaps = []
            if snaps:
                try:
                    moods = []
                    foods = []
                    for s in snaps:
                        try:
                            moods.append(float((s.get("summary") or {}).get("min_mood") or 0))
                        except Exception:
                            moods.append(0.0)
                        try:
                            foods.append(float((s.get("summary") or {}).get("food_days") or 0))
                        except Exception:
                            foods.append(0.0)
                    detail = (
                        f"[b]Detail: {rid}[/b]\n"
                        f"mood: {_sparkline(moods)}  {moods[-1] if moods else '?'}\n"
                        f"food: {_sparkline(foods)}  {foods[-1] if foods else '?'}\n"
                        f"snapshots: {len(snaps)}"
                    )
                except Exception as e:
                    detail = f"[b]Detail: {rid}[/b]\nError building detail: {e}"
            else:
                detail = f"[b]Detail: {rid}[/b]\nNo snapshots."
        else:
            detail = ""

        self.app.call_from_thread(self._apply, "\n".join(lines) or "No runs.", detail)

    def _apply(self, runs_text: str, detail: str) -> None:
        try:
            self.query_one("#run-list", Static).update(runs_text)
            self.query_one("#run-detail", Static).update(detail)
        except Exception:
            pass

    def _apply_error(self, msg: str) -> None:
        try:
            self.query_one("#run-list", Static).update(f"[red]{msg}[/red]")
            self.query_one("#run-detail", Static).update("")
        except Exception:
            pass