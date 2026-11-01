# sidecar/replay.py — Replay Harness Sidecar Entry Point

Thin wrapper for `smartrim.replay` module.

## Content
```python
#!/usr/bin/env python3
"""Sidecar entry point for replay harness."""

from smartrim.replay import main

if __name__ == "__main__":
    main()
```

## Purpose
- Standalone entry point for replay testing
- Can be run in isolated environment
- Delegates to `src/smartrim/replay.py:main()`

## Notes
- 318 lines (with comments)
- Duplicate entry point for sidecar deployment
- See `src/smartrim/replay.py` for full documentation