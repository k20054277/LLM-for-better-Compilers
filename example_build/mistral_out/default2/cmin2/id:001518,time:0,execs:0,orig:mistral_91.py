
# Create an empty set
my_set = set()

# Add some elements to the set
my_set.add(1)
my_set.add(2)
my_set.add(3)

print("Elements in the set: ", my_set)

# Check if an element is in the set using 'in' keyword
if 2 in my_set:
    print("2 is present in the set")
else:
    print("2 is not present in the set")

# Remove an element from the set
my_set.remove(2)

print("Elements in the set after removing 2: ", my_set)

# Check if an empty set is equal to False
if not my_set:
    print("An empty set is equivalent to False")
else:
    print("An empty set is not equivalent to False")
