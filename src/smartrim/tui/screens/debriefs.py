"""Debrief Viewer screen for the SmartRim TUI."""

from __future__ import annotations

from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, ScrollableContainer
from textual.widgets import Button, Input, Static

from smartrim import data as D


class DebriefScreen(ScrollableContainer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._filter_timer = None

    def compose(self) -> ComposeResult:
        yield Static("Debrief Viewer", classes="title")
        with Horizontal():
            yield Input(placeholder="Filter filename...", id="deb-filter")
            yield Button("Refresh", id="deb-refresh", variant="primary")
        yield Static("", id="deb-list")
        yield Static("", id="deb-content")

    def on_mount(self) -> None:
        self.refresh_data()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "deb-refresh":
            self.refresh_data()

    def on_input_changed(self, event: Input.Changed) -> None:
        if self._filter_timer is not None:
            try:
                self._filter_timer.stop()
            except Exception:
                pass
        self._filter_timer = self.set_timer(0.3, self._trigger_refresh)

    def _trigger_refresh(self) -> None:
        self._filter_timer = None
        self.refresh_data()

    def refresh_data(self) -> None:
        try:
            filt = self.query_one("#deb-filter", Input).value.strip().lower()
        except Exception:
            filt = ""
        self._load_debriefs(filt)

    @work(thread=True, exclusive=True)
    def _load_debriefs(self, filt: str) -> None:
        try:
            debriefs = D.load_debriefs()
        except Exception as e:
            self.app.call_from_thread(self._apply_error, f"Error loading debriefs: {e}")
            return
        if filt:
            debriefs = [d for d in debriefs if filt in d.get("filename", "").lower()]

        names = [d.get("filename", "?") for d in debriefs]
        content = ""
        if debriefs:
            try:
                content = debriefs[0].get("content", "")[:2000]
                if len(debriefs[0].get("content", "")) > 2000:
                    content += "\n\n[dim]... (truncated)[/dim]"
            except Exception:
                content = ""

        self.app.call_from_thread(self._apply, "\n".join(names) or "No debriefs.", content)

    def _apply(self, names: str, content: str) -> None:
        try:
            self.query_one("#deb-list", Static).update(names)
            self.query_one("#deb-content", Static).update(content)
        except Exception:
            pass

    def _apply_error(self, msg: str) -> None:
        try:
            self.query_one("#deb-list", Static).update(f"[red]{msg}[/red]")
            self.query_one("#deb-content", Static).update("")
        except Exception:
            pass