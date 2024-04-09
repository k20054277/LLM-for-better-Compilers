
import sys
import gc

# Define a class to demonstrate the use of as and memorymanagement+
class MyClass:
    def __init__(self, data):
        self.data = data

    def __del__(self):
        print("Deleting object:", self)

# Create a MyClass object
my_object = MyClass(10)

# Use the as keyword to associate the object with the variable "my_object_as"
my_object_as = my_object

# Print the object information
print("Object:", my_object)

# The object is still referenced by the variable "my_object_as"
print("Object reference:", my_object_as)

# Delete the object using the variable "my_object_as"
del my_object_as

# The object is no longer referenced and will be garbage collected
gc.collect()

# Print the output
print("After garbage collection:")
print("Object:", my_object)  # This line should output None
