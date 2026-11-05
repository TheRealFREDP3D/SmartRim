"""Advice Browser screen for the SmartRim TUI."""

from __future__ import annotations

from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, ScrollableContainer
from textual.widgets import Button, Input, Static

from smartrim import data as D


class AdviceScreen(ScrollableContainer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._filter_timer = None

    def compose(self) -> ComposeResult:
        yield Static("Advice Browser", classes="title")
        with Horizontal():
            yield Input(placeholder="Filter (severity/run/status)...", id="adv-filter")
            yield Button("Refresh", id="adv-refresh", variant="primary")
        yield Static("", id="adv-count")
        yield Static("", id="adv-list")

    def on_mount(self) -> None:
        self.refresh_data()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "adv-refresh":
            self.refresh_data()

    def on_input_changed(self, event: Input.Changed) -> None:
        # Debounce filter input
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
            filt = self.query_one("#adv-filter", Input).value.strip().lower()
        except Exception:
            filt = ""
        self._load_advice(filt)

    @work(thread=True, exclusive=True)
    def _load_advice(self, filt: str) -> None:
        try:
            advice = D.load_all_advice()
        except Exception as e:
            self.app.call_from_thread(self._apply_error, f"Error loading advice: {e}")
            return
        if filt:
            advice = [
                a
                for a in advice
                if filt in str(a.get("severity", "")).lower()
                or filt in str(a.get("run_id", "")).lower()
                or filt in str(a.get("status", "")).lower()
                or filt in str(a.get("situation", "")).lower()
                or filt in str(a.get("trigger", "")).lower()
            ]
        advice = sorted(advice, key=lambda x: x.get("timestamp", ""), reverse=True)[:50]

        lines = []
        for a in advice:
            sit = str(a.get("situation", ""))
            if len(sit) > 80:
                sit = sit[:77] + "..."
            lines.append(
                f"[{a.get('timestamp','')[:16]}] {str(a.get('severity','')).upper()} "
                f"{a.get('trigger','')} — {sit}"
            )

        self.app.call_from_thread(self._apply, len(advice), "\n".join(lines) or "No advice records.")

    def _apply(self, count: int, text: str) -> None:
        try:
            self.query_one("#adv-count", Static).update(f"Records: {count}")
            self.query_one("#adv-list", Static).update(text)
        except Exception:
            pass

    def _apply_error(self, msg: str) -> None:
        try:
            self.query_one("#adv-count", Static).update("[red]Error[/red]")
            self.query_one("#adv-list", Static).update(f"[red]{msg}[/red]")
        except Exception:
            pass