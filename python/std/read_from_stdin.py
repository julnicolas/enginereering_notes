""" Shows different methods to read from stdin"""
import sys


def out(s: str | list[str]):
    print(f"-> {s}")


# Prompt for input
out(input("type a str\n"))

# Read several lines with input
try:
    print("echo str, exit with ctrl+d (EOF) or typing exit")
    exit_str = "exit"
    line = ""
    while line.strip() != exit_str:
        # Remove trailing end-of-line char
        line = input()
        out(line)
except EOFError:
    print("received EOF, i.e. ctrl + D")

# Read all lines from stream until EOF
# keeps the end of line char
# readlines can take an int to restrict read lines
print("reading lines until EOF:")
lines = sys.stdin.readlines()
out(lines)

# readline can take an int to restrict read lines
# reads a single line until '\n' or EOF
print("using readline to read a single line:")
line = sys.stdin.readline()
out(line)
