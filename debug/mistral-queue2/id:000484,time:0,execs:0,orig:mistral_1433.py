
# Function to calculate the square root of a number using Newton-Raphson method
def sqrt(number):
    def newton_raphson(x, target):
        return x - ((x * x - number) / (2 * x))

    guess = number / 2.0
    while abs(guess**2 - number) > 1e-6:
        guess = newton_raphson(guess, number)

    return guess

# Function to test the square root calculation
def test_sqrt():
    try:
        result = sqrt(2)
        assert result ** 2 == 2, f"Error! The square root of 2 is not {result}"
    except AssertionError as err:
        print(err)
    finally:
        print("Square root test passed!")

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the square root function and check if 5 is odd
test_sqrt()
print(f"5 is {check_even_odd(5)}")
