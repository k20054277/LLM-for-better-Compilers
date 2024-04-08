
import numpy as np

# Create a NumPy array of 10 integers
arr = np.arange(10)

# Convert the array to a bytearray
arr_byte = arr.tobytes()

# Print the bytearray
print(arr_byte)

# Convert the bytearray back to an array
arr_recovered = np.frombuffer(arr_byte, dtype=np.int)

# Print the recovered array
print(arr_recovered)
