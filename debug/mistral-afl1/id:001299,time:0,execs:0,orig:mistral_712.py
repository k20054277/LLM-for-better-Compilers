
# Using True
boolean_variable = True
if boolean_variable:
    print("This statement will be executed.")

# Memory Management in Python
# Python automatically manages memory through a process called Garbage Collection.
# When an object is no longer being referenced by any variable, it becomes eligible for garbage collection.
# The Python interpreter periodically checks the memory and frees up any memory occupied by objects that are no longer in use.

# Here's an example showing Python's memory management:
class MyClass:
    def __init__(self):
        self.data = [i for i in range(10000)]
        
my_object = MyClass()  # This creates a new instance of MyClass and allocates memory for the list.
del my_object             # Once we're done with 'my_object', we delete it and make the memory it occupied eligible for garbage collection.
# The Python interpreter will eventually free up the memory used by 'my_object'.
