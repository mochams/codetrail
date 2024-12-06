"""This module holds the object representing the repository."""

from functools import cached_property
from pathlib import Path

from codetrail import exceptions
from codetrail import utils
from codetrail.config import DEFAULT_CODETRAIL_DIRECTORY


class CodetrailRepository:
    """A Codetrail repository.

    This class represents a Codetrail repository, managing the repository's worktree
    and repodir. It provides utilities for working with repository paths, creating
    files, and directories within the repository structure.
    """

    worktree: Path
    repodir: Path

    def __init__(self, path: Path | str, *, strict: bool = True) -> None:
        """Initialize a codetrail repository object.

        Args:
            path: The file system path to the repository's worktree.
            strict: Enable to enforce that the repository exists at the specified path.

        Raises:
            NotARepositoryError: If `strict` and the path is not a valid repository.
        """
        self.worktree = Path(path)
        self.repodir = self.worktree / DEFAULT_CODETRAIL_DIRECTORY

        if strict and not utils.path_is_directory(self.repodir):
            msg = "Not a repository!"
            raise exceptions.NotARepositoryError(msg)

    @cached_property
    def absolute_worktree(self) -> Path:
        """Get the absolute path of worktree."""
        return self.worktree.absolute()

    @cached_property
    def absolute_repodir(self) -> Path:
        """Get the absolute path of repodir."""
        return self.repodir.absolute()

    def repository_path(self, path: str) -> Path:
        """Get the full path to a file or directory in the repository.

        Args:
            path: A relative path within the repository.

        Returns:
            The full Path object pointing to the specified location in the repository.
        """
        return self.repodir / path

    def make_file(self, path: str) -> None:
        """Create a file in the repository directory.

        Args:
            path: The relative path to the file to create within the repository.
        """
        utils.make_file(self.repository_path(path))

    def make_directory(self, path: str) -> None:
        """Make a directory in the repository directory.

        Args:
            path: The relative path to the directory to create within the repository.
        """
        utils.make_directory(self.repository_path(path))
