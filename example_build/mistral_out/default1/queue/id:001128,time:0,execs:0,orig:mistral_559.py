
# Define a simple class named MyClass
class MyClass:
    def __init__(self, value=0):
        self.my_attribute = value

# Create an instance of MyClass
my_instance = MyClass(10)

# Using True to check if a condition is met
if True:  # This condition always evaluates to True, so the following code will always execute
    print("The value of True is:", True)

# Using hasattr to check if an instance has a specific attribute
if hasattr(my_instance, 'my_attribute'):  # Check if my_instance has an attribute named 'my_attribute'
    print("The instance has the attribute 'my_attribute'", my_instance.my_attribute)
else:
    print("The instance does not have the attribute 'my_attribute'")
