# Lesson Store Migration: SQLite + FTS5 Semantic Search

## Overview

The lesson retrieval system has been migrated from a pure JSONL scan to a hybrid SQLite + FTS5 approach for semantic matching. This addresses the limitation where lessons required exact phrase matches on trigger fields.

## What Changed

### Before (O(N) Scan)
- `situation.retrieve()` scanned all lessons in memory/lessons.jsonl
- Exact set-membership checks on 6 trigger fields: phases, threats, resources, difficulty, storyteller, biome
- No semantic matching: a lesson about "low food in early game" would not match unless the trigger explicitly contained `low_food`

### After (SQLite + FTS5)
- Structured fields are stored in SQLite for fast indexed filtering
- Full-text search on (title, recommendation, rationale, tags) using FTS5
- Retrieval path: (1) SQL filter on structured trigger columns, (2) FTS5 rank on situation summary, (3) return top-K
- JSONL remains the human-editable source of truth; SQLite is the query index

## New Files

### `src/smartrim/lesson_store.py`
- **LessonStore Protocol**: Interface for lesson storage and retrieval
- **SqliteLessonStore**: SQLite-backed store with FTS5 full-text search
- **JsonlLessonStore**: Backward-compatible JSONL file store
- **Lesson dataclass**: Structured lesson object with to_dict/from_dict methods

### `tests/test_lesson_store.py`
- Tests for Lesson dataclass
- Tests for JsonlLessonStore (backward compatibility)
- Tests for SqliteLessonStore (FTS5, reindex)
- Tests for get_store() factory

## Modified Files

### `src/smartrim/situation.py`
- Added `store` and `use_semantic_search` parameters to `retrieve()`
- Added `store` and `use_semantic_search` parameters to `rank_actions()`
- Added `reindex` CLI command to rebuild SQLite from JSONL
- Backward compatible: when `lessons` list is provided, uses legacy JSONL scan

### `src/smartrim/lessons.py`
- No changes (shim remains unchanged)

## SQLite Schema

### lessons table
```sql
CREATE TABLE lessons (
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
```

### lesson_fts table (FTS5 virtual table)
```sql
CREATE VIRTUAL TABLE lesson_fts USING fts5(
    lesson_id,
    title,
    recommendation,
    rationale,
    tags
)
```

## Usage

### Reindex the SQLite database
After editing memory/lessons.jsonl, rebuild the SQLite index:

```bash
python -c "import sys; sys.path.insert(0, 'src'); from smartrim.situation import main; main(['lessons.py', 'reindex'])"
```

Or via the module:
```python
from smartrim.lesson_store import SqliteLessonStore
store = SqliteLessonStore()
store.reindex()
store.close()
```

### Use SQLite store (default)
```python
from smartrim.situation import retrieve

situation = {
    "phase": "early_survival",
    "threats": ["low_food"],
    "resources": ["food_under_5_days"],
    "difficulty": "any",
    "storyteller": "any",
    "biome": "any",
}

# Uses SqliteLessonStore by default
lessons = retrieve(situation, limit=5)
```

### Use JSONL store (legacy)
```python
from smartrim.situation import retrieve
from smartrim.lesson_store import JsonlLessonStore

store = JsonlLessonStore()
lessons = retrieve(situation, store=store, use_semantic_search=False)
```

### Use with semantic query text
```python
from smartrim.lesson_store import SqliteLessonStore

store = SqliteLessonStore()
situation = {...}

# FTS5 search on situation summary
lessons = store.retrieve(
    situation,
    limit=5,
    query_text="food shortage hunt animals early game"
)
store.close()
```

## Backward Compatibility

- Existing code that passes a `lessons` list to `retrieve()` continues to work (uses legacy scan)
- All existing tests pass without modification
- JSONL file remains the source of truth for human editing
- Can disable semantic search globally by setting `use_semantic_search=False`

## Performance

- **Structured filter**: Fast SQL queries with indexes on status and confidence
- **Semantic search**: FTS5 BM25 ranking on full-text fields
- **Scalability**: With 500 lessons, retrieval is still microseconds; the bottleneck shifts from O(N) scan to SQL query + FTS5 rank

## Future Improvements

- Add JSON1 extension support for direct SQL queries on trigger_json fields
- Consider embedding vectors for true semantic matching (vs keyword-based FTS5)
- Add automatic reindex on JSONL modification (file watcher)
