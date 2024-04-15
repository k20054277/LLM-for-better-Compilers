
# Define a function that calculates the square root of a number
def sqrt(number):
    return number ** 0.5

# Use an assert statement to check if a number has a positive square root
number = 4
assert number >= 0, "Number must be non-negative"
result = sqrt(number)
print("The square root of {} is {}".format(number, result))
