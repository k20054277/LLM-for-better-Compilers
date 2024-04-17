
# Function to calculate the square root using simple method (before math.sqrt)
def simple_square_root(number):
    if number >= 0:
        guess = number / 2.0
        while abs(guess*guess - number) > 0.01:
            guess = (guess + number / guess) / 2.0
        return guess
    else:
        raise ValueError("Square root of negative number")

# Function to calculate the factorial
def factorial(n):
    assert n >= 0, "Factorial is not defined for negative numbers"
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

# Testing the functions with some inputs
print("Square root of 4 is:", simple_square_root(4))
print("Square root of 25 is:", simple_square_root(25))
try:
    print("Square root of -1 is:", simple_square_root(-1))
except AssertionError as e:
    print("Error:", e)

print("Factorial of 0 is:", factorial(0))
print("Factorial of 4 is:", factorial(4))
try:
    print("Factorial of -3 is:", factorial(-3))
except ValueError as ve:
    print("Error:", ve)
