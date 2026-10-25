"""Lesson store abstraction with SQLite + FTS5 semantic search.

Provides:
- LessonStore Protocol: interface for lesson storage and retrieval
- SqliteLessonStore: SQLite-backed store with FTS5 full-text search
- JsonlLessonStore: backward-compatible JSONL file store (human-editable source of truth)

The JSONL file (memory/lessons.jsonl) remains the human-editable source.
SQLite (memory/lessons.sqlite) is the query index, rebuilt via `lessons.py reindex`.
"""

import json
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass

try:
    from smartrim.config import BASE_DIR
except ImportError:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_JSONL_PATH = os.path.join(BASE_DIR, "memory", "lessons.jsonl")
DEFAULT_SQLITE_PATH = os.path.join(BASE_DIR, "memory", "lessons.sqlite")


def _normalize_list(val):
    """Normalize list/singleton to list (shared helper)."""
    if val is None:
        return []
    if isinstance(val, str):
        v = val.strip().lower()
        if v == "any" or v == "":
            return []
        return [val]
    if isinstance(val, (list, set, tuple)):
        out = []
        for item in val:
            if item is None:
                continue
            if isinstance(item, str) and item.strip().lower() == "any":
                continue
            out.append(item)
        return out
    return [val]


def _ci_contains(allowed, value) -> bool:
    """Case-insensitive membership test for scoped trigger fields.

    The situation carries values as the game reports them ("adventure story")
    while lessons store the canonical label ("Adventure story"), so an exact
    comparison silently rejects every difficulty/storyteller-scoped lesson.
    """
    if value is None:
        return False
    target = str(value).strip().lower()
    if not target or target == "any":
        return True
    return any(str(a).strip().lower() == target for a in allowed)


