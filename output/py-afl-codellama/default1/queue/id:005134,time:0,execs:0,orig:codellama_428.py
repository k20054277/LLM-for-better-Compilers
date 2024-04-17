def foo(x):
    if x is None:
        return "None"
    else:
        return str(x)

def bar():
    nonlocal x
    x = 5
    print("Inside bar:", foo(x))

bar()