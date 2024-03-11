""" Shows how to print a duration in plain English. """
from pendulum import now
from time import sleep


def chrono():
    start = now()
    while True:
        print((now() - start).in_words())
        sleep(1)


chrono()
