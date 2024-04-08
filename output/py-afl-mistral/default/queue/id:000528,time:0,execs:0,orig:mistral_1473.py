
# Define a function to calculate the square root using the Babylonian method (scripting)
def babylonian_sqrt(number, precision=0.01, max_iterations=50):
    guess = number / 2.0
    for _ in range(max_iterations):
        new_guess = (guess + number / guess) / 2.0
        if abs(new_guess - guess) < precision:
            return new_guess
        guess = new_guess

# Function to test the square root calculation and demonstrate assert usage
def test_square_root():
    num = 16.0
    expected_result = 4.0
    result = babylonian_sqrt(num)

    # Use assert statement to check if the result is close enough to the expected value
    assert abs(expected_result - result) < 0.01, f"Expected square root of {num} to be approximately {expected_result}, but got {result}"

# Run the test case
test_square_root()
print("Test passed!")
