
import sys
import gc

# Define a class to demonstrate memory management
class MyClass:
    def __init__(self, data):
        self.data = data

    def __del__(self):
        print("Deleting object:", self)

# Create a list of MyClass objects
my_objects = [MyClass(i) for i in range(10)]

# Use the objects
for obj in my_objects:
    print(obj.data)

# Collect garbage collector
gc.collect()

# Print the remaining objects
print("Remaining objects:")
for obj in gc.get_objects():
    print(obj)
