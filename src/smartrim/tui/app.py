"""Root Textual application for SmartRim."""

from __future__ import annotations

import os
from typing import ClassVar

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header, TabbedContent, TabPane

from smartrim.tui.screens.advice import AdviceScreen
from smartrim.tui.screens.command_center import CommandCenterScreen
from smartrim.tui.screens.debriefs import DebriefScreen
from smartrim.tui.screens.help import HelpScreen
from smartrim.tui.screens.lessons import LessonScreen
from smartrim.tui.screens.live_monitor import LiveMonitorScreen
from smartrim.tui.screens.runs import RunsScreen
from smartrim.tui.screens.timelapse import TimelapseScreen
from smartrim.tui.screens.workflow import WorkflowScreen


class SmartRimApp(App):
    CSS = """
    Screen {
        background: $background;
    }
    .title {
        text-style: bold;
        color: $accent;
        margin: 1 0;
    }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os.getenv("NO_COLOR"):
            self.ansi_color = False

    BINDINGS: ClassVar[list[Binding]] = [
        Binding("q", "quit", "Quit"),
        Binding("r", "refresh", "Refresh"),
        Binding("t", "toggle_theme", "Theme"),
        Binding("question_mark", "help", "Help"),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with TabbedContent():
            with TabPane("Command Center", id="tab-cc"):
                yield CommandCenterScreen()
            with TabPane("Live Monitor", id="tab-lm"):
                yield LiveMonitorScreen()
            with TabPane("Advice Browser", id="tab-adv"):
                yield AdviceScreen()
            with TabPane("Lesson Explorer", id="tab-les"):
                yield LessonScreen()
            with TabPane("Run History", id="tab-runs"):
                yield RunsScreen()
            with TabPane("Debrief Viewer", id="tab-deb"):
                yield DebriefScreen()
            with TabPane("Timelapse", id="tab-tl"):
                yield TimelapseScreen()
            with TabPane("Workflow", id="tab-wf"):
                yield WorkflowScreen()
        yield Footer()

    def action_refresh(self) -> None:
        for screen_cls in (
            CommandCenterScreen,
            LiveMonitorScreen,
            AdviceScreen,
            LessonScreen,
            RunsScreen,
            DebriefScreen,
            TimelapseScreen,
            WorkflowScreen,
        ):
            try:
                for widget in self.query(screen_cls):
                    if hasattr(widget, "refresh_data"):
                        widget.refresh_data()
                    elif hasattr(widget, "refresh_status"):
                        widget.refresh_status()
            except Exception:
                continue

    def action_toggle_theme(self) -> None:
        try:
            self.theme = "textual-light" if str(self.theme).startswith("textual-dark") else "textual-dark"
            self.notify(f"Theme: {self.theme}", title="SmartRim TUI")
        except Exception:
            pass

    def action_help(self) -> None:
        try:
            self.push_screen(HelpScreen())
        except Exception:
            pass


def main() -> int:
    app = SmartRimApp()
    app.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


def main() -> int:
    app = SmartRimApp()
    app.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


def main() -> int:
    app = SmartRimApp()
    app.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
