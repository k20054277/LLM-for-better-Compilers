def assert_next(n):
    assert n > 0, "n must be positive"
    if n == 1:
        return 1
    else:
        return n * assert_next(n-1)

print(assert_next(5)) # should print