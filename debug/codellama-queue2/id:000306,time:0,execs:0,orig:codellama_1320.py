import numpy as np

# Define a function that takes a 2D array as input and returns the transpose of the array
def transpose(arr):
    # Use assert to check that the input is a 2D array
    assert len(arr.shape) == 2, "Input must be a 2D array"
    # Use memoryview to create a view of the array
    m = np.asarray(arr).T
    return m

# Test the function
a = np.array([[1, 2, 3], [4, 5, 6]])
print(transpose(a)) # Output: [[1, 4]
                     #         [2, 5]
                     #         [3, 6]]