# SOLID
SOLID is a mnemonic to present a few principles to
improve object oriented designs. Reducing coupling.

- `S` - Single Responsibility principle
    a class should only have one purpose, making it smaller,
    reducing coupling, easier to combine.
- `O` - Open to extension closed to modification principle
    A class should be extended, subclassed or whatever rather than
    modifying its behaviour. That could confuse programmers and break
    existing code. Of course, bug fixes are not considered a modification
    per se as it is aiming to correct intended behaviour
- `L` - Liskov Substitution, replacing an object by its parent should not
    break the meaning of the program. If so, there is a logical issue as
    classes should not be linked by an inherency relation.
- `I` - Interface segregation principle, users should not have to implement
    interfaces that they do not need. Meaning, interface must be as concise
    as possible. Interface must be composed in case a complex behaviour is
    absolutely needed.
    Doing so reduces the amount of dead code to maintain, as well as reduces
    coupling.
- `D` - Dependency Inversion principle, rely on abstraction rather than on
    implementation. Relying on implementation introduces tight coupling.

