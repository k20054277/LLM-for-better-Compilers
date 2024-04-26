
def divide(num1, num2):
    try:
        result = num1 / num2
        print("Result: {0}".format(result))

        # Check if number is even
        if num1 % 2 == 0:
            print("Number 1 is even.")
        else:
            print("Number 1 is odd.")
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
    finally:
        print("Executing finally block.")

if __name__ == "__main__":
    num1 = 6
    num2 = 3
    divide(num1, num2)

    num1 = 5
    num2 = 0
    try:
        divide(num1, num2)
    except Exception as e:
        print("Caught an exception! Message: {0}".format(e))
