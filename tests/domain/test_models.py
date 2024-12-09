import pytest

from codetrail import exceptions
from codetrail.config import DEFAULT_CODETRAIL_DIRECTORY
from codetrail.domain import models


class TestCodetrailRepository:
    """Tests for `CodetrailRepository` class."""

    def test_initializes_without_strict_mode(self, temporary_dir):
        repo = models.CodeRepository(temporary_dir, strict=False)
        assert repo.work_tree == temporary_dir
        assert repo.repo_dir == temporary_dir / DEFAULT_CODETRAIL_DIRECTORY

    def test_initializes_with_strict_mode(self, temporary_dir):
        repo_dir = temporary_dir / DEFAULT_CODETRAIL_DIRECTORY
        repo_dir.mkdir()
        repo = models.CodeRepository(temporary_dir)
        assert repo.work_tree == temporary_dir
        assert repo.repo_dir == temporary_dir / DEFAULT_CODETRAIL_DIRECTORY

    def test_raises_exception_in_strict_mode_missing_repo_dir(self, temporary_dir):
        with pytest.raises(exceptions.NotARepositoryError):
            models.CodeRepository(temporary_dir)
