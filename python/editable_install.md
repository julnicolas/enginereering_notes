# Editable Install
An `editable install` installs a python package located at a provided path on a system
or virtual environment using simbolic links. It is also known as a `local install`.

Editable installs are used by developpers to install their package under development
locally so that they can test it (either manually or with testing frameworks).

*GOOD PRACTICE:* run the `editable install` in a `virtual environment`.

``` sh
cd package_in_development

# Create venv and enable
mkdir .venvs
python -m venv ./.venvs/myvenv
source ./venvs/myvenv/bin/activate

# edit install package in venv
pip install -e .
```

Note - pip uses a `setup.py` file or a `pyproject.toml` file for the
installation.

