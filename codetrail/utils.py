"""This module holds shared functions used by commands."""

from pathlib import Path

from codetrail.config import DEFAULT_CODETRAIL_DIRECTORY


def path_is_directory(path: Path) -> bool:
    """Check if a given path is a directory.

    Args:
        path: The file system path to check.

    Returns:
        True if the path is a directory, False otherwise.
    """
    return Path.is_dir(path)


def path_exists(path: Path) -> bool:
    """Check if a given path exists.

    Args:
        path: The file system path to check.

    Returns:
        True if the path exists, False otherwise.
    """
    return Path(path).exists()


def make_file(path: Path) -> None:
    """Create a new file at the specified path.

    Args:
        path: The file system path where the file should be created.
    """
    Path.touch(path, exist_ok=True)


def make_directory(path: Path) -> None:
    """Create a new directory at the specified path.

    Args:
        path: The file system path where the directory should be created.
    """
    Path.mkdir(path, parents=True, exist_ok=True)


def find_repository_path(path: str | Path) -> Path | None:
    """Find the root of the Codetrail repository.

    Starts at the given directory and moves upwards until it finds the repository
    root (a directory containing the `.codetrail` folder).
    Stops at the user's home directory.

    Args:
        path: The directory to start searching from.

    Returns:
        The Path object representing the repository root.
    """
    start = Path(path).resolve()
    home = Path.home()
    for current in [start, *start.parents]:
        if path_is_directory(current / DEFAULT_CODETRAIL_DIRECTORY):
            return current
        if current == home:
            break
    return None


def find_child_repository_path(path: str | Path) -> Path | None:
    """Find out if any child directory contains a Codetrail repository.

    Args:
        path: The root directory to start checking from.

    Returns:
        The Path object representing the repository root. None otherwise.
    """
    start = Path(path).resolve()
    for child in start.rglob(DEFAULT_CODETRAIL_DIRECTORY):
        return child.parent if path_is_directory(child) else None
    return None


def write_to_file(file_path: Path, content: str) -> None:
    """Write content to a file, creating or overwriting it.

    Args:
        file_path: The path to the file where content will be written.
        content: The string content to write to the file.
    """
    with Path.open(file_path, "w", encoding="utf-8") as file:
        file.write(f"{content}\n")
