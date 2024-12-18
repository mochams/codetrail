import argparse
import logging
from unittest.mock import patch

import pytest

from codetrail import commands
from codetrail import exceptions
from codetrail import handlers


class TestInit:
    """Tests for `init` function."""

    def test_calls_initialize_repository(self, temporary_dir):
        """Test valid initialization of the repository."""
        arguments = argparse.Namespace(command="init", path=temporary_dir)
        with patch(
            "codetrail.handlers.initialize_repository",
        ) as mock_init_repo:
            handlers.init(arguments)
            mock_init_repo.assert_called_once_with(
                commands.InitializeRepository(path=temporary_dir),
            )

    def test_logs_on_exception(self, temporary_dir, caplog):
        """Test logs error."""
        arguments = argparse.Namespace(command="init", path=temporary_dir)
        with (
            caplog.at_level(logging.ERROR),
            patch(
                "codetrail.handlers.initialize_repository",
            ) as mock_init_repo,
        ):
            mock_init_repo.side_effect = exceptions.ExistingRepositoryError("Exists")
            handlers.init(arguments)

            assert "Exists" in caplog.text


class TestConfig:
    """Tests for `config` function."""

    def test_calls_set_config(self, temporary_dir):
        """Test valid setting of the configuration."""
        arguments = argparse.Namespace(
            command="set",
            key=["user.name"],
            value=["Chill Guy"],
        )
        with patch(
            "codetrail.handlers.set_config",
        ) as mock_set_config:
            handlers.config(arguments)
            mock_set_config.assert_called_once_with(
                commands.SetConfig(key=arguments.key[0], value=arguments.value[0]),
            )

    def test_raises_exception_on_wrong_command(self, argument_namespace):
        """Test with wrong command."""
        arguments = argparse.Namespace(
            command="set it",
            key=["user.name"],
            value=["Chill Guy"],
        )
        with pytest.raises(exceptions.InvalidCommandError):
            handlers.config(arguments)
