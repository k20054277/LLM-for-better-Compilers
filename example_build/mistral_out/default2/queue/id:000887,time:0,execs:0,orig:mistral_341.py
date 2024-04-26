
# Define an empty class as a base
class MyClass: pass

# Create an instance of the class with no initial attributes
my_instance = MyClass()

# Using None to represent the absence of an attribute
print("Initial state: my_instance.attribute is", my_instance.attribute)  # Output: AttributeError: 'MyClass' object has no attribute 'attribute'
my_instance.attribute = None
print("Setting an attribute to None:", my_instance.attribute)  # Output: None

# Using setattr to dynamically add and modify attributes
setattr(my_instance, "new_attribute", 42)
print("Adding a new attribute with setattr: my_instance.new_attribute is", my_instance.new_attribute)  # Output: Adding a new attribute with setattr: my_instance.new_attribute is 42
setattr(my_instance, "another_attribute", [1, 2, 3])
print("Adding a list as an attribute with setattr: my_instance.another_attribute is", my_instance.another_attribute)  # Output: Adding a list as an attribute with setattr: my_instance.another_attribute is [1, 2, 3]
