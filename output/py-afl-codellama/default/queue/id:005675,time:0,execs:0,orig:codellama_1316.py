def assert_max(x, y):
    assert x <= y, f"{x} is greater than {y}"
    return y

print(assert_max(3, 4)) # Output: 4
print(assert_max(4, 3)) # Output: AssertionError: 4 is greater than