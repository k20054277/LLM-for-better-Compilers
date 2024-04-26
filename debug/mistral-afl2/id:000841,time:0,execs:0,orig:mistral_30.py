
def divide(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
        raise
    else:
        if result.is_integer():
            print(f"Result: {result} (This is an integer)")
            return int(result)
        else:
            print(f"Result: {result}")
            return result

# Calling the divide function with valid inputs
print("Result of dividing 10 by 3 is:")
print(divide(10, 3))

# Calling the divide function with invalid input (zero divisor)
try:
    print("Result of dividing 10 by 0 is:")
    divide(10, 0)
except ZeroDivisionError as e:
    print(e)
else:
    print("This should not be printed.")

# Demonstrating the use of False
def greater_than_five(number):
    if number > 5:
        return True
    else:
        raise ValueError("Number is not greater than five.")

if greater_than_five(4):
    print("Number is indeed greater than five.")
else:
    print("Number is not greater than five.")
