
# Function to calculate the square of a number
def calculate_square(number):
    return number * number

# Function to test the calculation of square
def test_calculate_square():
    assert type(5) is int, "Expected an integer"
    expected = 25
    actual = calculate_square(5)
    message = "Square of {number} should be {expected}, but got {actual}"
    assert expected == actual, message.format(number=5, expected=expected, actual=actual)
    print("Test passed")

# Function to call test_calculate_square() function
def main():
    try:
        test_calculate_square()
    except AssertionError as e:
        print("Test failed: {}".format(e))

if __name__ == "__main__":
    main()
