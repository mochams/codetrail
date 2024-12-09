"""This module holds the configuration for the application."""

from __future__ import annotations

import logging
from typing import Final

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
LOGGER: Final = logging.getLogger("codetrail")
LOGGER.setLevel(level=logging.INFO)

DEFAULT_CODETRAIL_DIRECTORY = ".codetrail"
DEFAULT_REPOSITORY_DESCRIPTION = (
    "Unnamed repository; edit this file 'description' to name the repository."
)
DEFAULT_REPOSITORY_HEAD = "ref: refs/heads/master"
