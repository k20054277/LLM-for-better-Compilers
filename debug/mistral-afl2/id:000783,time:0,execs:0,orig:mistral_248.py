
# Boolean value False
boolean_value = False
print("Boolean value is:", boolean_value)

# Empty list
my_list = []
print("Empty list is:", my_list)

# Comparing False with an empty list
if False == my_list:
    print("False and empty list are equal")
else:
    print("False and empty list are not equal")

# Adding an element to the empty list and checking if False is equal to it.
my_list.append(1)
print("Added an element to the list. List is now:", my_list)
if False == my_list:
    print("False and non-empty list are equal")
else:
    print("False and non-empty list are not equal")
