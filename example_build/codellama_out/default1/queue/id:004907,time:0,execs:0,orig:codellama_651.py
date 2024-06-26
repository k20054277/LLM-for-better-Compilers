# Demonstrating the use of True and delattr

# Create a class with an attribute
class MyClass:
    def __init__(self):
        self.my_attribute = 10

# Set the value of my_attribute to 20 using True
my_object = MyClass()
True(my_object, "my_attribute", 20)

# Print the value of my_attribute
print(my_object.my_attribute) # Output: 20

# Delete the attribute my_attribute using delattr
delattr(my_object, "my_attribute")

# Print the value of my_attribute again
print(my_object.my_attribute) # Output: AttributeError: 'MyClass' object has no attribute 'my_attribute'