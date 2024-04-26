
# Define a custom class named MyClass
class MyClass:
    def __init__(self, value=0):
        self.value = value

# Create an instance of MyClass
my_instance = MyClass(5)

# Using hasattr() to check if 'MyInstance' has an attribute named 'some_attribute' (which it doesn't)
if not hasattr(my_instance, 'some_attribute'):
    print("The instance 'my_instance' does not have the 'some_attribute'.")
    # Assign a new attribute to the instance if the condition is true
    my_instance.some_attribute = 10
    print(f"Assigned new attribute 'some_attribute' with value: {my_instance.some_attribute}")
else:
    print("The instance 'my_instance' already has the 'some_attribute'.")

# Printing the values of attributes of 'my_instance' to verify the changes
print(f"The value of 'value' attribute is: {my_instance.value}")
print(f"The value of 'some_attribute' attribute is: {my_instance.some_attribute}")
