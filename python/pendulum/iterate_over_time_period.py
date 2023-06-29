import pendulum

now = pendulum.now()

# A periode is a difference between two date times
upcoming_week = now.add(days=6) - now

# Set period of time to be iterable per days
# Default iteration may be a second?
upcoming_week.in_days()

# Iterate over days in period of time
# from starting moment in period (now)
# until the end of the interval (today + 6)
for day in upcoming_week:
    print(day)
