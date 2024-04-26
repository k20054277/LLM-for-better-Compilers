
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        print(f"The result of {x} divided by {y} is: {result}")

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    divide(num1, num2)

    num1 = 10
    num2 = 0
    divide(num1, num2)
