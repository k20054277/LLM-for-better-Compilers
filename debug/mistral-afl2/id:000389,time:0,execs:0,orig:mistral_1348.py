
def add_numbers(num1, num2):
    """
    Adds two numbers and checks if the result is as expected using assert.
    """

    # Perform addition operation
    result = num1 + num2

    # Print local variables using locals() function
    print("Local variables inside add_numbers():")
    for key, value in locals().items():
        print(f"{key}={value}")

    # Assertion to check if the addition result is as expected
    assert result == 3, "Unexpected result from adding numbers."

# Testing the add_numbers() function with different inputs
add_numbers(1, 2)
add_numbers(5, 2)
