""" Run formatting, linting in a repeatable way.
It must be run using:

poetry run python -m nox

"""

import nox


def should_auto_fix(session: nox.session) -> bool:
    """Checks if the session should auto fix
    problems. This is fine for development, must
    be an error for a CI pipeline.

    This mode is enabled if the auto_fix argument is passed to nox:
    nox -- fix
    """
    return "fix" in session.posargs


@nox.session(venv_backend="none")
def black(session):
    """Runs black formatter on all source files."""
    if should_auto_fix(session):
        session.run("black", ".")
    else:
        session.run("black", "--diff", "--check", ".")


@nox.session(venv_backend="none")
def ruff(session):
    """Does code linting and fixes to be more PEP compliant"""
    if should_auto_fix(session):
        session.run("ruff", "check", "--fix", ".")
    else:
        session.run("ruff", "check", ".")


# Reuse mypy venv if already created, saves time
@nox.session(venv_backend="none")
def mypy(session):
    """Runs mypy on all source files."""
    # Install type stubs and run
    session.run("mypy", "--install-types", "--non-interactive", "epdl")


@nox.session(venv_backend="none")
def pytest(session):
    """Runs pytest on all source files"""
    session.run("python", "-m", "pytest")

