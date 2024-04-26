
def nonlocal_func():
    nonlocal x
    x = 10
    assert x == 10
    print(x)

nonlocal_func()
