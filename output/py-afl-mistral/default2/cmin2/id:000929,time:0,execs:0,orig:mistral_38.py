
# A list of boolean values
boolean_values = [False, True, False, True, False]

# Using False in a boolean expression
if False:
    print("This block will not be executed")
else:
    print("This block will be executed")

# Using any() function
def is_any_true(boolean_list):
    """
    This function uses the any() function to check if there's at least one True value in the given boolean list.
    """
    return any(bool(x) for x in boolean_list)

print("Any value in the list is true: ", is_any_true(boolean_values))
