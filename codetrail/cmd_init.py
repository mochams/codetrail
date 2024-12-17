"""This module holds the logic to initialize repository.

Usage:
    codetrail init <path>
"""

from configparser import ConfigParser
from pathlib import Path

from codetrail import commands
from codetrail import exceptions
from codetrail import models
from codetrail import utils
from codetrail.conf import CONFIG_FILE
from codetrail.conf import CONFIG_SECTIONS
from codetrail.conf import DEFAULT_REPOSITORY_DESCRIPTION
from codetrail.conf import DEFAULT_REPOSITORY_HEAD
from codetrail.conf import DESCRIPTION_FILE
from codetrail.conf import HEAD_FILE
from codetrail.conf import LOGGER


def initialize_repository(command: commands.InitializeRepository) -> None:
    """Initialize a new, empty repository.

    Args:
        command: The command responsible for initializing a repository.

    Raises:
        NotADirectoryError: If the specified path is not a directory.
        ExistingRepositoryError: If the path parents/children has a repository.
    """
    parent_repository = utils.find_repository_path(command.path)
    if parent_repository:
        msg = f"Found an existing repository at {parent_repository}. Exiting!"
        raise exceptions.ExistingRepositoryError(msg)

    repository = models.CodetrailRepository(path=command.path, strict=False)
    if utils.path_exists(repository.work_tree):
        if not utils.path_is_directory(repository.work_tree):
            msg = ""
            raise NotADirectoryError(msg)

        child_repository = utils.find_child_repository_path(command.path)
        if child_repository:
            msg = f"Found an existing repository at {child_repository}. Exiting!"
            raise exceptions.ExistingRepositoryError(msg)

    make_initial_directories(repository.repo_dir)
    make_initial_files(repository.repo_dir)
    write_to_initial_files(repository.repo_dir)
    write_to_initial_config(repository.config_path, repository.config)

    LOGGER.info(f"Initialized new repository at {repository.abs_work_tree}.")
    LOGGER.info(f"New codetrail directory at {repository.abs_repo_dir}.")


def make_initial_directories(path: Path) -> None:
    """Create the initial directory structure for a new repository.

    Args:
        path: The repository path.
    """
    utils.make_directory(path / "objects")
    utils.make_directory(path / "refs/tags")
    utils.make_directory(path / "refs/heads")


def make_initial_files(path: Path) -> None:
    """Create the initial files required for a new repository.

    Args:
        path: The repository path.
    """
    utils.make_file(path / DESCRIPTION_FILE)
    utils.make_file(path / HEAD_FILE)
    utils.make_file(path / CONFIG_FILE)


def write_to_initial_files(path: Path) -> None:
    """Write content to a initial files.

    Args:
        path: The repository path.
    """
    utils.write_to_file(
        path / DESCRIPTION_FILE,
        DEFAULT_REPOSITORY_DESCRIPTION,
    )
    utils.write_to_file(path / HEAD_FILE, DEFAULT_REPOSITORY_HEAD)


def write_to_initial_config(path: Path, config: ConfigParser) -> None:
    """Write content to a initial files.

    Args:
        path: The repository path.
        config: The repository configuration parser instance.
    """
    for section in CONFIG_SECTIONS:
        config.add_section(section)
    utils.write_to_config_file(path, config)
