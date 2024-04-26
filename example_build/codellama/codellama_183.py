def foo(x):
    if x > 0:
        return True
    else:
        nonlocal result
        result = False
        return result

result = None
print(foo(5)) # prints True
print(result)  # prints False