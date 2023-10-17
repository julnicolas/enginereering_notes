""" These examples illustrate simple pattern matching cases using python's
match syntax. """

lst = [
    ("Sonic", {"speed": 100, "strength": 45}),
    ("Knuckles", {"speed": 75, "strength": 90}),
    ("Shadow", "Rouge", "Tails", "Amy"),
]

for e in lst:
    # Only one case per element can match, the first one takes priority
    match e:
        case ("Sonic", _):
            print("This is Sonic!")
        case (_, {"strength": 90}):
            print("This is a strong character!")
        case ("Sonic", "Knuckles", *others):
            # Pack and unpack tuple elements in 'others' var
            print("Found Sonic, Knuckles and others are:", *others)
        case ("Sonic" | "Shadow", "Rouge", *others) as v:
            # Pack and unpack tuple elements in 'others' var
            # Defining v is useful if a complex succession of functions is applied
            # to 'e'
            print("Happy bunch: ", v)
        case _:
            print("this matches every character, let's print it out!")
            print(e)
