# Demonstration of using True and tuples in Python

# Creating a tuple with True as one of its elements
my_tuple = (1, 2, 3, True)

# Using the len() function to get the length of the tuple
print("Length of my_tuple:", len(my_tuple)) # Output: Length of my_tuple: 4

# Using the in operator to check if True is an element of the tuple
if True in my_tuple:
    print("True is an element of my_tuple")
else:
    print("True is not an element of my_tuple") # Output: True is an element of my_tuple