"""This module holds the parser for command line options."""

import argparse

arg_parser = argparse.ArgumentParser(
    prog="Codetrail",
    description="Version Control inspired by Git.",
    epilog="Text at the bottom of help",
)

arg_subparsers = arg_parser.add_subparsers(title="Commands", dest="command")
arg_subparsers.required = True

# INIT COMMAND
init = arg_subparsers.add_parser("init", help="Initialize a new, empty repository.")
init.add_argument(
    "path",
    metavar="directory",
    nargs="?",
    default=".",
    help="Where to create the repository.",
)

# CONFIG COMMAND
config = arg_subparsers.add_parser(
    "config",
    help="Manage repository configuration settings.",
)

config_subparsers = config.add_subparsers(title="Commands", dest="command")
config_subparsers.required = True

set_ = config_subparsers.add_parser("set", help="Set a config value")
set_.add_argument(
    "key",
    metavar="key",
    help="The name of the key that will hold the configuration value.",
    type=str,
    nargs=1,
)
set_.add_argument(
    "value",
    metavar="value",
    help="The value of the configuration setting.",
    type=str,
    nargs=1,
)
