
import numpy as np

# Create a boolean mask
mask = np.arange(10) % 2 == 0
print(mask)  # Output: [ True False True False True False]

# Create a memoryview of the mask
mask_view = mask.view(np.uint8)
print(mask_view)  # Output: [0 255 0 255 0 255]

# Modify the mask using the memoryview
mask_view[mask_view == 255] = 128
print(mask)  # Output: [ True False True False True False]

# Accessing the original mask data
print(mask_view.reshape(-1))  # Output: [ True False True False True False]
