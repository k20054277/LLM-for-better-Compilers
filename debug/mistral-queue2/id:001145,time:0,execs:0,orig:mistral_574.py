
import numpy as np

# Creating two NumPy arrays
array1 = np.random.rand(5, 5)
array2 = np.random.rand(5, 5) + 0.5

print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)

# Creating memoryviews from NumPy arrays
memview_array1 = np.ascontiguousarray(array1).tobytes()
memview_array2 = np.ascontiguousarray(array2).tobytes()
memoryview_arrays = [np.frombuffer(m, dtype=np.float32) for m in (memview_array1, memview_array2)]
memoryviews = [memoryview(m) for m in memoryview_arrays]

# Perform element-wise AND operation using memoryviews
result = np.bitwise_and(memoryviews[0], memoryviews[1])
result_memview = memoryview(result)

# Convert the result back to a NumPy array
np_result = np.frombuffer(result_memview, dtype=np.float32).reshape((5, 5))

print("\nResult:")
print(np_result)

# Perform the same operation using Boolean True values
boolean_arrays = [np.full((5, 5), True) for _ in range(2)]
boolean_results = np.bitwise_and(boolean_arrays[0], boolean_arrays[1]).astype(np.float32).reshape((5, 5))

print("\nResult using Boolean True values:")
print(boolean_results)
