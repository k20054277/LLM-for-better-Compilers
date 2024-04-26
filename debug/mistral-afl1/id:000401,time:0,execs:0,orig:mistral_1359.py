
# Function to calculate the square root using Newtown-Raphson method
def sqrt(number):
    if number < 0:
        raise ValueError("Square root of negative number is not defined.")
    
    guess = number / 2.0
    while abs(guess*guess - number) > 0.01:
        guess = (guess + number/guess) / 2.0
        
    return guess

# Function to test the square root calculation
def test_sqrt():
    num = 25
    result = sqrt(num)
    
    # Assert statement to check if the square root is correct
    assert result * result == num, f"Square root of {num} is not correct. Expected: {num}, Got: {result}"

    print("Test passed! The square root of", num, "is:", result)

# Test the function
test_sqrt()

# Another test with negative number
try:
    test_sqrt()
except AssertionError as error:
    print("Test failed:", error.args[0])
