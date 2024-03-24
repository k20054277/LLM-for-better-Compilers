
import numpy as np

# Using Python's built-in True boolean value
x = 10
y = 20
z = -5

if x > 0 and y > 0 and z > 0:
    print("All numbers are positive")
else:
    print("At least one number is not positive")

# Using NumPy array with only True values
np_array = np.full((3, 3), True)
print(np_array)

# Using NumPy to create an array of boolean values based on a condition
numbers = np.array([1, -2, 3, 0, 5])
boolean_values = numbers > 0
print(boolean_values)
