
# Assigning an alias to a variable using numpy library
import numpy as np
x = np.array([1, 2, 3, 4]) as y
print("Original variable: ", x)
print("Aliased variable: ", y)

# Both variables (x and y) refer to the same numpy array
print(id(x))
print(id(y))
