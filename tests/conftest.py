"""This module contains global fixtures for the tests."""

import argparse
import logging
from pathlib import Path
from unittest.mock import patch

import pytest

from codetrail.config import DEFAULT_CODETRAIL_DIRECTORY
from codetrail.repository import CodetrailRepository


@pytest.fixture
def temporary_dir(tmp_path):
    """Provide a temporary directory.

    Returns:
        The temporay directory.
    """
    directory = tmp_path / "sub"
    directory.mkdir()
    return directory


@pytest.fixture
def temporary_file(temporary_dir):
    """Provide a temporary file.

    Returns:
        The temporay directory.
    """
    file = temporary_dir / "hello.txt"
    file.write_text("content", encoding="utf-8")
    return file


@pytest.fixture
def noneexistent_dir():
    """Provide a nonexistent directory.

    Returns:
        The nonexistent directory.
    """
    return Path("/nonexistent/path/")


@pytest.fixture
def noneexistent_file():
    """Provide a nonexistent file.

    Returns:
        The nonexistent file.
    """
    return Path("/nonexistent/path/hello.txt")


@pytest.fixture
def argument_namespace():
    """Provide an argparse namespace.

    Returns:
        The arguments Namespace.
    """
    return argparse.Namespace()


@pytest.fixture
def repository(temporary_dir):
    """Provides valid repository."""
    repo_dir = temporary_dir / DEFAULT_CODETRAIL_DIRECTORY
    repo_dir.mkdir()
    return CodetrailRepository(temporary_dir)


@pytest.fixture
def caplog_info(caplog):
    """Provides caplog at level INFO"""
    with caplog.at_level(logging.INFO) as cap_info:
        yield cap_info


@pytest.fixture
def codetrail_logger():
    """Provides caplog at level ERROR"""
    with patch("codetrail.config.LOGGER") as logger:
        yield logger
