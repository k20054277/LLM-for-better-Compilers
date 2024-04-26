
# Import individual functions from numpy as 'np' alias
import numpy as np

# Import matplotlib.pyplot as 'plt' alias and renaming NumPy nucleotide array as 'ndarray'
import matplotlib.pyplot as plt
from numpy import ndarray

# Using np and plt in the script
np_array = np.array([1, 2, 3, 4])
plt_scatter = plt.scatter(np_array, np_array)

# Using ndarray from NumPy in matplotlib
plt.hist(np.random.randn(1000).astype(ndarray), bins=20)
plt.show()
