"""This module holds all exceptions used in the application."""


class NotARepositoryError(Exception):
    """Exception raised when a folder is missing a repository directory."""


class ExistingRepositoryError(Exception):
    """Exception raised when folder parents has a repository directory."""


class InvalidCommandError(Exception):
    """Exception raised when a wrong/incorrect command is issued."""
