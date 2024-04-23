
# A counter variable to be updated every time the function is called
counter = 0

def calculate_square(number):
    global counter
    # Increase the counter every time the function is called
    counter += 1
    
    # Use assert to check if the input number is non-negative
    assert number >= 0, "Input number must be non-negative"

    return number ** 2

# Function call examples
print(calculate_square(3))   # Output: 9
print(calculate_square(5))   # Output: 25
print(calculate_square(-1))  # Raises an AssertionError with the message: 'Input number must be non-negative'

# Printing the number of function calls made
print("The calculate_square function has been called", counter, "times.")
