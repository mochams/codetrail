"""This module defines all command classes used by command handlers.

Commands are responsible for encapsulating data required to perform specific operations.
Each command inherits from the `BaseCommand` class, which serves as a base for
validation and serialization using Pydantic.
"""

from pathlib import Path

import pydantic


class BaseCommand(pydantic.BaseModel):
    """The base class for all commands.

    This class provides validation and serialization capabilities
    for any commands that inherit from it. It uses Pydantic's `BaseModel`
    to ensure that command data adheres to the defined schema.

    Attributes:
        None: This is a base class with no predefined attributes.
    """


class InitializeRepository(BaseCommand):
    """Command to initialize a repository at the specified path.

    Attributes:
        path (str): The file system path where the repository will be initialized.
    """

    path: str | Path
