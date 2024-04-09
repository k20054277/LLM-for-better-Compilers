
import gc

# Define a class
class Example:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Deleting object:", self.name)

# Create an object
example = Example("John")

# Use the object
print("Object name:", example.name)

# Collect garbage
gc.collect()

# Check if the object is still alive
if example is not None:
    print("Object is still alive")

# Delete the object
del example

# Collect garbage again
gc.collect()

# Check if the object is no longer alive
if example is None:
    print("Object is no longer alive")
