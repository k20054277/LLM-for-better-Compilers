def foo(x):
    return x + 1

print(callable(foo)) # prints "True"
print(callable(5)) # prints "False"

bar = foo(2)
print(callable(bar)) # prints "True"