
def outer():
    x = 10
    def inner():
        nonlocal x
        print(x)
    inner()

outer()
