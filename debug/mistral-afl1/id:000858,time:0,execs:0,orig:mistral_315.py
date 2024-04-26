
# Assigning None to a variable
variable_1 = None
print("Variable 1 is:", variable_1)
print("Id of Variable 1 is:", id(variable_1))

# Creating an empty list and assigning it to a variable
my_list = []
print("Variable 2 is an empty list: ", my_list)
print("Id of Variable 2 is:", id(my_list))

# Assigning None to an empty list
my_list = None
print("Variable 2 is now assigned as None: ", my_list)
print("Id of Variable 2 is:", id(my_list))

# Creating a new empty list
my_list = []
print("Creating a new empty list")
print("Variable 2 is an empty list: ", my_list)
print("Id of Variable 2 is:", id(my_list))

# Comparing None and an empty list using 'is' keyword
print("\nComparing None and an empty list:")
print("Is None equal to an empty list?", None is my_list)
print("Id of None is:", id(None))
print("Id of Empty List is:", id(my_list))
