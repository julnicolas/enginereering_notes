# Why use contexts
At google, every function on the path of an ingoing or
outgoing request must take a context struct as first
parameter.

This has several perks:
- functions starting with a context param may be on
    a path
- developed software can interoperate easily across
teams in the whole company
- it becomes easy to pass along request-context-dependent
objects such as loggers, tracers, credentials and timeout
options amongst others.
- it acts as a dependency injection, loosening coupling
even though contexts loose type informations.

Amongst the cons:
- type information is lost withing context structs
- it adds a parameter to a lot of functions

