
def outer():
    nonlocal x
    x = 10
    print("Outer:", x)

def inner():
    print("Inner:", x)

outer()
inner()

print("Global:", x)
