"""This module holds all command line handlers."""

import argparse

from codetrail import commands
from codetrail import exceptions
from codetrail.cmd_config import set_config
from codetrail.cmd_init import initialize_repository
from codetrail.conf import LOGGER


def init(arguments: argparse.Namespace) -> None:
    """Handle the initialization command by creating a new repository.

    Args:
        arguments: Parsed command-line arguments containing the target path.
    """
    LOGGER.info("Initializing a new repository.")
    try:
        command = commands.InitializeRepository(path=arguments.path)
        initialize_repository(command)
    except (exceptions.ExistingRepositoryError, NotADirectoryError) as e:
        LOGGER.error(str(e))


def config(arguments: argparse.Namespace) -> None:
    """Handle the config management command.

    Args:
        arguments: Parsed command-line arguments.
    """
    try:
        run_config(arguments)
    except exceptions.UnsupportedConfigError as e:
        LOGGER.error(str(e))


def run_config(arguments: argparse.Namespace) -> None:
    """Match the config command based to the appropriate handler.

    Args:
        arguments: Parsed command-line arguments.

    Raises:
        InvalidCommandError: In case of an incorrect command.
    """
    match arguments.command:
        case "set":
            command = commands.SetConfig(key=arguments.key[0], value=arguments.value[0])
            set_config(command)
        case _:
            msg = f"Invalid Command '{arguments.command}'. Choose from (set,)"
            raise exceptions.InvalidCommandError(msg)
