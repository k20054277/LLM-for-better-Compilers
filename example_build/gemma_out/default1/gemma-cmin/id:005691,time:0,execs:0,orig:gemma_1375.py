
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

# Test code
assert divide(10, 2) == 5
assert divide(10, 0) raises ZeroDivisionError

# Documentation
def help_divide():
    print("The divide function divides two numbers.")
    print("It raises a ZeroDivisionError if the denominator is 0.")
    print("Usage:")
    print("divide(x, y) -> float")
    print("  where:")
    print("    x: The first number.")
    print("    y: The second number.")

print(help_divide())
