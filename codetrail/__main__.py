"""This is the entrypoint to our cli application."""

import sys

from codetrail.cli import parsers
from codetrail.cli import utils
from codetrail.config import LOGGER


def main() -> None:
    """Entrypoint for the version control system."""
    LOGGER.info("Welcome to codetrail!")
    args = parsers.argparser.parse_args(sys.argv[1:])
    utils.match_commands(args.command, args)


if __name__ == "__main__":
    main()
