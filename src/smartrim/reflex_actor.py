"""Layer 2 reflex actor: whitelisted, guarded, audited in-game actions.

Consumes alerts (from ``monitor.run_reflex_checks``), a situation
(``situation.build_situation``) and game state (``counselor.game_state``), and
issues whitelisted state changes via ``counselor``. Ships in
``dry_run: true`` by default: no MCP write calls, audit records written to
``runtime/<run>/actions.jsonl``, intent logged via ``counselor.say``.

Safety order per action:
REFLEX_KILL -> REFLEX_PAUSE (one in-game day) -> REFLEX_LOCK (PID file) ->
human-action window (60s) -> preconditions -> dry-run -> say intent -> execute
-> audit record. The monitor's ``advice_log`` and ``auto_pauses`` counters are
never touched; outcomes are closed by reusing ``outcomes._close_advice``.
"""

import json
import os
import re
from contextlib import suppress
from datetime import datetime, timedelta

from smartrim import config, counselor
from smartrim.config import UNSET_RUN_ID
from smartrim.logging_config import get_logger
from smartrim.reflex_preconditions import PRECONDITIONS

try:
    from smartrim import outcomes
except ImportError:  # pragma: no cover - outcomes always present in this repo
    outcomes = None

try:
    from smartrim.monitor import _pid_alive
except ImportError:  # pragma: no cover - monitor always present in this repo
    _pid_alive = None

logger = get_logger(__name__)

# Control files live in runtime/control so the CLI can find them without a run id.
# Per-run audit ledgers live in runtime/<run_id>/. None means "resolve from config".
ACTIONS_FILE: str | None = None
HUMAN_ACTION_FILE: str | None = None
REFLEX_LOCK_FILE: str | None = None
REFLEX_PAUSE_FILE: str | None = None
REFLEX_ACTIONS_FILE: str = config.REFLEX_ACTIONS_FILE


def _actions_file() -> str | None:
    return ACTIONS_FILE or config.actions_file(create=True)


def _human_action_file() -> str | None:
    return HUMAN_ACTION_FILE or config.HUMAN_ACTION_FILE


def _lock_file() -> str:
    return REFLEX_LOCK_FILE or config.REFLEX_LOCK_FILE


def _pause_file() -> str:
    return REFLEX_PAUSE_FILE or config.REFLEX_PAUSE_FILE

ENV_KILL = "REFLEX_KILL"
ENV_DRY_RUN = "REFLEX_DRY_RUN"
ENV_PAUSE = "REFLEX_PAUSE"

HUMAN_WINDOW_SECONDS = 60

# How long an action that already ran for the same situation stays quiet. Keeps
# idempotent maintain-actions from repeating their in-game say every poll.
ATTEMPT_COOLDOWN_SECONDS = int(os.getenv("REFLEX_COOLDOWN_SECONDS", "600"))

EXECUTE_ACTIONS = (
    "draft_and_focus_fire", "designate_firefighting", "assign_beds",
    "rescue_downed", "prioritize_treatment", "ensure_food_supply",
    "set_research_project",
)

FOOD_CROPS = ("rice", "potato", "corn", "pumpkin")


def _env_flag(name, default="1"):
    return os.getenv(name, default) == "1"


def _now():
    return datetime.now().isoformat()


def _load_yaml_file(path):
    """Load a YAML file, falling back to a small built-in parser when PyYAML is unavailable."""
    try:
        import yaml  # type: ignore

        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except ImportError:
        pass
    except (OSError, yaml.YAMLError):
        return None
    with open(path, encoding="utf-8") as f:
        return _parse_simple_yaml(f.read())


