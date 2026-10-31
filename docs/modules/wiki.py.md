# wiki.py — RimWorld Wiki Fetch & Convert

Downloads wiki pages, converts HTML to clean markdown for LLM context.

## Commands
```bash
python -m smartrim.wiki fetch    # Download raw HTML to memory/wiki/raw/
python -m smartrim.wiki convert  # Convert raw HTML → memory/wiki/*.md
```

## Manifest (`memory/wiki/manifest.json`)
```json
{
  "pages": {
    "Food": {"url": "https://rimworldwiki.com/wiki/Food", "fetched": "2026-10-30", "selector": "#mw-content-text"},
    "Medicine": {"url": "...", "selector": "..."}
  }
}
```

## Functions

| Function | Description |
|----------|-------------|
| `fetch_pages()` | Download all pages in manifest |
| `_strip_html(html, selector)` | Extract main content, remove nav/sidebar/scripts |
| `convert_pages()` | Convert raw HTML → markdown (markdownify) |
| `main()` | CLI entry (fetch/convert subcommands) |

## Page Selection
- Target pages defined in manifest
- CSS selector per page (default `#mw-content-text`)
- Only main article content kept

## Output
- `memory/wiki/raw/*.html` — raw downloads (gitignored)
- `memory/wiki/*.md` — clean markdown (tracked in git, read by LLM)

## Regeneration
```bash
python -m smartrim.wiki fetch
python -m smartrim.wiki convert
```

## Notes
- 372 lines
- Uses `markdownify` for HTML→MD conversion
- Wiki cache is LLM's knowledge base for game mechanics
- Run periodically to update for game patches