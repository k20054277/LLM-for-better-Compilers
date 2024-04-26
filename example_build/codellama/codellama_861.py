# This program demonstrates the use of `and` and `global` in Python

x = 5
y = 10

def test(a, b):
    global x, y
    if a > 0 and b > 0:
        x = a + b
        y = a - b

test(3, 4)
print("x =", x)
print("y =", y)