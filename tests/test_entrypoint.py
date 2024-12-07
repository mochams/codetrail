"""Tests for main entrypoint."""

import logging
from unittest.mock import MagicMock, patch

import pytest

from codetrail import cmd_init, exceptions
from codetrail.__main__ import main, match_commands  # noqa: PLC2701


def test_main_logs_message(caplog):
    """Test that main logs a weilcome message."""
    with (
        caplog.at_level(logging.INFO),
        patch("sys.argv", ["codetrail", "init", "/some/path"]),
        patch("codetrail.__main__.argparser.parse_args") as mock_parser,
        patch("codetrail.__main__.match_commands") as mock_match_commands,
    ):
        mock_args = MagicMock()
        mock_args.command = "init"
        mock_args.path = "/some/path"
        mock_parser.return_value = mock_args

        main()

        mock_parser.assert_called_once_with(["init", "/some/path"])
        mock_match_commands.assert_called_once_with("init", mock_args)

        assert "Welcome to codetrail!" in caplog.text


class TestMatchCommands:
    """Tests for `match_commands` function."""

    def test_run_init(self, argument_namespace):
        """Test `init` command."""
        with patch.object(cmd_init, "run") as mock_run:
            match_commands("init", argument_namespace)
            mock_run.assert_called_once_with(argument_namespace)

    def test_raises_exception_on_wrong_command(self, argument_namespace):
        with pytest.raises(exceptions.InvalidCommandError):
            match_commands("invalid_command", argument_namespace)
