
# Get user input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Check if both numbers are positive using the and operator
if num1 > 0 and num2 > 0:
    print("Both numbers are positive.")
else:
    print("One or both of the numbers is not positive.")

# Perform an operation on the numbers if they are both positive
if num1 > 0 and num2 > 0:
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")
