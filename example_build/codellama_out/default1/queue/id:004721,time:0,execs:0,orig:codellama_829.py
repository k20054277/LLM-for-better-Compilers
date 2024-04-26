# This program demonstrates the use of 'and' and 'from' keywords in Python

# Importing 'math' module to perform mathematical operations
import math

# Using 'and' keyword to check if a number is even and greater than 5
print("Is 8 an even number greater than 5?")
if 8 and (8 % 2 == 0) and (8 > 5):
    print("Yes, it is.")
else:
    print("No, it is not.")

# Using 'from' keyword to import specific functions from a module
print("\nImporting only 'pow' function from the 'math' module:")
from math import pow
print(pow(2, 3))