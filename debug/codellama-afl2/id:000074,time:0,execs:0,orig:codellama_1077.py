x = 5

def foo():
    global x
    x += 1
    print(x)

foo()
print(x)