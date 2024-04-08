
def division(num1, num2):
    try:
        result = num1 / num2
        print("The result is:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("The program has finished")

division(10, 2)
division(10, 0)
