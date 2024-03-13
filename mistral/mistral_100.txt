
# Define a custom class with a boolean value as an attribute
class MyClass:
    def __init__(self, is_active=False):
        self.is_active = is_active

# Create instances of MyClass with different boolean values
instance1 = MyClass()
instance2 = MyClass(True)

# Check the type and value of the boolean attribute for each instance
print(f"Type of instance1.is_active: {type(instance1.is_active)}")
print(f"Value of instance1.is_active: {instance1.is_active}")
print(f"Type of False: {type(False)}")
print(f"Value of False: {False}")

# Comparing False with an attribute value using == operator
print(f"Comparing instance1.is_active with False: {instance1.is_active == False}")
