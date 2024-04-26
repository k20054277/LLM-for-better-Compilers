
def foo(a, b):
    print("Inside foo:", a, b)
    as c, d = a, b
    print("Inside foo, using as:", c, d)
    locals()["e"] = 10
    print("Inside foo, using locals:", e)

foo(2, 3)
print("Outside foo:", a, b, e)
