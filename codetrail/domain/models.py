"""This module holds the domain objects."""

from functools import cached_property
from pathlib import Path

from codetrail import exceptions
from codetrail.config import DEFAULT_CODETRAIL_DIRECTORY


class CodeRepository:
    """A Codetrail repository.

    This class represents a Codetrail repository, managing the repository's work_tree
    and repo_dir. It provides utilities for working with repository paths, creating
    files, and directories within the repository structure.
    """

    work_tree: Path
    repo_dir: Path

    def __init__(self, path: Path | str, *, strict: bool = True) -> None:
        """Initialize a codetrail repository object.

        Args:
            path: The file system path to the repository's work tree.
            strict: Enable to enforce that the repository exists at the specified path.

        Raises:
            NotARepositoryError: If `strict` and the path is not a valid repository.
        """
        self.work_tree = Path(path)
        self.repo_dir = self.work_tree / DEFAULT_CODETRAIL_DIRECTORY

        if strict and not self.repo_dir.is_dir():
            msg = "Not a repository!"
            raise exceptions.NotARepositoryError(msg)

    @cached_property
    def abs_work_tree(self) -> Path:
        """Get the absolute path of work tree."""
        return self.work_tree.absolute()

    @cached_property
    def abs_repo_dir(self) -> Path:
        """Get the absolute path of repository dir."""
        return self.repo_dir.absolute()
