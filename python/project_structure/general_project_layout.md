# General Project Layout

- `/scripts` or `/bin` for that kind of command-line interface stuff
- `/tests` for your tests
- `/lib` for your C-language libraries
- `/doc` for most documentation
- `/apidoc` for the Epydoc-generated API docs.
- `/data` data used by the application
- then either a `src` dir with several packages or the packages directly
  that's the preferred option since python doesn't impose a src dir
- any files such as `.gitignore`, `pyproject.toml`

