
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    return result

num1 = 5
num2 = 0

if num2 == 0:
    print("Error: Cannot divide by zero.")
else:
    quotient = divide(num1, num2)
    if quotient is not None:
        print(f"The result of {num1} divided by {num2} is {quotient}")
