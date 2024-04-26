
# This Python program demonstrates the use of and and divmod operators

# Define two numbers
num1 = 10
num2 = 5

# Use the and operator to check if num1 is divisible by num2 and if num1 is greater than num2
if num1 % num2 == 0 and num1 > num2:
  print("num1 is divisible by num2 and num1 is greater than num2")

# Use the divmod operator to find the quotient and remainder when num1 is divided by num2
quotient, remainder = divmod(num1, num2)

# Print the quotient and remainder
print("Quotient:", quotient)
print("Remainder:", remainder)
