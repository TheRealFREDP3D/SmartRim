"""Command Center screen for the SmartRim TUI."""

from __future__ import annotations

import contextlib
import os
from datetime import datetime

from textual import work
from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Static

from smartrim import data as D


class CommandCenterScreen(ScrollableContainer):
    """Dense glanceable view mirroring the Streamlit Command Center."""

    def compose(self) -> ComposeResult:
        yield Static("SmartRim — Command Center", classes="title")
        yield Button("Refresh", id="refresh", variant="primary")
        yield Static("", id="alerts")
        yield Static("", id="colonists")
        yield Static("", id="resources")
        yield Static("", id="reflex")
        yield Static("", id="lessons")

    def on_mount(self) -> None:
        self.refresh_data()
        try:
            interval = int(os.getenv("TUI_REFRESH", "10"))
        except (TypeError, ValueError):
            interval = 10
        if interval > 0:
            self.set_interval(interval, self.refresh_data)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "refresh":
            self.refresh_data()

    @work(thread=True, exclusive=True)
    def refresh_data(self) -> None:
        try:
            game_state = D.get_live_game_state()
        except Exception:
            game_state = None
        try:
            alerts = D.load_current_alerts()
        except Exception:
            alerts = []
        try:
            colonists = D.game_colonists(game_state)
        except Exception:
            colonists = []
        try:
            resources_raw = D.fetch_resources()
            resources = (resources_raw or {}).get("resources", []) if isinstance(resources_raw, dict) else []
        except Exception:
            resources = []
        try:
            reflex = D.load_reflex_actions(3)
        except Exception:
            reflex = []
        try:
            lessons = [ls for ls in D.load_lessons() if ls.get("status", "active") == "active"]
        except Exception:
            lessons = []

        try:
            alert_lines = []
            urgent = [a for a in alerts if a.get("type") == "urgent"]
            warnings = [a for a in alerts if a.get("type") == "warning"]
            if urgent:
                for a in urgent[:4]:
                    alert_lines.append(f"[red]URGENT[/red] {a.get('message','')}")
            elif warnings:
                for a in warnings[:4]:
                    alert_lines.append(f"[yellow]WARN[/yellow] {a.get('message','')}")
            else:
                alert_lines.append("[green]All clear — no active alerts[/green]")
        except Exception:
            alert_lines = ["[yellow]Alerts unavailable[/yellow]"]

        try:
            colonist_lines = []
            for c in colonists[:8]:
                name = c.get("name", "?")
                mood = c.get("mood", 0)
                health = c.get("health", 0)
                job = c.get("job", "")
                downed = " [DOWNED]" if c.get("downed") else ""
                colonist_lines.append(f"{name}{downed}  mood {mood}%  hp {health}%  {job}")
            if not colonist_lines:
                colonist_lines.append("No colonist data.")
        except Exception:
            colonist_lines = ["Colonist data unavailable"]

        try:
            res_lines = []
            important = ["Meal", "Medicine", "Steel", "Wood", "Component", "Food", "Cloth", "Leather"]
            filtered = [r for r in resources if any(k.lower() in str(r.get("label", "")).lower() for k in important)]
            for r in filtered[:8]:
                res_lines.append(f"{r.get('label','?')}: {r.get('count',0)}")
            if not res_lines:
                res_lines = ["No resource data."]
        except Exception:
            res_lines = ["Resource data unavailable"]

        try:
            reflex_lines = []
            if reflex:
                ra = reflex[0]
                status = "dry-run" if ra.get("dry_run") else ("ok" if ra.get("success") else "failed")
                reflex_lines.append(f"Last: {ra.get('action','?')} — {status}")
                reflex_lines.append(f"Would: {ra.get('would_do', ra.get('message',''))}")
            else:
                reflex_lines.append("No reflex actions yet.")
            try:
                reflex_lines.append(
                    f"Reflex: {'enabled' if D.reflex_enabled() else 'disabled'} · "
                    f"{'dry-run' if D.reflex_dry_run() else 'LIVE writes'}"
                )
            except Exception:
                reflex_lines.append("Reflex: status unavailable")
        except Exception:
            reflex_lines = ["Reflex data unavailable"]

        try:
            lesson_lines = []
            lessons.sort(key=lambda x: (x.get("confidence") or 0), reverse=True)
            for ls in lessons[:5]:
                lesson_lines.append(f"{ls.get('id','?')} (conf {ls.get('confidence','?')}) {ls.get('title','')}")
            if not lesson_lines:
                lesson_lines.append("No active lessons.")
        except Exception:
            lesson_lines = ["Lessons unavailable"]

        self.app.call_from_thread(
            self._apply,
            {
                "alerts": "\n".join(alert_lines) or "No alerts.",
                "colonists": "\n".join(colonist_lines),
                "resources": "\n".join(res_lines),
                "reflex": "\n".join(reflex_lines),
                "lessons": "\n".join(lesson_lines),
            },
        )

    def _apply(self, data: dict) -> None:
        ts = datetime.now().strftime("%H:%M:%S")
        try:
            self.query_one("#alerts", Static).update(f"[b]Alerts[/b]  [dim]{ts}[/dim]\n{data['alerts']}")
            self.query_one("#colonists", Static).update(f"[b]Colonists[/b]\n{data['colonists']}")
            self.query_one("#resources", Static).update(f"[b]Resources[/b]\n{data['resources']}")
            self.query_one("#reflex", Static).update(f"[b]Reflex[/b]\n{data['reflex']}")
            self.query_one("#lessons", Static).update(f"[b]Lessons[/b]\n{data['lessons']}")
        except Exception as e:  # pragma: no cover - defensive
            with contextlib.suppress(Exception):
                self.app.notify(f"UI update failed: {e}", severity="error")
