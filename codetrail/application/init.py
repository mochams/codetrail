"""This module holds the logic to initialize repository.

Usage:
    codetrail init <path>
"""

from pathlib import Path

from codetrail import exceptions
from codetrail.application import utils
from codetrail.application.commands import InitializeRepository
from codetrail.config import DEFAULT_REPOSITORY_DESCRIPTION
from codetrail.config import DEFAULT_REPOSITORY_HEAD
from codetrail.config import LOGGER
from codetrail.domain import models


def initialize_repository(command: InitializeRepository) -> None:
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

    repository = models.CodeRepository(path=command.path, strict=False)
    if utils.path_exists(repository.work_tree):
        if not utils.path_is_directory(repository.work_tree):
            msg = ""
            raise NotADirectoryError(msg)

        child_repository = utils.find_child_repository_path(command.path)
        if child_repository:
            msg = f"Found an existing repository at {child_repository}. Exiting!"
            raise exceptions.ExistingRepositoryError(msg)
    else:
        utils.make_directory(repository.work_tree)

    make_initial_directories(repository.repo_dir)
    make_initial_files(repository.repo_dir)
    write_to_initial_files(repository.repo_dir)

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
    utils.make_file(path / "description")
    utils.make_file(path / "HEAD")
    utils.make_file(path / "config")


def write_to_initial_files(path: Path) -> None:
    """Write content to a initial files.

    Args:
        path: The repository path.
    """
    utils.write_to_file(
        path / "description",
        DEFAULT_REPOSITORY_DESCRIPTION,
    )
    utils.write_to_file(path / "HEAD", DEFAULT_REPOSITORY_HEAD)
