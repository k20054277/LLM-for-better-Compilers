
import math

# Function to calculate the square root using math.sqrt()
def calc_square_root(number):
    return math.sqrt(number)

# Function to check if a number is perfect square
def is_perfect_square(number):
    sqrt = calc_square_root(number)
    return (sqrt * sqrt).is_integer()

# Testing the functions
num = 16
square_root = calc_square_root(num)
print("The square root of", num, "is:", square_root)

if is_perfect_square(num):
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square")

# Testing with an incorrect input
num = 15
square_root = calc_square_root(num)
assert math.isclose(square_root * square_root, num), f"{num} is not a perfect square"
print("The square root of", num, "is:", square_root)
if is_perfect_square(num):
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square")
