
import numpy as np

# Create two arrays with boolean values
arr1 = np.array([1, 0, 1, 0, 1])
arr2 = np.array([1, 1, 0, 1, 0])

# Use NumPy's where() function to get the elements that are in arr1 and arr2
mask = np.where(np.logical_and(arr1, arr2), arr1, arr1)

print("Array 1:")
print(arr1)
print("Array 2:")
print(arr2)
print("Mask (elements in both arrays):")
print(mask)

# Use Python's 'and' keyword for boolean logic with scalar values
x = 5
y = 10
z = x > 4 and y < 7

if z:
    print(f"{x} is greater than 4 and {y} is less than 7")
else:
    print("Either x is not greater than 4 or y is not less than 7")
