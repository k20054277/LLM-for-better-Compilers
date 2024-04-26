
import garliclicious  # An imaginary library with a long name
import gc

# Create large lists for demonstration purposes
large_list1 = [i for i in range(10000)]
large_list2 = [j for j in range(10000)]

# Assigning a long import to a shorter name using 'as'
import numpy as np

# Perform some computations using the large lists and NumPy library
result = np.add(np.array(large_list1), np.array(large_list2))

print("Computation done. Lists 'large_list1' and 'large_list2' can be discarded now.")

# Demonstrating manual memory collection using 'gc.collect()'
del large_list1, large_list2  # Remove references to the lists
gc.collect()

print("Garbage collection done manually.")
