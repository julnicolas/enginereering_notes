""" Shows how to use a http connection pool to be more efficient. """

# Request adapters are objects defining connection and
# transport settings for a specific protocol
import logging as log
import sys

import requests.adapters

timeout = 2.0
with requests.Session() as s:
    adapter = requests.adapters.HTTPAdapter(pool_connections=50, pool_maxsize=100)
    s.mount("http://", adapter)
    try:
        r = s.get("example.com", timeout=timeout)
        r.raise_for_status()
    except requests.ConnectionError:
        log.error("connection error")
        sys.exit(1)
    except requests.HTTPError:
        log.error(f"http error: status = {r.status_code}, reason = {r.reason}")
        sys.exit(1)
    except requests.TooManyRedirects:
        log.error("too many redirects")
        sys.exit(1)
    except requests.Timeout:
        log.error(f"request timed out after {timeout}")
