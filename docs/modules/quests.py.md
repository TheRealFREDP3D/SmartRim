# quests.py — Quest Context for Snapshots & Debrief

Tracks quest state across snapshots for debrief bundle v3.

## Functions

| Function | Description |
|----------|-------------|
| `update(client, day_label, path)` | Fetch quests via MCP `get_quest`, merge with registry, return current quests |
| `load_registry(path)` | Load quest registry JSON |
| `save_registry(registry, path)` | Save quest registry |
| `list_quests(registry)` | List all known quests |
| `summary_lines(registry)` | One-line summaries for debrief |
| `quests_from_snapshots(snapshots_dir)` | Reconstruct quest timeline from snapshots |

## Data Structures

### Quest Registry (`memory/quests.json`)
```json
{
  "quest_id": {
    "name": "Quest Name",
    "state": "Ongoing|Completed|Failed",
    "start_day": 5,
    "end_day": 12,
    "rewards": [...],
    "description": "..."
  }
}
```

### Snapshot Quest Entry
```json
{
  "quest_id": "Quest_123",
  "name": "Bandit Camp",
  "state": "Ongoing",
  "ticks_remaining": 120000
}
```

## Helpers
- `clean_text(text)` — strip RimWorld rich text tags
- `_detail(quest)` — extract structured fields from MCP response

## Integration
- Called by `monitor.write_snapshot()` if `_quests` module available
- Used by `debrief_bundle._load_wiki_facts()` for quest context
- Optional: older game builds without `get_quest` don't break snapshots

## Notes
- 171 lines
- Registry persists across runs (separate file per run)
- Enables quest-aware lessons in future