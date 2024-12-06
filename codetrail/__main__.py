"""This is the entrypoint to our cli application."""

import argparse
import sys

from codetrail import cmd_init
from codetrail import exceptions
from codetrail.config import LOGGER
from codetrail.parsers import argparser


def main() -> None:
    """Entrypoint for the version control system."""
    LOGGER.info("Welcome to codetrail!")
    args = argparser.parse_args(sys.argv[1:])
    match_commands(args.command, args)


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
            cmd_init.run(arguments)
        case _:
            msg = "Invalid Command. Choose from (init,)"
            raise exceptions.InvalidCommandError(msg)


if __name__ == "__main__":
    main()
