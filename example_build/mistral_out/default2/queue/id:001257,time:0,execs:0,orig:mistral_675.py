
def divide(dividend, divisor):
    """This function divides two numbers."""

    try:
        result = dividend / divisor
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(e)
        raise ValueError("Error: Division by zero is not allowed.")

# Input values
num1 = 10
num2 = 5

# Calling the function
divide(num1, num2)

# Calling the function with an error condition
try:
    divide(num1, 0)
except Exception as e:
    print("Error:", e)
