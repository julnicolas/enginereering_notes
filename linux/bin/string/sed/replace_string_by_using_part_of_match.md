# Backckward Reference Replacement

Replaces part of a string by another using a regex with backward reference.
``` sh
sed 's/hello \(.*\)!/greetings \1!/g'
```
The example above replaces any 'hello Bobby!' by 'greetings Bobby!'. Where
'Bobby' can be any string.

Note - the regular regex syntax is 'hello (.*)!' and 'greetings $1!'.
