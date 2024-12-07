"""This module holds the logic to initialize repository.

Usage:
    codetrail init <path>
"""

import argparse

from codetrail import exceptions
from codetrail import utils
from codetrail.config import LOGGER
from codetrail.repository import CodetrailRepository


def run(arguments: argparse.Namespace) -> None:
    """Handle the initialization command by creating a new repository.

    Args:
        arguments: Parsed command-line arguments containing the target path.
    """
    LOGGER.info("Initializing a new repository.")
    try:
        initialize_repository(arguments.path)
    except (exceptions.ExistingRepositoryError, NotADirectoryError) as e:
        LOGGER.error(str(e))


def initialize_repository(path: str) -> None:
    """Initialize a new, empty repository.

    Args:
        path: The path where the repository should be created.

    Raises:
        NotADirectoryError: If the specified path is not a directory.
        ExistingRepositoryError: If the path parents/children has a repository.
    """
    parent_repository = utils.find_repository_path(path)
    if parent_repository:
        msg = f"Found an existing repository at {parent_repository}. Exiting!"
        raise exceptions.ExistingRepositoryError(msg)

    repository = CodetrailRepository(path, strict=False)
    if utils.path_exists(repository.worktree):
        if not utils.path_is_directory(repository.worktree):
            msg = ""
            raise NotADirectoryError(msg)

        child_repository = utils.find_child_repository_path(path)
        if child_repository:
            msg = f"Found an existing repository at {child_repository}. Exiting!"
            raise exceptions.ExistingRepositoryError(msg)
    else:
        utils.make_directory(repository.worktree)

    make_initial_directories(repository)
    make_initial_files(repository)
    write_to_initial_files(repository)

    LOGGER.info(f"Initialized new repository at {repository.absolute_worktree}.")
    LOGGER.info(f"New codetrail directory at {repository.absolute_repodir}.")


def make_initial_directories(repository: CodetrailRepository) -> None:
    """Create the initial directory structure for a new repository.

    Args:
        repository: An instance of the repository.
    """
    repository.make_directory("objects")
    repository.make_directory("refs/tags")
    repository.make_directory("refs/heads")


def make_initial_files(repository: CodetrailRepository) -> None:
    """Create the initial files required for a new repository.

    Args:
        repository: An instance of the repository.
    """
    repository.make_file("description")
    repository.make_file("HEAD")
    repository.make_file("config")


def write_to_initial_files(repository: CodetrailRepository) -> None:
    """Write content to a initial files.

    Args:
        repository: An instance of the repository.
    """
    utils.write_to_file(
        repository.repository_path("description"),
        "Unnamed repository; edit this file 'description' to name the repository.",
    )
    utils.write_to_file(
        repository.repository_path("HEAD"),
        "ref: refs/heads/master",
    )
