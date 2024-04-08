import numpy as np

# create two arrays
a = np.array([True, False, True, False])
b = np.array([False, True, False, True])

# use 'and' to element-wise AND the arrays
c = a & b

print(c)