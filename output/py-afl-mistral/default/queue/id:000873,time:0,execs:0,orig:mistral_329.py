
class MyClass:
    def __init__(self, name):
        self.name = name

# Using None
var_none = None
print("Type of var_none: ", type(var_none))
if var_none is not None:
    print("Var_none has a value:", var_none)
else:
    print("Var_none is empty or None")

# Creating an object
my_object = MyClass("Example Object")
print("Type of my_object: ", type(my_object))
print("My object's name: ", my_object.name)

# Using None with an object
var_object = MyClass(None)
if var_object is not None:
    print("Var_object has a name:", var_object.name)
else:
    print("Var_object is an empty or None MyClass instance")
