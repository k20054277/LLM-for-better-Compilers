
# This Python program demonstrates the use of assert and exception

def divide(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("The result is:", result)

# Asserting a condition
assert num1 % 2 == 0

# Testing the divide function with different inputs
divide(10, 2)
divide(10, 0)
