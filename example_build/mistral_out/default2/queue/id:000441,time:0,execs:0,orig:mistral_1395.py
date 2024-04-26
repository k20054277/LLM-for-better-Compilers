
import numpy as np

# Function to validate input data shape and type
def validate_input(data):
    if not isinstance(data, np.ndarray):
        raise TypeError("Input should be a NumPy array")
    if data.shape[1] != 2:
        raise ValueError("Input array should have shape (samples, 2)")

# Function to perform matrix operations using NumPy
def scale_data(data):
    assert validate_input(data), "Invalid input data"
    min_value = np.min(data, axis=0)
    max_value = np.max(data, axis=0)
    scaled_data = (data - min_value) / (max_value - min_value)
    return scaled_data

# Example usage:
input_data = np.array([[1, 3], [2, 4], [5, 6]])
scaled_data = scale_data(input_data)

print("Input Data:")
print(input_data)
print("\nScaled Data:")
print(scaled_data)
