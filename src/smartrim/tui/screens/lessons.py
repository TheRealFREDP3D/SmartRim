"""Lesson Explorer screen for the SmartRim TUI."""

from __future__ import annotations

import contextlib

from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, ScrollableContainer
from textual.widgets import Button, Input, Static

from smartrim import data as D


class LessonScreen(ScrollableContainer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._filter_timer = None

    def compose(self) -> ComposeResult:
        yield Static("Lesson Explorer", classes="title")
        with Horizontal():
            yield Input(placeholder="Filter (status/tag)...", id="les-filter")
            yield Button("Refresh", id="les-refresh", variant="primary")
        yield Static("", id="les-count")
        yield Static("", id="les-list")

    def on_mount(self) -> None:
        self.refresh_data()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "les-refresh":
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
            filt = self.query_one("#les-filter", Input).value.strip().lower()
        except Exception:
            filt = ""
        self._load_lessons(filt)

    @work(thread=True, exclusive=True)
    def _load_lessons(self, filt: str) -> None:
        try:
            lessons = D.load_lessons()
        except Exception as e:
            self.app.call_from_thread(self._apply_error, f"Error loading lessons: {e}")
            return
        if filt:
            lessons = [
                ls
                for ls in lessons
                if filt in str(ls.get("status", "")).lower()
                or filt in " ".join(ls.get("tags") or []).lower()
                or filt in str(ls.get("title", "")).lower()
                or filt in str(ls.get("id", "")).lower()
            ]
        lessons.sort(key=lambda x: (x.get("confidence") or 0), reverse=True)

        lines = []
        for ls in lessons[:40]:
            lines.append(
                f"{ls.get('id','?')} [{ls.get('status','?')}] conf {ls.get('confidence','?')} "
                f"{ls.get('title','')}"
            )

        self.app.call_from_thread(self._apply, len(lessons), "\n".join(lines) or "No lessons.")

    def _apply(self, count: int, text: str) -> None:
        try:
            self.query_one("#les-count", Static).update(f"Lessons: {count}")
            self.query_one("#les-list", Static).update(text)
        except Exception:
            pass

    def _apply_error(self, msg: str) -> None:
        try:
            self.query_one("#les-count", Static).update("[red]Error[/red]")
            self.query_one("#les-list", Static).update(f"[red]{msg}[/red]")
        except Exception:
            pass