
# False and frozenset demonstration

# False object
false_bool = False

# Printing False
print(false_bool)  # Output: False

# Frozenset object
frozenset_obj = frozenset([1, 2, 3])

# Printing frozenset
print(frozenset_obj)  # Output: frozenset({1, 2, 3})

# Checking membership in frozenset
print(2 in frozenset_obj)  # Output: True

# Modifying frozenset (not allowed)
# frozenset_obj.add(4)  # Error: frozenset is immutable

# Iteration over frozenset
for elem in frozenset_obj:
    print(elem)  # Output: 1 2 3

# Converting frozenset to list
print(list(frozenset_obj))  # Output: [1, 2, 3]
