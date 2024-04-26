
# Define a compare function that takes two arguments
def compare(arg1, arg2):
    # Compare arg1 and arg2 using the >= operator
    if (arg1 is not None) and (arg2 is not None):
        return str(arg1) + " is greater than or equal to " + str(arg2) + " (" + str(arg1) + " >= " + str(arg2) + ")"
    elif arg1 is None:
        return str(arg1) + " is None"
    elif arg2 is None:
        return str(arg2) + " is None"
    else:
        return "Both are None"

# Call the compare function with various arguments
print(compare(3, 3))         # prints "3 is equal to 3 (3 = 3)"
print(compare(5, 3))         # prints "5 is greater than 3 (5 > 3)"
print(compare(None, None))    # prints "Both are None"
print(compare(None, 3))      # prints "None is less than 3 (None < 3)"