def _parse_simple_yaml(text):
    """Minimal indentation-based parser for the reflex_actions.yaml subset.

    Handles scalar mappings, inline lists ([a, b]), and block lists (- item)
    with nested mappings. Enough for the v1 whitelist schema.
    """

    def parse_scalar(raw):
        raw = raw.strip()
        if (raw.startswith('"') and raw.endswith('"')) or (
            raw.startswith("'") and raw.endswith("'")
        ):
            return raw[1:-1]
        return raw

    def parse_inline_list(raw):
        raw = raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            if not inner:
                return []
            return [parse_scalar(item) for item in inner.split(",")]
        return [parse_scalar(raw)]

    lines = [
        (len(line) - len(line.lstrip(" ")), line.rstrip())
        for line in text.splitlines()
        if line.strip() and not line.lstrip(" ").startswith("#")
    ]

    def parse_block(start_index, indent):
        """Parse a mapping or list block at ``indent`` starting at lines[start_index]."""
        if start_index >= len(lines):
            return {}, start_index
        first_indent, first_line = lines[start_index]
        if first_indent != indent or first_line.lstrip().startswith("- "):
            return parse_list_block(start_index, indent)
        mapping = {}
        index = start_index
        while index < len(lines):
            cur_indent, line = lines[index]
            if cur_indent != indent:
                break
            key, sep, value = line.partition(":")
            if not sep:
                break
            key = key.strip()
            value = value.strip()
            index += 1
            if value:
                mapping[key] = parse_inline_list(value) if value.startswith("[") else parse_scalar(value)
            else:
                # Nested block: list or mapping at deeper indent.
                if index < len(lines) and lines[index][0] > indent:
                    if lines[index][1].lstrip().startswith("- "):
                        child, index = parse_list_block(index, lines[index][0])
                    else:
                        child, index = parse_block(index, lines[index][0])
                    mapping[key] = child
        return mapping, index

    def parse_list_block(start_index, indent):
        items = []
        index = start_index
        while index < len(lines):
            cur_indent, line = lines[index]
            if cur_indent != indent or not line.lstrip().startswith("- "):
                break
            body = line.lstrip()[2:].strip()
            index += 1
            if ":" in body:
                key, _, value = body.partition(":")
                item = {key.strip(): parse_inline_list(value) if value.startswith("[") else parse_scalar(value)}
                if index < len(lines) and lines[index][0] > indent:
                    child_indent = lines[index][0]
                    if lines[index][1].lstrip().startswith("- "):
                        child, index = parse_list_block(index, child_indent)
                    else:
                        child, index = parse_block(index, child_indent)
                    item.update(child)
                items.append(item)
            else:
                items.append(parse_inline_list(body)[0] if body.startswith("[") else parse_scalar(body))
                while index < len(lines) and lines[index][0] > indent:
                    if lines[index][1].lstrip().startswith("- "):
                        child, index = parse_list_block(index, lines[index][0])
                        items.append(child)
                    else:
                        child, index = parse_block(index, lines[index][0])
                        items.append(child)
        return items, index

    data, _ = parse_block(0, 0)
    return data


class ReflexAction:
    """One whitelisted reflex action loaded from memory/reflex_actions.yaml."""

    def __init__(self, aid, action_type, label_contains=None, category=None,
                 dry_run=True, kill_switch_env=ENV_KILL, preconditions=None):
        self.id = aid
        self.action_type = action_type
        self.label_contains = list(label_contains or [])
        self.category = category
        self.dry_run = bool(dry_run)
        self.kill_switch_env = kill_switch_env
        self.preconditions = list(preconditions or [])

    def matches(self, alert):
        """True if this action's alert_match matches the alert (label/category)."""
        if not isinstance(alert, dict):
            return False
        text = " ".join(str(alert.get(k) or "") for k in ("label", "message")).lower()
        if self.label_contains and not any(
            kw.lower() in text for kw in self.label_contains
        ):
            return False
        return not (
            self.category is not None
            and alert.get("category") != self.category
        )

    def precondition_fns(self):
        return [PRECONDITIONS[name] for name in self.preconditions if name in PRECONDITIONS]


