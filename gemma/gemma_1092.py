
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
        print(x)

    inner()
    print(x)

outer()
