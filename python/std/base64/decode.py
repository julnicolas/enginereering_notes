""" Decode base64 payload. """
from base64 import b64decode as decode

t = """PyBJIGFtIHRoZSByaWRkbGVyLCBJIHdhbnQgdG8gcGxheSBhIGdhbWUuCgpSSURETEVfMT0iIiAjIFVzZSBtZSBpbnN0ZWFkIG9mIExSTywgSSBkbyBVRFAhLgpSSURETEVfMj0iIiAjIEhleCB2YWx1ZSBvZiBUQ1AgZmxhZyB3aGVuIHNlcnZlciBJU04gaXMgZ2l2ZW4uClJJRERMRV8zPSIiICMgV2hhdCB0byBjaGVjayB0byBhdm9pZCB0byBET1MgcHJvbWV0aGV1czogIkMqKioqSVRZIgpSSURETEVfND0iIiAjIEluIGZvdXIgbGV0dGVycywgSSBsaW5rIEVLUyB0byBJQU0KUklERExFXzU9IiIgIyBUaGUgYW5zd2VyIHRvIGV2ZXJ5dGhpbmcuCgpCT05VU18xID0gIiIgICMgMHgwRjAtMEZGIGluIHRocmVlIGxldHRlcnMuCkJPTlVTXzIgPSAiIiAjIHNlY3Rpb24gLnRleHQsIGRiIDB4ZWEgaW4gNCBsZXR0ZXJzLgoK"""

# Output is byte, use bytes' methode decode('utf-8')
# if a string object is wanted instead
print(decode(t))
