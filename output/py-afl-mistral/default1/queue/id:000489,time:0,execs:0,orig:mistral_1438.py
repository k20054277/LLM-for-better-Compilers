
# A simple function to calculate the square root of a number
def sqrt(number):
    # Assertion check to ensure that the input is a positive number
    assert number >= 0, "Error: The input number should be non-negative"
    
    # Calculate the square root using the built-in math library function
    result = number ** 0.5
    
    return result

# Function to test the sqrt function
def test_sqrt():
    # Testing with valid inputs
    print("Square root of 16 is:", sqrt(16))
    print("Square root of 25 is:", sqrt(25))

    # Testing with an invalid input
    try:
        print("Square root of -1 is:", sqrt(-1))
    except AssertionError as error:
        print(error)

# Call the test function
test_sqrt()
