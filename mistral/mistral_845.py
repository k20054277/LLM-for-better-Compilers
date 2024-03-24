
# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Perform set operations using 'and' keyword
# The '&' operator is equivalent to using 'and' for sets in Python
result1 = set1 & set2
print("Set intersection using 'and': ", result1)

# Create a frozenset from one of the sets
frozen_set = frozenset(set1)

# Compare the original set and the frozen set using 'and' keyword
result2 = frozen_set & set2
print("Set intersection using 'and' on frozen set: ", result2)

# Check if two sets are identical (using '==') and print result
if set1 == set2:
    print("Both sets are identical.")
else:
    print("Both sets are different.")
