
# Using True
boolean_value = True
if boolean_value:
    print("This statement will be executed because True is considered as a 'truthy' value.")

# Using iter()
list_data = [1, 2, 3, 4, 5]
iterator = iter(list_data)
next_element = next(iterator)
print("The first element of the list is:", next_element)

# Iterating through a list using a for loop and an iterator
for number in iter(list_data):
    print("Current number is:", number)
