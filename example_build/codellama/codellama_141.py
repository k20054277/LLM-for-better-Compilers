import math

x = 2
y = 3

if x < y and math.gcd(x, y) == 1:
    print("The greatest common divisor of", x, "and", y, "is 1.")
else:
    print("The greatest common divisor of", x, "and", y, "is not 1.")