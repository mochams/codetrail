"""Logging configuration for the codetrail application.

This module initializes the logging settings for the application. It sets up a logger
named 'codetrail' and configures its log level at 'INFO'

"""

from __future__ import annotations

import logging
from typing import Final

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
logger: Final = logging.getLogger("codetrail")
logger.setLevel(level=logging.INFO)
