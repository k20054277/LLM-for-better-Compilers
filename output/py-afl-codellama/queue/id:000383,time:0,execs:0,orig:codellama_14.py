# Demonstrate the use of True and garbage collection

# Create a simple class that holds a reference to an object
class MyClass:
    def __init__(self, obj):
        self.obj = obj

# Create an instance of the class with a reference to an object
my_object = "Hello"
my_class = MyClass(my_object)

# Print the value of my_object and my_class.obj
print("Before garbage collection:")
print(my_object, my_class.obj)

# Run the garbage collector to release the reference to my_object
gc.collect()

# Print the value of my_object and my_class.obj again after garbage collection
print("After garbage collection:")
print(my_object, my_class.obj)