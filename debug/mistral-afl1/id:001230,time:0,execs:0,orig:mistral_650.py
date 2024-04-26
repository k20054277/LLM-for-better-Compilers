
class MyClass:
    def __init__(self):
        self.my_attribute = 42

    @property
    def my_property(self):
        return self.my_attribute * 2

if __name__ == "__main__":
    obj = MyClass()

# Check if 'MyClass' has an attribute named 'my_attribute' using hasattr
print("Has attribute 'my_attribute':", hasattr(MyClass, "my_attribute"))

# Create an instance of 'MyClass' and check for presence of methods and attributes
print("\nInstance 'obj' has method 'my_property':", hasattr(obj, "my_property"))
print("Instance 'obj' has attribute 'my_attribute':", hasattr(obj, "my_attribute"))

# Check if the method 'my_property' of 'MyClass' is a method using ismethod
print("\n'MyClass.my_property' is a method:", ismethod(getattr(MyClass, "my_property")))
