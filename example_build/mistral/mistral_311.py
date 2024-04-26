
class MyClass:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
        self.hidden_attribute = None

    def greet(self):
        if self.name is not None:
            print(f"Hello, {self.name}!")
        else:
            print("Hi there!")


# Create an instance of MyClass with no initial value for name and age
my_instance = MyClass()

# Use None intentionally for some attributes
my_instance2 = MyClass(None, 30)

print("Checking if 'name' exists in my_instance:")
print(hasattr(my_instance, "name"))  # False
print(getattr(my_instance, "name", "Not defined"))  # Not defined

print("Checking if 'age' exists in my_instance:")
print(hasattr(my_instance, "age"))  # True
print(getattr(my_instance, "age"))  # None

print("\nChecking if 'hidden_attribute' exists in my_instance:")
print(hasattr(my_instance, "hidden_attribute"))  # True
print(getattr(my_instance, "hidden_attribute"))  # None

print("\nCalling methods on my_instance with and without name defined:")
my_instance.greet()  # Hi there!
my_instance.name = "John"
my_instance.greet()  # Hello, John!
