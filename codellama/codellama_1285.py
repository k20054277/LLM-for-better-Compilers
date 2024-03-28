def test_function(x, y):
    assert x > 0, "x must be positive"
    assert y > 0, "y must be positive"
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"{x} divided by {y} is {result}")