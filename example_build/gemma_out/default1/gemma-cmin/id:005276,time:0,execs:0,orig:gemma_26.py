
import sys
import gc

# Define a class to demonstrate memory management
class LargeObject:
    def __init__(self, size):
        self.data = chr(size) * size

    def __del__(self):
        print("Destroyed:", self)

# Create a large object
large_object = LargeObject(100000)

# Use the object
print("Large object:", large_object)

# Force garbage collection
gc.collect()

# Check if the object is still alive
if large_object is not None:
    print("Large object is still alive")

# Print the memory usage before and after garbage collection
print("Memory usage before garbage collection:", sys.getsizeof(large_object))
print("Memory usage after garbage collection:", sys.getsizeof(large_object))

# Delete the object
del large_object

# Check if the object is destroyed
if large_object is None:
    print("Large object is destroyed")

# Print the memory usage after deletion
print("Memory usage after deletion:", sys.getsizeof(large_object))
