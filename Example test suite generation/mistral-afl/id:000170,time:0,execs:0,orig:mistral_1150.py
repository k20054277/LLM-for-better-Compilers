
import numpy as np

# Create a NumPy array of shape (2, 3) with random integers
random_numbers = np.random.randint(0, 10, size=(2, 3))
print("Original NumPy Array:")
print(random_numbers)

# Type casting using as keyword
single_dimension = random_numbers.reshape(-1)  # flattening the array
int_array = single_dimension.astype('int32')
print("Int32 Array:")
print(int_array)

float_array = int_array.astype('float64')
print("Float64 Array:")
print(float_array)

# Reshaping using as keyword
reshaped_array = np.asarray(random_numbers, dtype='float32').reshape((1, 6))
print("Reshaped NumPy Array (1x6):")
print(reshaped_array)
