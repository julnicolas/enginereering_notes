""" Decompresses a gzip file chunk by chunk
in a streaming fashion. """
import gzip

# fileobj takes a file-like object, that is
# implementing common file operations like open
# read, write...
#
# In this case as the file is beeing read, it must
# implement the io.Reader interface
# (read, readline, readlines)
#
# Note - urllib3's response object implements this
# interface. It is therefore compatible with this code.
with gzip.GzipFile(fileobj=resp) as archive:
    for chunk in archive:
        # Only use decode if archived content is text
        print(chunk.decode("utf-8"))

