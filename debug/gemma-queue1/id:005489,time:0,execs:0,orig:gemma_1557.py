
# This Python program demonstrates the use of assert and ...

def square(x):
    return x ** 2

assert square(5) == 25
print(square(5))

# The following line will raise an error, as square(6) does not equal 36
assert square(6) == 36

print("The program has completed.")
