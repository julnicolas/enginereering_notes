""" Shows how to document a CLI app. """

from typing import Annotated
import typer

app = typer.Typer()


@app.command()
def cmd(
    foo: int,
    bar: Annotated[int, typer.Argument(help="bar is an int")] = 2,
    baz: str = "hello",
    babe: Annotated[
        str, typer.Option(help="do you know what comes after baz?")
    ] = "hello",
):
    """Documenation Headline
    Some more information about the CLI"""
    typer.Exit()


if __name__ == "__main__":
    app()
