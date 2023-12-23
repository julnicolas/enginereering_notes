# Publish Type Hinting For Python Package
## Generate a py.typed file
First of all generate a `py.typed` file at the root of the *source*
directory.

For instance if your project is called `foo`, generate the file in `foo/foo`:
``` sh
cd foo/foo
touch py.typed
```

## Generate stubs
The simplest solution is to use mypy's `stubgen` tool.

If `foo` contains your source code:
``` sh
stubgen foo
```
`stubgen` generates type stub files in a directory called `out` by default.

## Prepare type stubs for packaging
They are two options:
- copy type stub files (`.pyi`) next to their implementation (`.py`).
This is the prefered solution as this way type hinting is titely coupled to
software version. That is, the risk of having version drift between code and
stubs is lowered.
- publish a `foo-stubs` package containing type stubs. Not advised as users have
to make sure package version and stub version are aligned. On top of that any package
release implies necessarily the release of a dedicated stub package. Coupling is there
reduced, increasing the risk to have version drift between the two.

Note
----
I coded utilities to automate copy, generation and various other checks in the
`fh_db` project. These tools will be moved to a dedicated repository later.

