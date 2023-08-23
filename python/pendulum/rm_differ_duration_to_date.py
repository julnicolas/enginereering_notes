"""Differ duration to date."""
import pendulum

# Let's remove a year and 3 months
print(pendulum.now().add(years=-1, months=-3))
