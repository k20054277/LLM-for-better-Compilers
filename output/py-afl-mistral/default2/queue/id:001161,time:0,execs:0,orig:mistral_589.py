
class MyClass:
    def __init__(self, name):
        self.is_active = False
        self.name = name

# Create an instance of MyClass
my_instance = MyClass("John Doe")

# Using True to set an attribute
setattr(my_instance, "is_active", True)

# Accessing the new attribute using getattr and printing the result
print(getattr(my_instance, "is_active"))  # Output: True
print(my_instance.is_active)             # Output: True
