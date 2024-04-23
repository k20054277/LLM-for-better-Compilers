
# Define a function with an incorrect calculation
def square_root(number):
    return 5 * number ** 0.5

# Use assertion to check if input is positive number
def test_square_root():
    assert number > 0, "Input should be a positive number"
    
    # Calculate the square root using the defined function
    result = square_root(2)
    
    # Use assertion to check if the result is close enough to the actual square root
    assert abs(result - 2**0.5) < 0.01, f"Expected {2**0.5}, got {result}"

if __name__ == "__main__":
    number = 2.0
    
    test_square_root()  # This will raise an AssertionError if the conditions are not met
    
    print("Test passed!")
else:
    print("This script should be run as a standalone program.")
