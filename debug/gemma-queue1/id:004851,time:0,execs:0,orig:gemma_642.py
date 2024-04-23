
# True and frozenset demonstration

# Define a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 5])

# Print the frozenset
print(my_frozenset)

# Check if an element is in the frozenset
if 3 in my_frozenset:
    print("3 is in the frozenset")

# Iterate over the frozenset
for element in my_frozenset:
    print(element)

# Check if the frozenset is true
print(bool(my_frozenset))

# Compare two frozensets
print(my_frozenset == frozenset([1, 2, 3, 4, 5]))
