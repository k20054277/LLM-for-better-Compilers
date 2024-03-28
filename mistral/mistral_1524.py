
def calculate(number):
    # Assertion: number must be greater than zero
    assert number > 0, "Error: Number must be positive"
    
    # Calculate the square and cube of the given number
    square = number * number
    cube = number * number * number

    print(f"The square of {number} is {square}")
    print(f"The cube of {number} is {cube}")

# Test the calculate function with positive and non-positive numbers
calculate(3)  # Output: The square of 3 is 9
             #        The cube of 3 is 27

try:
    calculate(-2)  # Output: Error: Number must be positive
except AssertionError as error:
    print(error)
