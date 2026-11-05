"""Live Monitor screen for the SmartRim TUI."""

from __future__ import annotations

import os

from textual import work
from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Static

from smartrim import data as D


class LiveMonitorScreen(ScrollableContainer):
    def compose(self) -> ComposeResult:
        yield Static("Live Game Monitor", classes="title")
        yield Button("Refresh", id="lm-refresh", variant="primary")
        yield Static("", id="lm-status")
        yield Static("", id="lm-alerts")
        yield Static("", id="lm-colonists")
        yield Static("", id="lm-resources")

    def on_mount(self) -> None:
        self.refresh_data()
        try:
            interval = int(os.getenv("TUI_REFRESH", "10"))
        except (TypeError, ValueError):
            interval = 10
        if interval > 0:
            self.set_interval(interval, self.refresh_data)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "lm-refresh":
            self.refresh_data()

    @work(thread=True, exclusive=True)
    def refresh_data(self) -> None:
        try:
            game_state = D.get_live_game_state()
            alerts = D.load_current_alerts()
        except Exception as e:
            self.app.call_from_thread(self._apply_error, f"Error loading monitor data: {e}")
            return

        try:
            colonists_raw = D.fetch_colonists()
            colonists = (colonists_raw or {}).get("colonists", []) if isinstance(colonists_raw, dict) else []
        except Exception:
            colonists = []

        try:
            resources_raw = D.fetch_resources()
            resources = (resources_raw or {}).get("resources", []) if isinstance(resources_raw, dict) else []
        except Exception:
            resources = []

        status_lines = []
        if game_state:
            try:
                status_lines.append(
                    f"Connected · Day {game_state.get('daysPassed','?')} · "
                    f"Colonists {game_state.get('colonistCount','?')} · "
                    f"Wealth {game_state.get('wealthTotal','?')} · "
                    f"Difficulty {game_state.get('difficulty','?')}"
                )
            except Exception:
                status_lines.append("Connected (status details unavailable)")
        else:
            status_lines.append("[red]Game not connected[/red]")

        alert_lines = []
        try:
            for a in alerts[:8]:
                sev = a.get("type", "info")
                if sev == "urgent":
                    icon = "[red]!![/red]"
                elif sev == "warning":
                    icon = "[yellow]![/yellow]"
                else:
                    icon = "[blue]i[/blue]"
                alert_lines.append(f"{icon} {sev.upper()}: {a.get('message','')}")
        except Exception:
            alert_lines.append("[yellow]Alerts unavailable[/yellow]")

        colonist_lines = []
        try:
            for c in colonists[:12]:
                colonist_lines.append(
                    f"{c.get('name','?')}  age {c.get('age','?')}  mood {c.get('mood','?')}  "
                    f"hp {c.get('health','?')}  job {c.get('job','?')}"
                )
        except Exception:
            colonist_lines.append("Colonist data unavailable")

        res_lines = []
        try:
            for r in resources[:12]:
                res_lines.append(f"{r.get('label','?')}: {r.get('count','?')}")
        except Exception:
            res_lines.append("Resource data unavailable")

        self.app.call_from_thread(
            self._apply,
            {
                "status": "\n".join(status_lines),
                "alerts": "\n".join(alert_lines) or "No alerts.",
                "colonists": "\n".join(colonist_lines) or "No colonist data.",
                "resources": "\n".join(res_lines) or "No resource data.",
            },
        )

    def _apply(self, data: dict) -> None:
        try:
            self.query_one("#lm-status", Static).update(f"[b]Status[/b]\n{data['status']}")
            self.query_one("#lm-alerts", Static).update(f"[b]Alerts[/b]\n{data['alerts']}")
            self.query_one("#lm-colonists", Static).update(f"[b]Colonists[/b]\n{data['colonists']}")
            self.query_one("#lm-resources", Static).update(f"[b]Resources[/b]\n{data['resources']}")
        except Exception:
            pass

    def _apply_error(self, msg: str) -> None:
        try:
            self.query_one("#lm-status", Static).update(f"[b]Status[/b]\n[red]{msg}[/red]")
            self.query_one("#lm-alerts", Static).update("[b]Alerts[/b]\n")
            self.query_one("#lm-colonists", Static).update("[b]Colonists[/b]\n")
            self.query_one("#lm-resources", Static).update("[b]Resources[/b]\n")
        except Exception:
            pass