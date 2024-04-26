
def square(x):
    return x**2

# using as to bind a temporary variable to the parameter x
as y = square(5)
print(y)

# using parameter with default value
def cube(x=2):
    return x**3

print(cube())
print(cube(3))
