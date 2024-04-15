
import itertools

def list1(n):
    """Return a list with n unique elements."""
    return list(range(1, n + 1))

def list2(m):
    """Return a list with m unique elements."""
    return list(range(m + 1, m - 5, 2))

# Create two lists with the given lengths
list_a = list1(5)
list_b = list2(3)

# Using assert to check if the lists have the same elements
assert set(list_a) == set(list_b), "The sets of elements in the lists are not equal."

print("Lists contain the same elements: True")

# Using itertools.intersection_disjoint() to check for common elements
if not itertools.intersection_disjoint(list_a, list_b):
    print("The lists have common elements.")
else:
    print("The lists do not have any common elements.")

# Now let's add a common element and see if it's detected
list_b.append(2)
print("\nAfter adding a common element to list_b, the output should be:")

if not itertools.intersection_disjoint(list_a, list_b):
    print("The lists have common elements.")
else:
    print("The lists do not have any common elements.")

assert 2 in list_a or 2 in list_b, "The common element is not present in either list."
print("Common element found using assert.")
