"""This module contains global fixtures for the tests."""

import argparse
import configparser
from pathlib import Path
from unittest.mock import patch

import pytest

from codetrail import cmd_init
from codetrail import commands
from codetrail import models


@pytest.fixture
def temporary_dir(tmp_path):
    """Provide a temporary directory.

    Returns:
        The temporary directory.
    """
    directory = tmp_path / "sub"
    directory.mkdir()
    return directory


@pytest.fixture
def temporary_file(temporary_dir):
    """Provide a temporary file.

    Returns:
        The temporary directory.
    """
    file = temporary_dir / "hello.txt"
    file.write_text("content", encoding="utf-8")
    return file


@pytest.fixture
def nonexistent_dir():
    """Provide a nonexistent directory.

    Returns:
        The nonexistent directory.
    """
    return Path("/nonexistent/path/")


@pytest.fixture
def nonexistent_file():
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
def default_path(temporary_dir):
    """Provides default path."""
    with patch.object(commands.BaseCommand, "default_path", temporary_dir):
        yield


@pytest.fixture
def code_repository(temporary_dir):
    """Provides valid repository."""
    cmd_init.initialize_repository(commands.InitializeRepository(path=temporary_dir))
    return models.CodetrailRepository(temporary_dir)


@pytest.fixture
def config_parser():
    """Provides config parser."""
    return configparser.ConfigParser()
