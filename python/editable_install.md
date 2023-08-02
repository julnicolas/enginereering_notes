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

## A note on extra dependencies in setup.py
Let's consider the following exerpt from a `setup.py` file:
``` python
setup(
    ...
    extras_require={
        'extra_feature': ['dependency3', 'dependency4']
    }
    ...
)
```

To local/edit install `extra_feature` on top of the rest of dependencies, the syntax is:
``` sh
pip install -e .[extra_feature]
```

