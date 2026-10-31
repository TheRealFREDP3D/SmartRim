# logging_config.py — Logging Setup

Simple logging configuration.

## Functions

| Function | Description |
|----------|-------------|
| `setup_logging(level=logging.INFO)` | Configure root logger with console handler |
| `get_logger(name)` | Get module logger |

## Usage
```python
from smartrim.logging_config import setup_logging, get_logger
setup_logging(logging.INFO)
logger = get_logger(__name__)
```