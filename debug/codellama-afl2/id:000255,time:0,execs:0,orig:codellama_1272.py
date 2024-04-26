def my_function(x):
    assert x > 0, "x must be greater than 0"
    if x == 1:
        return "one"
    elif x == 2:
        return "two"
    else:
        return "more than two"