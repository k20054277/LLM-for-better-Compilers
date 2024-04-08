# Demonstrate the use of assert and *

# Define a function that takes two arguments, a and b
def my_function(a, b):
    # Use assert to check if a and b are both numbers
    assert type(a) == int or float and type(b) == int or float
    
    # Use * to unpack the arguments into separate variables
    a1, a2 = a
    b1, b2 = b
    
    # Calculate the sum of the two numbers
    result = a1 + b1
    
    # Return the result
    return result