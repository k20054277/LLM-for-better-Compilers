
# Function to calculate the square of a number or return None if no argument is given
def square(number=None):
    if number is None:
        return None
    else:
        result = number * number
        return result

# Using semicolon to place multiple statements on the same line (not recommended for readability)
x = 5; y = 10
print(f"Value of x: {x}")
print(f"Value of y: {y}")

# Function call examples
print("Square of 4: ", square(4)) # Should print "Square of 4: 16"
print("Square of None: ", square()) # Should print "Square of None: None"
