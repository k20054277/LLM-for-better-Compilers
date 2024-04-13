def demo_and_locals():
    x = 5
    y = 3
    print(x)
    if x > 0 and y > 0:
        z = x + y
        print(z)
    return locals()

print(demo_and_locals())