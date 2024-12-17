"""This package contains the domain model logic."""

import configparser
from functools import cached_property
from pathlib import Path

from codetrail import exceptions
from codetrail.conf import CONFIG_FILE
from codetrail.conf import DEFAULT_CODETRAIL_DIRECTORY


class CodetrailRepository:
    """A Codetrail repository.

    This class represents a Codetrail repository, managing the repository's work_tree
    and repo_dir. It provides utilities for working with repository paths, creating
    files, and directories within the repository structure.
    """

    work_tree: Path
    repo_dir: Path
    config_path: Path

    def __init__(self, path: Path | str, *, strict: bool = True) -> None:
        """Initialize a codetrail repository object.

        Args:
            path: The file system path to the repository's work tree.
            strict: Enable to enforce that the repository exists at the specified path.

        Raises:
            NotARepositoryError: If `strict` and the path is not a valid repository.
            MissingConfigurationFileError: Missing or invalid configuration file.
        """
        self.work_tree = Path(path)
        self.repo_dir = self.work_tree / DEFAULT_CODETRAIL_DIRECTORY
        self.config = configparser.ConfigParser()

        if strict and not self.repo_dir.is_dir():
            msg = "There is no repository in the path!"
            raise exceptions.NotARepositoryError(msg)

        self.config_path = self.repo_dir / CONFIG_FILE
        config_exists = self.config_path.exists() and self.config_path.is_file()

        if strict and config_exists:
            self.config.read(self.config_path)
        elif strict:
            msg = "The configuration file is missing or it is not a valid file."
            raise exceptions.MissingConfigurationFileError(msg)

    @cached_property
    def abs_work_tree(self) -> Path:
        """Get the absolute path of work tree."""
        return self.work_tree.absolute()

    @cached_property
    def abs_repo_dir(self) -> Path:
        """Get the absolute path of repository dir."""
        return self.repo_dir.absolute()
