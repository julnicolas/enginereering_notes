""" Shows how to parse a Unix timestamp. """
from pendulum import from_timestamp

start = from_timestamp(1549573860)
end = from_timestamp(1549574340)
print((end - start).in_words())
