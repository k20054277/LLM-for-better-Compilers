
class Parent:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)


class Child(Parent):
    def say_hello(self):
        print("Hello, " + self.name + "!)")


# Create an instance of the Parent class
parent = Parent("John")

# Call the say_hello method
parent.say_hello()

# Create an instance of the Child class
child = Child("Jane")

# Call the say_hello method
child.say_hello()

# Output:
# Hello, John
# Hello, Jane!
