
# True and tuple demonstration

# True is a boolean value that evaluates to True or False
print(True)  # Output: True

# Tuple is an immutable sequence of items
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # Output: (1, 2, 3, 4)

# Accessing items in a tuple
print(my_tuple[1])  # Output: 2

# Iterating over a tuple
for item in my_tuple:
    print(item)  # Output: 1 2 3 4

# Converting a tuple to a list
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3, 4]

# Modifying a list
my_list[0] = 5
print(my_list)  # Output: [5, 2, 3, 4]

# Comparisons
print(True == False)  # Output: False
print(1 == 2)  # Output: False
print(my_tuple == (1, 2, 3, 4))  # Output: True
