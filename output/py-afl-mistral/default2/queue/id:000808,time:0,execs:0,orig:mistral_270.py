
# Define a function that takes two arguments, returns the quotient if both are numbers, otherwise returns None
def divide(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        result = x / y
        return result
    else:
        print("Both arguments must be numbers.")
        return None

# Test the function with various inputs
result1 = divide(5, 2)
print(f"Quotient of 5 and 2 is: {result1}")

result2 = divide(5, "three")
print(result2)

result3 = divide("four", 2)
print(result3)

# Use if statement to check if a value is None or not
value = None
if value is None:
    print("Value is None.")
else:
    # If value is not None, perform some operation
    print("Value is not None.")
