
# Import numpy module and rename alias to 'np' using 'as' keyword
import numpy as np

# Create a dictionary as a namespace
my_namespace = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y
}

# Import another module and rename alias to 'ms' using 'as' keyword
import math as ms

# Use functions from numpy and my_namespace namespace
print("Numpy add: ", np.add(2, 3))
print("Namespace add: ", my_namespace["add"](2, 3))

print("Numpy subtract: ", np.subtract(2, 3))
print("Namespace subtract: ", my_namespace["subtract"](2, 3))

print("Square root of 16: ", ms.sqrt(16))
