"""This package contains the command line app logic."""

import argparse

from codetrail import cmd_config
from codetrail import cmd_init
from codetrail import commands
from codetrail import exceptions
from codetrail.conf import LOGGER


def run(command: str, arguments: argparse.Namespace) -> None:
    """Match the command based to the appropriate handler.

    Args:
        command: The command string provided by the user (e.g., 'init').
        arguments: Parsed command-line arguments specific to the command.

    Raises:
        InvalidCommandError: In case of an incorrect command.
    """
    if command == "init":
        init(arguments)

    elif command in {"set", "unset", "get", "list", "edit"}:
        config(arguments)

    else:
        msg = f"Invalid Command '{command}'. Choose from (init,config)"
        raise exceptions.InvalidCommandError(msg)


def init(arguments: argparse.Namespace) -> None:
    """Handle the initialization command by creating a new repository.

    Args:
        arguments: Parsed command-line arguments containing the target path.
    """
    try:
        command = commands.InitializeRepository(path=arguments.path)
        cmd_init.initialize_repository(command)
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
            cmd_config.set_config(command)
        case "get":
            command = commands.GetConfig(key=arguments.key[0])
            cmd_config.get_config(command)
        case "list":
            command = commands.ListConfig()
            cmd_config.list_config(command)
        case _:
            msg = f"Invalid Command '{arguments.command}'. Choose from (set,get)"
            raise exceptions.InvalidCommandError(msg)
