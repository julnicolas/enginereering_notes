""" Compute a sha256 hash from bytes. """
import hashlib

h = hashlib.sha256()
h.update(b"hello")
h.update(b"world")

# hexdigest -> str
print(h.hexdigest())