def load_reflex_actions(path=REFLEX_ACTIONS_FILE):
    """Load the whitelist from disk. Empty list when the file is missing/invalid."""
    try:
        data = _load_yaml_file(path)
    except (OSError, ValueError):
        data = None
    actions = []
    if not isinstance(data, dict):
        return actions
    for item in data.get("reflex_actions") or []:
        if not isinstance(item, dict):
            continue
        am = item.get("alert_match") or {}
        actions.append(
            ReflexAction(
                aid=item.get("id", ""),
                action_type=item.get("action_type", ""),
                label_contains=list(am.get("label_contains") or []),
                category=am.get("category"),
                dry_run=bool(item.get("dry_run", True)),
                kill_switch_env=item.get("kill_switch_env", ENV_KILL),
                preconditions=list(item.get("preconditions") or []),
            )
        )
    return actions


def _read_jsonl(path):
    if not path or not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def _write_jsonl(path, records):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(json.dumps(rec, default=str) + "\n" for rec in records)


def _append_jsonl(path, record):
    if not path:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, default=str) + "\n")


def _alert_id(alert):
    if not isinstance(alert, dict):
        return "unknown"
    return f"{alert.get('category','')}|{alert.get('label') or alert.get('message') or ''}"


_NUMBERS = re.compile(r"\d+(?:\.\d+)?")


def _normalized_alert_id(alert_id):
    """Collapse volatile counts so 'Food stock low (17 units)' matches '(12 units)'."""
    return _NUMBERS.sub("#", str(alert_id or "").lower()).strip()


def _with_alert(game_state, alert):
    """Return a game_state whose alerts include the alert that triggered the action.

    The monitor derives some alerts itself (food stock, mood, medicine) instead of
    reading them from the game, so they never appear in ``game_state['alerts']``.
    Preconditions must still see them, otherwise an action matches its alert but
    fails its own precondition over and over.
    """
    if not isinstance(game_state, dict):
        return {"alerts": [alert]}
    alerts = list(game_state.get("alerts") or [])
    alerts.append(alert)
    return {**game_state, "alerts": alerts}


