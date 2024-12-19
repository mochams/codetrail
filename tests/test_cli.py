import argparse
import logging
from unittest.mock import patch

import pytest

from codetrail import cli
from codetrail import cmd_config
from codetrail import cmd_init
from codetrail import commands
from codetrail import exceptions


class TestRunCommands:
    """Tests for `run` function."""

    def test_run_init(self, argument_namespace):
        """Test `init` command."""
        with patch.object(cli, "init") as mock_run:
            cli.run("init", argument_namespace)
            mock_run.assert_called_once_with(argument_namespace)

    def test_run_config(self, argument_namespace):
        """Test `config` command."""
        with patch.object(cli, "config") as mock_run:
            cli.run("set", argument_namespace)
            mock_run.assert_called_once_with(argument_namespace)

    def test_raises_exception_on_wrong_command(self, argument_namespace):
        """Test with wrong command."""
        with pytest.raises(exceptions.InvalidCommandError):
            cli.run("invalid_command", argument_namespace)


class TestInit:
    """Tests for `init` function."""

    def test_calls_initialize_repository(self, temporary_dir):
        """Test valid initialization of the repository."""
        arguments = argparse.Namespace(command="init", path=temporary_dir)
        with patch.object(cmd_init, "initialize_repository") as mock_init_repo:
            cli.init(arguments)
            mock_init_repo.assert_called_once_with(
                commands.InitializeRepository(path=temporary_dir),
            )

    def test_logs_on_exception(self, temporary_dir, caplog):
        """Test logs error."""
        arguments = argparse.Namespace(command="init", path=temporary_dir)
        with (
            caplog.at_level(logging.ERROR),
            patch.object(cmd_init, "initialize_repository") as mock_init_repo,
        ):
            mock_init_repo.side_effect = exceptions.ExistingRepositoryError("Exists")
            cli.init(arguments)

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
        with patch.object(cmd_config, "set_config") as mock_set_config:
            cli.config(arguments)
            mock_set_config.assert_called_once_with(
                commands.SetConfig(key=arguments.key[0], value=arguments.value[0]),
            )

    def test_calls_get_config(self, temporary_dir):
        """Test getting of the configuration value."""
        arguments = argparse.Namespace(
            command="get",
            key=["user.name"],
        )
        with patch.object(cmd_config, "get_config") as mock_get_config:
            cli.config(arguments)
            mock_get_config.assert_called_once_with(
                commands.GetConfig(key=arguments.key[0]),
            )

    def test_calls_list_config(self, temporary_dir):
        """Test listing of the configuration."""
        arguments = argparse.Namespace(command="list")
        with patch.object(cmd_config, "list_config") as mock_list_config:
            cli.config(arguments)
            mock_list_config.assert_called_once_with(commands.ListConfig())

    def test_calls_unset_config(self, temporary_dir):
        """Test removing of the configuration value."""
        arguments = argparse.Namespace(
            command="unset",
            key=["user.name"],
        )
        with patch.object(cmd_config, "unset_config") as mock_unset_config:
            cli.config(arguments)
            mock_unset_config.assert_called_once_with(
                commands.UnsetConfig(key=arguments.key[0]),
            )

    def test_calls_edit_config(self, temporary_dir):
        """Test valid editing of the configuration."""
        arguments = argparse.Namespace(
            command="edit",
            key=["user.name"],
            value=["Chill Guy"],
        )
        with patch.object(cmd_config, "set_config") as mock_set_config:
            cli.config(arguments)
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
            cli.config(arguments)
