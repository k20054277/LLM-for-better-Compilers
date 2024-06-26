
import numpy as np

# Create a NumPy array of 10 bytes
arr = np.arange(10).astype(np.uint8)

# Convert the array to a bytearray
arr_bytearray = np.array(arr).astype(np.uint8).to_bytes()

# Print the data of the bytearray
print(arr_bytearray)

# Print the elements of the array
print(arr)