class ReflexActor:
    """Evaluate and execute whitelisted reflex actions."""

    def __init__(self, run_id=None, actions_path=None,
                 actions_file=None, human_action_file=None,
                 lock_file=None, pause_file=None,
                 counselor_mod=None):
        self.run_id = run_id or os.getenv("RUN_ID", UNSET_RUN_ID)
        self.actions_path = actions_path or REFLEX_ACTIONS_FILE
        self.actions_file = actions_file or _actions_file()
        self.human_action_file = human_action_file or _human_action_file()
        self.lock_file = lock_file or _lock_file()
        self.pause_file = pause_file or _pause_file()
        self.counselor = counselor_mod or counselor
        self.actions = load_reflex_actions(self.actions_path)
        # Why the last execute failed/no-op; recorded in the audit trail.
        self.last_error: str | None = None

    def rebind_run(self, run_id):
        """Point the actor at a run the monitor allocated *after* import.

        The actions audit path is resolved at import time from the active-run
        pointer, which still names the previous run, so without this the actor
        records this run's actions into the previous run's directory.
        """
        self.run_id = run_id
        self.actions_file = _actions_file()
        return self.actions_file

    # --- guards ---------------------------------------------------------

    def _paused(self, current_day):
        if not _env_flag(ENV_PAUSE, "1"):
            return False
        if not os.path.exists(self.pause_file):
            return False
        try:
            with open(self.pause_file, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError):
            # Fail closed: treat malformed file as paused
            return True
        # Ensure data is an object, not a scalar or array
        if not isinstance(data, dict):
            return True
        day = data.get("day")
        if day is None:
            return True  # indefinite pause, cleared by `reflex resume`
        if current_day is not None and str(day) != str(current_day):
            # Day rolled: one in-game day elapsed, clear the pause only if
            # the file still contains the same data we just read.
            try:
                with open(self.pause_file, encoding="utf-8") as f:
                    current_data = json.load(f)
                # Verify the file still contains the exact record we read
                if isinstance(current_data, dict) and current_data == data:
                    with suppress(OSError):
                        os.remove(self.pause_file)
                    return False
                # File was modified after our read - fail closed
                return True
            except (OSError, json.JSONDecodeError):
                # If we can't read or verify, fail closed
                return True
        return True

    def _acquire_lock(self):
        if os.path.exists(self.lock_file):
            try:
                old_pid = int(open(self.lock_file).read().strip())
                if _pid_alive is not None and _pid_alive(old_pid):
                    return False
            except (ValueError, OSError):
                pass
        try:
            os.makedirs(os.path.dirname(self.lock_file), exist_ok=True)
            with open(self.lock_file, "w") as f:
                f.write(str(os.getpid()))
            return True
        except OSError:
            return False

    def _release_lock(self):
        try:
            if os.path.exists(self.lock_file):
                pid = int(open(self.lock_file).read().strip())
                if pid == os.getpid():
                    os.remove(self.lock_file)
        except (ValueError, OSError):
            pass

    def _human_recent(self):
        try:
            data = json.load(open(self.human_action_file, encoding="utf-8"))
            ts = datetime.fromisoformat(str(data.get("timestamp", "")))
        except (OSError, json.JSONDecodeError, ValueError, TypeError, KeyError):
            return False
        return (datetime.now() - ts).total_seconds() < HUMAN_WINDOW_SECONDS

    def _dry_run(self, action):
        return _env_flag(ENV_DRY_RUN, "1")

    def _preconditions_pass(self, action, game_state):
        return all(fn(game_state) for fn in action.precondition_fns())

    def _already_acted(self, alert_id, action_type):
        """True only if this run already *executed* the action for this alert.

        Failed attempts (MCP error, missing precondition, dry-run) must not
        suppress a retry: the earlier version marked them as acted and a
        transient gap became permanent for the rest of the run.
        """
        for rec in _read_jsonl(self.actions_file):
            if (
                rec.get("run_id") == self.run_id
                and rec.get("alert_id") == alert_id
                and rec.get("action") == action_type
                and rec.get("executed") is True
            ):
                return True
        return False

    def _in_cooldown(self, alert_id, action_type):
        """True if the action already ran for this situation within the cooldown.

        An idempotent action (``ensure_food_supply`` and friends) reports
        "nothing left to do" every poll while the alert persists - the stock is
        still low until the harvest. Without a cooldown that repeats the in-game
        say and the audit record every 30 seconds. Only attempts that actually
        ran (preconditions passed) count; a precondition failure is re-checked
        every poll because the underlying situation may have changed.
        """
        if ATTEMPT_COOLDOWN_SECONDS <= 0:
            return False
        needle = _normalized_alert_id(alert_id)
        cutoff = datetime.now() - timedelta(seconds=ATTEMPT_COOLDOWN_SECONDS)
        for rec in _read_jsonl(self.actions_file):
            if rec.get("action") != action_type:
                continue
            if rec.get("precondition_result") is False:
                continue
            if _normalized_alert_id(rec.get("alert_id")) != needle:
                continue
            try:
                when = datetime.fromisoformat(str(rec.get("timestamp")))
            except (TypeError, ValueError):
                continue
            if when >= cutoff:
                return True
        return False

    # --- say / execute --------------------------------------------------

    def _draftable_colonists(self, game_state):
        out = []
        for c in _colonists(game_state):
            if not isinstance(c, dict):
                continue
            if c.get("downed"):
                continue
            job = str(c.get("job", "")).lower()
            if "sleep" in job or "rest" in job:
                continue
            health = c.get("health")
            if health is not None and health <= 0:
                continue
            if c.get("drafted") is True:
                continue
            out.append(c)
        return out

    def _say_intent(self, action, alert, game_state):
        label = alert.get("label") or alert.get("message") or ""
        at = action.action_type
        if at == "draft_and_focus_fire":
            names = [c.get("name", "?") for c in self._draftable_colonists(game_state)]
            return f"SmartRim: drafting {', '.join(names)} to focus fire ({label})"
        if at == "designate_firefighting":
            return f"SmartRim: fire alert ({label}) — designate firefighting; no fire cell in alert"
        if at == "assign_beds":
            unassigned = sum(
                1 for c in _colonists(game_state)
                if isinstance(c, dict) and not c.get("bed_id") and not c.get("bed")
            )
            return f"SmartRim: {unassigned} unassigned colonist(s) — assign beds ({label})"
        if at == "ensure_food_supply":
            return f"SmartRim: food low ({label}) — checking rice zone and cooking bill"
        if at == "set_research_project":
            return f"SmartRim: no research selected ({label}) — picking a project"
        return f"SmartRim: reflex {at} ({label})"

    def _execute(self, action, game_state):
        at = action.action_type
        self.last_error = None
        try:
            if at == "draft_and_focus_fire":
                ok = self._exec_draft(game_state)
            elif at == "designate_firefighting":
                ok = self._exec_firefighting(game_state)
            elif at == "assign_beds":
                ok = self._exec_assign_beds(game_state)
            elif at == "rescue_downed":
                ok = self._exec_rescue_downed(game_state)
            elif at == "prioritize_treatment":
                ok = self._exec_prioritize_treatment(game_state)
            elif at == "ensure_food_supply":
                ok = self._exec_ensure_food_supply(game_state)
            elif at == "set_research_project":
                ok = bool(self.counselor.ensure_research_project())
            else:
                ok = False
                self.last_error = f"no executor for {at}"
        except Exception as e:  # pragma: no cover - defensive
            logger.error("reflex execute %s failed: %s", at, e)
            self.last_error = f"{at} raised: {e}"
            return False
        if not ok and self.last_error is None:
            self.last_error = f"{at} returned false"
        return ok

    def _exec_rescue_downed(self, game_state):
        """Order an able colonist to rescue each downed colonist."""
        colonists = [c for c in _colonists(game_state) if isinstance(c, dict)]
        downed = [c for c in colonists if c.get("downed")]
        able = [
            c for c in colonists
            if not c.get("downed") and not c.get("drafted")
            and str(c.get("job", "")).lower().find("sleep") < 0
        ]
        if not downed or not able:
            return False
        rescuer = able[0]
        rescuer_id = rescuer.get("id") or rescuer.get("name")
        ok = True
        for target in downed:
            target_id = target.get("id") or target.get("name")
            result = self.counselor.order(rescuer_id, target_id, "Rescue")
            ok = ok and not _is_mcp_error(result)
        return ok

    def _exec_prioritize_treatment(self, game_state):
        """Put the best medic on doctoring at priority 1 when someone is hurt."""
        colonists = [c for c in _colonists(game_state) if isinstance(c, dict)]
        wounded = [
            c for c in colonists
            if not c.get("downed") and c.get("health") is not None and c.get("health") < 100
        ]
        if not wounded:
            return False

        def medicine_skill(colonist):
            best = -1
            for skill in colonist.get("topSkills") or []:
                match = re.search(r"Medicine\s+(\d+)", str(skill))
                if match:
                    best = max(best, int(match.group(1)))
            return best

        able = [c for c in colonists if not c.get("downed")]
        if not able:
            return False
        medic = max(able, key=medicine_skill)
        result = self.counselor.set_priority(medic.get("name") or medic.get("id"), "Doctor", 1)
        return not _is_mcp_error(result)

    def _exec_ensure_food_supply(self, game_state):
        """Make sure food is actually being produced: a food crop plus a cooking bill.

        On failure, ``self.last_error`` carries the precise reason (e.g.
        "no campfire or stove found") so the audit trail shows *why*.
        """
        zones_result = self.counselor.zones()
        if isinstance(zones_result, dict) and "error" in zones_result:
            self.last_error = f"list_zones failed: {zones_result['error']}"
            return False

        self.last_error = None
        zone_list = counselor._zone_list(zones_result)
        acted = False
        reasons = []
        food_zone = any(
            isinstance(zone, dict)
            and zone.get("kind") == "growing"
            and any(crop in str(zone.get("plant") or "").lower() for crop in FOOD_CROPS)
            for zone in zone_list
        )
        if not food_zone:
            ok, detail = _as_ok_detail(self.counselor.start_food_zone())
            reasons.append(detail)
            acted = ok or acted
        else:
            reasons.append("food growing zone already present")
        ok, detail = _as_ok_detail(self.counselor.ensure_cooking_bill())
        reasons.append(detail)
        acted = ok or acted

        if acted:
            return True
        self.last_error = "; ".join(r for r in reasons if r)
        return False

    def _exec_draft(self, game_state):
        targets = self._draftable_colonists(game_state)
        if not targets:
            return False
        # The MCP draft tool addresses pawns by ThingID; names are not unique
        # and fail with "Pawn not found".
        ids = [c.get("id") for c in targets if c.get("id")]
        if ids:
            result = self.counselor.draft(ids)
        else:
            names = [c.get("name", "?") for c in targets]
            result = self.counselor.draft(names)
        return not _is_mcp_error(result)

    def _exec_firefighting(self, game_state):
        # Fire cell coordinates are not carried by the alert; never issue a
        # blind coordinate designator. Player must designate manually after the say.
        self.last_error = "fire cells not on the alert; designation is manual"
        return False

    def _exec_assign_beds(self, game_state):
        # Bed building IDs are not carried by the alert; never issue a blind
        # assign. Player assigns manually after the say.
        self.last_error = "bed building ids not on the alert; assignment is manual"
        return False

    # --- audit ----------------------------------------------------------

    def _write_audit(self, result):
        record = {
            "timestamp": _now(),
            "run_id": self.run_id,
            "alert_id": result.get("alert_id"),
            "action": result.get("action"),
            "action_id": result.get("action_id"),
            "precondition_result": result.get("precondition_result"),
            "dry_run": result.get("dry_run"),
            "executed": result.get("executed"),
            "outcome_check_at": result.get("outcome_check_at"),
            "outcome_status": result.get("outcome_status"),
        }
        if result.get("skipped_reason"):
            record["skipped_reason"] = result["skipped_reason"]
        if result.get("reason"):
            record["reason"] = result["reason"]
        _append_jsonl(self.actions_file, record)

    # --- entry point ----------------------------------------------------

    def evaluate(self, alerts, situation, game_state, current_day=None):
        """Run every whitelisted action whose alert matches.

        Returns a list of per-action result dicts. Never raises.
        """
        results = []
        for action in self.actions:
            matched = [a for a in (alerts or []) if action.matches(a)]
            if not matched:
                continue
            alert = matched[0]
            alert_id = _alert_id(alert)
            base = {
                "alert_id": alert_id,
                "action": action.action_type,
                "action_id": action.id,
                "skipped_reason": None,
                "alert": alert,
            }

            if _env_flag(ENV_KILL, "1"):
                results.append({**base, "skipped_reason": "kill_switch"})
                continue
            if self._paused(current_day):
                results.append({**base, "skipped_reason": "paused"})
                continue
            if not self._acquire_lock():
                results.append({**base, "skipped_reason": "lock_held"})
                continue
            try:
                if self._human_recent():
                    results.append({**base, "skipped_reason": "human_window"})
                    continue
                if self._already_acted(alert_id, action.action_type):
                    results.append({**base, "precondition_result": None, "skipped_reason": "duplicate"})
                    continue
                if self._in_cooldown(alert_id, action.action_type):
                    results.append({**base, "precondition_result": None, "skipped_reason": "cooldown"})
                    continue
                pre = self._preconditions_pass(action, _with_alert(game_state, alert))
                dry = self._dry_run(action)
                if not pre:
                    self._write_audit({**base, "precondition_result": False,
                                       "dry_run": dry, "executed": False,
                                       "outcome_check_at": None, "outcome_status": None})
                    results.append({**base, "precondition_result": False, "skipped_reason": "preconditions"})
                    continue
                intent = self._say_intent(action, alert, game_state)
                if dry:
                    logger.info("REFLEX dry-run: would have %s for %s", action.action_type, alert_id)
                    self._write_audit({**base, "precondition_result": True, "dry_run": True,
                                       "executed": False, "outcome_check_at": None,
                                       "outcome_status": None})
                    results.append({**base, "precondition_result": True, "dry_run": True,
                                    "executed": False, "say": intent})
                    continue
                try:
                    self.counselor.say(intent)
                except Exception as e:  # say must not block execution
                    logger.debug("reflex say failed: %s", e)
                # Recheck pause under the action lock before executing
                if self._paused(current_day):
                    logger.info("REFLEX paused before execute; skipping execution")
                    self._write_audit({**base, "precondition_result": True, "dry_run": False,
                                       "executed": False, "outcome_check_at": None,
                                       "outcome_status": None, "skipped_reason": "paused_before_execute"})
                    results.append({**base, "precondition_result": True, "dry_run": False,
                                    "executed": False, "say": intent, "skipped_reason": "paused_before_execute"})
                    continue
                executed = self._execute(action, game_state)
                record = {**base, "precondition_result": True, "dry_run": False,
                          "executed": executed, "outcome_check_at": None,
                          "outcome_status": None}
                if not executed and self.last_error:
                    record["reason"] = self.last_error
                self._write_audit(record)
                results.append({**base, "precondition_result": True, "dry_run": False,
                                "executed": executed, "say": intent})
            finally:
                self._release_lock()
        return results


