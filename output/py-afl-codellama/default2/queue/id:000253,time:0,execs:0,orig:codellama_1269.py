def test_assert():
    x = 5
    assert x > 0, "x must be positive"
    return x

def test_del():
    x = 5
    y = 10
    del y
    print(x) # output: