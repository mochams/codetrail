"""This module holds all exceptions used in the application."""


class NotARepositoryError(Exception):
    """Exception raised when a folder is missing a repository directory."""


class ExistingRepositoryError(Exception):
    """Exception raised when folder parents has a repository directory."""


class InvalidCommandError(Exception):
    """Exception raised when a wrong/incorrect command is issued."""


class MissingConfigurationFileError(Exception):
    """Exception raised when a configuration file is missing."""


class UnsupportedConfigError(Exception):
    """Exception raise when configuration an invalid section or option."""
