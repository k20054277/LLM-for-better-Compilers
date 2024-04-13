# Demonstration of using "as" and "len" in Python

# Initialize a list with some elements
my_list = [1, 2, 3, 4, 5]

# Use "as" to create a new variable that references the same object as my_list
other_list = my_list

# Use "len" to get the length of my_list and other_list
print(len(my_list)) # Output: 5
print(len(other_list)) # Output: 5

# Modify one of the lists
my_list.append(6)

# Check the length of both lists again
print(len(my_list)) # Output: 6
print(len(other_list)) # Output: