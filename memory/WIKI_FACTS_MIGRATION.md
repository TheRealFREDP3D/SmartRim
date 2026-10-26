# Wiki Facts Migration: YAML Single Source of Truth

## Overview

The wiki facts in `debrief_bundle.py` were hardcoded as two lists (`WIKI_FACTS` and `UNVERIFIED`). This created a duplication problem: updating a wiki page in `memory/wiki/*.md` did not update the hardcoded list, so the debrief bundle kept feeding old (potentially wrong) facts to the LLM.

## What Changed

### Before (Hardcoded Lists)
- `debrief_bundle.WIKI_FACTS` (lines 24-40): 15 hardcoded strings with wiki:citation format
- `debrief_bundle.UNVERIFIED` (lines 42-48): 5 hardcoded unverified claims
- Source of truth: comments pointing to `memory/wiki-audit-20261018.md`
- Duplication: silent - updating wiki files didn't update the Python lists

### After (YAML Single Source of Truth)
- `memory/wiki_facts.yaml`: Single source of truth for all wiki facts
- Each entry has: `text`, `source_page`, `verified_date`, `status`
- `debrief_bundle._load_wiki_facts()`: Loads YAML at module init, formats citations
- `lessons.py verify-facts`: CI check that source pages still contain cited claims
- Added `pyyaml` dependency to `pyproject.toml`

## New File

### `memory/wiki_facts.yaml`
```yaml
- text: "Mental break base thresholds for a normal colonist: minor 35%, major 20%, extreme 5%. Traits shift them."
  source_page: Mental_break
  verified_date: "2026-10-18"
  status: verified

- text: "Base mood by difficulty: Peaceful 42, Community builder 42, Adventure story 37, Strive to survive 32, Blood and dust 27, Losing is Fun 22."
  source_page: Mood
  verified_date: "2026-10-18"
  status: verified
```

## Modified Files

### `src/smartrim/debrief_bundle.py`
- Removed hardcoded `WIKI_FACTS` and `UNVERIFIED` lists
- Added `_load_wiki_facts()` function to load from YAML
- Added `WIKI_FACTS_PATH` constant pointing to YAML file
- Module init loads facts at startup (cached for performance)
- Graceful degradation: returns empty lists if YAML missing or PyYAML not installed

### `pyproject.toml`
- Added `pyyaml` to dependencies

### `src/smartrim/situation.py`
- Added `verify-facts` CLI command to `main()`
- Checks each verified fact's `source_page` exists in `memory/wiki/*.md`
- Heuristic check: searches for key terms from the fact text in the wiki page
- Exits with error if any source page is missing or key terms not found

### `tests/test_debrief_bundle.py`
- Added `TestWikiFactsLoading` test class
- Tests for `_load_wiki_facts()` returning correct types
- Tests for citation formatting
- Tests for graceful degradation on missing file

## Usage

### Load wiki facts programmatically
```python
from smartrim.debrief_bundle import _load_wiki_facts

verified, unverified = _load_wiki_facts()
# verified: list of strings with wiki:citation format
# unverified: list of strings without citations
```

### Verify wiki facts (CI check)
```bash
python -c "import sys; sys.path.insert(0, 'src'); from smartrim.situation import main; main(['lessons.py', 'verify-facts'])"
```

This checks:
- Each verified fact has a `source_page`
- The source page exists in `memory/wiki/*.md`
- Key terms from the fact are present in the wiki page (heuristic)

### Add a new wiki fact
Edit `memory/wiki_facts.yaml`:
```yaml
- text: "Your fact text here."
  source_page: WikiPageName
  verified_date: "2026-10-25"
  status: verified
```

Then run `verify-facts` to ensure the source page exists and contains the claim.

### Update an existing fact
Edit the entry in `memory/wiki_facts.yaml`, update `verified_date`, and run `verify-facts`.

## Verification

The `verify-facts` command uses a heuristic check:
- Extracts the first 5 words from the fact text
- Searches for those terms (case-insensitive) in the wiki page
- Reports errors if:
  - Source page file doesn't exist
  - Key terms not found in the page content

This is not perfect (it's a substring search), but it's good for catching:
- Typos in page names
- Deleted or moved wiki pages
- Major content changes that removed the cited claim

## Backward Compatibility

- The bundle output format is unchanged (still markdown with sections)
- Existing tests pass without modification (except new tests added)
- If YAML file is missing, debrief bundle still works (graceful degradation to empty lists)
- If PyYAML is not installed, debrief bundle still works (empty lists + warning)

## Benefits

1. **Single source of truth**: `memory/wiki_facts.yaml` is the only place to edit facts
2. **No silent duplication**: Updating wiki files is tracked via `verify-facts`
3. **Structured metadata**: Each fact has `verified_date` and `status`
4. **CI safety**: `verify-facts` catches broken citations before they reach the LLM
5. **Human-editable**: YAML is easier to edit than Python lists
6. **Extensible**: Can add more fields (e.g., `confidence`, `last_reviewed`) without code changes

## Future Improvements

- Add automated citation extraction from wiki pages (parse wiki:citation format)
- Improve verification with more sophisticated text matching (e.g., sentence similarity)
- Add `confidence` field to facts (similar to lessons)
- Add git integration to detect when wiki files change and trigger re-verification
- Add a web UI for managing wiki facts
