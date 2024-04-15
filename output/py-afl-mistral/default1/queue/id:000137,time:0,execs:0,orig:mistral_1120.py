
# Definition of a tuple
source = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Creating a set from a list or tuple using set() constructor
new_set = set(source)

print("Original tuple: ", source)
print("Set created from tuple: ", new_set)

# Using as keyword for assignment
variable = "example string"
another_variable as new_name

print("Variable before assigment: ", variable)
print("Another variable name: ", another_name) # It will raise a NameError if 'another_variable' is not defined

# Assigning the value of variable to another_variable using as keyword
as another_name as variable:
    another_variable = "new example string"

print("Variable after assigment: ", variable)
print("Another variable name: ", another_name)

# Add an element to set
new_set.add(10)
print("Set with added element: ", new_set)

# Difference between list and set
list1 = [1, 2, 3, 4, 5]
set1 = {1, 2, 3, 4, 5}

print("List1: ", list1)
print("Set1: ", set1)

# Find the difference between List and Set using '-' operator
difference_list_and_set = list1 - set1
print("Difference between List and Set: ", difference_list_and_set)
