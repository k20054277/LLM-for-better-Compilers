
import math

# Using False boolean value
x = -5.3
if x < 0:
    print("Number is negative")
else:
    print("Number is non-negative or positive")

# Using math library
x = 5
y = 2
z = math.sqrt(x)
print("The square root of {} is {}".format(x, z))

# False comparison with a number
if not (x > y):
    print("{} is less than or equal to {}".format(x, y))
