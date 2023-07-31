""" This method shows how to build an URL
component by component using urlunparse. """

import urllib.parse as u

# Useful to create the path part of the url
# in a portable manner
from pathlib import PurePosixPath as Posix

args = {"first name": "john", "surname": "doe"}

url = u.ParseResult(
    scheme="https",
    netloc="foo.com",
    path=Posix().joinpath("bar", "baz", "blah").as_posix(),
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
    query=u.urlencode(args, doseq=True, quote_via=u.quote),
    params="",
    fragment="",
)

print(u.urlunparse(url))
