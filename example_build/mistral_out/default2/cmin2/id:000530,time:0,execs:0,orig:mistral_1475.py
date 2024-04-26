
import numpy as np

def add(a, b):
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Both a and b must be numbers"
    return a + b

def batch_process(arrays, func):
    """Batch process a list of arrays using given function"""
    result = np.array([func(arr) for arr in arrays])
    assert len(result) == len(arrays, "Number of results must equal the number of input arrays"), \
        "Error in batch processing: Number of results is not equal to number of input arrays"
    return result

# Test adding two numbers
assert add(2, 3) == 5

# Test adding a string and a number
try:
    add("hello", 3)
except AssertionError as e:
    print(e)

# Batch process arrays using addition function
arrays = [np.array([1, 2, 3]), np.array([4, 5, 6])]
result = batch_process(arrays, add)
assert result.shape == (2, 3), "Shape of results must match the shape of input arrays"
print(result)
