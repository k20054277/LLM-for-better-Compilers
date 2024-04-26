def outer_function():
    x = 5
    def inner_function():
        nonlocal x
        x += 1
        return True
    return inner_function()

print(outer_function()) # Output: True