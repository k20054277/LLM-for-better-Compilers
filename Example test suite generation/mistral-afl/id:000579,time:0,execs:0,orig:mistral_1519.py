
def calculate_sum(num1, num2):
    """
    This function takes two numbers as arguments and returns their sum.
    """
    total = num1 + num2
    return total

# Define a tuple with two values
numbers = (3, 4)

# Use assert to check if the length of the input tuple is exactly 2
assert len(numbers) == 2, "Input should be a tuple with exactly 2 elements"

# Extract the numbers from the tuple using tuple unpacking
num1, num2 = numbers

sum_result = calculate_sum(num1, num2)

# Use assert to check if the function returned the expected result
assert sum_result == 7, "Function should return the sum of input numbers"

print("The sum of", num1, "and", num2, "is:", sum_result)
