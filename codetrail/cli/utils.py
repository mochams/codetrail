"""This module holds shared functions used in cli logic."""

import argparse

from codetrail import exceptions
from codetrail.cli import handlers


def match_commands(command: str, arguments: argparse.Namespace) -> None:
    """Match and execute the appropriate command based on user input.

    Args:
        command: The command string provided by the user (e.g., 'init').
        arguments: Parsed command-line arguments specific to the command.

    Raises:
        InvalidCommandError: In case of an incorrect command.
    """
    match command:
        case "init":
            handlers.init(arguments)
        case _:
            msg = "Invalid Command. Choose from (init,)"
            raise exceptions.InvalidCommandError(msg)
