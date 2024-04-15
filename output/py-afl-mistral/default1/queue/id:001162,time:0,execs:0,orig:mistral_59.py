
# Define an empty set using frozenset
my_set = frozenset()

# Demonstrate that frozenset is immutable by trying to add an element
try:
    my_set.add(42)
except TypeError as e:
    print("Error:", e)
    
print("my_set is a frozenset: ", isinstance(my_set, frozenset))
print("my_set is empty: ", len(my_set) == 0)

# Define a boolean value False
bool_value = False

# Compare the two using equality operator (==)
if my_set == frozenset() and bool_value is False:
    print("Both my_set and False have the same value as an empty set and False respectively.")
else:
    print("Oops! Something went wrong!")
