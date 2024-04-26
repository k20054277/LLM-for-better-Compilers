
# Demonstrate the use of and and frozenset

# Create a frozenset of numbers
frozenset1 = frozenset([1, 2, 3, 4, 5])

# Check if a number is in the frozenset
print(3 in frozenset1)  # Output: True

# Iterate over the frozenset
for num in frozenset1:
    print(num)  # Output: 1 2 3 4 5

# Compare two frozensets
frozenset2 = frozenset([3, 4, 5, 6, 7])

print(frozenset1 == frozenset2)  # Output: False

# Convert a frozenset to a list
print(list(frozenset1))  # Output: [1, 2, 3, 4, 5]

# Create a new frozenset with the elements of the first one and add a new element
frozenset1.add(6)

print(frozenset1)  # Output: frozenset({1, 2, 3, 4, 5, 6})
