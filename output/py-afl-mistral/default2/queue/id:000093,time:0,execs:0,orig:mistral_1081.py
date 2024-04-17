
# Define a tuple with two integers
numbers = (10, 5)

# Use divmod() to get quotient and remainder
quotient, remainder = divmod(numbers[0], numbers[1])

# Print the result using f-strings
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")

# Use as keyword for unpacking the tuple returned by divmod()
x, y = divmod(numbers[0], numbers[1])

# Print the result using f-strings
print(f"Quotient using as keyword: {x}")
print(f"Remainder using as keyword: {y}")
