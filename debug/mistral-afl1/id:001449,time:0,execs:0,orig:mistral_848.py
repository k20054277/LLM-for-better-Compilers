
# Define a simple class MyClass
class MyClass:
    def __init__(self, value):
        self.value = value

# Create an instance of MyClass
my_instance = MyClass(5)

# Check if the instance has an attribute 'other' and its value is greater than 10
# using 'and' and 'hasattr' combination
if not hasattr(my_instance, 'other') or my_instance.other > 10:
    print("Condition met")
else:
    print("Condition not met")

# Set a new attribute 'other' on the instance with a value less than 10
my_instance.other = 5

# Check if the instance has an attribute 'other' and its value is greater than 10
# using 'and' and 'hasattr' combination (this time, the condition should not be met)
if not hasattr(my_instance, 'other') or my_instance.other > 10:
    print("Condition met")  # This will never print since we set other to 5 previously
else:
    print("Condition not met")
