from unittest.mock import patch

import pytest

from codetrail import exceptions
from codetrail.cli import handlers
from codetrail.cli import utils


class TestMatchCommands:
    """Tests for `match_commands` function."""

    def test_run_init(self, argument_namespace):
        """Test `init` command."""
        with patch.object(handlers, "init") as mock_run:
            utils.match_commands("init", argument_namespace)
            mock_run.assert_called_once_with(argument_namespace)

    def test_raises_exception_on_wrong_command(self, argument_namespace):
        with pytest.raises(exceptions.InvalidCommandError):
            utils.match_commands("invalid_command", argument_namespace)
