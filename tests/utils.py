"""Shared assertions in the tests module."""

from pathlib import Path


def assert_file_has_content(path, content):
    """Assert specified file has specifiend content."""
    with Path.open(path, "r", encoding="utf-8") as file:
        file_content = file.read()
        assert file_content == content, f"Expected {file_content} != {content}"
