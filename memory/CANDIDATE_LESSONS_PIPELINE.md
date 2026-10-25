# Candidate Lessons Auto-Promotion Pipeline

## Overview

The LLM → lesson pipeline has been streamlined to reduce manual friction. Previously, a human had to read the LLM analysis, manually write a JSONL lesson, and run `lessons.py validate` to merge it. Now, the pipeline is automated:

1. LLM generates candidate lessons from debrief bundle
2. Candidates are written to `memory/candidates/<run>-<timestamp>.jsonl`
3. Human reviews and promotes with `lessons.py promote <candidate-file>`
4. Promoted lessons are assigned L-XXXX IDs and merged into `lessons.jsonl`

## What Changed

### Before (Manual Copy-Paste-Edit)
1. `debrief_llm.write_analysis()` writes analysis to `memory/debriefs/<run>-llm.md`
2. Human reads analysis, manually writes JSONL lesson
3. Human runs `lessons.py validate` to check schema
4. Human appends to `lessons.jsonl`
5. Friction: only 3 of 52 lessons have non-session sources

### After (Automated Pipeline)
1. `debrief_llm.write_analysis()` writes:
   - Analysis to `memory/debriefs/<run>-llm.md` (unchanged)
   - Candidates to `memory/candidates/<run>-<timestamp>.jsonl` (new)
2. Human runs `lessons.py promote <candidate-file>`
3. Interactive review: select lessons, edit status/confidence
4. Promoted lessons get L-XXXX IDs and are appended to `lessons.jsonl`
5. One-command merge instead of copy-paste-edit cycle

## Modified Files

### `src/smartrim/debrief_llm.py`
- Added `_write_candidate_lessons()` function
- Added `_normalize_trigger()` helper
- Updated `write_analysis()` to call `_write_candidate_lessons()`
- Candidate lessons are written with:
  - `id`: "C-<run_id>-<index>" (candidate format)
  - `status`: "needs_review"
  - `confidence`: 0.3 (floor for single observations)
  - `times_applied/helped/failed`: 0
  - Schema validation (ID validation skipped for candidates)

### `src/smartrim/situation.py`
- Added `promote` CLI command to `main()`
- Interactive flow:
  1. Load candidate file
  2. List candidates with indices
  3. Prompt for selection (comma-separated or "all")
  4. For each selected: prompt for status/confidence edits
  5. Assign new L-XXXX ID (auto-increment)
  6. Validate with full lesson schema
  7. Append to `lessons.jsonl`

### `tests/test_candidate_lessons.py` (new)
- Tests for `_normalize_trigger()`
- Tests for `_write_candidate_lessons()`
- Tests for candidate schema
- Tests for multiple candidates
- Tests for missing candidates_dir

## Usage

### Generate candidate lessons (automatic)
When running `debrief_llm.py`, candidates are automatically written:

```bash
python -c "import sys; sys.path.insert(0, 'src'); from smartrim.debrief_llm import main; main()" --run run-005
```

This creates:
- `memory/debriefs/run-005-llm.md` (analysis)
- `memory/candidates/run-005-20261025-123456.jsonl` (candidate lessons)

### Promote candidates to lessons
```bash
python -c "import sys; sys.path.insert(0, 'src'); from smartrim.situation import main; main(['lessons.py', 'promote', 'memory/candidates/run-005-20261025-123456.jsonl'])"
```

Interactive flow:
```
Found 3 candidate lesson(s):
  0. C-run-005-0: Test lesson 1 (status: needs_review)
  1. C-run-005-1: Test lesson 2 (status: needs_review)
  2. C-run-005-2: Test lesson 3 (status: needs_review)

Enter lesson numbers to promote (comma-separated, or 'all'):
> 0,2

--- Editing lesson 0: Test lesson 1 ---
Current status: needs_review
Current confidence: 0.3
Leave blank to keep current value.

Status [needs_review]: active
Confidence [0.3]: 0.6

Promoted as L-0053

--- Editing lesson 2: Test lesson 3 ---
Current status: needs_review
Current confidence: 0.3
Leave blank to keep current value.

Status [needs_review]: active
Confidence [0.3]: 0.5

Promoted as L-0054

Promoted 2 lesson(s) to memory/lessons.jsonl
Run 'lessons.py validate' to verify.
```

### Verify promoted lessons
```bash
python -c "import sys; sys.path.insert(0, 'src'); from smartrim.situation import main; main(['lessons.py', 'validate'])"
```

## Candidate Lesson Schema

Candidates are written with the full lesson schema, but with:
- `id`: "C-<run_id>-<index>" (candidate format, not L-XXXX)
- `status`: "needs_review" (must be reviewed before activation)
- `confidence`: 0.3 (floor for single observations)
- `times_applied`: 0
- `times_helped`: 0
- `times_failed`: 0
- `source_runs`: [run_id]
- `last_updated`: current date

During promotion:
- `id` is reassigned to L-XXXX format (auto-increment)
- `status` can be changed (default: "needs_review")
- `confidence` can be adjusted (default: 0.3)
- Full schema validation with proper L-XXXX ID

## Benefits

1. **Reduced friction**: One-command merge instead of copy-paste-edit
2. **Structured candidates**: Schema-validated before promotion
3. **Interactive review**: Human can edit status/confidence before merging
4. **Auto-increment IDs**: No manual ID assignment
5. **Traceability**: Candidates retain `source_runs` for audit trail
6. **Batch promotion**: Select multiple lessons at once

## Future Improvements

- Add non-interactive promotion mode for CI/automation
- Add bulk promotion: `lessons.py promote-all` to promote all candidates in a directory
- Add candidate deduplication: detect similar candidates before promotion
- Add candidate ranking: sort by confidence or relevance
- Add web UI for candidate review
- Add automatic promotion based on confidence threshold
