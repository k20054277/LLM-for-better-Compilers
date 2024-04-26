
# This Python program demonstrates the use of the and and divmod operators.

# Define two numbers.
a = 10
b = 3

# Use the and operator to check if a and b are both even.
if a % 2 == 0 and b % 2 == 0:
    print("a and b are both even")

# Use the divmod operator to find the quotient and remainder when a is divided by b.
quotient, remainder = divmod(a, b)

# Print the quotient and remainder.
print("Quotient:", quotient)
print("Remainder:", remainder)
