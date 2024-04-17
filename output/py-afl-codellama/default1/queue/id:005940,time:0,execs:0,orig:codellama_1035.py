x = 5

def foo():
    x = 10
    print(x)

def bar():
    global x
    x = 20
    print(x)

foo()
print(x)
bar()
print(x)