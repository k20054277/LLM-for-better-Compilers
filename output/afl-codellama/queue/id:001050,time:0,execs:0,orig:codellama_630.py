def my_function(x):
    if x > 10:
        raise ValueError("x must be less than or equal to 10")
    return True

try:
    my_function(15)
except ValueError as e:
    print(e)