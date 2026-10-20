"""Advice log: append-only JSONL of every piece of advice given, with outcome tracking."""

import os
import json
import uuid
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADVICE_DIR = os.path.join(BASE_DIR, "memory", "advice")
ADVICE_FILE = os.path.join(ADVICE_DIR, "advice.jsonl")


def _ensure_dir():
    os.makedirs(ADVICE_DIR, exist_ok=True)


def new_advice_id():
    return "adv-" + datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:6]


def log_advice(run_id, snapshot_day, trigger, severity, situation, actions,
               risks=None, watch_next=None, linked_lessons=None, reflex_name=None,
               auto_paused=False, llm_model=None, context_tokens=None):
    """Append one advice record. Returns the advice_id."""
    _ensure_dir()
    advice_id = new_advice_id()
    record = {
        "advice_id": advice_id,
        "run_id": run_id,
        "timestamp": datetime.now().isoformat(),
        "snapshot_day": snapshot_day,
        "trigger": trigger,
        "reflex_name": reflex_name,
        "severity": severity,
        "status": "open",
        "outcome_note": None,
        "situation": situation,
        "risks": risks or [],
        "actions": actions,
        "watch_next": watch_next or [],
        "linked_lessons": linked_lessons or [],
        "auto_paused": auto_paused,
        "llm_model": llm_model,
        "context_tokens": context_tokens,
    }
    with open(ADVICE_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, default=str) + "\n")
    return advice_id


def update_outcome(advice_id, status, outcome_note=None):
    """Update the status/outcome of an existing advice record by rewriting the file."""
    _ensure_dir()
    if not os.path.exists(ADVICE_FILE):
        return False
    records = []
    found = False
    with open(ADVICE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if rec.get("advice_id") == advice_id:
                rec["status"] = status
                if outcome_note is not None:
                    rec["outcome_note"] = outcome_note
                found = True
            records.append(rec)
    if not found:
        return False
    with open(ADVICE_FILE, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, default=str) + "\n")
    return True


def find_open_duplicate(run_id, situation):
    """Return the advice_id of an already-open record with the same situation, if any.

    Used to stop monitor restarts (or repeated polls after a restart) from writing the
    same urgent advice again and again.
    """
    for rec in read_advice(run_id=run_id, status="open"):
        if rec.get("situation") == situation:
            return rec.get("advice_id")
    return None


def read_advice(run_id=None, status=None):
    """Read advice records, optionally filtered by run_id or status."""
    _ensure_dir()
    if not os.path.exists(ADVICE_FILE):
        return []
    out = []
    with open(ADVICE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if run_id and rec.get("run_id") != run_id:
                continue
            if status and rec.get("status") != status:
                continue
            out.append(rec)
    return out


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: advice_log.py list [run_id] | update <advice_id> <status> [note]")
        sys.exit(0)
    cmd = sys.argv[1]
    if cmd == "list":
        rid = sys.argv[2] if len(sys.argv) > 2 else None
        for r in read_advice(run_id=rid):
            print(r["advice_id"], r["trigger"], r["severity"], r["status"], "-", r["situation"][:60])
    elif cmd == "update":
        aid = sys.argv[2]
        st = sys.argv[3]
        note = " ".join(sys.argv[4:]) if len(sys.argv) > 4 else None
        print("updated:", update_outcome(aid, st, note))
