
import numpy as np

# Create a NumPy array
data = np.array([1, 2, 3, 4, 5], dtype=np.float32)

# Create a memoryview from the NumPy array
memview = np.ascontiguousarray(data).astype('B').view('B0')

# Perform some calculations using the memoryview
shape = memview.shape
stride = memview.strides[0]
offset = memview.base + stride * 1
element1 = memview[offset]

index = 1
offset = memview.base + stride * index
element2 = memview[offset]

result = np.add(element1, element2).item()

# Use assert statements to verify the results
assert result == 3.0, "The sum of the first two elements is not correct."
assert memview.shape == (len(data),), "The shape of the memoryview is incorrect."
