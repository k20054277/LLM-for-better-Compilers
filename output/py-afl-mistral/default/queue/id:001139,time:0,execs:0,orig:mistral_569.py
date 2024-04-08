
# An empty list as an example, can be replaced with any other iterable like strings, tuples or sets
my_list = []

# Using len() to find the length of my_list
length_of_my_list = len(my_list)
print("Length of my_list: ", length_of_my_list)

# Using True to check if a condition is met, here checking if my_list is empty or not
if not my_list:
    print("my_list is empty")
else:
    # If the list is not empty, print out its first element
    print("First element of my_list: ", my_list[0])
