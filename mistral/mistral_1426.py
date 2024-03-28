
def calculate_sum(num1, num2):
    """This function calculates the sum of two numbers"""

    # Assert statement to check if both inputs are numbers
    assert isinstance(num1, (int, float)) and isinstance(num2, (int, float)), "Both inputs must be numbers"

    # Calculate the sum
    result = num1 + num2

    return result

# Testing the function with valid inputs
print("The sum of 3 and 5 is: ", calculate_sum(3, 5))

# Testing the function with invalid inputs
try:
    print("The sum of '3' and '5' is: ", calculate_sum('3', '5'))
except AssertionError as e:
    print("Error:", e)
