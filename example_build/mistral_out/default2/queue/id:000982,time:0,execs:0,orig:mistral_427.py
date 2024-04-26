
def divide(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return result

# Test the divide function with valid input
x = 10
y = 5
print(f"Result: {divide(x, y)}")

# Test the divide function with an error input
try:
    print(f"Result: {divide(3, 0)}")
except Exception as e:
    print("Error:", e)
