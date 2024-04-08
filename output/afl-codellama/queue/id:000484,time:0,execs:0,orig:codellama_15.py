import sys

# Create a list of integers
my_list = [1, 2, 3, 4, 5]

# Print the first element of the list
print(my_list[0])

# Check if the list is empty
if my_list:
    print("The list is not empty")
else:
    print("The list is empty")

# Add an element to the end of the list
my_list.append(6)

# Print the length of the list
print(len(my_list))

# Remove the first element from the list
del my_list[0]

# Print the new length of the list
print(len(my_list))