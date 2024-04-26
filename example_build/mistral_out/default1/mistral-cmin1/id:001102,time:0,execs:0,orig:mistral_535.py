
# A list of boolean values
boolean_list = [False, True, False, True, False]

# Using any() to check if there is at least one True value in the list
if any(value for value in boolean_list if value):
    print("At least one element in the list is True")
else:
    print("All elements in the list are False")

# Directly using True to compare with an iterable (in this case, a list)
if True in boolean_list:
    print("True is present in the list")
else:
    print("True is not present in the list")
