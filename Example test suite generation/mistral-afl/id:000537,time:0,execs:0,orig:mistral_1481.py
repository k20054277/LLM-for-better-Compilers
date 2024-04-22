
# This function calculates the square root of a number
def sqrt(number):
    if number >= 0:
        return number ** 0.5
    else:
        raise ValueError("Cannot take the square root of a negative number")

# This function checks if a number is an integer and greater than zero
def is_positive_integer(n):
    assert isinstance(n, int), "Input must be an integer"
    assert n > 0, "Input must be positive"

# Now we call these functions with some input
try:
    x = sqrt(-1)
except ValueError as e:
    print("Error:", e)

is_positive_integer(5)
is_positive_integer(-3)
