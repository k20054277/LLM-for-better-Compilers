def foo(x, y):
    if x > 0 and y > 0:
        return True
    else:
        return False

def bar():
    nonlocal x = 10
    nonlocal y = 20
    if foo(x, y):
        print("The values of x and y are greater than zero.")
    else:
        print("The values of x and y are not greater than zero.")

bar()