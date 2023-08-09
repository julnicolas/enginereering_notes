"""" HTTP GET Requests With Query Params.

requests.get is equivalent to requests.request(method="GET").
"""
import logging as log
import sys

import requests

url = "https://example.com"
url = "https://blah.com"
params = {
    "param_1": "value_1",
    "param_2": "value_2",
}
timeout = 2  # In seconds

# Timeout is in seconds
try:
    response = requests.get(url, params=params, timeout=timeout)
    # Raises a HTTPError if r.status_code >= 400
    response.raise_for_status()
except requests.ConnectionError:
    log.error("couldn't connect to server")
    sys.exit(1)
except requests.HTTPError:
    log.error(f"status code == {response.status_code}")
    sys.exit(1)
except requests.TooManyRedirects:
    log.error("too many redirects to reach remote host")
    sys.exit(1)
except requests.Timeout:
    log.error("request timed out after {timeout} seconds")
    sys.exit(1)

# If the content-type is unknown, check it using http headers!
print(f"content-type == {response.headers['Content-Type']}")

## Get content as bytes
# print(response.content)

## Show response as a raw str
print(response.text)

## Show response with JSON body
# raise a JSONDecodeError if the content is
# not in json
# print(response.json())