def close_action_outcomes(snapshot_summary, run_id=None, actions_file=None):
    """Close executed action records by reusing outcomes._close_advice.

    Mirrors monitor.close_outcomes for the actions audit log. Idempotent.
    """
    if outcomes is None:
        return False
    run_id = run_id or os.getenv("RUN_ID", UNSET_RUN_ID)
    actions_file = actions_file or _actions_file()
    if not actions_file or not os.path.exists(actions_file):
        return False
    records = _read_jsonl(actions_file)
    changed = False
    check_at = _now()
    for rec in records:
        if rec.get("executed") is not True:
            continue
        if rec.get("outcome_status"):
            continue
        if rec.get("run_id") != run_id:
            continue
        advice = {"situation": f"{rec.get('alert_id', '')} {rec.get('action', '')}".strip()}
        new_status, note = outcomes._close_advice(advice, snapshot_summary)
        if new_status is None:
            continue
        rec["outcome_status"] = new_status
        if note:
            rec["outcome_note"] = note
        rec["outcome_check_at"] = check_at
        changed = True
    if changed:
        _write_jsonl(actions_file, records)
    return changed


def _colonists(game_state):
    return game_state.get("colonists") or [] if isinstance(game_state, dict) else []


def _is_mcp_error(result):
    return isinstance(result, dict) and "error" in result


def _as_ok_detail(result):
    """Normalize a counselor return into (ok, detail).

    Counselors return (ok, reason) tuples; older tooling and test doubles may
    still return bare booleans — those map to (ok, "ok"/"failed").
    """
    if isinstance(result, tuple) and len(result) == 2:
        ok, detail = result
        return bool(ok), str(detail)
    ok = bool(result)
    return ok, "done" if ok else "action returned false"


if __name__ == "__main__":  # pragma: no cover

    print("actions:", len(load_reflex_actions()))
    for action in load_reflex_actions():
        print(" ", action.id, action.action_type, "dry_run:", action.dry_run)
