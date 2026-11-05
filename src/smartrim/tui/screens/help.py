"""Help overlay for the SmartRim TUI."""

from __future__ import annotations

from typing import ClassVar

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import ScrollableContainer
from textual.screen import Screen
from textual.widgets import Static


class HelpScreen(Screen):
    BINDINGS: ClassVar[list[Binding]] = [
        Binding("escape", "pop_screen", "Close"),
        Binding("q", "pop_screen", "Close"),
    ]

    def compose(self) -> ComposeResult:
        with ScrollableContainer():
            yield Static(
                "[b]SmartRim TUI — Help[/b]\n\n"
                "Navigation:\n"
                "  Tab / Shift+Tab  Switch tabs\n\n"
                "Global keys:\n"
                "  r   Refresh all views\n"
                "  t   Toggle dark/light theme\n"
                "  ?   Show this help\n"
                "  q   Quit\n\n"
                "Filters (Advice/Lessons/Runs/Debriefs):\n"
                "  Type to filter; cleared by deleting text.\n\n"
                "Notes:\n"
                "  Auto-refresh every TUI_REFRESH seconds (default 10; 0 = manual).\n"
                "  Set NO_COLOR=1 to disable color output.\n",
                markup=True,
            )

    def action_pop_screen(self) -> None:
        self.app.pop_screen()
