
# Create two sets and make them immutable using frozenset
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
frozen_set1 = frozenset(set1) # convert set to frozenset using list or set syntax
frozen_set2 = frozenset(set2)

# Print original sets
print("Original Sets:")
print("Set1:", set1)
print("Set2:", set2)

# Perform union operation on two frozen sets (not directly possible, use a regular set instead)
regular_union = set1.union(set2)
frozen_union = frozenset(regular_union) # convert the result to a frozenset

# Use 'as' keyword to assign the name of the variable being unpacked
# from the frozenset to the result of the union operation
as_variable, _ = frozen_union

print("\nUnion of Set1 and Set2 as a Frozenset:")
print("Frozen Union:", as_variable)

# Perform intersection operation on two original sets
intersection = set1.intersection(set2)
regular_intersection = {x for x in set1 if x in set2}
frozen_intersection = frozenset(regular_intervention)

print("\nIntersection of Set1 and Set2 as a Frozenset:")
print("Frozen Intersection:", frozen_intersection)
