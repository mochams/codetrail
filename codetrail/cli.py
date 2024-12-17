"""This package contains the command line app logic."""

import argparse

from codetrail import exceptions
from codetrail import handlers


def run(command: str, arguments: argparse.Namespace) -> None:
    """Match the command based to the appropriate handler.

    Args:
        command: The command string provided by the user (e.g., 'init').
        arguments: Parsed command-line arguments specific to the command.

    Raises:
        InvalidCommandError: In case of an incorrect command.
    """
    if command == "init":
        handlers.init(arguments)

    elif command in {"set", "unset", "get", "list", "edit"}:
        handlers.config(arguments)

    else:
        msg = f"Invalid Command '{command}'. Choose from (init,config)"
        raise exceptions.InvalidCommandError(msg)
