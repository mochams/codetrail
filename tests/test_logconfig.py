"""Tests for 'codetrail.logconfig`."""

import logging

from codetrail.logconfig import logger


def test_logger_name_is_codetrail():
    """Test that the logger has the correct name."""
    assert logger.name == "codetrail"


def test_log_level_is_info():
    """Test that the log level is set correctly from the environment."""
    assert logger.level == logging.INFO


def test_log_output(caplog):
    """Test that log messages are formatted and emitted correctly."""
    test_message = "Test log message"

    with caplog.at_level(logging.INFO):
        logger.info(test_message)

    assert test_message in caplog.text
    assert "INFO" in caplog.text
    assert "codetrail" in caplog.text
