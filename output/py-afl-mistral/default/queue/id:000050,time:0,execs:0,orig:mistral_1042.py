
# Importing numpy library for this example
import numpy as np

# Defining a dictionary with some keys and values
data = {'a': 1, 'b': 2, 'c': 3}

# Using numpy as a module and aliasing it as np
np_array = np.array(list(data.values()))

print("Original NumPy array:")
print(np_array)

# Assigning the first element of the NumPy array to a variable 'x' using as keyword
x = np_array[0] as int

print("\nValue of x after using 'as' keyword:")
print(x)

# Renaming keys in dictionary using del keyword
del data['b']

print("\nDictionary after removing key 'b' using 'del':")
print(data)
