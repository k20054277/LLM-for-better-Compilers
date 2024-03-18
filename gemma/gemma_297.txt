
def outer():
    nonlocal x
    x = False

    def inner():
        print(x)

    inner()

outer()
