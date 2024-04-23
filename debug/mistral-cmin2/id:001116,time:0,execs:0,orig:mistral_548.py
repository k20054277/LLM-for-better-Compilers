
# Define a simple class with a few attributes
class SimpleClass:
    def __init__(self, num):
        self.num = num
        self.is_positive = True

# Create an instance of the class
my_instance = SimpleClass(5)

print("Is my_instance.is_positive true? ", my_instance.is_positive)
print()

# Use dir() to show the attributes and methods of my_instance
print("Attributes and methods of my_instance:")
print(dir(my_instance))
