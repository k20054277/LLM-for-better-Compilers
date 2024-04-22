
import gc

# Define a class with a __del__ method
class MyClass:
    def __init__(self, data):
        self.data = data

    def __del__(self):
        print("Object of MyClass is being destroyed")

# Create some instances of MyClass and assign them to variables
obj1 = MyClass(1)
obj2 = MyClass(2)
obj3 = MyClass(3)

# Assign None to some variables
obj4 = None
obj5 = None

# Print some objects' addresses for reference
print("Address of obj1: ", id(obj1))
print("Address of obj2: ", id(obj2))
print("Address of obj3: ", id(obj3))

# Remove references to obj1 and obj2 from variables, but they still exist
del obj1
del obj2

# Objects that are no longer reachable will be collected by the garbage collector.
# However, we can manually trigger garbage collection using gc.collect()
gc.collect()

# After garbage collection, all objects that were no longer reachable should be destroyed
print("Address of obj1 after GC: ", id(obj1))  # Should print None
print("Address of obj2 after GC: ", id(obj2))  # Should print None
