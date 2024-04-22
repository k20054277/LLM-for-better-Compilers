
# Function to calculate the square root of a number using Newtons method
def sqrt(number):
    guess = number / 2.0
    while abs(guess * guess - number) > 0.01:
        guess = (guess + number / guess) / 2.0
    return guess

# Function under test which calculates the square of a number
def square(number):
    assert number >= 0, "Number must be non-negative"
    return number * number

# Testing the square function
num = 5
result = square(num)
assert result == num*num, f"Expected {num*num}, got {result}"
print("Square of {num} is correct")

# Calculate and check the square root of a number
num = 16
result = sqrt(num)
expression = result * result - num
assert expression < 0.01, f"Expected square root of {num} to be close to {result}, but got expression: {expression}"
print(f"Square root of {num} is close to {result}")
