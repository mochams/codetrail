import argparse
import logging
from unittest.mock import patch

import pytest
from codetrail import cmd_init, exceptions, utils
from codetrail.commands import InitializeRepository
from codetrail.config import DEFAULT_CODETRAIL_DIRECTORY


def initialize_repository_command(path):
    return InitializeRepository(path=path)


class TestRunInit:
    """Tests for `run` function."""

    def test_calls_initialize_repository(self, temporary_dir):
        """Test valid initilization of the repository."""
        arguments = argparse.Namespace(command="init", path=temporary_dir)
        with patch("codetrail.cmd_init.initialize_repository") as mock_init_repo:
            cmd_init.run(arguments)
            mock_init_repo.assert_called_once_with(
                command=InitializeRepository(path=temporary_dir)
            )

    def test_logs_on_exception(self, temporary_dir, caplog):
        """Test logs error."""
        arguments = argparse.Namespace(command="init", path=temporary_dir)
        with (
            caplog.at_level(logging.ERROR),
            patch("codetrail.cmd_init.initialize_repository") as mock_init_repo,
        ):
            mock_init_repo.side_effect = exceptions.ExistingRepositoryError("Exists")
            cmd_init.run(arguments)

            assert "Exists" in caplog.text


class TestInitializeRepository:
    """Tests for `run` function."""

    def test_creates_initial_files(self, temporary_dir):
        """Test initializes repistory."""
        desired_dir = temporary_dir / "python-cache"

        cmd_init.initialize_repository(initialize_repository_command(desired_dir))

        assert utils.path_exists(desired_dir / ".codetrail")
        assert utils.path_exists(desired_dir / ".codetrail/objects")
        assert utils.path_exists(desired_dir / ".codetrail/refs/heads")
        assert utils.path_exists(desired_dir / ".codetrail/refs/tags")
        assert utils.path_exists(desired_dir / ".codetrail/description")
        assert utils.path_exists(desired_dir / ".codetrail/HEAD")
        assert utils.path_exists(desired_dir / ".codetrail/config")

    def test_creates_initial_files_in_existing_directory(self, temporary_dir):
        """Test initializes repistory in existing folder."""
        existing_dir = temporary_dir / "blog-app"
        existing_dir.mkdir()

        cmd_init.initialize_repository(initialize_repository_command(existing_dir))

        assert utils.path_exists(existing_dir / ".codetrail")
        assert utils.path_exists(existing_dir / ".codetrail/objects")
        assert utils.path_exists(existing_dir / ".codetrail/refs/heads")
        assert utils.path_exists(existing_dir / ".codetrail/refs/tags")
        assert utils.path_exists(existing_dir / ".codetrail/description")
        assert utils.path_exists(existing_dir / ".codetrail/HEAD")
        assert utils.path_exists(existing_dir / ".codetrail/config")

    def test_raises_eception_with_existing_parent_repository(self, temporary_dir):
        """Test initializes repistory in folder with parent folder having repository."""
        parent_dir = temporary_dir / "blog-app"
        parent_dir.mkdir()
        (parent_dir / DEFAULT_CODETRAIL_DIRECTORY).mkdir()

        desired_dir = parent_dir / "python-cache"
        desired_dir.mkdir()

        with pytest.raises(exceptions.ExistingRepositoryError):
            cmd_init.initialize_repository(initialize_repository_command(desired_dir))

    def test_raises_eception_with_existing_child_repository(self, temporary_dir):
        """Test initializes repistory in folder with child folder having repository."""
        parent_dir = temporary_dir / "blog-app"
        parent_dir.mkdir()

        desired_dir = parent_dir / "python-cache"
        desired_dir.mkdir()
        (desired_dir / DEFAULT_CODETRAIL_DIRECTORY).mkdir()

        with pytest.raises(exceptions.ExistingRepositoryError):
            cmd_init.initialize_repository(initialize_repository_command(parent_dir))

    def test_raise_exception_desired_path_not_valid_directory(self, temporary_file):
        with pytest.raises(NotADirectoryError):
            cmd_init.initialize_repository(
                initialize_repository_command(temporary_file)
            )
