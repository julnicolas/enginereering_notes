""" Change print separator. 

Watch out it changes the default separator
globaly. So it is not a good practice for 
anything else than very short programs.
"""

print("default is new line")
print(1, 2, sep="\n")

print("\nnow let us use a space char instead")
print(1, 2, sep=" ")

# Now default separator is space
print(3, 4)
