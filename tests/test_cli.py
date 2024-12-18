from unittest.mock import patch

import pytest

from codetrail import cli
from codetrail import exceptions
from codetrail import handlers


class TestRunCommands:
    """Tests for `run` function."""

    def test_run_init(self, argument_namespace):
        """Test `init` command."""
        with patch.object(handlers, "init") as mock_run:
            cli.run("init", argument_namespace)
            mock_run.assert_called_once_with(argument_namespace)

    def test_run_config(self, argument_namespace):
        """Test `config` command."""
        with patch.object(handlers, "config") as mock_run:
            cli.run("set", argument_namespace)
            mock_run.assert_called_once_with(argument_namespace)

    def test_raises_exception_on_wrong_command(self, argument_namespace):
        """Test with wrong command."""
        with pytest.raises(exceptions.InvalidCommandError):
            cli.run("invalid_command", argument_namespace)
