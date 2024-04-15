
class MyClass:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

# Create an instance of MyClass with some values
my_instance = MyClass("John Doe", 30)
print(my_instance.name) # Output: John Doe
print(my_instance.age) # Output: 30

# Set an attribute to None using delattr
delattr(my_instance, "age")
print(my_instance.age) # Output: None

# Setting an attribute to None in the constructor
none_instance = MyClass(None, None)
print(none_instance.name) # Output: None
print(none_instance.age) # Output: None
