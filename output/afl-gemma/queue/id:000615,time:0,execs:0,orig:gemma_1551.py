
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

# Use assert to check if the function raises ZeroDivisionError
assert divide(10, 2) == 5
assert raise ZeroDivisionError == divide(10, 0)

# Use or to provide a default value if the function raises an error
result = divide(10, 2) or 0
print(result)  # Output: 5

# Use assert and or together
assert result == 5 or raise ZeroDivisionError
print(result)  # Output: 5
