
# An example function that may or may not return a value
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None
    else:
        return result

x = 10
y = 2
result = divide(x, y)

if result is not None:
    print(f"Result: {result}")
else:
    print("No result.")
