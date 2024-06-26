
class MyClass:
    # A class property with default value as None
    property = None

    def __init__(self, value=None):
        self.value = value

    # Custom method to set the class property
    @classmethod
    def set_class_property(cls, value):
        cls.property = value

# Creating an instance of MyClass with no initial value
instance1 = MyClass()
print("Instance 1 value: ", instance1.value)
print("Instance 1 class property: ", MyClass.property)

# Setting class property using custom method
MyClass.set_class_property("new_value")

# Creating another instance of MyClass with initial value
instance2 = MyClass("initial_value")
print("Instance 2 value: ", instance2.value)
print("Instance 2 class property: ", MyClass.property)