@dataclass
class Lesson:
    """Structured lesson object."""
    id: str
    title: str
    trigger: dict
    recommendation: str
    rationale: str
    source: list
    confidence: float
    status: str
    tags: list
    times_applied: int = 0
    times_helped: int = 0
    times_failed: int = 0
    source_runs: list = None
    last_updated: str = ""

    def to_dict(self) -> dict:
        """Convert to dictionary format compatible with JSONL."""
        return {
            "id": self.id,
            "title": self.title,
            "trigger": self.trigger,
            "recommendation": self.recommendation,
            "rationale": self.rationale,
            "source": self.source,
            "confidence": self.confidence,
            "status": self.status,
            "tags": self.tags,
            "times_applied": self.times_applied,
            "times_helped": self.times_helped,
            "times_failed": self.times_failed,
            "source_runs": self.source_runs or [],
            "last_updated": self.last_updated,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Lesson":
        """Create Lesson from dictionary."""
        return cls(
            id=data.get("id", ""),
            title=data.get("title", ""),
            trigger=data.get("trigger", {}),
            recommendation=data.get("recommendation", ""),
            rationale=data.get("rationale", ""),
            source=data.get("source", []),
            confidence=data.get("confidence", 0.0),
            status=data.get("status", "active"),
            tags=data.get("tags", []),
            times_applied=data.get("times_applied", 0),
            times_helped=data.get("times_helped", 0),
            times_failed=data.get("times_failed", 0),
            source_runs=data.get("source_runs"),
            last_updated=data.get("last_updated", ""),
        )


class LessonStore(ABC):
    """Protocol for lesson storage and retrieval."""

    @abstractmethod
    def load_all(self) -> list[Lesson]:
        """Load all lessons from storage."""

    @abstractmethod
    def retrieve(
        self,
        situation: dict,
        limit: int = 5,
        query_text: str | None = None,
    ) -> list[Lesson]:
        """Retrieve lessons matching situation and optional semantic query.

        Args:
            situation: Dict with phase, threats, resources, difficulty, storyteller, biome
            limit: Maximum number of lessons to return
            query_text: Optional text for semantic/FTS search (e.g., situation summary)

        Returns:
            List of matching lessons, ranked by relevance.
        """

    @abstractmethod
    def reindex(self) -> None:
        """Rebuild the search index from source data."""


class JsonlLessonStore(LessonStore):
    """Backward-compatible JSONL file store.

    This is the human-editable source of truth. It does not support semantic search.
    """

    def __init__(self, path: str = DEFAULT_JSONL_PATH):
        self.path = path

    def load_all(self) -> list[Lesson]:
        """Load all lessons from JSONL file."""
        lessons = []
        if not os.path.exists(self.path):
            return lessons
        with open(self.path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                lessons.append(Lesson.from_dict(json.loads(line)))
        return lessons

    def retrieve(
        self,
        situation: dict,
        limit: int = 5,
        query_text: str | None = None,
    ) -> list[Lesson]:
        """Retrieve lessons using exact match on trigger fields (no semantic search).

        query_text is ignored in JSONL store.
        """
        from smartrim.situation import _normalize_list

        lessons = self.load_all()

        phase = situation.get("phase")
        threats = set(situation.get("threats") or [])
        resources = set(situation.get("resources") or [])
        difficulty = situation.get("difficulty")
        storyteller = situation.get("storyteller")
        biome = situation.get("biome")

        candidates = []
        for lesson in lessons:
            if lesson.status != "active":
                continue
            trigger = lesson.trigger or {}
            phases = _normalize_list(trigger.get("phases"))
            l_threats = set(_normalize_list(trigger.get("threats")))
            l_resources = set(_normalize_list(trigger.get("resources")))
            l_diff = _normalize_list(trigger.get("difficulty"))
            l_st = _normalize_list(trigger.get("storyteller"))
            l_biome = _normalize_list(trigger.get("biome"))

            if phases and phase not in phases:
                continue
            if not phases and not l_threats and not l_resources and not l_diff and not l_st and not l_biome:
                continue
            if l_threats or l_resources:
                threat_match = bool(threats & l_threats)
                resource_match = bool(resources & l_resources)
                if not (threat_match or resource_match):
                    continue
            if l_diff and difficulty not in l_diff:
                continue
            if l_st and storyteller not in l_st:
                continue
            if l_biome and biome not in l_biome:
                continue

            conf = lesson.confidence
            helped = lesson.times_helped
            failed = lesson.times_failed
            last_updated = lesson.last_updated or ""
            key = (-conf, -(helped - failed), last_updated, lesson.id)
            candidates.append((key, lesson))

        candidates.sort(key=lambda x: x[0])
        return [c[1] for c in candidates[:limit]]

    def reindex(self) -> None:
        """No-op for JSONL store (no index to rebuild)."""


class SqliteLessonStore(LessonStore):
    """SQLite-backed lesson store with FTS5 full-text search.

    Schema:
    - lessons: structured columns (id, status, trigger fields, confidence, etc.)
    - lesson_fts: FTS5 virtual table on (title, recommendation, rationale, tags)

    Retrieval path:
    1. SQL filter on structured trigger columns (indexed, fast)
    2. FTS5 rank on query_text (semantic search)
    3. Return top-K results
    """

    def __init__(
        self,
        db_path: str = DEFAULT_SQLITE_PATH,
        jsonl_path: str = DEFAULT_JSONL_PATH,
    ):
        self.db_path = db_path
        self.jsonl_path = jsonl_path
        self._conn = None

    def _get_conn(self):
        """Lazy connection initialization."""
        if self._conn is None:
            import sqlite3

            self._conn = sqlite3.connect(self.db_path)
            self._conn.row_factory = sqlite3.Row
        return self._conn

    def _init_schema(self) -> None:
        """Initialize database schema if not exists."""
        conn = self._get_conn()
        cursor = conn.cursor()

        # Main lessons table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lessons (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                trigger_json TEXT NOT NULL,
                recommendation TEXT NOT NULL,
                rationale TEXT NOT NULL,
                source_json TEXT NOT NULL,
                confidence REAL NOT NULL,
                status TEXT NOT NULL,
                tags_json TEXT NOT NULL,
                times_applied INTEGER DEFAULT 0,
                times_helped INTEGER DEFAULT 0,
                times_failed INTEGER DEFAULT 0,
                source_runs_json TEXT,
                last_updated TEXT
            )
        """)

        # Create indexes on structured trigger fields
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_status ON lessons(status)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_confidence ON lessons(confidence)")

        # FTS5 virtual table for full-text search (separate table, simpler)
        cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS lesson_fts USING fts5(
                lesson_id,
                title,
                recommendation,
                rationale,
                tags
            )
        """)

        conn.commit()

    def load_all(self) -> list[Lesson]:
        """Load all lessons from SQLite."""
        self._init_schema()
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lessons")
        return [self._row_to_lesson(row) for row in cursor.fetchall()]

    def _row_to_lesson(self, row) -> Lesson:
        """Convert SQLite row to Lesson object."""
        return Lesson(
            id=row["id"],
            title=row["title"],
            trigger=json.loads(row["trigger_json"]),
            recommendation=row["recommendation"],
            rationale=row["rationale"],
            source=json.loads(row["source_json"]),
            confidence=row["confidence"],
            status=row["status"],
            tags=json.loads(row["tags_json"]),
            times_applied=row["times_applied"],
            times_helped=row["times_helped"],
            times_failed=row["times_failed"],
            source_runs=json.loads(row["source_runs_json"]) if row["source_runs_json"] else None,
            last_updated=row["last_updated"] or "",
        )

    def _normalize_list(self, val):
        """Normalize list/singleton to list (shared helper)."""
        return _normalize_list(val)

    def retrieve(
        self,
        situation: dict,
        limit: int = 5,
        query_text: str | None = None,
    ) -> list[Lesson]:
        """Retrieve lessons with structured filter + optional FTS5 semantic search.

        Args:
            situation: Dict with phase, threats, resources, difficulty, storyteller, biome
            limit: Maximum number of lessons to return
            query_text: Optional text for FTS5 search (e.g., situation summary)

        Returns:
            List of matching lessons, ranked by relevance.
        """
        self._init_schema()
        conn = self._get_conn()
        cursor = conn.cursor()

        phase = situation.get("phase")
        threats = set(situation.get("threats") or [])
        resources = set(situation.get("resources") or [])
        difficulty = situation.get("difficulty")
        storyteller = situation.get("storyteller")
        biome = situation.get("biome")

        # We need to parse trigger_json for structured fields
        # Since SQLite doesn't have JSON operations in standard builds,
        # we'll load lessons and filter in Python, then apply FTS ranking
        # This is a hybrid approach: structured filter in Python, FTS for ranking

        lessons = self.load_all()
        candidates = []

        for lesson in lessons:
            if lesson.status != "active":
                continue
            trigger = lesson.trigger or {}
            phases = self._normalize_list(trigger.get("phases"))
            l_threats = set(self._normalize_list(trigger.get("threats")))
            l_resources = set(self._normalize_list(trigger.get("resources")))
            l_diff = self._normalize_list(trigger.get("difficulty"))
            l_st = self._normalize_list(trigger.get("storyteller"))
            l_biome = self._normalize_list(trigger.get("biome"))

            if phases and phase not in phases:
                continue
            if not phases and not l_threats and not l_resources and not l_diff and not l_st and not l_biome:
                continue
            if l_threats or l_resources:
                threat_match = bool(threats & l_threats)
                resource_match = bool(resources & l_resources)
                if not (threat_match or resource_match):
                    continue
            if l_diff and not _ci_contains(l_diff, difficulty):
                continue
            if l_st and not _ci_contains(l_st, storyteller):
                continue
            if l_biome and not _ci_contains(l_biome, biome):
                continue

            candidates.append(lesson)

        if not candidates:
            return []

        # If query_text provided, use FTS5 to rank candidates
        if query_text and candidates:
            # Get lesson IDs for candidates
            candidate_ids = [lesson.id for lesson in candidates]
            placeholders = ",".join(["?"] * len(candidate_ids))

            # FTS5 search with BM25 ranking
            cursor.execute(f"""
                SELECT lesson_id, rank
                FROM lesson_fts
                WHERE lesson_fts MATCH ?
                AND lesson_id IN ({placeholders})
                ORDER BY rank
            """, [query_text, *candidate_ids])

            fts_scores = {row["lesson_id"]: row["rank"] for row in cursor.fetchall()}

            # Sort by FTS rank (lower is better in BM25)
            candidates.sort(key=lambda lesson: fts_scores.get(lesson.id, float("inf")))
        else:
            # No semantic search: sort by confidence and effectiveness
            candidates.sort(
                key=lambda lesson: (
                    -lesson.confidence,
                    -(lesson.times_helped - lesson.times_failed),
                    lesson.last_updated or "",
                    lesson.id,
                )
            )

        return candidates[:limit]

    def reindex(self) -> None:
        """Rebuild SQLite index from JSONL source file."""
        # Load from JSONL
        jsonl_store = JsonlLessonStore(self.jsonl_path)
        lessons = jsonl_store.load_all()

        # Clear and rebuild SQLite
        conn = self._get_conn()
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS lesson_fts")
        cursor.execute("DROP TABLE IF EXISTS lessons")
        conn.commit()

        self._init_schema()

        # Insert lessons
        for lesson in lessons:
            cursor.execute("""
                INSERT INTO lessons (
                    id, title, trigger_json, recommendation, rationale,
                    source_json, confidence, status, tags_json,
                    times_applied, times_helped, times_failed,
                    source_runs_json, last_updated
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                lesson.id,
                lesson.title,
                json.dumps(lesson.trigger),
                lesson.recommendation,
                lesson.rationale,
                json.dumps(lesson.source),
                lesson.confidence,
                lesson.status,
                json.dumps(lesson.tags),
                lesson.times_applied,
                lesson.times_helped,
                lesson.times_failed,
                json.dumps(lesson.source_runs) if lesson.source_runs else None,
                lesson.last_updated,
            ))

        # Populate FTS table
        cursor.execute("""
            INSERT INTO lesson_fts(lesson_id, title, recommendation, rationale, tags)
            SELECT id, title, recommendation, rationale, tags_json FROM lessons
        """)

        conn.commit()
        print(f"Reindexed {len(lessons)} lessons from {self.jsonl_path}")

    def close(self) -> None:
        """Close database connection."""
        if self._conn is not None:
            self._conn.close()
            self._conn = None


def get_store(use_sqlite: bool = True) -> LessonStore:
    """Factory function to get the appropriate lesson store.

    Args:
        use_sqlite: If True, use SqliteLessonStore; otherwise JsonlLessonStore.

    Returns:
        LessonStore instance.
    """
    if use_sqlite:
        return SqliteLessonStore()
    return JsonlLessonStore()
