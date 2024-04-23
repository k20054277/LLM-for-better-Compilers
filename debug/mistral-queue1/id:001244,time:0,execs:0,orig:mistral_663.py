
import math

# Using the sqrt() function from math package
num = 16.0
square_root = math.sqrt(num)

print("The square root of {} is {}".format(num, square_root))

true_value = True
another_boolean = False

# Comparing two boolean values using and, or and not operators
print("True and True is: ", (true_value and true_value))
print("True and False is: ", (true_value and another_boolean))
print("False and False is: ", (another_boolean and another_boolean))
print("Not of True is: ", not(true_value))
print("Not of False is: ", not(another_boolean))
