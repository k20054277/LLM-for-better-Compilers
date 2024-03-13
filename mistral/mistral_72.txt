
# An empty list as an example of a collection that has a length of 0
my_list = []

# Check if my_list is empty (has a length of 0) using len() and a boolean comparison with False
if len(my_list) == 0:
    print("The list is empty.")
else:
    # If the list has an element, print its first element
    print("The first element of the list is:", my_list[0])

# Use False directly in a boolean expression
if not my_list:
    print("The list is empty using boolean negation.")
else:
    print("The list has an element.")
