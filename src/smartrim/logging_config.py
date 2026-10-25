"""Logging configuration for SmartRim."""

import logging
import sys


# Configure root logger
def setup_logging(
    level: int = logging.INFO,
    log_file: str | None = None,
    format_string: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
) -> None:
    """Set up logging for SmartRim.

    Args:
        level: Logging level (default: INFO)
        log_file: Optional file path to write logs to
        format_string: Log message format
    """
    handlers = [logging.StreamHandler(sys.stdout)]
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(
        level=level,
        format=format_string,
        handlers=handlers,
    )

# Get a logger for modules
def get_logger(name: str) -> logging.Logger:
    """Get a logger with the given name."""
    return logging.getLogger(name)
