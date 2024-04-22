
def divide(x, y):
    assert y != 0, "Error: Division by zero is not allowed"
    return x / y

try:
    result = divide(10, 5)
except ZeroDivisionError as e:
    print("Caught expected ZeroDivisionError:", e)
else:
    print("Result:", result)
