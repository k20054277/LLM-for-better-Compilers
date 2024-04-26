def foo(x):
    assert callable(x), "Argument 'x' must be a function"
    return x()

print(foo(lambda: 5)) # prints 5
print(foo("Hello")) # raises an AssertionError, because "Hello" is not a function