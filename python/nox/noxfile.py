"""
Show how to create sessions which install python packages, then run them.

Really useful for tooling.

To run nox:
``` sh
pip install nox
nox
```

Nox automatically runs a noxfile.py in the current dir.
"""
import nox


@nox.session
def black(session):
    """
    Runs the black formatter inside its own venv.
    A new venv is created on every call.
    """
    # Install a python module in the venv
    session.install("black")

    # Run a python script
    session.run("black", ".")


@nox.session(reuse_venv=True)
def mypy(session):
    """Runs mypy in its own venv but reuse it if it already exist"""
    session.install("mypy")

    # Funny enough, nox must install nox so that mypy can read the imports
    session.install("nox")
    session.run("mypy", "--install-types", "--non-interactive", ".")
