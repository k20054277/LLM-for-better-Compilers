
assert 5 > 3
assert 3 == 3

# Create a frozenset
my_frozenset = frozenset([1, 2, 3])

# Check if an element is in the frozenset
assert 2 in my_frozenset

# Try to add an element to the frozenset
try:
    my_frozenset.add(4)
except ValueError:
    print("Addition to frozenset is not allowed")

# Print the elements of the frozenset
print(my_frozenset)
