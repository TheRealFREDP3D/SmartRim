"""Workflow and Operations screen for the SmartRim TUI.

Start/stop Monitor & Ollama, run debrief commands, and show
process/memory status.
"""

from __future__ import annotations

import contextlib
import os
import subprocess
import sys
from pathlib import Path

from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.widgets import Button, Static

from smartrim import data as D
from smartrim.config import BASE_DIR, MONITOR_PID_FILE, resolve_run_id


class WorkflowScreen(ScrollableContainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.monitor_running = False
        self.ollama_running = False

    # --- process helpers (cross-platform, PID-file aware) -----------------
    @staticmethod
    def _pid_file() -> Path:
        return Path(MONITOR_PID_FILE)

    def _monitor_pid(self) -> int | None:
        pf = self._pid_file()
        if not pf.exists():
            return None
        try:
            pid = int((pf.read_text(encoding="utf-8") or "").strip())
        except (ValueError, OSError):
            return None
        return pid if pid > 0 else None

    def _proc_alive(self, pid: int) -> bool:
        try:
            if sys.platform == "win32":
                import ctypes

                HANDLE = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)
                if HANDLE:
                    ctypes.windll.kernel32.CloseHandle(HANDLE)
                    return True
                return False
            os.kill(pid, 0)
            return True
        except Exception:
            return False

    def _proc_cmdline(self, pid: int) -> str:
        try:
            if sys.platform == "win32":
                out = subprocess.run(
                    ["wmic", "process", "where", f"ProcessId={pid}", "get", "CommandLine", "/format:value"],
                    capture_output=True,
                    text=True,
                    timeout=5,
                    creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
                )
                return out.stdout or ""
            out = subprocess.run(
                ["ps", "-p", str(pid), "-o", "command="],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return out.stdout or ""
        except Exception:
            return ""

    def _is_monitor_pid(self, pid: int | None) -> bool:
        """True if pid is alive and its cmdline contains smartrim.monitor."""
        if not pid:
            return False
        if not self._proc_alive(pid):
            return False
        return "smartrim.monitor" in self._proc_cmdline(pid)

    def _stop_monitor(self, label: str) -> None:
        self._log(f"[{label}] Stopping monitor via PID file…")
        pid = self._monitor_pid()
        if pid is None:
            self._log(f"[{label}] No PID file — monitor not running")
            return
        if not self._proc_alive(pid):
            self._log(f"[{label}] Stale PID file (PID {pid} not alive) — removing")
            with contextlib.suppress(OSError):
                self._pid_file().unlink()
            return
        if "smartrim.monitor" not in self._proc_cmdline(pid):
            self._log(f"[{label}] PID {pid} is not a SmartRim monitor — refusing to kill")
            return
        try:
            import signal

            os.kill(pid, signal.SIGTERM)
            self._log(f"[{label}] Sent SIGTERM to PID {pid}")
            # Verify, then clean PID file if still ours
            try:
                cur = int((self._pid_file().read_text(encoding="utf-8") or "").strip())
            except Exception:
                cur = None
            if cur == pid:
                with contextlib.suppress(OSError):
                    self._pid_file().unlink()
        except Exception as e:
            self._log(f"[{label}] Error stopping monitor: {e}")

    def _ollama_alive(self) -> bool:
        # Use HTTP probe (works on all platforms) instead of tasklist.
        try:
            import urllib.request

            with urllib.request.urlopen("http://127.0.0.1:11434/api/version", timeout=2) as r:
                return bool(r.status and r.status < 500)
        except Exception:
            return False

    def compose(self) -> ComposeResult:
        yield Static("Workflow and Operations", classes="title")
        yield Static("", id="wf-status")
        with Horizontal():
            with Vertical(id="col-monitor"):
                yield Static("[b]Monitor[/b]")
                yield Button("Start Monitor", id="wf-start-mon", variant="primary")
                yield Static("  Start the polling monitor")
                yield Button("Stop Monitor", id="wf-stop-mon", variant="error")
                yield Static("  Stop the running monitor")
            with Vertical(id="col-ollama"):
                yield Static("[b]Ollama[/b]")
                yield Button("Start Ollama", id="wf-start-ollama", variant="primary")
                yield Static("  Start local LLM server")
                yield Button("Stop Ollama", id="wf-stop-ollama", variant="error")
                yield Static("  Stop the Ollama server")
        yield Static("[b]Debrief & Lessons[/b]")
        yield Button("Create Debrief Bundle", id="wf-bundle")
        yield Static("  Bundle the current run for LLM review")
        yield Button("Debrief Latest", id="wf-debrief")
        yield Static("  Run debrief on the current run")
        yield Button("Add Lessons from Response", id="wf-lessons")
        yield Static("  Extract lessons from debrief response")
        yield Button("Refresh Status", id="wf-refresh")
        yield Static("  Update process and memory status")
        yield Static("", id="wf-log")

    def on_mount(self) -> None:
        self.refresh_status()

    def _update_button_styles(self) -> None:
        try:
            start_mon = self.query_one("#wf-start-mon", Button)
            stop_mon = self.query_one("#wf-stop-mon", Button)
            start_oll = self.query_one("#wf-start-ollama", Button)
            stop_oll = self.query_one("#wf-stop-ollama", Button)
            start_mon.variant = "success" if self.monitor_running else "primary"
            stop_mon.variant = "error" if self.monitor_running else "default"
            start_oll.variant = "success" if self.ollama_running else "primary"
            stop_oll.variant = "error" if self.ollama_running else "default"
        except Exception:
            pass

    def on_button_pressed(self, event: Button.Pressed) -> None:
        bid = event.button.id
        if bid == "wf-refresh":
            self.refresh_status()
            return
        if bid == "wf-start-mon":
            self.run_cmd("Start Monitor", ["powershell", "-ExecutionPolicy", "Bypass", "-File", "start-monitor.ps1"], background=True)
            return
        if bid == "wf-stop-mon":
            # PID-file aware stop — never taskkill all python.exe
            self._stop_monitor_cmd("Stop Monitor")
            return
        if bid == "wf-start-ollama":
            self.run_cmd("Start Ollama", ["ollama", "serve"], background=True)
            return
        if bid == "wf-stop-ollama":
            self._stop_ollama_cmd("Stop Ollama")
            return
        if bid == "wf-bundle":
            self._run_for_active_run("Create Bundle", lambda rid: [sys.executable, "-m", "smartrim.debrief_bundle", rid])
            return
        if bid == "wf-debrief":
            self._run_for_active_run("Debrief", lambda rid: [sys.executable, "-m", "smartrim.debrief_llm", "--run", rid])
            return
        if bid == "wf-lessons":
            self.run_cmd("Add Lessons", [sys.executable, "-m", "smartrim.debrief", "add-lessons"])
            return

    @work(thread=True)
    def _run_for_active_run(self, label: str, build_cmd) -> None:
        """Run a per-run command only when a concrete run id exists."""
        rid = resolve_run_id()
        if not rid:
            self.app.call_from_thread(self._log, f"[{label}] No active run — start the monitor first")
            return
        self.run_cmd(label, build_cmd(rid))

    @work(thread=True)
    def _stop_monitor_cmd(self, label: str) -> None:
        self._stop_monitor(label)
        self.app.call_from_thread(self.refresh_status)

    @work(thread=True)
    def _stop_ollama_cmd(self, label: str) -> None:
        self._log(f"[{label}] Stopping Ollama…")
        if sys.platform == "win32":
            # Kill only the ollama.exe process (not python) — scoped, not broad.
            try:
                proc = subprocess.run(
                    ["taskkill", "/T", "/F", "/IM", "ollama.exe"],
                    capture_output=True,
                    text=True,
                    timeout=10,
                    creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
                )
                if proc.returncode == 0:
                    self.app.call_from_thread(self._log, f"[{label}] Done (rc=0)")
                else:
                    self.app.call_from_thread(self._log, f"[{label}] Done (rc={proc.returncode}) — {proc.stderr.strip()[:200]}")
            except Exception as e:
                self.app.call_from_thread(self._log, f"[{label}] Error: {e}")
        else:
            # POSIX: pkill ollama — scoped by exact name
            try:
                proc = subprocess.run(["pkill", "-x", "ollama"], capture_output=True, text=True, timeout=10)
                self.app.call_from_thread(self._log, f"[{label}] Done (rc={proc.returncode})")
            except Exception as e:
                self.app.call_from_thread(self._log, f"[{label}] Error: {e}")
        self.app.call_from_thread(self.refresh_status)

    @work(thread=True)
    def run_cmd(self, label: str, cmd: list, check: bool = True, background: bool = False) -> None:
        self.app.call_from_thread(self._log, "[" + label + "] Running: " + " ".join(map(str, cmd)))
        try:
            if background:
                if sys.platform == "win32":
                    subprocess.Popen(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE | 0x00000200, cwd=BASE_DIR)
                else:
                    subprocess.Popen(cmd, cwd=BASE_DIR)
                self.app.call_from_thread(self._log, "[" + label + "] Started in background")
                return
            proc = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True, timeout=600)
            if proc.stdout:
                for line in proc.stdout.strip().splitlines()[-30:]:
                    self.app.call_from_thread(self._log, "  " + line)
            if proc.stderr:
                for line in proc.stderr.strip().splitlines()[-15:]:
                    self.app.call_from_thread(self._log, "  [err] " + line)
            self.app.call_from_thread(self._log, "[" + label + "] Done (rc=" + str(proc.returncode) + ")")
        except subprocess.TimeoutExpired:
            self.app.call_from_thread(self._log, "[" + label + "] Timed out")
        except Exception as e:
            self.app.call_from_thread(self._log, "[" + label + "] Error: " + str(e))
        self.app.call_from_thread(self.refresh_status)

    @work(thread=True)
    def refresh_status(self) -> None:
        status_lines = []
        monitor_running = False
        ollama_running = False

        # --- Monitor: PID-file + cmdline verification (honest, cross-platform)
        try:
            pid = self._monitor_pid()
            if pid is None:
                status_lines.append("[red]Monitor:[/red] not running (no PID file)")
            elif self._is_monitor_pid(pid):
                status_lines.append(f"[green]Monitor:[/green] running (PID {pid})")
                monitor_running = True
            elif self._proc_alive(pid):
                status_lines.append(f"[yellow]Monitor:[/yellow] PID {pid} alive but not smartrim.monitor — stale file")
            else:
                status_lines.append(f"[red]Monitor:[/red] stale PID file (PID {pid} not alive)")
        except Exception:
            status_lines.append("[dim]Monitor check unavailable[/dim]")

        # --- Ollama: HTTP probe (cross-platform, no tasklist)
        try:
            if self._ollama_alive():
                status_lines.append("[green]Ollama:[/green] running")
                ollama_running = True
            else:
                status_lines.append("[red]Ollama:[/red] not running")
        except Exception:
            status_lines.append("[dim]Ollama check unavailable[/dim]")

        self.monitor_running = monitor_running
        self.ollama_running = ollama_running

        # --- Memory counts via shared data.py (BASE_DIR-correct, not cwd)
        try:
            runs = D.load_runs_metadata()
            status_lines.append("[blue]Runs:[/blue] " + str(len(runs)) + " end files")
        except Exception:
            pass
        try:
            advice = D.load_all_advice()
            status_lines.append("[blue]Advice:[/blue] " + str(len(advice)) + " records")
        except Exception:
            pass
        try:
            lessons = D.load_lessons()
            status_lines.append("[blue]Lessons:[/blue] " + str(len(lessons)) + " entries")
        except Exception:
            pass
        try:
            debriefs = D.load_debriefs()
            bundles = sum(1 for d in debriefs if ".bundle." in d.get("filename", ""))
            responses = sum(1 for d in debriefs if ".response." in d.get("filename", ""))
            total = len(debriefs)
            status_lines.append("[blue]Debriefs:[/blue] " + f"{bundles} bundles / {responses} responses ({total} total)")
        except Exception:
            pass

        self.app.call_from_thread(self._apply_status, "\n".join(status_lines))

    def _apply_status(self, text: str) -> None:
        try:
            self.query_one("#wf-status", Static).update("[b]Status[/b]\n" + text)
            self._update_button_styles()
        except Exception:
            pass

    def _log(self, msg: str) -> None:
        try:
            log = self.query_one("#wf-log", Static)
            current = str(log.renderable)
            if current.strip():
                log.update(current + "\n" + msg)
            else:
                log.update(msg)
        except Exception:
            pass
