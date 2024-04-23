
# Define a class called Parent
class Parent:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)

# Define a class called Child that inherits from Parent
class Child(Parent):
    def say_hello(self):
        print("Hello, " + self.name + "!")

# Create an instance of the Child class
child = Child("John")

# Call the say_hello method on the child object
child.say_hello()

# Output: Hello, John!

# Check if the child object is a subclass of the Parent class
if isinstance(child, Parent):
    print("child is a subclass of Parent")

# Output: child is a subclass of Parent

# Check if the child object is False
if not child:
    print("child is False")

# Output: child is False
