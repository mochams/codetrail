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

# ~ Set
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
# ~ Get
get = config_subparsers.add_parser("get", help="Get a config value")
get.add_argument(
    "key",
    metavar="key",
    help="The name of the key that holds the configuration value.",
    type=str,
    nargs=1,
)
# ~ List
list_ = config_subparsers.add_parser("list", help="List all config values")
# ~ Unset
unset = config_subparsers.add_parser("unset", help="Unset a config value")
unset.add_argument(
    "key",
    metavar="key",
    help="The name of the key that holds the configuration value.",
    type=str,
    nargs=1,
)
# ~ Edit
edit = config_subparsers.add_parser("edit", help="Edit the config file.")
edit.add_argument(
    "key",
    metavar="key",
    help="The name of the key that will hold the configuration value.",
    type=str,
    nargs=1,
)
edit.add_argument(
    "value",
    metavar="value",
    help="The new value of the configuration setting.",
    type=str,
    nargs=1,
)
