# lesson_store.py — Lesson Persistence Abstraction

Provides protocol + two implementations for lesson storage and retrieval.

## Protocol: `LessonStore` (ABC)

| Method | Description |
|--------|-------------|
| `load_all()` | Load all lessons |
| `retrieve(situation, limit=5, query_text=None)` | Semantic search |
| `reindex(verbose=True)` | Rebuild search index |
| `save_all(lessons)` | Persist all lessons |
| `append(lesson)` | Append single lesson |

## Implementations

### `JsonlLessonStore` (Source of Truth)
- File: `memory/lessons.jsonl` (human-editable, tracked in git)
- No semantic search — exact match on trigger fields only
- `query_text` ignored

### `SqliteLessonStore` (Query Index)
- File: `memory/lessons.sqlite` (derived, gitignored)
- FTS5 full-text search on trigger fields + recommendation + rationale
- Rebuilt via `sync_sqlite()` or `python -m smartrim.situation reindex`

## Dataclass: `Lesson`
```python
@dataclass
class Lesson:
    id: str
    title: str
    trigger: dict          # phase, threats, resources, difficulty, storyteller, biome
    recommendation: str
    rationale: str
    source: list[str]
    confidence: float      # 0.0-1.0
    status: str            # "active" | "deprecated"
    tags: list[str]
    times_applied: int = 0
    times_helped: int = 0
    times_failed: int = 0
    source_runs: list[str] | None = None
    last_updated: str = ""
```

## Factory
```python
def get_store(backend: str = "sqlite", **kwargs) -> LessonStore:
    # backend: "jsonl" or "sqlite"
```

## Helpers
- `_normalize_list(val)` — normalize list/singleton to list (shared with situation.py)
- `_ci_contains(allowed, value)` — case-insensitive membership for trigger fields

## Sync
```python
def sync_sqlite(jsonl_path=DEFAULT_JSONL_PATH, sqlite_path=DEFAULT_SQLITE_PATH, verbose=True):
    # Rebuild SQLite from JSONL
```

## Notes
- JSONL is source of truth; SQLite is derived index
- Mutable defaults in dataclass use `None` and normalized in `__post_init__`
- 608 lines