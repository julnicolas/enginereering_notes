""" Examples on how to sort a list """

# list.sort modifies the list in place, it returns None!
# builtin.sorted creates a new sorted list

print("-- Ascending Order")
l = [3, 1, 4, 2]

l.sort()
print(l)
print(sorted([3, 1, 4, 2]))

print("\n-- Descending Order")
l.sort(reverse=True)

print(l)
print(sorted([3, 1, 4, 2], reverse=True))

print("\n-- Custom key function")
l = [("Sonic", 100), ("Tails", 60), ("Knuckles", 50)]

print("sort by speed component of the tupple")
l.sort(key=lambda e: e[1])

print(l)
print(sorted([("Sonic", 100), ("Tails", 60), ("Knuckles", 50)], key=lambda e: e[1]))
