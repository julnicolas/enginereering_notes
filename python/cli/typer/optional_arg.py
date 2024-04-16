""" Shows how to exit from CLI. """

import typer
from typing import Annotated

app = typer.Typer()


@app.command()
def cmd1(arg1: str, arg2: Annotated[str, typer.Argument()] = ""):
    """Exit with code 0."""
    typer.Exit()


if __name__ == "__main__":
    app()
