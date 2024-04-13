# When should I use it
For general purpose use `requests`.

Requests relies on `urllib3` but might change
in the future if more efficient exists.

## Streaming Download
This library can be used for very specific use-cases
such as file streaming. When trying to do it with `requests`
we end up interacting with urllib3 plus `requests` internals.
It ends up beeing simpler using `urllib3`.

## Http Proxy Tunneling

