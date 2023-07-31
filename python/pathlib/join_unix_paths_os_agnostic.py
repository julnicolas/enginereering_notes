""" The pathlib modules and the PurePath classes are useful to manipulate paths
without any IO involved.

This modules shows how to join unix paths no matter on which OS python is
running on. """

from pathlib import PurePosixPath as Posix

# Default value is "."
path = Posix()

# Append/join paths
path = path / "foo" / "bar"

# join paths like os.path.join
path = path.joinpath("baz", "blah")

# Display path as string
print(path.as_posix())
