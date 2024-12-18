import pytest

from codetrail import exceptions
from codetrail import models
from codetrail.conf import DEFAULT_CODETRAIL_DIRECTORY


class TestCodetrailRepository:
    """Tests for `CodetrailRepository` class."""

    def test_initializes_without_strict_mode(self, temporary_dir):
        repo = models.CodetrailRepository(temporary_dir, strict=False)
        assert repo.work_tree == temporary_dir
        assert repo.repo_dir == temporary_dir / DEFAULT_CODETRAIL_DIRECTORY

    def test_initializes_with_strict_mode(self, temporary_dir, code_repository):
        repo = code_repository
        assert repo.work_tree == temporary_dir
        assert repo.repo_dir == temporary_dir / DEFAULT_CODETRAIL_DIRECTORY

    def test_raises_exception_in_strict_mode_missing_repo_dir(self, temporary_dir):
        with pytest.raises(exceptions.NotARepositoryError):
            models.CodetrailRepository(temporary_dir)

    def test_raises_exception_in_strict_mode_missing_config_file(
        self,
        temporary_dir,
        code_repository,
    ):
        code_repository.config_path.unlink()
        with pytest.raises(exceptions.MissingConfigurationFileError):
            models.CodetrailRepository(temporary_dir)
