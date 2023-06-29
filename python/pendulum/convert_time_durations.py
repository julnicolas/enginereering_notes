import pendulum

dur = pendulum.duration(days=1)

print(dur.in_days())
print(dur.in_hours())
print(dur.in_minutes())
print(dur.in_seconds())
print(dur.in_words())
