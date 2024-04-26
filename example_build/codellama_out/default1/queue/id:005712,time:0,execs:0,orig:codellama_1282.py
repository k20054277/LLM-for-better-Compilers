def test():
    x = 5
    assert x > 0, "x must be positive"
    return x

def main():
    x = 10
    nonlocal x
    x = test()
    print(x)

main()