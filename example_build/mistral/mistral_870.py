
# Simple usage of 'and' keyword in if statement
num1 = 5
num2 = 10

if num1 > 0 and num2 > 0:
    print("Both numbers are positive.")
else:
    print("One or both numbers are not positive.")

# Usage of 'and' keyword with variables and constants
boolean_expression = (num1 > 0) and (num2 % 2 == 0)
if boolean_expression:
    print("Num1 is positive and Num2 is even.")
else:
    print("Condition is false.")

# Usage of 'pow' function to raise a number to an exponent
base = 2
exponent = 3
result = pow(base, exponent)
print(f"Result of {base} raised to the power of {exponent} is: {result}")
