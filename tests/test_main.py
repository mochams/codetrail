"""Tests for main entrypoint."""

import logging
from unittest.mock import MagicMock
from unittest.mock import patch

from codetrail.__main__ import main  # noqa: PLC2701


def test_main_logs_message():
    """Test that main logs a welcome message."""
    with (
        patch("sys.argv", ["codetrail", "init", "/some/path"]),
        patch("codetrail.__main__.parsers.arg_parser.parse_args") as mock_parser,
        patch("codetrail.__main__.cli.run") as mock_match_commands,
    ):
        mock_args = MagicMock()
        mock_args.command = "init"
        mock_args.path = "/some/path"
        mock_parser.return_value = mock_args

        main()

        mock_parser.assert_called_once_with(["init", "/some/path"])
        mock_match_commands.assert_called_once_with("init", mock_args)
