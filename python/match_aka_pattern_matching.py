""" These examples illustrate simple pattern matching cases using python's
match syntax. """

lst = [
    ("Sonic", {"speed": 100, "strength": 45}),
    ("Knuckles", {"speed": 75, "strength": 90}),
]

for e in lst:
    # Only one case per element can match, the first one takes priority
    match e:
        case ("Sonic", _):
            print("This is Sonic!")
        case (_, {"strength": 90}):
            print("This is a strong character!")
        case _:
            print("this matches every character, let's print it out!")
            print(e)
