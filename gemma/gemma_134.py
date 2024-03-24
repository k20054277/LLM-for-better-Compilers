
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(result)

divide(10, 2)
divide(10, 0)
