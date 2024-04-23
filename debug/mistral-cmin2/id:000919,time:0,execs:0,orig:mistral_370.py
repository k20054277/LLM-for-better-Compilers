
import numpy as np

def create_numpy_array(input):
    """
    Create a NumPy array if input is not None, otherwise return None.
    """
    if input is not None:
        # Create a NumPy array of zeros with the given shape
        array = np.zeros((3, 3))
        print("Created a NumPy array of shape (3, 3):")
        print(array)
        return array
    else:
        print("Input is None.")
        return None

# Test the function with a None value and a valid argument
test_none = None
print(f"Testing with None: {create_numpy_array(test_none)}")

# Test the function with a valid argument (list)
test_list = [1, 2, 3]
test_array = create_numpy_array(test_list)
print(f"Testing with list: {test_array.shape if test_array is not None else 'None'}")

# Test the function with a valid argument (tuple)
test_tuple = (1, 2, 3)
test_numpy_array = create_numpy_array(test_tuple)
print(f"Testing with tuple: {test_numpy_array.shape if test_numpy_array is not None else 'None'}")
