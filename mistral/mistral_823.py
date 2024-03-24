
# A list of boolean values
boolean_values = [True, False, True, False, True]

# Using 'and' to check multiple conditions
if condition1 and condition2:
    print("Both condition1 and condition2 are True")

# Applying 'and' for all elements in a list
if all(value is True for value in boolean_values):
    print("All boolean values in the list are True")
else:
    print("There is at least one False value in the list")
