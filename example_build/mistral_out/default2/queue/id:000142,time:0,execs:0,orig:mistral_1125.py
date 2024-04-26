
import numpy as np

# Define a NumPy array
data = np.array([1.23, 2.46, 3.78], dtype=np.float32)

# Perform a calculation and assign the result to a variable using 'as' keyword
result, _ = np.square(data)  # Square each element in data
result_str = str(np.max(result))  # Convert maximum value of result to string

print("Original NumPy array:")
print(data)
print("\nCalculated NumPy array:")
print(result)
print("\nMaximum value of calculated NumPy array as a string:")
print(result_str)
