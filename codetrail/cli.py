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
        msg = f"Invalid Command '{command}'"
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
            cmd_config.set_config(
                commands.SetConfig(key=arguments.key[0], value=arguments.value[0]),
            )
        case "get":
            cmd_config.get_config(commands.GetConfig(key=arguments.key[0]))
        case "list":
            cmd_config.list_config(commands.ListConfig())
        case "unset":
            cmd_config.unset_config(commands.UnsetConfig(key=arguments.key[0]))
        case "edit":
            cmd_config.set_config(
                commands.SetConfig(key=arguments.key[0], value=arguments.value[0]),
            )
        case _:
            msg = f"Invalid Command '{arguments.command}'"
            raise exceptions.InvalidCommandError(msg)
