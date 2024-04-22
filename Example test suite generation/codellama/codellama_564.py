# Demonstration of None and Resource in Python

# Importing necessary libraries
import sys
import os

# Declaring variables to demonstrate None and resource
var1 = 5
var2 = "hello"
var3 = None
var4 = 10

# Printing the values of variables
print("Before using 'None' and 'resource', the values of variables are:")
print(var1, var2, var3, var4)

# Using None and resource
var3 = None
var4 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Printing the values of variables after using None and resource
print("\nAfter using 'None' and 'resource', the values of variables are:")
print(var1, var2, var3, var4)