
# Define a function that calculates the square root of a number using the Newton-Raphson method
def sqrt(number):
    guess = number / 2.0
    while abs(guess * guess - number) > 0.01:
        guess = (guess + number / guess) / 2.0
    return guess

# Use assert statements to test the input and output of the sqrt function
assert number >= 0, "Input must be non-negative"
result = sqrt(4.0)
assert abs(result * result - 4.0) < 0.01, "sqrt(4.0) should be 2.0, not {}".format(result)
