
# Custom Base Class
class MyBaseClass:
    def __init__(self, value=None):
        self.value = value

# Custom Subclass
class MySubclass(MyBaseClass):
    pass

# Instantiating with None and without any arguments
my_instance_none = MySubclass(None)
print(f"Instance using None: {my_instance_none.value}")  # Output: Instance using None: None

# Instantiating with an argument
my_instance_arg = MySubclass("Hello, World!")
print(f"Instance with an argument: {my_instance_arg.value}")  # Output: Instance with an argument: Hello, World!
