
# Function to calculate the square of a number
def calculate_square(number):
    assert number >= 0, "Error: Number should be non-negative"
    return number * number

# Function to determine if a number is even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Testing the calculate_square function
try:
    result = calculate_square(-3)
except AssertionError as error:
    print(error)
else:
    print("Calculated square is:", result)

# Testing some numbers and checking if they are even or odd
numbers = [2, 5, 10, -3]
for number in numbers:
    square = calculate_square(number)
    if is_even(number):
        print(f"{number} is even. Its square is {square}")
    else:
        print(f"{number} is odd. Its square is {square}")
