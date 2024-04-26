def check_input(x):
    assert type(x) == int, "Input must be an integer"
    return x**2

print(check_input(5))  # Output: 25
print(check_input("hello"))  # Output: AssertionError: Input must be an integer