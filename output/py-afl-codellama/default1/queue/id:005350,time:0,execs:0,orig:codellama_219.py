# Demonstrate the use of False and memoryview in Python

# Create a list of integers
my_list = [1, 2, 3, 4, 5]

# Use False as an argument for the memoryview function
memoryview(my_list)

# Print the type of the memoryview object
print(type(memoryview(my_list)))