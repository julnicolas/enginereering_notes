""" Shows how to download a file following
the streaming method (chunk by chunk download). """
import urllib3
from time import sleep

# It supposedly decompress archives when streaming but in effect
# it doesn't work. Gzipping processes must be done elsewhere.
with urllib3.PoolManager(maxsize=10) as pool:
    resp = urllib3.request(
        "GET",
        "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-amd64.gz",
        preload_content=False, # enables chunk-by-chunk download
        timeout=timeout,
    )
    
    chunk_size = 128
    # other way to query
    # for chunk in resp.stream(chunk_size):
    
    # read blocks waiting for more content comming to the socket
    while chunk := resp.read(chunk_size):
        print(chunk)
        sleep(1)
    
    # mandatory when streaming content with urllib
    resp.release_conn()  # mandatory when streaming content

