def outer():
    x = 10
    def inner():
        print(x)
    inner()

outer() # prints 10

def outer2():
    x = 20
    def inner2():
        nonlocal x
        x = 30
    inner2()
    print(x) # prints 30

outer2()