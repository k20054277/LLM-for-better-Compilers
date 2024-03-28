
def divide(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return False
    else:
        print(f"Result: {result}")
        return True

# Test cases
if divide(10, 2):
    print("Test case 1: Success")
else:
    print("Test case 1: Error")

if divide(5, 0):
    print("Test case 2: Success")
else:
    print("Test case 2: Error")

if divide(3, 3):
    print("Test case 3: Success")
else:
    print("Test case 3: Error")
