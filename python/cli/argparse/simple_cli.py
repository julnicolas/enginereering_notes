""" Shows how to implement a very simple CLI.

Argparse CLIs tend to become verbose, use typer if
more flexibility is required.

Also, it has many if such is defined then call this...
Which makes it needlessly hard to use.

Argparse is part of the python std lib.
"""
import argparse

# Instantiate the argument parser
parser = argparse.ArgumentParser(
            prog="my_program",
            description="what my program does",
            epilog="text at the bottom of help")

# Positional argument
# By default they are required
parser.add_argument('pos_arg1', help="some help")

# To make a positional argument not required a hack is needed
# nargs stands for the number of times an argument can be used,
# when providing '?' it is 0 or 1 times.
parser.add_argument('pos_arg2', default="heyhey", nargs="?", help="some help for 2")

# Flag with value
# By default they are not required
parser.add_argument("-l", "--list", help="some help message")
parser.add_argument("-p", "--p-option", required=True, help="some help message")
parser.add_argument("-b", help="some help message")

# Finally, parse - get CLI corresponding values
args = parser.parse_args()

# Showing provided args
# The long name is used to access options
# If provided
print(f"""positional arg 1: {args.pos_arg1}
positional arg 2: {args.pos_arg2}
list: {args.list}
p: {args.p_option}
b: {args.b}
""")

