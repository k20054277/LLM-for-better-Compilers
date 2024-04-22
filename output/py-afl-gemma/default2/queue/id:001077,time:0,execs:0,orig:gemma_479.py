
# None and Data Structure Demonstration

# Define a function that returns None
def no_return():
    return None

# Define a list
my_list = [1, 2, 3, None]

# Print the list
print(my_list)

# Check if the list contains None
if None in my_list:
    print("None is in the list")

# Iterate over the list
for item in my_list:
    # Print each item
    print(item)

# Access the first item in the list
print(my_list[0])

# Remove None from the list
my_list.remove(None)

# Print the list after removing None
print(my_list)
