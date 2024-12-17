"""This module defines all command classes used by command handlers.

Commands are responsible for encapsulating data required to perform specific operations.
Each command inherits from the `BaseCommand` class, which serves as a base for
validation and serialization using Pydantic.
"""

from functools import cached_property
from pathlib import Path

import pydantic

from codetrail.conf import DEFAULT_CURRENT_PATH


class BaseCommand(pydantic.BaseModel):
    """The base class for all commands.

    This class provides validation and serialization capabilities
    for any commands that inherit from it. It uses Pydantic's `BaseModel`
    to ensure that command data adheres to the defined schema.

    Attributes:
        None: This is a base class with no predefined attributes.
    """

    @cached_property
    def default_path(self) -> str:
        """Get the default repository path.

        Returns:
            The default path as '.'
        """
        return DEFAULT_CURRENT_PATH


class InitializeRepository(BaseCommand):
    """Command to initialize a repository at the specified path.

    Attributes:
        path (str): The file system path where the repository will be initialized.
    """

    path: str | Path


class SetConfig(BaseCommand):
    """Command to set a configuration with key and value.

    Attributes:
        key (str): The key that will hold the value.
        value (str): The value to set .
    """

    key: str
    value: str

    @cached_property
    def section(self) -> str:
        """Get configuration section from key.

        Returns:
            Section(str) from the key.

        Example:
            key "user.name", returns 'user'
        """
        return self.key.split(".")[0]

    @cached_property
    def option(self) -> str:
        """Get configuration option from key.

        Returns:
            Option(str) from the key.

        Example:
            key "user.name", returns 'name'
        """
        return self.key.split(".")[1]
