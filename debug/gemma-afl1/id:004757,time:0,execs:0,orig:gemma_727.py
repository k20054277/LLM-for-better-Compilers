
# True and Data Structure Demonstration

# Defining a list
my_list = [1, 2, 3, 4, 5]

# Checking if the list is empty
if not my_list:
    print("The list is empty")

# Checking if the list contains a certain element
if 3 in my_list:
    print("The list contains the element 3")

# Iterating over the list
for element in my_list:
    print(element)

# Converting the list into a string
my_list_str = str(my_list)

# Printing the string representation of the list
print("The string representation of the list is:", my_list_str)

# Checking if the list is sorted in ascending order
my_list.sort()

# Printing the sorted list
print("The sorted list is:")
for element in my_list:
    print(element)

# True and False Examples
is_active = True
is_passive = False

# Checking the truth value of the variables
print("is_active is:", is_active)
print("is_passive is:", is_passive)

# Using True and False in an if statement
if is_active:
    print("The system is active")
else:
    print("The system is passive")
