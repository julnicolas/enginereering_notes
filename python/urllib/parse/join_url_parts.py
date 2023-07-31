""" Join different url parts consistently """

import urllib.parse as url

# Only two url parts can be joined (a third or fourth parameter is ignored
url.urljoin("https://google.com", "foo/bar")

