
# This function returns False if x is even, otherwise it returns True
def is_odd(x):
    return x % 2 != 0

# Main part of the program
if is_odd(5):  # This condition will be True, so the following block will be executed
    print("Five is an odd number")
else:
    print("Five is an even number")
    
# Using False directly in a conditional statement
if not is_odd(10):  # This condition will be True, so the following block will be executed
    print("Ten is an even number")
else:
    print("Ten is an odd number")

# Using boolean operator (), which returns the opposite of a given boolean value
if not (is_odd(10)):  # This condition will be True, so the following block will be executed
    print("Ten is an even number")
else:
    print("Ten is an odd number")

# Using False and () in combination
if not (is_odd(0) or is_odd(1)):
    print("Neither zero nor one is an odd number")
