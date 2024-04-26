
def divide(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return False
    else:
        print(f"Result: {result}")
        return True

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    divide(num1, num2)

    num1 = 10
    num2 = 0
    divide(num1, num2)
