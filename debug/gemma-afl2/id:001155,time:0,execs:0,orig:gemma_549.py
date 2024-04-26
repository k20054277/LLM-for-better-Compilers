
import sys

# Demonstrate the use of None and memory management

# Define a class to manage memory
class MyClass:
    def __init__(self, data):
        self.data = data

    def __del__(self):
        print("Object deleted:", self.data)

# Create an instance of the class
my_object = MyClass(10)

# Use the object
print("Object data:", my_object.data)

# None is assigned to the object
my_object = None

# The object is deleted when it goes out of scope
print("Memory management:", sys.getrefcount(my_object))

# Output:
# Object data: 10
# Object deleted: 10
# Memory management: 0
