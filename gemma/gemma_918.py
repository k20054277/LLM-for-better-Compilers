
class Parent:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    def say_hello(self):
        print("Hello, " + self.name + "!")

# Create an instance of the Child class
child = Child("John")

# Call the say_hello method
child.say_hello()

# Output:
# Hello, John!
