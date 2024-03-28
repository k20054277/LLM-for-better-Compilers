
# Define a frozenset object
my_frozenset = frozenset([1, 2, 3])

# Comparing frozenset with True using equality operator (==)
if my_frozenset == True:
    print("Frozenset is equal to True")
else:
    print("Frozenset is not equal to True")

# Comparing frozenset with True using inequality operator (!= or !=)
if my_frozenset != True:
    print("Frozenset is not equal to True")
else:
    print("Frozenset is equal to True (this will never be true)")

# Comparing frozenset with True using less than operator (<)
if my_frozenset < True:
    print("Frozenset is less than True")
else:
    print("Frozenset is greater than or equal to True")

# Comparing frozenset with True using greater than operator (>)
if my_frozenset > True:
    print("Frozenset is greater than True")
else:
    print("Frozenset is less than or equal to True")

# Comparing frozenset with True using membership operator (in)
if True in my_frozenset:
    print("True is a member of the frozenset")
else:
    print("True is not a member of the frozenset")
