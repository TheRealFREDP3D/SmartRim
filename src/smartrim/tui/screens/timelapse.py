"""Timelapse screen for the SmartRim TUI."""

from __future__ import annotations

import os

from textual import work
from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Static

from smartrim.config import RUN_ID


class TimelapseScreen(ScrollableContainer):
    def compose(self) -> ComposeResult:
        yield Static("Timelapse", classes="title")
        yield Button("Refresh", id="tl-refresh", variant="primary")
        yield Static("", id="tl-info")
        yield Static("", id="tl-frames")

    def on_mount(self) -> None:
        self.refresh_data()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "tl-refresh":
            self.refresh_data()

    @work(thread=True, exclusive=True)
    def refresh_data(self) -> None:
        try:
            from smartrim.timelapse import list_captures

            data = list_captures(RUN_ID)
            files = data.get("files", [])
            d = data.get("dir", "")
            info = f"Run: {data.get('run_id','?')}  Captures: {len(files)}  Dir: {d}"
            frames = "\n".join(files[-10:]) if files else "No captures yet."
            gif_path = os.path.join(d, "timelapse.gif") if d else ""
            if gif_path and os.path.exists(gif_path):
                frames += f"\nGIF: {gif_path}"
        except Exception as e:
            info = f"[red]Timelapse unavailable: {e}[/red]"
            frames = ""

        self.app.call_from_thread(self._apply, info, frames)

    def _apply(self, info: str, frames: str) -> None:
        try:
            self.query_one("#tl-info", Static).update(info)
            self.query_one("#tl-frames", Static).update(frames)
        except Exception:
            pass