
import math

# Define some variables
num1 = 5
num2 = 3
boolean_expr1 = num1 > 0
boolean_expr2 = num2 > 0

# Perform some arithmetic operations using math module
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
remainder = num1 % num2
square_num1 = math.pow(num1, 2)
square_root_num1 = math.sqrt(num1)

# Use and operator to check if both numbers are positive
if boolean_expr1 and boolean_expr2:
    print("Both numbers are positive.")
else:
    print("At least one number is not positive.")

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Remainder: {remainder}")
print(f"Square of {num1}: {square_num1}")
print(f"Square root of {num1}: {square_root_num1}")
