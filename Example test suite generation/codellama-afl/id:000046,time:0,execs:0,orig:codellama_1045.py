def foo(x):
    try:
        y = x / 0
    except ZeroDivisionError as e:
        raise ValueError("Division by zero not allowed") from e
    return y

print(foo(5)) # Output: 5
print(foo(0)) # Output: Traceback (most recent call last): ...