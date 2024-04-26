def foo(x):
    if x > 0:
        y = 10
        return y
    else:
        nonlocal y
        y = -10
        return y

y = 5
print(foo(2)) # returns 10
print(y) # returns