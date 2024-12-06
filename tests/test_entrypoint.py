"""Tests for main entrypoint."""

import logging

from codetrail.__main__ import main  # noqa: PLC2701


def test_main_logs_message(caplog):
    """Test that main logs a weilcome message."""
    with caplog.at_level(logging.INFO):
        main()

    assert "You've reached entrypoint, Hello Codetrail!" in caplog.text
