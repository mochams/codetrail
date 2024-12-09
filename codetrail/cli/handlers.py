"""This module holds all command line handlers."""

import argparse

from codetrail import exceptions
from codetrail.application import commands
from codetrail.application import initialize_repository
from codetrail.config import LOGGER


def init(arguments: argparse.Namespace) -> None:
    """Handle the initialization command by creating a new repository.

    Args:
        arguments: Parsed command-line arguments containing the target path.
    """
    LOGGER.info("Initializing a new repository.")
    try:
        initialize_repository(commands.InitializeRepository(path=arguments.path))
    except (exceptions.ExistingRepositoryError, NotADirectoryError) as e:
        LOGGER.error(str(e))
