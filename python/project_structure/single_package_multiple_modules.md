# Single Package Multiple Modules
Here is a simple layout to follow when distributing a single package:
```
helloworld/
│
├── helloworld/
│   ├── __init__.py
│   ├── helloworld.py
│   └── helpers.py
│
├── tests/
│   ├── helloworld_tests.py
│   └── helpers_tests.py
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

`setup.py` can be replaced by a `pyproject.toml`.

