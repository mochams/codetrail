"""Unit tests for module `command.utils`."""

from pathlib import Path
from unittest.mock import patch

import pytest

from codetrail import exceptions
from codetrail import utils
from codetrail.config import DEFAULT_CODETRAIL_DIRECTORY
from tests.utils import assert_file_has_content


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("temporary_dir", True),  # Temporary directory
        ("temporary_file", False),  # Temporary file
        ("noneexistent_dir", False),  # Non-existent path
    ],
)
def test_path_is_directory(path, expected, request):
    """Test path_is_directory with various scenarios."""
    path = request.getfixturevalue(path)
    assert utils.path_is_directory(path) == expected


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("temporary_dir", True),  # Temporary directory
        ("temporary_file", True),  # Temporary file
        ("noneexistent_dir", False),  # Non-existent directory
    ],
)
def test_path_exists(path, expected, request):
    """Test path_exists with various scenarios."""
    path = request.getfixturevalue(path)
    assert utils.path_exists(path) == expected


@pytest.mark.parametrize(
    ("path", "directory", "expected"),
    [
        ("temporary_dir", "objects", True),  # Temporary directory
        (  # noqa: PT014
            "temporary_dir",
            "objects",
            True,
        ),  # Existing temporary directory
        ("temporary_dir", "refs/heads", True),  # Temporary directory with parents
    ],
)
def test_make_directory(path, directory, expected, request):
    """Test make_directory with various scenarios."""
    path = request.getfixturevalue(path)
    utils.make_directory(path / directory)
    assert utils.path_exists(path / directory) == expected


@pytest.mark.parametrize(
    ("path", "directory", "expected"),
    [
        ("temporary_dir", "HEAD", True),  # Temporary file
        (  # noqa: PT014
            "temporary_dir",
            "HEAD",
            True,
        ),  # Existing temporary file
    ],
)
def test_make_file(path, directory, expected, request):
    """Test make_file with various scenarios."""
    path = request.getfixturevalue(path)
    utils.make_file(path / directory)
    assert utils.path_exists(path / directory) == expected


@pytest.mark.parametrize(
    ("path", "content", "expected"),
    [
        ("temporary_file", "Hello World", "Hello World\n"),
    ],
)
def test_write_to_file(path, content, expected, request):
    """Test write_to_file with various scenarios."""
    path = request.getfixturevalue(path)
    utils.write_to_file(path, content)

    assert_file_has_content(path, expected)


class TestFindRepositoryPath:
    """Tests for `find_repository_path` function."""

    def test_retruns_none_for_missing_repository_path(self, temporary_dir):
        """Test when the repository path is not found."""
        assert utils.find_repository_path(str(temporary_dir)) is None

    def test_returns_existing_repository_path(self, temporary_dir):
        """Test when the repository path is found."""
        repo_path = temporary_dir / "repo"
        repo_path.mkdir()
        (repo_path / DEFAULT_CODETRAIL_DIRECTORY).mkdir()

        result = utils.find_repository_path(str(repo_path))
        assert result == repo_path

    def test_stops_at_home_directory(self, temporary_dir):
        """Test stopping at the home directory."""
        with patch.object(Path, "home") as mock_home:
            temporary_home = temporary_dir / "home"
            temporary_home.mkdir()
            mock_home.return_value = temporary_home

            current_path = temporary_home / "Music"
            current_path.mkdir()

            assert utils.find_repository_path(str(current_path)) is None

    def test_returns_existing_repository_path_in_home_path(self, temporary_dir):
        """Test stopping at the home directory."""
        with patch.object(Path, "home") as mock_home:
            temporary_home = temporary_dir / "home"
            temporary_home.mkdir()
            (temporary_home / DEFAULT_CODETRAIL_DIRECTORY).mkdir()
            mock_home.return_value = temporary_home

            current_path = temporary_home / "Desktop"
            current_path.mkdir()

            result = utils.find_repository_path(str(current_path))
            assert result == temporary_home


class TestFindChildRepositoryPath:
    """Tests for `find_child_repository_path` function."""

    def test_retruns_none_for_missing_repository_path(self, temporary_dir):
        """Test when the repository path is not found."""
        assert utils.find_child_repository_path(str(temporary_dir)) is None

    def test_returns_existing_repository_path(self, temporary_dir):
        """Test when the repository path is found."""
        desired_repo_path = temporary_dir / "repo"
        desired_repo_path.mkdir()
        child_path = desired_repo_path / "Desktop/Library"
        child_path.mkdir(parents=True)
        (child_path / DEFAULT_CODETRAIL_DIRECTORY).mkdir()

        result = utils.find_child_repository_path(str(desired_repo_path))
        assert result == child_path
