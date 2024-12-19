"""This module holds the configuration for the application."""

from __future__ import annotations

import logging
import sys
from typing import Final


class CodetrailFormatter(logging.Formatter):
    """Custom formatter for Codetrail logs."""

    log_format: str = "%(message)s"
    red: str = "\033[1;31m"
    green: str = "\033[1;32m"
    yellow: str = "\033[1;33m"
    reset: str = "\033[1;0m"

    FORMATS = {
        logging.INFO: f"{green}{log_format}{reset}",
        logging.WARNING: f"{yellow}{log_format}{reset}",
        logging.ERROR: f"{red}{log_format}{reset}",
    }

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record.

        Returns:
            str: The formatted log record.
        """
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)


LOGGER: Final = logging.getLogger("codetrail")
LOGGER.setLevel(level=logging.INFO)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(CodetrailFormatter())
handler.setLevel(level=logging.INFO)
LOGGER.addHandler(handler)

DEFAULT_CODETRAIL_DIRECTORY = ".codetrail"
DEFAULT_REPOSITORY_DESCRIPTION = (
    "Unnamed repository; edit this file 'description' to name the repository."
)
DEFAULT_REPOSITORY_HEAD = "ref: refs/heads/master"

CONFIG_FILE = "config"
HEAD_FILE = "HEAD"
DESCRIPTION_FILE = "description"

DEFAULT_CURRENT_PATH = "."

CONFIG_SECTIONS = ["user", "core"]
CONFIG_USER_OPTIONS = ["name", "email"]
