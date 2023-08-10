# Boolean Trap
The boolean trap is the fact of using a `boolean` in a function signature
in order to execute two different behaviours depending on the boolean's
value.

It is an anti-pattern.

Example:
``` python
def move(distance: float, forward: bool) -> float:
    if forward:
        return distance
    else:
        return -distance
```

So they are three problems here.

## Problems
### The use of a boolean as positional argument is ambiguous
Let's try it to make it clear:
``` python
move(2.0, True)
```

In this case it is absolutely not clear what `True` means here.

It is possible to make it clearer by using keyword argument passing instead:
``` python
move(2.0, forward=True)
```

This is a bit clearer, so let's enforce it by using keyword-only argument passing in python:
``` python
def move(distance: float, *, forward: bool) -> float:
    # same code as before
```

But that raises another issue.

### Using a boolean can only describe two cases
What would the direction be if `forward=False`? It could be `backward` or any direction
in between. Any reader would interpret the call their own way with a high chance of being wrong.

### Adding other behaviours is hard
It would require adding more booleans causing to change all previous calls and then manage interaction
between boolean flags.

## Solutions
### Use one function per case
It is very explicit and restrain the number of implementations if the number of possibilites is low.

Example:
``` python
def md5(blob: []byte) -> []byte: ...
def sha256(blob: []byte) -> []byte: ...
# ...
```

### Use mutually exclusive booleans
Each boolean corresponds to an unique well identified behaviour to enforce clarity. On top of it
keyword-argument passing must be enforced.

However, booleans are opaque in term of concepts, it would be more interesting to have a type descibing
what kind of behaviour it is about! (see enums in the next section).

On top of that, the signature becomes very long if a lot of methods are possible and imposes to change
function signatures if a method must be added! This problem doesn't occur with a specific type (enums).

Example:
``` python
def hash(blob: []byte, *, md5: bool, sha256: bool) -> []byte: ...
```

### Best solution - use enums
Let's define the function first and enum type first:

``` python
from enum import Enum
# IntEnum or StrEnum are a good choice

class HashMethod(Enum):
    MD5 = "md5"
    SHA256 = "sha256"

# Access enum's value - HashMethod.MD5.value
def hash(blob: []byte, method: HashMethod) -> []byte: ...
```

``` cpp
enum class HashMethod {
    MD5,
    SHA256,
};

void hash(unsigned char* bytes, HashMethod m);
```

