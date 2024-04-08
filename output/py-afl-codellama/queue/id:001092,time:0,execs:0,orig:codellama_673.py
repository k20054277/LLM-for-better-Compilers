import numpy as np

# create a NumPy array
arr = np.array([1, 2, 3, 4])

# use True to check if an element is present in the array
if True in arr:
    print("Element found")
else:
    print("Element not found")

# use memoryview to access the underlying data of the array
mv = memoryview(arr)
print(mv.nbytes)  # prints the number of bytes in the array