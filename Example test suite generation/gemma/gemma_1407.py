
# This Python program demonstrates the use of assert and str

def square(x):
    return x ** 2

assert square(5) == 25
assert str(square(5)) == "25"

print("The value of square(5) is:", square(5))
print("The string representation of square(5) is:", str(square(5)))
