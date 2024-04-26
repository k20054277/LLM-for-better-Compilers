
# Define a parent class called Parent
class Parent:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)


# Define a subclass called Child that inherits from Parent
class Child(Parent):
    def say_hello(self):
        print("Hello, " + self.name + "!)")


# Create an instance of the Parent class
parent = Parent("John")

# Create an instance of the Child class
child = Child("Jane")

# Call the say_hello method on the parent and child instances
parent.say_hello()
child.say_hello()
