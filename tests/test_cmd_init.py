import pytest

from codetrail import commands
from codetrail import exceptions
from codetrail import utils
from codetrail.cmd_init import initialize_repository
from codetrail.conf import DEFAULT_CODETRAIL_DIRECTORY


def initialize_repository_command(path):
    return commands.InitializeRepository(path=path)


class TestInitializeRepository:
    """Tests for `initialize_repository` function."""

    def test_creates_initial_files(self, temporary_dir):
        """Test initializes repository."""
        desired_dir = temporary_dir / "python-cache"

        initialize_repository(initialize_repository_command(desired_dir))

        assert utils.path_exists(desired_dir / ".codetrail")
        assert utils.path_exists(desired_dir / ".codetrail/objects")
        assert utils.path_exists(desired_dir / ".codetrail/refs/heads")
        assert utils.path_exists(desired_dir / ".codetrail/refs/tags")
        assert utils.path_exists(desired_dir / ".codetrail/description")
        assert utils.path_exists(desired_dir / ".codetrail/HEAD")
        assert utils.path_exists(desired_dir / ".codetrail/config")

    def test_creates_initial_files_in_existing_directory(self, temporary_dir):
        """Test initializes repository in existing folder."""
        existing_dir = temporary_dir / "blog-app"
        existing_dir.mkdir()

        initialize_repository(initialize_repository_command(existing_dir))

        assert utils.path_exists(existing_dir / ".codetrail")
        assert utils.path_exists(existing_dir / ".codetrail/objects")
        assert utils.path_exists(existing_dir / ".codetrail/refs/heads")
        assert utils.path_exists(existing_dir / ".codetrail/refs/tags")
        assert utils.path_exists(existing_dir / ".codetrail/description")
        assert utils.path_exists(existing_dir / ".codetrail/HEAD")
        assert utils.path_exists(existing_dir / ".codetrail/config")

    def test_raises_exception_with_existing_parent_repository(self, temporary_dir):
        """Test initializes repository in folder with parent folder having repository."""
        parent_dir = temporary_dir / "blog-app"
        parent_dir.mkdir()
        (parent_dir / DEFAULT_CODETRAIL_DIRECTORY).mkdir()

        desired_dir = parent_dir / "python-cache"
        desired_dir.mkdir()

        with pytest.raises(exceptions.ExistingRepositoryError):
            initialize_repository(initialize_repository_command(desired_dir))

    def test_raises_exception_with_existing_child_repository(self, temporary_dir):
        """Test initializes repository in folder with child folder having repository."""
        parent_dir = temporary_dir / "blog-app"
        parent_dir.mkdir()

        desired_dir = parent_dir / "python-cache"
        desired_dir.mkdir()
        (desired_dir / DEFAULT_CODETRAIL_DIRECTORY).mkdir()

        with pytest.raises(exceptions.ExistingRepositoryError):
            initialize_repository(initialize_repository_command(parent_dir))

    def test_raise_exception_desired_path_not_valid_directory(self, temporary_file):
        with pytest.raises(NotADirectoryError):
            initialize_repository(initialize_repository_command(temporary_file))
