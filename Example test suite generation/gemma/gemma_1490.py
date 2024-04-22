
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("The result is:", result)
    assert result is not None
    print("The assert statement passed")


divide(10, 2)
divide(10, 0)
