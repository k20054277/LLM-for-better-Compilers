def my_function(x, y):
    if x < 0 or y < 0:
        raise ValueError("Negative values are not allowed")
    return x + y

print(my_function(-1, -2)) # This will raise a ValueError because both arguments are negative