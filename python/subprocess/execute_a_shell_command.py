""" Execute a shell command from python. 

Runs a subcommand from a subshell process, with a timeout of 2 seconds and
capturing stdout and stderr."""

import subprocess
from sys import exit

cmd = "ls -1"
r = subprocess.run(
    cmd,
    cwd=".",  # Current working directory
    shell=True,  # Runs cmd in shell process
    timeout=2,  # Raises a timeout exception
    text=True,  # Return responses as str instead of bytes
    capture_output=True,
)  # Captures stdout and err

if r.returncode != 0:
    print("error!")
    exit(1)

print("printing stdout:")

# stdout is a byte list, to convert in string - str(r.stdout)
print(r.stdout)
