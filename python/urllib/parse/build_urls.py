""" Shows how to build a URL """
import urllib.parse as u

# Useful to create the path part of the url
# in a portable manner
from pathlib import PurePosixPath as Posix

# scheme + fqdn
base = "https://foo.com"

# Append path to url
url_path = Posix().joinpath("foo", "bar", "baz").as_posix()
url = u.urljoin(base, url_path)

# Make query params
args = {"first name": "bob", "surname": "dylan"}

# Uses %20 for spaces instead of +
# Some legacy backend may reject this but this should
# the best practice now
# + for spaces used to be recommended by the html standard
# prior to 2.0
#
# doseq is used to translate sequences (such as lists) in a listing
# of n times the same argument
# Ex: "range": [1, 2, 3] would be encoded as
# range=1&range=2&range=3
query = u.urlencode(args, doseq=True, quote_via=u.quote)

url = u.urljoin(url, f"?{query}")

print(url)
