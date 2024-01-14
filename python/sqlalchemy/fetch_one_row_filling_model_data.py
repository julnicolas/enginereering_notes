""" Shows how to query a single row using SQL alchemy
using the modern ORM driven API.
"""

import logging
from os import exit

from sqlalchemy import select
from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.orm import Session

statement = select(DownloadKey).where(DownloadKey.id == key)
try:
    # Necessarilly one tupple is created here because:
    # If no results or multiple, an exception is raised
    r: DownloadKey = session.execute(statement).one()[0]
except NoResultFound as e:
    logging.exception(e)
    exit(1)
except MultipleResultsFound as e:
    logging.exception(e)
    exit(1)

print(r.expires_on)
