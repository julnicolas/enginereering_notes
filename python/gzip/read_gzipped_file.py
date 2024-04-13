""" Shows how to read a file compressed with gzip. """
import gzip

with gzip.open("file.gz") as f:
    for chunk in f:
        # If the file contains text content
        # otherwise do not use encode
        print(chunk.decode("utf-8"))

