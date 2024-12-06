from unittest.mock import patch
import pytest
from codetrail import exceptions, utils
from codetrail.config import DEFAULT_CODETRAIL_DIRECTORY
from codetrail.repository import CodetrailRepository


class TestCodetrailRepository:
    """Tests for `CodetrailRepository` class."""

    def test_initializes_without_strict_mode(self, temporary_dir):
        repo = CodetrailRepository(temporary_dir, strict=False)
        assert repo.worktree == temporary_dir
        assert repo.repodir == temporary_dir / DEFAULT_CODETRAIL_DIRECTORY

    def test_initializes_with_strict_mode(self, temporary_dir):
        repo_dir = temporary_dir / DEFAULT_CODETRAIL_DIRECTORY
        repo_dir.mkdir()
        repo = CodetrailRepository(temporary_dir)
        assert repo.worktree == temporary_dir
        assert repo.repodir == temporary_dir / DEFAULT_CODETRAIL_DIRECTORY

    def test_raises_exceptio_in_strict_mode_missing_repo_dir(self, temporary_dir):
        with pytest.raises(exceptions.NotARepositoryError):
            CodetrailRepository(temporary_dir)

    def test_makes_directory_in_repo_dir(self, repository):
        test_dir = "test_directory"
        repository.make_directory(test_dir)
        assert (repository.repodir / test_dir).is_dir()

    def test_makes_file_in_repo_dir(self, repository):
        test_dir = "test_file.txt"
        repository.make_file(test_dir)
        assert (repository.repodir / test_dir).is_file()
