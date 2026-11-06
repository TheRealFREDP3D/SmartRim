"""Shared candidate -> lesson promotion logic.

Used by the interactive CLI (`situation promote`) and the automated pipeline
(`pipeline`). Everything here is deterministic and side-effect-light:

- candidate files may contain ``#`` comment lines (the writer annotates
  validation problems) — they are skipped, never promoted;
- rule-based auto-promotion requires:
    1. title, recommendation and rationale non-empty;
    2. a non-empty ``source`` (cited observation);
    3. at least one non-empty trigger scoping field (phases, threats or
       resources) — too-broad lessons are never retrieved anyway;
    4. no duplicate of an existing lesson (token-Jaccard >= 0.8 on
       title + recommendation) and no duplicate within the batch;
    5. status is forced to ``needs_review`` — automatic promotion never
       activates a lesson; a human flips it to ``active``.
"""

from __future__ import annotations

import json
import os
import re

from smartrim import config
from smartrim.situation import LESSONS_FILE, validate_lesson

DUPLICATE_THRESHOLD = 0.8


def load_candidates(path):
    """Parse a candidates JSONL file; ``#`` comment lines are skipped."""
    candidates = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                candidates.append(json.loads(line))
            except json.JSONDecodeError:
                # Keep going: one bad line must not sink the whole batch.
                continue
    return candidates


def _tokens(text):
    return set(re.findall(r"[a-z0-9]+", str(text or "").lower()))


def similarity(a, b):
    """Token Jaccard similarity between two texts."""
    ta, tb = _tokens(a), _tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def _candidate_signature(candidate):
    return f"{candidate.get('title', '')} {candidate.get('recommendation', '')}"


def find_duplicate(candidate, existing_lessons, threshold=DUPLICATE_THRESHOLD):
    """Return (lesson_id, score) of the best-matching existing lesson, or None."""
    sig = _candidate_signature(candidate)
    best = None
    for lesson in existing_lessons:
        other = f"{lesson.get('title', '')} {lesson.get('recommendation', '')}"
        score = similarity(sig, other)
        if score >= threshold and (best is None or score > best[1]):
            best = (lesson.get("id"), score)
    return best


def auto_promote_rules(candidate, existing_lessons, batch_signatures=()):
    """Check the auto-promotion rules; returns a list of skip reasons (empty = promote)."""
    reasons = []
    if candidate.get("promoted_as"):
        reasons.append("already promoted")
        return reasons
    if not (candidate.get("title") or "").strip():
        reasons.append("missing title")
    if not (candidate.get("recommendation") or "").strip():
        reasons.append("missing recommendation")
    if not (candidate.get("rationale") or "").strip():
        reasons.append("missing rationale")
    if not candidate.get("source"):
        reasons.append("no source citation")
    trigger = candidate.get("trigger") or {}
    scoped = any(
        bool(trigger.get(field)) for field in ("phases", "threats", "resources")
    )
    if not scoped:
        reasons.append("too broad (no phases/threats/resources scoping)")
    sig = _candidate_signature(candidate)
    for other in batch_signatures:
        if similarity(sig, other) >= DUPLICATE_THRESHOLD:
            reasons.append("duplicate within batch")
            break
    if not reasons:
        dup = find_duplicate(candidate, existing_lessons)
        if dup:
            reasons.append(f"duplicate of {dup[0]} (similarity {dup[1]:.2f})")
    return reasons


def next_lesson_number(existing_lessons):
    best = 0
    for lesson in existing_lessons:
        m = re.match(r"^L-(\d{4})$", str(lesson.get("id", "") or ""))
        if m:
            best = max(best, int(m.group(1)))
    return best + 1


def load_existing_lessons(lessons_file=None):
    lessons_file = lessons_file or LESSONS_FILE
    lessons = []
    if not os.path.isfile(lessons_file):
        return lessons
    with open(lessons_file, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                lessons.append(json.loads(line))
    return lessons


def append_lessons_to_store(promoted, lessons_file=None):
    """Append via the SQLite store (keeps the FTS index in sync), raw JSONL on failure."""
    from smartrim.lesson_store import DEFAULT_SQLITE_PATH, SqliteLessonStore

    lessons_file = lessons_file or LESSONS_FILE
    db_path = (
        os.path.splitext(lessons_file)[0] + ".sqlite"
        if os.path.join(config.BASE_DIR, "memory", "lessons.jsonl") != lessons_file
        else DEFAULT_SQLITE_PATH
    )
    try:
        store = SqliteLessonStore(db_path=db_path, jsonl_path=lessons_file)
        try:
            for lesson in promoted:
                store.append(lesson)
        finally:
            store.close()
        return True
    except Exception:
        with open(lessons_file, "a", encoding="utf-8") as fh:
            for lesson in promoted:
                fh.write(json.dumps(lesson, default=str) + "\n")
        return False


def annotate_candidates_file(path, promoted_map):
    """Rewrite a candidates file, tagging promoted lines with ``promoted_as``."""
    if not promoted_map:
        return
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            stripped = line.rstrip("\n")
            body = stripped.strip()
            if not body or body.startswith("#"):
                out.append(stripped)
                continue
            try:
                rec = json.loads(body)
            except json.JSONDecodeError:
                out.append(stripped)
                continue
            new_id = promoted_map.get(rec.get("id"))
            if new_id:
                rec["promoted_as"] = new_id
                rec["status"] = "promoted"
            out.append(json.dumps(rec, default=str))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")


def promote_rule_based(candidates, existing_lessons, *, lessons_file=None,
                       dry_run=False, today=None):
    """Auto-promote rule-passing candidates as ``needs_review``.

    Returns (promoted, skipped, mapping): ``promoted`` is a list of assigned
    lessons, ``skipped`` a list of (candidate_id, reasons), and ``mapping``
    maps candidate id -> assigned lesson id for file annotation.
    """
    promoted: list[dict] = []
    skipped: list[tuple[str, list[str]]] = []
    mapping: dict[str, str] = {}
    batch_signatures: list[str] = []
    next_num = next_lesson_number(existing_lessons)
    today = today or __import__("datetime").datetime.now().strftime("%Y-%m-%d")

    for candidate in candidates:
        cid = candidate.get("id", "?")
        reasons = auto_promote_rules(candidate, existing_lessons, batch_signatures)
        if reasons:
            skipped.append((cid, reasons))
            continue
        lesson = dict(candidate)
        lesson["id"] = f"L-{next_num:04d}"
        lesson["status"] = "needs_review"
        lesson.setdefault("times_applied", 0)
        lesson.setdefault("times_helped", 0)
        lesson.setdefault("times_failed", 0)
        lesson["last_updated"] = today
        errors = [e for e in validate_lesson(lesson) if not e.startswith("bad id")]
        if errors:
            skipped.append((cid, [f"fails validation: {errors}"]))
            continue
        promoted.append(lesson)
        mapping[cid] = lesson["id"]
        existing_lessons = [*existing_lessons, lesson]
        batch_signatures.append(_candidate_signature(lesson))
        next_num += 1

    if promoted and not dry_run:
        append_lessons_to_store(promoted, lessons_file=lessons_file)
    return promoted, skipped, mapping
