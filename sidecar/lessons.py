"""Backward-compatible shim.

All implementation lives in ``situation.py`` (single source of truth). This
module re-exports it so existing imports and CLI entry points keep working.
"""

from situation import *  # noqa: F401,F403
from situation import main as _main


def main(argv=None):
    _main(argv)


if __name__ == "__main__":
    main()