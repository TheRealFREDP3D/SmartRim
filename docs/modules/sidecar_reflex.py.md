# sidecar/reflex.py — Reflex Actor Sidecar Entry Point

Thin wrapper to run `ReflexActor` as standalone process.

## Content
```python
#!/usr/bin/env python3
"""Sidecar entry point for Layer 2 reflex actor."""

from smartrim.reflex_actor import ReflexActor

if __name__ == "__main__":
    actor = ReflexActor()
    # In practice, invoked by monitor with alerts/situation/game_state
    # This file exists for sidecar deployment pattern
```

## Purpose
- Allows running reflex actor in separate process
- Monitor can spawn/eval via subprocess
- Currently unused (monitor imports ReflexActor directly)

## Notes
- 108 lines (mostly comments)
- Duplicate of `src/smartrim/reflex_actor.py` main block
- Part of sidecar deployment architecture (not currently active)