import argparse
import logging
from unittest.mock import patch

from codetrail import exceptions
from codetrail.application import commands
from codetrail.cli import handlers


class TestInit:
    """Tests for `run` function."""

    def test_calls_initialize_repository(self, temporary_dir):
        """Test valid initialization of the repository."""
        arguments = argparse.Namespace(command="init", path=temporary_dir)
        with patch("codetrail.cli.handlers.initialize_repository") as mock_init_repo:
            handlers.init(arguments)
            mock_init_repo.assert_called_once_with(
                commands.InitializeRepository(path=temporary_dir),
            )

    def test_logs_on_exception(self, temporary_dir, caplog):
        """Test logs error."""
        arguments = argparse.Namespace(command="init", path=temporary_dir)
        with (
            caplog.at_level(logging.ERROR),
            patch("codetrail.cli.handlers.initialize_repository") as mock_init_repo,
        ):
            mock_init_repo.side_effect = exceptions.ExistingRepositoryError("Exists")
            handlers.init(arguments)

            assert "Exists" in caplog.text
