""" Shows how to implement a context manager which
is able to manage exceptions raised within the context.
"""
from typing import Any


# Defines a fake pytest mimicking pytest's layout
class pytest:  # noqa: N801
    class raises:  # noqa: N801
        class NoExceptionError(Exception):
            def __init__(self):
                msg = "an exception was expected but none was raised"
                super().__init__(msg)

        class WrongExceptionError(Exception):
            def __init__(self, exception: Exception):
                msg = "an exception was expected but another was raised:"
                msg += f"\n{exception}"
                super().__init__(msg)

        def __init__(self, exc: Exception):
            self._e = exc

        def __enter__(self) -> None:
            """Context manager entrypoint. Empty function."""
            ...

        def __exit__(self, exc_type: Any, exc: Exception, tcbk: Any) -> bool:
            """Checks if provided exception has been raised.
            If not, either a NoExceptionError is raised or a
            WrongExceptionError.

            Returns True if no issues were found so that exceptions
            are not propagated.
            """
            if exc is None:
                raise pytest.raises.NoExceptionError()

            if not isinstance(exc, self._e):
                raise pytest.raises.WrongExceptionError(exc)

            return True
