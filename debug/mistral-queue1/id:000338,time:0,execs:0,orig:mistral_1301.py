
# Function to check if a number is positive
def is_positive(num):
    """
    This function checks if a given number is positive.
    """
    assert num != 0, "Error: Number should be positive. Got {}".format(num)
    return num > 0

# Function to check if two numbers are equal
def are_equal(num1, num2):
    """
    This function checks if two given numbers are equal.
    """
    return num1 == num2

# Testing the functions
num1 = 5
num2 = 3

if __name__ == "__main__":

    print("Testing is_positive function:")
    print("Number 1:", is_positive(num1)) # Should print: True
    print("Number 2:", is_positive(num2)) # Raises an AssertionError with the message: Error: Number should be positive. Got -3

    print("\nTesting are_equal function:")
    print("Numbers are equal?:", are_equal(num1, num1)) # Should print: True
    print("Numbers are equal?:", are_equal(num1, num2)) # Should print: False

    print("\nChecking if numbers are not equal:")
    print("Numbers are not equal?:", not are_equal(num1, num2)) # Should print: True
