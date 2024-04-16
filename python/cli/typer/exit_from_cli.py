""" Shows how to exit from CLI. """

import typer

app = typer.Typer()


@app.command()
def cmd1():
    """Exit with code 0."""
    typer.Exit()


@app.command()
def cmd2():
    """Exit with error code 1."""
    raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
