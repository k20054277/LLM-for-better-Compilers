
# A list of some boolean values
boolean_values = [True, False, True, False, True]

# Using 'and' operator
print("Using 'and' operator")
if True and False:
    print("This block will not be executed as both conditions are not true.")
else:
    print("Both conditions were checked, but the result is false.")

# Checking all elements in a list are True using 'any' operator
print("\nUsing 'any' operator")
if any(condition for condition in boolean_values if not condition):
    print("At least one condition was False.")
else:
    print("All conditions were true.")

# Checking all elements in a list are True using 'and' operator
print("\nUsing 'and' operator (for checking all elements)")
if all(condition for condition in boolean_values):
    print("All conditions were true.")
else:
    print("At least one condition was False.")
