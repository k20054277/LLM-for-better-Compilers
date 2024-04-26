
import timeit

def method1(num1, num2, lower_limit, upper_limit):
""" checking range using if statements """
if (num1 >= lower_limit) and (num1 <= upper_limit) and (num2 >= lower_limit) and (num2 <= upper_limit):
    print(f"{num1}, {num2} are within the given range.")

def method2(num1, num2, lower_limit, upper_limit):
""" checking range using and operator """
if (lower_limit <= num1 <= upper_limit) and (lower_limit <= num2 <= upper_limit):
    print(f"{num1}, {num2} are within the given range.")

# Test data
num1 = 10
num2 = 15
lower_limit = 5
upper_limit = 20

method1(num1, num2, lower_limit, upper_limit)
method2(num1, num2, lower_limit, upper_limit)

# Performance test using timeit module
setup = """
from __main__ import method1, method2, lower_limit, upper_limit
num1 = 10
num2 = 15
"""

print("Performance of method1:")
print(timeit.timeit(lambda: method1(num1, num2, lower_limit, upper_limit), number=100000))

print("Performance of method2:")
print(timeit.timeit(lambda: method2(num1, num2, lower_limit, upper_limit), number=100000))
