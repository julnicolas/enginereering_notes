""" This module shows how to parse an url """

import urllib.parse as u

url = "https://foo.com/bar/baz/blah?first%20name=john&surname=doe"

url = u.urlparse(u.unquote(url))
print("parsed url", url)
print("query params parsed as a dict", u.parse_qs(url.query))
