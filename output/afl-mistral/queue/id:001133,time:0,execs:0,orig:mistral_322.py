
# Define an empty list
my_list = []

# Assigning None to a variable
none_value = None

# Appending elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Printing the list and checking if it's empty
print("My list is empty? ", my_list or False)
print("My list: ", my_list)

# Assigning None to a list element
my_list[2] = None

# Checking if an element in a list is equal to None
if my_list[2] is None:
    print("The third element of the list is None.")
else:
    print("The third element of the list is not None.")

# Checking if the entire list is None or empty
if not my_list:
    print("My list is empty or all elements are None.")
else:
    print("My list contains some values.")
