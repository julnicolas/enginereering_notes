""" Dead simple CLI definition
Install:
pip install typer
pip install rich # not mandatory, just to have a good looking CLI
pip install shellingham # optional, auto shell detection for auto completion
                        # install

pip install typer[all] # installs typer and all optional deps
"""

import typer

app = typer.Typer()


@app.command()
def greeting(name: str, first_name: str, formal: bool = True):
    """ 2 first arguments are mandatory CLI args. formal is an option."""
    if formal:
        print(f"Good morning Mr {name}")
    else:
        print(f"Hey {first_name}")


@app.command()
def valediction(name: str, language: str = "en"):
    """language is an optional option.
    It happens when giving a default value.
    """
    if language.lower() == "fr":
        print(f"Au revoir M. {name}")
    else:
        print(f"Farewell Mr {name}")


@app.command()
def kubectl(namespace: str = typer.Option(...)):
    """ The option is mandatory """
    print(f"namespace == {namespace}")

if __name__ == "__main__":
    app()
