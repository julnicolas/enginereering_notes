""" Execute a shell command from python. 

Runs a subcommand from a subshell process, with a timeout of 2 seconds and
capturing stdout and stderr."""
import subprocess
from os import exit

cmd = "ls -1"
r = subprocess.run(cmd, shell=True, timeout=2, capture_stdout=True)

if r.returncode != 0:
    print('error!')
    exit(1)

print("printing stdout:")

# stdout is a byte list, to convert in string - str(r.stdout)
print(r.stdout)
