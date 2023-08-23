"""Let's create a standard datetime.datetime object from
a pendulum Datetime object."""
import pendulum
from datetime import datetime

n = pendulum.now()
d = datetime(
    year=n.year, month=n.month, day=n.day, hour=n.hour, minute=n.minute, second=n.second
)

print("pendulum", n)
print("datetime", d)
