"""This is the entrypoint to our cli application."""

import sys

from codetrail import cli
from codetrail import parsers
from codetrail.conf import LOGGER


def main() -> None:
    """Entrypoint for the version control system."""
    LOGGER.info("Welcome to codetrail!")
    args = parsers.arg_parser.parse_args(sys.argv[1:])
    cli.run(args.command, args)


if __name__ == "__main__":
    main()
