"""This module holds the parser for command line options."""

import argparse

argparser = argparse.ArgumentParser(
    prog="Codetrail",
    description="Version Control inspired by Git.",
    epilog="Text at the bottom of help",
)

argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True

# INIT COMMAND
init = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
init.add_argument(
    "path",
    metavar="directory",
    nargs="?",
    default=".",
    help="Where to create the repository.",
)
